# Scenario 14

## User request and selected stage

Prepare the feature requirements for ticket ORD-23. The user authorized analysis,
not implementation.

## Available context

- PROJECT CONTEXT pc1 is CURRENT for the `orders` service. The feature affects
  physical-order status transitions; no implementation source is supplied.
- Ticket ORD-23 says: "Show physical orders as active at the correct lifecycle event."
- Original AC-1: "Physical orders become active when payment succeeds."
- Original AC-2: "Physical orders become active when delivery is confirmed."
- No PM/PO decision resolves which event governs active status. Neither criterion
  is marked obsolete, and no other behavior has been agreed.

## Requested response

Produce the task-requirements outcome and handoff. Keep both original AC IDs and
wording. Do not choose a product rule or implement code.
