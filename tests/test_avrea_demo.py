"""Avrea demo only, not part of upstream FastAPI.

Fails on every other workflow run, so Avrea Test Intelligence has a test that
flips between runs of the same commit to show.
"""

import os


def test_alternates_between_runs() -> None:
    run_number = int(os.environ.get("GITHUB_RUN_NUMBER", "0"))
    assert run_number % 2 == 0, f"run {run_number}: odd runs fail on purpose"
