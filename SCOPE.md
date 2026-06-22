# SCOPE — AI Brain for Australia Lawyers · v0.1

## IN SCOPE (this build)

- Fork from the local memory layer 3.0.0 (MIT-licensed scaffold)
- Package renamed to `ailawfirm_australia`
- pyproject.toml v0.1.0 with Australia Solo metadata
- README + DISCLAIMER + NO_PII_NO_DATA + SECURITY + MODEL_SETUP (Step 2.6 playbook-compliant)
- SCOPE.md (this file)
- KNOWLEDGE_PROVENANCE.md (every claim traces to a `_research/` file)
- `core/ontology.py` — Australian matter types · Federal + state court hierarchy · statute registry · ART (post-Oct 2024 transition) · LPUL Rule 9 confidentiality firewall · APP 8 cross-border deemed-liability flag
- `core/calendar/` — ICS writer + publisher (timezone Australia/Sydney default · DST-aware · multi-state TZ support)
- `brain/` — 10-intent classifier (router + intents.py)
- `agents/` — 7 specialist agents (compliance · court · citation · calendar · matter · drafting · deadline)
- 3 working MCP tools:
  - `australia_court_lookup` (Federal + state + tribunal stubs · ART included)
  - `australia_citation_validator` (AGLC4 format · neutral citations · CLR · ALR · FCR · NSWLR · VR · etc.)
  - `australia_calendar_sync` (ICS · multi-TZ AUS support)
- 4 language onboarding guides: English · Simplified Chinese · Vietnamese · Arabic (RTL)
- TRANSLATION_HELP_WANTED.md
- CLI welcome banner showing 4 languages
- Test suite covering ontology · MCP tools · brain end-to-end · ICS validity
- MCP server wired with the 3 new tools
- ruff check + format both green
- Local commits clean · NO push

## Explicitly OUT OF SCOPE (v0.2+)

- Firm/ILP mode (multi-user · roles · billing · Legal Practitioner Director compliance) — v0.3+
- Real statute verbatim text — needs source PDFs · v0.2+
- Drafting templates — wolfgang_rush plugin family · separate repo
- AustLII / Federal Register / state-specific case-law direct lookup — v0.4+
- Matter calendar UI · matter dashboard — v0.2+
- Apple EventKit native — v0.2 (macOS only)
- CalDAV bidirectional sync — v0.2+
- Google Calendar API direct — REJECTED per ADR-002 D6 (privacy)
- Tranche 2 AML automated reporting module (effective July 2026) — v0.2 priority feature
- Essential Eight cybersecurity assessment tool — v0.3+
- Per-state procedural depth (NSW/VIC/QLD/WA/SA/TAS/ACT/NT-specific civ/crim rules) — v0.2+
- ART case-management workflow — v0.2+
- ML/AI generation of legal advice — Rule 9 confidentiality + Law Council Joint Statement 2024 + Dayal [2024] precedent → FORBIDDEN PERMANENTLY (compliance_agent firewall)
- Production deployment · UI beyond CLI stubs · GitHub publish — post-publisher-verify only
- Google Calendar API direct — REJECTED per ADR-002 D6 (privacy). ICS is the architecture-approved calendar sync mechanism.
- Pseudonymisation Gateway (full NER-based cloud-filter) — v0.2. Basic regex layer ported from India and adapted for AU conventions is present; spaCy-based NER deferred to v0.2.

## v0.1 test suite coverage (83 tests · 100% passing)

- Ontology enums: AustralianCourt, AustralianStatute, AustralianBarRule, MatterType, Jurisdiction
- Brain: Intent classification (10 intents), router dispatch
- Compliance agent: LPUL Rule 9 · APP 8 · Section 77 · Tranche 2 AML · Dayal [2024] · LPUL Rule 36
- Court agent: 15+ court lookups (Federal + state + ART)
- Citation agent: AGLC4 medium-neutral + reported + bracket format validation
- Calendar agent: ICS creation · multi-TZ support · DST handling · 8 Australian timezones
- MCP tools: court_lookup, citation_validator, calendar_sync — end-to-end via MCP server
- Pseudonymisation: TokenMap · sanitize/desanitize round-trip · is_safe_for_cloud checks

## Architecture notes

- **Engine:** the local memory layer 3.0.0 (MIT) — downstream fork, specialized for Australian solo practice.
- **Brain:** Rule-based + keyword classifier (no LLM dependency in v0.1). LLM gateway planned for v0.2.
- **Calendar:** ICS-only (RFC 5545 compliant). No Google Calendar API. No CalDAV. Apple EventKit native deferred to v0.2 (macOS only).
- **MCP:** 3 tools wired via JSON-RPC stdio transport. Claude Code / Cursor / any MCP-compatible client.
- **Config:** `~/.ailawfirm-australia/config.json`. Env-var overrides supported. Cloud mode gated behind `cloud_warning_acknowledged` flag.
- **Storage:** ChromaDB (palace memory) + SQLite. All local under `~/.ailawfirm-australia/`.

## Compliance

- LEGAL_EXPOSURE_PLAYBOOK v0.1 compliant from Day 1.
- All 16 pre-ship checklist items addressed.
- COMPLIANCE_POSTURE.md encodes Australian AI-use doctrine (Law Council 2024 · Dayal [2024] · LPUL · APP 8 · Section 77 · Tranche 2 AML).
- DISCLAIMER.md + NO_PII_NO_DATA.md + SECURITY.md + MODEL_SETUP.md shipped.
- Knowledge provenance: every domain claim traces to a CITED: research file.

## Dependencies (pinned)

- mcp>=0.5.0 · pydantic>=2.0 · icalendar>=5.0 · python-dateutil>=2.8 · pyyaml>=6.0
- Python ≥3.10 (zoneinfo for DST-native calendar support)
