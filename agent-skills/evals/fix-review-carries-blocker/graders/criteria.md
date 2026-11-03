---
type: llm
---

PASS if the reply marks CR-1 corrected with status READY_FOR_RE_REVIEW, carries BLK-1 forward as still open with its owner, action, and resume condition, keeps review_cycles=1 and failed_cycles=2, cites CHK-2 as the earlier fix-attempt run rather than a new one, and routes the change back to code review.
FAIL if the reply drops, closes, or renumbers BLK-1, returns BLOCKED for the whole fix only because of BLK-1, approves the change or declares it done, changes either counter, or claims a new test run.
