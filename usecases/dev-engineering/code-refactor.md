# Use Case: Refactoring a Module (Callbacks → Async/Await)

**Category:** Dev / Engineering
**Difficulty:** Intermediate

---

## The Problem

You have a Python module that was written with synchronous blocking calls or nested callbacks. You need it converted to `async/await` without changing external behavior — no new features, no reshuffled logic, just a clean migration.

This is exactly the kind of task that goes wrong in a single-agent session: the agent starts refactoring, notices something "smelly" nearby, rewrites an unrelated function, and suddenly you have a 400-line diff you didn't ask for.

## Why MADE fits this

The Architect explicitly lists which functions are in scope and which are not. The Builder is bound to that list. The Reviewer checks that the external interface is unchanged. Scope creep is structurally prevented.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Refactor src/services/email.py from synchronous blocking calls to async/await. Use httpx.AsyncClient instead of requests.Session. Do not change the public function signatures or return types."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Migrate src/services/email.py to async/await using httpx.AsyncClient.

## Context Files
- src/services/email.py
- src/services/__init__.py    ← check if sync wrappers are re-exported
- tests/test_email.py         ← Builder must not break existing test signatures

## Acceptance Criteria
1. All functions that were synchronous are now declared with `async def`.
2. `requests.Session` is replaced with `httpx.AsyncClient` used as an async context manager.
3. Public function signatures (name, parameters, return types) are identical to before.
4. The module still exports the same symbols via __init__.py.
5. `./scripts/run-linter.sh` passes with zero errors.

## Scope Boundaries
- Do NOT modify: tests/test_email.py, src/services/__init__.py (read only), any other service file.

## Edge Cases
- If a function calls another internal function, both must be migrated together.
- Do not add retry logic or timeout config — that is out of scope.
```

### 3. Review focus

The Reviewer specifically checks:
- No new parameters were added to public functions
- `requests` is fully removed from imports
- `httpx` is properly added to `requirements.txt`
- No other files in `src/services/` were modified

### 4. Verify yourself

After the pipeline completes, run your existing tests:

```bash
pytest tests/test_email.py -v
```

If tests pass without modification, the refactor was clean.

---

## Tips

- **Specify the replacement library.** Don't just say "make it async" — say "use `httpx.AsyncClient`". This prevents the Builder from choosing an unexpected library.
- **Point the Architect at the test file.** Including the test file in context files ensures the Builder doesn't accidentally break the test interface.
- **One module at a time.** If you have multiple modules to refactor, run the pipeline once per module. Batching them into one request produces loose briefs.
