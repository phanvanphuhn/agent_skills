# ROOT CAUSE REPORT

- Bug ID / target: <matching BUG CONTRACT>
- Bug contract revision: <bN>
- Reproduction report/status: <artifact and REPRODUCED/EVIDENCE_CONFIRMED/qualified exception>
- Root-cause revision: <rc1; increment only for materially changed cause/evidence>
- Status: <CONFIRMED / INSUFFICIENT_EVIDENCE / BLOCKED>
- Confidence: <HIGH / MEDIUM / LOW with one-sentence reason>
- Context used: <max L0-L6 and hypothesis justifying escalation>

## Symptom

<Observed confirmed failure.>

## Reproduction Evidence

<Artifact/evidence IDs and limitations.>

## Failure Path

<Concise causal sequence from trigger/state to symptom.>

## Hypotheses

- H1: <hypothesis> — <CONFIRMED/REJECTED/UNCONFIRMED>; evidence/test/result.

## Confirmed Root Cause

<Actionable technical cause, or N/A with insufficient evidence.>

## Evidence

- <failing test/path/stack/log/code/history evidence and what it proves>

## Affected Code

- <file/symbol/line and role in failure>

## Why Existing Behavior Fails

<Direct explanation tied to evidence.>

## Regression Risk

<Affected paths/states/consumers and risk evidence.>

## Fix Strategy

<Smallest safe correction; no implementation details unsupported by evidence.>

## Areas That Must Not Change

- <existing behavior/contract to preserve>

## Tests Required

- <original failure regression plus boundaries/error/state/API/platform checks tied to cause>

## Handoff

- CONFIRMED with adequate confidence: bug-fix.
- INSUFFICIENT_EVIDENCE/LOW: bug-reproduction or human, with exact required evidence.
- BLOCKED: named owner/action/resume condition.
