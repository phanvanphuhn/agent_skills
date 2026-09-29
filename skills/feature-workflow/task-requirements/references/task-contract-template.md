# TASK CONTRACT

- Task ID / title: <stable identity>
- Target: <repository/workspace and relevant component>
- Project context: <PROJECT CONTEXT revision and target>
- Revision: <r1; increment on requirements changes>
- Status: <DRAFT or READY; only requirement-validator assigns READY>
- Requested scope: <analysis/planning/implementation>
- Sources: <S1: user story; S2: source path/section; S3: confirmed stakeholder answer>
- Prior revision / changes: <what changed and why, or initial>
- Context used: <L0-L3; unresolved question that justified any move above L1>

## Task

<Concrete requested change and scope boundaries.>

## Business Intent

<Who benefits and why.>

## Current Behavior

<Observed behavior with file/symbol/line evidence, or explicit unknown.>

## Expected Behavior

<Observable desired behavior; link claims to sources.>

## Acceptance Criteria

### AC1 — <title>

- Original: <original wording and source; label derived criteria if none supplied>
- Normalized: <preconditions, action, observable result>
- Verification: <required evidence/check and boundary: unit, mocked, real integration>
- Conflicts / unresolved interpretation: <none or explicit conflict>

<Repeat for every AC; retain existing identifiers.>

## Functional Requirements

- FR1: <behavior, source, related ACs>

## Non-Functional Requirements

- NFR1: <measurable requirement, source, verification; do not invent targets>

## Relevant Files / Components

- <path/symbol>: <responsibility, observed behavior, likely impact>

## Existing Patterns

- <evidence of analogous behavior and what can be reused>

## Dependencies

- D1: <dependency, owner, available/missing status, task impact>

## Edge Cases

- E1: <case, expected behavior or unknown, related AC/requirement>

## Assumptions

- A1: <assumption, rationale, risk, affected AC; pending validator classification>

## Unknowns

- U1: <uncertainty, evidence searched, effect, likely decision owner>

## Implementation Constraints

<Architecture, compatibility, scope, permissions, platform, naming, dependency constraints.>

## Verification Requirements

- V1: <AC/FR/NFR covered; check or manual evidence; required environment; pass condition>
- Commands: <discovered commands with working directory; label proposed commands>
- Required checks unavailable: <reason and owner, or none>
- Completion boundary: <what must be proven; explicitly distinguish mocked/external stages>

## Handoff

- Next stage: requirement-validator for DRAFT; implementation for authorized READY work.
- Questions / remaining gaps: <stable U/D IDs or none>
- Validation reference: <matching VALIDATION REPORT and revision, required for READY>

Keep entries compact. State decisions, evidence, and open gaps; link to sources
instead of copying long documents or replaying the full investigation.
