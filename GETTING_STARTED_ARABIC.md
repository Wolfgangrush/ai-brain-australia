# دليل البدء — AI Brain · أستراليا · إصدار المحامي المستقل · v0.1

> ⚠️ ترجمة بمساعدة الذكاء الاصطناعي · مرحب بالناطقين الأصليين للتحسين عبر PR · انظر TRANSLATION_HELP_WANTED.md

**للمهنيين القانونيين المؤهلين فقط.** راجع [DISCLAIMER.md](DISCLAIMER.md).

## 1. المتطلبات الأساسية

- **Python 3.10+** — تحقق باستخدام `python3 --version`
- **pip** — تحقق باستخدام `python3 -m pip --version`
- **Ollama** (موصى به لعمل العملاء) — راجع [MODEL_SETUP.md](MODEL_SETUP.md)

## 2. التثبيت

```bash
cd ~/ai-law-firm-australia/
pip install -e .
```

تحقق:
```bash
ailawfirm-australia --version
```

سترى شعار الترحيب متعدد اللغات (الإنجليزية · الصينية · الفيتنامية · العربية).

## 3. إعداد الذكاء الاصطناعي المحلي (موصى به لعمل العملاء)

راجع [MODEL_SETUP.md](MODEL_SETUP.md) للحصول على دليل الخصوصية الكامل.

إعداد سريع:
```bash
# تثبيت Ollama
brew install ollama       # Mac
# أو قم بالتنزيل من https://ollama.com

# تحميل نموذج (مرة واحدة، حوالي 10-20 دقيقة، حوالي 10 جيجابايت)
ollama pull qwen3:14b
```

تم تكوين الأداة افتراضيًا للذكاء الاصطناعي المحلي. لا حاجة لحسابات سحابية.

## 4. الاتصال بعميل MCP

### Claude Code

```bash
claude mcp add ailawfirm-australia -- python ~/ai-law-firm-australia/ailawfirm_australia/mcp_server.py
```

### Cursor / عملاء MCP الآخرين

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

## 5. العمليات الأولى

### البحث عن المحاكم
استخدم أداة MCP `australia_court_lookup`:
- ابحث عن المحكمة العليا الأسترالية (HCA)
- ما هي المحاكم في ولاية فيكتوريا (VIC)؟
- عرض تفاصيل ART (محكمة المراجعة الإدارية)

### التحقق من الاقتباسات
استخدم أداة MCP `australia_citation_validator`:
- تحقق من [2024] FCAFC 100
- حلل (2023) 97 ALJR 100

### مزامنة التقويم
استخدم أداة MCP `australia_calendar_sync`:
- جدولة جلسة توجيهية في 15 يونيو 2026 الساعة 10 صباحًا بتوقيت سيدني

## 6. ملاحظات الامتثال الهامة

- **LPUCSR القاعدة 9 (السرية):** استخدم الذكاء الاصطناعي المحلي فقط لبيانات العملاء. لا تقم بتحميل مواد العملاء إلى الذكاء الاصطناعي السحابي.
- **APP 8 (المسؤولية عبر الحدود):** نقل المعلومات الشخصية إلى مزودين في الخارج يجعلك مسؤولاً.
- **المادة 77 (قانون السجلات الصحية):** يُحظر تمامًا معالجة البيانات الصحية في الخارج.
- **Tranche 2 AML (ساري المفعول يوليو 2026):** سيتم إدراج المحامين في نطاق الإبلاغ عن مكافحة غسل الأموال.

## 7. دعم اللغات

- English — [GETTING_STARTED.md](GETTING_STARTED.md) (النسخة الرسمية)
- 简体中文 — [GETTING_STARTED_CHINESE.md](GETTING_STARTED_CHINESE.md)
- Tiếng Việt — [GETTING_STARTED_VIETNAMESE.md](GETTING_STARTED_VIETNAMESE.md)

ساعد في تحسين الترجمات بمساعدة الذكاء الاصطناعي: [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md)

---

مبني على the local memory layer 3.0.0 (MIT). نُشر بواسطة wolfgang_rush (محكمة بومباي العليا، دائرة ناجبور).
