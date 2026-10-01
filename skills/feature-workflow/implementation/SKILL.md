---
name: implementation
description: "Implements an authorized READY TASK CONTRACT or a focused verification FIX REQUEST and prepares the resulting baseline for code review."
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

## Required outcome

Make the scoped code/test/configuration changes and produce an
[IMPLEMENTATION REPORT](references/implementation-report-template.md) with status
READY_FOR_REVIEW or BLOCKED. Map every acceptance criterion or repair ID to actual
files and available checks.

## Boundaries

Do not implement against DRAFT, NEEDS_CLARIFICATION, BLOCKED, missing, or stale
requirements. Do not broaden the product scope, overwrite unrelated changes, conceal
failed checks, or weaken requirements/tests. A discovered product ambiguity returns to
requirement-validator.

## Handoff

READY_FOR_REVIEW goes to code-review with the exact baseline and artifacts. BLOCKED
identifies the missing authority, dependency, evidence, or decision and its owner.
Implementation never declares the task complete.
