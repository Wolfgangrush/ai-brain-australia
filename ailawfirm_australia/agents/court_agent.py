"""Court agent — Australian Federal + State court lookup stubs.

PROVENANCE: CITED:01-court-hierarchy.md · CITED:21-tribunals-quasi-judicial.md
           CITED:16-e-filing-system.md
"""

# PROVENANCE: CITED:01-court-hierarchy.md + CITED:16-e-filing-system.md
COURT_DATABASE = {
    "HCA": {
        "name": "High Court of Australia",
        "level": "appellate",
        "jurisdiction": "federal",
        "e_filing_portal": "https://www.hcourt.gov.au/filing",
        "website": "https://www.hcourt.gov.au",
        "address": "Parkes Place, Canberra ACT 2600",
        "contact": "+61 2 6270 6861",
        "description": (
            "The highest court in the Australian judicial system. "
            "Hears appeals by special leave on matters of public importance "
            "and constitutional questions under s 75-76 of the Constitution."
        ),
    },
    "FCA": {
        "name": "Federal Court of Australia",
        "level": "superior",
        "jurisdiction": "federal",
        "e_filing_portal": "https://www.fedcourt.gov.au/online-services/elodgment",
        "website": "https://www.fedcourt.gov.au",
        "address": "Registries in all state capitals",
        "contact": "+61 2 8099 8000 (Sydney)",
        "description": (
            "Original and appellate jurisdiction in federal matters including "
            "commercial, corporations, tax, industrial, native title, ADM, IP, "
            "and human rights."
        ),
    },
    "FCAFC": {
        "name": "Full Court of the Federal Court of Australia",
        "level": "appellate",
        "jurisdiction": "federal",
        "e_filing_portal": "https://www.fedcourt.gov.au/online-services/elodgment",
        "website": "https://www.fedcourt.gov.au",
        "address": "Registries in all state capitals",
        "description": "Appellate division of the Federal Court (3+ judges).",
    },
    "FCFCOA": {
        "name": "Federal Circuit and Family Court of Australia",
        "level": "trial",
        "jurisdiction": "federal",
        "e_filing_portal": "https://www.fcfcoa.gov.au/efiling",
        "website": "https://www.fcfcoa.gov.au",
        "address": "Registries in all state capitals",
        "description": "Family law and general federal law matters (Division 1 and Division 2).",
    },
    # CURRENCY: ART operative October 2024 — PROVENANCE: CITED:21-tribunals-quasi-judicial.md
    "ART": {
        "name": "Administrative Review Tribunal",
        "level": "tribunal",
        "jurisdiction": "federal",
        "e_filing_portal": "https://www.art.gov.au/lodge",
        "website": "https://www.art.gov.au",
        "address": "Registries in all state capitals",
        "description": (
            "The Administrative Review Tribunal (ART) replaced the AAT in October 2024. "
            "Conducts independent merits review of administrative decisions made under "
            "Commonwealth laws. The most significant change in federal administrative "
            "law in decades."
        ),
        "currency_note": "Replaced AAT — October 2024 transition. PROVENANCE: CITED:21-tribunals-quasi-judicial.md",
    },
    # State Supreme Courts — PROVENANCE: CITED:01-court-hierarchy.md
    "NSWSC": {
        "name": "Supreme Court of New South Wales",
        "level": "superior",
        "jurisdiction": "NSW",
        "e_filing_portal": "https://onlineregistry.lawlink.nsw.gov.au",
        "website": "https://www.supremecourt.justice.nsw.gov.au",
        "address": "184 Phillip Street, Sydney NSW 2000",
    },
    "NSWCA": {
        "name": "New South Wales Court of Appeal",
        "level": "appellate",
        "jurisdiction": "NSW",
        "website": "https://www.supremecourt.justice.nsw.gov.au",
    },
    "NSWDC": {
        "name": "District Court of New South Wales",
        "level": "district",
        "jurisdiction": "NSW",
        "e_filing_portal": "https://onlineregistry.lawlink.nsw.gov.au",
        "website": "https://www.districtcourt.justice.nsw.gov.au",
    },
    "NSWLC": {
        "name": "Local Court of New South Wales",
        "level": "local",
        "jurisdiction": "NSW",
        "website": "https://www.localcourt.justice.nsw.gov.au",
    },
    "VSC": {
        "name": "Supreme Court of Victoria",
        "level": "superior",
        "jurisdiction": "VIC",
        "e_filing_portal": "https://www.supremecourt.vic.gov.au/filing",
        "website": "https://www.supremecourt.vic.gov.au",
        "address": "210 William Street, Melbourne VIC 3000",
    },
    "VSCA": {
        "name": "Victorian Court of Appeal",
        "level": "appellate",
        "jurisdiction": "VIC",
        "website": "https://www.supremecourt.vic.gov.au",
    },
    "VCC": {
        "name": "County Court of Victoria",
        "level": "county",
        "jurisdiction": "VIC",
        "website": "https://www.countycourt.vic.gov.au",
    },
    "VMC": {
        "name": "Magistrates Court of Victoria",
        "level": "local",
        "jurisdiction": "VIC",
        "website": "https://www.mcv.vic.gov.au",
    },
    "QSC": {
        "name": "Supreme Court of Queensland",
        "level": "superior",
        "jurisdiction": "QLD",
        "website": "https://www.courts.qld.gov.au/courts/supreme-court",
        "address": "415 George Street, Brisbane QLD 4000",
    },
    "QDC": {
        "name": "District Court of Queensland",
        "level": "district",
        "jurisdiction": "QLD",
        "website": "https://www.courts.qld.gov.au/courts/district-court",
    },
    "WASC": {
        "name": "Supreme Court of Western Australia",
        "level": "superior",
        "jurisdiction": "WA",
        "website": "https://www.supremecourt.wa.gov.au",
    },
    "SASC": {
        "name": "Supreme Court of South Australia",
        "level": "superior",
        "jurisdiction": "SA",
        "website": "https://www.courts.sa.gov.au",
    },
    "TASSC": {
        "name": "Supreme Court of Tasmania",
        "level": "superior",
        "jurisdiction": "TAS",
        "website": "https://www.supremecourt.tas.gov.au",
    },
    "ACTSC": {
        "name": "Supreme Court of the ACT",
        "level": "superior",
        "jurisdiction": "ACT",
        "website": "https://www.courts.act.gov.au/supreme",
    },
    "NTSC": {
        "name": "Supreme Court of the Northern Territory",
        "level": "superior",
        "jurisdiction": "NT",
        "website": "https://localcourt.nt.gov.au",
    },
}


def lookup_court(court_name: str = None, court_code: str = None, jurisdiction: str = None) -> dict:
    """Look up Australian court details by name, code, or jurisdiction filter.

    PROVENANCE: CITED:01-court-hierarchy.md · CITED:16-e-filing-system.md
    CITED:21-tribunals-quasi-judicial.md (ART — post-Oct 2024)
    """
    results = []

    for code, info in COURT_DATABASE.items():
        match = False
        if court_code and court_code.upper() == code:
            match = True
        elif court_name and court_name.lower() in info["name"].lower():
            match = True
        elif jurisdiction and info["jurisdiction"].upper() == jurisdiction.upper():
            match = True
        elif not court_name and not court_code and not jurisdiction:
            match = True

        if match:
            entry = {"code": code, **info}
            results.append(entry)

    return {
        "query": {"court_name": court_name, "court_code": court_code, "jurisdiction": jurisdiction},
        "count": len(results),
        "results": results,
    }


def get_art_currency_warning() -> dict:
    """Return ART transition currency warning.

    PROVENANCE: CITED:21-tribunals-quasi-judicial.md
    CURRENCY: October 2024 transition from AAT to ART.
    """
    return {
        "warning": (
            "The AAT was abolished and replaced by the ART (Administrative Review Tribunal) "
            "in October 2024. All references to the AAT should now reference the ART. "
            "Verify any AAT-era case citations for transfer status to the ART."
        ),
        "transition_date": "October 2024",
        "provenance": "CITED:21-tribunals-quasi-judicial.md",
    }
