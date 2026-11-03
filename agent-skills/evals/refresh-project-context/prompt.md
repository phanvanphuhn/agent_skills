---
tags: [smoke, discovery]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

We're about to diagnose a checkout bug. First bring our project map for the `checkout` Python service up to date.

All I have is the summary of our previous project map pc1: it was current for the repository layout, architecture, entry points, ownership, and instructions; it maps `app/pricing.py` to checkout totals and `tests/unit/test_pricing.py` to focused tests. The full pc1 document and the current Git state aren't available.

Since pc1, only `pyproject.toml` changed: its test command went from `pytest tests/` to `pytest tests/unit/`. Nothing else changed. There's no repository checked out here and nothing can be run.
