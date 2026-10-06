# VALIDATION REPORT

- Task ID / target: <matching contract>
- Project context: <PROJECT CONTEXT revision used for repository evidence>
- Contract revision: <rN>
- Input artifacts: <TASK CONTRACT revision and prior report/answers>
- Status: <READY / NEEDS_CLARIFICATION / BLOCKED>

## Repository Evidence

- <file/symbol/line or command>: <finding and implication>
- Inspected behavior: <architecture/data flow/navigation/state/API/errors/flags/platform/tests as applicable>
- Unavailable evidence: <what could not be inspected and why>

## Uncertainty Assessment

### U1 — <uncertainty>

- Classification: <ANSWERED_BY_CODE / SAFE_ASSUMPTION / NEEDS_CLARIFICATION / BLOCKER>
- Current disposition: <open / resolved>
- Evidence: <source locations and what they establish>
- Answer or assumption: <explicit statement>
- Risk / impact: <affected ACs and consequence>
- Low-risk rationale: <required for SAFE_ASSUMPTION; otherwise N/A>
- Owner: <likely stakeholder if needed>

<Repeat for every unknown, assumption, dependency gap, and newly discovered conflict.>

## Resolved Decisions

- <uncertainty ID>: <stakeholder/source answer, provenance, previous classification, contract effect>

## Questions and Required Actions

### Q1 — <owner>

- Unclear: <specific gap>
- Why it matters: <behavior/effort/AC impact>
- Repository finding: <evidence or searches that did not answer it>
- Concrete options: <only real known options, or explain unavailable>
- Decision/action needed: <one concise stakeholder-ready question/request>
- Blocks: <ACs/requirements and why>

## Readiness Assessment

- AC coverage and consistency: <assessment>
- Dependencies and constraints: <assessment>
- Verification feasibility: <checks and missing prerequisites>
- Accepted safe assumptions: <IDs or none>
- Open clarification/blocker IDs: <IDs or none; must be none for READY>

## Handoff

<READY: emit the finalized TASK CONTRACT if changed; otherwise explicitly promote the
accessible unchanged revision to READY by reference. Recipients resolve the complete
body before implementation. Route only authorized work.>
<NEEDS_CLARIFICATION/BLOCKED: stop implementation; give the human questions/actions and resume condition.>

Keep the report decision-dense. Omit exploratory narration and duplicate contract
text; retain only evidence necessary to support classifications and the next action.
