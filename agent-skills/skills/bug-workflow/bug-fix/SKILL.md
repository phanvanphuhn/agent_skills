---
name: bug-fix
description: "Applies the smallest authorized correction for a CONFIRMED root cause, or a verification BUG FIX REQUEST, with regression tests, then hands the baseline to code review. Use when asked to fix or patch a bug whose root cause has been confirmed."
---

# Bug fix

## Purpose

Correct the confirmed cause while preserving unrelated behavior and user work.

## Use when

Run after a CONFIRMED ROOT CAUSE REPORT or with a focused BUG FIX REQUEST from
bug-verification. The user must have authorized the correction.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- Compatible BUG CONTRACT, REPRODUCTION REPORT, and ROOT CAUSE REPORT.
- Authorized scope, current worktree, relevant code/tests, and cycle history.
- In repair mode: current BUG FIX REQUEST and prior fix report.

## Walk It Down

- Start: Confirm user authorization and an accessible CONFIRMED ROOT CAUSE REPORT, or a focused BUG FIX REQUEST in repair mode. If either is missing, ask once and do not edit.
- Expand: Inspect direct dependencies, consumers, or analogous tests only for a named correction or regression-risk question.
- Stop: Stop at the smallest cause-correcting change and evidence needed for review, return contradictory evidence upstream, or block when authority or the governing artifact is unavailable.

## Required outcome

If user authorization or the CONFIRMED ROOT CAUSE REPORT / BUG FIX REQUEST is missing
or inaccessible, ask once, leave the repository unchanged, and return BLOCKED with the
owner and resume condition.

Otherwise make the scoped correction and regression-test changes, then produce a
[BUG FIX REPORT](references/bug-fix-report-template.md) with status IMPLEMENTED or
BLOCKED. Map the confirmed cause to actual changes and available checks.

## Boundaries

Do not edit without confirmed user authorization. Do not fix an unconfirmed cause,
broaden scope to unrelated cleanup, overwrite local changes, conceal failed checks,
weaken tests, or preserve a disproven cause merely to justify the patch.

## Handoff

IMPLEMENTED proceeds to code-review. Contradictory implementation evidence returns to
bug-root-cause. BLOCKED names the missing authority, dependency, evidence, or owner.
