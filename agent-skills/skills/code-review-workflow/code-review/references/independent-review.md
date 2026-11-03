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

In Claude Code, dispatch this plugin's `fresh-reviewer` subagent (namespaced
`agent-skills:fresh-reviewer`) through the Agent tool with the complete packet as its
prompt. The subagent starts without the implementation conversation and receives only
the packet, which establishes reviewer separation. Record the subagent type, the packet
baseline, and its returned report; merge its findings into the gate's CODE REVIEW
REPORT without softening them.

Recheck the worktree before treating APPROVED as applicable. If the subagent is
unavailable and no other separate reviewer is, return the copy-ready packet and an
OPEN separation blocker.
