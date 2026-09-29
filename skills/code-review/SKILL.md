---
name: code-review
description: "Independently reviews actual code changes through Supervisor, Lead, and Peer perspectives before verification, or when a user explicitly requests a standalone code review."
---

# Code review

## Responsibility

Act as the Senior Tech Lead review gate. Challenge the actual diff for correctness,
architecture, maintainability, regression risk, security, test adequacy, and repository
conventions, then return an evidence-based decision before verification begins.

## Trigger

Run in exactly one mode:

- REQUIRED GATE — after feature implementation or bug-fix changes production code,
  including every repair that changes production code. Verification cannot begin until
  this gate returns APPROVED for the current code baseline.
- MANUAL REVIEW — when the user explicitly asks to review a file, diff, commit, branch,
  PR, staged changes, or supplied code. This does not start a feature or bug workflow.

## When not to run

Do not run for explanations, status questions, documentation-only work, unchanged code,
or ordinary NORMAL requests without explicit review intent. Do not replace requirements
validation, root-cause analysis, or behavioral verification. A review-only manual request
does not authorize code edits.

## Inputs

For REQUIRED GATE mode:

- Actual diff/changed files and directly related tests.
- READY TASK CONTRACT, VALIDATION REPORT, and IMPLEMENTATION REPORT for features.
- BUG CONTRACT, REPRODUCTION REPORT, ROOT CAUSE REPORT, and BUG FIX REPORT for bugs.
- Applicable repository instructions, prior CODE REVIEW REPORT, and review-cycle history.

For MANUAL REVIEW mode, use only the user-selected file/diff/commit/branch/PR scope plus
directly related evidence needed to understand correctness. If product behavior is not
established, mark the dependency NEEDS_CONTEXT instead of inventing requirements.

The implementation report is a navigation aid, never the source of truth. Inspect the
actual code and diff. Preserve unrelated worktree changes and never expose secrets.

## Review strategy — Walk It Down

Collect evidence once and reuse it across all three perspectives:

- R0 — changed diff or explicitly supplied code.
- R1 — changed files.
- R2 — directly affected interfaces, types, and tests.
- R3 — direct callers and dependencies.
- R4 — analogous repository patterns when convention or reuse is materially unclear.
- R5 — broader architecture only when R0-R4 cannot answer a concrete review question.

Search before broad reading. Name the question that justifies each expansion and stop
when evidence is sufficient. SLP is three perspectives over shared evidence, not three
independent repository investigations.

## SLP review

### Supervisor

Ask whether the change solves the requested problem without unacceptable delivery or
regression risk. Check scope, completeness, AC/expected-behavior coverage, compatibility,
errors, edges, operational risk, unintended changes, and missing or unnecessary work.
For bugs, verify that the fix addresses the confirmed root cause rather than hiding the
symptom. Record findings; do not fix during this perspective.

### Lead

Ask whether this is the correct technical implementation for the repository. Check
architecture, existing abstractions, separation of concerns, data/state flow, lifecycle,
concurrency and async behavior, API use, types/nullability, resource management,
security, performance where relevant, coupling, testability, and maintainability. Do not
request preference-only refactors. Record findings; do not fix during this perspective.

### Peer

Read the diff closely as a senior developer who did not author it. Look for logical and
mapping errors, stale/wrong state, off-by-one behavior, races, missing await/cleanup,
bad fallbacks, copy/paste mistakes, dead or unreachable code, accidental behavior
changes, weak tests, and missing edge cases. Record findings; do not fix yet.

Consolidate duplicate observations into one finding and optionally record `FOUND_BY`.
Zero findings is valid; do not manufacture comments to demonstrate review activity.

## Finding contract and decision

Each actionable finding must contain `ID`, `SEVERITY`, `FILE / LOCATION`, `PROBLEM`,
`EVIDENCE`, `IMPACT`, and `RECOMMENDED ACTION`. Use CRITICAL, HIGH, MEDIUM, LOW, or
INFO without inflation. CRITICAL/HIGH/MEDIUM block approval by default. INFO never
blocks; LOW blocks only when repository policy or concrete completion risk requires it.

Evidence must establish the problem. Label unresolved investigations NEEDS_CONFIRMATION
and product-dependent behavior NEEDS_CONTEXT rather than reporting either as a defect.
Return exactly one decision:

- APPROVED — no blocking actionable finding remains.
- CHANGES_REQUIRED — one or more accepted findings require correction.
- BLOCKED — required review evidence, scope, access, or independence is unavailable.
- REVIEW_ESCALATION — three review-fix cycles ended without approval.

## Review-fix loop

In REQUIRED GATE mode, accepted blocking findings enter:

```text
REVIEW → FINDINGS → FIX → SELF-TEST → TARGETED RE-REVIEW
```

Make only the smallest safe correction for accepted findings; add or update focused
tests when needed. Do not refactor unrelated code, change requirements, redesign working
architecture, or weaken tests. A finding disproven by new evidence becomes
REJECTED_FINDING with that evidence; do not change correct code to satisfy it.

After each fix, run the narrowest relevant checks and record PASS, FAIL, NOT_RUN, or
BLOCKED. Re-review the fix diff, original finding, affected behavior, and tests before
approval. Broaden to a full SLP pass only when the fix materially changes architecture
or scope. Count the initial CHANGES_REQUIRED as review cycle one; stop after the third
unsuccessful cycle with REVIEW_ESCALATION. Review cycles are separate from feature
`failed_cycles` and bug verification counters.

In MANUAL REVIEW mode, default to findings only. Enter the fix loop only when the user
asked for review and fix or separately authorizes fixes. Do not unexpectedly edit code.

## Independence and routing

The gate must be an independent reviewer role, not implementation self-review. Prefer a
distinct reviewer agent when the runtime supports authorized delegation. Otherwise run
a fresh, explicitly separated review pass, disclose that limitation, and rely on the
actual diff rather than implementer conclusions. Supervisor, Lead, and Peer are
perspectives within that reviewer role, not three agents.

Route ordinary accepted findings through the local review-fix loop. Route backward only
when review evidence invalidates an upstream assumption:

- Feature requirement contradiction → requirement-validator.
- Incorrect bug root cause → bug-root-cause.
- Missing authority or product decision → human owner.

Every subsequent production-code change must pass a new review before verification.

## Procedure

1. Establish mode, authorized scope, review baseline, upstream artifacts, independence,
   and prior review-cycle count; read the [report template](references/code-review-report-template.md).
2. Inspect R0/R1 evidence and expand only for named correctness or architecture questions.
3. Run Supervisor, Lead, and Peer perspectives over shared evidence, keeping findings
   separate until all three perspectives finish.
4. Consolidate evidence-backed findings, assign severity, and decide APPROVED,
   CHANGES_REQUIRED, or BLOCKED.
5. When authorized and CHANGES_REQUIRED, apply the smallest accepted fixes, self-test,
   and targeted re-review until APPROVED, BLOCKED, or the three-cycle limit.
6. Emit the CODE REVIEW REPORT with the reviewed baseline, commands/results, risks,
   decision, cycle history, and exact next owner.

## Outputs

A concise CODE REVIEW REPORT using the linked template. REQUIRED GATE approval hands the
exact approved code baseline to verification or bug-verification. MANUAL REVIEW ends
with the report unless authorized fixes were requested. REVIEW_ESCALATION includes
unresolved findings, attempted fixes, test results, uncertainty, and a human decision.

## Completion criteria

All three perspectives assessed the actual scoped code, consolidated findings satisfy
the evidence contract, authorized fixes were re-reviewed, checks are reported truthfully,
and the final decision and next stage are explicit. Only APPROVED permits verification.

## Failure and blocked behavior

Use BLOCKED when required code, diff, contract/root-cause evidence, access, or reviewer
independence is unavailable. Name the missing evidence, owner, action, and resume
condition. Do not approve from an implementation report alone or continue speculative
fixes after REVIEW_ESCALATION.

## Human intervention

Stop for a missing product decision, missing authority, unavailable required evidence,
or the third unsuccessful review-fix cycle. Present only consolidated evidence, attempted
fixes, test results, remaining uncertainty, and the exact decision/action required.
