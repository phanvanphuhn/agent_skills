# Example: optional export filename

This is a fictional worked example. Paths, commands, results, and the code excerpt
illustrate the handoff contract; they are not evidence of tests run in this workspace.
No example action should be executed against the real repositories by default.

## Input

Task DEMO-17 in a fictional Node repository `demo-api`: allow callers of the existing
export endpoint to supply an optional `filename` query parameter.

- AC1: A non-empty filename is used after trimming outer whitespace.
- AC2: An absent or whitespace-only filename uses `export.txt`.
- AC3: Existing response content and HTTP status remain unchanged.

## TASK CONTRACT

- Task ID / title: DEMO-17 — optional export filename
- Target: demo-api
- Revision: r1
- Status: DRAFT
- Requested scope: implementation
- Sources: S1 user story above; S2 `src/export.ts`; S3 `tests/export.spec.ts`; S4 `package.json`
- Prior revision / changes: initial
- Context used: L1 supplied task and referenced files; no escalation required to draft.

### Task

Add optional query filename support to the existing export response.

### Business Intent

Allow callers to identify their exported files while preserving existing clients.

### Current Behavior

`src/export.ts:12` always returns filename `export.txt`, status 200, and the existing
text payload. The query parser already normalizes optional scalar query values.

### Expected Behavior

Use a supplied trimmed non-empty value; otherwise preserve `export.txt`.

### Acceptance Criteria

- AC1 original: "A non-empty filename is used after trimming outer whitespace."
  Normalized: `filename= report.txt ` produces filename `report.txt`.
  Verification: unit assertion on the response filename.
- AC2 original: "An absent or whitespace-only filename uses export.txt."
  Normalized: both an absent value and `filename=   ` produce `export.txt`.
  Verification: separate absent-value and whitespace-only tests.
- AC3 original: "Existing response content and HTTP status remain unchanged."
  Normalized: all cases retain status 200 and the previous payload.
  Verification: regression tests assert both fields.

### Functional Requirements

FR1: Select an optional filename according to AC1/AC2. FR2: Preserve AC3 behavior.

### Non-Functional Requirements

No new measurable targets supplied; preserve existing synchronous response behavior.

### Relevant Files / Components

`src/export.ts`: response builder. `tests/export.spec.ts`: filename/content/status tests.

### Existing Patterns

Existing query parser returns `string | undefined` and rejects repeated query keys.

### Dependencies

Existing runtime and test runner from `package.json`; no external service required.

### Edge Cases

Missing, empty, whitespace-only, padded, and valid filenames. Repeated query keys
remain covered by the existing parser tests and are outside this behavior change.

### Assumptions

A1: Preserve existing parser validation and error behavior.

### Unknowns

U1: Whether the query parser can return arrays instead of a scalar string.

### Implementation Constraints

Reuse the existing parser and response builder; no API shape or payload change.

### Verification Requirements

V1: AC1/AC2 filename tests. V2: AC3 content/status regression tests.
V3: Run `npm test -- --runInBand` and `npx tsc --noEmit` in demo-api.
Commands here are proposed until recorded as executed in the fictional reports below.

### Handoff

Next stage: requirement-validator. Resolve U1 and assess A1 before READY.

## VALIDATION REPORT

- Task ID / target: DEMO-17 / demo-api
- Contract revision: r1
- Input artifacts: TASK CONTRACT r1
- Status: READY
- Repository evidence: `src/query.ts:8` rejects repeated keys and returns `string | undefined`.
- Investigation log: U1 walked L0 contract → L2 parser search → L3 direct parser/tests;
  the signature and tests answered it, so investigation stopped before dependencies.
- U1: ANSWERED_BY_CODE; resolved by the parser signature and tests.
- A1: SAFE_ASSUMPTION; preserve current parser semantics because the requested change
  affects only filename selection and introducing new validation would change scope.
- Questions/actions: none. All criteria have local executable checks.
- Handoff: finalized TASK CONTRACT r1 → implementation.

## TASK CONTRACT — finalized

- Task ID / title: DEMO-17 — optional export filename
- Target: demo-api
- Revision: r1
- Status: READY
- Requested scope: implementation
- Sources: S1 user story; S2 `src/export.ts`; S3 `tests/export.spec.ts`; S4 `package.json`;
  S5 `src/query.ts:8` and parser tests.
- Prior revision / changes: validation finalized r1 without changing requirements.
- Context used: L0 contract → L2 targeted parser search → L3 `src/query.ts` and tests;
  stopped when U1 was answered.

### Task

Add optional query filename support to the existing export response.

### Business Intent

Allow callers to identify exported files while preserving existing clients.

### Current Behavior

`src/export.ts:12` returns `export.txt`, status 200, and the existing payload. The
query parser returns `string | undefined` and rejects repeated keys.

### Expected Behavior

Use a supplied trimmed non-empty filename; otherwise preserve `export.txt`.

### Acceptance Criteria

- AC1 original: "A non-empty filename is used after trimming outer whitespace."
  Normalized: `filename= report.txt ` produces `report.txt`.
  Verification: response filename assertion on padded and valid inputs.
- AC2 original: "An absent or whitespace-only filename uses export.txt."
  Normalized: absent, empty, and whitespace-only values produce `export.txt`.
  Verification: separate tests for all three inputs.
- AC3 original: "Existing response content and HTTP status remain unchanged."
  Normalized: status 200 and previous payload remain identical for all inputs.
  Verification: status/content regression assertions.

### Functional Requirements

FR1: Choose filename according to AC1/AC2. FR2: Preserve AC3 response behavior.

### Non-Functional Requirements

No new measurable targets supplied; preserve synchronous response behavior.

### Relevant Files / Components

`src/export.ts` response builder; `tests/export.spec.ts` behavior tests;
`src/query.ts` existing scalar parser.

### Existing Patterns

Reuse the parser and current response assembly; add behavior tests to the existing suite.

### Dependencies

Runtime/test runner from `package.json`; no external service.

### Edge Cases

Absent, empty, whitespace-only, padded, and valid values. Repeated keys retain
the existing tested parser behavior.

### Assumptions

A1 SAFE_ASSUMPTION, accepted: preserve parser behavior; changing it is outside scope
and unnecessary for the requested filename selection.

### Unknowns

None open. U1 ANSWERED_BY_CODE: `src/query.ts:8` and tests establish scalar inputs.

### Implementation Constraints

Reuse existing parser and response builder; preserve API shape, payload, and status.

### Verification Requirements

V1: AC1/AC2 filename assertions. V2: AC3 status/content regression assertions.
V3: `npm test -- --runInBand` and `npx tsc --noEmit` in demo-api must succeed.
All checks are local. They are proposed until execution is recorded.

### Handoff

Matching VALIDATION REPORT r1 is READY; authorized implementation follows.

## IMPLEMENTATION REPORT — initial pass

- Task ID / target: DEMO-17 / demo-api
- Contract revision: r1
- Input artifacts: finalized READY TASK CONTRACT r1 and VALIDATION REPORT r1
- Status: READY_FOR_REVIEW
- Mode: initial
- failed_cycles: 0

### Summary

Added optional filename selection while preserving status and content.

### Files Changed

- `src/export.ts:12`: filename selection.
- `tests/export.spec.ts`: present/absent filename cases.

### Implementation Decisions

Reused the scalar query parser. Initial selection was:

```typescript
const filename = requestedFilename?.trim() ?? "export.txt";
```

### AC Mapping

AC1/AC2 → `src/export.ts:12`; AC3 → unchanged response content/status assembly.

### Assumptions Used

A1: Existing parser behavior preserved.

### Developer Self-Review

Reviewed scope, parser reuse, and response fields. Whitespace-only coverage was missed.

### Developer Checks

Fictional execution: demo-api, `npm test -- --runInBand`, exit 0, 4 existing tests pass.

### Context Escalation

L3 contract-listed implementation/tests only; no search beyond the READY contract.

### Risks

Uncovered whitespace-only case could violate AC2.

### Tests Needed

Add whitespace-only input, verify content/status for every branch, run type check.

### Remaining Concerns

Coverage gap disclosed; verifier must establish actual behavior.

### Repair Response

Not applicable to the initial pass.

### Handoff

READY contract, implementation report, actual diff, and tests → code-review;
failed_cycles remains 0.

## CODE REVIEW REPORT — review/fix/re-review

- Task / target: DEMO-17 / demo-api
- Mode: REQUIRED GATE
- Review baseline: initial implementation diff
- Review cycle: 1
- Context used: R0 diff → R2 affected test; stopped after AC2 was resolved by code.

### SLP Summary

- Supervisor: AC2 is incomplete because whitespace-only input produces an empty name.
- Lead: existing parser and response architecture are reused appropriately.
- Peer: `trim() ??` does not fall back after `trim()` returns `""`; the required
  whitespace test is missing.

### Consolidated Finding

- CR-001; MEDIUM; `src/export.ts:12`; found by Supervisor and Peer.
- Evidence: optional chaining returns `""` for whitespace and nullish coalescing keeps it.
- Impact: AC2 fails for a required input.
- Action/status: replace the empty-string path with the existing default and add the
  whitespace regression case; FIXED during the required review loop.

### Fix, Self-Test, and Re-review

The review fix uses `requestedFilename?.trim() || "export.txt"` and adds the missing
test. Fictional focused tests pass 6/6 and typecheck exits 0. Targeted re-review confirms
CR-001 is resolved, AC1/AC3 remain unchanged, and no new finding was introduced.

### Final Decision and Handoff

APPROVED for the post-fix diff → verification. Review cycle remains 1; feature
failed_cycles remains 0.

## VERIFICATION REPORT — final pass

- Task ID / target: DEMO-17 / demo-api
- Contract revision: r1
- Input artifacts: READY contract, validation, implementation report, APPROVED CODE REVIEW REPORT
- Final status: PASS
- failed_cycles: 0
- Implementation inspected: approved post-review filename branch and complete assertions.
- Verification scope: V0/V1 repaired diff, V2 AC tests, and contract-required V4
  typecheck; V3/V5/V6 were unnecessary after sufficient passing evidence.
- AC verification: AC1 PASS (padded/valid), AC2 PASS (absent/empty/whitespace),
  AC3 PASS (status/content assertions for each input).
- Other required checks: V1/V2/V3 PASS.
- Regression risk: existing parser and response behavior covered.
- Code quality: fallback follows explicit empty-string rule.
- Architecture compliance: existing parser and response builder preserved.
- Uncovered edge cases: none required by this contract.
- Test coverage: every criterion covered by behavior assertions.
- Commands executed: fictional demo-api `npm test -- --runInBand`, exit 0, 6 passed;
  `npx tsc --noEmit`, exit 0.
- Failures: none remaining.
- Cycle history: review correction occurred before verification; verification PASS;
  failed_cycles remains 0.
- Handoff: DONE, with evidence limited to this fictional local contract.

## Alternative stop paths

If the story omitted blank-input behavior and the repository did not settle it,
the validator would classify it NEEDS_CLARIFICATION, ask the PO to choose the behavior,
and stop before implementation. If a required service could not be reached,
verification would return BLOCKED and identify the missing evidence. If two further
review fixes failed after CR-001, review_cycles would reach three and emit
REVIEW_ESCALATION. A later verification FAIL would route to implementation, then back
through code-review before re-verification; its separate failed_cycles would increment.
