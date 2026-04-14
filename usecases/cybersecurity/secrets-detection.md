# Use Case: Secrets Detection in Source Code

**Category:** Cybersecurity
**Difficulty:** Beginner

---

## The Problem

A developer accidentally committed an API key three months ago. It was "removed" in the next commit, but it's still in git history. Or worse — it's still in the code, just buried in a config file nobody looks at. Hardcoded secrets (API keys, tokens, connection strings, private keys, passwords) in source code are one of the most common and highest-impact security mistakes.

This use case scans your codebase for hardcoded secrets and produces a report with file/line references so they can be rotated and removed before they reach production — or before a breach.

## Why MADE fits this

Secrets scanning needs to be thorough (many file types, many patterns) but the results need to be triaged (not every `password` variable is a real secret). The Architect defines the exact patterns to scan for. The Builder applies them systematically and labels each hit as `[CONFIRMED]`, `[LIKELY]`, or `[FALSE POSITIVE]`. The Reviewer re-reads each finding and challenges any that are labeled incorrectly.

> **Note:** This use case scans the working directory only. For git history scanning, use a dedicated tool like `git-secrets` or `trufflehog` alongside this report.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Scan all files in the project (excluding .venv/, .git/, node_modules/) for hardcoded secrets. Patterns to detect: API keys (long alphanumeric strings assigned to variables named *key*, *token*, *secret*, *password*, *credential*), connection strings (postgresql://, mysql://, mongodb:// with embedded credentials), private key blocks (-----BEGIN * PRIVATE KEY-----), JWT secrets, and any string matching common key formats (sk-*, ghp_*, xoxb-*). Write findings to reports/secrets_report.md with file, line, pattern matched, severity, and classification. Do not print secret values in full — mask the middle characters."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Scan project source files for hardcoded secrets. Output: reports/secrets_report.md.

## Patterns to Detect

| Pattern | Example | Severity |
|---|---|---|
| Variable assignment with secret name | `API_KEY = "abc123..."` | Critical |
| Connection string with credentials | `postgresql://user:pass@host/db` | Critical |
| Private key block | `-----BEGIN RSA PRIVATE KEY-----` | Critical |
| Anthropic API key | `sk-ant-...` (prefix match) | Critical |
| GitHub token | `ghp_...` or `ghs_...` | Critical |
| Slack token | `xoxb-...` or `xoxp-...` | Critical |
| OpenAI key | `sk-...` (length > 40) | High |
| Generic long secret (> 32 chars) in secret-named variable | — | High |
| Placeholder/example values | `your-api-key-here`, `changeme` | Low (informational) |

## Acceptance Criteria
1. Scan all files except: .venv/, .git/, node_modules/, *.pyc, binary files.
2. For each finding: file path, line number, variable name (if applicable), pattern matched, severity, classification.
3. Classification rules:
   - [CONFIRMED]: pattern matches and the value looks like a real secret (non-placeholder, non-test).
   - [LIKELY]: pattern matches but context is ambiguous (e.g., inside a test file or example config).
   - [FALSE POSITIVE]: pattern matches but is clearly not a secret (e.g., a comment, a URL without credentials).
4. Secret values must be masked: show first 4 and last 4 characters only (e.g., `sk-a...x9Kz`).
5. Report opens with a summary: total findings by severity and classification.
6. .env files: scan and report, but note that .env should be in .gitignore — flag if it is not.
7. No source files are modified.

## Scope Boundaries
- Scan working directory only. Do NOT read .git/ history.
- Do NOT attempt to validate secrets against live APIs.

## Edge Cases
- A secret-looking value inside a comment → classify as [FALSE POSITIVE], note it is in a comment.
- A secret inside a test fixture (`tests/fixtures/`) → classify as [LIKELY], note the test context.
- .env.example with placeholder values → classify as [FALSE POSITIVE] — placeholders are expected.
- .env (real env file, not example) found in repo → escalate to Critical regardless of values, note it must be gitignored and rotated.
```

### 3. Sample report output (`reports/secrets_report.md`)

```markdown
# Secrets Detection Report

**Scope:** Project root (excluding .venv/, .git/)
**Date:** 2026-04-15

---

## Summary

| Severity | Confirmed | Likely | False Positive |
|---|---|---|---|
| Critical | 2 | 0 | 0 |
| High | 0 | 1 | 0 |
| Low | 0 | 0 | 3 |

---

## Critical Findings

### S-01 — Hardcoded Anthropic API key
**File:** src/config.py **Line:** 14
**Pattern:** Anthropic API key prefix (sk-ant-)
**Classification:** [CONFIRMED]

```python
# Line 14
ANTHROPIC_API_KEY = "sk-an...Tz9q"  # masked
```

**Action:** Rotate this key immediately at console.anthropic.com. Remove from source and load from environment:
```python
import os
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
```

---

### S-02 — Database connection string with embedded password
**File:** src/db/session.py **Line:** 8
**Pattern:** postgresql:// with credentials
**Classification:** [CONFIRMED]

```python
# Line 8
DATABASE_URL = "postgresql://admin:s3cr3t@prod-db.internal:5432/appdb"  # masked password
```

**Action:** Rotate the database password. Move to environment variable:
```python
DATABASE_URL = os.environ["DATABASE_URL"]
```

---

## Informational (Low)

### S-05 — Placeholder values in .env.example
**File:** .env.example **Lines:** 1
**Classification:** [FALSE POSITIVE]
`.env.example` contains placeholder values (`your-api-key-here`). This is expected — no action needed.
```

### 4. Immediate actions after the pipeline

For every `[CONFIRMED]` Critical finding:

1. **Rotate the secret immediately** — assume it is compromised.
2. **Remove it from source code** and replace with an environment variable load.
3. **Check git history** with a dedicated tool:
   ```bash
   # Install trufflehog
   brew install trufflehog
   trufflehog git file://. --since-commit HEAD~50
   ```
4. **Verify `.gitignore`** covers `.env`:
   ```bash
   grep "^\.env$" .gitignore || echo "WARNING: .env not in .gitignore"
   ```

---

## Tips

- **Run this before every major release and after every new developer onboards.** New developers often don't know the secret handling conventions and hardcode things during local development.
- **Mask secrets in the report.** The brief requires masking (`sk-a...x9Kz`). A secrets report that prints real secret values in plaintext is itself a security risk — especially if the report is committed or shared.
- **Git history is a separate problem.** This scan only covers the working directory. If a secret was committed and then removed, it still exists in history. Use `trufflehog` or `git-secrets` for history scanning.
- **Pair with pre-commit hooks.** Once the codebase is clean, prevent regression by adding `detect-secrets` as a pre-commit hook so secrets are caught before they ever reach the repo.
  ```bash
  pip install detect-secrets
  detect-secrets scan > .secrets.baseline
  ```
