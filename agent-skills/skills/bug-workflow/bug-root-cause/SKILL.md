---
name: bug-root-cause
description: "Establishes an evidence-backed actionable cause for a reproduced or evidence-confirmed bug before code changes."
---

# Bug root cause

## Purpose

Identify and document why the confirmed failure occurs and what correction boundary the
evidence supports.

## Use when

Run after REPRODUCED or EVIDENCE_CONFIRMED, or when verification disproves an earlier
cause. Do not proceed from NEEDS_INFORMATION or BLOCKED evidence.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- BUG CONTRACT and matching REPRODUCTION REPORT.
- Relevant execution evidence, logs/traces, code, tests, configuration, and history.
- Prior ROOT CAUSE REPORT and contradictory verification evidence when revising.

## Walk It Down

- Start: Trace the confirmed symptom through the directly responsible code and state boundary.
- Expand: Follow the next caller, dependency, service, or competing hypothesis only when current evidence cannot explain the failure.
- Stop: Stop when the cause is confirmed with contradictions resolved, or the precise missing evidence prevents confirmation.

## Required outcome

Produce a [ROOT CAUSE REPORT](references/root-cause-report-template.md) with status
CONFIRMED, INSUFFICIENT_EVIDENCE, or BLOCKED. A confirmed report must connect the
observed failure to an actionable cause, affected code, supporting evidence, regression
risk, required preserved behavior, and tests needed for the correction.

## Boundaries

Do not implement a fix, promote correlation or speculation to cause, hide contradictory
evidence, or authorize code changes from insufficient evidence.

## Handoff

CONFIRMED proceeds to bug-fix. INSUFFICIENT_EVIDENCE returns to bug-reproduction or the
human with the exact missing evidence. BLOCKED identifies owner/action/resume condition.
