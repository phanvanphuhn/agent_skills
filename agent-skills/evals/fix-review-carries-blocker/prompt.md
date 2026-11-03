---
tags: [smoke, review]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Fix accepted issue CR-1 from review cr1 and get it ready for re-review. The correction is already applied below; I just need the fix report and handoff. You can't run anything further.

Review cr1 at baseline S1: CHANGES_REQUIRED, review_cycles=1, verification failed_cycles=2.
- CR-1 (accepted): `tax(100)` must return 20, but `tax` multiplied by `0.02`.
- BLK-1 (open): `regional.py` is unavailable. Owner: repository maintainer. Action: provide `regional.py`. Resume when a reviewer has inspected it. It is independent of CR-1.

Current S2:

```python
# pricing.py
def tax(amount):
    return amount * 0.20
```

Check CHK-2 from fix attempt f1 on S2, Python 3.12: `python3 -m unittest test_pricing`, asserting `tax(100) == 20`, exit 0, output `Ran 1 test ... OK`. The diff changes only `0.02` to `0.20`. `regional.py` is still unavailable.
