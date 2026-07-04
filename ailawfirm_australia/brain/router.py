"""Router — maps Intent → specialist agent for AI Brain Australia v0.1."""

from __future__ import annotations

import importlib
from typing import Any, Dict

from .intents import Intent

# Agent dispatch table
AGENT_DISPATCH = {
    Intent.MATTER_UPDATE: "matter_agent",
    Intent.CITATION_LOOKUP: "citation_agent",
    Intent.COURT_QUERY: "court_agent",
    Intent.DRAFTING_NEED: "drafting_agent",
    Intent.DEADLINE_CHECK: "deadline_agent",
    Intent.CLIENT_COMM: "matter_agent",
    Intent.COMPLIANCE_FLAG: "compliance_agent",
    Intent.CALENDAR_QUERY: "calendar_agent",
    Intent.CALENDAR_ADD: "calendar_agent",
    Intent.UNKNOWN: "unknown",
}


def route(intent: Intent) -> str:
    """Return the agent name for a given intent."""
    return AGENT_DISPATCH.get(intent, "unknown")


def _invoke_agent(agent_name: str, payload: str) -> Dict[str, Any]:
    """Import the agent module and call handle(payload) on it.

    Returns a dict shaped like the agent's result, falling back to a
    structured error response when the agent can't be reached.
    """
    full_module = f"ailawfirm_australia.agents.{agent_name}"
    try:
        mod = importlib.import_module(full_module)
    except ImportError as exc:
        return {
            "ok": False,
            "intent": None,
            "agent": agent_name,
            "error": f"agent module import failed: {exc}",
        }

    handler = getattr(mod, "handle", None)
    if handler is None:
        return {
            "ok": False,
            "intent": None,
            "agent": agent_name,
            "error": f"agent module {full_module} has no handle() function",
        }

    try:
        result = handler(payload)
    except Exception as exc:  # noqa: BLE001 — surface any agent failure cleanly
        return {
            "ok": False,
            "intent": None,
            "agent": agent_name,
            "error": f"agent {agent_name}.handle() raised: {exc}",
        }

    if isinstance(result, dict) and "agent" not in result:
        result = {**result, "agent": agent_name}
    if not isinstance(result, dict):
        result = {"result": result, "agent": agent_name}
    return result


def process(user_input: str):
    """Full pipeline: classify → route → invoke agent → return response.

    Kept for backward compatibility with callers that already use ``process``.
    New code should use :func:`think` instead, which also wires in the AI-backed
    specialist answer when a host LLM is reachable.
    """
    from .classifier import classify

    intent = classify(user_input)
    agent = route(intent)
    if agent == "unknown":
        # No specific agent — return an empty-routed response without
        # invoking anything; ``process`` preserves the legacy contract that
        # ``think`` then layers the AI answer on top of.
        return {
            "ok": True,
            "intent": intent.value,
            "agent": agent,
            "result": {"message": "no specialist routed for this query"},
        }

    response = _invoke_agent(agent, user_input)
    response.setdefault("intent", intent.value)
    response.setdefault("agent", agent)
    response.setdefault("ok", True)
    return response


def think(text: str) -> Dict[str, Any]:
    """Classify, route, invoke agent, then attach AI-backed specialist answer.

    This is the user-facing brain entry point. The local engine's structured
    result is always returned deterministically; the AI-backed answer from
    ``specialists.answer()`` is layered on as ``response["answer"]`` only when
    a host LLM (e.g. Claude, GLM 5.2, Codex, AGY) is reachable via the ANTHROPIC_*
    environment. Offline-safe: specialists.answer() returns None when no key is
    present, so structured-mode tests still pass without any external service.
    """
    from .classifier import classify

    intent = classify(text)
    agent = route(intent)

    # 1. Structured engine result — deterministic, always present.
    if agent == "unknown":
        response: Dict[str, Any] = {
            "ok": True,
            "intent": intent.value,
            "agent": agent,
            "result": {"message": "no specialist routed for this query"},
        }
    else:
        response = _invoke_agent(agent, text)
        response.setdefault("intent", intent.value)
        response.setdefault("agent", agent)
        response.setdefault("ok", True)

    # 2. AI-backed specialist answer when a host LLM is available.
    #    Never raises out of think(); a provider outage just means we return
    #    the structured engine result unchanged.
    try:
        from ailawfirm_australia.brain import specialists

        grounding = response.get("result", {}) if isinstance(response, dict) else {}
        ai = specialists.answer(intent.value, text, grounding)
        if ai:
            response["answer"] = ai
    except Exception:
        pass

    return response
