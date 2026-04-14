# Use Case: Containerizing a Python App with Docker

**Category:** Ops / Infra
**Difficulty:** Beginner–Intermediate

---

## The Problem

You have a working Python application — maybe a FastAPI service, a CLI tool, or a background worker — and you need to ship it as a Docker image. You want a production-grade `Dockerfile`: multi-stage build, non-root user, health check, minimal final image. Writing this from scratch means reading Docker docs for an hour. MADE does it in one pipeline run.

## Why MADE fits this

Dockerfiles have a deceptively large surface area: layer ordering for cache efficiency, multi-stage builds to keep image size down, correct signal handling with `exec` form `CMD`, non-root user for security. The Architect captures all of this as explicit acceptance criteria. The Reviewer catches common mistakes (wrong CMD form, root user, wrong port) before you build and push.

---

## Step-by-Step

### 1. Run the pipeline

```bash
python -m src.pipeline "Write a production Dockerfile for this Python 3.13 FastAPI app. Use a multi-stage build: builder stage installs deps, final stage copies only the venv. Run as a non-root user. Expose port 8000. Add a health check on GET /health. Entry point: uvicorn src.main:app --host 0.0.0.0 --port 8000."
```

### 2. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Write a production-grade Dockerfile for the FastAPI app.

## Context Files
- requirements.txt       ← needed to understand what gets installed
- src/main.py            ← confirm the app object name and health check route

## Acceptance Criteria
1. Multi-stage build: stage 1 (`builder`) installs dependencies into /venv; stage 2 copies only /venv and src/.
2. Base image: python:3.13-slim for both stages.
3. Final image runs as a non-root user named `appuser` (UID 1000).
4. Port 8000 is EXPOSEd.
5. HEALTHCHECK polls GET http://localhost:8000/health every 30s, timeout 5s, 3 retries.
6. CMD uses exec form (JSON array), not shell form.
7. .dockerignore excludes: .venv/, .git/, __pycache__/, .env, tests/.

## Scope Boundaries
- Create Dockerfile and .dockerignore at project root only.
- Do NOT modify any source files.

## Edge Cases
- If src/main.py does not have a /health route, note it in build_result.md but do not add it — that is a separate task.
- Layer order must place requirements installation before source copy to maximize cache hits.
```

### 3. What the Builder produces (`Dockerfile`)

```dockerfile
# --- Stage 1: Builder ---
FROM python:3.13-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# --- Stage 2: Final ---
FROM python:3.13-slim

RUN useradd --uid 1000 --create-home appuser
WORKDIR /app

COPY --from=builder /venv /venv
COPY src/ ./src/

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD ["/venv/bin/python", "-c", \
         "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]

CMD ["/venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

And `.dockerignore`:
```
.venv/
.git/
__pycache__/
*.pyc
.env
tests/
handoff/
usecases/
```

### 4. Build and test locally

```bash
docker build -t made-app:local .
docker run -p 8000:8000 made-app:local

# In another terminal:
curl http://localhost:8000/health
docker inspect --format='{{json .State.Health}}' $(docker ps -q)
```

---

## Tips

- **Specify the app entrypoint exactly.** "uvicorn src.main:app" only works if your module path is correct. Check `src/main.py` exists and the FastAPI object is named `app`.
- **Multi-stage builds are non-negotiable for production.** The single-stage alternative installs build tools in the final image, bloating it by hundreds of MB. The brief enforces multi-stage as a criterion.
- **Test the health check status, not just the HTTP response.** `docker inspect` shows whether Docker considers the container healthy, which is what orchestrators (ECS, Kubernetes) actually use.
