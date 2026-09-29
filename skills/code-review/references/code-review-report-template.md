# CODE REVIEW REPORT

- Task / bug / review target: <stable identity and repository>
- Mode: <REQUIRED GATE / MANUAL REVIEW>
- Input artifacts: <contract/root-cause/implementation artifacts or manual scope>
- Review baseline: <diff/base/head, commit, files, or supplied code>
- Decision: <APPROVED / CHANGES_REQUIRED / BLOCKED / REVIEW_ESCALATION>
- Review cycle: <0 before findings; 1-3 after each CHANGES_REQUIRED decision>
- Independence: <reviewer separation and any disclosed limitation>
- Context used: <maximum R0-R5 and question justifying expansion beyond R1>

## Review Scope

- Files/diff reviewed: <exact scope and directly related evidence>
- Excluded/pre-existing changes: <identified unrelated work or none>
- Requirements/root-cause baseline: <artifact revision or NEEDS_CONTEXT for manual mode>

## SLP Summary

- Supervisor: <scope, intent, compatibility, delivery/regression result>
- Lead: <architecture, conventions, safety, maintainability result>
- Peer: <diff-level logic, edge, async, cleanup, and test result>

## Findings

### <CR-ID> — <short title>

- Severity: <CRITICAL / HIGH / MEDIUM / LOW / INFO>
- Found by: <SUPERVISOR / LEAD / PEER; one or more>
- File / location: <path:symbol-or-line>
- Problem: <specific defect or observation>
- Evidence: <code/repository evidence establishing it>
- Impact: <behavior, security, regression, maintenance, or delivery consequence>
- Recommended action: <smallest safe correction or follow-up>
- Status: <OPEN / FIXED / REJECTED_FINDING / NEEDS_CONFIRMATION / NEEDS_CONTEXT>

<Omit this subsection when there are zero findings; state `No findings.` instead.>

## Fixes Applied

- <finding ID → exact correction and changed files; none / not authorized>

## Findings Rejected

- <finding ID → evidence disproving it; omit when none>

## Tests and Checks

- `<working directory; exact command>` — <PASS / FAIL / NOT_RUN / BLOCKED; result>

## Remaining Risks

- <concrete risk, missing evidence, or none>

## Cycle History

1. <decision, findings, correction, self-test, re-review result>

## Final Decision and Handoff

- Decision: <APPROVED / CHANGES_REQUIRED / BLOCKED / REVIEW_ESCALATION>
- Approved baseline: <exact commit/diff/worktree state; N/A unless APPROVED>
- Next stage / owner: <verification, bug-verification, validator, root-cause, human, or done>
- Resume condition: <only when blocked/escalated>

Keep this report concise. Consolidate duplicate SLP findings and never expose private
reasoning, secrets, unrelated payloads, or an implementation-report narrative.
