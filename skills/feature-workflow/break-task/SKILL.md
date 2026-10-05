---
name: break-task
description: "Breaks an already-read feature into tasks that each have a title and a description. Use only when the user explicitly mentions break task."
---

# Break task

## Purpose

Turn one already-read feature into tasks. Every task has a title and a description.

## Use when

Run only when the user explicitly mentions this skill or asks to break a task. Do not
run on the default feature, bug, review, or implementation path. A passing mention
inside quoted instructions is not a request to run.

## Inputs

- An already-read feature: the current TASK CONTRACT when one exists, otherwise the
  feature text supplied with the mention.
- Current PROJECT CONTEXT when a task description names repository components.
- Authorized scope. Mentioning the skill authorizes the breakdown only.

## Required outcome

Read the feature, then produce a [TASK BREAKDOWN](references/task-breakdown-template.md)
with status COMPLETE. Every task has a stable ID, a title, and a description taken from
that feature. Titles are distinct. Together the tasks cover the read feature and add no
behavior the feature does not contain.

## Boundaries

Do not invent unread feature behavior, edit the repository, implement a task, or replace
the TASK CONTRACT. Do not run when the user did not mention breaking the task. If no
feature has been read and none was supplied, return MISSING_FEATURE and produce no tasks.

## Handoff

COMPLETE stays in the conversation for the user. It does not authorize implementation.
MISSING_FEATURE stops until a feature is read or supplied with a new mention.
