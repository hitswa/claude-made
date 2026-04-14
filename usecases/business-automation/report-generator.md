# Use Case: Weekly Report Generator from JSON Data

**Category:** Business / Automation
**Difficulty:** Beginner

---

## The Problem

Every Monday morning someone exports a JSON file of last week's metrics — sales numbers, active users, error rates, whatever — and pastes numbers into a Word doc or Notion page by hand. You want a script that reads the JSON, formats it into a clean Markdown report, and saves it to a file so it can be pasted, emailed, or committed to a repo.

## Why MADE fits this

Report generation sounds simple but always has fiddly requirements: how to format currency, what to do with missing fields, how to sort items, what the header date range should say. Dumping all of this into a one-shot prompt produces code that works for the sample data but breaks on real data. The Architect captures every formatting rule explicitly; the Builder implements it exactly; the Reviewer runs it against a real JSON file.

---

## Step-by-Step

### 1. Prepare your data file

Drop your real (or sample) JSON into `data/weekly_metrics.json`:

```json
{
  "week_start": "2026-04-07",
  "week_end": "2026-04-13",
  "revenue": {
    "total": 48320.50,
    "by_product": [
      { "name": "Pro Plan", "amount": 31200.00 },
      { "name": "Starter Plan", "amount": 12400.50 },
      { "name": "Enterprise", "amount": 4720.00 }
    ]
  },
  "users": {
    "new": 214,
    "churned": 18,
    "active": 3841
  },
  "errors": {
    "total": 47,
    "p1_count": 2
  }
}
```

### 2. Run the pipeline

```bash
python -m src.pipeline "Write a script at scripts/generate_report.py that reads data/weekly_metrics.json and writes a formatted Markdown weekly report to reports/weekly_YYYY-MM-DD.md (using week_end date). Format currency as USD with commas. Sort products by amount descending. Highlight P1 errors in bold if p1_count > 0."
```

### 3. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Create scripts/generate_report.py: read metrics JSON, write a formatted Markdown report.

## Context Files
- data/weekly_metrics.json    ← read to understand exact schema before coding

## Acceptance Criteria
1. Output file path: reports/weekly_{week_end}.md (create reports/ dir if missing).
2. Report sections in order: title, date range, Revenue, Users, Errors.
3. Revenue: total formatted as $XX,XXX.XX; product breakdown as a Markdown table sorted by amount descending.
4. Users: new, churned, active as a bullet list. Include net change: (new - churned).
5. Errors: total count. If p1_count > 0, render as: "**⚠ P1 Incidents: {p1_count}**".
6. Missing fields in JSON → skip that section with a note "data unavailable", do not crash.
7. Script is runnable as: python scripts/generate_report.py (no CLI args required).

## Scope Boundaries
- Do NOT modify data/weekly_metrics.json.
- Do NOT use any third-party libraries — stdlib only (json, pathlib, datetime).
```

### 4. Expected output (`reports/weekly_2026-04-13.md`)

```markdown
# Weekly Metrics Report

**Period:** April 7, 2026 – April 13, 2026

---

## Revenue

**Total:** $48,320.50

| Product | Revenue |
|---|---|
| Pro Plan | $31,200.00 |
| Starter Plan | $12,400.50 |
| Enterprise | $4,720.00 |

---

## Users

- **New:** 214
- **Churned:** 18
- **Active:** 3,841
- **Net change:** +196

---

## Errors

- **Total:** 47
- **⚠ P1 Incidents: 2**
```

### 5. Run and review

```bash
python scripts/generate_report.py
cat reports/weekly_2026-04-13.md
```

---

## Tips

- **Drop the real JSON before running.** The Architect reads the file to understand the exact schema. A sample with all possible fields (including optional ones that are sometimes missing) produces a much more robust brief.
- **Stdlib only keeps the script portable.** No pandas, no Jinja2 — the report is simple enough that the standard `json` + `pathlib` + string formatting is sufficient and produces a script with zero dependencies.
- **Automate the run with cron.** Once the script is working, pair it with a cron job or a GitHub Actions schedule to generate the report automatically every Monday. See the `ci-cd-setup` use case for the Actions pattern.
