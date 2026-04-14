# Use Case: Code Security Review (OWASP Top 10)

**Category:** Cybersecurity
**Difficulty:** Intermediate

---

## The Problem

Your codebase handles user input, authenticates users, and talks to a database. Before a release or a penetration test, you need a structured security review mapped to known vulnerability classes — not just a generic "looks fine" from a single-agent scan that reads too much context and loses focus halfway through.

## Why MADE fits this

Security reviews require reading code carefully in a narrow scope, not broadly. The Architect identifies which files are attack-surface-adjacent (request handlers, auth logic, DB queries, template rendering) and scopes the Builder to those files only. The Builder maps each finding to an OWASP category and a specific line. The Reviewer confirms each finding references real code and flags false positives — preventing the report from becoming noise.

> **Note:** MADE performs static analysis — it reads source code. It does not run dynamic scans, exploit payloads, or interact with live systems. Use this alongside (not instead of) tools like Bandit, Semgrep, or a professional pentest.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Perform a static security review of the src/ directory. Map findings to OWASP Top 10 categories. For each finding include: file path, line number, OWASP category, severity (Critical/High/Medium/Low), description of the vulnerability, and a concrete fix recommendation. Write the report to reports/security_review.md. Do not modify any source files."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Static security review of src/ mapped to OWASP Top 10. Output: reports/security_review.md.

## Context Files
- src/routers/         ← all route handlers (user input entry points)
- src/auth/            ← authentication and session logic
- src/db/              ← query construction and ORM usage
- src/templates/       ← Jinja2 or HTML templates (XSS surface)
- src/config.py        ← environment variable handling, secret loading

## OWASP Categories to check
| ID  | Category |
|-----|----------|
| A01 | Broken Access Control |
| A02 | Cryptographic Failures |
| A03 | Injection (SQL, command, LDAP) |
| A04 | Insecure Design |
| A05 | Security Misconfiguration |
| A06 | Vulnerable & Outdated Components |
| A07 | Identification & Authentication Failures |
| A08 | Software & Data Integrity Failures |
| A09 | Security Logging & Monitoring Failures |
| A10 | Server-Side Request Forgery (SSRF) |

## Acceptance Criteria
1. Every finding includes: file path, line number, OWASP ID, severity, description, fix recommendation.
2. Findings are grouped by OWASP category, sorted by severity descending within each group.
3. Report opens with an Executive Summary: total findings by severity.
4. Each finding is labeled [CONFIRMED] or [REVIEW NEEDED] — Builder must not mark uncertain findings as confirmed.
5. No source files are modified.
6. Report written to reports/security_review.md (create reports/ if missing).

## Scope Boundaries
- Review src/ only. Do NOT review tests/, scripts/, or .claude/.
- Do NOT attempt to run code or make HTTP requests.

## Edge Cases
- If a pattern looks suspicious but context is ambiguous (e.g., a raw query inside a test fixture), label [REVIEW NEEDED] and explain why.
- Hardcoded secrets found during review → escalate to Critical severity under A02, even if not originally in scope.
```

### 3. Sample report output (`reports/security_review.md`)

```markdown
# Security Review Report

**Scope:** src/
**Date:** 2026-04-15
**Reviewer:** MADE builder-agent (static analysis)

---

## Executive Summary

| Severity | Count |
|---|---|
| Critical | 1 |
| High | 2 |
| Medium | 3 |
| Low | 1 |

---

## A03 — Injection

### [CONFIRMED] SQL Injection via string formatting
**File:** src/routers/users.py **Line:** 42
**Severity:** Critical

**Code:**
```python
query = f"SELECT * FROM users WHERE email = '{email}'"
db.execute(query)
```

**Description:** User-controlled `email` is interpolated directly into a raw SQL string. An attacker can inject arbitrary SQL by crafting a malicious email value (e.g., `' OR 1=1 --`).

**Fix:** Use parameterized queries:
```python
db.execute("SELECT * FROM users WHERE email = ?", (email,))
```

---

## A07 — Identification & Authentication Failures

### [CONFIRMED] Weak password hashing algorithm
**File:** src/auth/passwords.py **Line:** 17
**Severity:** High

**Description:** `hashlib.md5` is used to hash passwords. MD5 is cryptographically broken and unsuitable for password storage.

**Fix:** Replace with `bcrypt` or `argon2-cffi`:
```python
from argon2 import PasswordHasher
ph = PasswordHasher()
hashed = ph.hash(password)
```
```

### 4. After the pipeline

Review the report and triage findings:

```bash
cat reports/security_review.md
```

For each `[CONFIRMED]` Critical or High finding, open a tracked issue and fix it before the next release. For `[REVIEW NEEDED]` items, a human engineer should read the referenced code and make the call.

---

## Tips

- **Scope to attack-surface files, not the whole repo.** Asking the Architect to review `src/utils/formatting.py` is noise. Routers, auth, DB queries, and templates are where the real risks live.
- **Run Bandit alongside this.** MADE provides human-readable findings with fix guidance. Bandit gives you machine-readable output for CI. They complement each other.
  ```bash
  .venv/bin/python -m bandit -r src/ -f txt
  ```
- **Do not auto-apply fixes.** The Builder's job here is reporting only. Apply fixes in a separate pipeline run (e.g., use the `rest-api-feature` or `code-refactor` pattern for each finding).
