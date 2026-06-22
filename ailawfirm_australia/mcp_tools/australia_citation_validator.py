"""MCP Tool: australia_citation_validator.

PROVENANCE: CITED:13-citation-format-primary.md · CITED:14-citation-format-secondary.md
"""


def validate_citation(citation: str) -> dict:
    """Validate and parse an AGLC4-format Australian legal citation.

    Delegates to citation_agent.validate_citation.
    """
    from ..agents.citation_agent import validate_citation as _validate

    return _validate(citation)
