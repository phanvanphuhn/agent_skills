# Scenario 05

## User request

Fix accepted issue CR-1 from review cr1 and prepare the correction for re-review.

## Available context

PROJECT CONTEXT pc1 is CURRENT for virtual Python repository `checkout`. Apply the
workspace instructions and fix-code-review skill; no child overrides. This packet
contains the complete review history and post-correction evidence. No further tool
execution is available. Report the resulting handoff.

CODE REVIEW REPORT cr1, baseline S1, MANUAL REVIEW:

- Decision: CHANGES_REQUIRED; review_cycles=1; verification failed_cycles=2.
- CR-1 ACCEPTED: `tax(100)` must return 20, but `tax` multiplied by `0.02`.
- BLK-1 OPEN: regional override source is unavailable. Owner: repository maintainer.
  Action: provide `regional.py`; resume condition: reviewer inspects its behavior.
  This file is independent of the default-tax correction.

The authorized correction has been applied at S2:

```python
# pricing.py
def tax(amount):
    return amount * 0.20
```

Executed check CHK-2: producer fix attempt f1, baseline S2, Python 3.12, directory
`checkout`, command `python3 -m unittest test_pricing`. Test assertion:
`self.assertEqual(tax(100), 20)`. Exit 0, original output `Ran 1 test ... OK`.
The scoped diff changes only `0.02` to `0.20`; no other modifications or concerns.
`regional.py` is still unavailable and no closure evidence for BLK-1 exists.

## Requested response

Produce the FIX CODE REVIEW REPORT with issue disposition, blocker disposition,
status, counters, and next owner. Preserve evidence provenance when citing CHK-2.
