# TASK HANDOFF

- Task ID: <supplied ticket/task ID, or generated TASK-YYYYMMDD-NN>
- Description: <short kebab-case description used in folder name>
- Handoff folder: <agent-skills/handoffs/TASK-YYYYMMDD-NN-description/ or supplied-ID-description/>
- Handoff revision / date: <h1 and local date>
- Status: <DONE / REVIEW_COMPLETE / NORMAL_COMPLETE / CHECKPOINT>
- Target and repository baseline: <repository root, branch, full commit; relevant dirty/untracked file list AND content identity, such as per-file SHA-256 or a reproducible sorted-path manifest digest; include the manifest and digest method here, and name any generated handoff files excluded from the digest>
- Project context: <saved PROJECT CONTEXT path and revision, or reason unavailable>
- Governing artifacts: <contract/report IDs and revisions, or none>
- Workflow state: <applicable failed_cycles, review_cycles, failed_cycles_for_root_cause, total_fix_cycles; governing revisions; stable finding/blocker IDs and statuses, or not applicable>

## Task Inputs

- Original request and scope: <concise, faithful summary; retain ticket/AC IDs and original wording where applicable>
- Supplied inputs: <files, links, decisions, constraints, environment facts and their source>
- Authorized actions: <what the user authorized for this task>

## Outputs

- Deliverables: <paths, artifacts, behavior or documentation produced>
- Changed files: <actual task-owned changes; distinguish unrelated work>
- Current outcome: <what is complete, with exact status and artifact references>

## Definition of Done

| Item / original AC ID | Required result | Status | Evidence or gap |
| --- | --- | --- | --- |
| <ID or task-specific DoD item> | <observable condition> | <MET / NOT_MET / BLOCKED / NOT_APPLICABLE> | <path/report/check with baseline, or missing prerequisite> |

State when no explicit DoD was supplied; use only observable task outcomes rather than
inventing acceptance criteria. Feature and bug DONE require the applicable verification
PASS on the recorded approved baseline.

## Implementation or Investigation Flow

1. <Major stage and decision with relevant artifact/path>
2. <Change or investigation result and why it was needed>
3. <Review, verification, and final outcome; omit stages that did not occur>

Summarize observable decisions and work, not hidden reasoning or a conversation log.

## Checks and Evidence

- Executed: <command or manual check, result, environment, and exact input content identity matching the baseline above; or none>
- Not run / blocked: <required or material check, reason, owner, resume condition; or none>
- Evidence limits: <mocked boundary, stale result, UNKNOWN historical baseline, or other qualification; or none>

## Governing Artifacts for Resume

- Persisted artifacts: <accessible file paths with exact revision/status, or none>
- Conversation-only artifacts required by the next stage: <include each complete
  current artifact body here, with revision, status, original AC wording, decisions,
  evidence limits, and counters; or none>
- Missing content: <artifact/section that cannot be preserved safely, owner, and resume
  condition; or none>

An artifact ID or paraphrase alone does not make a conversation-only contract accessible
to a fresh session. Preserve the full governing body needed by the owning next stage.

## Open Items and Risks

- <remaining work, blocker, owner, and resume condition; or none>

## Resume in a Fresh Session

Read this file, its sibling `CHANGELOG.md`, the cited PROJECT CONTEXT, and current
repository instructions. Compare the saved baseline with the worktree, inspect the
referenced artifacts/code, and continue at <next owning stage or new task>. Revalidate
any conclusion or check evidence affected by changes since this handoff.
