---
name: task-requirements
description: "Converts development stories, acceptance criteria, designs, contracts, mapping files, and repository evidence into a TASK CONTRACT. Use at the start of a development task or when its requirements change."
---

# Task requirements

## Responsibility

Act as a senior technical analyst/software engineer. Turn task evidence into a
structured TASK CONTRACT that another stage can validate without hidden context.

## Trigger

Run when a development task first arrives, when explicitly requested, or when new
requirements require a revised contract. Start from examples of the desired output
when available and identify the inputs, transformations, and checks that produce it.

## When not to run

Do not run for a standalone explanation/status request, an implementation repair
against an unchanged READY contract, or a verification-only handoff. Do not implement
production code, decide unresolved product behavior, or label the contract READY.

## Inputs

- Current PROJECT CONTEXT revision covering the target repository/workspace.
- The user's requested change and any supplied story, description, or ACs.
- Available designs, screenshots, API contracts, mappings, documentation, comments,
  approved examples, prior decisions, and related implementation.
- Target repository/workspace and applicable instructions.
- Previous contract and new evidence when revising a task.

## Context budget

Default exploration level: L1. Start with the user story, description, ACs,
explicitly supplied files, and referenced artifacts. Do not reverse engineer the
whole project; deep investigation belongs to requirement-validator.

When repository evidence is necessary to understand or normalize a requirement,
search at L2 and read only the directly relevant file at L3. Stop when the contract
can state the current evidence and remaining unknown. Record deeper questions for
the validator rather than expanding into dependencies, analogous features, or broad
architecture. Every escalation must name the requirement it is trying to clarify.

## Procedure

1. Read workspace `AGENTS.md` and the task context. Identify the target repository
   and user-authorized outcome. Inventory available and missing source material.
2. Read supplied/referenced files. If needed to understand a requirement, run a
   targeted search and inspect only the direct responsible file. Record evidence,
   the context level reached, and unknowns; leave deep reverse engineering to the
   validator.
3. Separate current behavior, requested behavior, source conflicts, and assumptions.
   Preserve original ACs and normalize each into explicit conditions without
   changing meaning. If no ACs exist, propose labeled derived criteria for validation.
4. Identify functional/non-functional requirements, dependencies, constraints,
   edge cases, reuse opportunities, and concrete verification obligations.
5. Read the [TASK CONTRACT template](references/task-contract-template.md) and produce
   its applicable sections. Group empty optional sections as `N/A — sections/reason`.
   Preserve every AC, constraint, assumption, unknown, and verification obligation.
6. Check that every supplied AC and material source is represented and that unknowns
   remain visible. Handoff to requirement-validator.

## Outputs

A concise TASK CONTRACT with task identity, revision, sources, applicable sections,
testable ACs, explicit assumptions/unknowns, and status DRAFT. Cite repository
evidence and source sections rather than narrating the investigation. Prefer IDs,
short decisions, and locations over repeated prose.

## Completion criteria

Every available source has been assessed; current behavior is evidenced or marked
unknown; each AC retains its meaning and has a verification requirement; relevant
direct files and visible reuse patterns are identified or left as validator unknowns.
The artifact is sufficient for validation, even if it exposes blockers rather than
implementation-ready requirements.

## Failure and blocked behavior

If a source is unreadable or the target cannot be determined, record the exact
limitation and emit a partial DRAFT contract with visible unknowns. Never invent
missing source content. Send those gaps to requirement-validator; use the shared
stop rules if required access or authority is unavailable.

## Human intervention

Ask only for missing user intent or inaccessible inputs that cannot be discovered
locally. Product conflicts and stakeholder questions are finalized by the validator.
Continue independent evidence gathering while a non-blocking question is pending.
