---
name: requirement-validator
description: "Validates a TASK CONTRACT by reverse engineering repository behavior and resolving uncertainty before implementation. Use after task-requirements, stakeholder answers, or material requirements changes."
---

# Requirement validator

## Responsibility

Act as a senior developer validating whether a TASK CONTRACT is sufficient to
implement safely. Challenge incomplete or contradictory requirements using evidence.

## Trigger

Run after task-requirements, after clarification answers, or when implementation or
verification discovers a requirements conflict. Run even when a ticket appears simple.

## When not to run

Do not implement production code, silently approve a new product interpretation,
or replace verification of completed code. An unchanged implementation defect
with a valid contract belongs in the implementation/verification repair loop.

## Inputs

- Current PROJECT CONTEXT revision covering the target repository/workspace.
- Complete TASK CONTRACT and its cited sources/revision.
- Repository instructions, relevant code/configuration/tests, and known examples.
- Prior validation report and stakeholder answers if resuming.

## Investigation strategy — Walk It Down

Investigate each unknown progressively and stop as soon as evidence answers it:

1. L0/L1 — Check the TASK CONTRACT and its explicit sources. If answered, stop.
2. L2 — Search for the component, route, API, hook, flag, error code, or domain term.
3. L3 — Read only the files directly responsible for the behavior and related tests.
4. L4 — Inspect direct imports, services, stores, API clients, or tests only as needed.
5. L4 — Search a similar implementation only if architecture/convention is unclear.
6. L5 — Explore broadly only when L0-L4 cannot resolve a material blocker.

Tie every expansion to a stable unknown/requirement ID. Record the maximum level and
decisive evidence, not a transcript of every search. Never explore code "just in case."

## Execution routing

Apply [shared execution routing](../../references/execution-routing.md) through this profile;
open the linked reference only for an override, delegation, or runtime fallback.

- `START_CLASS`: STANDARD
- `ESCALATE_WHEN`: Unresolved cross-system, security, concurrency, or irreversible product risk requires DEEP; bounded lookup may use ECONOMY.
- `DELEGATE_WHEN`: Evidence gathering is independent; one validator owns the final contract decision.

## Procedure

1. Read the contract, workspace `AGENTS.md`, applicable repository instructions,
   and the [validation report template](references/validation-report-template.md).
2. Apply the investigation ladder independently to each material unknown before
   asking questions. Trace only the architecture/data flow needed to resolve it.
   Do not infer desired behavior solely from a legacy implementation.
3. Resolve each assumption, unknown, dependency gap, and discovered conflict into
   exactly one classification, retaining its stable ID:
   - ANSWERED_BY_CODE: cite code/tests/configuration establishing the answer.
   - SAFE_ASSUMPTION: state the assumption and why it is low risk, reversible, and
     does not invent product behavior or change an AC.
   - NEEDS_CLARIFICATION: a stakeholder decision is needed to fix scope/behavior.
   - BLOCKER: missing access, artifact, dependency, or authority prevents readiness.
4. Where an answer comes from an explicit stakeholder/source decision, record that
   provenance as a resolved decision, not ANSWERED_BY_CODE. Preserve the prior
   uncertainty classification in history and exclude resolved items from open gaps.
5. For every NEEDS_CLARIFICATION/BLOCKER, formulate a concise question or action:
   what is unclear, why it matters, repository findings, concrete options if known,
   decision needed, and likely PO/BA/designer/backend/QA/mobile/platform owner.
6. Check AC completeness, consistency, dependencies, technical feasibility,
   implementation constraints, and whether the proposed checks can prove each AC.
7. Emit the report. Use BLOCKED if any hard blocker remains; otherwise use
   NEEDS_CLARIFICATION if a decision remains; otherwise use READY.
8. With READY and changed requirements, emit the complete finalized TASK CONTRACT with
   accepted assumptions, resolved decisions, and report reference. If its entire body
   is unchanged and accessible, explicitly promote that exact revision to READY by
   reference. The recipient must resolve it; never implement from an unavailable body.
   Otherwise hand questions/actions to the human and stop implementation.

## Outputs

A concise VALIDATION REPORT with one final status: READY, NEEDS_CLARIFICATION, or BLOCKED.
READY includes the finalized TASK CONTRACT or explicit promotion of the accessible,
unchanged revision. The other
statuses include questions and required actions sufficient to resume validation.
Reuse contract IDs and sources instead of restating established analysis.

## Completion criteria

Every uncertainty is classified or explicitly resolved with provenance. All ACs
have unambiguous behavior and adequate verification obligations before READY.
READY is permitted with documented low-risk assumptions, but not unresolved product
decisions or missing necessary contracts. It does not authorize additional actions.

## Failure and blocked behavior

Do not label inaccessible code as inspected. If evidence is missing, report its
impact and the precise next action. If a conflict cannot be resolved locally, stop
with NEEDS_CLARIFICATION/BLOCKED and do not implement.

## Human intervention

Ask the generated questions after exhausting relevant local evidence. When answers
arrive, update the contract revision and rerun validation. Never carry READY forward
across a material change without revalidation.
