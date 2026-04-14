---
name: new-task
description: Start a new Orchestrator-Worker cycle. Clears handoff files and invokes the architect agent.
---

Clear existing handoff state and begin a new task cycle:

1. Archive any existing files in `handoff/` by appending a timestamp suffix.
2. Invoke `@architect-agent` with the user's request.
3. Wait for `handoff/task_brief.md` to be written before proceeding.
4. Invoke `@builder-agent`.
5. After `handoff/build_result.md` is written, invoke `@reviewer-agent` with `LOOP_COUNT=1`.
6. If the review FAILs, invoke `@builder-agent` again with the fix instructions, then `@reviewer-agent` with `LOOP_COUNT=2`.
7. If LOOP_COUNT=2 still FAILs, halt and surface the issue to the human operator.
