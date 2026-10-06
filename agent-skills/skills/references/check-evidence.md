# Check evidence record

Load when recording or reusing executed checks. Store each record once in its producing
artifact and cite its artifact revision plus `CHK-*` ID downstream. Shared baseline and
environment definitions may be recorded once and referenced by several checks.

## Record

- ID / covers: <CHK-001; AC, requirement, bug, or review issue IDs>
- Execution: <producer/report revision; time; working directory; exact command or manual steps>
- Inputs: <relevant source, tests, fixtures, configuration, dependencies/data; content identity>
- Baseline: <commit plus relevant dirty/untracked content fingerprints, or immutable snapshot>
- Environment: <runtime/tool versions, configuration, service/data state; no secrets>
- Result: <PASS/FAIL/NOT_RUN/BLOCKED; actual exit code or N/A; observed outcome and boundary>
- Evidence: <accessible original tool result or log/artifact reference; decisive excerpt>

Never invent fingerprints, versions, outputs, or execution times. Mark unavailable fields
UNKNOWN; a proposed command is NOT_RUN and has no execution result. Keep raw results
accessible without copying complete logs into every report.

## Reuse decision

Before reuse, independently confirm expected behavior, relevant input content, environment,
and evidence still match. Record `REUSED: artifact/CHK-ID; matching inputs/environment;
current baseline`. It remains evidence of that recorded execution, not a new run.

Rerun if relevant inputs changed, their dependency scope is unknown, original results
are unavailable, state is unstable, or policy requires fresh evidence. A commit ID alone
does not describe a dirty worktree. If a command modifies relevant inputs, record before
and after identities and verify the resulting baseline; updated test assets also need
code review. Reusing checks never substitutes for approval of the current baseline.
