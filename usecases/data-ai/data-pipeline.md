# Use Case: Building an ETL Data Pipeline

**Category:** Data / AI
**Difficulty:** Intermediate

---

## The Problem

You have raw CSV exports landing in a folder daily — sales records, user events, sensor readings, whatever. You need a Python script that reads them, validates and transforms the rows, and writes cleaned output to a target location. The script must be repeatable, handle bad rows gracefully, and log what it skipped.

## Why MADE fits this

ETL requirements always have a dozen edge cases hiding in the data. The Architect surfaces them upfront (what to do with nulls, duplicates, out-of-range values) so the Builder handles them in code rather than discovering them at runtime. The Reviewer validates the transformation logic against sample data before the script ever runs in production.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Build an ETL script at scripts/etl_sales.py that reads all CSV files from data/raw/, validates each row (required fields: order_id, amount, created_at), drops invalid rows to data/rejected.csv with a reason column, and writes cleaned rows to data/clean/sales_YYYYMMDD.csv. Log a summary at the end: total rows, accepted, rejected."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Create scripts/etl_sales.py: read CSVs from data/raw/, validate, split into clean and rejected outputs.

## Context Files
- data/raw/sample.csv    ← read 5–10 rows to understand the schema before writing code

## Acceptance Criteria
1. Script reads all *.csv files from data/raw/ (not recursive).
2. Validation rules:
   - order_id: must be non-empty string
   - amount: must be a positive float
   - created_at: must parse as ISO 8601 date
3. Invalid rows are written to data/rejected.csv with an added `rejection_reason` column.
4. Valid rows are written to data/clean/sales_YYYYMMDD.csv where date = today's date.
5. Summary log printed to stdout: total/accepted/rejected counts.
6. Script is idempotent: running twice on the same input produces the same output.
7. `./scripts/run-linter.sh` passes.

## Scope Boundaries
- Do NOT modify existing files in data/raw/.
- Do NOT use pandas — use Python's built-in csv module only.

## Edge Cases
- Empty CSV file → skip silently, log "skipped empty file: <name>".
- CSV with no valid rows → data/clean/ file is created but empty (header only).
- Duplicate order_ids → keep first occurrence, reject subsequent with reason "duplicate".
```

### 3. Sample input / expected output

Given `data/raw/sales_2026-04-15.csv`:

```csv
order_id,amount,created_at
ORD001,49.99,2026-04-15
ORD002,,2026-04-15
ORD003,25.00,not-a-date
ORD001,10.00,2026-04-15
```

Expected `data/clean/sales_20260415.csv`:
```csv
order_id,amount,created_at
ORD001,49.99,2026-04-15
```

Expected `data/rejected.csv`:
```csv
order_id,amount,created_at,rejection_reason
ORD002,,2026-04-15,missing required field: amount
ORD003,25.00,not-a-date,invalid date format: created_at
ORD001,10.00,2026-04-15,duplicate order_id
```

### 4. Verify after pipeline

```bash
python scripts/etl_sales.py
cat data/clean/sales_$(date +%Y%m%d).csv
cat data/rejected.csv
```

---

## Tips

- **Provide a sample CSV.** Drop a few rows in `data/raw/` before running the pipeline. The Architect reads it to understand the real schema rather than guessing.
- **Ban heavy libraries explicitly if you want them banned.** Saying "no pandas" forces simpler, more auditable code. If pandas is fine, remove that constraint.
- **Idempotency is a criterion, not an assumption.** Always add it to acceptance criteria — it forces the Builder to think about output file naming and overwrite behavior.
