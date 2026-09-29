# CODE REVIEW REPORT

- Task / bug / review target: <stable identity and repository>
- Mode: <REQUIRED GATE / MANUAL REVIEW>
- Input artifacts: <contract/root-cause/implementation artifacts or manual scope>
- Review baseline: <diff/base/head, commit, files, or supplied code>
- Decision: <APPROVED / CHANGES_REQUIRED / BLOCKED / REVIEW_ESCALATION>
- Review cycle: <0 initial approval; 1-3 after each CHANGES_REQUIRED review>
- Independence: <reviewer separation and any disclosed limitation>
- Context used: <maximum R0-R5 and question justifying expansion beyond R1>

## Review Scope

- Files/diff reviewed: <exact scope and directly related evidence>
- Excluded/pre-existing changes: <identified unrelated work or none>
- Requirements/root-cause baseline: <artifact revision or NEEDS_CONTEXT>

## SLP Summary

- Supervisor: <intent, completeness, compatibility, delivery/regression result>
- Lead: <architecture, conventions, safety, and maintainability result>
- Peer: <diff-level logic, edge, async, cleanup, and test result>

## Issues

### <CR-ID> — <short title>

- Severity: <HIGH / MEDIUM / LOW>
- Found by: <SUPERVISOR / LEAD / PEER; one or more>
- File / location: <path:symbol-or-line>
- Problem: <specific defect>
- Evidence: <code/repository evidence establishing it>
- Impact: <behavior, security, regression, maintenance, or delivery consequence>
- Recommended action: <smallest safe correction or follow-up>
- Status: <OPEN / RESOLVED / NEEDS_CONFIRMATION / NEEDS_CONTEXT>

<When there are zero issues, state `No issues.` instead of creating empty severity sections.>

## Read-Only Checks

- `<working directory; exact command>` — <PASS / FAIL / NOT_RUN / BLOCKED; result>

## Remaining Risks

- <concrete risk, missing evidence, or none>

## Review History

1. <baseline, decision, issue IDs, and relationship to any prior FIX CODE REVIEW REPORT>

## Final Decision and Handoff

- Decision: <APPROVED / CHANGES_REQUIRED / BLOCKED / REVIEW_ESCALATION>
- Approved baseline: <exact commit/diff/worktree state; N/A unless APPROVED>
- Next stage / owner: <verification, bug-verification, user/fix-code-review, validator, root-cause, or human>
- Resume condition: <explicit fix instruction, missing evidence, or escalation decision when applicable>

This report is read-only. Do not claim fixes were applied or tests passed unless the
recorded command actually ran. Never expose private reasoning, secrets, or unrelated data.
