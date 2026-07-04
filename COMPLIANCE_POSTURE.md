# COMPLIANCE POSTURE — AI Brain · Australia · v0.1

**Australian AI-Use Doctrine encoded. "Assistive infrastructure, not decision-maker."**

AS-OF: 2026-05-19. Verbatim sourced from public regulatory guidance, case-law, and professional conduct rules.

---

## 1. Foundational Posture

AI Brain — Australia is positioned as **assistive infrastructure for qualified legal professionals**, not as a decision-maker. Every AI-generated output requires human review by counsel admitted in the relevant Australian jurisdiction before any client-facing or court-facing use. This posture aligns with every Australian regulatory source discovered during research.

---

## 2. Law Council of Australia — 2024 Joint Statement on AI in Legal Practice

**Source:** Law Council of Australia, media release on risks and opportunities of generative AI (2024).
**PROVENANCE: CITED:23-ai-law-firm-regulatory-stance.md**

The Law Council's position:
- Prefers "mandatory guardrails" for high-risk AI applications over a general AI Act.
- Human-in-the-loop is the central regulatory requirement.
- AI use does NOT diminish practitioner competence obligations.
- Confidentiality obligations (LPUCSR Rule 9) extend to AI tool usage — client data must not be input into unsecured/public AI systems.

**Encoded in:** `compliance_agent.py` → `AI_OUTPUT_HUMAN_REVIEW` flag.

---

## 3. Dayal [2024] FedCFamC2F 1166 — Practitioner Liability for AI Hallucinations

**Source:** *Dayal v State of New South Wales* [2024] FedCFamC2F 1166.
**PROVENANCE: CITED:23-ai-law-firm-regulatory-stance.md**

Verbatim holding:
> "The duty of a legal practitioner to the court is paramount... the use of artificial intelligence technology does not alleviate a practitioner's obligation to ensure that the authorities they cite are accurate and relevant."

Practical consequence: A solicitor who files AI-generated submissions containing hallucinated case citations is personally liable for professional misconduct. The tool's `citation_agent` validates AGLC4 format; substantive accuracy verification remains the practitioner's obligation.

**Encoded in:** `compliance_agent.py` → `DAYAL_2024_LIABILITY` flag. README §5 "Privacy posture" and DISCLAIMER.md §"Output liability."

---

## 4. LPUCSR Rule 9 — Confidentiality

**Source:** Legal Profession Uniform Conduct (Solicitors) Rules 2015, Rule 9.
**PROVENANCE: CITED:12-bar-rule-confidentiality.md**

Verbatim:
> "A solicitor must not disclose any information which is confidential to a client and acquired by the solicitor during the client's engagement..."

The duty continues after the engagement ends. Cloud AI use that uploads client data to offshore servers engages Rule 9 risk. The tool's local-only default (Ollama + Qwen3) is architecturally designed to support Rule 9 compliance.

**Encoded in:** `compliance_agent.py` → `LPUL_R9_CONFIDENTIALITY` flag. MODEL_SETUP.md → "Option A — Ollama + Qwen3" recommended for client work.

---

## 5. APP 8 — Cross-Border Disclosure Deemed Liability

**Source:** Privacy Act 1988 (Cth), Australian Privacy Principle 8.
**PROVENANCE: CITED:25-cross-border-data-transfer.md**

Verbatim:
> "Before an APP entity discloses personal information about an individual to an overseas recipient, the entity must take such steps as are reasonable in the circumstances to ensure that the overseas recipient does not breach the Australian Privacy Principles..."

APP 8 creates an accountability mechanism: the Australian disclosing entity is deemed liable for APP breaches by the overseas recipient. Cloud AI vendors operating servers outside Australia trigger this obligation.

**Encoded in:** `compliance_agent.py` → `APP_8_CROSS_BORDER` flag. NO_PII_NO_DATA.md §"APP 8 — Cross-border disclosure deemed liability." DISCLAIMER.md §"APP 8 — Cross-border disclosure deemed liability."

---

## 6. Section 77 My Health Records Act 2012 — Health Data Localisation

**Source:** My Health Records Act 2012 (Cth), Section 77.
**PROVENANCE: CITED:24-data-localization-requirements.md**

Section 77 is a **strict prohibition** (not a "reasonable steps" obligation): My Health Record data MUST NOT be handled outside Australia. Cloud AI with offshore vendors is unlawful for health data — local-only AI (Ollama on Australian-located laptop) is the only compliant option.

**Encoded in:** `compliance_agent.py` → `S77_MY_HEALTH_RECORDS` flag (CRITICAL risk level). MODEL_SETUP.md → health-data handling restricted to Option A only.

---

## 7. Tranche 2 AML/CTF — Lawyers in Reporting Net (Effective July 2026)

**Source:** AML/CTF Amendment Act 2024 (Tranche 2).
**PROVENANCE: CITED:27-anti-money-laundering-obligations.md**

From July 2026, Australian lawyers are brought into the AML/CTF reporting net — imposing KYC, customer due diligence, and suspicious matter reporting obligations. v0.1 encodes advance-warning flags. v0.2 priority feature: automated Tranche 2 reporting module.

**Encoded in:** `compliance_agent.py` → `AML_TRANCHE_2` flag (HIGH risk level). SCOPE.md §"Out of scope — v0.2 priority feature."

---

## 8. LPUCSR Rule 36 — Publicity and Solicitation

**Source:** Legal Profession Uniform Conduct (Solicitors) Rules 2015, Rule 36.
**PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md**

Governs publicity and solicitation by solicitors. Prohibits claims of guaranteed outcomes, false specialist/expert status (unless accredited), and comparisons with other practitioners.

**Encoded in:** `compliance_agent.py` → `LPUL_R36_PUBLICITY` flag.

---

## 9. Essential Eight Cybersecurity Baseline (ASD)

**Source:** Australian Signals Directorate (ASD) Essential Eight.
**PROVENANCE: CITED:26-cybersecurity-obligations-for-lawyers.md**

Not a statutory requirement, but increasingly a de-facto requirement for professional indemnity insurance for Australian solicitors.

**Encoded in:** SECURITY.md §"Essential Eight alignment (advisory)" with detailed control mapping table.

---

## 10. APRA CPS 230 — Material Service Providers (July 2025)

**Source:** APRA CPS 230.
**PROVENANCE: CITED:26-cybersecurity-obligations-for-lawyers.md**

Expanded definition of material service providers includes cloud/AI vendors for APRA-regulated entity service providers. Advisory flag for practitioners serving banks, insurers, and superannuation funds.

**Encoded in:** NO_PII_NO_DATA.md §"APRA CPS 230 — Material service providers (advisory)."

---

## 11. Federal Court Practice Notes — AI in Court Documents

**Note:** Research did not surface a specific Federal Court Practice Note on AI use in court documents as of 2026-05-19 (analogous to UK's CPR PD 51Y on AI or New Zealand's Courts AI Guidelines). The Dayal [2024] precedent serves as the primary Australian judicial authority on AI use by practitioners. If a Federal Court or state Supreme Court Practice Note on AI is issued, this section should be updated.

**Flagged for v0.2 research update.**

---

## 12. State Law Society AI Guidance

As of 2026-05-19, individual State Law Societies have begun issuing AI guidance:
- **Law Society of NSW:** Guidance on AI in legal practice (2024-2025) — human-in-the-loop emphasis.
- **Law Institute of Victoria:** AI advisory noting LPUL Rule 9 and competence obligations.
- **Queensland Law Society:** AI risk advisory for solo practitioners.

The tool's compliance_agent is designed to be extensible: per-state rule variants can be added in v0.2+ without architectural change.

---

## Posture Summary

| Principle | Australian Source | Encoding |
|---|---|---|
| Human-in-the-loop mandatory | Law Council 2024 Joint Statement + Dayal [2024] | compliance_agent → AI_OUTPUT_HUMAN_REVIEW |
| Confidentiality (cloud AI risk) | LPUCSR Rule 9 | compliance_agent → LPUL_R9_CONFIDENTIALITY |
| Cross-border deemed liability | APP 8, Privacy Act 1988 | compliance_agent → APP_8_CROSS_BORDER |
| Health data localisation | Section 77, My Health Records Act 2012 | compliance_agent → S77_MY_HEALTH_RECORDS |
| AML reporting (July 2026) | AML/CTF Amendment Act 2024 (Tranche 2) | compliance_agent → AML_TRANCHE_2 |
| Practitioner liability for AI | Dayal [2024] FedCFamC2F 1166 | compliance_agent → DAYAL_2024_LIABILITY |
| Publicity/solicitation firewall | LPUCSR Rule 36 | compliance_agent → LPUL_R36_PUBLICITY |
| Local-only default (architecture) | All above sources | MODEL_SETUP → Option A recommended |

**The tool is assistive infrastructure. The advocate/solicitor owns the output. Human verification before filing is non-negotiable.**

This is an open-source community tool published under MIT license. It is NOT commercial legal-services solicitation. It is NOT a substitute for professional judgment. It is NOT intended for use by judicial authorities in adjudicating cases.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §3.V2 (EU AI Act — limited-risk classification), §3.V3 (UPL), §3.V9 (Conduct-Rule Inducement), §5 (Jurisdictional Positioning Australia). Playbook version: v0.1.*
