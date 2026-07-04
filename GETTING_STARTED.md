# Getting Started — AI Brain for Australia Lawyers · v0.1

**For qualified legal professionals only.** See [DISCLAIMER.md](DISCLAIMER.md).

## 1. Prerequisites

- **Python 3.10+** — check with `python3 --version`
- **pip** — check with `python3 -m pip --version`
- **Ollama** (recommended for client work) — see [MODEL_SETUP.md](MODEL_SETUP.md)

## 2. Install

```bash
cd ~/ai-law-firm-australia/
pip install -e .
```

Verify:
```bash
ailawfirm-australia --version
```

You should see the multi-language welcome banner:
```
═══════════════════════════════════════════════════════════════════
  AI Brain for Australia Lawyers · v0.1
  G'day · 你好 · Xin chào · مرحبا
═══════════════════════════════════════════════════════════════════
```

## 3. Set up local AI (recommended for client work)

See [MODEL_SETUP.md](MODEL_SETUP.md) for the full honest privacy guide.

Quick setup:
```bash
# Install Ollama
brew install ollama       # Mac
# or download from https://ollama.com

# Download a model (one-time, ~10-20 min, ~10 GB)
ollama pull qwen3:14b
```

The tool is configured for local AI by default. No cloud accounts needed.

## 4. Connect to MCP client

### Claude Code

```bash
claude mcp add ailawfirm-australia -- python ~/ai-law-firm-australia/ailawfirm_australia/mcp_server.py
```

### Cursor / other MCP clients

Add to your MCP config:
```json
{
  "mcpServers": {
    "ailawfirm-australia": {
      "command": "python",
      "args": ["~/ai-law-firm-australia/ailawfirm_australia/mcp_server.py"]
    }
  }
}
```

## 5. First operations

### Court lookup
Try the `australia_court_lookup` MCP tool:
```
> Look up the High Court of Australia
> What courts are in VIC?
> Show me ART details
```

### Citation validation
Try the `australia_citation_validator` MCP tool:
```
> Validate: [2024] FCAFC 100
> Parse: (2023) 97 ALJR 100
> Check: [2023] HCA 12
```

### Calendar sync
Try the `australia_calendar_sync` MCP tool:
```
> Schedule directions hearing on 2026-06-15 at 10am Sydney time
> Create ICS for Federal Court mention on 2026-07-01 9:30am Melbourne
```

## 6. What's next

- Read [SCOPE.md](SCOPE.md) — what's in v0.1, what's coming
- Read [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) — where every domain claim comes from
- Read [SECURITY.md](SECURITY.md) — reporting vulnerabilities
- Read [CONTRIBUTING.md](CONTRIBUTING.md) — PR and contribution guidelines

## 7. Language support

- 简体中文 — [GETTING_STARTED_CHINESE.md](GETTING_STARTED_CHINESE.md)
- Tiếng Việt — [GETTING_STARTED_VIETNAMESE.md](GETTING_STARTED_VIETNAMESE.md)
- العربية — [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md)

Help improve AI-assisted translations: [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md)

---

Built from MemPalace 3.0.0 (MIT). Published by wolfgang_rush (High Courts of India).
