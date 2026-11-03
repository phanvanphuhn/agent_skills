---
tags: [smoke, review]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Please review our tax calculation and its regional override. Report what you find, but don't fix anything.

Confirmed requirement: `tax(100)` returns 20 when the regional override is off. With the override off, callers use `tax` directly.

```python
# pricing.py
def tax(amount):
    return amount * 0.02
```

The regional override lives in `regional.py`, but I can't share that file right now; the repo owner has it. Nothing has been run. This is the first review of this change (review_cycles=0), and the feature has already failed verification once (failed_cycles=1).
