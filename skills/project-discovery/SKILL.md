---
name: project-discovery
description: "Builds a reusable evidence-based map of an arbitrary repository or workspace before repository-dependent work begins."
---

# Project discovery

## Responsibility

Act as a senior engineer onboarding to an unfamiliar codebase. Establish the smallest
reliable architectural baseline needed by later work and publish it as PROJECT CONTEXT.
Discover what the repository actually contains instead of assuming a language,
framework, layout, command, or deployment model.

## Trigger

Run after task-router selects a repository-dependent route and before that route's
specialized work. Run when no PROJECT CONTEXT exists, when the target repository or
workspace changes, or when instructions, manifests, baseline, entry points, or
architecture-relevant files make the current context stale.

Repository-dependent NORMAL requests also use discovery when their answer or action
depends on source, configuration, tests, history, or project architecture.

## When not to run

Do not run before intent routing, for generic conversation unrelated to a repository,
or when a current PROJECT CONTEXT already covers the target and task. Do not read every
file, traverse generated/vendor/build output, expose secrets, install dependencies,
execute application behavior, or modify the repository merely to understand it.

## Inputs

- Selected route and user-authorized scope.
- Candidate repository/workspace path and applicable parent/runtime instructions.
- Existing PROJECT CONTEXT, if any, plus current baseline/worktree metadata.
- Explicitly supplied documentation, architecture material, or task-relevant files.

## Investigation strategy — Walk It Down

Use progressive discovery and stop when the next stage has a trustworthy map:

1. P0 — Resolve workspace/repository boundaries, Git roots, worktree state, and all
   applicable instruction files without opening unrelated source.
2. P1 — Inspect the shallow tree, README/index documentation, manifests, lockfiles,
   build files, workspace configuration, and test/static-analysis configuration.
3. P2 — Locate and read entry points plus a small representative set of source files
   that establish module responsibilities, interfaces, and control/data flow.
4. P3 — Follow direct dependencies across a boundary only when needed to explain a
   material architectural relationship or the selected task's likely component.
5. P4 — Explore broader architecture only when P0-P3 cannot answer a named question
   that would otherwise block safe downstream work.

Search and list before reading. Prefer repository metadata and direct source evidence
over filenames alone. Record the highest level and the question that justified P3/P4.

## Procedure

1. Resolve the exact target. Detect a single repository, nested repositories, a
   monorepo, or a parent workspace; identify which boundaries are relevant to the route.
2. Read applicable instruction files from broadest to most specific. Inspect worktree
   status without changing it and distinguish user changes from the discovery baseline.
3. At P1, identify languages, frameworks, package/workspace managers, build/test/lint/
   typecheck tools, infrastructure definitions, and likely generated or vendored areas.
4. At P2, read entry points and representative implementation files. Map major modules,
   ownership boundaries, public interfaces, dependency direction, runtime/control flow,
   and data/storage/external-service boundaries only where evidence supports them.
5. Discover commands from repository configuration or documentation. Label commands
   as observed/proposed; do not claim they pass unless a later authorized stage runs them.
6. Relate the selected route to likely components while keeping task-specific analysis
   in its owning feature, bug, review, or NORMAL stage.
7. Compare any previous PROJECT CONTEXT with repository identity, instructions,
   manifests, baseline, and architecture-relevant changes. Reuse unchanged evidence and
   increment the revision only for a material context change.
8. Emit the complete [PROJECT CONTEXT template](references/project-context-template.md).

## Outputs

A concise PROJECT CONTEXT with status CURRENT, PARTIAL, or BLOCKED. It identifies the
target and freshness evidence, governing instructions, stack, repository topology,
entry points, module boundaries, important flows, commands, risks, and unknowns.

PARTIAL may proceed only when its missing information is immaterial to the selected
route. BLOCKED stops downstream repository work and names the owner/action needed.

## Completion criteria

The target boundary is explicit; applicable instructions and worktree state are known;
architecture claims cite inspected evidence; the next stage can locate relevant code
and commands without repeating general onboarding; unknowns and freshness conditions
are visible; and no broad scan was performed without a named reason.

## Failure and blocked behavior

Never infer a technology or architecture from directory names alone. If the repository,
required source, instructions, or manifest cannot be accessed, return PARTIAL when the
gap is irrelevant or BLOCKED when it prevents the selected route. Preserve all local
changes and report unreadable, generated, external, or intentionally excluded areas.

## Human intervention

Ask only for a target selection, missing access, or unavailable architecture artifact
that cannot be resolved locally and materially blocks the selected route. Do not ask
the user to explain structure that repository evidence can establish safely.
