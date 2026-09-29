---
name: bug-analysis
description: "Normalizes bug reports, media, logs, environment details, and supplied evidence into a BUG CONTRACT. Use when a bug first arrives or material reporter evidence changes."
---

# Bug analysis

## Responsibility

Act as a senior software engineer and technical bug analyst. Convert all explicitly
supplied bug information into a concise evidence-based BUG CONTRACT before investigation.

## Trigger

Run when a bug is reported, when explicitly requested, or when new reporter evidence
materially changes the bug description. The BUG CONTRACT is the baseline for the
bug-reproduction stage.

## When not to run

Do not fix code, prove a root cause, perform broad repository exploration, or treat
the reporter's suspected cause as fact. An unchanged bug already in reproduction,
root-cause, fix, or verification uses its existing contract.

## Inputs

- Current PROJECT CONTEXT revision covering the target repository/workspace.
- Title, description, expected/actual behavior, occurrence time, frequency, and steps.
- Environment, app/build, platform, OS, device, state/data, and user/account context.
- Screenshots, videos, logs, crash/network/API data, monitoring, comments, text files,
  related tickets, and explicitly referenced code or documentation.
- Workspace instructions and prior BUG CONTRACT when revising.

## Context budget

Default to L1: supplied report and evidence. Inspect every supplied artifact relevant
to the bug, using suitable available document/media tools, but do not search the
repository broadly. At most use L2 targeted search or one L3 directly responsible
file to identify a potentially relevant area; leave technical investigation to
bug-reproduction. Tie escalation to a specific missing contract fact and stop early.

## Procedure

1. Identify the target repository/component and authorized scope. Inventory every
   supplied artifact, including timestamps/timezones and environment identifiers.
2. Normalize expected behavior, actual behavior, occurrence, frequency, and reporter
   steps without inventing missing steps or state.
3. For every evidence item, record its type, provenance/location, direct observation,
   and limitation. Separate observations from conclusions. Redact secrets and avoid
   unnecessary personal/account data.
4. Record evidence-supported Known Facts; unavailable information as UNKNOWN; and
   optional Initial Suspicions as HYPOTHESES. A screenshot/log correlation is not a
   confirmed root cause.
5. Identify potentially relevant components only from current evidence. State the
   environment, account/state/data/build/tool access needed for reproduction.
6. Prioritize the next evidence/reproduction action and produce the complete
   [BUG CONTRACT template](references/bug-contract-template.md) with status DRAFT.

## Outputs

A concise BUG CONTRACT containing observations, facts, unknowns, hypotheses,
potential areas, reproduction prerequisites, priority, provenance, and revision.

## Completion criteria

Every supplied artifact is assessed or explicitly unreadable; expected and actual
behavior remain distinct; environment gaps use UNKNOWN; observations are not promoted
to causes; reproduction has a concrete starting point and visible prerequisites.

## Failure and blocked behavior

If an attachment cannot be read or the target is unknown, record the limitation and
produce the partial contract. Never fabricate its contents. bug-reproduction decides
whether remaining evidence supports action, NEEDS_INFORMATION, or BLOCKED.

## Human intervention

Do not ask broad boilerplate questions at analysis time. Record actionable unknowns
and let bug-reproduction request only the information its attempted investigation
shows is necessary.
