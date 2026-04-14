# MADE Use Cases

Practical examples of using the **Multi-Agent Development Ecosystem (MADE)** framework. Each use case shows you exactly what prompt to run, what the Architect produces, what the Builder implements, and how the Reviewer validates it.

## How to use these guides

1. Pick a use case that matches your task.
2. Copy the `python -m src.pipeline "..."` command and adapt it to your codebase.
3. Follow the step-by-step to understand what each agent does and how to verify the result.

## Token efficiency — OpenWolf

All use cases in this framework automatically benefit from [OpenWolf](https://openwolf.com), which runs invisibly as Claude Code middleware. It maintains a file index (`anatomy.md`) so agents skip redundant reads, and a learned-preference memory (`cerebrum.md`) so corrections are never repeated across sessions. Install it once and it works across every pipeline run:

```bash
npm install -g openwolf && openwolf init
```

---

## Dev / Engineering

Everyday software development tasks — adding features, refactoring, writing tests.

| Use Case | What it solves |
|---|---|
| [Adding a REST API Endpoint](dev-engineering/rest-api-feature.md) | New route with schema, validation, and 404 handling |
| [Refactoring a Module](dev-engineering/code-refactor.md) | Migrate sync callbacks to async/await without behavior change |
| [Generating a Test Suite](dev-engineering/test-suite.md) | Unit + integration tests with coverage targets for an untested module |

---

## Data / AI

Data processing pipelines and AI tooling.

| Use Case | What it solves |
|---|---|
| [ETL Data Pipeline](data-ai/data-pipeline.md) | Read CSVs → validate → clean/rejected outputs with summary log |
| [Prompt Evaluation Harness](data-ai/llm-eval.md) | Batch-test a Claude prompt against expected outputs and produce a scored report |

---

## Ops / Infra

Infrastructure configuration and containerization.

| Use Case | What it solves |
|---|---|
| [GitHub Actions CI/CD](ops-infra/ci-cd-setup.md) | Lint → type-check → test → coverage gate on every push |
| [Dockerfile](ops-infra/dockerfile.md) | Multi-stage build, non-root user, health check for a Python app |

---

## Business / Automation

Scripts that automate recurring manual work.

| Use Case | What it solves |
|---|---|
| [Weekly Report Generator](business-automation/report-generator.md) | JSON metrics → formatted Markdown report, stdlib only |
| [Slack Slash Command Handler](business-automation/slack-bot-command.md) | `/status <id>` → real-time lookup with signature verification |

---

## Cybersecurity

Static analysis, vulnerability auditing, and secrets management — defensive use only.

| Use Case | What it solves |
|---|---|
| [Code Security Review](cybersecurity/code-security-review.md) | OWASP Top 10 static analysis with file/line findings and fix recommendations |
| [Code Quality Review](cybersecurity/code-quality-review.md) | Complexity, duplication, dead code, and missing validation — severity graded |
| [Dependency Vulnerability Report](cybersecurity/dependency-vulnerability-report.md) | CVE audit of installed packages with upgrade action plan |
| [Secrets Detection](cybersecurity/secrets-detection.md) | Scan source files for hardcoded API keys, tokens, and credentials |
