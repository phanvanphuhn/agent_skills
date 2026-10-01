---
name: code-review
description: "Performs a read-only review of actual code or a changed baseline and returns evidence-backed findings and an approval decision."
---

# Code review

## Purpose

Independently assess the scoped code for correctness, requirement or root-cause
coverage, architecture, security, regressions, maintainability, and test adequacy.

## Use when

- REQUIRED GATE: after implementation, bug fixes, review corrections, or later
  code/test/fixture/snapshot/behavior-affecting configuration changes.
- MANUAL REVIEW: when the user explicitly requests review of code, files, a diff,
  commit, branch, PR, or supplied snippet.

## Inputs

- Current PROJECT CONTEXT, repository instructions, actual scope/diff, exact baseline,
  related tests, review history, and available evidence.
- For required gates: the governing feature or bug artifacts and implementation report.
- For re-review: prior CODE REVIEW REPORT and FIX CODE REVIEW REPORT or changed-baseline
  evidence.

## Required outcome

Produce a [CODE REVIEW REPORT](references/code-review-report-template.md) with one
decision: APPROVED, CHANGES_REQUIRED, BLOCKED, or REVIEW_ESCALATION.

Each finding must include a stable ID, HIGH/MEDIUM/LOW severity, location, problem,
evidence, impact, recommended action, and status. HIGH and MEDIUM findings block by
default. Unknown product behavior is NEEDS_CONTEXT, not a defect.

## Boundaries

Review is read-only. Do not fix code, approve from reports without inspecting the
actual scope, invent missing behavior, hide confirmed defects behind missing evidence,
or claim unexecuted checks passed.

## Handoff

APPROVED permits verification of the exact baseline. CHANGES_REQUIRED stops for explicit
fix authorization. BLOCKED identifies missing evidence/access and its owner.
REVIEW_ESCALATION stops after the third blocking review for human direction. Preserve
stable blocker IDs and `review_cycles` history.
