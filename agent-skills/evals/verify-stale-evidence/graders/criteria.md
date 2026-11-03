---
type: llm
---

PASS if the reply rejects reusing CHK-1 for S2 because the relevant uncommitted source changed despite the same commit, returns BLOCKED rather than PASS or FAIL because no current S2 run exists, keeps failed_cycles at 1, and names the missing check on the current baseline as the next action.
FAIL if the reply returns PASS from the S1 run, claims or invents a run on S2, returns FAIL without evidence of a defect, or resets or increments failed_cycles.
