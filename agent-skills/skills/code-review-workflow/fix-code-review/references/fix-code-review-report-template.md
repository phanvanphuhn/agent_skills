# FIX CODE REVIEW REPORT

- Task / bug / review target: <matching CODE REVIEW REPORT>
- Project context: <PROJECT CONTEXT revision for the reviewed/current baseline>
- Input CODE REVIEW REPORT: <revision/baseline; CHANGES_REQUIRED or human-directed REVIEW_ESCALATION>
- Explicit authorization: <user instruction authorizing fixes>
- Review cycle: <review_cycles carried unchanged from CODE REVIEW REPORT>
- Fix attempt: <attempt identity; separate from review_cycles>
- Status: <READY_FOR_RE_REVIEW / BLOCKED>
- Pre-fix baseline: <exact commit/diff/worktree state>
- Post-fix baseline: <exact commit/diff/worktree state or partial state>

## Issue Disposition

### <CR-ID> — <short title>

- Disposition: <ACCEPTED / REJECTED_FINDING / NEEDS_CONTEXT / BLOCKED>
- Evidence: <why this disposition is correct>
- Correction: <changed file/symbol and resulting behavior; N/A unless ACCEPTED>
- Regression coverage: <test/check tied to the issue>

## Files Changed

- `<path>` — <issue ID and smallest correction; distinguish pre-existing changes>

## Self-Tests

Use the shared [check evidence record](../../../references/check-evidence.md).
List CHK-* records and reference their IDs for each corrected issue.

## Remaining Issues and Risks

- <open/rejected/context-dependent issue, risk, or none>

## Carried Review Blockers

- <BLK-ID>: <OPEN / EVIDENCE_SUPPLIED>; <originating report; scope; owner; action;
  resume condition; new evidence or unchanged reference>

Reconcile every inherited unresolved ID. Only code-review confirms RESOLVED; fixing
CR-* findings does not close BLK-* gaps. Cite already-resolved history without copying it.
State `None` only if the input review has no unresolved blockers and none were discovered.

## Cycle History

1. <review decision → explicit authorization → fix attempt → self-test result>

## Handoff

- Next stage / owner: <code-review targeted re-review; human/upstream owner if blocked>
- Re-review scope: <original issues, fix diff, affected tests, and preserved behavior>
- Resume condition: <only when blocked/escalated>

Do not claim APPROVED. Only a new CODE REVIEW REPORT may approve the post-fix baseline.
