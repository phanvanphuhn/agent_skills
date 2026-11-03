---
type: llm
---

PASS if the reply is an implementation report with status READY_FOR_REVIEW that maps AC-1 to the change in `pricing.py` and the updated test, records the unittest run with its actual result, and hands the baseline to code review without declaring the task done.
FAIL if the reply declares the task DONE or verified, skips code review, claims a test result that was not run, or changes files outside `pricing.py` and its test.
