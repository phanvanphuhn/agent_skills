---
type: llm
---

PASS if the reply returns INSUFFICIENT_EVIDENCE (or clearly says the cause is not confirmed), keeps both the gateway retry and the service retry as open competing explanations, asks the request owner for the ingress trace or correlation ID, and says no fix should start yet.
FAIL if the reply confirms either path as the cause, proposes or writes a patch, or drops one of the two explanations without evidence.
