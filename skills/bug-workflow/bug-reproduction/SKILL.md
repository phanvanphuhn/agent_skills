---
name: bug-reproduction
description: "Reproduces or evidence-confirms a BUG CONTRACT before production code changes, and produces actionable ticket comments when information or access is missing. Use after bug-analysis or when new reproduction evidence arrives."
---

# Bug reproduction

## Responsibility

Act as a senior developer/debugging engineer. Confirm the reported failure through
direct reproduction or sufficiently strong evidence before production code changes.

## Trigger

Run after bug-analysis, after requested information arrives, or when a fix/verification
finding requires renewed reproduction. Use the current BUG CONTRACT revision.

## When not to run

Do not modify production code, claim reproduction from a reporter statement alone,
or explore broadly before targeted evidence warrants it. Do not repeat attempts that
cannot answer a new question.

## Inputs

- Current PROJECT CONTEXT revision covering the target repository/workspace.
- BUG CONTRACT and every evidence item it cites.
- Available local/DEV/QA/UAT environment, build, account/state/data, and tools.
- Applicable repository instructions and previous reproduction report, if resuming.

## Investigation strategy — Walk It Down

For each unresolved reproduction question, progress only as necessary:

- L0 — BUG CONTRACT and earlier structured artifacts.
- L1 — supplied logs, video, screenshots, crash/network/API/monitoring evidence.
- L2 — targeted symbol, error, route, API, flag, or domain search.
- L3 — directly responsible implementation and related tests.
- L4 — direct dependencies, state, navigation, services, APIs, and tests.
- L5 — similar implementation or architecture needed to explain setup/behavior.
- L6 — broader investigation only when L0-L5 cannot resolve a material blocker.

Every escalation names a stable unknown/hypothesis and stops when evidence is enough.

## Procedure

1. Compare EXPECTED, REPORTED ACTUAL, and OBSERVED. Select the smallest safe
   environment that can answer the highest-priority question. Never mutate production
   data merely to reproduce a bug or perform an unauthorized external write.
2. Follow supplied steps exactly first. Then vary only evidence-backed state/data,
   build, device, timing, or dependency conditions. Record environment and results.
3. When useful, add an isolated failing test/fixture or use existing diagnostics,
   without changing production behavior. Preserve a useful failing test for the fix.
4. If direct reproduction succeeds, record exact steps/state/logs and return REPRODUCED.
5. If direct reproduction is unavailable/unnecessary but evidence proves the failure
   path, return EVIDENCE_CONFIRMED and state exactly why. Historical/intermittent or
   external failures may qualify; inference without direct evidence does not.
6. After reasonable attempts without the behavior, return CANNOT_REPRODUCE. If the
   input cannot support a meaningful attempt, return NEEDS_INFORMATION. If tooling,
   environment, permission, or external dependency prevents it, return BLOCKED.
7. For CANNOT_REPRODUCE/NEEDS_INFORMATION/BLOCKED, produce a concise professional
   BUG COMMENT with what was checked, observed result, and only actionable requests.
8. Emit the complete [REPRODUCTION REPORT](references/reproduction-report-template.md)
   and route according to status.

## Outputs

A REPRODUCTION REPORT with exactly one status: REPRODUCED, EVIDENCE_CONFIRMED,
CANNOT_REPRODUCE, NEEDS_INFORMATION, or BLOCKED. Where stopped, include paste-ready
ticket text without internal reasoning.

## Completion criteria

Claims match actual evidence; attempts/environment are reproducible; expected,
reported, and observed behavior are distinct; limitations and next stage are clear.
Only REPRODUCED/EVIDENCE_CONFIRMED normally proceed to root-cause analysis.

## Failure and blocked behavior

Do not modify production code based only on speculation. CANNOT_REPRODUCE returns to
the human unless compelling independent technical evidence justifies root-cause work;
document that exception explicitly. BLOCKED names the owner/action/resume condition.

## Human intervention

Use the report's BUG COMMENT. Ask only questions that change reproduction or evidence
quality, such as affected build, time/timezone, device/OS, consistency, state/data,
or a specific log/video/network trace.
