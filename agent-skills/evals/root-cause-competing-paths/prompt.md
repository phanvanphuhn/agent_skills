---
tags: [smoke, bug]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Find the root cause of BUG-72 before anyone attempts a fix.

- The bug write-up and reproduction report rp1 confirm that retrying one payment request causes a duplicate charge in test environment T1.
- The execution record shows two charge calls, but the trace starts only after the request enters the service. It can't show whether the HTTP gateway sent the request twice or the service retried internally.
- The code has a gateway retry policy and a separate service retry path; either could explain the second call.
- No correlation ID or earlier trace segment is available. The request owner can provide the ingress trace.
