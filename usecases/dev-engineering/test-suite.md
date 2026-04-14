# Use Case: Generating a Test Suite for an Untested Module

**Category:** Dev / Engineering
**Difficulty:** Beginner–Intermediate

---

## The Problem

You shipped a module under deadline pressure and it has zero tests. Now it's becoming critical infrastructure. You need unit tests and at least one integration test — without a human spending hours writing boilerplate.

## Why MADE fits this

The Architect reads the module and defines exactly which functions need tests and what edge cases matter. The Builder writes only the test file. The Reviewer runs the tests and checks coverage targets are met. The AI never touches the source module itself.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Write a pytest test suite for src/utils/pricing.py. Cover all public functions, at least one happy path and one edge case per function. Target 90% line coverage. Do not modify pricing.py."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Write tests/test_pricing.py covering all public functions in src/utils/pricing.py.

## Context Files
- src/utils/pricing.py     ← read fully before writing any tests

## Acceptance Criteria
1. A test file exists at tests/test_pricing.py.
2. Every public function (not prefixed with _) has at least one test.
3. Each function has at least one edge case test (zero values, negative inputs, empty lists, etc.).
4. `pytest tests/test_pricing.py` exits with code 0.
5. `pytest --cov=src/utils/pricing --cov-report=term-missing` shows ≥ 90% coverage.
6. No mocks of internal business logic — only mock external I/O (DB calls, HTTP requests).

## Scope Boundaries
- Do NOT modify: src/utils/pricing.py or any other source file.
- Do NOT create conftest.py unless absolutely required for fixtures.

## Edge Cases to cover
- calculate_discount(price=0) → should return 0, not divide-by-zero
- apply_tax(amount=-5) → should raise ValueError
- format_price(None) → check documented behavior
```

### 3. What the Builder produces

The Builder reads `pricing.py` top to bottom, then writes `tests/test_pricing.py` with:
- One test class per function (or flat functions if the module is small)
- Parametrized tests where multiple inputs share the same logic
- Fixtures for any repeated setup

### 4. What the Reviewer checks

```bash
pytest tests/test_pricing.py -v
pytest --cov=src/utils/pricing --cov-report=term-missing
```

The Reviewer verifies both commands pass and coverage meets the 90% target. If not, it sends specific failing test names back to the Builder.

---

## Tips

- **Name the coverage target explicitly.** Without a number, the Builder writes minimal tests. `≥ 90% line coverage` is a concrete, checkable criterion.
- **Tell it what NOT to mock.** Over-mocking is a common failure mode — mocked tests pass but real behavior breaks. The brief should state: mock only external I/O.
- **Run coverage yourself after the pipeline.** The Reviewer checks the report, but always confirm locally before merging:
  ```bash
  pytest --cov=src/utils/pricing --cov-fail-under=90
  ```
