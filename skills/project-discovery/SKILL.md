---
name: project-discovery
description: "Creates or refreshes a reusable map of the repository boundaries, architecture, entry points, and commands needed by a repository-dependent task."
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
- Target workspace/repository and applicable instructions.
- Relevant manifests, entry points, source, tests, and prior PROJECT CONTEXT if present.
- Current Git/worktree state where available.

## Required outcome

Produce the [PROJECT CONTEXT](references/project-context-template.md) with status
CURRENT, PARTIAL, or BLOCKED. It must identify the target boundary, governing
instructions, technology/tooling, task-relevant structure and flows, entry points,
available commands, risks, unknowns, and the next stage.

## Boundaries

Discovery is read-only. Do not install dependencies, run the application, inspect
secrets, or scan generated/vendor/build output unless the task explicitly requires it.
Do not claim architecture or commands without repository evidence.

## Handoff

CURRENT proceeds to the selected route. PARTIAL may proceed only when its missing facts
do not affect that work. BLOCKED names the owner, required action, and resume condition.
