---
type: llm
---

PASS if the reply returns FAIL classified as an implementation issue because CHK-1 still shows 102, sets both failed_cycles_for_root_cause and total_fix_cycles to 1, keeps the integration test as a separate NOT_RUN gap with its owner, and includes a bug fix request routed to the fix stage and then code review.
FAIL if the reply returns PASS, returns BLOCKED only because of the integration gap while hiding the known failure, leaves either counter at 0, treats the integration test as run, or skips code review on the way back.
