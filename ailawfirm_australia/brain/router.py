"""Router — maps Intent → specialist agent for AI Brain Australia v0.1."""

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


def process(user_input: str):
    """Full pipeline: classify → route → return agent name."""
    from .classifier import classify

    intent = classify(user_input)
    agent = route(intent)
    return {"intent": intent.value, "agent": agent}
