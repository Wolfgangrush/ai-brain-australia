# NO_PII_NO_DATA — Zero-Collection Architecture (Australia)

**This document explains, in detail, why AI Brain — Australia collects no personal information from you, and what that means under the Privacy Act 1988 (Cth) and Australian Privacy Principles.**

## The short version

The publisher (wolfgang_rush) operates **zero infrastructure** that touches your data. There is no server. There is no telemetry. There is no analytics. There is no "anonymous usage improvement data." The tool runs entirely on your laptop.

## The architectural guarantee

AI Brain — Australia is **local-first** software. Specifically:

**(1) The codebase contains zero telemetry.** Verify with `grep -ri "telemetry\|analytics\|tracking\|requests.post\|urlopen" ailawfirm_australia/` — should return only legitimate cloud-AI calls (user-initiated, routed direct to your chosen vendor).

**(2) The publisher operates no server.** No AI Brain Australia API. No cloud service. No database. The publisher's only infrastructure is the GitHub repository.

**(3) Storage is on your laptop.** Your matter data, citation cache, calendar entries, and configuration live under `~/.ailawfirm-australia/`. The publisher has no access to this folder.

**(4) Network calls are limited to:**
- Package installation (PyPI during `pip install`)
- User-initiated AI cloud calls (if you opt into cloud mode — direct to vendor, not through publisher)
- Optional update checks (v0.2+ if added — will be opt-in and check GitHub releases only)

## Cloud-mode (when you opt in)

If you choose to use cloud AI processing, your queries route **directly from your laptop to the AI vendor**. The publisher is not in the data path. The contract for cloud-mode usage is between **you** and the **AI vendor** under their terms of service.

For client-confidential work, do NOT use cloud mode. Use the local-only mode. See [MODEL_SETUP.md](MODEL_SETUP.md).

## Privacy Act 1988 implications

Under the Privacy Act 1988 (Cth) and the Australian Privacy Principles (APPs):

**The publisher is NOT an APP entity.** An APP entity "collects, holds, uses or discloses personal information" (APP entities include most Australian government agencies and private sector organisations with annual turnover exceeding $3 million). The publisher is an Indian individual publishing open-source software — neither an Australian government agency nor an Australian private-sector organisation.

**The publisher is NOT a data controller or processor.** The publisher determines neither the purposes of processing nor processes any data on anyone's behalf. The publisher's activity is software publication, not data handling.

**The publisher is a software publisher.** Publishing open-source software does not constitute "collecting," "holding," "using," or "disclosing" personal information under APP 3-8. It is a publication activity governed by intellectual property law (Copyright Act 1968), not privacy law.

If you use the tool to process personal information of your clients, **you** are the APP entity for that processing. Your Privacy Act 1988 obligations apply:
- APP 1 — Open and transparent management of personal information (privacy policy)
- APP 2 — Anonymity and pseudonymity
- APP 3 — Collection of solicited personal information (by lawful and fair means)
- APP 4 — Dealing with unsolicited personal information
- APP 6 — Use or disclosure (primary purpose only)
- APP 8 — Cross-border disclosure (see below)
- APP 11 — Security of personal information
- APP 12 — Access to personal information
- APP 13 — Correction of personal information
- Notifiable Data Breaches (NDB) scheme (Part IIIC — notify OAIC + affected individuals within 30 days)

## APP 8 — Cross-border disclosure deemed liability

**This is a critical risk for Australian practitioners using cloud AI.**

APP 8.1 provides that an APP entity that discloses personal information to an overseas recipient must take "reasonable steps" to ensure the overseas recipient does not breach the APPs. APP 8 provides an **accountability mechanism** (sometimes called "deemed liability"): the Australian disclosing entity remains liable under the Privacy Act for the overseas recipient's acts or practices that would breach the APPs.

**Practical consequence:** If you use cloud AI (DeepSeek servers in China · Anthropic servers in USA · Google servers globally) with client personal information, and that overseas vendor suffers a data breach, **you** may be deemed liable under APP 8 for that breach. APP 8 does not just require "reasonable steps" — it imposes direct accountability for the overseas recipient's breach.

**Mitigation:** The local-only default (Ollama + Qwen3) keeps all PI processing on your laptop within Australia. APP 8 cross-border obligations are not triggered because there is no overseas disclosure.

## Section 77 My Health Records Act 2012 — Health data localisation

Section 77 of the My Health Records Act 2012 strictly prohibits the handling of My Health Record data outside Australia. This is a **hard prohibition**, not a "reasonable steps" obligation.

**If you handle My Health Record data or health information subject to this Act:**
- Cloud AI with any offshore vendor is **unlawful**, not merely risky.
- Local-only AI (Ollama on your laptop in Australia) is the ONLY compliant option.
- APP framework alone is insufficient for health data — Section 77 is the gold standard and imposes absolute geographic restrictions.

## APRA CPS 230 — Material service providers (advisory)

APRA CPS 230 (effective July 2025) expands the definition of "material service providers" for APRA-regulated entities. If your practice serves APRA-regulated clients (banks · insurers · superannuation funds), cloud AI vendors may be classified as material service providers under CPS 230, requiring your client to assess and manage the outsourcing risk. This is your client's obligation, not yours — but awareness is prudent.

## Verification path

You can independently verify zero-collection:

1. `grep -ri "telemetry\|analytics\|posthog\|mixpanel\|segment\|amplitude\|google-analytics\|datadog\|sentry" ailawfirm_australia/` — should return zero results.
2. `cat requirements.txt` — no analytics or telemetry libraries.
3. Run the tool offline — should work fully (cloud-AI calls will fail, which is expected and visible).
4. Inspect network traffic with `nettop` (macOS) / `nethogs` (Linux) — should show traffic only to user-initiated cloud-AI endpoints if cloud mode is on.

## If this changes

If a future version adds telemetry, opt-in update checks, or any cloud touchpoint involving the publisher's infrastructure, that change will be:
- Announced in CHANGELOG
- Default OFF · user-opt-in only
- Documented in this file with the change date and specific data category

This file always represents the current state. If it differs from the code, the code is the truth — file an issue.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §2(b) (Zero Data Collection pillar), §3.V4 (Data Protection — Privacy Act 1988 + APP 8 + Section 77 My Health Records), §3.V9 (Conduct-Rule Inducement — LPUCSR Rule 9). Playbook version: v0.1.*
