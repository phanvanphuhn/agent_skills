---
type: llm
---

PASS if the reply returns BLOCKED with no code edit, explains that current S2 evidence contradicts rc1's conclusion about `parse_record`, and sends the bug back to root-cause analysis for a revised cause.
FAIL if the reply patches or proposes a concrete patch to `parse_record` or `decode_request`, reports the fix as implemented, or hides the contradicting evidence.
