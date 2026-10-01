---
name: requirement-validator
description: "Checks a TASK CONTRACT against repository evidence and resolves whether feature work is READY, needs clarification, or is blocked."
---

# Requirement validator

## Purpose

Confirm that a TASK CONTRACT is complete, consistent, technically actionable, and
verifiable before implementation.

## Use when

Run after task-requirements, after stakeholder answers, or when later evidence reveals
a requirements conflict. Do not implement or silently choose product behavior.

## Inputs

- Current PROJECT CONTEXT.
- Complete TASK CONTRACT and cited sources.
- Relevant repository code, configuration, tests, interfaces, and decisions.
- Prior validation report and stakeholder answers when resuming.

## Required outcome

Produce a [VALIDATION REPORT](references/validation-report-template.md) with exactly one
status: READY, NEEDS_CLARIFICATION, or BLOCKED. Classify each unresolved item as
ANSWERED_BY_CODE, SAFE_ASSUMPTION, NEEDS_CLARIFICATION, or BLOCKER and cite evidence.

READY requires unambiguous acceptance criteria, available implementation contracts,
and adequate verification obligations. If requirements changed, include the finalized
READY TASK CONTRACT; otherwise promote the accessible unchanged contract by reference.

## Boundaries

Repository behavior does not override an explicit requested change. Do not mark missing
evidence as inspected, treat a product choice as a technical assumption, or carry READY
across a material contract change without validation.

## Handoff

READY proceeds to implementation only when the user authorized implementation.
NEEDS_CLARIFICATION or BLOCKED stops with concise questions/actions, owner, impact, and
resume condition.
