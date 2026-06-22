# Hướng dẫn Bắt đầu — AI Brain · Úc · Phiên bản Hành nghề Độc lập · v0.1

> ⚠️ Dịch hỗ trợ AI · Hoan nghênh người bản xứ cải thiện qua PR · Xem TRANSLATION_HELP_WANTED.md

**Chỉ dành cho chuyên gia pháp lý có chứng chỉ hành nghề.** Xem [DISCLAIMER.md](DISCLAIMER.md).

## 1. Yêu cầu Tiên quyết

- **Python 3.10+** — kiểm tra với `python3 --version`
- **pip** — kiểm tra với `python3 -m pip --version`
- **Ollama** (khuyến nghị cho công việc khách hàng) — xem [MODEL_SETUP.md](MODEL_SETUP.md)

## 2. Cài đặt

```bash
cd ~/ai-law-firm-australia/
pip install -e .
```

Xác minh:
```bash
ailawfirm-australia --version
```

Bạn sẽ thấy biểu ngữ chào mừng đa ngôn ngữ (Anh · Trung · Việt · Ả Rập).

## 3. Thiết lập AI cục bộ (khuyến nghị cho công việc khách hàng)

Xem [MODEL_SETUP.md](MODEL_SETUP.md) để biết hướng dẫn đầy đủ về quyền riêng tư.

Thiết lập nhanh:
```bash
# Cài đặt Ollama
brew install ollama       # Mac
# hoặc tải từ https://ollama.com

# Tải mô hình (một lần, ~10-20 phút, ~10 GB)
ollama pull qwen3:14b
```

Công cụ được cấu hình mặc định cho AI cục bộ. Không cần tài khoản đám mây.

## 4. Kết nối với MCP Client

### Claude Code

```bash
claude mcp add ailawfirm-australia -- python ~/ai-law-firm-australia/ailawfirm_australia/mcp_server.py
```

### Cursor / các MCP client khác

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

## 5. Thao tác đầu tiên

### Tra cứu Tòa án
Sử dụng công cụ MCP `australia_court_lookup`:
- Tra cứu Tòa án Tối cao Úc (HCA)
- Tòa án nào ở VIC?
- Hiển thị chi tiết ART (Tòa Xét xử Hành chính)

### Xác thực Trích dẫn
Sử dụng công cụ MCP `australia_citation_validator`:
- Xác thực [2024] FCAFC 100
- Phân tích (2023) 97 ALJR 100

### Đồng bộ Lịch
Sử dụng công cụ MCP `australia_calendar_sync`:
- Lên lịch phiên họp chỉ đạo vào ngày 15/06/2026 lúc 10 giờ sáng giờ Sydney

## 6. Lưu ý Tuân thủ Quan trọng

- **LPUCSR Quy tắc 9 (Bảo mật):** Chỉ sử dụng AI cục bộ cho dữ liệu khách hàng. Không tải tài liệu khách hàng lên AI đám mây.
- **APP 8 (Trách nhiệm xuyên biên giới):** Truyền thông tin cá nhân cho nhà cung cấp nước ngoài khiến bạn chịu trách nhiệm.
- **Mục 77 (Đạo luật My Health Records):** Nghiêm cấm xử lý dữ liệu sức khỏe ở nước ngoài.
- **Tranche 2 AML (hiệu lực tháng 7/2026):** Luật sư sẽ được đưa vào phạm vi báo cáo AML.

## 7. Hỗ trợ Ngôn ngữ

- English — [GETTING_STARTED.md](GETTING_STARTED.md) (bản chính thức)
- 简体中文 — [GETTING_STARTED_CHINESE.md](GETTING_STARTED_CHINESE.md)
- العربية — [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md)

Giúp cải thiện bản dịch AI: [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md)

---

Xây dựng từ the local memory layer 3.0.0 (MIT). Được xuất bản bởi wolfgang_rush (Tòa án Tối cao Bombay, [Your Bench]).
