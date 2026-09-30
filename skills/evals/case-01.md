# Scenario 01

## User request

Verify the reviewed checkout change against contract r1. Reuse existing check evidence
where valid. Do not change production code.

## Available context

This is a supplied virtual repository snapshot, not a path on the evaluator's machine.
PROJECT CONTEXT pc1 is CURRENT for `checkout`, a Python library. Applicable instructions
are the workspace rules and verification skill; there are no child overrides.
Only supplied execution records are available; a current runtime cannot be accessed.

- Complete READY TASK CONTRACT r1: AC-1 (original wording): `total(100) returns 120`.
  Scope: `pricing.py`; preserve its public signature. Required check: execute
  `python3 -m unittest test_pricing` against the current baseline. No other ACs,
  requirements, unknown product decisions, or verification obligations.
- VALIDATION REPORT v1: r1 is READY, implementation authorized.
- IMPLEMENTATION REPORT i2: implements AC-1 at S2, READY_FOR_REVIEW.
- CODE REVIEW REPORT cr2: APPROVED for r1/S2; review_cycles=0.
- Previous verification: failed_cycles=1; retain that history.

Snapshots use the same Git commit `abc123` but different dirty content identities:

```python
# S1/pricing.py
def total(amount):
    return round(amount * 1.2, 2)

# S2/pricing.py (current)
def total(amount):
    return round(amount + amount * 0.2, 2)

# test_pricing.py (unchanged)
import unittest
from pricing import total

class PricingTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(100), 120)
```

Accessible original CHK-1: executed by verification report v0 on S1 in `checkout`,
using `python3 -m unittest test_pricing`, Python 3.12, r1 and the supplied test content.
Exit 0; raw output: `Ran 1 test ... OK`.
No current S2 execution record exists. The earlier report proposes reusing CHK-1
because the Git commit and environment labels match.

## Requested response

Produce the verification disposition, evidence reuse decision, failed-cycle count,
and next action. Distinguish observed execution from proposed checks.
