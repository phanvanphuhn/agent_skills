---
name: fix-code-review
description: "Applies explicitly authorized corrections for accepted CODE REVIEW REPORT findings and returns the changed baseline for re-review."
---

# Fix code review

## Purpose

Correct only the accepted review findings covered by explicit user authorization and
prepare the result for independent re-review.

## Use when

Run after CHANGES_REQUIRED, or human-directed REVIEW_ESCALATION, when the user explicitly
requests fixes or originally requested `review and fix`. Never start automatically.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- Explicit user authorization, latest CODE REVIEW REPORT, exact reviewed baseline,
  current worktree, issue IDs, blocker IDs, and cycle history.
- Governing feature/bug artifacts and directly related code/tests.

## Required outcome

Apply scoped corrections and produce a
[FIX CODE REVIEW REPORT](references/fix-code-review-report-template.md) with status
READY_FOR_RE_REVIEW or BLOCKED. Give every reported issue a disposition: ACCEPTED,
REJECTED_FINDING, NEEDS_CONTEXT, or BLOCKED, with evidence and checks.

## Boundaries

Do not fix unreported technical debt, reinterpret requirements, alter an established
root cause without evidence, close review blockers yourself, approve the correction,
or bypass re-review. Preserve unrelated user changes.

## Handoff

READY_FOR_RE_REVIEW returns the exact post-fix baseline to code-review. BLOCKED names
the missing evidence, authority, access, decision, owner, and resume condition. Carry
`review_cycles` unchanged.
