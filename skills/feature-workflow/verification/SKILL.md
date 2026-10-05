---
name: verification
description: "Verifies every acceptance criterion on an APPROVED feature baseline and returns PASS, FAIL with a FIX REQUEST, or BLOCKED."
---

# Verification

## Purpose

Provide executed evidence that the reviewed implementation satisfies the READY TASK
CONTRACT and required regression obligations.

## Use when

Run only after code-review APPROVES the exact current baseline. Do not certify an
unvalidated contract, changed baseline, or unavailable implementation.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- READY TASK CONTRACT, VALIDATION REPORT, IMPLEMENTATION REPORT, and matching APPROVED
  CODE REVIEW REPORT.
- Actual code/diff, tests, available environments, prior verification reports, and
  `failed_cycles`.

## Walk It Down

- Start: Map each acceptance criterion to the approved implementation, focused test, and existing evidence.
- Expand: Run affected suites, static checks, regression checks, or real integration only when required by the contract or unresolved risk.
- Stop: Stop when required evidence supports PASS, establishes FAIL, or identifies the exact BLOCKED prerequisite.

## Required outcome

Produce a [VERIFICATION REPORT](references/verification-report-template.md) mapping
every criterion to implementation, test/evidence, boundary, and PASS, FAIL, NOT_RUN,
or BLOCKED. The final status is PASS, FAIL, or BLOCKED.

On FAIL, increment `failed_cycles` once and produce a focused
[FIX REQUEST](references/fix-request-template.md). PASS requires all required evidence
and an unchanged APPROVED baseline.

## Boundaries

Do not change production code, weaken criteria, invent executions, or treat mocked
evidence as live integration. Any test, fixture, snapshot, code, or behavior-affecting
configuration change returns the new baseline to code-review before certification.

## Handoff

PASS permits DONE. FAIL below cycle three returns to implementation and then code-review.
The third FAIL, a product ambiguity, or missing authority stops for human action.
BLOCKED identifies the missing prerequisite, owner, and resume condition without
incrementing the counter unless a known defect independently establishes FAIL.
