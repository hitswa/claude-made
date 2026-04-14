"""
Agent runners for the Orchestrator-Worker triad.
Each function maps to one agent persona defined in .claude/agents/.
"""

from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

HANDOFF_DIR = Path("handoff")
TASK_BRIEF = HANDOFF_DIR / "task_brief.md"
BUILD_RESULT = HANDOFF_DIR / "build_result.md"
REVIEW_RESULT = HANDOFF_DIR / "review_result.md"


async def run_architect(user_request: str) -> str:
    """
    Architect: decomposes user_request into a task brief.
    Writes output to handoff/task_brief.md.
    Returns the brief content.
    """
    prompt = (
        f"User request:\n\n{user_request}\n\n"
        "Decompose this into a task brief and write it to handoff/task_brief.md "
        "following your agent instructions."
    )
    result = ""
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Write"],
            setting_sources=["project"],
            permission_mode="plan",
            model="claude-sonnet-4-6",
        ),
    ):
        if hasattr(message, "result") and message.result:
            result = message.result

    return result


async def run_builder() -> str:
    """
    Builder: reads handoff/task_brief.md and implements the task.
    Writes output to handoff/build_result.md.
    """
    brief = TASK_BRIEF.read_text() if TASK_BRIEF.exists() else ""
    prompt = (
        f"Task brief (from handoff/task_brief.md):\n\n{brief}\n\n"
        "Implement the task exactly as specified. "
        "Write your completion report to handoff/build_result.md."
    )
    result = ""
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Write", "Edit", "Bash"],
            setting_sources=["project"],
            permission_mode="acceptEdits",
            model="claude-sonnet-4-6",
        ),
    ):
        if hasattr(message, "result") and message.result:
            result = message.result

    return result


async def run_reviewer(loop: int) -> tuple[bool, str]:
    """
    Reviewer: validates build_result.md against task_brief.md.
    Writes verdict to handoff/review_result.md.
    Returns (passed, review_text).
    """
    brief = TASK_BRIEF.read_text() if TASK_BRIEF.exists() else ""
    build = BUILD_RESULT.read_text() if BUILD_RESULT.exists() else ""
    prompt = (
        f"This is revision loop {loop} of 2.\n\n"
        f"Task brief:\n{brief}\n\n"
        f"Build result:\n{build}\n\n"
        "Validate the implementation strictly against the acceptance criteria. "
        "Write your verdict to handoff/review_result.md."
    )
    result = ""
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Write"],
            setting_sources=["project"],
            permission_mode="plan",
            model="claude-haiku-4-5-20251001",
        ),
    ):
        if hasattr(message, "result") and message.result:
            result = message.result

    review_text = REVIEW_RESULT.read_text() if REVIEW_RESULT.exists() else result
    passed = "verdict: pass" in review_text.lower()
    return passed, review_text
