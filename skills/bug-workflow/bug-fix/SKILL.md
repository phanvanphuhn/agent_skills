---
name: bug-fix
description: "Implements an authorized correction for a confirmed root cause and prepares the resulting baseline for independent code review."
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

## Required outcome

Make the scoped correction and regression-test changes, then produce a
[BUG FIX REPORT](references/bug-fix-report-template.md) with status IMPLEMENTED or
BLOCKED. Map the confirmed cause to actual changes and available checks.

## Boundaries

Do not fix an unconfirmed cause, broaden scope to unrelated cleanup, overwrite local
changes, conceal failed checks, weaken tests, or preserve a disproven cause merely to
justify the patch.

## Handoff

IMPLEMENTED proceeds to code-review. Contradictory implementation evidence returns to
bug-root-cause. BLOCKED names the missing authority, dependency, evidence, or owner.
