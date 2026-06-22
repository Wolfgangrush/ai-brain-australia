---
name: retrospective
description: End-of-session save discipline for Australia AI Brain users. Runs 2-pass leak-check (Rule 6: no internal-shorthand, no internal-paths, no personal-build references). Saves session learning so the firm gets smarter with every use.
allowed-tools: Bash, Read, Glob
---

# /retrospective — End-of-Session Save Discipline (Australia)

Saves what the Australia AI Brain learned this session. Runs at session end. The firm accumulates knowledge across sessions without leaking personal context.

## 2-Pass Leak-Check (Rule 6 — execute BEFORE any save)

### Pass 1 — Internal-shorthand codes + the local memory layer paths
```bash
# Detect any 2-5 letter all-caps token (potential internal matter shorthand / entity-aliasing entity code)
grep -rniE '\b[A-Z]{2,5}\b' --include="*.md" --include="*.json" --include="*.txt" . 2>/dev/null \
  | grep -vE '\b(AAS|ABN|ACL|ACT|ADR|AFP|AGD|AGLC|AGS|AHRC|AML|APP|APRA|ART|ASIC|ASIO|AUD|AUSTRAC|BSA|CAC|CCA|CDC|CEO|CFO|CGT|CIO|COI|CPD|CPS|CTF|DPP|DPRO|DV|EOC|EPA|FCA|FCFCOA|FOI|FWC|FWO|GST|HCA|ICAC|ICO|IT|JSON|LACC|LIV|LPL|LPUCSR|LPUL|MD|MHRA|NDIS|NSW|NSWCA|NSWSC|NT|OAIC|OECD|PI|PII|PIN|QBE|QC|QCAT|QLD|RIA|SA|SC|SCA|SLA|SME|TAS|TFN|TPB|UNSW|US|VIC|VCAT|VCAA|VIC|VLSB|WA|WACA)\b'
# Detect references to user-home dot-directories (potential machine-internal paths)
grep -rniE '~/\.[a-z]+/' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = STOP. Do not save. Flag for manual review.

Note: the inner exclusion list whitelists common Australian-legal acronyms so the leak-detector doesn't false-positive on legitimate jurisdiction shorthand. Extend the whitelist as your firm encounters new domain acronyms.

### Pass 2 — External architecture references + personal-vs-business markers
```bash
# Detect references to external project-architecture names (extend this regex with your firm's internal terms)
grep -rniE 'YOUR_INTERNAL_ARCHITECTURE_PATTERN_HERE' --include="*.md" --include="*.json" . 2>/dev/null
# Detect personal-build references (extend with your firm's specific personal-vs-business markers if any)
grep -rniE 'YOUR_PERSONAL_VS_BUSINESS_MARKER_HERE' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = STOP.

## Workflow

### Step 1: Collect session summary
Review the current conversation for:
- Which specialists were invoked (Receptionist, Matter Manager, Citation Clerk, Court Registrar, Drafting Assistant, Compliance Officer, Deadline Tracker)
- What legal domains were touched (LPUL, AML/CTF Tranche 2, My Health Records, corporations law, privacy, migration, family, criminal, civil procedure)
- What courts or jurisdictions were referenced (High Court of Australia, Federal Court, FCFCOA, state Supreme Courts, ART)
- Any errors or blockers encountered

### Step 2: Run 2-pass leak-check (above)

### Step 3: If passes leak-check, write session summary
Save to `.ailawfirm-australia/sessions/` with timestamp. Format:
```markdown
# Session — YYYY-MM-DD HH:MM
- Specialists used: [list]
- Domains: [list]
- Courts: [list]
- Key outcomes: [brief]
- Leak-check: PASS (2-pass, Rule 6)
```

### Step 4: Display save confirmation
```
🧠 Australia AI Brain — session saved.
   Leak-check: ✅ PASS (Pass 1: 0 shorthand, 0 paths | Pass 2: 0 personal-build)
   Next session starts smarter.
```

## Output Format
```markdown
## /retrospective — Australia AI Brain · Session Save

**Session:** YYYY-MM-DD HH:MM
**Specialists active:** [N]
**Domains touched:** [list]
**Leak-check:** ✅ PASS / ❌ BLOCKED

[If PASS: "Session learning saved. Firm knowledge base updated."]
[If BLOCKED: "Leak detected. Session NOT saved. Review flagged content above."]
```

## Anti-Pollution Rules (DO NOT BREAK)
- Never reference user-home dot-directories or absolute paths from a developer's machine
- Never use internal entity codes, matter shorthand, or non-Australian-context identifiers
- Never reference external project-architecture names not tied to this firm
- Never reference the publisher's personal builds, personal-vs-business markers, or personal handles
- The publisher credit line in README.md is the sole exception — it is public-facing attribution, not a leak

## What this skill does NOT do
- Does NOT read or write to the local memory layer
- Does NOT access personal diary, KG, or self-assessment data
- Does NOT touch any other firm's directory
- Does NOT auto-save without passing leak-check
