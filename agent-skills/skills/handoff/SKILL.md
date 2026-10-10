---
name: handoff
description: "On explicit user request, save a self-contained task handoff and task changelog for a completed task or unfinished checkpoint."
---

# Handoff

## Purpose

Preserve the task's outcome and the evidence needed to resume in a fresh conversation
without relying on the prior conversation transcript.

## Use when

Run only when the user explicitly invokes `$handoff` or asks to create a handoff.
Task completion alone never triggers this skill. A completed feature or bug is DONE
only after verification PASS. Label an unfinished handoff CHECKPOINT and retain blockers.

## Inputs

- Original user request and supplied inputs, including requirement or bug artifact IDs.
- Current PROJECT CONTEXT, governing instructions, task artifacts, decisions, and status.
- Actual changed-file/worktree baseline, outputs, review and verification reports, and
  executed check evidence when relevant.
- Prior handoff for the same task, if this is a later revision.

## Walk It Down

- Start: Collect the final task status, inputs, outputs, exact baseline, and accessible evidence.
- Expand: Inspect only the files or artifacts needed to resolve a missing handoff fact or stale status.
- Stop: Stop when a fresh session can identify what was done, what remains, and how to verify the current baseline.

## Required outcome

Create one dedicated folder under `../../handoffs/` for the task. It contains exactly
`HANDOFF.md` and `CHANGELOG.md`, following the
[handoff template](references/handoff-template.md) and
[task changelog template](references/task-changelog-template.md). Name the folder
`<taskID>-<description>`, with the supplied ticket/task ID when available and a short
kebab-case description. If no ID was supplied, allocate a stable local ID such as
`TASK-YYYYMMDD-NN` using the next unused number for that date; record the ID in both
files. Keep the same folder for later revisions of the same task and append a dated
changelog entry instead of replacing history. Do not reuse an ID for a different task.

The handoff must state the task inputs, concrete outputs, Definition of Done and its
evidence, implementation or investigation flow, exact repository baseline, open items,
and a short fresh-session resume instruction. Link to accessible source artifacts and
checks. For any governing artifact that exists only in the conversation, preserve its
complete current body in `HANDOFF.md` when the next stage requires that artifact;
retain original acceptance-criterion wording, revisions, statuses, and evidence limits.
For relevant dirty or untracked inputs, record content fingerprints or an immutable
snapshot with a reproducible file list and digest method; paths plus HEAD are not an
exact baseline. Tie each reusable check or review result to its recorded input baseline.
If a historical result lacks content identity, mark that baseline UNKNOWN and require
fresh evidence before reuse.
Record applicable review and verification counters with their governing revision and
stable finding/blocker IDs. The old conversation must not be needed to resume.
The changelog records only this task's material changes and outcome transitions.
Return the two saved paths and the recorded status in the final response.

## Boundaries

The handoff is a summary, not a new review or verification result. Never infer DONE
from code changes, proposed checks, or an approval without required verification PASS.
Do not turn unknown or blocked DoD items into completed ones. Do not copy secrets,
private payloads, or entire conversations. If a required artifact cannot be preserved
safely, name the missing content and its owner as a resume blocker. Preserve unrelated files and prior task
history; write only this task's two files. If the destination cannot be written,
return both documents in the conversation and state the persistence gap.

## Handoff

A fresh session should read `HANDOFF.md`, its `CHANGELOG.md`, the cited PROJECT CONTEXT,
and current repository instructions; then compare the saved baseline to the current
worktree before reusing conclusions or execution evidence. Continue through the
owning workflow stage if the recorded status is CHECKPOINT or later facts changed.
