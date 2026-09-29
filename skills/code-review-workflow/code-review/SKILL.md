---
name: code-review
description: "Performs a read-only Supervisor, Lead, and Peer review of actual code changes, producing prioritized findings before verification or on explicit manual review requests."
---

# Code review

## Responsibility

Act as the independent Senior Tech Lead review gate. Inspect the actual diff for
correctness, architecture, maintainability, regression risk, security, test adequacy,
and repository conventions, then emit prioritized findings. Never modify code.

## Trigger

Run in exactly one mode:

- REQUIRED GATE — after feature implementation or bug-fix changes production code,
  including every production repair and every fix-code-review pass.
- MANUAL REVIEW — when the user explicitly asks to review a file, diff, staged changes,
  commit, branch, PR, or supplied code. This does not start feature or bug analysis.

Run again after a FIX CODE REVIEW REPORT returns READY_FOR_RE_REVIEW. Verification
cannot begin until code-review returns APPROVED for the exact current baseline.

## When not to run

Do not run for explanations, status questions, documentation-only work, unchanged code,
or ordinary NORMAL requests without explicit review intent. Do not edit code, apply
review fixes, replace requirements validation/root-cause analysis, or treat earlier
implementation/review reports as proof.

## Inputs

- Current PROJECT CONTEXT revision covering the reviewed repository/workspace.

For REQUIRED GATE mode:

- Actual diff/changed files and directly related tests.
- READY TASK CONTRACT, VALIDATION REPORT, and IMPLEMENTATION REPORT for features.
- BUG CONTRACT, REPRODUCTION REPORT, ROOT CAUSE REPORT, and BUG FIX REPORT for bugs.
- Prior CODE REVIEW REPORT and FIX CODE REVIEW REPORT when re-reviewing.
- Applicable repository instructions and current review-cycle history.

For MANUAL REVIEW mode, use the user-selected file/diff/commit/branch/PR scope plus only
directly related evidence needed for correctness. Mark unknown product-dependent behavior
NEEDS_CONTEXT instead of inventing requirements. Preserve unrelated worktree changes and
never expose secrets.

## Review strategy — Walk It Down

Collect evidence once and reuse it across all three perspectives:

- R0 — changed diff or supplied code.
- R1 — changed files.
- R2 — directly affected interfaces, types, and tests.
- R3 — direct callers and dependencies.
- R4 — analogous repository patterns when reuse or convention is materially unclear.
- R5 — broader architecture only when R0-R4 cannot answer a concrete review question.

Search before broad reading. Name the question justifying each expansion and stop when
evidence is sufficient. SLP is three perspectives over shared evidence, not three full
repository investigations.

## SLP review

### Supervisor

Ask whether the change solves the requested problem without unacceptable delivery or
regression risk. Check scope, completeness, AC/expected-behavior coverage, compatibility,
errors, edges, operations, and unintended or unnecessary changes. For bugs, ensure the
fix follows the confirmed root cause instead of hiding the symptom.

### Lead

Ask whether this is the correct technical implementation for the repository. Check
architecture, existing abstractions, separation of concerns, state/data flow, lifecycle,
concurrency/async behavior, API use, types/nullability, resource management, security,
performance where relevant, coupling, testability, and maintainability. Do not report
preference-only refactors.

### Peer

Read the diff as a senior developer who did not author it. Look for logical or mapping
errors, stale/wrong state, off-by-one behavior, races, missing await/cleanup, bad
fallbacks, copy/paste mistakes, dead code, accidental changes, weak tests, and missing
edge cases.

Keep perspective notes separate until all three finish, then consolidate duplicate
observations into one issue. Zero issues is valid; never manufacture findings.

## Issue contract and decision

Every issue must contain `ID`, `SEVERITY`, `FOUND_BY`, `FILE / LOCATION`, `PROBLEM`,
`EVIDENCE`, `IMPACT`, and `RECOMMENDED ACTION`. Use exactly:

- HIGH — broken requirement/root-cause fix, security or data risk, serious regression,
  or major architectural defect; blocks approval.
- MEDIUM — concrete correctness, reliability, test, or maintainability defect that
  should be corrected before completion; blocks approval.
- LOW — limited-risk concrete improvement; non-blocking unless repository policy or
  direct completion risk says otherwise.

Evidence must establish the issue. Label unresolved investigations NEEDS_CONFIRMATION
and product-dependent behavior NEEDS_CONTEXT rather than presenting them as defects.

Return exactly one decision:

- APPROVED — no blocking HIGH/MEDIUM issue remains.
- CHANGES_REQUIRED — one or more blocking issues remain.
- BLOCKED — required scope, evidence, access, or reviewer independence is unavailable.
- REVIEW_ESCALATION — the third post-fix review still has blocking issues.

Code-review is read-only. CHANGES_REQUIRED stops and hands the issue list to the user.
Never invoke fix-code-review automatically. A separate explicit user instruction is
required, except that an original combined `review and fix` request already supplies
that authorization after the initial report is produced.

## Independence and routing

The gate is an independent reviewer role, not implementation self-review. Prefer a
distinct reviewer agent when available and authorized. Otherwise run a fresh, explicitly
separated pass, disclose that limitation, and rely on the actual diff rather than
implementer conclusions. Supervisor, Lead, and Peer are perspectives, not three agents.

Route backward only when review evidence invalidates an upstream assumption:

- Feature requirement contradiction → requirement-validator.
- Incorrect bug root cause → bug-root-cause.
- Missing authority or product decision → human owner.

Ordinary code issues remain in the CODE REVIEW REPORT for optional explicit handling by
fix-code-review. Any resulting production change must return to code-review.

## Procedure

1. Establish mode, scope, exact baseline, upstream artifacts, reviewer independence,
   and review-cycle count; read the [report template](references/code-review-report-template.md).
2. Inspect R0/R1 evidence and expand only for named correctness/architecture questions.
3. Run Supervisor, Lead, and Peer perspectives over the shared evidence.
4. Consolidate issues, assign HIGH/MEDIUM/LOW, and determine the decision without
   modifying any file.
5. On re-review, compare each prior issue with the FIX CODE REVIEW REPORT and actual
   fix diff; also check for regressions introduced by the fix.
6. Emit the CODE REVIEW REPORT with issues, read-only checks, risks, decision, reviewed
   baseline, cycle history, and exact next owner.

## Outputs

A concise CODE REVIEW REPORT using the linked template. APPROVED hands the exact baseline
to verification or bug-verification. CHANGES_REQUIRED hands a prioritized issue list to
the user and stops. BLOCKED/REVIEW_ESCALATION identifies the human action required.

## Completion criteria

All SLP perspectives assessed the actual scoped code, issues satisfy the evidence
contract, no code was modified, checks are reported truthfully, and the decision and
next owner are explicit. Only APPROVED permits verification.

## Failure and blocked behavior

Use BLOCKED when required code, diff, contract/root-cause evidence, access, or reviewer
independence is unavailable. Name the missing evidence, owner, action, and resume
condition. Never approve from reports alone or hide a blocking issue because fixing it
was not authorized.

## Human intervention

Stop for a missing product decision, missing authority, unavailable required evidence,
CHANGES_REQUIRED without explicit fix authorization, or REVIEW_ESCALATION. Present the
prioritized issues, review-cycle history, remaining uncertainty, and exact action needed.
