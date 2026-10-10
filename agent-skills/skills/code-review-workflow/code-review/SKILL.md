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

## Walk It Down

- Start: Inspect the actual scoped code or diff against its governing requirements, cause, and tests.
- Expand: Inspect affected interfaces, callers, dependencies, or analogous patterns only for a named correctness or risk question.
- Stop: Stop when evidence supports one review decision while preserving any separate coverage blocker.

## Required outcome

Produce a [CODE REVIEW REPORT](references/code-review-report-template.md) with one
decision: APPROVED, CHANGES_REQUIRED, BLOCKED, or REVIEW_ESCALATION.

Each finding must include a stable ID, HIGH/MEDIUM/LOW severity, location, problem,
evidence, impact, recommended action, and status. HIGH and MEDIUM findings block by
default. Unknown product behavior is NEEDS_CONTEXT, not a defect.
For a REQUIRED GATE, APPROVED requires a fresh reviewer context separate from the
implementation conversation, with the actual baseline and governing artifacts supplied.
Record how separation was established. If it is unavailable or unverified, keep an
OPEN review blocker: confirmed blocking findings still return CHANGES_REQUIRED or
REVIEW_ESCALATION; otherwise return BLOCKED, never APPROVED. MANUAL REVIEW may use the
current context with the limitation disclosed.
When the implementation context cannot establish a fresh reviewer, include the
template's copy-ready independent-review handoff. Use an available authorized fresh
session or reviewer with a compact packet of the governing artifacts, actual baseline,
directly related tests, and available check evidence; otherwise give the handoff to
the user. A role label or copied implementation conversation is not reviewer separation.
For a REQUIRED GATE, use the [independent review packet guide](references/independent-review.md)
to assemble a reproducible packet and record how the fresh reviewer was started.
If confirmed findings require changes, request explicit fix authorization first; the
fresh reviewer then inspects the corrected baseline, not a known-defective one.

## Boundaries

Review is read-only. Do not fix code, approve from reports without inspecting the
actual scope, invent missing behavior, hide confirmed defects behind missing evidence,
claim unexecuted checks passed, or infer independence from a role label alone.

## Handoff

APPROVED permits verification of the exact baseline. CHANGES_REQUIRED stops for explicit
fix authorization. BLOCKED identifies missing evidence/access and its owner.
REVIEW_ESCALATION stops after the third blocking review for human direction. Preserve
stable blocker IDs and `review_cycles` history.
