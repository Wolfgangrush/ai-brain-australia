"""Citation agent — AGLC4 format parser and validator.

Handles medium-neutral and reported Australian legal citations.

PROVENANCE: CITED:13-citation-format-primary.md · CITED:14-citation-format-secondary.md
"""

import re

# AGLC4 medium-neutral citation: [YEAR] COURT NNN
# PROVENANCE: CITED:13-citation-format-primary.md
MEDIUM_NEUTRAL_PATTERN = re.compile(
    r"^\[(?P<year>\d{4})\]\s*(?P<court>[A-Za-z]+(?:\s+[A-Za-z]+)*)\s*(?P<number>\d+)$"
)

# AGLC4 reported citation: (YEAR) VOL REPORTER PAGE
# PROVENANCE: CITED:13-citation-format-primary.md
REPORTED_PATTERN = re.compile(
    r"^\((?P<year>\d{4})\)\s*(?P<volume>\d+)\s*(?P<reporter>[A-Za-z\.\s]+)\s*(?P<page>\d+)$"
)

# AGLC4 reported with square brackets (no volume): [YEAR] REPORTER PAGE
REPORTED_BRACKET_PATTERN = re.compile(
    r"^\[(?P<year>\d{4})\]\s*(?P<reporter>[A-Za-z\.\s]+)\s*(?P<page>\d+)$"
)

# Recognised Australian law reporters — PROVENANCE: CITED:13-citation-format-primary.md
RECOGNISED_REPORTERS = {
    "CLR": "Commonwealth Law Reports",
    "ALJR": "Australian Law Journal Reports",
    "ALR": "Australian Law Reports",
    "FCR": "Federal Court Reports",
    "FLR": "Federal Law Reports",
    "NSWLR": "New South Wales Law Reports",
    "VR": "Victorian Reports",
    "Qd R": "Queensland Reports",
    "SASR": "South Australian State Reports",
    "WAR": "Western Australian Reports",
    "Tas R": "Tasmanian Reports",
    "ACTR": "Australian Capital Territory Reports",
    "NTLR": "Northern Territory Law Reports",
    "A Crim R": "Australian Criminal Reports",
    "Fam LR": "Family Law Reports",
    "IPR": "Intellectual Property Reports",
}

# Recognised court identifiers for medium-neutral citations
RECOGNISED_COURTS = [
    "HCA",
    "FCAFC",
    "FCA",
    "FCFCOA",
    "FCCA",
    "NSWCA",
    "NSWSC",
    "NSWCCA",
    "NSWDC",
    "VSCA",
    "VSC",
    "QCA",
    "QSC",
    "WACA",
    "WASC",
    "SACA",
    "SASC",
    "TASCA",
    "TASSC",
    "ACTCA",
    "ACTSC",
    "NTCA",
    "NTSC",
]


def validate_citation(citation: str) -> dict:
    """Validate and parse an AGLC4-format Australian legal citation.

    PROVENANCE: CITED:13-citation-format-primary.md

    Returns parsed components, validity flag, and canonical form.

    Examples:
        >>> validate_citation("[2024] FCAFC 100")
        {"valid": True, "type": "medium-neutral", "year": 2024, "court": "FCAFC", ...}
        >>> validate_citation("(2023) 97 ALJR 100")
        {"valid": True, "type": "reported", "year": 2023, "volume": 97, ...}
    """
    citation = citation.strip()
    result = {
        "input": citation,
        "valid": False,
        "type": None,
        "canonical": None,
        "errors": [],
        "components": {},
    }

    # Try medium-neutral: [YEAR] COURT NNN
    mn_match = MEDIUM_NEUTRAL_PATTERN.match(citation)
    if mn_match:
        year = int(mn_match.group("year"))
        court = mn_match.group("court").strip()
        number = int(mn_match.group("number"))

        result["type"] = "medium-neutral"
        result["components"] = {
            "year": year,
            "court": court,
            "number": number,
        }

        if court.upper() in RECOGNISED_COURTS:
            result["valid"] = True
            result["canonical"] = f"[{year}] {court.upper()} {number}"
        else:
            result["errors"].append(
                f"Court identifier '{court}' not recognised. Known: {', '.join(RECOGNISED_COURTS)}"
            )

        return result

    # Try reported: (YEAR) VOL REPORTER PAGE
    rp_match = REPORTED_PATTERN.match(citation)
    if rp_match:
        year = int(rp_match.group("year"))
        volume = int(rp_match.group("volume"))
        reporter = rp_match.group("reporter").strip()
        page = int(rp_match.group("page"))

        result["type"] = "reported"
        result["components"] = {
            "year": year,
            "volume": volume,
            "reporter": reporter,
            "page": page,
        }

        # Check if reporter is recognised
        reporter_short = reporter.split()[0] if reporter.split() else reporter
        if reporter in RECOGNISED_REPORTERS or reporter_short in RECOGNISED_REPORTERS:
            result["valid"] = True
            result["canonical"] = f"({year}) {volume} {reporter} {page}"
        else:
            result["valid"] = True  # Still valid format even if reporter unknown
            result["canonical"] = f"({year}) {volume} {reporter} {page}"
            result["warnings"] = [
                f"Reporter '{reporter}' not in recognised list. Verify against AGLC4."
            ]

        return result

    # Try reported with square brackets: [YEAR] REPORTER PAGE
    rb_match = REPORTED_BRACKET_PATTERN.match(citation)
    if rb_match:
        year = int(rb_match.group("year"))
        reporter = rb_match.group("reporter").strip()
        page = int(rb_match.group("page"))

        result["type"] = "reported-bracket"
        result["components"] = {
            "year": year,
            "reporter": reporter,
            "page": page,
        }
        result["valid"] = True
        result["canonical"] = f"[{year}] {reporter} {page}"
        return result

    # Try party-name format: Party v Party [YYYY] COURT NNN or Party v Party [YYYY] RPTR PAGE
    # Simpler: just try to extract year/court from text containing square brackets
    bracket_extract = re.search(r"\[(\d{4})\]\s*([A-Za-z\.\s]+)\s*(\d+)", citation)
    if bracket_extract:
        year = int(bracket_extract.group(1))
        identifier = bracket_extract.group(2).strip()
        number = int(bracket_extract.group(3))

        # Determine if it's a court or reporter
        if identifier.upper() in RECOGNISED_COURTS:
            result["type"] = "medium-neutral"
            result["components"] = {"year": year, "court": identifier, "number": number}
            result["valid"] = True
            result["canonical"] = f"[{year}] {identifier.upper()} {number}"
            return result
        else:
            result["type"] = "reported-bracket"
            result["components"] = {"year": year, "reporter": identifier, "page": number}
            result["valid"] = True
            result["canonical"] = f"[{year}] {identifier} {number}"
            return result

    # Nothing matched
    result["errors"].append(
        "Could not parse citation. Expected formats: "
        "[YEAR] COURT NNN (medium-neutral) or (YEAR) VOL REPORTER PAGE (reported)"
    )
    return result


def handle(payload: str) -> dict:
    """Citation agent entry point — extract the first AGLC4-looking token and validate.

    Accepts a free-form payload, scans for the most AGLC4-shaped substring
    (medium-neutral `[YYYY] COURT NNN` or reported `(YYYY) VOL RPTR PAGE`),
    and routes it through ``validate_citation``. Always returns a dict
    containing ``"agent": "citation_agent"``.
    """
    import re

    text = (payload or "").strip()
    if not text:
        return {
            "agent": "citation_agent",
            "ok": False,
            "error": "empty payload",
            "result": None,
        }

    # Prefer medium-neutral or reported brackets; fall back to the first bracket cluster.
    candidates = re.findall(
        r"\[[0-9]{4}\]\s*[A-Za-z][A-Za-z\.\s]*?\s*\d+", text
    ) + re.findall(
        r"\([0-9]{4}\)\s*\d+\s*[A-Za-z\.\s]+?\s*\d+", text
    )
    citation = candidates[0].strip() if candidates else text
    validation = validate_citation(citation)
    return {
        "agent": "citation_agent",
        "ok": True,
        "action": "validate_citation",
        "result": validation,
    }
