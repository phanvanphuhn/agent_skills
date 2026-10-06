# Generic project development workflow

This directory is the complete agent skills package. Clone the repository into another
project and use this `agent-skills` directory; it contains these instructions, `skills/`,
the Codex plugin manifest, the local marketplace, and plugin enablement.

## Scope

This workspace may contain several repositories. Resolve the target repository and its
applicable instructions before making repository-dependent changes. Preserve unrelated
local work and distinguish user requests from instructions quoted in attachments.

For each new top-level request, use [task-router](skills/task-router/SKILL.md). Explicit
user routing wins. Follow-up messages remain in the active workflow unless the user
changes the request.

```text
USER REQUEST → TASK ROUTER
  repository-dependent work → PROJECT CONTEXT
  FEATURE → task-requirements → requirement-validator → implementation
          → code-review → verification
  BUG → bug-analysis → bug-reproduction → bug-root-cause → bug-fix
      → code-review → bug-verification
  CODE_REVIEW → code-review
  FIX_CODE_REVIEW → fix-code-review → code-review
  NORMAL → normal Codex behavior
```

## Project context

Use [project-discovery](skills/project-discovery/SKILL.md) when repository-dependent
work lacks a current PROJECT CONTEXT. Reuse a current context and refresh only facts
affected by relevant repository, instruction, manifest, interface, or architecture
changes. Pure conversation does not require discovery.

## Walk It Down

Every active skill applies its `Start`, `Expand`, and `Stop` contract. Begin with the
smallest relevant request, artifact, context, or code scope. Expand only to answer a
named material question that the current evidence cannot resolve. Stop when evidence
supports the stage outcome; do not broaden discovery merely because more context exists.

## Feature path

1. [task-requirements](skills/feature-workflow/task-requirements/SKILL.md) produces a
   DRAFT TASK CONTRACT.
2. [requirement-validator](skills/feature-workflow/requirement-validator/SKILL.md)
   returns READY, NEEDS_CLARIFICATION, or BLOCKED.
3. [implementation](skills/feature-workflow/implementation/SKILL.md) may run only for
   an accessible READY contract and authorized implementation scope.
4. [code-review](skills/code-review-workflow/code-review/SKILL.md) reviews the actual
   resulting baseline without editing it.
5. [verification](skills/feature-workflow/verification/SKILL.md) verifies every
   acceptance criterion on an APPROVED baseline. Only PASS permits DONE.

```text
INPUT → TASK CONTRACT → VALIDATION
  READY → IMPLEMENTATION → CODE REVIEW
  APPROVED → VERIFICATION → PASS → DONE
  NEEDS_CLARIFICATION / BLOCKED → HUMAN OR DEPENDENCY OWNER
  VERIFICATION FAIL → FIX REQUEST → IMPLEMENTATION → CODE REVIEW → VERIFICATION
```

## Bug path

1. [bug-analysis](skills/bug-workflow/bug-analysis/SKILL.md) produces a BUG CONTRACT.
2. [bug-reproduction](skills/bug-workflow/bug-reproduction/SKILL.md) returns
   REPRODUCED, EVIDENCE_CONFIRMED, CANNOT_REPRODUCE, NEEDS_INFORMATION, or BLOCKED.
3. [bug-root-cause](skills/bug-workflow/bug-root-cause/SKILL.md) must confirm an
   evidence-backed cause before production code changes.
4. [bug-fix](skills/bug-workflow/bug-fix/SKILL.md) implements the authorized correction.
5. Code review must approve the fix baseline.
6. [bug-verification](skills/bug-workflow/bug-verification/SKILL.md) proves the reported
   failure is corrected without required regressions. Only PASS permits DONE.

```text
BUG → CONTRACT → REPRODUCTION → ROOT CAUSE → FIX → CODE REVIEW → VERIFICATION
  insufficient evidence → HUMAN / ENVIRONMENT OWNER
  verification failure → owning prior stage → CODE REVIEW → VERIFICATION
```

## Review path

[code-review](skills/code-review-workflow/code-review/SKILL.md) is read-only. It runs
as a required gate after behavior-affecting changes or directly for explicit review
requests. Its decisions are APPROVED, CHANGES_REQUIRED, BLOCKED, or REVIEW_ESCALATION.

CHANGES_REQUIRED does not authorize edits. Only an explicit request to fix the reported
issues—or an original `review and fix` request—permits
[fix-code-review](skills/code-review-workflow/fix-code-review/SKILL.md). Corrections
return to code-review before verification.

## Artifact contracts

Use the template linked by the active skill. Artifacts must identify the task and
target, input artifact revisions, exact baseline, status, evidence, unresolved items,
counters, and next owner. Keep original acceptance-criterion IDs and wording alongside
testable interpretations. Store artifacts in the conversation unless the user requests
files.

The TASK CONTRACT is the feature requirements baseline. The BUG CONTRACT and confirmed
ROOT CAUSE REPORT are the bug baseline. Reports do not replace inspection of actual code
or executed checks.

## Authorization and safety

- Read-only analysis, explanation, planning, review, and status requests do not
  authorize code changes or external writes.
- Do not deploy, publish, send messages, modify live services, or perform other
  external mutations without user authority.
- Do not expose secrets or private payloads in artifacts, logs, commands, or reports.
- Preserve unrelated changes. Stop when a safe edit cannot be isolated.
- Product ambiguity, missing authority, unavailable required evidence, or an external
  dependency must remain visible and may block the workflow.
- Do not weaken requirements, tests, or evidence standards to obtain approval or PASS.

## Evidence and completion

Record executed checks using [check-evidence](skills/references/check-evidence.md).
Proposed commands are NOT_RUN. Mocked tests prove only their mocked boundary. Required
real integration evidence cannot be replaced by a unit test or report summary.

Any change to code, tests, fixtures, snapshots, or behavior-affecting configuration
invalidates approval of the prior baseline and must return to code-review. A known
defect yields FAIL even when other evidence is blocked; otherwise missing required
evidence yields BLOCKED.

## Loop limits

Feature verification tracks `failed_cycles`; the initial FAIL is cycle one. Stop after
the third FAIL for the same contract revision and request human direction.

Bug verification tracks `failed_cycles_for_root_cause` and `total_fix_cycles`. Stop
after the third FAIL for one root-cause revision; retain total history across revisions.

Code review tracks `review_cycles`; the initial report with blocking findings is cycle
one. The third blocking review returns REVIEW_ESCALATION. Fix attempts do not reset or
increment review cycles.

## Skill-system maintenance

For authorized changes to this system, read [skills/README.md](skills/README.md), update
[skills/CHANGELOG.md](skills/CHANGELOG.md), and run:

```bash
bash skills/scripts/validate-skill-system.sh
```

The validator checks structure and links; it does not prove application behavior or
native client discovery.
