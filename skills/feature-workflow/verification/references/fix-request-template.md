# FIX REQUEST

- Task ID / target: <matching contract>
- Contract revision: <same READY revision>
- Input artifacts: <VERIFICATION REPORT and IMPLEMENTATION REPORT>
- failed_cycles: <current count>
- Routing: <implementation / human intervention at third failure>
- Repair context: <failed AC IDs, named files/tests, decisive evidence; exclude passing analysis>

## Defects

### F1 — <short finding>

- Failing AC / obligation: <stable ID>
- Expected behavior: <contract requirement>
- Actual behavior: <observed result>
- Evidence: <reproduction command, exit code, relevant output or test failure>
- Relevant file: <path/symbol/line>
- Recommended correction: <bounded change, with reasoning>
- Regression verification: <test proving the fix and protecting existing behavior>

<Repeat per defect; do not mix unresolved product decisions into assumed fixes.>

## Constraints

<Preserve the READY contract, unrelated work, and applicable architecture. Do not weaken ACs.>

## Prior Attempts and Remaining Blockers

<Cumulative attempts and why they failed; unrelated missing verification prerequisites.>

## Required Handoff

<After repair: IMPLEMENTATION REPORT → code-review → verification with the same contract revision/count.>
<At limit or a product/authority gap: exact human action required before work resumes.>

Keep this artifact minimal. Include only information needed for the targeted repair;
link to the READY contract for unchanged requirements and do not restate passing ACs.
