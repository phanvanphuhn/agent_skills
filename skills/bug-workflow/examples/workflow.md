# Worked bug workflow example

This fictional example demonstrates routing, evidence separation, a confirmed root
cause, a failed first fix, focused repair, and final PASS. Commands and paths are
illustrative; no application check is claimed to have run.

## Input and Route

> Fix the checkout issue: after a payment retry succeeds, the Continue button stays
> disabled. QA reproduced it in build 123 and attached a network trace.

```text
ROUTE: BUG
CONFIDENCE: HIGH
```

task-router passes the original request and attachment to bug-analysis, then stops.

## BUG CONTRACT

- Bug ID / title: PAY-42 — Continue disabled after successful payment retry
- Target: `mobile-app` / checkout payment state
- Revision: b1
- Status: DRAFT
- Requested scope: investigate, fix, and verify
- Sources: E1 QA report; E2 `retry-success.har`
- Prior revision / changes: initial
- Context used: L1

### Bug Summary

Checkout does not enable Continue after a failed payment attempt is retried successfully.

### Expected Behavior

Continue becomes enabled when the retry response succeeds.

### Actual Behavior

QA reports that Continue remains disabled after the successful retry.

### Environment

- Environment: QA
- App version/build: 123
- Platform/OS/device: Android 15 / emulator model UNKNOWN
- Account/role/state/data: test account; first attempt declined, second accepted
- External services/flags/config: payment QA endpoint; flags UNKNOWN

### Occurrence

- Timestamp/timezone: 2026-09-22 10:14 UTC
- Frequency: 3/3 on supplied sequence

### Reproduction Steps

1. Submit a payment that returns declined.
2. Retry with the supplied successful test method.
3. Observe the Continue button.

### Evidence

- E1 Observation: QA reports 3/3 occurrences in build 123. Limitation: reporter evidence.
- E2 Observation: first response is `DECLINED`; retry is HTTP 200 with `APPROVED`.
  Demonstrates: backend accepted retry. Limitation: does not establish UI state handling.

### Known Facts

- KF1: The supplied retry response is successful (E2).

### Unknowns

- U1: Whether the app reducer consumes the second response.

### Initial Suspicions

- H1 HYPOTHESIS: retry success does not replace the prior disabled state.

### Potentially Relevant Areas

- Checkout payment state reducer and Continue selector, based on the symptom.

### Reproduction Requirements

- Build 123 or source-equivalent tests and the declined-then-approved sequence.

### Investigation Priority

1. Reproduce the transition and inspect state after the approved response.

### Handoff

- Next stage: bug-reproduction.
- Open unknowns: U1.

## REPRODUCTION REPORT

- Bug contract revision: b1
- Status: REPRODUCED
- Context used: L3 to inspect the direct reducer test after L1 evidence
- Attempt number: 1

### Expected / Reported / Observed

- Expected: enabled after approved retry.
- Reported actual: disabled.
- Observed: focused test produces `canContinue=false` after DECLINED → APPROVED.

### Environment and State

Local unit-test environment matching checkout state schema at build 123.

### Attempts

1. Added an isolated declined-then-approved fixture; test failed consistently.

### Confirmation Evidence

- T1 `payment-state.spec.ts`: expected `true`, received `false` after retry.

### Reproduction Steps

1. Initialize checkout state.
2. Reduce DECLINED attempt one.
3. Reduce APPROVED attempt two.
4. Evaluate Continue selector; it incorrectly returns false.

### Investigation Log

- U1: L3 test confirms the reducer receives both responses; stop with reproduction.

### Missing Information or Blocker

- None.

### BUG COMMENT

N/A.

### Handoff

- Route to bug-root-cause.

## ROOT CAUSE REPORT

- Bug contract revision: b1
- Reproduction report/status: rr1 / REPRODUCED
- Root-cause revision: rc1
- Status: CONFIRMED
- Confidence: HIGH — deterministic failing test and state-path evidence
- Context used: L4 for the direct selector dependency

### Symptom and Failure Path

DECLINED sets `paymentLocked=true`; APPROVED updates status but does not clear that flag;
the Continue selector requires `paymentLocked=false` and remains disabled.

### Hypotheses

- H1 stale lock flag — CONFIRMED; state snapshots show it remains true after APPROVED.
- H2 response not received — REJECTED; reducer trace contains the approved action.

### Confirmed Root Cause

The APPROVED reducer branch does not clear the attempt-scoped payment lock.

### Affected Code and Fix Strategy

- `payment-state.ts` APPROVED branch and transition tests.
- Clear the attempt-scoped lock on approval; preserve permanent fraud locks.

### Tests Required

- Declined → approved enables Continue.
- Fraud-locked → approved remains disabled.
- First-attempt approval remains enabled.

### Handoff

- Route to bug-fix.

## BUG FIX REPORT f1

- Root-cause revision: rc1
- Fix revision: f1
- Status: IMPLEMENTED
- Fix cycles: total 0; rc1 0 before verification

### Root Cause to Change Mapping

- Stale attempt lock → clear `paymentLocked` in APPROVED branch → selector can enable.

### Regression Test and Developer Checks

- T1 failed before and passed after the change.
- Focused state test command passed; broader module tests were NOT_RUN by developer.

### Handoff

- Route to bug-verification.

## BUG VERIFICATION REPORT — first cycle

- Root-cause revision: rc1
- Fix revision: f1
- Status: FAIL
- Failure classification: IMPLEMENTATION_ISSUE
- Verification level: V3
- Failed cycles for root cause: 1
- Total fix cycles: 1

### Evidence Chain and Result

T1 passes, but the required fraud-lock boundary test fails: f1 clears both the
attempt-scoped and permanent lock. The root cause remains supported; implementation is
too broad.

### BUG FIX REQUEST fr1

- Route to: bug-fix
- Failed expectation: permanent fraud locks must remain disabled.
- Reproduction: run the checkout state module tests.
- Required correction: clear only the attempt-scoped lock on approval.
- Constraint: preserve fraud-lock behavior and the now-passing retry test.

## BUG FIX REPORT f2

- Root-cause revision: rc1
- Input fix request: fr1
- Fix revision: f2
- Status: IMPLEMENTED
- Fix cycles: total 1; rc1 1 before verification

The reducer now clears only `attemptPaymentLocked`; T1 and all three boundary tests pass.

## BUG VERIFICATION REPORT — final

- Root-cause revision: rc1
- Fix revision: f2
- Status: PASS
- Failure classification: N/A
- Verification level: V4; module tests and required static checks passed
- Failed cycles for root cause: 1
- Total fix cycles: 1

### Evidence Chain

- Reported failure: b1/E1-E2.
- Reproduction: rr1/T1 failed on the original behavior.
- Root cause: rc1 state snapshots prove the stale attempt lock.
- Implementation: f2 clears only the attempt-scoped lock.
- Regression: original retry and preserved fraud-lock tests pass.

### Commands Executed

- Focused regression, checkout module suite, type check, and lint: PASS in the example.

### Handoff

- PASS: DONE.

The router does not run again between artifacts. The first FAIL returns only to bug-fix,
and the root-cause counter remains one after final PASS; history is not rewritten.
