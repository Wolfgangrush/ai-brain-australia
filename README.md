<div align="center">

<img src="docs/banner.png" width="820"/>

**A practice brain for Australia's lawyers — local-first, running on your own machine.**

Visit the live site: [wolfgangrush.github.io](https://wolfgangrush.github.io)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Local-first](https://img.shields.io/badge/local--first-on%20your%20machine-blue)
![Jurisdiction](https://img.shields.io/badge/jurisdiction-Australia-orange)
![Lawtech](https://img.shields.io/badge/built%20for-lawyers-lightgrey)

</div>


# 🇦🇺 AI Brain for Australia Lawyers

> **Free practice OS for every Australian solo solicitor and barrister. Terminal-native. Local-first by default (Ollama + Qwen3 — nothing leaves your laptop). Cloud-LLM optional with the [Pseudonymisation Gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) sanitising PII before any prompt leaves the machine. ⚠️ Section 77 My Health Records data: use Local Ollama tier only — Gateway sanitisation does not cure the offshore-handling prohibition. Built for the LPUL era + Tranche 2 AML + Section 77 reality.**

**For qualified legal professionals only.** Intended for solicitors and barristers admitted to practice in any Australian state or territory under the Legal Profession Uniform Law (NSW · VIC) or the relevant state Legal Profession Act, in-house counsel of Australian entities, and paralegals working under their supervision. **If you are not a qualified legal professional, do not use this tool to produce client-facing legal work.** Read [DISCLAIMER.md](DISCLAIMER.md) before installation.

**Version:** 2.0.0 · **License:** MIT · **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). NOT admitted in any Australian jurisdiction. This is a software publication for Australian-admitted practitioners. · **Engine:** Built on [MemPalace](https://github.com/MemPalace/mempalace) (MIT)

## 🆕 New in v2.0 — the terminal brain now works end-to-end

Earlier the brain (classify → route → specialists) was not wired to the terminal and several agents were placeholders. **Now it is a working second brain you talk to:**

| Command | What it does |
|---|---|
| `reception` | **"turn it on"** — greets you, checks every specialist is online, loads your retrospective memory |
| `ask "<question>"` | one-shot — routes your question to the right specialist and answers |
| `chat` | interactive session — keep asking; every line is routed for you (no commands to memorise) |
| `recap` | what you did in past sessions (memory persists across runs) |

Every specialist is **AI-backed** by whatever host you launch it under (Claude · GLM · Codex — it reads your `ANTHROPIC_*` environment), grounded on a deterministic engine so answers stay accurate. It runs under **any** host CLI — a `UserPromptSubmit` hook + `AGENTS.md` route every query through the brain instead of the model free-answering. Free public edition — no enterprise features.


> ⚠️ **AI can make mistakes. Always verify the output.**
>
> This software generates assistive drafts and suggestions only. Every legal claim, citation, statute reference, procedural step, deadline calculation, and ground of relief must be independently verified by a qualified human practitioner before filing, advising a client, or relying on the output. The publisher accepts no liability for outputs used without verification.

> 🛡️ **Privacy primitive: PII pseudonymisation** via [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) (wolfgang_rush · MIT). This firm uses the `australia` jurisdiction module + Indian-diaspora overlay for cross-jurisdiction PII coverage. Open-source · zero runtime deps · session-scoped · in-memory only · never writes PII to disk.


> 🛡️ **Pseudonymisation coverage (v0.1.1):** The privacy gateway pseudonymises PII before any cloud-API call; any residue the scanner can't fully resolve is surfaced to you and audit-logged — you retain the final call (v0.3 honest-disclosure). Covers Australia-native identifiers (TFN · Medicare · ABN · ACN · AU phone numbers · AUD amounts · AU Federal/state court case numbers · BSB codes) and Indian-diaspora identifiers (Aadhaar · PAN · GSTIN · IFSC · Indian phone — Australia has substantial South Asian diaspora, essential for South-Asian-Australian client matters). Generic patterns (email · names with honorifics · dates · case numbers) work cross-jurisdiction.

> **🧠 AI Brain that LEARNS.** Every session makes the next one smarter. Two built-in Claude Code skills power this: `/retrospective` saves what the firm learned at session end — every jurisdiction, statute, argument pattern, and procedural rule you touched is logged so the firm's knowledge compounds. `/wake` loads that accumulated context the next time you start, so you never begin from zero. The firm is your second brain, and it gets sharper with every case.

---

## 🌐 Choose your language

| Script | Language | Audience | Guide |
|---|---|---|---|
| 🇦🇺 | **English** | All Australian jurisdictions · authoritative | [GETTING_STARTED.md](GETTING_STARTED.md) |
| 🇨🇳 | **中文 (Simplified Chinese)** | Mandarin-speaking community (Sydney · Melbourne) | [GETTING_STARTED_CHINESE.md](GETTING_STARTED_CHINESE.md) |
| 🇻🇳 | **Tiếng Việt (Vietnamese)** | Vietnamese-Australian legal community | [GETTING_STARTED_VIETNAMESE.md](GETTING_STARTED_VIETNAMESE.md) |
| 🌍 | **العربية (Arabic)** | Arabic-speaking bar (Lebanese · Syrian · Iraqi Australian) | [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md) — RTL |

> 🙏 **Honest note:** Three of these guides were AI-assisted. **Native-speaker PRs warmly welcome** via [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md).

---

## 💛 Why this exists

> Australian solo practitioners navigate a uniquely shifting regulatory stack as of 2026:
> - **AAT → ART transition** (Administrative Review Tribunal, October 2024) — most significant federal administrative-law change in decades
> - **Tranche 2 AML/CTF Amendment Act 2024** — lawyers brought into reporting net **by July 2026**; significant KYC + reporting overhead for solo practice
> - **APRA CPS 230** (July 2025) — material service providers definition expanded to include cloud + AI vendors for financial-services-adjacent practice
> - **Section 77 My Health Records Act** — gold-standard data-localisation prohibition; offshore handling of health data flatly forbidden
> - **APP 8 deemed-liability** — Australian firms responsible for the privacy breaches of their overseas vendors
> - **Dayal [2024] FedCFamC2F 1166** — practitioners remain personally liable for AI output; "human in the loop" no longer optional per Law Council 2024 Joint Statement
> - **Essential Eight cybersecurity** — de facto requirement for professional indemnity insurance
> - **CPD 10 units annual** with mandatory categories
> - **ILP structure (Incorporated Legal Practice)** with mandatory Legal Practitioner Director — modern standard for tech-enabled solo practice

Top-tier firms have AI procurement teams + compliance officers. Solo practitioners don't. We built this so an Australian solo — whether ex-Magic-Circle going solo in Brisbane or career rural-town sole-practitioner in regional NSW — can have a second brain that costs **AU$0 forever**, runs locally by default (Ollama + Qwen3), and supports APP 8 + LPUL Rule 9 confidentiality + Tranche 2 AML at the architecture layer — either by absence of transmission (local mode) or by Pseudonymisation Gateway sanitisation (cloud mode). **Section 77 My Health Records data is a hard exception** — the prohibition is on offshore handling itself, not on what is transmitted, so Gateway sanitisation does not cure it; for actual MHR matters use Local Ollama tier only.

---

## 🧠 What's inside — specialists who live in your terminal

| # | Specialist | What they do for you |
|---|---|---|
| 🧠 | **The Receptionist (brain)** | Listens to what you say. Figures out who you need. Calls the right specialist. You never memorize commands. |
| 📂 | **The Matter Manager** | Holds every active matter — parties, prayers, hearings, orders, draft state. Walk into court · context comes back instantly. |
| 📜 | **The Citation Clerk** | Parses Australian citations — AGLC4 format · medium-neutral (`[2024] HCA 12` · `[2024] FCAFC 100`) · reported (`(2023) 271 CLR 1` · `(1991) 25 NSWLR 1`). |
| 🏛️ | **The Court Registrar** | Knows the Australian court hierarchy: HCA · FCA · FCFCOA · **ART** (post-Oct 2024 transition) · plus state Supreme · District/County · Local/Magistrates courts across NSW · VIC · QLD · WA · SA · TAS · ACT · NT. |
| ✍️ | **The Drafting Assistant** | Ships with 13 verified Australian statute digests + 39 jurisdiction research files **plus 79 drafting templates** in [`_drafting_data/`](_drafting_data/) covering: 9 contracts (sale of goods · services · employment · NDA · tenancy · commercial lease · shareholders · loan · deed of release) · 5 pleadings · 5 motions · affidavits + statutory declarations · ART application · pre-action + consent orders · costs · subpoenas · drafting style **plus full 13-category litigation backbone**: appeals (FCAFC · HCA special leave · grounds · written submissions · Appeal Book) · injunctions (without-notice · Mareva GPN-FRZG · Anton Piller GPN-SRCH · undertaking · interlocutory skeleton) · disclosure (FCR Part 20 list of documents · privilege log Esso doctrine · subpoena + non-party discovery) · expert evidence (FCR Part 23 letter of instruction · expert report · joint conference · single joint expert · concurrent evidence / hot-tubbing) · default judgment + set aside (Evans v Bartlam) · enforcement (Writ of Execution · garnishee · charging order · EJD · bankruptcy) · skeleton arguments (trial · interlocutory · CMC/directions) · counsel briefing (brief to counsel · advice on merits) · judicial review (ADJR Form 56 · grounds map) · trial documentation (Court Book · chronology + cast list + reading list · List of Authorities AGLC4 · written closing Briginshaw + Fox v Percy) · ADR (mediation position · agreement · settlement deed · WP/Calderbank/FCR Part 25) · insolvency (Corporations Act winding-up · VA · DOCA) · tribunals (FWC unfair dismissal · NCAT/VCAT/QCAT + ART post-AAT 2024 · FCFCOA family law). All templates use AGLC4 citation and cite Federal Court Practice Notes (GPN-APP · GPN-DISC · GPN-EXPT · GPN-FRZG · GPN-SRCH · GPN-SUBP · GPN-WRTS · CM 1). Optionally connects to the wolfgang_rush drafting plugin family (separate, MIT) for additional drafting flows. |
| 🛡️ | **The Compliance Officer** | Watches your firm website, LinkedIn, marketing for **LPUL Solicitors' Conduct Rule 36** (publicity/solicitation) firewall risks. Surfaces **Tranche 2 AML** advance-warning flag (effective July 2026). Flags **Section 77 My Health Records** health-data-localisation prohibition. Flags **APP 8** cross-border deemed-liability. Warns when AI-output use requires human-in-the-loop per Dayal [2024] FedCFamC2F 1166 + Law Council 2024 Joint Statement. |
| 📅 | **The Calendar Sync** | ICS feed sync to iPhone Calendar / Google Calendar / Outlook — no third-party API, no data processor. code-aliased summary line (lock-screen safe) · full matter detail in event body. Multi-TZ Australian support (Sydney default · Melbourne · Brisbane · Perth · Adelaide · Hobart · Darwin · ACT · zoneinfo DST-aware where applicable; Perth + Brisbane handled as no-DST). |

---

## 🚀 Install in 30 minutes

### Step 1 — Pick your operating system

| OS | Guide |
|---|---|
| 🍎 **Mac** | Standard Python install (Terminal) |
| 🪟 **Windows** | PowerShell · standard pip install |
| 🐧 **Linux** | Same commands as Mac |

### Step 2 — Install Python (one-time) + the tool

```bash
pip install git+https://github.com/Wolfgangrush/ai-law-firm-australia.git
```

### Step 3 — Connect an AI brain (ONE COMMAND)

```bash
ailawfirm-australia connect-local
```

This single command:
1. Detects if Ollama is installed; if not, prints platform-specific install instructions
2. Detects your laptop's RAM
3. Recommends and downloads the right Qwen3 model (14b for 16GB+ · 7b for 8GB · 1.7b for older laptops)
4. Writes config so all subsequent calls route to local Ollama
5. Runs a smoke test to confirm local connectivity

After this, **no queries leave your laptop**.

Three honest model options — see [MODEL_SETUP.md](MODEL_SETUP.md):

| Choice | Cost | Privacy | Best for |
|---|---|---|---|
| 🥇 **Local Ollama + Qwen3** | AU$0 forever | 🟢 Perfect — nothing leaves your laptop | **Client matters · Section 77 health-data work (MANDATORY tier for actual MHR data — Section 77 is a hard offshore-handling prohibition that Gateway sanitisation does NOT cure) · APP 8-restricted data · LPUL Rule 9 confidentiality · use this tier when zero cross-border data flow is required** |
| 🥈 **DeepSeek API** | ~AU$3-7/mo | ⚠️ Pseudonymisation Gateway sanitises TFN/Medicare/ABN/ACN/Aadhaar + names before transmission, BUT China is NOT an APP 8 adequate jurisdiction; cross-border deemed-liability still applies to the pseudonymised transmission | Non-client work · public-law research · templates |
| 🥉 **Claude / Gemini API** | ~AU$30-100/mo | 🟢 Strong (enterprise privacy default-ON) — Gateway sanitises before transmission | Heavy daily users with executed APP 8 third-party-service-provider risk assessment + your vendor's APP 8.2 disclosure documentation. **NOT for Section 77 MHR data** — that requires Local Ollama tier irrespective of Gateway. |

### Step 4 — Run

**▶ Quickstart — the commands that now work:**
```bash
python3 -m ailawfirm_australia reception                 # turn it on: greeting + systems check + memory
python3 -m ailawfirm_australia ask "validate a case citation"
python3 -m ailawfirm_australia ask "which court has jurisdiction over my matter"
python3 -m ailawfirm_australia chat                      # interactive — type anything, it routes for you
python3 -m ailawfirm_australia recap                     # what you did last time
```
Inside a host CLI (Claude / GLM / Codex) opened in this folder, just say **"turn it on"** — the receptionist greets you, Solicitor, and routes everything through the brain.


```bash
ailawfirm-australia
```

Sample commands:

```
> tell me about ART jurisdiction (post-AAT transition)
> validate [2024] HCA 12
> check this advert: "Best personal-injury solicitor in Brisbane"
> what's the Tranche 2 AML reporting threshold for solicitors?
> add hearing MAT-2026-014 NSWSC Banco Court 2026-06-09 10:00 AEST
> sync calendar
```

---

## 🔒 Privacy & Data Handling — what stays where

**Architecture — three pieces decide your privacy posture:**

**(1) Local-only state.** Your matters, drafts, audit logs, calendar entries, and configuration live in `~/.ailawfirm_australia/`. Never uploaded by the tool. Never synced to a third-party cloud by the tool. No telemetry. No "anonymous usage statistics." The publisher operates zero infrastructure and cannot access this folder. Verifiable via `grep -ri "telemetry\|analytics\|requests.post\|urlopen" ailawfirm_australia/` — should return only user-initiated cloud-LLM calls.

**(2) LLM backend — you choose.** The default `connect-local` command configures Ollama + Qwen3 to run the language model on your laptop (truly nothing leaves). If you opt into a cloud-LLM tier (DeepSeek / Claude / Gemini) for quality reasons, see the tier table above for cost + privacy trade-offs.

**(3) Pseudonymisation Gateway — always-on for cloud mode.** When you configure a cloud-LLM provider in `~/.ailawfirm_australia/config.json`, the internalised `PseudonymisationGateway` (source: `ailawfirm_australia/pseudonymisation.py`) automatically substitutes real names, government IDs (TFN · Medicare · ABN · ACN · BSB · Aadhaar for Indian-diaspora matters), contact identifiers (phone · email), and case references (HCA · FCA · FCAFC · state Supreme Court numbers) with deterministic placeholders BEFORE the prompt leaves your machine. The placeholder ↔ original map lives in memory only (never written to disk; destroyed when the gateway goes out of scope). Cloud vendors see only the abstract structure of the matter; the user sees real values restored in the response.

**⚠️ Section 77 My Health Records hard exception.** Section 77 of the *My Health Records Act 2012* (Cth) prohibits the offshore handling of MHR data — the prohibition is on the act of transmission itself, NOT on what is transmitted. **Gateway sanitisation does not cure this prohibition** because the pseudonymised payload is still being handled offshore by the cloud-LLM vendor. For any matter that touches actual MHR identifiers, the only compliant tier is Local Ollama. The Compliance Officer agent flags this automatically when it detects Section 77 keywords in your matter context.

**APP 8 cross-border deemed-liability** also applies to cloud-mode use: Gateway sanitisation supports your APP 8.2 risk assessment (because what crosses the border is structurally pseudonymised) but does not displace your underlying APP 8.1 disclosure duty to the affected individual. Document the choice in your audit log.

The wedge: every other cloud-AI legal tool sends raw client PII to the LLM by default. wolfgang_rush AI Brain — Australia ships Ollama-first AND ships the Gateway as the privacy primitive that closes the gap when you choose cloud mode for quality reasons — while remaining honest that Section 77 is a hard local-only ceiling no library can cure.

### What goes to the API provider during each query

Each time the firm reasons about a matter, the following are sent to your chosen API provider:
- Your prompt (the question or instruction)
- Relevant context the firm pulls from your local matter folder (current draft state, recent orders, citations being verified)

Your full matter history, audit logs, and unrelated cases are NOT sent. The firm sends the minimum context needed to answer the current question.

### What API providers contractually guarantee

| Provider | Trains on your data? | Retention | Source |
|---|---|---|---|
| **Claude API** (Anthropic) | ❌ No — Commercial Services data is not used for training | ~30 days for safety/abuse review (Zero Data Retention available on enterprise contract) | [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy) · [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) |
| **OpenAI API** (GPT-4) | ❌ No — API data not used for training since March 2023 | ~30 days for abuse review (ZDR available) | [OpenAI API Data Usage Policies](https://openai.com/policies/api-data-usage-policies) |
| **Gemini API (paid via Vertex AI)** | ❌ No — paid-tier API data not used for training | Per Google Cloud contract | [Vertex AI data governance](https://cloud.google.com/vertex-ai/docs/general/data-governance) |
| **Gemini Free Tier** | ⚠️ **YES — Google AI uses free-tier prompts to improve products** | — | [Google AI Studio terms](https://ai.google.dev/gemini-api/terms) — **DO NOT use free-tier Gemini for confidential client matters.** |
| **DeepSeek V4 Pro API** | ❌ No — per DeepSeek API terms, inputs/outputs not used for model training | Retention policy less documented than OpenAI/Anthropic; verify for matter sensitivity | [DeepSeek API ToS](https://platform.deepseek.com/api-docs/legal) · **Note:** provider is China-based; consider jurisdictional data-residency requirements |

### What that does NOT mean — solicitor's residual risk

Even though API data is not used for training:

1. **Data IS in transit** during each query — it passes through the provider's infrastructure
2. **Brief logging retention** (typically 30 days) means the provider holds the data for that window
3. **Lawful access requests** — a subpoena, lawful intercept warrant, Privacy Act data-subject access request, or provider security incident could expose data during the retention window
4. **Provider-side breach risk** — however small, it exists

This is fundamentally different from local-LLM mode (where no data leaves your machine, ever, period). The `connect-local` command already configures Ollama + Qwen3 as the v0.1 default — solicitors handling confidential, privileged, or special-category data should stay in local-LLM mode for that work. The cloud-LLM tier exists for non-confidential research, public-law analysis, and template scaffolding where contractual no-training is a sufficient safeguard.

### Solicitor's decision

If your matter is:
- **General commercial / corporate / contract drafting** → Claude / OpenAI / paid Gemini API are appropriate. Contractual no-training protections are strong. Audit logs are local.
- **Legal-privileged client communication / privileged litigation strategy** → Evaluate against your jurisdiction's professional conduct rules. Most regulators permit reasoned use of cloud-AI with disclosure to the client. (See Australia (state Bar associations) guidance.) Document the choice in your audit log.
- **APP special-category data / health / criminal record / political opinion** → Stay in `connect-local` (Ollama + Qwen3) mode. Do not opt into any cloud-LLM tier for these matters; do not use free-tier Gemini.
- **State secrets / classified material / under-seal court orders** → Stay in `connect-local` (Ollama + Qwen3) mode. For physically air-gapped networks where the pip-install / model-download / auto-update paths are also prohibited, await the v0.3+ signed offline-install bundle below.

The firm's audit log captures every API call (timestamp, agent, prompt-summary, output-summary) at `~/.ailawfirm_australia/audit_logs/`. Logs never leave your machine. They are your professional-conduct compliance trail.

### v0.3+ roadmap

> What v0.1 already ships: (a) local-LLM default via `connect-local` (Ollama + Qwen3 — nothing leaves your laptop in local mode), (b) configurable cloud-LLM tier covering Claude / OpenAI / paid Gemini / DeepSeek, (c) Pseudonymisation Gateway sanitising PII before any cloud-LLM call, and (d) no first-party telemetry. The items below extend the floor — they are not a future replacement for what is already shipped.

- **Signed offline-install bundle** — the `pip install` path currently touches PyPI and the Ollama model registry; v0.3+ ships a signed offline-installable archive with the Qwen3 model pre-bundled, removing the last network-touch point even at install time. For solicitors on physically air-gapped networks (under-seal court matter rooms, state-secret-clearance environments).
- **In-firm LLM tenant adapter** — drop-in config for Azure OpenAI / private Vertex / on-prem vLLM endpoints. Distinct from the today-shipped public-API cloud-LLM tier; targets solicitors whose firm already provisions LLM infrastructure under its own DPA.
- **Expanded local-model surface** — Llama 3.3 70B / Qwen 2.5 72B / DeepSeek V4 Pro (open-weights via Ollama), for solicitors with larger laptops who want better-than-Qwen3-14b local reasoning.

Tracked at: [drafting-agents-core issues](https://github.com/Wolfgangrush/drafting-agents-core/issues).

---

**No agenda · no telemetry · no cloud-default · MIT licensed · A$0 forever.**

**Australia (state Bar associations) Rule compliance built into the tool's audit + transparency-gate architecture.** Solicitor remains professionally responsible for every output. The firm is a force-multiplier, not a substitute for judgment.

---

## 📁 Where your data lives

```
~/.ailawfirm-australia/              ← Mac/Linux
C:\Users\YourName\.ailawfirm-australia\  ← Windows
├── palace/                          ← all matter/client/citation memory (ChromaDB)
├── config.json                      ← your settings (AI provider · state · timezone · prefs)
├── calendars/                       ← generated .ics feeds for iPhone/Outlook subscribe
└── people_map.json                  ← optional client alias system (lock-screen safety)
```

Copy this folder to a USB drive · OneDrive · iCloud Drive · Dropbox = complete backup of your practice in 5 seconds.

---

## 🔄 How to update your firm

When a new version of AI Brain — Australia is published, you pull it in with **one command**. Your matter data + your project-root `CLAUDE.md` are **never touched** — only the firm's installed code, skills, and prompts refresh.

### Path 1 — Plain terminal

```
ailawfirm-australia update
```

Under the hood this runs `pip install --upgrade git+https://github.com/Wolfgangrush/ai-law-firm-australia.git`. After it finishes, restart any open `ailawfirm-australia` session so the new skills + prompts load.

### Path 2 — Inside Claude Code

Type:

```
/update
```

Claude runs the same command for you and reports the result.

### Path 3 — Inside Gemini CLI

Type:

```
/update
```

Same outcome — Gemini calls `ailawfirm-australia update` for you.

### When to update

- **The publisher tells you** a new version is out → update.
- **Monthly hygiene** → update once a month so you stay current on skills + bug fixes.
- **After hitting a bug** → first thing to try is updating, in case it is already fixed upstream.

### What does NOT update (by design)

- Your matter folders (`~/Desktop/<your-firm>/<matter>/...`)
- Your project-root `CLAUDE.md` (your customisations always win)
- Your `~/.ailawfirm-australia/` config + palace data
- Your chosen AI model setup (Ollama · DeepSeek · Claude · Gemini)

Only the firm's installed Python code, skills, and template files refresh. Your practice is unaffected.

### One catch — existing users + new template rules

If a new version updates the template `CLAUDE.md` (the firm's standing rules), your project-root `CLAUDE.md` is preserved because your customisations always win. To see what changed in the template after an update:

```
diff CLAUDE.md "$(python3 -c 'import ailawfirm_australia, os; print(os.path.join(os.path.dirname(ailawfirm_australia.__file__), "templates/CLAUDE.md"))')"
```

Review the diff and merge what you want into your own `CLAUDE.md`.

---

## 🛤️ Roadmap (honest)

> 🙏 **Honest note on timelines:** Solo-author OSS · ships as time permits · v0.2 / v0.3 / v0.4+ targets are indicative, not committed dates. Open an issue if a specific feature on a specific timeline matters to your work.



- **v0.1.0** *(shipped)* — bootstrap: architecture, brain layer with 10-intent classifier, 7 specialist agents (4 live · 3 stubs), 3 working MCP tools (court · citation · calendar), 4-language onboarding (English · Mandarin · Vietnamese · Arabic), connect-local one-command CLI, LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance, ART (post-Oct 2024) + Tranche 2 AML + Section 77 + APP 8 + Dayal [2024] FedCFamC2F 1166 compliance flags baked in
- **v0.2 — knowledge layer** *(shipped 2026-05-28)* — **79 drafting templates** in `_drafting_data/` covering the full litigation + commercial + tribunal backbone for Australian solo practice: (a) 9 contracts; (b) 5 pleadings + 5 motions + affidavits/statutory declarations; (c) court forms (Federal commencement · ART application) · pre-action + consent orders · costs · subpoenas; (d) **full 13-category litigation backbone (46 new templates)** — appeals (FCAFC · HCA special leave · grounds · submissions · Appeal Book), injunctions (without-notice · Mareva GPN-FRZG · Anton Piller GPN-SRCH · undertaking · interlocutory skeleton), disclosure (FCR Part 20 · privilege log Esso doctrine · subpoena + non-party discovery), expert evidence (FCR Part 23 · joint conference · SJE · concurrent evidence), default judgment + Evans v Bartlam set aside, enforcement (Writ · garnishee · charging order · EJD · bankruptcy), skeleton arguments (trial · interlocutory · CMC), counsel briefing (brief · advice on merits), judicial review (ADJR Act Form 56 · grounds map), trial documentation (Court Book · chronology · List of Authorities AGLC4 · written closing), ADR (mediation · settlement deed · WP/Calderbank/FCR Part 25), insolvency (Corporations Act winding-up · VA · DOCA), tribunals (FWC unfair dismissal · state CATs · ART · FCFCOA family law). All templates cite Federal Court Practice Notes + AGLC4 throughout.
- **v0.2 — statute knowledge layer** *(shipped 2026-05-28)* — **13 Tier-1 statute digests** in `_statute_corpus/` — ACL (Competition and Consumer Act) · Corporations Act 2001 · Fair Work Act 2009 · Family Law Act 1975 · Privacy Act 1988 + APP · Federal Court of Australia Act 1976 · Evidence Act (Cth + NSW) · LPUL (Legal Profession Uniform Law) · Australian Contract Law (common-law digest) · Bankruptcy Act 1966 · Migration Act 1958 · AML/CTF Act 2006 + 2024 Amendment · PPS Act 2009. Plus 39 research files in `_research/` traced via PROVENANCE headers.
- **v0.1.1 — Pseudonymisation Gateway** *(shipped 2026-05-29)* — internalised at `ailawfirm_australia/pseudonymisation.py`; sanitises PII before any cloud-LLM call. Standalone source at [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway).
- **v0.2 — frontend / UX layer** *(in progress)* — remaining Tier-2 statute depth (Solicitors' Conduct Rules · My Health Records Act) · Tranche 2 AML reporting helper · matter dashboard
- **v0.3** *(following milestone)* — **ILP firm mode** for Incorporated Legal Practices · Legal Practitioner Director compliance · multi-lawyer · conflict-check · trust-account compliance · Essential Eight cybersecurity assessment tool
- **v0.4+** — AustLII / Federal Register / state-specific case-law direct lookup · Apple EventKit native · CalDAV bidirectional sync · per-state procedural depth (NSW · VIC · QLD · WA · SA · TAS · ACT · NT) · ART case-management workflow · Native Title forms · admiralty · construction Security of Payment Acts · IP licensing

Six sister jurisdictions on the same architecture: 🇮🇳 India · 🇸🇬 Singapore · 🇬🇧 UK · 🇦🇪 Dubai-DIFC · 🇪🇺 EU · 🇺🇸 USA — each as its own MIT-licensed repo.

---

## 🌐 Family Status (honest · cross-firm)

The wolfgang_rush AI Brain family ships across 7 jurisdictions. Honest status of the v0.2 legal-knowledge layer (statute corpus + drafting data) per firm:

| Firm | Statute corpus | Drafting corpus | Shared agents | GitHub |
|------|---|---|---|---|
| 🇮🇳 **India** | Native knowledge base · maintainer-curated | wolfgang_rush plugins (14 Indian-litigation plugins · separate stack) | Not applicable — Indian-specific | ✅ LIVE |
| 🇪🇺 **EU** | ✅ 11 statutes · 8/8 Tier-1 | ✅ **56 templates** · litigation + commercial complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇺 **Australia** | ✅ 13 Tier-1 statute digests + 39 research files | ✅ **79 templates** · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇪 **Dubai-DIFC** | ✅ 24 statute digests · dual-track (15 DIFC + 9 Mainland UAE Federal) · v0.2 closed 2026-05-29 | ✅ **81 templates** · dual-track DIFC + Mainland · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇸🇬 **Singapore** | ✅ 17 statute digests Tier-1 | ✅ **55 templates + 6 scaffolds** · litigation + commercial + regulatory complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇬🇧 **UK** | ✅ 10 statute digests Tier-1 | ✅ **107 templates** · litigation + commercial + Tier-3 specialist + procedural anchors complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇺🇸 **USA** | ✅ 23 federal-first Tier-1 statute digests | ✅ **89 templates** · all 13 litigation categories + commercial + corporate complete (v0.2 closed 2026-05-29) | ✅ Migrated | ✅ LIVE |

**Plus:**
- **AI Startup Firm — India v0.1** (legal-ops brain for founders)
- **GC In-House Brain** (multi-jurisdictional, 8 modules — 3 live · 5 shipping v0.2+)

Both share the same `drafting-agents-core` architecture pattern.

All firms migrated to the central [drafting-agents-core](https://github.com/Wolfgangrush/drafting-agents-core) agent library on 2026-05-20 (Path B-Lite) — single source of truth for the agent layer; jurisdictional knowledge stays per-firm.

---

## 📚 Documentation

| File | What it covers |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) + 3 language variants | Layman-friendly 30-minute tour |
| [DISCLAIMER.md](DISCLAIMER.md) | Full legal disclaimer · LPUL conduct rules · Privacy Act / APP framework · UPL exclusion · cross-border |
| [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) | Zero-collection architecture · Privacy Act 1988 / APP controller analysis · APP 8 cross-border · Section 77 health-data |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting · coordinated disclosure · Essential Eight alignment notes |
| [MODEL_SETUP.md](MODEL_SETUP.md) | Honest privacy table · local vs cloud · third-party CLI tool warning |
| [SCOPE.md](SCOPE.md) | What's in v0.1, what's not, falsification rules |
| [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) | Every domain claim's source (CITED:<research-file>) |
| [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) | Community call for native-speaker translation PRs |

---

## 🙏 Credits

- **Engine — all architectural credit:** [MemPalace](https://github.com/MemPalace/mempalace) — the highest-scoring open-source AI memory system ever benchmarked (96.6% LongMemEval R@5), MIT-licensed. Downstream fork of MemPalace 3.0.0. All architectural credit to the MemPalace Contributors.
- **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). MIT-licensed legal-tech publisher.
- **Inspired by:** every Australian solo who's worked Sunday night on an ART hearing brief due Tuesday — across state lines, in two languages, with a Tranche 2 KYC pile on the side.

---

## ⚠️ Disclaimer

This tool helps you organize your practice. It does **NOT** give legal advice. It does **NOT** replace your professional judgment. It does **NOT** solicit work on your behalf. LPUL Solicitors' Conduct Rule 36 publicity firewall is built in but **YOU** remain responsible for compliance with all bar conduct rules, Privacy Act 1988 / APP framework, AML/CTF obligations (Tranche 2 from July 2026), Section 77 My Health Records prohibition, and any Law Council / state-bar advisory on AI tool use.

The publisher is not admitted in any Australian jurisdiction. The publisher does not offer legal services in Australia. This is a software publication under the MIT License.

Ships AS-IS without warranty. See [LICENSE](LICENSE).

---

## 📞 Support

- **Issues / bugs:** https://github.com/Wolfgangrush/ai-law-firm-australia/issues
- **Translation help:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) (Mandarin · Vietnamese · Arabic native-PRs welcome)
- **State-specific feature?** Open an issue with `[state-NSW]` / `[state-VIC]` / etc. label
- **Federal feature?** Open an issue with `[federal]` label

---

`Let's begin. G'day. 让我们开始. Hãy bắt đầu. لنبدأ.` 🙏
