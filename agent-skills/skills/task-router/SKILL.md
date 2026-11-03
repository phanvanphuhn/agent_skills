---
name: task-router
description: "Picks the development workflow for a new software request when the right path is unclear: build or change a feature, fix something broken, review code, fix review findings, save a handoff, or add code comments. Emits one route, then starts that workflow's first stage."
---

# Task router

## Purpose

Select one route from the user's intent, then continue into that route's entry skill in
the same turn, passing the untouched request and authority. Hosts that do not load a
workspace instruction file rely on this skill, or on each entry skill's own
description, to start the correct workflow.

## Walk It Down

- Start: Use the user's stated intent and explicit routing.
- Expand: Check only immediately available request metadata when the route is materially ambiguous.
- Stop: Emit one confident route and hand control to its entry skill, or ask one clarification question when the route remains unclear.

## Routes

| Route | Use when | Destination |
| --- | --- | --- |
| `FIX_CODE_REVIEW` | Explicitly fix an existing CODE REVIEW REPORT | [fix-code-review](../code-review-workflow/fix-code-review/SKILL.md) |
| `CODE_REVIEW` | Explicitly review code, files, a diff, commit, branch, or PR | [code-review](../code-review-workflow/code-review/SKILL.md) |
| `HANDOFF` | User explicitly invokes `/handoff` or asks to create a handoff | [handoff](../handoff/SKILL.md) |
| `COMMENT` | User explicitly invokes `/comment` or asks to comment a named scope | [comment](../comment/SKILL.md) |
| `BUG` | Investigate or fix behavior that should already work | [bug-analysis](../bug-workflow/bug-analysis/SKILL.md) |
| `FEATURE` | Introduce or intentionally change product behavior | [task-requirements](../feature-workflow/task-requirements/SKILL.md) |
| `NORMAL` | Explanation, documentation, planning, maintenance, or other work | Normal assistant behavior |

Explicit user routing wins. Mentioning handoff or comment selects that route and does
not insert it into the default feature or bug path. `Review and fix` starts with
`CODE_REVIEW` and carries authorization for the later fix stage. Follow-up messages
stay with an active workflow. Repository-dependent FEATURE and BUG work passes through
[project-discovery](../project-discovery/SKILL.md) first when no current PROJECT
CONTEXT covers the target.

## Output

```text
ROUTE: <FEATURE | BUG | CODE_REVIEW | FIX_CODE_REVIEW | HANDOFF | COMMENT | NORMAL>
CONFIDENCE: HIGH
```

Then load the destination skill and produce its outcome under that skill's own
contract. When the user asks only which route applies, stop after the route lines.
When user intent cannot be resolved without changing the workflow, output one short
question with `ROUTE: UNCLEAR` and `CONFIDENCE: LOW` and do not start a workflow.

## Boundaries

The routing step itself does not inspect the repository, investigate, plan, implement,
review, or test; the destination skill's boundaries govern everything after the route.
Routing does not grant additional authority: a read-only request stays read-only.
