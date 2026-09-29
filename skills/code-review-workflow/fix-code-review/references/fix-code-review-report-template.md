# FIX CODE REVIEW REPORT

- Task / bug / review target: <matching CODE REVIEW REPORT>
- Project context: <PROJECT CONTEXT revision for the reviewed/current baseline>
- Input CODE REVIEW REPORT: <revision/baseline and CHANGES_REQUIRED decision>
- Explicit authorization: <user instruction authorizing fixes>
- Review-fix cycle: <1-3; retain prior history>
- Status: <READY_FOR_RE_REVIEW / BLOCKED>
- Pre-fix baseline: <exact commit/diff/worktree state>
- Post-fix baseline: <exact commit/diff/worktree state or partial state>
- Context used: <maximum F0-F4 and reason for expansion beyond F1>

## Issue Disposition

### <CR-ID> — <short title>

- Disposition: <ACCEPTED / REJECTED_FINDING / NEEDS_CONTEXT / BLOCKED>
- Evidence: <why this disposition is correct>
- Correction: <changed file/symbol and resulting behavior; N/A unless ACCEPTED>
- Regression coverage: <test/check tied to the issue>

## Files Changed

- `<path>` — <issue ID and smallest correction; distinguish pre-existing changes>

## Self-Tests

- `<working directory; exact command>` — <PASS / FAIL / NOT_RUN / BLOCKED; result>

## Fix Diff Review

- Issue coverage: <all accepted IDs mapped or exact gap>
- Scope/unrelated changes: <result>
- Compatibility/security/secrets/diagnostics: <result>
- New regression risk: <concrete risk or none identified>

## Remaining Issues and Risks

- <open/rejected/context-dependent issue, risk, or none>

## Cycle History

1. <review decision → explicit authorization → fix attempt → self-test result>

## Handoff

- Next stage / owner: <code-review targeted re-review; human/upstream owner if blocked>
- Re-review scope: <original issues, fix diff, affected tests, and preserved behavior>
- Resume condition: <only when blocked/escalated>

Do not claim APPROVED. Only a new CODE REVIEW REPORT may approve the post-fix baseline.
