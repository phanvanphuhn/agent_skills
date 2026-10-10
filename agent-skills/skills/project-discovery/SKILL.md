---
name: project-discovery
description: "Creates or refreshes a visual, evidence-backed map of repository structure, architecture, workflows, and commands for repository-dependent work."
---

# Project discovery

## Purpose

Provide the active workflow with enough repository context to locate relevant source,
interfaces, and commands without assuming a language or architecture.

## Use when

Run before repository-dependent work when no current PROJECT CONTEXT covers the target.
Refresh an existing context only when relevant repository boundaries, instructions,
manifests, interfaces, architecture, or dirty files changed. Skip pure conversation.

## Inputs

- Selected route and authorized scope.
- Target workspace/repository, applicable instructions, and writable package location.
- Relevant manifests, entry points, source, tests, and prior PROJECT CONTEXT if present.
- Current Git/worktree state where available.

## Walk It Down

- Start: Resolve repository boundaries, applicable instructions, worktree state, and any saved context in `../../project-contexts/`.
- Expand: Inspect structure, manifests, entry points, representative source, then direct dependencies only for a named context gap.
- Stop: Stop when the active route has enough evidence, or report the exact immaterial gap or blocker.

## Required outcome

Produce the [PROJECT CONTEXT](references/project-context-template.md) with status
CURRENT, PARTIAL, or BLOCKED. It must identify the target boundary, governing
instructions, technology/tooling, task-relevant structure and flows, entry points,
available commands, risks, unknowns, and the next stage. Include high-level architecture,
important control and data flows, project notes, and known edge cases when supported by
repository evidence. Present the relevant folder layout as a compact tree. Use Mermaid
diagrams for component relationships and important workflows when they make boundaries,
direction, or sequence easier to see; use a small table or concise text for simpler
cases. Put source paths next to each visual, keep labels readable, and explain only
non-obvious relationships. Mark unverified details as unknown rather than drawing
speculative nodes or arrows. On refresh, reuse an unchanged visual by citing its prior
revision instead of redrawing it.

Save one Markdown snapshot per target repository in
[`../../project-contexts/`](../../project-contexts/README.md), using a stable,
distinct filename. On refresh, update that file in place, increment its revision only
for material context changes, and preserve relevant notes. Include the saved path in
the handoff. Keep other workflow reports in the conversation unless requested as files.

## Boundaries

Discovery may write only its PROJECT CONTEXT Markdown file. It must not change target
source or configuration. Do not install dependencies, run the application, inspect
secrets, or scan generated/vendor/build output unless the task explicitly requires it.
Do not claim architecture, flows, edge cases, or commands without repository evidence.
Do not infer dependencies from folder proximity or imply that a diagram proves runtime
behavior. Keep diagrams valid Markdown/Mermaid and provide a short text fallback when
the chosen renderer may not display Mermaid.
If the package location is unavailable or unwritable, emit the context in the
conversation and identify the persistence gap; do not write to another location.

## Handoff

CURRENT proceeds to the selected route. PARTIAL may proceed only when its missing facts
do not affect that work. BLOCKED names the owner, required action, and resume condition.
