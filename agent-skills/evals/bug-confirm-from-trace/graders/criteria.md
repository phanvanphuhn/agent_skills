---
type: llm
---

PASS if the reply marks the bug confirmed by evidence (EVIDENCE_CONFIRMED or equivalent) on the strength of the matching server trace, distinguishes the failed desktop attempt from that trace, makes no cause claim, and sends the investigation to root-cause analysis next.
FAIL if the reply says the bug cannot be reproduced while ignoring the trace, claims a local Android reproduction, speculates about or asserts a cause, or proposes a production code change.
