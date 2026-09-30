# Skill-system changelog

## 2026-09-30 — Dynamic agent and model walk-down

- Added a shared execution-routing policy that separates context depth, agent topology,
  model capability, and reasoning effort instead of pinning an entire workflow to one model.
- Added ECONOMY, STANDARD, and DEEP profiles with explicit escalation, de-escalation,
  delegation-value, runtime-fallback, and single-write-owner rules.
- Added a concise execution profile to all thirteen skills and made the validator require
  the profile and shared-policy link for every current or future `SKILL.md`.
- Added three isolation-ready routing probes for cheap single-agent work, high-risk deep
  reasoning, and worthwhile low-cost parallel delegation.
- Replaced prose-only stage profiles with validator-enforced `START_CLASS`,
  `ESCALATE_WHEN`, and `DELEGATE_WHEN` fields; empty or placeholder profiles now fail.
- Added a highest-applicable-minimum decision table so security/data risks, unresolved
  concurrency, cross-system contradictions, and repeated failed reasoning route consistently.
- Ran the corrected E6 routing matrix across Luna, Sol, and Astra: 8/9 decision PASS.
  Recorded the Luna DEEP failure, unknown token/per-run latency telemetry, shared-workspace
  isolation limitation, batch times, packet hashes, and excluded stale-fixture runs.
- Kept routine defaults artifact-free; an EXECUTION ROUTE is recorded only for delegation,
  a profile override, or an audit requirement, reducing repeated coordination tokens.

## 2026-09-30 — Persistent review blockers and auditable evaluation packets

- Added stable BLK-* identities and OPEN/EVIDENCE_SUPPLIED/RESOLVED lifecycle rules.
  Fix reports must carry every unresolved blocker; only code-review may confirm closure.
- Added a fix-code-review scenario proving that an unrelated open review gap survives
  a completed correction without incorrectly blocking READY_FOR_RE_REVIEW.
- Expanded behavioral evaluation to five base cases and five controls, including
  successful evidence reuse and APPROVED review paths so always-blocking behavior fails.
- Added a standard-library packet builder that allowlists the selected stage inputs,
  rejects fixture drift and symlinked inputs, and emits content hashes. Packet filtering
  does not enforce runtime isolation; results record ENFORCED, ISOLATION_UNVERIFIED,
  or CONTAMINATED separately from the decision result.
- Added six deterministic builder regression tests covering the then-current ten packets, variants,
  forbidden-file exclusion, invalid IDs, symlinks, hashes, and stdout/stderr separation.

## 2026-09-30 — Review precedence and behavioral decision cases

- Confirmed blocking findings now take precedence over missing review evidence:
  count the issued report once, returning CHANGES_REQUIRED or REVIEW_ESCALATION.
  With no confirmed blocking findings, required gaps yield BLOCKED; only sufficient
  evidence permits APPROVED. Counter history and unrelated verification counters persist.
- Review reports retain coverage gaps separately, with scope, owner, action, and resume
  condition. Correcting known findings does not erase unresolved review blockers.
- Added four isolated candidate packets and three control variants for evidence reuse,
  mixed findings/blockers, authorization, and context recovery. Evaluator expectations
  stay separate from candidate inputs; results require captured responses, not keyword checks.
- The evaluation set is opt-in and decision-level: it neither launches agents nor calls
  paid APIs. Structural success or a same-agent walkthrough is not an independent
  behavioral pass, an end-to-end run, or evidence of token savings.

## 2026-09-30 — Lean entrypoints and bounded agent inputs

- Removed repeated instructions from routing, discovery, and review while retaining
  their scope, evidence requirements, approval boundaries, and cycle limits.
- Input reports no longer imply loading their producers' skills/templates or recursively
  expanding artifact history. Required contracts and raw evidence remain accessible.
- Parallel work assigns one owner per write scope/check and shares results before review.
- The three edited entrypoints decreased from 2,458 to 1,493 words (39%); including
  the shared root policy, 4,094 to 3,176 words (22%). These are instruction-size
  measurements against the pre-edit working tree, not measured token or billing savings.
- Structural validation and whitespace checks passed; added a focused calibration case
  for consuming upstream artifacts without loading upstream skills.

## 2026-09-30 — Review consistency and reusable check evidence

- Review now covers later test, fixture, snapshot, and behavior-affecting configuration
  changes, including edits or generated changes during verification. Certification
  waits for approval of the final baseline; pending review alone consumes no failure cycle.
- Unified review_cycles: the initial blocking review counts as one; counts 1–2 request
  changes and count 3 escalates. Approval, blockers, and fixes retain the count.
- Added one shared check-evidence format referenced by seven producer templates,
  covering input identity, environment, execution provenance, outcomes, and safe reuse.
- Verification reuses approved engineering findings and focuses on behavior/coverage;
  new changes or contradictory evidence trigger targeted re-review.
- Added calibration cases and compact usage measurements; real token savings remain
  unmeasured until representative tasks provide client usage data.

## 2026-09-30 — Token-conscious context and handoffs

- Condensed the root instructions while preserving routing, authority, review,
  verification, evidence, and retry limits.
- Load stage skills/templates only when needed; defer failure templates and examples.
  Reuse instructions already in context and pass bounded context when delegation is authorized.
- Refresh project context by affected source facts, including dirty/untracked state;
  avoid rescanning solely because a commit changed. Allow narrow task-scoped discovery.
- Group empty optional report sections; promote an accessible unchanged contract to
  READY by reference. Changed requirements still require a complete finalized contract.
- Reuse executed checks only with matching inputs, environment, baseline, and observable
  results; preserve independent code review and mandatory checks.
- Clarified that explicit manual review can inspect existing files without a diff.
- Instruction word counts are size measurements; real token/cost savings need task-level measurement.

## 2026-09-29 — Generic project discovery baseline

- Removed application-specific repository names, machine paths, and workspace-layout
  assumptions from active orchestration and usage guidance.
- Added `project-discovery`, a project-agnostic onboarding stage that runs after cheap
  intent routing and before repository-dependent feature, bug, review, or NORMAL work.
- Added the versioned PROJECT CONTEXT artifact covering repository boundaries,
  instructions, worktree baseline, technology, tooling, entry points, module
  responsibilities, dependency/runtime/data flows, commands, risks, and unknowns.
- Added P0-P4 progressive discovery, representative source inspection, explicit
  exclusions for generated/vendor/build areas, freshness checks, and reuse rules so
  later stages do not repeat general codebase exploration.
- Updated all downstream skills and report templates to consume and identify the
  PROJECT CONTEXT revision used for their repository evidence.
- Updated the feature and bug examples to demonstrate project discovery before their
  existing pipelines.
- Extended structural validation for the thirteenth skill, its template, required
  orchestration/freshness markers, downstream context references, and rejection of
  application-specific names or absolute user-home paths in active generic guidance.
- Fixed related-test discovery so repositories with zero conventionally named tests
  produce an empty candidate list instead of stopping the verification wrapper; real
  ripgrep errors still propagate.

## 2026-09-29 — Split code review from review fixes

- Replaced the bundled review-and-fix behavior with two single-responsibility skills
  under `code-review-workflow/`: read-only `code-review` and explicit-only
  `fix-code-review`.
- Standardized CODE REVIEW REPORT issues on HIGH, MEDIUM, and LOW severity. HIGH and
  MEDIUM findings return CHANGES_REQUIRED; LOW findings remain non-blocking unless a
  repository rule or concrete completion risk requires otherwise.
- Made CHANGES_REQUIRED a stop condition. Only an explicit user fix request, invocation
  of fix-code-review, or an original combined `review and fix` request authorizes the
  separate correction stage after the initial report exists.
- Added the FIX CODE REVIEW REPORT contract with issue dispositions, bounded changes,
  self-test evidence, exact post-fix baseline, and mandatory return to code-review.
  The fix skill cannot approve changes or route directly to verification.
- Updated task routing, workspace orchestration, examples, README, and structural
  validation for twelve skills and the read-only review boundary.
- Validation: dependency-free structural validation and Bash syntax checks passed;
  all twelve restricted frontmatter blocks, templates, links, paths, line limits,
  routing states, stop conditions, and review-cycle markers were checked.

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
