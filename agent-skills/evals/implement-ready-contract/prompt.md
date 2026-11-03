---
tags: [writes, feature]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Go ahead and implement this approved contract in the repository in the current directory. You're authorized to change code and tests. Run `python3 -m unittest test_pricing` when you're done.

READY TASK CONTRACT r1 (validation report v1: READY, implementation authorized)
- AC-1 (original): "Checkout totals include 20% tax: `total(100)` returns 120."
- Scope: `pricing.py` and its test. Keep the public signature `total(amount)`.
- Verification: `python3 -m unittest test_pricing` passes on the changed baseline.
