"""Australian legal ontology — courts, statutes, bar rules, matter types, jurisdictions.

Every enum entry carries PROVENANCE: CITED:<research-file> from _research/.
AS-OF: 2026-05-18 unless otherwise noted.
"""

from enum import Enum


class AustralianCourt(Enum):
    """Federal and state courts of Australia. ART replaces AAT (Oct 2024 transition)."""

    # Federal — PROVENANCE: CITED:01-court-hierarchy.md
    HCA = ("High Court of Australia", "federal", "appellate")
    FCA = ("Federal Court of Australia", "federal", "superior")
    FCAFC = ("Full Court of the Federal Court of Australia", "federal", "appellate")
    FCFCOA = ("Federal Circuit and Family Court of Australia", "federal", "trial")
    # PROVENANCE: CITED:21-tribunals-quasi-judicial.md — CURRENCY: ART operative Oct 2024
    ART = ("Administrative Review Tribunal", "federal", "tribunal")

    # NSW — PROVENANCE: CITED:01-court-hierarchy.md
    NSWSC = ("Supreme Court of New South Wales", "NSW", "superior")
    NSWCA = ("New South Wales Court of Appeal", "NSW", "appellate")
    NSWDC = ("District Court of New South Wales", "NSW", "district")
    NSWLC = ("Local Court of New South Wales", "NSW", "local")

    # VIC — PROVENANCE: CITED:01-court-hierarchy.md
    VSC = ("Supreme Court of Victoria", "VIC", "superior")
    VSCA = ("Victorian Court of Appeal", "VIC", "appellate")
    VCC = ("County Court of Victoria", "VIC", "county")
    VMC = ("Magistrates Court of Victoria", "VIC", "local")

    # QLD — PROVENANCE: CITED:01-court-hierarchy.md
    QSC = ("Supreme Court of Queensland", "QLD", "superior")
    QCA = ("Queensland Court of Appeal", "QLD", "appellate")
    QDC = ("District Court of Queensland", "QLD", "district")
    QMC = ("Magistrates Court of Queensland", "QLD", "local")

    # WA — PROVENANCE: CITED:01-court-hierarchy.md
    WASC = ("Supreme Court of Western Australia", "WA", "superior")
    WACA = ("Western Australian Court of Appeal", "WA", "appellate")
    WADC = ("District Court of Western Australia", "WA", "district")
    WAMC = ("Magistrates Court of Western Australia", "WA", "local")

    # SA — PROVENANCE: CITED:01-court-hierarchy.md
    SASC = ("Supreme Court of South Australia", "SA", "superior")
    SACA = ("South Australian Court of Appeal", "SA", "appellate")
    SADC = ("District Court of South Australia", "SA", "district")
    SAMC = ("Magistrates Court of South Australia", "SA", "local")

    # TAS — PROVENANCE: CITED:01-court-hierarchy.md
    TASSC = ("Supreme Court of Tasmania", "TAS", "superior")
    TASCA = ("Tasmanian Court of Criminal Appeal", "TAS", "appellate")
    TASMC = ("Magistrates Court of Tasmania", "TAS", "local")

    # ACT — PROVENANCE: CITED:01-court-hierarchy.md
    ACTSC = ("Supreme Court of the Australian Capital Territory", "ACT", "superior")
    ACTCA = ("ACT Court of Appeal", "ACT", "appellate")
    ACTMC = ("Magistrates Court of the Australian Capital Territory", "ACT", "local")

    # NT — PROVENANCE: CITED:01-court-hierarchy.md
    NTSC = ("Supreme Court of the Northern Territory", "NT", "superior")
    NTCA = ("Northern Territory Court of Appeal", "NT", "appellate")
    NTLC = ("Local Court of the Northern Territory", "NT", "local")

    def __init__(self, display_name, jurisdiction, level):
        self.display_name = display_name
        self.jurisdiction = jurisdiction
        self.level = level


class AustralianStatute(Enum):
    """Key Australian statutes relevant to legal practice. PROVENANCE: CITED:04 through 09."""

    # Commonwealth — PROVENANCE: CITED:04-statute-data-protection.md
    PRIVACY_ACT_1988 = ("Privacy Act 1988 (Cth)", "federal", "data-protection")
    # PROVENANCE: CITED:24-data-localization-requirements.md
    MY_HEALTH_RECORDS_ACT_2012 = ("My Health Records Act 2012 (Cth)", "federal", "health")
    # PROVENANCE: CITED:25-cross-border-data-transfer.md
    APP_8 = (
        "Australian Privacy Principle 8 — Cross-border disclosure",
        "federal",
        "data-protection",
    )
    # PROVENANCE: CITED:06-statute-company-law-overview.md
    CORPORATIONS_ACT_2001 = ("Corporations Act 2001 (Cth)", "federal", "company")
    # PROVENANCE: CITED:05-statute-contract-law-overview.md
    ACL = ("Australian Consumer Law (Schedule 2 CCA)", "federal", "consumer")
    # PROVENANCE: CITED:07-statute-criminal-code.md
    CRIMES_ACT_1914 = ("Crimes Act 1914 (Cth)", "federal", "criminal")
    CRIMINAL_CODE_1995 = ("Criminal Code Act 1995 (Cth)", "federal", "criminal")
    # PROVENANCE: CITED:08-statute-evidence-act.md
    EVIDENCE_ACT_1995 = ("Evidence Act 1995 (Cth)", "federal", "evidence")
    # PROVENANCE: CITED:09-statute-limitation-act.md
    LIMITATION_ACTS = ("Limitation Acts (state-based, varies)", "state", "procedure")
    # PROVENANCE: CITED:27-anti-money-laundering-obligations.md
    AML_CTF_ACT_2006 = (
        "Anti-Money Laundering and Counter-Terrorism Financing Act 2006",
        "federal",
        "compliance",
    )
    AML_CTF_AMENDMENT_2024 = ("AML/CTF Amendment Act 2024 (Tranche 2)", "federal", "compliance")

    def __init__(self, display_name, jurisdiction, category):
        self.display_name = display_name
        self.jurisdiction = jurisdiction
        self.category = category


class AustralianBarRule(Enum):
    """Professional conduct rules — LPUL + LPUCSR + LPUBR. PROVENANCE: CITED:10/11/12."""

    # PROVENANCE: CITED:12-bar-rule-confidentiality.md
    LPUCSR_R9_CONFIDENTIALITY = ("LPUCSR Rule 9 — Confidentiality", "LPUCSR", "confidentiality")
    # PROVENANCE: CITED:11-bar-rule-conflict-of-interest.md
    LPUCSR_R10_CONFLICT_FORMER = (
        "LPUCSR Rule 10 — Conflicts (former clients)",
        "LPUCSR",
        "conflict",
    )
    LPUCSR_R11_CONFLICT_CURRENT = (
        "LPUCSR Rule 11 — Conflicts (current clients)",
        "LPUCSR",
        "conflict",
    )
    # PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md
    LPUCSR_R36_PUBLICITY = ("LPUCSR Rule 36 — Publicity and solicitation", "LPUCSR", "publicity")

    def __init__(self, display_name, rule_set, category):
        self.display_name = display_name
        self.rule_set = rule_set
        self.category = category


class MatterType(Enum):
    """Australian legal matter types. PROVENANCE: CITED:18-life-of-solo-advocate-typical-day.md"""

    CIVIL_COMMERCIAL = "civil-commercial"
    FAMILY = "family"
    CRIMINAL = "criminal"
    EMPLOYMENT = "employment"
    IP = "intellectual-property"
    PROPERTY_CONVEYANCING = "property-conveyancing"
    MIGRATION = "migration"
    ADMINISTRATIVE_REVIEW = "administrative-review"
    ARBITRATION = "arbitration"


class Jurisdiction(Enum):
    """Australian jurisdictions. PROVENANCE: CITED:01-court-hierarchy.md"""

    FEDERAL = "federal"
    NSW = "NSW"
    VIC = "VIC"
    QLD = "QLD"
    WA = "WA"
    SA = "SA"
    TAS = "TAS"
    ACT = "ACT"
    NT = "NT"
