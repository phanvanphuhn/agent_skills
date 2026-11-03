---
tags: [smoke, feature]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Can you confirm the reviewed checkout change meets its acceptance criterion so we can call it done? Reuse the earlier test run if it's still valid. Don't touch production code. You can't run anything here; use only what I paste.

- READY contract r1, AC-1: `total(100) returns 120`. Required check: run `python3 -m unittest test_pricing` on the current baseline.
- Code review cr2 APPROVED baseline S2. Previous verification failed once: failed_cycles=1.
- S1 and S2 share Git commit `abc123` but have different uncommitted content.

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

Earlier run CHK-1: `python3 -m unittest test_pricing` on S1, Python 3.12, exit 0, output `Ran 1 test ... OK`. Nobody has run anything on S2. A teammate says CHK-1 still counts because the commit matches.
