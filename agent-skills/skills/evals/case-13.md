# Scenario 13

## User request and selected stage

The user asks to diagnose a checkout bug. Refresh PROJECT CONTEXT before bug-analysis.

## Available context

- Target repository: `checkout`, a Python service. Repository boundary and applicable
  `AGENTS.md` were resolved in prior PROJECT CONTEXT pc1.
- Only the supplied summary of pc1 is accessible. It reports CURRENT repository
  topology, architecture, entry points, component ownership, and instructions, and
  maps `app/pricing.py` to checkout totals and `tests/unit/test_pricing.py` to focused
  coverage. The complete pc1 body and current Git/worktree snapshot are unavailable.
- Since pc1, only `pyproject.toml` changed. Its test command changed from
  `pytest tests/` to `pytest tests/unit/`. No source, interface, architecture,
  instruction, or other manifest changes are reported.
- The changed manifest content is supplied above. No repository filesystem or
  execution environment is available in this scenario.

## Requested response

Produce the project-discovery outcome for the bug-analysis handoff. Distinguish
reused pc1 facts from the refreshed command. Do not restart broad discovery or claim
to have run tests.
