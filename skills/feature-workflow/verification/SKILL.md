---
name: verification
description: "Verifies an APPROVED reviewed implementation and tests against every acceptance criterion in a READY TASK CONTRACT, producing evidence and FIX REQUESTs before development completion."
---

# Verification

## Responsibility

Act as a senior QA engineer with development experience. Independently determine
whether the actual implementation satisfies the TASK CONTRACT with sufficient evidence.

## Trigger

Run after code-review returns APPROVED for the current implementation baseline. It is
the final gate before DONE. Use a separate verification pass; a second agent is not
required.

## When not to run

Do not certify a missing/unvalidated contract, unavailable implementation, outdated
contract revision, or code baseline without a matching APPROVED CODE REVIEW REPORT.
Do not trust implementation or review reports as behavioral proof. Do not change
production code or weaken ACs to make checks pass.

## Inputs

- Complete READY TASK CONTRACT and matching VALIDATION REPORT.
- Actual approved code/diff, tests, IMPLEMENTATION REPORT, and CODE REVIEW REPORT.
- Previous verification/fix reports, failed-cycle count, and relevant human direction.
- Available test environment and authorized verification capabilities.

## Verification strategy — Walk It Down

Proceed from the cheapest/narrowest evidence to broader checks:

- V0 — Compare the diff/code against the READY TASK CONTRACT.
- V1 — Inspect changed files and only the direct dependencies needed for behavior.
- V2 — Run AC-specific tests associated with the changed behavior.
- V3 — Run the affected feature/module suite when V2 is insufficient or policy requires it.
- V4 — Run applicable typecheck, lint, or static analysis required by risk/policy.
- V5 — Run broader regression when shared infrastructure, navigation, common state,
  common components, or public APIs changed, or narrower evidence shows risk.
- V6 — Run the full project suite only when repository policy or demonstrated risk requires it.

Stop when every contract obligation has sufficient evidence. Required checks in the
contract or repository policy are not optional even if they are broad. Record the
highest level reached and why each escalation beyond V2 was necessary. Do not run an
expensive broad check merely because it exists.

Use [changed-files.sh](scripts/changed-files.sh) and
[related-tests.sh](scripts/related-tests.sh) when Git/name-based discovery helps.
Use [verify.sh](scripts/verify.sh) to collect the same manifest and optionally run
one explicit repository-specific command without `eval`. These helpers are seeds,
not proof that all affected tests were found; apply contract and architecture evidence.

## Procedure

1. Read workspace `AGENTS.md`, applicable repository instructions, the contract,
   implementation report, matching APPROVED CODE REVIEW REPORT,
   [verification template](references/verification-report-template.md), and
   [fix request template](references/fix-request-template.md).
2. Start at V0/V1 with actual code and diff. For each AC, trace
   `AC → implementation → test → result`. Evaluate every required obligation.
3. Create or strengthen appropriate automated tests. Where applicable cover negative
   cases, edge cases, errors, state transitions, navigation, API success/failure,
   loading/empty states, platform behavior, and regression risks. Do not mirror
   implementation details in tests without checking observable requirements.
4. Run V2 first, then broaden according to the verification ladder and contract.
   Record directory, command, exit status, and concise observed results. Distinguish
   mock evidence from real external acceptance; do not perform unauthorized live writes.
5. Assess regression risk, quality, architecture compliance, uncovered edges, and
   test coverage. A passing test count alone is not proof of acceptance.
6. Mark checks and individual ACs PASS, FAIL, NOT_RUN, or BLOCKED. PASS requires
   sufficient executed evidence for every required criterion/obligation. A required
   NOT_RUN/BLOCKED check prevents final PASS.
7. Assign final FAIL for an established implementation defect; document any concurrent
   blocked checks too. Otherwise use BLOCKED for missing required evidence and PASS
   only when all required obligations pass. New requirements contradictions return
   to requirement-validator, retaining evidence of any established defects.
8. On final FAIL, increment `failed_cycles` once and emit a FIX REQUEST. Below three,
   route to implementation; every production repair then returns through code-review
   before re-verification. On the third failure stop for human intervention with
   cumulative attempts. Carry the counter unchanged on PASS/BLOCKED.
9. Emit the VERIFICATION REPORT and any FIX REQUEST, then perform the stated handoff.

## Outputs

A concise VERIFICATION REPORT with final PASS, FAIL, or BLOCKED and evidence for every AC.
FAIL additionally produces a FIX REQUEST containing expected/actual behavior,
reproduction evidence, relevant code, and recommended correction for each defect.
On failure, pass only the FIX REQUEST and necessary baseline/evidence into repair;
do not replay the complete workflow.

## Completion criteria

All required criteria have an evidence-backed disposition, commands are truthful,
limitations are explicit, and the next stage/owner is clear. Only final PASS allows
the orchestrator to declare the task complete.

## Failure and blocked behavior

Missing credentials, unavailable dependencies, denied authority, or absent required
environment evidence yield BLOCKED unless a known defect requires FAIL. State which
AC/check cannot be verified and the exact action needed. Do not invent results or
retry an unchanged external blocker indefinitely.

## Human intervention

Stop at three failed cycles, or earlier if a product decision/authority is missing.
Provide cumulative findings, attempted corrections, and the requested decision.
If requirements change, require a revised validated contract before further repairs.
