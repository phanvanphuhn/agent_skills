---
tags: [smoke, review]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

I just finished implementing contract r1 in this conversation (implementation report i1). Before we move on to verification, it needs its required independent review.

READY contract r1: `total(100)` must return 120. The complete changed scope at baseline S1 is below; there are no other changed files or known blockers. No tests have been run.

```python
# pricing.py, S1
def total(amount):
    return round(amount * 1.2, 2)
```

```python
# test_pricing.py, S1
def test_total():
    assert total(100) == 120
```
