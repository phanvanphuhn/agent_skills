---
name: bug-verification
description: "Independently verifies that an APPROVED reviewed bug fix removes the reproduced failure without regressions and routes failures to the necessary prior stage."
---

# Bug verification

## Responsibility

Act as an independent senior reviewer and test engineer. Determine whether the actual
fix resolves the confirmed bug, covers its cause, and preserves required behavior.

## Trigger

Run after code-review returns APPROVED for the current IMPLEMENTED BUG FIX REPORT and
code baseline, including repair revisions. Verification is required even when developer
and review checks passed.

## When not to run

Do not verify a code baseline without a matching APPROVED CODE REVIEW REPORT, implement
production fixes, infer success from reports alone, or mark PASS when a required check
is NOT_RUN/BLOCKED. Do not rerun unrelated stages by default.

## Inputs

- Current PROJECT CONTEXT revision covering the target repository/workspace.
- BUG CONTRACT, REPRODUCTION REPORT, ROOT CAUSE REPORT, BUG FIX REPORT, and matching
  APPROVED CODE REVIEW REPORT.
- Actual diff/worktree, tests, repository instructions, and available environments.
- Prior BUG VERIFICATION REPORT/FIX REQUEST and complete cycle history, when present.

## Verification strategy — Walk It Down

Inspect independently and escalate only as evidence requires:

- V0 — validate artifact revisions, statuses, scope, and required evidence.
- V1 — inspect actual changed files/diff and root-cause-to-change mapping.
- V2 — run the original reproduction/regression test; where technically possible,
  establish that it failed before the fix and passes after it.
- V3 — run directly related module/component tests and boundaries.
- V4 — run repository-required lint, type, build, security, or static checks.
- V5 — run broader regression/integration checks justified by the risk surface.
- V6 — run full-suite or real-environment validation only when required by the bug,
  contract, repository, release risk, or unresolved lower-level evidence.

Use [changed-files.sh](../../feature-workflow/verification/scripts/changed-files.sh),
[related-tests.sh](../../feature-workflow/verification/scripts/related-tests.sh), and
[verify.sh](../../feature-workflow/verification/scripts/verify.sh) for deterministic discovery/execution
when applicable. Helpers do not decide test completeness.

## Procedure

1. Confirm compatible artifact revisions, APPROVED review baseline, and counters.
   Inspect the actual diff rather than relying on implementation or review summaries.
2. Check that the edit addresses the confirmed cause and contains no unrelated change,
   secret, temporary diagnostic, weakened assertion, or hidden failure.
3. Verify `reported failure → reproduction evidence → root cause → change → regression
   test → result`. Re-run the original path/test and meaningful boundaries.
4. Check required preserved behavior, regression surface, architecture, interfaces,
   error handling, and repository-mandated checks through the necessary V-level.
5. Record every command, working directory, exit status, result, and limitation.
   Required unexecuted evidence is NOT_RUN or BLOCKED, never PASS.
6. Return PASS only when the failure is resolved and required evidence passes. On
   failure, classify it as IMPLEMENTATION_ISSUE, ROOT_CAUSE_INCORRECT, or
   REQUIREMENT_UNCLEAR and produce a focused BUG FIX REQUEST.
7. Route IMPLEMENTATION_ISSUE to bug-fix and require code-review again after its
   production repair; route ROOT_CAUSE_INCORRECT to bug-root-cause and REQUIREMENT_UNCLEAR
   to human/bug-analysis. BLOCKED names owner/resume condition.
8. Update `failed_cycles_for_root_cause` and `total_fix_cycles`. The initial FAIL is
   cycle one. Stop at the third FAIL for the same root-cause revision and request human
   intervention with cumulative evidence. A materially different evidence-backed root
   cause resets only its per-root-cause count; never reset the total history.
9. Produce the [BUG VERIFICATION REPORT](references/bug-verification-report-template.md)
   and, on FAIL, the [BUG FIX REQUEST](references/bug-fix-request-template.md).

## Outputs

A BUG VERIFICATION REPORT with final status PASS, FAIL, or BLOCKED. FAIL includes one
failure classification and a BUG FIX REQUEST routed only to the necessary stage.

## Completion criteria

The actual diff and original failure are independently assessed; cause coverage,
regression behavior, required checks, limitations, and cycle history are explicit.
Only PASS permits the bug workflow to reach DONE.

## Failure and blocked behavior

Known fix defects produce FAIL even if another check is blocked; record both. Otherwise
missing required evidence produces BLOCKED. Do not weaken the expected behavior, revise
the cause without evidence, or silently reset counters to obtain completion.

## Human intervention

Stop at the third FAIL for one root-cause revision, or earlier for a product ambiguity,
missing authority, unsafe environment, or unavailable external dependency. Provide a
concise ticket-ready summary of attempts, decisive evidence, and the exact action needed.
