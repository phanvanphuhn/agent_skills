# Scenario 02

## User request

Review the tax calculation and its regional override. Report findings; do not fix them.

## Available context

PROJECT CONTEXT pc1 is CURRENT for virtual Python repository `checkout`, baseline S2.
All applicable instructions are supplied workspace rules and the code-review skill;
there are no child overrides. Use MANUAL REVIEW. The current review has not yet issued
a report. Prior review_cycles=0; feature failed_cycles=1. Prior reports are accessible.

The user-confirmed requirement is: `tax(100) returns 20 when the regional override is off`.
The override-off path calls `tax` directly with no transformation. Current source:

```python
# pricing.py
def tax(amount):
    return amount * 0.02
```

Review of the regional override is also explicitly required, but `regional.py` cannot
be read and no execution evidence for it is available. The repository owner can provide
that file; its behavior must be inspected before regional review can be completed.
No evidence establishes whether the regional behavior is correct or broken.

## Requested response

Produce the CODE REVIEW REPORT: findings, any missing evidence, decision, resulting
counters, and next owner/action. No new check execution results are available.
