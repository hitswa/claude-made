# Use Case: Adding a New REST API Endpoint

**Category:** Dev / Engineering
**Difficulty:** Beginner — good first use case for learning MADE

---

## The Problem

A product manager drops a requirement: _"We need a `GET /users/{id}/summary` endpoint that returns the user's name, total orders, and last login date."_ You have an existing FastAPI codebase. You need the endpoint implemented, validated, and reviewed — without the AI drifting into unrelated files.

## Why MADE fits this

A single-agent session tends to read the whole codebase, rewrite things that weren't asked for, and lose focus halfway through. MADE keeps the Architect scoped to the spec, the Builder scoped to the implementation files, and the Reviewer scoped to the acceptance criteria — nothing leaks.

---

## Step-by-Step

### 1. Write your request and run the pipeline

```bash
python -m src.pipeline "Add a GET /users/{id}/summary endpoint that returns name, total_orders (int), and last_login (ISO date string). Return 404 if user not found."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

The Architect will explore your codebase and write a brief like:

```markdown
## Objective
Add GET /users/{id}/summary to the FastAPI app.

## Context Files
- src/routers/users.py
- src/models/user.py
- src/db/session.py

## Acceptance Criteria
1. Route returns 200 with { "name": str, "total_orders": int, "last_login": str } for a valid user.
2. Route returns 404 with { "detail": "User not found" } for an unknown ID.
3. Response model is defined as a Pydantic schema, not an inline dict.
4. No new database queries outside of the existing session pattern.

## Scope Boundaries
- Do NOT modify: src/routers/auth.py, src/main.py, any migration files.

## Edge Cases
- User exists but has never logged in → last_login should be null, not omitted.
- Non-integer ID in path → FastAPI handles this automatically via path type; do not add manual validation.
```

### 3. What the Builder produces

The Builder reads the brief, modifies only `src/routers/users.py` and `src/models/user.py`, adds the Pydantic response schema, and writes `handoff/build_result.md`:

```markdown
[Source: builder-agent] [Confidence: High] [Timestamp: 2026-04-15T10:22:00Z]

## Changes Made
- src/routers/users.py: Added GET /users/{id}/summary route with db session dependency.
- src/schemas/user.py: Added UserSummaryResponse Pydantic model.

## Acceptance Criteria Status
- [x] 200 response with correct shape
- [x] 404 for unknown ID
- [x] Pydantic schema defined
- [x] Uses existing session pattern

## Notes for Reviewer
last_login is returned as None (not omitted) when the field is null in the DB.
```

### 4. What the Reviewer checks

The Reviewer reads the diff against the brief and verifies:
- Response shape matches the schema exactly
- 404 is raised with the correct detail string
- No files outside scope were touched

If it passes, the pipeline exits with `PIPELINE COMPLETE: PASS`. If not, the Builder gets one more loop.

---

## Tips

- **Be specific in your request.** The more precise your input, the tighter the Architect's brief. Vague requests like "add a user endpoint" produce loose acceptance criteria.
- **List files off-limits explicitly.** If you know the Builder shouldn't touch auth or migrations, say so in your prompt: _"Do not touch auth.py or any Alembic migration files."_
- **Check `handoff/task_brief.md` before the Builder runs.** If the Architect misunderstood the schema, edit the brief manually before proceeding — it's just a Markdown file.
