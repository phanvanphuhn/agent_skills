---
tags: [smoke, bug]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

You're authorized to apply the fix for BUG-73 using root-cause report rc1. Fix the confirmed cause only; no new investigation or speculative patches.

- The bug write-up and reproduction report rp1 describe malformed UTF-8 in imported records.
- rc1 concluded that `parse_record` drops malformed bytes.
- Before editing, I inspected the current baseline S2. In S2, `parse_record` keeps and flags malformed input; the failing fixture reaches `decode_request` with the bytes already missing. A current-baseline test confirms this.
- There are no unrelated local changes.

What's the fix status, and should code change now?
