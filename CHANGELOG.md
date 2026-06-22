# CHANGELOG — AI Brain · Australia

All notable changes to the AI Brain — Australia project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.1] — 2026-06-05

### Changed

- **README.md** — refined headline tagline, "Why this exists" closing line, tier table rows (Local Ollama · DeepSeek · Claude/Gemini), and "Privacy & Data Handling — what stays where" section to honestly disclose the dual-mode architecture (local-default · cloud-optional) and the role of the internalised Pseudonymisation Gateway as the structural privacy primitive when cloud mode is invoked.
- **Section 77 My Health Records hard-exception is now explicit at three places** (headline · tier-table · privacy section):
  - The Section 77 prohibition is on the act of offshore handling itself, NOT on what is transmitted.
  - Gateway sanitisation does NOT cure this prohibition because the pseudonymised payload is still being handled offshore by the cloud-LLM vendor.
  - For any matter that touches actual MHR identifiers, the only compliant tier is Local Ollama.
- **APP 8** is also reframed: Gateway sanitisation supports APP 8.2 risk assessment, but does NOT displace APP 8.1 disclosure duty.

### Why this matters
An Australian solo solicitor relying on the prior *"Your data stays on your machine"* line who configured a cloud-LLM provider for MHR-touching work would have been seriously misled — Section 77 is a hard offshore-handling prohibition with civil-penalty exposure up to AU$50M, and Gateway sanitisation does NOT cure it. The refinement makes the hard ceiling explicit. The wedge over commodity cloud AI is preserved for non-MHR matters.

### Unchanged

- All agents, drafting templates (79 templates + 13 statute digests + 39 jurisdiction research files), tests, getting-started guides, and the Pseudonymisation Gateway itself are unchanged. This is a documentation + privacy-disclosure-honesty refinement, not a behavioural change.

---

## [0.1.0] — 2026-05-19

### Added

- **Bootstrap layer:** Forked from the local memory layer 3.0.0 (MIT) — package renamed to `ailawfirm_australia`.
- **Brain layer:** 10-intent classifier (rule-based + keyword) with router dispatching to 7 specialist agents.
- **7 specialist agents:** compliance_agent (LIVE) · court_agent (LIVE) · citation_agent (LIVE) · calendar_agent (LIVE) · matter_agent (STUB) · drafting_agent (STUB) · deadline_agent (STUB).
- **3 working MCP tools:** `australia_court_lookup` (Federal + state + ART tribunal) · `australia_citation_validator` (AGLC4 format: medium-neutral + reported) · `australia_calendar_sync` (ICS with multi-TZ Australian support: 8 timezones, DST-aware).
- **Core ontology:** AustralianCourt (30 courts) · AustralianStatute (11 statutes) · AustralianBarRule (4 rules) · MatterType (9 types) · Jurisdiction (9 jurisdictions). Every entry carries `PROVENANCE: CITED:<research-file>`.
- **Compliance encoding:** LPUL Rule 9 confidentiality · APP 8 cross-border deemed liability · Section 77 My Health Records health-data localisation · Tranche 2 AML advance warning (effective July 2026) · Dayal [2024] AI-output liability · Law Council 2024 Joint Statement human-in-the-loop · LPUCSR Rule 36 publicity/solicitation firewall.
- **LEGAL_EXPOSURE_PLAYBOOK v0.1 compliant from Day 1:** DISCLAIMER.md · NO_PII_NO_DATA.md · SECURITY.md · MODEL_SETUP.md · KNOWLEDGE_PROVENANCE.md · SCOPE.md shipped.
- **4-language onboarding:** English (authoritative) · Simplified Chinese (简体中文) · Vietnamese (Tiếng Việt) · Arabic (العربية, RTL). AI-assisted with native-PR-welcome pattern.
- **CLI welcome banner:** G'day · 你好 · Xin chào · مرحبا.
- **Connect-local one-command CLI:** `ailawfirm-australia connect-local` detects Ollama install, RAM, recommends and downloads model, configures local AI.
- **83 tests passing** (38+ target exceeded). ruff check + format both green.
- **Provenance discipline:** Every domain claim traces to `_research/` or `_statute_corpus/` file. AS-OF dated. No TRAINED-only claims.
- **Pseudonymisation gateway:** Ported from India architecture, adapted for Australian data conventions (AU phone format · TFN format · ABN/ACN format · Medicare number format · driver licence format · Australian postcodes).

### Built against

- LEGAL_EXPOSURE_PLAYBOOK v0.1 (2026-05-18)
- the local memory layer 3.0.0 (MIT)
- Australia research corpus: 39 markdown digests (Gemini-on-Mac-mini, 2026-05-19)
- Australia statute corpus: 13 statute-text digests (8/8 Tier 1 · 5/9 Tier 2 verified)

---

*[0.1.0]: https://github.com/Wolfgangrush/ai-law-firm-australia/releases/tag/v0.1.0*
