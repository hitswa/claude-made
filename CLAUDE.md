# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A learning project implementing a multi-agent AI development system using the Claude framework. The architecture follows the **Orchestrator-Worker (Triad) pattern**:

- **Architect** (`claude-sonnet-4-6`, plan mode) — decomposes requirements into briefs; never writes code; outputs to `handoff/task_brief.md`
- **Builder** (`claude-sonnet-4-6`, acceptEdits mode) — reads briefs, implements features within a restricted scope
- **Reviewer** (`claude-haiku-4-5`, read-only) — validates output against brief and CLAUDE.md; hard cap of 2 revision loops

## Environment

- Python 3.13, virtual environment at `.venv/`
- Activate: `source .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`
- Key packages: `claude-agent-sdk`, `mcp`, `pydantic`, `uvicorn`, `python-dotenv`

## Directory Structure

```text
.claude/agents/     # Subagent persona definitions (architect.md, builder.md, reviewer.md)
.claude/skills/     # Progressive-disclosure skill files (SKILL.md per skill)
.claude/commands/   # Slash command definitions
.claude/memory/     # Persistent cross-session context
.wolf/              # OpenWolf token optimization layer (anatomy.md, cerebrum.md, hooks/)
handoff/            # Plain-text Markdown files for inter-agent communication
scripts/            # Deterministic shell/Python scripts (linting, git, CI)
```

## Token Optimization — OpenWolf

This project uses [OpenWolf](https://openwolf.com) to minimize token consumption across all agent sessions. OpenWolf runs as invisible middleware via Claude Code hooks — no manual steps are needed during normal use.

**What it maintains in `.wolf/`:**

| File | Purpose |
|---|---|
| `anatomy.md` | File index with token estimates — agents consult this before reading files to skip unnecessary full reads |
| `cerebrum.md` | Learned preferences, Do-Not-Repeat patterns, and enforced conventions across sessions |
| `memory.md` | Chronological action log per session |
| `buglog.json` | Searchable record of bug encounters and resolutions |

**Hook responsibilities:**
- `PreToolUse / pre-read.js` — warns on repeated reads, shows file summary from anatomy.md instead
- `PreToolUse / pre-write.js` — checks cerebrum.md for known patterns before any write
- `PostToolUse / post-read.js` — records token estimate for the file just read
- `PostToolUse / post-write.js` — updates anatomy.md file index after writes
- `SessionStart / session-start.js` — loads session context from memory
- `Stop / stop.js` — writes session summary to token ledger

**Setup (run once):**
```bash
npm install -g openwolf
openwolf init
```

## Core Protocols

**Inter-agent communication:** Plain-text Markdown files in `handoff/` only. Never use nested JSON between agents — it causes silent schema degradation.

**State write-backs** must include: `[Source]`, `[Confidence: High/Medium/Low]`, `[Timestamp]`.

**Revision loop cap:** Builder↔Reviewer limited to 2 rounds. Escalate to human operator on failure.

**Prompt caching:** Static context (system prompts, CLAUDE.md, tool schemas) goes first with `cache_control: {"type": "ephemeral"}`. Dynamic data (logs, user input) goes at the end of every request.

## SDK Usage

```python
from claude_agent_sdk import query, ClaudeAgentOptions

async for message in query(
    prompt="...",
    options=ClaudeAgentOptions(
        allowed_tools=["Agent", "Read", "Edit"],
        setting_sources=["project"],   # inherits .claude/ and CLAUDE.md
        permission_mode="acceptEdits",
        model="claude-sonnet-4-6"
    )
):
    if hasattr(message, "result"):
        print(message.result)
```

## Skill File Structure

Each `.claude/skills/<name>/SKILL.md` uses YAML frontmatter with: `name`, `description`, `hooks` (PostToolUse matchers). Skills follow Progressive Disclosure — only injected when trigger conditions are met.
