---
type: llm
---

PASS if the reply reports a blocking finding that `tax(100)` returns 2 instead of 20 because of the `0.02` multiplier, returns CHANGES_REQUIRED with review_cycles=1, separately keeps an open blocker that `regional.py` was not reviewed and the repo owner must supply it, and makes no edits.
FAIL if the reply approves, returns only BLOCKED while hiding the confirmed tax defect, invents a defect in the unseen regional code, drops the regional blocker, leaves review_cycles at 0, or applies a fix.
