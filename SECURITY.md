# SECURITY — AI Brain · Australia

## Reporting a vulnerability

If you discover a security vulnerability in AI Brain — Australia, please report it via **GitHub Security Advisories** at the repository:

https://github.com/Wolfgangrush/ai-law-firm-australia/security/advisories/new

Or via private email to: rushikesh@mahajan-rush.dev (private channel — please do NOT post vulnerabilities to public GitHub Issues).

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested mitigation

We aim to acknowledge reports within 72 hours and provide an initial assessment within 7 days.

## Scope

Vulnerabilities in scope:
- Code-execution vulnerabilities (path traversal · command injection · pickle deserialization · etc.)
- Sensitive-data exposure (config-file world-readable · credentials in logs · etc.)
- Local privilege escalation via tool usage
- Cryptographic weaknesses in any signing or encryption layer

Out of scope:
- Vulnerabilities in upstream dependencies — report to those projects directly
- Vulnerabilities in cloud AI vendors — report to those vendors directly
- Social-engineering attacks against users
- Physical access attacks against the user's laptop

## Disclosure policy

We follow **coordinated disclosure**:
- We will not disclose the vulnerability publicly until a fix is released or 90 days pass, whichever is sooner
- We will credit the reporter in the CHANGELOG and security advisory (unless they prefer anonymity)
- We do NOT offer bug bounties at this time

## Security hygiene practices

- Dependencies pinned in `requirements.txt`
- Quarterly `pip-audit` review
- No `eval` · no `exec` in code
- All user input filtered before crossing tool/OS boundary
- File paths normalized to prevent path traversal
- Subprocess calls audited and use explicit argument lists (never shell=True with user input)

## Essential Eight alignment (advisory)

The Australian Signals Directorate (ASD) **Essential Eight** is the recommended baseline for cybersecurity maturity in Australian legal practices. While not a mandatory statutory requirement, Essential Eight compliance is increasingly a de-facto requirement for professional indemnity insurance for Australian solicitors.

The Essential Eight controls relevant to your use of this tool:

| Control | Relevance to AI Brain — Australia |
|---|---|
| **Application control** | Run the tool from a trusted, non-admin user account. Do not run the tool as root/Administrator. |
| **Patch applications** | Keep Python ≥3.10, Ollama, and all dependencies updated. Run `python3 -m pip list --outdated` quarterly. |
| **Configure Microsoft Office macro settings** | Not directly applicable, but if using cloud AI for document generation, disable macros in generated documents before opening. |
| **User application hardening** | Block Flash, Java, web ads. Not directly tool-relevant but standard practice. |
| **Restrict administrative privileges** | Do not run this tool as Administrator/root. Audit your laptop's admin accounts. |
| **Patch operating systems** | Keep macOS/Windows/Linux updated with security patches. |
| **Multi-factor authentication** | Enable MFA on your cloud AI provider accounts (DeepSeek · Anthropic · Google). MFA protects your API keys from account takeover. |
| **Regular backups** | Backup your `~/.ailawfirm-australia/` directory (config · calendar · matter data). |

## Past advisories

(None as of v0.1)

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §3.V11 (Security Vulnerability). Essential Eight references sourced from ASD (Australian Signals Directorate) public guidance. Playbook version: v0.1.*
