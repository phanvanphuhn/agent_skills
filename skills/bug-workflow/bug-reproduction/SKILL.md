---
name: bug-reproduction
description: "Confirms a BUG CONTRACT through direct reproduction or sufficient independent evidence before root-cause work and production changes."
---

# Bug reproduction

## Purpose

Establish whether the reported failure is observable or otherwise proven by available
evidence.

## Use when

Run after bug-analysis, after requested evidence arrives, or when later findings require
reconfirmation. Production code must not be changed in this stage.

## Inputs

- Current PROJECT CONTEXT and repository instructions.
- BUG CONTRACT and all cited evidence.
- Available environment, build, state/data, access, tools, and prior reproduction report.

## Required outcome

Produce a [REPRODUCTION REPORT](references/reproduction-report-template.md) with one
status: REPRODUCED, EVIDENCE_CONFIRMED, CANNOT_REPRODUCE, NEEDS_INFORMATION, or BLOCKED.
Record actual environment, attempts, observed results, evidence limitations, and exact
reproduction steps when available.

## Boundaries

Do not mutate production data, perform unauthorized external writes, infer success from
a reporter statement alone, invent execution evidence, or repeatedly run an unchanged
blocked attempt.

## Handoff

REPRODUCED or EVIDENCE_CONFIRMED proceeds to bug-root-cause. Other statuses stop with a
ticket-ready request identifying the evidence/access owner and resume condition.
