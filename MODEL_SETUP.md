# AI Model Setup — Honest Privacy Guide (Australia)

The tool itself stores everything on your laptop. But to do "smart" work (drafting, conversation, reasoning) you connect it to an AI model. **Where that model runs determines your privacy — and your APP 8 liability.**

This guide is honest about every option. No marketing fluff. Read before you pick.

> **Getting-started in other languages:**
> English ([GETTING_STARTED.md](GETTING_STARTED.md)) · 中文 ([GETTING_STARTED_CHINESE.md](GETTING_STARTED_CHINESE.md)) · Tiếng Việt ([GETTING_STARTED_VIETNAMESE.md](GETTING_STARTED_VIETNAMESE.md)) · العربية ([GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md))

---

## The honest privacy table

| Option | Where it runs | Who can see your queries | Cost | Best for |
|---|---|---|---|---|
| **Ollama + Qwen3 (local)** | Your laptop | ONLY you | $0 forever | **Client matters · APP 8 compliance · Health data (Section 77) · Court drafts** |
| **DeepSeek API** | DeepSeek servers (China) | DeepSeek (unless opted-out) | ~AUD 3-15/mo moderate use | NON-client work · drafting templates · research summaries |
| **Claude API** | Anthropic servers (USA) | Anthropic (per their privacy policy) | ~AUD 30-100/mo | Heavy daily users after first paid engagement |
| **Gemini API** | Google servers (USA + globally) | Google | ~AUD 10-40/mo | Long-PDF reads · large research synthesis |

## Option A — Ollama + Qwen3 (local, recommended for client work)

### Why this is the best privacy option
- Model runs ON YOUR LAPTOP. Your queries never leave the machine.
- No internet needed after one-time model download.
- No Privacy Act 1988 / APP concern about third-party data processing.
- No APP 8 cross-border deemed-liability risk.
- **No Section 77 My Health Records Act breach risk** — health data stays on your Australian-located laptop.
- Suitable for handling actual client matters, drafting, confidential research.

### Install
**Mac:** `brew install ollama` (or download from https://ollama.com/download/Mac)
**Windows:** Download installer from https://ollama.com/download
**Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

### Download a model (one-time, 10-20 minutes, ~10 GB)
```
ollama pull qwen3:14b
```

Alternative models if you have less storage:
- `ollama pull qwen3:7b` — 4 GB · slightly worse quality, faster
- `ollama pull llama3.3:8b` — 5 GB · Meta's model, decent
- `ollama pull mistral:7b` — 4 GB · good European model

### Connect to AI Brain Australia
Open `~/.ailawfirm-australia/config.json` (Mac) or `C:\Users\YourName\.ailawfirm-australia\config.json` (Windows) and add:

```json
{
  "ai_provider": "ollama",
  "ollama_model": "qwen3:14b",
  "ollama_host": "http://localhost:11434"
}
```

Restart `ailawfirm-australia`. It now uses local Ollama. **No queries leave your laptop.**

### Tradeoffs (honest)
- Slower than cloud APIs (maybe 2-5x slower depending on your laptop)
- Quality is slightly lower than top cloud models (but improving rapidly)
- Uses laptop battery + RAM during use
- Best on machines with 16 GB+ RAM (will work on 8 GB but tightly)

### Hardware reality check
- MacBook Air M1/M2 8GB: works with `qwen3:7b` (smaller model)
- MacBook Air M2/M3 16GB+: works smoothly with `qwen3:14b`
- Windows laptop with 16GB RAM + dedicated GPU: works well with `qwen3:14b`
- Older Windows laptops (4-8GB RAM, no GPU): use `qwen3:7b` or smaller
- Phone/tablet: not supported for local model (use Option B/C/D)

---

## Option B — DeepSeek API (cheap cloud, MANDATORY privacy setup)

### Why solo practitioners like DeepSeek
- **Cheapest** capable cloud model right now (~10-20x cheaper than Claude/GPT)
- Anthropic-compatible API (works with Claude Code and similar tools out of the box)
- Strong on agentic / tool-use workloads

### ⚠️ APP 8 — Cross-border deemed liability (READ BEFORE USING)

DeepSeek operates servers in **China**. Under APP 8 of the Privacy Act 1988, if you disclose client personal information to DeepSeek's Chinese servers, you are **deemed liable** for any APP breach that occurs on those servers (including unauthorised access · data breach · secondary use). This is NOT a "reasonable steps" safe harbour — APP 8 is a statutory accountability mechanism.

**Plus DeepSeek's own privacy policy:** they may use API inputs and outputs for service improvement (training). They offer an opt-out, but it is NOT the default.

**Per DeepSeek's official policy:**
> *"DeepSeek may use inputs and outputs to a minimal extent to develop or improve services under secure encryption technology processing, strict de-identification rendering, and with irreversibility to identify specific individuals."*

> *"Users can disable the option labeled 'Improve the model for everyone' to reduce the likelihood that their chats will end up in DeepSeek's training datasets."*

### MANDATORY setup before using DeepSeek with any data

1. Sign up at https://platform.deepseek.com
2. Top up USD 10-20 (~AUD 15-30)
3. **Go to Settings → Privacy → toggle OFF "Improve the model for everyone"** — this is the opt-out
4. Settings → API Keys → Create New Key → copy the `sk-...` string immediately
5. **Verify the opt-out by reloading the page** — it must show OFF

### Connect to AI Brain Australia

Add to `~/.ailawfirm-australia/config.json`:

```json
{
  "ai_provider": "anthropic-compatible",
  "base_url": "https://api.deepseek.com/anthropic",
  "api_key": "sk-YOUR-DEEPSEEK-KEY-HERE",
  "model": "deepseek-v4-pro"
}
```

### What's safe to use DeepSeek for (even with opt-out)

✅ Safe:
- Legal research summaries (you provide the source, DeepSeek summarizes)
- Drafting templates (general structure, no client facts)
- Privacy Act / LPUL study sessions (learning the law, not applying it to a client)
- General writing assistance (your LinkedIn post, your blog)

❌ NOT safe (use Option A instead):
- Actual client matter drafts (names, facts, prayers)
- Confidential communications
- **Any health-related data (Section 77 My Health Records Act — strict offshore prohibition)**
- Strategy discussions involving real opposing parties
- Anything covered by legal professional privilege

### Cost reality
- ~AUD 1.50-5 per heavy day
- Light personal use: AUD 0.30-1/day
- USD 10 lasts most users 4-8 weeks

---

## Option C — Claude API (Anthropic)

### Why use it
- Top-tier quality (top-tier reasoning quality for complex research workflows)
- Anthropic's privacy posture is strong (they explicitly state API inputs are NOT used for training unless you opt in)
- Long context (200K-1M tokens — can ingest full case files)

### ⚠️ APP 8 cross-border note
Anthropic servers are in the **USA**. APP 8 cross-border deemed-liability applies. Unlike DeepSeek, Anthropic's default privacy posture (no training on API data) provides a stronger "reasonable steps" argument. However, the APP 8 accountability mechanism still applies — you remain liable for any APP breach on Anthropic's servers.

### Privacy fact
Per Anthropic's policy: **API customer data is NOT used to train models by default.** This is the inverse of DeepSeek — privacy is default-on.

### Setup
1. Sign up at https://console.anthropic.com
2. Add billing · top up USD 20-50 (~AUD 30-75)
3. API Keys → Create → copy `sk-ant-...`

### Connect
```json
{
  "ai_provider": "anthropic",
  "api_key": "sk-ant-YOUR-KEY-HERE",
  "model": "claude-opus-4-7"
}
```

### Cost reality
- Heavy daily use: USD 30-150/month (~AUD 45-225/month)
- Light personal use: USD 5-20/month (~AUD 8-30/month)

### When this makes sense
- You're billing >AUD 60,000/year and the tool is doing >5hr/week of real work for you
- You handle complex matters where the model's reasoning quality matters

---

## Option D — Gemini API (Google)

### Why use it
- Largest context (1M-2M tokens · Gemini 3.1 Pro)
- Cheaper than Claude
- Excellent for long-PDF reading + research synthesis

### ⚠️ APP 8 cross-border note
Google servers are **globally distributed**. APP 8 cross-border deemed-liability applies. Ensure you're on the PAID tier (not free tier — free tier may use prompts for training).

### Privacy fact
Per Google AI Studio terms: **paid API tier (Gemini API with billing) does NOT use prompts for training.** Free tier DOES.

**Critical:** ensure you're on the PAID tier before using Gemini for any data.

### Setup
1. Sign up at https://aistudio.google.com
2. Set up billing (paid tier, not free)
3. Get API key

### Connect
```json
{
  "ai_provider": "google-gemini",
  "api_key": "AIza-YOUR-KEY-HERE",
  "model": "gemini-3.1-pro"
}
```

---

## The right answer for most Australian solo practitioners

**Use a hybrid:**
- **Local Ollama (Option A)** for everything involving actual client matter data + **mandatory for any health-related data**
- **DeepSeek API with opt-out (Option B)** for drafting templates, study, generic writing
- Switch by editing one line in `~/.ailawfirm-australia/config.json`

**Decision rule:** if the query mentions a real client name, real facts, or anything that could be construed as subject to legal professional privilege → use Ollama. For health-related personal information, Ollama is the ONLY lawful option (Section 77).

---

## Pro tip: rotate API keys quarterly

For any cloud API (DeepSeek · Claude · Gemini):
1. Create a new API key from the provider's dashboard
2. Replace the old one in `config.json`
3. Delete the old key from the provider's dashboard

Why: if your `config.json` ever leaks (laptop stolen, accidental git commit, etc.), the old key is dead. Standard infosec hygiene.

---

## Troubleshooting

### "API key invalid"
- Double-check you copied the full key (including the `sk-` prefix for DeepSeek/Claude, `AIza` for Gemini)
- Confirm billing is active on the provider's dashboard
- Check the key wasn't deleted

### "Connection timed out"
- Cloud APIs need internet
- Check if your office firewall blocks the API URL (corporate networks often do)
- Try from your phone's hotspot to isolate

### "Model not found"
- Model names change. Check the provider's current model list:
  - DeepSeek: https://api-docs.deepseek.com
  - Anthropic: https://docs.anthropic.com/en/docs/models-overview
  - Gemini: https://ai.google.dev/gemini-api/docs/models

### Ollama is slow
- Use a smaller model: `ollama pull qwen3:7b`
- Close other apps to free up RAM
- On Mac, check Activity Monitor → Memory tab; if pressure is yellow/red, you need a smaller model

---

## Sources

- [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)
- [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms)
- [Google AI Studio Terms](https://ai.google.dev/gemini-api/terms)
- [OAIC — APP 8 Cross-border disclosure](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-8-app-8-cross-border-disclosure-of-personal-information)
- [My Health Records Act 2012 — Section 77](https://www.legislation.gov.au/C2012A00063)
- [ASD Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cybersecurity/essential-eight)

---

**Last verified:** 2026-05-18. AI provider terms change. Re-verify before relying on any privacy claim for client work.
