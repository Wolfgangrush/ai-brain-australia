"""Rule-based keyword classifier for AI Brain Australia v0.1.

No LLM dependency in v0.1. LLM gateway added in v0.2.
"""

from .intents import Intent

KEYWORDS = {
    Intent.CITATION_LOOKUP: [
        "cite",
        "citation",
        "aglc",
        "AGLC4",
        "neutral citation",
        "CLR",
        "ALJR",
        "ALR",
        "FCR",
        "NSWLR",
        "VR",
        "HCA",
        "FCAFC",
        "FCA",
        "NSWCA",
        "NSWSC",
        "VSC",
        "QSC",
        "reported",
    ],
    Intent.COURT_QUERY: [
        "court",
        "federal court",
        "supreme court",
        "district court",
        "magistrates court",
        "high court",
        "HCA",
        "tribunal",
        "ART",
        "AAT",
        "FCFCOA",
        "jurisdiction",
        "e-filing",
        "registry",
        "eLodgment",
        "online registry",
    ],
    Intent.CALENDAR_ADD: [
        "schedule",
        "add event",
        "calendar",
        "hearing date",
        "mention",
        "directions hearing",
        "set down",
        "listing",
        "ICS",
        "sync",
        "appointment",
    ],
    Intent.CALENDAR_QUERY: [
        "what's on",
        "upcoming",
        "this week",
        "tomorrow",
        "calendar view",
        "my schedule",
        "next hearing",
    ],
    Intent.COMPLIANCE_FLAG: [
        "confidential",
        "privacy",
        "data breach",
        "APP 8",
        "cross-border",
        "overseas",
        "My Health Record",
        "Section 77",
        "AML",
        "Tranche 2",
        "rule 9",
        "rule 36",
        "LPUCSR",
        "LPUBR",
        "legal privilege",
        "privilege",
        "AI review",
        "human review",
        "Dayal",
    ],
    Intent.MATTER_UPDATE: [
        "matter",
        "case",
        "client",
        "file note",
        "update",
        "status",
        "brief",
        "instructions",
    ],
    Intent.DRAFTING_NEED: [
        "draft",
        "pleading",
        "affidavit",
        "submission",
        "contract",
        "deed",
        "statement of claim",
        "defence",
        "notice",
        "originating",
        "application",
    ],
    Intent.DEADLINE_CHECK: [
        "deadline",
        "limitation period",
        "limitation act",
        "due date",
        "filing date",
        "expiry",
        "statute of limitations",
        "time limit",
        "limitations act",
    ],
    Intent.CLIENT_COMM: [
        "client comm",
        "email client",
        "letter to client",
        "advise client",
        "update client",
        "reply",
    ],
}


def classify(text: str) -> Intent:
    """Classify input text into one of 10 intents using keyword matching."""
    text_lower = text.lower()
    scores = {intent: 0 for intent in Intent}
    # UNKNOWN starts with a small negative bias so keyword matches override it
    scores[Intent.UNKNOWN] = -1

    for intent, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                scores[intent] += 1

    best = max(scores, key=scores.get)
    if scores[best] <= 0:
        return Intent.UNKNOWN
    return best
