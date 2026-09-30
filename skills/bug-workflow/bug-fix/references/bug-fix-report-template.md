# BUG FIX REPORT

- Bug ID / target: <matching BUG CONTRACT>
- Project context: <PROJECT CONTEXT revision used>
- Bug contract revision: <bN>
- Reproduction report: <artifact/status>
- Root-cause revision: <rcN>
- Fix revision: <f1; increment for each material implementation revision>
- Input fix request: <none or request ID>
- Status: <IMPLEMENTED / BLOCKED>
- Context used: <max L0-L5 and reason for escalation>
- Fix cycles: <total and per-root-cause counts before verification>

## Summary

<What changed and why, tied to the confirmed cause.>

## Root Cause to Change Mapping

- <confirmed cause evidence> → <file/symbol/change> → <expected corrected behavior>

## Files Changed

- `<path>` — <production/test/config purpose>

## Behavior Preserved

- <named behavior/interface outside the failure path and evidence it remains intact>

## Regression Test

- <test/path and relationship to the reproduced failure>
- Before-fix result: <FAIL/equivalent evidence/NOT_RUN with reason>
- After-fix developer result: <PASS/FAIL/NOT_RUN/BLOCKED>

## Developer Checks

Use the shared [check evidence record](../../../references/check-evidence.md).
List CHK-* records here; reference their IDs in regression results and later reports.

## Diff Review

- Scope/unrelated changes: <result>
- Secrets/temporary diagnostics/generated files: <result>
- Architecture/style/error handling: <result>

## Risks and Limitations

- <remaining risk, unexecuted integration evidence, or none>

## Contradictory Evidence

- <evidence that challenges the root cause, or none>

## Handoff

- IMPLEMENTED: route to code-review with the BUG CONTRACT, REPRODUCTION REPORT,
  ROOT CAUSE REPORT, BUG FIX REPORT, actual diff, and directly related tests.
- Contradicted root cause: route to bug-root-cause with exact new evidence.
- BLOCKED: named owner/action/resume condition.
