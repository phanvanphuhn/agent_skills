---
name: project-discovery
description: "Builds a reusable evidence-based map of an arbitrary repository or workspace before repository-dependent work begins."
---

# Project discovery

## Responsibility

Build the smallest evidence-backed PROJECT CONTEXT needed for the selected task.
Discover actual boundaries, architecture, and commands without assuming a stack.

## Trigger

After routing, run before repository-dependent work, including NORMAL, when context
is missing, insufficient, or stale. Target, instruction, manifest, entry-point, or
architecture changes may require refresh; a different commit alone does not.

## When not to run

Skip pure conversation and reuse current context covering the target/task. Discovery
is read-only: no installs, application execution, secrets, or generated/vendor/build scans.

## Inputs

- Route, authorized scope, target path, and applicable parent/runtime instructions.
- Prior PROJECT CONTEXT, current baseline/worktree metadata, and supplied relevant files.

## Investigation strategy — Walk It Down

Search/list before reading; stop once the next stage has sufficient evidence.

- P0 — Repository/workspace boundaries, Git roots, worktree state, applicable instructions.
- P1 — Task-relevant shallow structure, docs, manifests, lockfiles, tooling/configuration.
- P2 — Entry points and representative source establishing modules, interfaces, dependencies,
  and control/data/storage/external-service flows.
- P3 — Direct dependencies needed to resolve a material boundary/task question.
- P4 — Broader architecture only for a blocking question unresolved by P0-P3.

Narrow maintenance, explanation, or review may stop at P0/P1 plus relevant source;
mark unrelated fields out of scope. A first project-wide overview or cross-cutting
change requires P2. Record depth and the question justifying P3/P4.

## Procedure

1. Resolve the target and read applicable instructions broadest to most specific;
   reuse unchanged instructions already in context. Preserve local changes.
2. Before expanding, compare prior source paths with tracked, dirty, and untracked
   changes. Refresh only affected facts/dependencies; unknown freshness requires the
   minimum inspection to establish it. Do not repeat unchanged onboarding.
3. Follow P0-P4 for missing facts. Source commands from configuration/docs and mark
   them discovered, not passed. Leave task-specific investigation to its owning stage.
4. When producing or refreshing context, use the
   [PROJECT CONTEXT template](references/project-context-template.md). Cite source paths
   and baseline/content fingerprints. Reuse a current revision by ID; refresh with changed
   facts plus its accessible prior revision, or a full snapshot if that revision is
   unavailable. Target roughly 250 words for routine context; expand when necessary.

## Outputs

PROJECT CONTEXT: CURRENT, PARTIAL, or BLOCKED, with task-relevant architecture,
evidence, instructions, commands, exclusions, risks, and next owner. PARTIAL permits
progress only when missing information is immaterial to the selected route.

## Completion criteria

The next stage can locate relevant code/commands without repeating onboarding;
boundaries, unknowns, freshness, and evidence supporting architecture claims are explicit.

## Failure and blocked behavior

Names alone do not establish architecture. Missing access/evidence is PARTIAL only
when immaterial; otherwise BLOCKED stops work with an owner, action, and resume condition.

## Human intervention

Ask only for material target/access/artifact gaps that local evidence cannot resolve.
