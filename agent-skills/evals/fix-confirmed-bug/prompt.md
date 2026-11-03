---
tags: [writes, bug]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Please fix BUG-80 in the repository in the current directory. You're authorized to change code and tests for the confirmed cause below. Run `python3 -m unittest test_quantity` afterwards.

- Bug write-up b1: the cart quantity form rejects `" 3 "` with an error, although quantities padded with spaces have always been accepted.
- Reproduction report rp1: REPRODUCED. `parse_qty(" 3 ")` raises `ValueError` on the current HEAD.
- Root-cause report rc1: CONFIRMED. `quantity.parse_qty` runs its `isdigit()` check on the raw form value. A recent refactor removed the `.strip()` call, and form values keep their surrounding whitespace, so padded digits fail the check. Preserve: values below 1 are still rejected. Required test: a padded value such as `" 3 "` parses to 3.
