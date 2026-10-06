# CODE REVIEW REPORT

- Task / bug / review target: <stable identity and repository>
- Project context: <PROJECT CONTEXT revision for the reviewed baseline>
- Mode: <REQUIRED GATE / MANUAL REVIEW>
- Input artifacts: <contract/root-cause/implementation artifacts or manual scope>
- Review baseline: <diff/base/head, commit, files, or supplied code>
- Decision: <APPROVED / CHANGES_REQUIRED / BLOCKED / REVIEW_ESCALATION>
- Review cycle: <review_cycles: prior + 1 for confirmed blocking findings, otherwise unchanged; initially 0>
- Reviewer context: <fresh run/session distinct from implementation or same context; evidence of separation>
- Independence: <established / unavailable / unverified, with limitation if needed>
- Coverage: <complete / incomplete; required gaps listed under Review Blockers>

## Review Scope

- Files/diff reviewed: <exact scope and directly related evidence>
- Excluded/pre-existing changes: <identified unrelated work or none>
- Requirements/root-cause baseline: <artifact revision or NEEDS_CONTEXT>

## Issues

### <CR-ID> — <short title>

- Severity: <HIGH / MEDIUM / LOW>
- File / location: <path:symbol-or-line>
- Problem: <specific defect>
- Evidence: <code/repository evidence establishing it>
- Impact: <behavior, security, regression, maintenance, or delivery consequence>
- Recommended action: <smallest safe correction or follow-up>
- Status: <OPEN / RESOLVED / NEEDS_CONFIRMATION / NEEDS_CONTEXT>

<When there are zero issues, state `No issues.` instead of creating empty severity sections.>

## Read-Only Checks

Use the shared [check evidence record](../../../references/check-evidence.md).
List new CHK-* records or REUSED references. Independent inspection still uses actual code.

## Remaining Risks

- <concrete risk, missing evidence, or none>

## Review Blockers

- <BLK-ID>: <OPEN / EVIDENCE_SUPPLIED / RESOLVED>; <scope; missing evidence/access;
  owner; action; resume condition; originating report and closure/reopening evidence>

Retain blockers alongside confirmed issues, including on CHANGES_REQUIRED/REVIEW_ESCALATION.
Reconcile inherited IDs; cite unchanged details by accessible report reference. Only
reviewer-confirmed closure permits RESOLVED. Resolving an issue does not resolve a blocker.
State `None` only when there are no inherited or new blockers; retain closed history by reference.
For a REQUIRED GATE, unavailable or unverified reviewer separation is an OPEN blocker;
without a confirmed blocking finding it yields BLOCKED, not APPROVED. A MANUAL REVIEW
may disclose the limitation without making it a blocker.

## Review History

1. <baseline, decision, issue IDs, and relationship to any prior FIX CODE REVIEW REPORT>

Confirmed blocking findings take precedence over missing evidence: count the issued
report once even with incomplete coverage. Counts 1–2 yield CHANGES_REQUIRED; 3+ yields
REVIEW_ESCALATION. Without confirmed blocking findings, required gaps yield BLOCKED;
only sufficient evidence permits APPROVED. Both preserve the count and prior history.

## Final Decision and Handoff

- Decision: <APPROVED / CHANGES_REQUIRED / BLOCKED / REVIEW_ESCALATION>
- Approved baseline: <exact commit/diff/worktree state; N/A unless APPROVED>
- Next stage / owner: <verification, bug-verification, user/fix-code-review, validator, root-cause, or human>
- Resume condition: <explicit fix instruction, missing evidence, or escalation decision when applicable>

## Independent Review Handoff

<For a REQUIRED GATE without established reviewer separation, give a copy-ready
request to a fresh reviewer/session. Identify the exact baseline, governing contract
or root-cause revision, implementation/fix report, actual code/diff and tests to inspect,
prior review and OPEN blocker IDs, and available CHK-* evidence. Reference accessible
artifacts; do not paste private payloads or the implementation conversation. For
BLOCKED due to separation, ask for a read-only CODE REVIEW REPORT on the current
baseline. For CHANGES_REQUIRED or REVIEW_ESCALATION, state that authorized correction
or human direction comes first, then request fresh review of the resulting baseline
with current finding and blocker IDs carried forward. Require the new reviewer to
record how separation was established. If an artifact is inaccessible, name its
owner and required action. Otherwise N/A.>

This report is read-only. Do not claim fixes were applied or tests passed unless the
recorded command actually ran. Never expose private reasoning, secrets, or unrelated data.
