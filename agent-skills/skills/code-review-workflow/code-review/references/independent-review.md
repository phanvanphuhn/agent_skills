# Independent review packet

Use this only for a REQUIRED GATE. A fresh reviewer must inspect the actual current
source; a different label in the same conversation does not establish separation.

## Packet contents

- Target repository and exact review scope: base/head commits or supplied snapshot,
  changed paths, relevant dirty/untracked content identities, and excluded local work.
- Complete governing READY contract or confirmed root-cause revision, plus the
  implementation/fix report and any prior review findings or OPEN blockers. Include
  complete bodies for conversation-only artifacts needed to judge the change.
- Paths to actual code, tests, and accessible CHK-* results, with each result's
  execution baseline and limits. A summary is a pointer, not replacement source.
- A request for a read-only CODE REVIEW REPORT on this baseline, including issue and
  blocker IDs, `review_cycles`, coverage gaps, and reviewer-context provenance.

Omit secrets, unrelated files, and the implementation conversation. If source or a
required artifact is unavailable, name the owner and missing item in the packet.

## Fresh-session launch

When a separate local Codex CLI session is available, save the packet outside the
repository and use a fresh, read-only run such as:

```bash
codex --ask-for-approval never exec --ephemeral --ignore-user-config \
  --sandbox read-only --cd /absolute/repository/path - < /absolute/review-packet.md
```

The packet must include the review skill and report template when user config is
ignored. The command is an example; confirm the installed CLI supports its options.
Record the new session identity, packet/content baseline, tool access, and resulting
report. Recheck the worktree before treating APPROVED as applicable. If no separate
reviewer is available, return the copy-ready packet and an OPEN separation blocker.
