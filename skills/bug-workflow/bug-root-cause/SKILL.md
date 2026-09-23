---
name: bug-root-cause
description: "Tests hypotheses against reproduction and technical evidence to identify the actionable root cause of a confirmed bug. Use after REPRODUCED or EVIDENCE_CONFIRMED, or when verification disproves a prior root cause."
---

# Bug root cause

## Responsibility

Act as a senior debugging/reverse-engineering engineer. Establish why the confirmed
failure occurs before production code changes.

## Trigger

Run after REPRODUCED or EVIDENCE_CONFIRMED. CANNOT_REPRODUCE may proceed only with
documented compelling independent technical evidence. Rerun when verification shows
the assumed root cause is incorrect.

## When not to run

Do not implement fixes, treat correlation as cause, or investigate unrelated code.
Do not proceed from NEEDS_INFORMATION/BLOCKED or weak speculation.

## Inputs

- BUG CONTRACT and REPRODUCTION REPORT at matching revisions.
- Reproduction/failing-test evidence, logs/traces, and relevant code/history/tests.
- Prior ROOT CAUSE REPORT and verification evidence when revising.

## Investigation strategy — Walk It Down

Start from the confirmed symptom and walk backward: failure → responsible component
→ state/data → caller → dependency/API/service → architecture only when necessary.
Apply the reproduction L0-L6 ladder to one active hypothesis at a time. Search before
reading broadly; stop when an actionable technical cause is proven.

Prefer reproduced failure plus a failing test, then deterministic code/stack evidence,
then logs/network/monitoring, then media/report evidence. This is guidance, not a rule
that discards valid lower-level or combined evidence.

## Procedure

1. State the symptom and strongest reproduction/evidence boundary.
2. For each hypothesis record `HYPOTHESIS → EVIDENCE → TEST → RESULT`, classifying it
   CONFIRMED, REJECTED, or UNCONFIRMED. Preserve contradictory evidence.
3. Trace only the path required to test the active hypothesis. Use a lightweight
   Five Whys when useful; do not force five levels or confuse an upstream condition
   with the actionable cause.
4. Prefer deterministic paths, failing tests, stack traces, state transitions,
   contract/mapping mismatches, race evidence, Git regression history, navigation,
   platform code, and flag/config behavior as applicable.
5. Identify affected code, why it fails, regression surface, smallest safe fix
   strategy, behavior that must remain unchanged, and regression tests tied to cause.
6. Assign HIGH/MEDIUM/LOW confidence with evidence. LOW plus speculative code change
   stops and routes back to reproduction/investigation or human evidence.
7. Produce the [ROOT CAUSE REPORT](references/root-cause-report-template.md).

## Outputs

A concise ROOT CAUSE REPORT with a root-cause revision, tested hypotheses, confirmed
cause or explicit insufficiency, affected code, fix boundary, tests, and confidence.

## Completion criteria

A confirmed cause explains the observed path, is supported by reproducible/direct
evidence, survives competing hypotheses, and yields a bounded correction and tests.

## Failure and blocked behavior

Insufficient evidence returns to bug-reproduction with the precise hypothesis and
evidence needed. LOW confidence blocks speculative implementation. Access/environment
limits identify an owner and resume condition.

## Human intervention

Request only evidence/decisions needed to distinguish remaining hypotheses. When a
verification result disproves the cause, revise the report from that new evidence;
do not preserve the earlier conclusion to justify the existing fix.
