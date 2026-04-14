"""
Orchestrator-Worker pipeline.
Runs the full Architect → Builder → Reviewer cycle with a 2-loop revision cap.

Usage:
    python -m src.pipeline "Add a hello-world FastAPI endpoint"
"""

import asyncio
import shutil
import sys
from datetime import datetime, timezone

from dotenv import load_dotenv

from src.agents import run_architect, run_builder, run_reviewer, HANDOFF_DIR

load_dotenv()

MAX_REVISION_LOOPS = 2


def _archive_handoff() -> None:
    """Move existing handoff files to handoff/archive/<timestamp>/ before a new cycle."""
    archive_files = list(HANDOFF_DIR.glob("*.md"))
    if not archive_files:
        return
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archive_dir = HANDOFF_DIR / "archive" / ts
    archive_dir.mkdir(parents=True, exist_ok=True)
    for f in archive_files:
        shutil.move(str(f), archive_dir / f.name)
    print(f"[pipeline] Archived previous handoff to {archive_dir}")


async def run_pipeline(user_request: str) -> None:
    print("\n=== MULTI-AGENT PIPELINE START ===")
    print(f"Request: {user_request}\n")

    _archive_handoff()

    # --- Phase 1: Architect ---
    print("[1/3] Architect: decomposing request...")
    await run_architect(user_request)
    print(f"      Brief written to {HANDOFF_DIR / 'task_brief.md'}\n")

    # --- Phase 2 & 3: Builder + Reviewer (up to MAX_REVISION_LOOPS) ---
    for loop in range(1, MAX_REVISION_LOOPS + 1):
        print(f"[2/3] Builder: implementing (loop {loop}/{MAX_REVISION_LOOPS})...")
        await run_builder()
        print(f"      Result written to {HANDOFF_DIR / 'build_result.md'}\n")

        print(f"[3/3] Reviewer: validating (loop {loop}/{MAX_REVISION_LOOPS})...")
        passed, _ = await run_reviewer(loop=loop)
        print(f"      Verdict written to {HANDOFF_DIR / 'review_result.md'}")

        if passed:
            print(f"\n=== PIPELINE COMPLETE: PASS (loop {loop}) ===\n")
            return

        if loop < MAX_REVISION_LOOPS:
            print(f"      FAIL — sending back to Builder for revision {loop + 1}...\n")
        else:
            print(
                "\n=== PIPELINE HALTED ===\n"
                f"Review FAILED after {MAX_REVISION_LOOPS} loops.\n"
                f"Human intervention required. See {HANDOFF_DIR / 'review_result.md'}\n"
            )
            sys.exit(1)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m src.pipeline \"<your task description>\"")
        sys.exit(1)
    user_request = " ".join(sys.argv[1:])
    asyncio.run(run_pipeline(user_request))


if __name__ == "__main__":
    main()
