---
name: fix-code-review
description: "Fixes accepted issues from a CODE REVIEW REPORT only when the user explicitly requests those corrections, then self-tests and hands the diff back for independent re-review."
---

# Fix code review

## Responsibility

Implement the smallest safe corrections for accepted CODE REVIEW REPORT issues after
explicit user authorization. Test the corrections and hand the changed baseline back to
code-review. Never approve the result.

## Trigger

Run only when all conditions hold:

- A CODE REVIEW REPORT identifies open issues with decision CHANGES_REQUIRED, or
  REVIEW_ESCALATION accompanied by new human direction authorizing another attempt.
- The user explicitly says to fix the review findings/issues, invokes fix-code-review,
  or originally requested `review and fix`.
- The reviewed baseline and current worktree can be matched safely.

This skill is never an automatic consequence of CHANGES_REQUIRED.

## When not to run

Do not run for APPROVED, BLOCKED, REVIEW_ESCALATION without new human direction, missing
review reports, vague requests to improve code, or review-only requests. Do not reinterpret
requirements, revise a confirmed root cause to fit a patch, fix unreviewed technical debt,
or approve your own corrections.

## Inputs

- Current PROJECT CONTEXT revision covering the reviewed repository/workspace.
- Explicit user fix authorization and the latest CODE REVIEW REPORT.
- Exact reviewed baseline, actual current diff/worktree, open issue IDs, and unresolved BLK-* IDs.
- Feature TASK CONTRACT/VALIDATION/IMPLEMENTATION artifacts or bug CONTRACT/ROOT CAUSE/
  BUG FIX artifacts when the review was a required gate.
- Directly related code/tests, repository instructions, prior FIX CODE REVIEW REPORTS,
  and review-cycle history.

## Context reuse and minimal fix

Start from the review issues and expand only as necessary:

- F0 — CODE REVIEW REPORT, authorization, and reviewed baseline.
- F1 — issue locations and changed files.
- F2 — directly affected interfaces/types/tests.
- F3 — callers/dependencies only when required to correct or safely test an issue.
- F4 — broader architecture only when the issue evidence proves the existing boundary
  is insufficient; otherwise return to code-review or the upstream owning stage.

Preserve unrelated user changes. For every issue, classify it as ACCEPTED,
REJECTED_FINDING, NEEDS_CONTEXT, or BLOCKED before editing. Reject a finding only when
new code/repository evidence disproves it; record that evidence instead of modifying
correct code.

## Execution routing

Apply [shared execution routing](../../references/execution-routing.md) through this profile;
open the linked reference only for an override, delegation, or runtime fallback.

- `START_CLASS`: ECONOMY
- `ESCALATE_WHEN`: Coupled or judgment-heavy fixes require STANDARD; high-risk evidence invalidating an upstream boundary requires DEEP.
- `DELEGATE_WHEN`: Fix scopes have separate write ownership; independent review remains a separate handoff.

## Procedure

1. Confirm explicit authorization, compatible report/baseline, open issue IDs, scope,
   upstream artifact revisions, and review_cycles from the review report; read the
   [fix report template](references/fix-code-review-report-template.md).
2. Inspect only the issue evidence and directly affected code/tests. Stop and route an
   invalid requirement to requirement-validator or incorrect bug cause to bug-root-cause.
3. Apply the smallest safe correction for each ACCEPTED issue. Do not refactor unrelated
   code, redesign working architecture, add speculative behavior, or weaken tests.
4. Add or strengthen focused regression tests where needed. Run the narrowest relevant
   checks, broadening only for demonstrated shared risk. Record PASS, FAIL, NOT_RUN, or
   BLOCKED with exact commands and results.
5. Review the fix diff for issue coverage, unintended changes, secrets, diagnostics,
   compatibility, and new regression risk. Do not mark issues APPROVED.
6. Emit the FIX CODE REVIEW REPORT with each issue disposition, corrections, checks,
   exact new baseline, and READY_FOR_RE_REVIEW or BLOCKED status.
   Carry each unresolved BLK-* ID, owner, action, and resume condition unchanged unless
   new evidence updates it. Mark proposed closure EVIDENCE_SUPPLIED, never RESOLVED;
   code-review must confirm it. Missing blocker history requires retrieval.
   An unrelated review gap does not prevent READY_FOR_RE_REVIEW when accepted fixes
   are complete; a gap preventing a safe authorized correction makes this stage BLOCKED.
7. Hand the result to code-review for an independent targeted re-review. Any later code,
   test, fixture, snapshot, or behavior-affecting configuration edit invalidates approval.
   Further review-issue corrections need explicit authorization; verification-authored
   tests return directly through review under the existing verification scope.

## Outputs

A concise FIX CODE REVIEW REPORT with status:

- READY_FOR_RE_REVIEW — authorized fixes/tests are complete; code-review must decide.
- BLOCKED — a correction requires missing evidence, access, authority, or product input.

The report never returns APPROVED and never hands directly to verification.

## Completion criteria

Every open issue has an evidence-backed disposition, accepted fixes are minimal, tests
are truthful, unrelated changes are preserved, and the exact post-fix baseline is ready
for independent code-review. No unrequested issue or technical debt was changed.

## Failure and blocked behavior

Use BLOCKED when authorization, report/baseline compatibility, requirements/root-cause
evidence, credentials, dependencies, or safe test capability is missing. Leave partial
changes visible, name the owner/action/resume condition, and never bypass re-review.

## Human intervention

Ask for direction when a finding depends on product intent, the review evidence is
incorrect but cannot be disproved locally, authorization does not cover the required
change, or review_cycles reaches 3. The initial blocking review counts as one; fixes
never increment or reset this counter. Beyond the limit, require human direction and
retain history. Present issue IDs, attempted fixes,
test results, and the exact decision needed.
