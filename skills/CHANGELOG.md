# Skill-system changelog

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
