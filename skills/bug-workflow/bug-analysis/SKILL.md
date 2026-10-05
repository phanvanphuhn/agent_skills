---
name: bug-analysis
description: "Converts a bug report, attachments, logs, and environment details into a traceable BUG CONTRACT before investigation."
---

# Bug analysis

## Purpose

Create the evidence baseline for investigating reported broken behavior.

## Use when

Run when a bug first arrives or material reporter evidence changes. Reuse the existing
contract once the bug has moved to reproduction, root cause, fix, or verification.

## Inputs

- Current PROJECT CONTEXT.
- Expected and actual behavior, steps, frequency, timestamps, environment, build, state,
  and relevant account/role context.
- Supplied screenshots, videos, logs, traces, network data, comments, and documents.
- Applicable instructions and prior BUG CONTRACT when revising.

## Walk It Down

- Start: Use every supplied report, artifact, environment fact, and current PROJECT CONTEXT.
- Expand: Search metadata or one directly relevant component only when needed to identify the affected area or reproduction prerequisite.
- Stop: Stop when the BUG CONTRACT separates facts, observations, hypotheses, and unknowns without claiming a cause.

## Required outcome

Produce a DRAFT [BUG CONTRACT](references/bug-contract-template.md) that separates
reported behavior from direct observations, records evidence provenance and limitations,
identifies unknowns and reproduction prerequisites, and does not claim a root cause.

## Boundaries

Do not fix code, state speculation as fact, fabricate unreadable artifacts, expose
secrets/private payloads, or claim reproduction that did not occur.

## Handoff

Send the BUG CONTRACT and cited evidence to bug-reproduction. Missing essential target
or artifact access remains explicit with its owner and impact.
