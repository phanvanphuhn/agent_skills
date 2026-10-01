---
name: bug-verification
description: "Verifies an APPROVED bug-fix baseline against the reproduced failure and required regressions, returning PASS, FAIL, or BLOCKED."
---

# Bug verification

## Purpose

Prove whether the reviewed fix removes the confirmed failure and preserves required
behavior.

## Use when

Run only after code-review APPROVES the exact current bug-fix baseline.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- Compatible BUG CONTRACT, REPRODUCTION REPORT, ROOT CAUSE REPORT, BUG FIX REPORT, and
  APPROVED CODE REVIEW REPORT.
- Actual baseline, tests, available environments, prior verification/fix requests, and
  complete cycle counters.

## Required outcome

Produce a [BUG VERIFICATION REPORT](references/bug-verification-report-template.md) with
PASS, FAIL, or BLOCKED. Verify the original failure, cause coverage, required preserved
behavior, regressions, and checks against the approved baseline.

FAIL must be classified as IMPLEMENTATION_ISSUE, ROOT_CAUSE_INCORRECT, or
REQUIREMENT_UNCLEAR and include a [BUG FIX REQUEST](references/bug-fix-request-template.md).

## Boundaries

Do not change production code, weaken expected behavior, invent execution evidence, or
certify a baseline changed after approval. Required NOT_RUN or BLOCKED evidence prevents
PASS unless a known defect independently requires FAIL.

## Handoff

PASS permits DONE. Failure routes only to the owning stage and must return through
code-review before re-verification. Preserve `failed_cycles_for_root_cause` and
`total_fix_cycles`; the third FAIL for one root-cause revision stops for human action.
