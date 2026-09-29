# VERIFICATION REPORT

- Task ID / target: <matching contract>
- Project context: <PROJECT CONTEXT revision used for the verified baseline>
- Contract revision: <rN>
- Input artifacts: <READY TASK CONTRACT, VALIDATION REPORT, IMPLEMENTATION REPORT, APPROVED CODE REVIEW REPORT, prior reports>
- Final status: <PASS / FAIL / BLOCKED>
- failed_cycles: <prior count + 1 for final FAIL; unchanged otherwise>
- Implementation inspected: <files/diff baseline; identify pre-existing local changes>

## Verification Scope

- Changed files: <deterministic manifest or inspected baseline>
- Related tests: <discovered candidates and how completeness was assessed>
- Highest level: <V0-V6>
- Escalations: <V3+ level, risk/policy/evidence that required it; or none>

## AC Verification

### AC1 — <title>

- Implementation: <actual file/symbol/line>
- Test: <test name/path or concrete manual procedure>
- Result: <PASS / FAIL / NOT_RUN / BLOCKED>
- Evidence: <executed command/result, observed behavior, or reason unavailable>
- Boundary: <unit / mock / real integration / manual inspection>

<Repeat for every AC, preserving IDs.>

## Other Required Checks

- <FR/NFR/V/constraint ID>: <test/evidence; PASS/FAIL/NOT_RUN/BLOCKED>

## Regression Risk

<Affected existing behavior and supporting checks.>

## Code Quality

<Concrete findings, not an unsupported approval.>

## Architecture Compliance

<Applicable patterns/instructions and observed compliance or deviations.>

## Uncovered Edge Cases

<Missing coverage, its materiality, and effect on final status.>

## Test Coverage

<Criteria covered, gaps, environment limitations; avoid equating line coverage with correctness.>

## Commands Executed

- <working directory; exact command; exit code; observed result; relevant IDs>
- Proposed but unexecuted: <command; NOT_RUN; reason, or none>

## Failures

- <finding ID; affected AC/obligation; expected/actual; reproduction evidence; severity>
- Concurrent blockers: <missing evidence/action/owner, or none>

## Cycle History

- <cycle: result; fix attempt; changed evidence; cumulative failed_cycles>

## Handoff

<PASS: completion evidence and meaningful limits.>
<FAIL below three: FIX REQUEST and READY contract → implementation → code-review → verification.>
<Third FAIL: FIX REQUEST and cumulative attempts → human intervention; no automatic repair.>
<BLOCKED: exact missing prerequisite, owner, and resume condition; no completion claim.>

Keep the report evidence-dense. Reference the contract/implementation report rather
than repeating them. On FAIL, put repair instructions in the FIX REQUEST only.
