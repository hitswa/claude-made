#!/usr/bin/env bash
# Deterministic linting script — called by PostToolUse hooks after every Edit/Write
set -euo pipefail

VENV_PYTHON=".venv/bin/python"

if [ ! -f "$VENV_PYTHON" ]; then
  echo "ERROR: .venv not found. Run: python3 -m venv .venv && pip install -r requirements.txt"
  exit 1
fi

echo "--- Running linter ---"

# Python: ruff (fast linter + formatter check)
if .venv/bin/python -m ruff --version &>/dev/null; then
  .venv/bin/python -m ruff check . --fix
  .venv/bin/python -m ruff format --check .
  echo "ruff: OK"
else
  echo "WARN: ruff not installed, skipping Python lint"
fi

# Python: mypy type check (if installed)
if .venv/bin/python -m mypy --version &>/dev/null; then
  .venv/bin/python -m mypy . --ignore-missing-imports
  echo "mypy: OK"
else
  echo "WARN: mypy not installed, skipping type check"
fi

echo "--- Linter complete ---"
