---
name: task-requirements
description: "Converts development stories, acceptance criteria, designs, mappings, and decisions into a traceable TASK CONTRACT before implementation."
---

# Task requirements

## Purpose

Create the requirements baseline for a feature or intentional behavior change.

## Use when

Run when feature work begins or when its requirements materially change. Do not run
for an unchanged repair, standalone explanation, or verification-only request.

## Inputs

- Current PROJECT CONTEXT.
- User request, story, acceptance criteria, designs, mappings, examples, and decisions.
- Referenced repository evidence and prior TASK CONTRACT when revising.
- Authorized scope and applicable instructions.

## Walk It Down

- Start: Use the request, acceptance criteria, supplied artifacts, and current PROJECT CONTEXT.
- Expand: Search targeted repository evidence only when a contract fact cannot otherwise be normalized.
- Stop: Stop when the DRAFT contract preserves all requirements and exposes every conflict or unknown.

## Required outcome

Produce a DRAFT [TASK CONTRACT](references/task-contract-template.md) that:

- preserves original acceptance-criterion IDs and wording;
- gives each criterion an observable interpretation and verification requirement;
- distinguishes current behavior, requested behavior, assumptions, conflicts, and unknowns;
- identifies relevant components, dependencies, constraints, and required evidence; and
- cites the source of every material requirement or decision.

## Boundaries

Do not implement code, decide unresolved product behavior, invent missing source
content, or mark the contract READY. Unavailable or conflicting requirements remain
visible for validation.

## Handoff

Send the DRAFT TASK CONTRACT to requirement-validator. If the target or essential
source is unavailable, identify the missing owner/action without fabricating a contract.
