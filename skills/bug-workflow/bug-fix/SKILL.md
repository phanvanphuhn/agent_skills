---
name: bug-fix
description: "Implements the smallest safe correction for a confirmed root cause and records the changed behavior and regression coverage. Use after bug-root-cause confirms an actionable cause or when bug-verification issues a focused fix request."
---

# Bug fix

## Responsibility

Act as a senior implementation engineer. Correct the confirmed root cause with the
smallest safe production change while preserving unrelated behavior.

## Trigger

Run after a ROOT CAUSE REPORT confirms an actionable cause with adequate confidence,
or in repair mode with that report plus a BUG FIX REQUEST from bug-verification.

## When not to run

Do not implement from an unconfirmed hypothesis, NEEDS_INFORMATION, BLOCKED, or a
LOW-confidence speculative cause. Do not broaden scope to nearby cleanup or redesign.

## Inputs

- BUG CONTRACT, REPRODUCTION REPORT, and ROOT CAUSE REPORT at compatible revisions.
- In repair mode, the current BUG FIX REQUEST and earlier fix-cycle history.
- Applicable repository instructions, relevant code/tests, and authorized scope.

## Context reuse and minimal fix

Start at L0 with the three trusted artifacts. Read only named affected code and tests
at L3; use L2 search to locate them. Move to L4/L5 only for a specific dependency or
regression-risk question not resolved upstream. Reuse established evidence instead of
repeating reproduction or root-cause analysis.

Change only what is required to remove the confirmed cause. Preserve interfaces,
behavior, style, and user changes outside the fix boundary. Add or strengthen the
root-cause regression test where technically practical. Do not weaken assertions,
silence failures, or hide errors to obtain a pass.

## Procedure

1. Confirm matching artifact revisions, authorization, clean scope, affected symbols,
   required preserved behavior, tests, and the current fix-cycle counters.
2. Inspect the working tree and direct files/tests. Protect unrelated user changes.
3. Translate the confirmed cause into a minimal edit and map each change to the cause,
   regression test, or required preservation constraint.
4. Implement production and test changes following repository patterns. Avoid new
   dependencies or public-interface changes unless the reports require them.
5. Run focused developer checks that are safe and available. Record exact commands,
   working directory, exit status, and limitations; proposed checks are NOT_RUN.
6. Review the diff for scope, secrets, temporary diagnostics, accidental generated
   files, and unsupported behavior changes.
7. If implementation evidence contradicts the root cause, stop and route back to
   bug-root-cause with that evidence. Do not force the planned patch.
8. Produce the complete [BUG FIX REPORT](references/bug-fix-report-template.md).

## Outputs

Code/test changes plus a BUG FIX REPORT with status IMPLEMENTED or BLOCKED. The report
maps the confirmed cause to files, behavior, regression coverage, checks, risks, and
the mandatory code-review gate as the next stage.

## Completion criteria

The change addresses the confirmed cause, stays within scope, preserves named behavior,
includes appropriate regression coverage, passes available focused developer checks,
and contains no known defect or secret. The report is sufficient for independent
code-review without reconstructing implementation reasoning; only an APPROVED review
baseline may proceed to bug-verification.

## Failure and blocked behavior

Return to bug-root-cause when new code evidence invalidates the cause. Mark BLOCKED for
missing authority, dependency, environment, or unsafe overlap, naming the owner and
resume condition. A failed developer check remains visible and must not be called PASS.

## Human intervention

Ask only for a product decision, authorization, unavailable external prerequisite, or
help after the configured failure-loop limit. Never ask a stakeholder to choose among
technical fixes when repository evidence can decide safely.
