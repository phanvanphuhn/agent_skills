# Skill-system changelog

## 2026-09-29 — Mandatory SLP code-review gate

- Added the shared `code-review` skill with REQUIRED GATE and MANUAL REVIEW modes.
  It gathers evidence once and reviews through Supervisor, Lead, and Peer perspectives,
  consolidates evidence-backed findings, and returns APPROVED, CHANGES_REQUIRED,
  BLOCKED, or REVIEW_ESCALATION.
- Added the CODE REVIEW REPORT contract, R0-R5 Walk-It-Down strategy, severity and
  finding schemas, NEEDS_CONTEXT/NEEDS_CONFIRMATION boundaries, independent-review
  requirement, and a three-cycle review/fix/self-test/re-review limit distinct from
  feature and bug verification counters.
- Routed every feature implementation and bug fix, including later production repairs,
  through code-review before verification. Upstream rerouting is limited to invalid
  requirements, incorrect root cause, missing authority, or human product decisions.
- Extended task-router with a cheap CODE_REVIEW route for explicit file/diff/commit/
  branch/PR review intent. Manual review remains report-only unless fixes are requested;
  explanations and unrelated NORMAL tasks do not trigger review.
- Updated feature and bug stage contracts, report templates, worked examples, README,
  AGENTS orchestration, and structural validation for the eleventh skill and mandatory
  APPROVED baseline.
- Validation: the dependency-free structural validator passed; all eleven frontmatter
  blocks parsed with Ruby YAML; Bash syntax, local links, required headings, line limits,
  unexpected-skill detection, and trailing-whitespace checks passed. Twelve routing and
  loop scenario assertions passed for feature, bug, NORMAL explanation, manual review,
  review-and-fix, zero findings, blocking findings, invalid root cause, rejected finding,
  repaired-code re-review, NEEDS_CONTEXT, and third-cycle escalation.
- Limit: the bundled skill-creator `quick_validate.py` could not run because PyYAML is
  not installed; the workspace validator and Ruby YAML parser covered its structural
  frontmatter/name/description checks. Real independent-agent calibration remains to be
  exercised on production development tasks.

## 2026-09-23 — Workflow folder organization

- Grouped the architecture into three top-level systems under `skills/`:
  `task-router/`, `feature-workflow/`, and `bug-workflow/`.
- Moved each feature and bug stage skill, its references, workflow example, and owned
  helper scripts into the corresponding workflow folder without changing skill names,
  responsibilities, handoff contracts, or automatic routing behavior.
- Updated orchestration, cross-workflow helper links, README examples, and structural
  validation for recursive skill discovery and exact expected paths.
- Established the convention that future workflow systems are added as sibling folders
  under `skills/`, while their independently triggered stages remain nested inside.
- Validation: all 29 files and all ten skill frontmatter blocks remained present; hash
  comparison found no content changes in mechanically moved artifacts. Structural and
  Bash syntax validation passed from the workspace and a relocated path containing
  spaces. The three verification helpers ran successfully from their new path. A
  recursive negative fixture correctly rejected an unregistered nested workflow skill;
  link, stale-path, trailing-whitespace, and Git diff checks passed.

## 2026-09-23 — Automatic task routing and evidence-first bug workflow

- Added the lightweight `task-router` entry skill. It classifies a new top-level
  request once as FEATURE, BUG, or NORMAL from user intent, routes the untouched input,
  and stops; UNCLEAR is reserved for a genuinely material ambiguity.
- Integrated automatic routing into `AGENTS.md`, including explicit-user overrides,
  NORMAL handling without a specialized workflow, and follow-up isolation.
- Added five single-responsibility bug skills for analysis, reproduction, root-cause
  evidence, minimal correction, and independent verification.
- Added structured bug artifacts, human-ready blocked/information comments, evidence
  hierarchy, L0-L6/V0-V6 walk-down, focused failure routing, and persistent per-cause
  plus total fix-cycle counters with a three-FAIL stop.
- Reused the existing generic changed-file, related-test, and verification command
  helpers rather than duplicating bug-specific scripts.
- Added a fictional end-to-end bug example with a failed first fix, focused BUG FIX
  REQUEST, repair, and final PASS. Updated README discovery, routing, and calibration.
- Expanded structural validation from four to ten skills, all new templates, router
  size/cost boundaries, bug statuses/routes, and loop-protection markers.
- Validation: the complete structural validator and Bash syntax checks passed; all ten
  frontmatter blocks parsed as YAML with matching directory names; no trailing-space or
  unfinished-placeholder findings remained. Four negative fixtures correctly rejected
  a missing router, unexpected eleventh skill, broken router link, and missing BUG route.
  A scenario review covered explicit overrides, feature/bug ambiguity, explanation-only
  NORMAL requests, attachment pass-through, and follow-up isolation. The bundled
  `quick_validate.py` could not run because its environment lacks PyYAML; equivalent
  frontmatter/name/description/placeholder checks passed through the dependency-free
  workspace validator plus Ruby's YAML parser.
- Limits: task-router is workspace-routed through `AGENTS.md`; because `skills/` is a
  custom directory, native client discovery still depends on opening this workspace or
  explicitly supplying the root instructions.

## 2026-09-22 — Walk It Down cost and context policy

- Added the L0-L5 context ladder and decision-based stopping rules to orchestration.
- Set task-requirements to L1 by default and moved deep investigation to the validator.
- Added progressive validator investigation, implementation context reuse, minimal
  changes, V0-V6 verification escalation, and compact handoff rules.
- Added read-only changed-file/test-candidate helpers and a manifest wrapper that
  runs only an explicitly supplied command without shell evaluation.
- Updated templates/example to record context and verification escalation.
- Model walk-down remains an optional calibrated client choice; the workflow does
  not switch models or trade correctness for a fixed token budget.
- Validation: all skill frontmatter parsed as YAML; all four Bash scripts passed
  syntax and structural validation. Helper behavior passed on the Ops worktree and
  an isolated Git fixture containing modified, untracked, and changed-test files,
  including a repository path with spaces. Explicit command success/failure and an
  invalid base ref propagated the expected status. Negative fixtures confirmed the
  validator rejects a missing cost policy, missing investigation strategy, and a
  syntactically broken helper.
- Limits: related-test discovery is deliberately name-based and requires verifier
  judgment for import-only/shared-impact tests. Real-task cost comparisons and model
  calibration remain unmeasured.

## 2026-09-22 — Initial workflow

- Added four single-responsibility skills and explicit artifact templates.
- Added workspace routing with READY/PASS gates, clarification handling, and a
  limit of three failed verification cycles, counting the initial FAIL.
- Kept artifacts in the conversation and tied reports to contract revisions.
- Added structural validation and a fictional worked example of failure and repair.
- Documented custom-directory discovery and workspace versioning limitations.
- Validation: Bash syntax, structural validator, and independent YAML parsing passed.
  A relocated copy with a space in its path also passed. Eight broken fixtures
  correctly failed: name mismatch, blank description, missing skill heading, broken
  link, missing template, removed loop limit, excessive lines, and missing report
  heading. Invalid-root and excess-argument cases returned usage errors.
- Limits: semantic workflow reviewed against the worked example; repeated real-task
  calibration, native client discovery, and cross-model evaluation have not been run.

## Feedback record format

When an authorized maintenance change addresses a recurring weakness, append:

- Date / affected skill:
- Observed task/scenario and evidence (redacted):
- Failure or recurring friction:
- Cause in the current instructions:
- Instruction/template/check change:
- Validation and repeated scenario results:
- Remaining limits / next evaluation:

Do not describe a proposed adjustment as a proven improvement. Avoid credentials,
private payloads, and unneeded customer information in feedback records.
