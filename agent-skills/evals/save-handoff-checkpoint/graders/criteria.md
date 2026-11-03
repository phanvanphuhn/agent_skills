---
type: llm
---

PASS if the reply contains both a HANDOFF.md and a CHANGELOG.md for one PAY-7 folder, labels the status CHECKPOINT, preserves the full r1 contract with AC1's original wording, marks gateway verification BLOCKED or NOT_RUN with the environment owner and resume condition, keeps review_cycles and failed_cycles at 0, and states plainly that the files were not saved.
FAIL if the reply claims the task is DONE or verification passed, claims the integration check ran, claims files were saved when they were not, omits the contract or the changelog, or rewrites AC1.
