# IMPLEMENTATION REPORT

- Task ID / target: <matching contract>
- Project context: <PROJECT CONTEXT revision used>
- Contract revision: <rN>
- Input artifacts: <READY TASK CONTRACT, VALIDATION REPORT, and FIX REQUEST if repair>
- Status: <READY_FOR_REVIEW / BLOCKED>
- Review baseline: <exact commit plus dirty/untracked content identity, or supplied source snapshot>
- Mode: <initial / repair>
- failed_cycles: <carried from latest verification; initially 0>

## Summary

<Problem and resulting behavior, or partial implementation and blocker.>

## Files Changed

- <path>: <change and purpose; distinguish this task's changes from existing local edits>

## Implementation Decisions

- <decision, evidence/pattern, rationale, contract IDs affected>

## AC Mapping

- AC1 → <actual file/symbol/line implementing the behavior; or explicit missing work>

## Assumptions Used

- <validated assumption IDs and how applied; none if unused>

## Developer Checks

Use the shared [check evidence record](../../../references/check-evidence.md).
List CHK-* records here; cite their IDs in AC mappings and later reports.

## Risks

<Specific remaining risk and affected behavior, or none identified.>

## Tests Needed

- <AC/verification obligation; required unit/integration/manual evidence not yet obtained>

## Remaining Concerns

<Unresolved items, external blockers, or none.>

## Repair Response

<For repair: each FIX REQUEST ID → correction and regression evidence. Otherwise N/A.>

## Handoff

- Next stage / owner: <code-review; validator/human if blocked>
- Artifacts: <accessible contract, report, actual diff/code, relevant tests, prior verification/fix request>
- Resume condition: <only if blocked>

Keep the report short. Reference contract and fix IDs instead of repeating their
text; include only decisions, changed locations, results, risks, and next actions.
