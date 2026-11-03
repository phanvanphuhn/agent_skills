---
type: llm
---

PASS if the reply is a verification report with final status PASS that maps AC-1 to an actually executed `python3 -m unittest test_pricing` run on the current baseline, records its command and observed result, confirms the baseline still matches the approved commit, and keeps failed_cycles at 0.
FAIL if the reply passes without running the check, records a result that wasn't observed, changes code or tests, or returns FAIL or BLOCKED despite a passing run on the approved baseline.
