# DISCLAIMER — AI Brain for Australia Lawyers

**Read this before installation or use.**

## What this tool is

AI Brain — Australia · Solo is **open-source developer software** (MIT-licensed) published by wolfgang_rush. It is a **productivity aid for qualified legal professionals**. It is not a legal service. It does not perform autonomous legal reasoning. Every output it produces must be reviewed by counsel admitted to practice in the relevant Australian jurisdiction before any client-facing use.

## Who may use this tool

AI Brain — Australia is intended exclusively for:

- **Solicitors** admitted to practice under the Legal Profession Uniform Law (NSW · VIC) or the relevant state Legal Profession Act
- **Barristers** regulated by the Australian Bar Association and the relevant state Bar Association
- **Legal Practitioner Directors** of Incorporated Legal Practices (ILPs) under Part 2.6 LPUL
- In-house counsel employed by Australian entities and working on Australian-law matters
- Paralegals working under the supervision of any of the above

**If you are not a qualified legal professional, do not use this tool to produce client-facing legal work.**

## What this tool is NOT

This tool does NOT:

- Provide legal advice
- Provide legal opinions
- Represent any party in any matter
- Perform any function that constitutes "engagement in legal practice" as defined under the Legal Profession Uniform Law (NSW · VIC) or state Legal Profession Acts
- Replace the role of a qualified Australian solicitor or barrister
- Generate court-grade or production-ready legal documents without counsel review
- Operate as a service from any server controlled by the publisher

## Publisher's jurisdiction

The publisher (wolfgang_rush — Rushikesh Mahajan) is an Indian advocate admitted to practice at the High Courts of India, under the Advocates Act 1961. The publisher is NOT admitted to practice in any Australian jurisdiction (NSW · VIC · QLD · WA · SA · TAS · ACT · NT). The publisher does NOT offer legal services in any Australian jurisdiction. The publisher offers this tool as **open-source software**, published from India under the MIT license, for use by Australian-admitted practitioners in their own practice.

## LPUL + State Bar Conduct Rules (your obligations)

If you are an Australian solicitor, your use of this tool must comply with:

- **LPUCSR Rule 9** — Confidentiality. You must not disclose confidential information concerning a client. The tool's local-only default mode is designed to support Rule 9 compliance. Cloud-mode use must consider Rule 9 implications carefully.
- **LPUCSR Rule 10** — Conflicts of interest concerning former clients.
- **LPUCSR Rule 11** — Conflicts of interest concerning current clients.
- **LPUCSR Rule 36** — Publicity and solicitation. AI-generated marketing material must comply with Rule 36 restrictions.
- **LPUBR** — Barristers' Conduct Rules (applicable barristers).

If you are a barrister, your use must additionally comply with the Barristers' Conduct Rules of your state Bar Association and the Australian Bar Association's guidelines.

## Privacy Act 1988 and Australian Privacy Principles (APP)

The publisher is **not an APP entity** with respect to your tool usage — the publisher operates no server processing user input. See [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) for the complete zero-collection architecture.

If you use the tool to process personal information of your clients or any individual, **you** are the APP entity for that processing and your obligations under the Privacy Act 1988 apply (APP 1 open and transparent management · APP 2 anonymity and pseudonymity · APP 3 collection of solicited PI · APP 6 use or disclosure · APP 8 cross-border disclosure — see below · APP 11 security of PI).

For client-confidential work, use the **local-only mode** (Ollama + Qwen3 or equivalent). See [MODEL_SETUP.md](MODEL_SETUP.md).

## APP 8 — Cross-border disclosure deemed liability

APP 8 of the Privacy Act 1988 provides that an APP entity that discloses personal information to an overseas recipient is **deemed to be liable** for any act or practice of the overseas recipient that breaches the APPs. If you use cloud AI services where the vendor processes data outside Australia, APP 8's deemed-liability provision applies to **you** as the disclosing entity. The publisher provides the tool; you decide whether and how to engage cloud processors.

## Section 77 — My Health Records Act 2012

Section 77 of the My Health Records Act 2012 prohibits handling of My Health Record data outside Australia. If you handle health information subject to the My Health Records Act, cloud-mode use with offshore vendors is **strictly prohibited**. Use local-only AI exclusively for any health-related personal information.

## Output liability

The tool is provided AS-IS under the MIT license, without warranty of any kind, express or implied. The publisher is not liable for tool output. **You** are the responsible operator. Every output must be reviewed by you before use.

The Law Council of Australia's 2024 Joint Statement on AI in Legal Practice requires a human-in-the-loop for all AI-assisted legal work. The precedent in *Dayal [2024] FedCFamC2F 1166* establishes practitioner liability for relying on AI-generated content without adequate review. The publisher accepts no responsibility for outputs you choose to act upon without review.

## Statutory currency

Australian statutory law evolves continuously. The tool's encoded knowledge has an AS-OF date documented in [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md). The publisher makes reasonable efforts to keep the tool current but does NOT guarantee currency. Always verify any statutory provision against the official source (Federal Register of Legislation · AustLII · state legislation websites) before relying on it for client work.

Particularly volatile areas as of 2026:
- Tranche 2 AML/CTF Amendment Act 2024 (effective July 2026 — lawyers brought into reporting net)
- ART transition (Administrative Review Tribunal operative October 2024 — AAT replaced)
- APRA CPS 230 (material service provider definition expanded July 2025)
- Privacy Act 1988 reform (review in progress)

## Cross-border practice

The publisher does not offer cross-border legal services. The act of publishing software from India for use in Australia does NOT constitute the practice of law in Australia by the publisher.

## Foreign judgment / enforcement

The publisher operates entirely from Indian soil with no assets in any Australian jurisdiction. Any claim against the publisher must comply with Indian law on enforcement of foreign judgments (Section 13, Code of Civil Procedure 1908).

## Contact

For questions about this disclaimer or tool usage: GitHub Issues at the repo URL. The publisher does NOT accept legal-services engagement through this tool or its repository.

---

*This disclaimer references LEGAL_EXPOSURE_PLAYBOOK §3.V3 (UPL — Australian state Legal Profession Acts), §3.V4 (Data Protection — Privacy Act 1988 + APP), §3.V6 (Advertising — ACCC), §3.V8 (Cross-border), §5 (Jurisdictional Positioning Australia). Playbook version: v0.1.*
