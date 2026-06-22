"""Deadline agent — STUB for v0.1. Full implementation planned for v0.2.

PROVENANCE: CITED:09-statute-limitation-act.md

Limitation periods vary by state and cause of action:
- NSW: Limitation Act 1969
- VIC: Limitation of Actions Act 1958
- QLD: Limitation of Actions Act 1974
- WA: Limitation Act 1935 (amended 2005)
- SA: Limitation of Actions Act 1936
- TAS: Limitation Act 1974
- ACT: Limitation Act 1985
- NT: Limitation Act 1981

v0.2 will encode limitation periods for common cause-of-action types
(contract, tort, personal injury, defamation, etc.) per jurisdiction.
"""

LIMITATION_NOTE = (
    "Limitation periods vary by state and cause of action. "
    "Common periods: 6 years (contract, tort in most states), "
    "3 years (personal injury in most states), "
    "1 year (defamation in most states). "
    "Always verify the applicable limitation period against the "
    "relevant state statute and the AS-OF date in KNOWLEDGE_PROVENANCE.md. "
    "PROVENANCE: CITED:09-statute-limitation-act.md · AS-OF: 2026-05-18"
)


def handle_deadline(query: str) -> dict:
    """Handle a deadline/limitation query. STUB in v0.1."""
    return {
        "agent": "deadline_agent",
        "status": "stub",
        "message": (
            "Limitation period tracking is a v0.2 priority feature. "
            "In v0.1, the deadline agent returns this placeholder with "
            "general limitation guidance. "
            "v0.2 will encode state-specific limitation periods for "
            "common cause-of-action types and provide automated deadline "
            "calculations with calendar integration."
        ),
        "limitation_note": LIMITATION_NOTE,
        "query": query,
    }
