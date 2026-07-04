"""MCP Tool: australia_court_lookup.

PROVENANCE: CITED:01-court-hierarchy.md · CITED:21-tribunals-quasi-judicial.md
"""


def lookup_court(court_name: str = None, court_code: str = None, jurisdiction: str = None) -> dict:
    """Look up an Australian court by name, code, or jurisdiction filter.

    Delegates to court_agent.lookup_court.
    """
    from ..agents.court_agent import get_art_currency_warning
    from ..agents.court_agent import lookup_court as _lookup

    result = _lookup(
        court_name=court_name,
        court_code=court_code,
        jurisdiction=jurisdiction,
    )

    # Always include ART currency warning if ART is in results or queried directly
    if court_name and "ART" in court_name.upper() or (court_code and court_code.upper() == "ART"):
        result["art_currency_warning"] = get_art_currency_warning()
    elif jurisdiction and jurisdiction.lower() == "federal":
        result["art_currency_warning"] = get_art_currency_warning()

    return result
