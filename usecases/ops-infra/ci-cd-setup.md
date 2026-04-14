# Use Case: Generating a GitHub Actions CI/CD Workflow

**Category:** Ops / Infra
**Difficulty:** Beginner

---

## The Problem

You have a Python project and no CI. Every merge to `main` is a prayer. You want GitHub Actions to automatically lint, run tests, and (optionally) deploy on push — without spending an afternoon reading YAML documentation.

## Why MADE fits this

CI/CD YAML is notoriously fiddly: wrong indentation, missing `on:` triggers, incorrect cache keys, forgotten secrets. The Architect defines exactly what the pipeline must do and what the environment looks like. The Builder writes the YAML. The Reviewer validates structure and checks for common mistakes before you push it and wait for a red build.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Generate a GitHub Actions workflow at .github/workflows/ci.yml for this Python 3.13 project. It should trigger on push and pull_request to main. Steps: checkout, set up Python 3.13, install deps from requirements.txt using pip with .venv cache, run ruff check, run mypy, run pytest with coverage. Fail the build if coverage drops below 80%."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Create .github/workflows/ci.yml: full lint → type-check → test pipeline for Python 3.13.

## Context Files
- requirements.txt          ← check what's installed (ruff, mypy, pytest already present?)
- .venv/bin/python --version ← confirm Python version

## Acceptance Criteria
1. Workflow triggers on: push and pull_request targeting the `main` branch.
2. Jobs: one job named `ci` running on `ubuntu-latest`.
3. Steps in order:
   a. actions/checkout@v4
   b. actions/setup-python@v5 with python-version: "3.13"
   c. pip cache using actions/cache@v4 keyed on requirements.txt hash
   d. pip install -r requirements.txt
   e. ruff check . (lint)
   f. mypy . --ignore-missing-imports (type check)
   g. pytest --cov=src --cov-fail-under=80 (test + coverage gate)
4. Each step has a human-readable `name:` field.
5. No hardcoded secrets in the YAML — use ${{ secrets.X }} for any credentials.

## Scope Boundaries
- Create .github/workflows/ directory if it does not exist.
- Do NOT modify any source files.
- Do NOT add a deploy step unless explicitly requested.

## Edge Cases
- If ruff is not in requirements.txt, add it — do not assume it is installed globally.
- Cache key must include the OS and Python version to avoid cross-platform cache poisoning.
```

### 3. What the Builder produces (`.github/workflows/ci.yml`)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.13
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Cache pip dependencies
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-py3.13-${{ hashFiles('requirements.txt') }}

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Lint with ruff
        run: ruff check .

      - name: Type check with mypy
        run: mypy . --ignore-missing-imports

      - name: Run tests with coverage
        run: pytest --cov=src --cov-fail-under=80
```

### 4. Push and verify

```bash
git add .github/workflows/ci.yml
git commit -m "Add CI workflow"
git push origin main
```

Check the **Actions** tab in your GitHub repo. The workflow should appear within seconds.

---

## Tips

- **Add a deploy step in a separate request.** Keep the CI request focused on lint/test. Once that's green and merged, run a second pipeline task for the deploy step. Mixing them produces a complex brief that's harder to review.
- **Specify the exact Python version.** "Python 3.13" is better than "latest Python" — it prevents surprising version bumps.
- **Test the cache key.** The hash of `requirements.txt` is a solid cache key. If you pin versions in `requirements.txt`, the cache invalidates only when deps actually change.
