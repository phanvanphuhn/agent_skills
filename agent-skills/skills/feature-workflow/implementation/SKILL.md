---
name: implementation
description: "Implements a feature from a READY TASK CONTRACT, or a verification FIX REQUEST, once the user authorizes code changes, then hands the baseline to code review. Use when asked to build, implement, or continue implementing an approved feature spec or contract."
---

# Implementation

## Purpose

Change the target repository so the authorized READY contract is implemented while
preserving unrelated behavior and user work.

## Use when

Run with an accessible READY TASK CONTRACT and matching validation report after the
user authorizes implementation. Repair mode additionally requires the latest FIX
REQUEST and verification history.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- READY TASK CONTRACT and VALIDATION REPORT.
- Authorized scope and current worktree.
- In repair mode: FIX REQUEST, prior reports, and `failed_cycles`.

## Walk It Down

- Start: Confirm user authorization and an accessible READY TASK CONTRACT, or a focused FIX REQUEST in repair mode. If either is missing, ask once and do not edit.
- Expand: Inspect direct dependencies or analogous code only for a named implementation or regression-risk question.
- Stop: Stop at the smallest contract-complete change and evidence needed for code review, or a precise blocker when authority or the governing artifact is unavailable.

## Required outcome

If user authorization or the READY TASK CONTRACT / FIX REQUEST is missing or
inaccessible, ask once, leave the repository unchanged, and return BLOCKED with the
owner and resume condition.

Otherwise make the scoped code/test/configuration changes and produce an
[IMPLEMENTATION REPORT](references/implementation-report-template.md) with status
READY_FOR_REVIEW or BLOCKED. Map every acceptance criterion or repair ID to actual
files and available checks.

## Boundaries

Do not edit without confirmed user authorization. Do not implement against DRAFT,
NEEDS_CLARIFICATION, BLOCKED, missing, or stale requirements. Do not broaden the
product scope, overwrite unrelated changes, conceal failed checks, or weaken
requirements/tests. A discovered product ambiguity returns to requirement-validator.

## Handoff

READY_FOR_REVIEW goes to code-review with the exact baseline and artifacts. BLOCKED
identifies the missing authority, dependency, evidence, or decision and its owner.
Implementation never declares the task complete.
