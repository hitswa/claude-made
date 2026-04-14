# Use Case: Code Quality Review

**Category:** Cybersecurity
**Difficulty:** Beginner–Intermediate

---

## The Problem

Code quality and security are more connected than they look. High-complexity functions are harder to reason about and easier to introduce bugs into. Dead code accumulates hidden logic that reviewers stop reading. Duplicated validation rules diverge over time and create inconsistency gaps. You need a structured quality audit that prioritizes findings by severity and gives engineers a clear fix backlog — not a wall of linter warnings.

## Why MADE fits this

A single-agent quality review either reads too little (misses cross-file duplication) or too much (drowns in irrelevant utility files). The Architect scopes the review to the modules that matter, defines the quality metrics explicitly, and sets severity thresholds. The Builder measures against those thresholds and produces a prioritized report. The Reviewer checks that every finding is real and actionable.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Perform a code quality review of the src/ directory. Identify: functions with cyclomatic complexity > 10, functions longer than 50 lines, duplicated logic blocks (same pattern in 3+ places), dead code (unused functions/variables), and missing input validation on public-facing functions. Write a prioritized report to reports/quality_review.md with severity Critical/Major/Minor per finding."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Code quality audit of src/ with severity-graded findings. Output: reports/quality_review.md.

## Context Files
- src/    ← full directory, all .py files

## Quality Metrics and Severity Thresholds

| Metric | Threshold | Severity |
|---|---|---|
| Cyclomatic complexity | > 15 | Critical |
| Cyclomatic complexity | 10–15 | Major |
| Function length | > 80 lines | Critical |
| Function length | 50–80 lines | Major |
| Duplicated logic block | 3+ locations | Major |
| Unused function/variable | any | Minor |
| Public function with no input validation | any | Major |

## Acceptance Criteria
1. Every finding includes: file, function name, line range, metric value, severity, and a one-sentence fix recommendation.
2. Report opens with a Quality Scorecard table: one row per file, columns for finding counts by severity.
3. Findings are sorted: Critical first, then Major, then Minor.
4. Duplication findings reference all locations where the duplicated pattern appears.
5. No source files are modified.
6. Report written to reports/quality_review.md.

## Scope Boundaries
- Review src/ only. Skip tests/, scripts/, migrations/.
- Do NOT attempt to auto-fix anything.

## Edge Cases
- A long function that is mostly a docstring or comments → count only executable lines, note the distinction.
- A function marked with # noqa or type: ignore → flag it in the report as [SUPPRESSED] and explain what is being suppressed.
```

### 3. Sample report output (`reports/quality_review.md`)

```markdown
# Code Quality Review

**Scope:** src/
**Date:** 2026-04-15

---

## Quality Scorecard

| File | Critical | Major | Minor |
|---|---|---|---|
| src/routers/orders.py | 1 | 2 | 0 |
| src/services/pricing.py | 0 | 1 | 3 |
| src/utils/validators.py | 0 | 0 | 2 |

---

## Critical Findings

### C-01 — Function too long + high complexity
**File:** src/routers/orders.py **Function:** `process_order` **Lines:** 45–132 (87 lines)
**Cyclomatic complexity:** 18
**Severity:** Critical

**Description:** `process_order` handles validation, pricing, inventory check, payment, and email notification in a single function body. Every conditional branch adds to the complexity score, making this function extremely difficult to test in isolation.

**Fix:** Extract into focused sub-functions: `validate_order_items()`, `calculate_order_total()`, `charge_payment()`, `notify_customer()`. Each should be independently testable.

---

## Major Findings

### M-01 — Duplicated validation logic
**Severity:** Major
**Locations:**
- src/routers/orders.py line 48
- src/routers/returns.py line 31
- src/routers/subscriptions.py line 67

**Description:** The pattern `if not re.match(r'^[A-Z]{2}\d{6}$', ref_id)` appears in 3 routers with slight variations. If the reference ID format changes, all 3 must be updated — and they will diverge.

**Fix:** Extract to `src/utils/validators.py` as `validate_reference_id(ref_id: str) -> bool` and import it in all three routers.
```

### 4. Turn the report into a backlog

After the pipeline completes, open one issue per Critical and Major finding:

```bash
# Example: create GitHub issues from the report
gh issue create --title "C-01: Refactor process_order (complexity 18)" \
  --body "See reports/quality_review.md — Critical finding C-01" \
  --label "tech-debt,critical"
```

---

## Tips

- **Set your own thresholds in the prompt.** The defaults above (complexity > 10, length > 50) are starting points. If your codebase has a lot of legacy code, tighten the thresholds over time as the debt is paid down.
- **Run this before a refactor sprint, not after.** The report becomes the sprint backlog. Running it after means you're auditing work you already did.
- **Combine with the security review.** High-complexity functions are also high-risk for security bugs. A function flagged as Critical in both reports should be the first thing refactored.
