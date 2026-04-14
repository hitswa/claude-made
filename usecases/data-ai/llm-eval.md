# Use Case: Building a Prompt Evaluation Harness

**Category:** Data / AI
**Difficulty:** Advanced

---

## The Problem

You have a Claude prompt (or a set of prompts) and you want to measure how well it performs across a batch of test cases. You need a script that sends each case to the API, scores the response against expected output, and produces a report — so you can iterate on prompts with data rather than gut feel.

## Why MADE fits this

Eval harnesses have a lot of moving parts: API calls, scoring logic, result aggregation, and report formatting. Giving all of that to one agent in one session produces sprawling, hard-to-review code. MADE breaks it into a tight brief: the Architect defines the scoring rubric, the Builder wires up the harness, the Reviewer runs it against a known-good test set.

---

## Step-by-Step

### 1. Prepare your test cases

Create `data/eval_cases.json` before running the pipeline:

```json
[
  {
    "id": "case_01",
    "input": "Summarize this in one sentence: The quick brown fox jumps over the lazy dog.",
    "expected_keywords": ["fox", "dog"],
    "max_words": 20
  },
  {
    "id": "case_02",
    "input": "What is 2 + 2?",
    "expected_exact": "4",
    "max_words": 5
  }
]
```

### 2. Run the pipeline

```bash
python -m src.pipeline "Build a prompt eval harness at scripts/eval_harness.py. It reads test cases from data/eval_cases.json, sends each input to claude-haiku-4-5-20251001 via the Anthropic SDK, scores each response, and writes a Markdown report to data/eval_report.md. Scoring rules are defined in the test cases themselves."
```

### 3. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Create scripts/eval_harness.py: batch eval runner with scoring and Markdown report output.

## Context Files
- data/eval_cases.json    ← read to understand the schema before coding

## Acceptance Criteria
1. Script reads all cases from data/eval_cases.json.
2. For each case, sends `input` as a user message to the Anthropic API (model: claude-haiku-4-5-20251001).
3. Scoring logic per case:
   - `expected_exact`: PASS if response stripped == expected_exact (case-insensitive).
   - `expected_keywords`: PASS if all keywords appear in response (case-insensitive).
   - `max_words`: PASS if word count of response ≤ max_words.
   - Overall case result: PASS only if all applicable checks pass.
4. Output data/eval_report.md with: per-case verdict, response text, failed checks, and a summary table (total/pass/fail/pass_rate%).
5. API key read from environment variable ANTHROPIC_API_KEY (via python-dotenv).
6. Script handles API errors gracefully: log the error, mark case as ERROR, continue.

## Scope Boundaries
- Do NOT modify data/eval_cases.json.
- Do NOT add caching or async — keep it simple and synchronous.

## Edge Cases
- Case with no scoring fields → mark as SKIP with reason "no scoring criteria defined".
- API rate limit (429) → retry once after 5 seconds, then mark as ERROR.
```

### 4. Sample report output (`data/eval_report.md`)

```markdown
# Eval Report — 2026-04-15T10:30:00Z

## Summary
| Metric | Value |
|---|---|
| Total | 2 |
| Pass | 1 |
| Fail | 1 |
| Pass Rate | 50% |

## Results

### case_01 — PASS
**Response:** "A fox jumps over a dog."
- [PASS] expected_keywords: fox, dog
- [PASS] max_words: 6 ≤ 20

### case_02 — FAIL
**Response:** "The answer is 4."
- [FAIL] expected_exact: got "The answer is 4." expected "4"
- [PASS] max_words: 4 ≤ 5
```

### 5. Run it

```bash
python scripts/eval_harness.py
cat data/eval_report.md
```

---

## Tips

- **Start with 5–10 test cases.** The Architect reads the JSON to understand the schema; a small file keeps the brief tight.
- **Put scoring rules in the data, not the prompt.** The design above embeds scoring criteria per case. This lets you add new check types (e.g., `regex_match`) without changing the harness code — just update the JSON.
- **Use Haiku for evals.** It's fast and cheap for batch scoring. Reserve Sonnet for the actual production prompt you're evaluating.
- **Iterate on the prompt, not the harness.** Once the harness is built, the only thing you should be changing between runs is your system prompt. Add it as a variable at the top of the script.
