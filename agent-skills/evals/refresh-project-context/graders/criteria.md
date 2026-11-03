---
type: llm
---

PASS if the reply returns a PARTIAL project context for `checkout` that reuses pc1's stated map, updates only the test command to `pytest tests/unit/`, names the unavailable full pc1 and Git state as a gap that does not block the next step, does not claim tests ran, and hands off to bug analysis.
FAIL if the reply rebuilds the architecture from files that don't exist, keeps the old `pytest tests/` command, presents pc1 facts as freshly inspected, claims test execution, or refuses to hand off because of the immaterial gap.
