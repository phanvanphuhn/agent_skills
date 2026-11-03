---
type: llm
---

PASS if the reply routes the request to the bug workflow with high confidence because existing, specified behavior is broken, and stops there without investigating.
FAIL if the reply routes to the feature workflow or a general answer, invents a cause, inspects code, or produces a full bug write-up despite the user asking only for the route.
