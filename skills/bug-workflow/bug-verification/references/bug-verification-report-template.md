# BUG VERIFICATION REPORT

- Bug ID / target: <matching BUG CONTRACT>
- Project context: <PROJECT CONTEXT revision used for the verified baseline>
- Bug contract revision: <bN>
- Reproduction report/status: <artifact/status>
- Root-cause revision: <rcN>
- Fix revision: <fN>
- Approved code review: <CODE REVIEW REPORT revision and exact baseline>
- Final baseline: <code/test/config content identity; matches approval or changed paths requiring review>
- Status: <PASS / FAIL / BLOCKED>
- Failure classification: <IMPLEMENTATION_ISSUE / ROOT_CAUSE_INCORRECT / REQUIREMENT_UNCLEAR / N/A>
- Verification level: <V0-V6 and reason for stopping/escalating>
- Failed cycles for root cause: <0-3 after this result>
- Total fix cycles: <count retained across root-cause revisions>

## Verification Scope

<Original failure, cause, fix boundary, regression surface, and required environments.>

## Evidence Chain

- Reported failure: <contract/evidence>
- Reproduction: <report/evidence>
- Root cause: <report/evidence>
- Implementation: <file/symbol/change>
- Regression test: <test/result>

## Original Failure Verification

- Before-fix evidence: <FAIL/equivalent direct evidence/NOT_RUN with reason>
- After-fix evidence: <PASS/FAIL/NOT_RUN/BLOCKED>

## Root Cause Coverage

<Whether the actual change removes the confirmed causal path and why.>

## Preserved Behavior and Regression

- <behavior/boundary/check/result>

## Code and Architecture Review

- <approved review reference; only new contradictory evidence or affected changes>

## Commands Executed

Use the shared [check evidence record](../../../references/check-evidence.md).
List new CHK-* records or REUSED references with matching inputs/environment/baseline.
- NOT_RUN: <required command/evidence and reason>

## Failures and Limitations

- <defect, missing evidence, environment limitation, or none>

## Cycle History

1. <root-cause revision, fix revision, classification, decisive evidence, action>

## Human-Ready Comment

<For BLOCKED or third FAIL: concise ticket-ready summary and exact request. Otherwise N/A.>

## Handoff

- PASS: DONE only with final baseline matching review approval.
- FAIL / IMPLEMENTATION_ISSUE: bug-fix with BUG FIX REQUEST, then code-review before re-verification.
- FAIL / ROOT_CAUSE_INCORRECT: bug-root-cause with new evidence and request.
- FAIL / REQUIREMENT_UNCLEAR: human/bug-analysis; revise the contract before resuming.
- BLOCKED: named owner/action/resume condition.
- Pending review: changed diff/baseline → code-review → bug-verification; counters
  unchanged, classification N/A unless a known defect establishes FAIL.
