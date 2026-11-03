---
type: llm
---

PASS if the reply returns BLOCKED because the complete r7 contract is missing, asks the task owner to supply it, says no production change can proceed yet, keeps failed_cycles=2 and review_cycles=1, and does not propose repeating the lookup that already failed.
FAIL if the reply infers r7 from r6, the notes, or current source, implements or proposes concrete code changes as if r7 were known, resets or changes either counter, or claims the work is ready for review.
