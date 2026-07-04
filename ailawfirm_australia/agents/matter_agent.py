"""Matter agent — STUB for v0.1. Full implementation planned for v0.2.

PROVENANCE: CITED:18-life-of-solo-advocate-typical-day.md · CITED:30-firm-structure-options.md
"""


def handle_matter(query: str) -> dict:
    """Handle a matter-related query. STUB in v0.1."""
    return {
        "agent": "matter_agent",
        "status": "stub",
        "message": (
            "Matter management is a v0.2 priority feature. "
            "In v0.1, matter data is stored as local JSON under "
            "~/.ailawfirm-australia/matters/. Matter tracking, conflict "
            "checking, and dashboard are planned for v0.2."
        ),
        "query": query,
    }


def handle(payload: str) -> dict:
    """Matter agent entry point — delegating wrapper around ``handle_matter``.

    Adds the canonical ``"agent": "matter_agent"`` key (idempotently). For
    empty payloads, returns a structured stub response so the router can
    always produce a usable reply.
    """
    text = (payload or "").strip()
    if not text:
        return {
            "agent": "matter_agent",
            "ok": False,
            "error": "empty payload",
            "status": "stub",
        }
    result = handle_matter(text)
    if isinstance(result, dict) and "agent" not in result:
        result["agent"] = "matter_agent"
    return result
