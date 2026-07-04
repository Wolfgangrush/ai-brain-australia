# 入门指南 — AI 律师事务所 · 澳大利亚 · 独立执业版 · v0.1

> ⚠️ AI辅助翻译 · 母语者欢迎通过 PR 完善 · 请参阅 TRANSLATION_HELP_WANTED.md

**仅供合格法律专业人士使用。** 详见 [DISCLAIMER.md](DISCLAIMER.md)。

## 1. 环境要求

- **Python 3.10+** — 用 `python3 --version` 检查
- **pip** — 用 `python3 -m pip --version` 检查
- **Ollama**（推荐用于客户工作）— 详见 [MODEL_SETUP.md](MODEL_SETUP.md)

## 2. 安装

```bash
cd ~/ai-law-firm-australia/
pip install -e .
```

验证：
```bash
ailawfirm-australia --version
```

您将看到多语言欢迎横幅（英文 · 中文 · 越南文 · 阿拉伯文）。

## 3. 设置本地 AI（推荐用于客户工作）

详见 [MODEL_SETUP.md](MODEL_SETUP.md) 获取完整的隐私指南。

快速设置：
```bash
# 安装 Ollama
brew install ollama       # Mac
# 或从 https://ollama.com 下载

# 下载模型（一次性，约 10-20 分钟，约 10 GB）
ollama pull qwen3:14b
```

该工具默认配置为本地 AI。不需要云账号。

## 4. 连接到 MCP 客户端

### Claude Code

```bash
claude mcp add ailawfirm-australia -- python ~/ai-law-firm-australia/ailawfirm_australia/mcp_server.py
```

### Cursor / 其他 MCP 客户端

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

## 5. 首次操作

### 法院查询
使用 `australia_court_lookup` MCP 工具：
- 查询澳大利亚高等法院
- VIC 州有哪些法院？
- 显示 ART（行政复审法庭）详情

### 引文验证
使用 `australia_citation_validator` MCP 工具：
- 验证 [2024] FCAFC 100
- 解析 (2023) 97 ALJR 100

### 日历同步
使用 `australia_calendar_sync` MCP 工具：
- 安排在 2026 年 6 月 15 日上午 10 点（悉尼时间）的指示聆讯

## 6. 重要合规提示

- **LPUCSR 规则 9（保密）：** 客户数据只能使用本地 AI。不要将客户资料上传到云端 AI。
- **APP 8（跨境责任）：** 向海外供应商传输个人信息会使您承担责任。
- **第 77 条（My Health Records 法）：** 严禁在海外处理健康数据。
- **Tranche 2 AML（2026年7月生效）：** 律师将被纳入反洗钱报告范围。

## 7. 语言支持

- English — [GETTING_STARTED.md](GETTING_STARTED.md)（权威版本）
- Tiếng Việt — [GETTING_STARTED_VIETNAMESE.md](GETTING_STARTED_VIETNAMESE.md)
- العربية — [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md)

帮助改进 AI 辅助翻译：[TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md)

---

基于 MemPalace 3.0.0 (MIT)。由 wolfgang_rush 发布（印度孟买高等法院那格浦尔法庭）。
