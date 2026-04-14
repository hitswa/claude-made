---
name: strict-code-review
description: Use when validating newly written code against project standards and running pre-commit linting.
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---

You are executing a strict code review.

1. Compare recent edits strictly against the acceptance criteria in `handoff/task_brief.md`.
2. Do not suggest feature expansions, refactoring of unrelated files, or scope creep.
3. Verify the PostToolUse hook ran `./scripts/run-linter.sh` successfully.
4. If violations exist, generate a precise fix plan (current code vs. required pattern) and return it to the Builder.
5. Adhere strictly to the two-round revision limit in `AGENTS.md`.
