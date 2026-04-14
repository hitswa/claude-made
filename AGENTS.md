# Multi-Agent Workflow Boundaries

## Agent Personas

| Agent | Model | Permission Mode | Authority |
|---|---|---|---|
| `@architect-agent` | claude-sonnet-4-6 | plan | Full read access. Cannot write code. Outputs to `handoff/task_brief.md` only. |
| `@builder-agent` | claude-sonnet-4-6 | acceptEdits | Writes source code within brief scope. Cannot alter routing, DB schemas, or architecture. |
| `@reviewer-agent` | claude-haiku-4-5-20251001 | plan | Read-only. Validates diffs against brief. Cannot suggest scope expansions. |

## Inter-Agent Handoff Protocol

1. All data passed between agents must be plain-text Markdown files in `handoff/`.
2. Never use nested JSON for agent-to-agent communication — it causes silent schema degradation.
3. Every write-back to shared state must include: `[Source: <agent>]`, `[Confidence: High/Medium/Low]`, `[Timestamp: <ISO 8601>]`.

## Handoff File Sequence

```text
handoff/task_brief.md    ← Architect writes, Builder reads
handoff/build_result.md  ← Builder writes, Reviewer reads
handoff/review_result.md ← Reviewer writes, Architect/human reads
```

## Anti-Loop Protocol

- Hard cap of **2** revision loops between Builder and Reviewer.
- On loop 2 failure, halt the pipeline and escalate to the human operator.
- Do not attempt a third loop under any circumstances.

## Scope Boundaries (All Agents)

- No agent may modify `.claude/` configuration files during a task cycle.
- No agent may push to remote git or modify CI/CD pipelines autonomously.
- Production database access is prohibited in all permission modes.
