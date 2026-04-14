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

## OpenWolf Hook Integration

OpenWolf registers six Claude Code hooks that run automatically alongside MADE's own hooks. They are non-conflicting — OpenWolf hooks handle token tracking and memory; MADE hooks handle linting and quality gates.

| OpenWolf Hook | Fires | Effect |
|---|---|---|
| `session-start.js` | SessionStart | Loads session context and memory log |
| `pre-read.js` | PreToolUse (Read) | Intercepts file reads — shows `anatomy.md` summary if file was recently read, blocking redundant full reads |
| `pre-write.js` | PreToolUse (Write/Edit) | Checks `cerebrum.md` for known patterns; surfaces Do-Not-Repeat rules before the Builder writes |
| `post-read.js` | PostToolUse (Read) | Records token cost of the read into the token ledger |
| `post-write.js` | PostToolUse (Write/Edit) | Updates `anatomy.md` file index with new content summary |
| `stop.js` | Stop | Writes session token summary to ledger |

**All agents benefit automatically.** The Architect's read-heavy exploration phase sees the largest token savings (repeated reads of the same files are blocked). The Builder benefits from `cerebrum.md` pattern enforcement. The Reviewer's lightweight reads are tracked for accurate cost reporting.

**Do not modify `.wolf/` files manually during a task cycle.** `anatomy.md` and `cerebrum.md` are updated by hooks — manual edits will be overwritten.

## Scope Boundaries (All Agents)

- No agent may modify `.claude/` or `.wolf/` configuration files during a task cycle.
- No agent may push to remote git or modify CI/CD pipelines autonomously.
- Production database access is prohibited in all permission modes.
