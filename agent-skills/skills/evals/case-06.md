# Scenario 06

## User request

As the developer, validate this feature ticket before I implement it. If something
blocks the work, give me the exact question I can take to the PM or PO.

## Ticket and available evidence

- Ticket `REF-42`: Add a refund request action for physical and digital orders.
- Description: The action should be available while an order is eligible for refund.
- AC1, original: "Customers can request a refund within 30 days of purchase."
- AC2, original: "For physical orders, the refund window starts on delivery."
- PROJECT CONTEXT pc1 is CURRENT for the target checkout repository. The order model
  records both purchase and delivery timestamps; code cannot decide which conflicting
  product rule takes precedence. There are no other known blockers.
- No PM/PO decision, policy document, or ticket amendment resolves AC1 versus AC2.
- DRAFT TASK CONTRACT r1 preserves AC1 and AC2 exactly as written and flags their
  physical-order start event as unknown U1. No additional criteria or conflicts exist.

## Requested response

Return the validation status, the developer-facing question, its owner and affected
criteria, and the condition for resuming implementation. Do not change code.
