"""Drafting agent — STUB for v0.1. Full implementation planned for v0.2.

PROVENANCE: CITED:18-life-of-solo-advocate-typical-day.md

Warning: AI-generated legal drafting must comply with:
- Law Council 2024 Joint Statement (human-in-the-loop)
- Dayal [2024] (practitioner liability for unreviewed AI output)
- LPUCSR Rule 9 (confidentiality — use local-only AI)
"""


def handle_drafting(query: str) -> dict:
    """Handle a drafting-related query. STUB in v0.1."""
    return {
        "agent": "drafting_agent",
        "status": "stub",
        "message": (
            "Legal drafting is a v0.2 priority feature. "
            "In v0.1, the drafting agent returns this placeholder. "
            "v0.2 will include drafting templates for common documents "
            "(statement of claim, defence, notice of appeal, affidavit, "
            "contract, deed). All AI-generated drafts require human review "
            "per the Law Council 2024 Joint Statement and Dayal [2024]."
        ),
        "compliance_note": (
            "WARNING: Do NOT enter client-confidential information into "
            "cloud AI for drafting. Use local-only Ollama mode. "
            "LPUCSR Rule 9 applies."
        ),
        "query": query,
    }


def handle(payload: str) -> dict:
    """Drafting agent entry point — delegating wrapper around ``handle_drafting``.

    Adds the canonical ``"agent": "drafting_agent"`` key (idempotently) so
    the router contract is satisfied even if the underlying stub changes.
    """
    text = (payload or "").strip()
    if not text:
        return {
            "agent": "drafting_agent",
            "ok": False,
            "error": "empty payload",
            "status": "stub",
            "compliance_note": (
                "WARNING: Do NOT enter client-confidential information into "
                "cloud AI for drafting. Use local-only Ollama mode. "
                "LPUCSR Rule 9 applies."
            ),
        }
    result = handle_drafting(text)
    if isinstance(result, dict) and "agent" not in result:
        result["agent"] = "drafting_agent"
    return result
