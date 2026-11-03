---
tags: [writes, comment]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Edit]
---

Please clean up the comments in `sync_client.py` in the current directory. Background you can rely on: the upstream API rate-limits clients that retry in lockstep, which is why the retry delay has random jitter; and older mobile clients still read only the `user_id` key, which is why the payload sends the id twice. Don't change any behavior.
