---
name: implementation
description: "Implements a validated READY TASK CONTRACT or repairs defects from a FIX REQUEST while preserving its acceptance criteria. Use after requirement validation authorizes the implementation stage or verification returns FAIL."
---

# Implementation

## Responsibility

Act as a senior developer implementing the smallest safe change that satisfies
the validated TASK CONTRACT. Keep production behavior aligned with that contract.

## Trigger

Run after a READY validation with user authorization to change code. In repair mode,
run with the same READY contract and the latest FIX REQUEST and VERIFICATION REPORT.

## When not to run

Do not run for DRAFT, NEEDS_CLARIFICATION, or BLOCKED requirements, planning-only
requests, unavailable contracts, stale READY revisions, or after the failure limit
without human direction. Do not implement speculative product behavior.

## Inputs

- Current PROJECT CONTEXT revision covering the target repository/workspace.
- Complete READY TASK CONTRACT and matching VALIDATION REPORT.
- User-authorized scope and target repository/workspace instructions.
- In repair mode: FIX REQUEST, latest VERIFICATION REPORT, prior implementation
  report, failed-cycle count, and any human direction after escalation.

## Context reuse rule

Treat the validated TASK CONTRACT as the primary task context. Start with its
Relevant Files / Components, Existing Patterns, Dependencies, constraints, and
verification requirements. Do not repeat requirement discovery or validator research.

If implementation reveals missing evidence, walk from a targeted L2 search to the
relevant L3 file and then an L4 direct dependency. Expand further only when blocked,
and record the unresolved question that justified it. Return a product ambiguity to
requirement-validator instead of solving it through additional code exploration.

In repair mode, load the READY contract only as the baseline and focus on the FIX
REQUEST, failed ACs, named files/tests, and latest evidence. Do not replay successful
requirements or restart earlier stages unless the failure exposes ambiguity.

## Minimal change principle

Prefer the smallest implementation that fully satisfies the ACs. Do not refactor or
inspect unrelated modules, rewrite working abstractions, improve unrelated technical
debt, or create a new abstraction without demonstrated reuse or a contract need.

## Execution routing

Apply [shared execution routing](../../references/execution-routing.md) through this profile;
open the linked reference only for an override, delegation, or runtime fallback.

- `START_CLASS`: STANDARD
- `ESCALATE_WHEN`: High-risk architectural ambiguity requires DEEP; localized mechanical READY work may use ECONOMY.
- `DELEGATE_WHEN`: Components do not overlap and have explicit path ownership; one owner retains dependent edits and shared interfaces.

## Procedure

1. Read the entire contract, workspace `AGENTS.md`, and applicable repository
   instructions. Confirm readiness, matching revision, authorization, and loop budget.
2. Inspect the worktree, then the contract-listed files and patterns. Search beyond
   them only when implementation evidence requires it. Select the smallest safe
   change and create a brief internal plan from the existing contract evidence.
3. Follow existing architecture and naming; reuse appropriate abstractions. Preserve
   compatibility unless explicitly changed. Avoid unrelated edits/refactoring and
   handle all documented edge cases. Compare work against the contract throughout.
4. In repair mode, address each requested defect and add focused regression tests.
   If fixing requires a new product decision, return to requirement-validator.
5. Run appropriate developer checks. Review the actual diff for AC coverage,
   unintended changes, errors, edge cases, types, compatibility, and architecture.
   Record successful, failed, blocked, and unexecuted checks accurately.
6. Emit the [IMPLEMENTATION REPORT](references/implementation-report-template.md)
   mapping each AC to actual code and naming remaining review and verification obligations.
7. Hand code, contract, report, and the unchanged failed-cycle count to code-review.

## Outputs

Implementation changes and a concise IMPLEMENTATION REPORT. A completed implementation
pass has status READY_FOR_REVIEW, not task completion. Include exact file
locations, decisions, and check evidence so the verifier can inspect independently;
do not repeat contract prose.

## Completion criteria

The intended change is implemented, each AC maps to code, developer self-review is
complete, unrelated changes are preserved, and risks/test gaps are disclosed. The
mandatory code-review gate is the next stage; only its APPROVED baseline may proceed
to verification, and only verification may return the PASS needed for DONE.

## Failure and blocked behavior

If a contract gap, unavailable dependency, or missing authority prevents progress,
emit a BLOCKED implementation report with any partial changes and precise evidence.
Route product gaps to requirement-validator and environment/authority issues to the
human. Do not claim unfinished work is ready for acceptance.

## Human intervention

Follow the shared three-failure limit. Report the attempted fixes, remaining failing
ACs, and the action/decision needed. Routine engineering choices within a READY
contract do not need repeated approval; record material choices in the report.
