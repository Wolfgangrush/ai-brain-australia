---
name: wake
description: Start-of-session state loader for Australia AI Brain users. Runs 2-pass leak-check (Rule 1: same scope as retrospective — no internal-shorthand, no internal-paths, no personal-build references). Loads jurisdiction context so every session begins informed.
allowed-tools: Bash, Read, Glob
---

# /wake — Start-of-Session State Loader (Australia)

Loads the Australia AI Brain's current state at session start. Displays readiness so the user knows exactly what's available before they begin work.

## 2-Pass Leak-Check (Rule 1 — execute FIRST, before displaying state)

### Pass 1 — Internal-shorthand codes + MemPalace paths
```bash
# Detect any 2-5 letter all-caps token (potential internal matter shorthand / entity-aliasing entity code)
grep -rniE '\b[A-Z]{2,5}\b' --include="*.md" --include="*.json" --include="*.txt" . 2>/dev/null \
  | grep -vE '\b(AAS|ABN|ACL|ACT|ADR|AFP|AGD|AGLC|AGS|AHRC|AML|APP|APRA|ART|ASIC|ASIO|AUD|AUSTRAC|BSA|CAC|CCA|CDC|CEO|CFO|CGT|CIO|COI|CPD|CPS|CTF|DPP|DPRO|DV|EOC|EPA|FCA|FCFCOA|FOI|FWC|FWO|GST|HCA|ICAC|ICO|IT|JSON|LACC|LIV|LPL|LPUCSR|LPUL|MD|MHRA|NDIS|NSW|NSWCA|NSWSC|NT|OAIC|OECD|PI|PII|PIN|QBE|QC|QCAT|QLD|RIA|SA|SC|SCA|SLA|SME|TAS|TFN|TPB|UNSW|US|VIC|VCAT|VCAA|VIC|VLSB|WA|WACA)\b'
# Detect references to user-home dot-directories (potential machine-internal paths)
grep -rniE '~/\.[a-z]+/' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = flag immediately. Do not proceed silently.

Note: the inner exclusion list whitelists common Australian-legal acronyms so the leak-detector doesn't false-positive on legitimate jurisdiction shorthand. Extend the whitelist as your firm encounters new domain acronyms.

### Pass 2 — External architecture references + personal-vs-business markers
```bash
# Detect references to external project-architecture names (extend this regex with your firm's internal terms)
grep -rniE 'YOUR_INTERNAL_ARCHITECTURE_PATTERN_HERE' --include="*.md" --include="*.json" . 2>/dev/null
# Detect personal-build references (extend with your firm's specific personal-vs-business markers if any)
grep -rniE 'YOUR_PERSONAL_VS_BUSINESS_MARKER_HERE' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = flag immediately.

## Workflow

### Step 1: Run 2-pass leak-check (above)
If either pass fails, display warning before proceeding.

### Step 2: System state check
```bash
echo "Python: $(python3 --version 2>&1)"
echo "Package: $(pip show ailawfirm_australia 2>&1 | head -3)"
echo "Data dir: $(ls -la ~/.ailawfirm-australia/ 2>&1 | head -5)"
echo "Config: $(cat ~/.ailawfirm-australia/config.json 2>&1 | head -10)"
```

### Step 3: Jurisdiction context
Display the Australia-specific legal framework:
- **High Court of Australia** + **Federal Court of Australia** + **Federal Circuit and Family Court of Australia** + **8 state/territory Supreme Courts**
- **Statutes:** LPUL (NSW · VIC), Tranche 2 AML/CTF Amendment Act 2024, My Health Records Act 2012 (s 77), Evidence Act 1995 (Cth), Corporations Act 2001 (Cth), Privacy Act 1988 (Cth)
- **Tribunals:** ART (Administrative Review Tribunal, post-Oct 2024), AAT (legacy matters)
- **Regulatory:** APRA CPS 230 (July 2025), OAIC, AUSTRAC

### Step 4: Specialists available
| # | Specialist | Status |
|---|---|---|
| 🧠 | Receptionist (brain) | READY |
| 📂 | Matter Manager | READY |
| 📜 | Citation Clerk | READY |
| 🏛️ | Court Registrar | READY |
| ✍️ | Drafting Assistant | READY |
| 🛡️ | Compliance Officer | READY |
| 📅 | Deadline Tracker | READY |

### Step 5: Present readiness summary

## Output Format

```markdown
## 🇦🇺 Australia AI Brain — Ready

🟢 Leak-check: PASS (Pass 1 clean · Pass 2 clean)

**System:**
- Python: [version]
- Package: ailawfirm_australia [version]
- Data: ~/.ailawfirm-australia/ [status]

**7 specialists online.**
**High Court + Federal Court + FCFCOA + 8 Supreme Courts mapped.**
**LPUL · Tranche 2 AML · My Health Records Act loaded.**

🧠 This firm LEARNS. Every session makes the next one smarter.
   Run `/retrospective` at session end to save what you learned.

---
What do you need today?
```

## Anti-Pollution Rules (DO NOT BREAK)
- Never reference user-home dot-directories or absolute paths from a developer's machine
- Never use internal entity codes
- Never reference external project-architecture names not tied to this firm
- Never reference the publisher's personal builds or personal-vs-business markers

## What this skill does NOT do
- Does NOT read or write to MemPalace
- Does NOT access personal diary or KG
- Does NOT touch any other firm's directory
- Does NOT modify any file (read-only state display)
