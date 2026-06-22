"""Compliance agent — LPUL Rule 9 · APP 8 · Section 77 · Tranche 2 AML · Dayal [2024].

PROVENANCE: CITED:12-bar-rule-confidentiality.md · CITED:25-cross-border-data-transfer.md
            CITED:24-data-localization-requirements.md · CITED:27-anti-money-laundering-obligations.md
            CITED:23-ai-law-firm-regulatory-stance.md · CITED:10-bar-rule-publicity-solicitation.md
"""

from dataclasses import dataclass, field
from enum import Enum


class ComplianceRiskLevel(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ComplianceCategory(Enum):
    # PROVENANCE: CITED:12-bar-rule-confidentiality.md
    LPUL_R9_CONFIDENTIALITY = "lpul-r9-confidentiality"
    # PROVENANCE: CITED:25-cross-border-data-transfer.md
    APP_8_CROSS_BORDER = "app-8-cross-border"
    # PROVENANCE: CITED:24-data-localization-requirements.md
    S77_MY_HEALTH_RECORDS = "s77-my-health-records"
    # PROVENANCE: CITED:27-anti-money-laundering-obligations.md
    AML_TRANCHE_2 = "aml-tranche-2"
    # PROVENANCE: CITED:23-ai-law-firm-regulatory-stance.md
    AI_OUTPUT_HUMAN_REVIEW = "ai-output-human-review"
    # PROVENANCE: CITED:23-ai-law-firm-regulatory-stance.md
    DAYAL_2024_LIABILITY = "dayal-2024-liability"
    # PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md
    LPUL_R36_PUBLICITY = "lpul-r36-publicity"


@dataclass
class ComplianceFlag:
    category: ComplianceCategory
    risk_level: ComplianceRiskLevel
    message: str
    guidance: str


@dataclass
class ComplianceResult:
    flags: list[ComplianceFlag] = field(default_factory=list)
    has_critical: bool = False
    has_high: bool = False

    @property
    def all_clear(self) -> bool:
        return len(self.flags) == 0


def check_compliance(text: str) -> ComplianceResult:
    """Scan input text for compliance risks.

    PROVENANCE: CITED:12-bar-rule-confidentiality.md (LPUL Rule 9)
              CITED:25-cross-border-data-transfer.md (APP 8)
              CITED:24-data-localization-requirements.md (Section 77)
              CITED:27-anti-money-laundering-obligations.md (Tranche 2 AML)
              CITED:23-ai-law-firm-regulatory-stance.md (Dayal [2024] + Law Council 2024)
              CITED:10-bar-rule-publicity-solicitation.md (LPUL Rule 36)
    """
    result = ComplianceResult()
    text_lower = text.lower()

    # Rule 9 Confidentiality — detect potential breach scenarios
    # PROVENANCE: CITED:12-bar-rule-confidentiality.md
    cloud_keywords = [
        "chatgpt",
        "gpt",
        "bard",
        "gemini",
        "copilot",
        "cloud ai",
        "openai",
        "upload",
        "paste into",
    ]
    rule9_triggers = [kw for kw in cloud_keywords if kw in text_lower]
    if rule9_triggers and any(c in text_lower for c in ["client", "matter", "case"]):
        result.flags.append(
            ComplianceFlag(
                category=ComplianceCategory.LPUL_R9_CONFIDENTIALITY,
                risk_level=ComplianceRiskLevel.CRITICAL,
                message=f"LPUL Rule 9 risk: detected potential cloud AI use ({', '.join(rule9_triggers)}) with client data",
                guidance=(
                    "LPUCSR Rule 9 requires maintaining client confidentiality. "
                    "Uploading client material to cloud AI services may breach Rule 9. "
                    "Use local-only Ollama mode for client work. See MODEL_SETUP.md."
                ),
            )
        )
        result.has_critical = True

    # APP 8 Cross-border deemed liability
    # PROVENANCE: CITED:25-cross-border-data-transfer.md
    if any(kw in text_lower for kw in ["cross-border", "overseas", "offshore", "foreign server"]):
        if any(c in text_lower for c in ["personal info", "client data", "pi", "disclose"]):
            result.flags.append(
                ComplianceFlag(
                    category=ComplianceCategory.APP_8_CROSS_BORDER,
                    risk_level=ComplianceRiskLevel.HIGH,
                    message=(
                        "APP 8 cross-border deemed liability: "
                        "disclosing personal information to overseas recipients "
                        "makes the disclosing entity liable for overseas breaches"
                    ),
                    guidance=(
                        "APP 8 of the Privacy Act 1988 creates deemed liability for overseas "
                        "data breaches. Use local-only AI or ensure contractual protections "
                        "with overseas vendors. See NO_PII_NO_DATA.md §APP 8."
                    ),
                )
            )
            result.has_high = True

    # Section 77 My Health Records Act — health data localisation
    # PROVENANCE: CITED:24-data-localization-requirements.md
    health_keywords = [
        "health record",
        "my health record",
        "medical record",
        "medical records",
        "patient data",
        "health data",
        "clinical",
        "diagnosis",
        "medicare",
        "mbs",
        "pbs",
    ]
    if any(kw in text_lower for kw in health_keywords):
        if any(kw in text_lower for kw in ["overseas", "offshore", "cloud", "api", "upload"]):
            result.flags.append(
                ComplianceFlag(
                    category=ComplianceCategory.S77_MY_HEALTH_RECORDS,
                    risk_level=ComplianceRiskLevel.CRITICAL,
                    message=(
                        "Section 77 My Health Records Act: strict prohibition on handling "
                        "health data outside Australia"
                    ),
                    guidance=(
                        "Section 77 My Health Records Act 2012 strictly prohibits offshore "
                        "handling of My Health Record data. APP framework alone is insufficient. "
                        "Use local-only AI for ALL health-related data. No cloud AI under any "
                        "circumstances."
                    ),
                )
            )
            result.has_critical = True
        else:
            result.flags.append(
                ComplianceFlag(
                    category=ComplianceCategory.S77_MY_HEALTH_RECORDS,
                    risk_level=ComplianceRiskLevel.HIGH,
                    message="Health data detected — Section 77 My Health Records Act localisation applies",
                    guidance=(
                        "Section 77 My Health Records Act 2012 prohibits offshore handling. "
                        "Use local-only AI (Ollama). Do NOT use cloud AI for health-related PI."
                    ),
                )
            )
            result.has_high = True

    # Tranche 2 AML — advance warning (effective July 2026)
    # PROVENANCE: CITED:27-anti-money-laundering-obligations.md — CURRENCY: July 2026
    aml_keywords = [
        "aml",
        "anti-money laundering",
        "kyc",
        "know your client",
        "suspicious matter",
        "cash transaction",
        "reportable",
        "money laundering",
        "terrorism financing",
        "ctf",
    ]
    if any(kw in text_lower for kw in aml_keywords):
        result.flags.append(
            ComplianceFlag(
                category=ComplianceCategory.AML_TRANCHE_2,
                risk_level=ComplianceRiskLevel.HIGH,
                message=(
                    "Tranche 2 AML/CTF: lawyers brought into reporting net "
                    "effective July 2026 — advance obligation warning"
                ),
                guidance=(
                    "The AML/CTF Amendment Act 2024 (Tranche 2) brings Australian lawyers "
                    "into the AML/CTF reporting net from July 2026. This will impose KYC, "
                    "customer due diligence, and suspicious matter reporting obligations. "
                    "Prepare compliance systems now. Automated Tranche 2 reporting module "
                    "planned for v0.2. CITED:27-anti-money-laundering-obligations.md."
                ),
            )
        )
        result.has_high = True

    # AI output without human review
    # PROVENANCE: CITED:23-ai-law-firm-regulatory-stance.md (Dayal [2024] + Law Council 2024)
    ai_review_keywords = [
        "ai draft",
        "ai generated",
        "auto draft",
        "automatic",
        "without review",
        "no review",
        "unreviewed",
        "ai output",
    ]
    if any(kw in text_lower for kw in ai_review_keywords):
        result.flags.append(
            ComplianceFlag(
                category=ComplianceCategory.AI_OUTPUT_HUMAN_REVIEW,
                risk_level=ComplianceRiskLevel.HIGH,
                message=(
                    "Law Council 2024 Joint Statement: human-in-the-loop required "
                    "for all AI-assisted legal work. Dayal [2024] establishes practitioner "
                    "liability for unreviewed AI outputs."
                ),
                guidance=(
                    "The Law Council of Australia's 2024 Joint Statement on AI in Legal "
                    "Practice requires human review of all AI-generated legal content. "
                    "The Dayal [2024] precedent establishes that practitioners are "
                    "personally liable for AI hallucinations relied upon without review. "
                    "Every AI-generated output must carry a 'draft for counsel review' caption."
                ),
            )
        )
        result.has_high = True

    # LPUL Rule 36 publicity/solicitation
    # PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md
    r36_keywords = [
        "guaranteed win",
        "guaranteed outcome",
        "guaranteed result",
        "specialist in",
        "expert in",
        "best lawyer",
        "top lawyer",
        "no win no fee query",
        "ambulance chaser",
    ]
    if any(kw in text_lower for kw in r36_keywords):
        result.flags.append(
            ComplianceFlag(
                category=ComplianceCategory.LPUL_R36_PUBLICITY,
                risk_level=ComplianceRiskLevel.MEDIUM,
                message=(
                    "LPUCSR Rule 36: potential publicity/solicitation boundary issue detected"
                ),
                guidance=(
                    "LPUCSR Rule 36 governs publicity and solicitation by solicitors. "
                    "Avoid claims of guaranteed outcomes, specialist/expert status "
                    "(unless accredited), or comparisons with other practitioners."
                ),
            )
        )

    return result
