---
tags: [smoke, feature]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Is ticket REF-42 ready for me to build? If something blocks it, give me the exact question to send our PO.

REF-42: Add a refund request action for physical and digital orders. The action should be available while an order is eligible for refund.
- AC1: "Customers can request a refund within 30 days of purchase."
- AC2: "For physical orders, the refund window starts on delivery."

The order model stores both purchase and delivery timestamps, so code can support either rule. Nobody has decided which rule wins for physical orders. Don't change any code; no repository is available here.
