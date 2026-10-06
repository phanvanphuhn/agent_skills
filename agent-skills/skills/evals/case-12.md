# Scenario 12

## New top-level user request

"Checkout now returns 102 for a 100-unit order, but the existing acceptance
criterion says 120. Diagnose why it is broken; do not change files."

## Available context

- This is a new request, not a follow-up in an active workflow.
- No repository or ticket artifact is available at the routing stage.
- No user-provided material names a skill or asks for a product behavior change.

## Requested response

Return only the task-router output. Do not investigate, inspect a repository, or
prepare a downstream artifact.
