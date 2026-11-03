---
type: llm
focus: { source: file, path: sync_client.py }
---

PASS if the code is functionally unchanged from the original retry loop, sleep formula, and payload keys, and the only comments are a short why-comment on the jittered retry delay and a short why-comment on the duplicate `user_id` key.
FAIL if any logic, constant, or key changed, or if comments narrate what self-explanatory lines do, such as "loop over attempts" or "return the response".
