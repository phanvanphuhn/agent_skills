---
name: task-router
description: "Routes a new top-level request to the applicable development workflow and performs no downstream work."
---

# Task router

## Purpose

Select one route from the user's intent, pass the untouched request and authority to
that route, and stop.

## Walk It Down

- Start: Use the user's stated intent and explicit routing.
- Expand: Check only immediately available request metadata when the route is materially ambiguous.
- Stop: Emit one confident route, or one clarification question when the route remains unclear.

## Routes

| Route | Use when | Destination |
| --- | --- | --- |
| `FIX_CODE_REVIEW` | Explicitly fix an existing CODE REVIEW REPORT | [fix-code-review](../code-review-workflow/fix-code-review/SKILL.md) |
| `CODE_REVIEW` | Explicitly review code, files, a diff, commit, branch, or PR | [code-review](../code-review-workflow/code-review/SKILL.md) |
| `BUG` | Investigate or fix behavior that should already work | [bug-analysis](../bug-workflow/bug-analysis/SKILL.md) |
| `FEATURE` | Introduce or intentionally change product behavior | [task-requirements](../feature-workflow/task-requirements/SKILL.md) |
| `NORMAL` | Explanation, documentation, planning, maintenance, or other work | Normal Codex behavior |

Explicit user routing wins. `Review and fix` starts with `CODE_REVIEW` and carries
authorization for the later fix stage. Follow-up messages stay with an active workflow.

## Output

```text
ROUTE: <FEATURE | BUG | CODE_REVIEW | FIX_CODE_REVIEW | NORMAL>
CONFIDENCE: HIGH
```

When user intent cannot be resolved without changing the workflow, output one short
question with `ROUTE: UNCLEAR` and `CONFIDENCE: LOW`.

## Boundaries

Do not inspect the repository, investigate, plan, implement, review, or test. Routing
does not grant additional authority.
