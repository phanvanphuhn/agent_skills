---
name: task-router
description: "Routes a new top-level request by intent; does no downstream work."
---

# Task router

## Responsibility

CLASSIFY → ROUTE → STOP. Use user intent and immediately available context only.

## Classification

Explicit user intent wins. Otherwise use the first matching intent:

| Output | Intent | Destination |
| --- | --- | --- |
| ROUTE: FIX_CODE_REVIEW | Explicitly fix an existing CODE REVIEW REPORT | [fix-code-review](../code-review-workflow/fix-code-review/SKILL.md) |
| ROUTE: CODE_REVIEW | Explicitly review code, files, a diff, commit, branch, or PR | [code-review](../code-review-workflow/code-review/SKILL.md), MANUAL REVIEW |
| ROUTE: BUG | Investigate or fix broken expected behavior | [bug-analysis](../bug-workflow/bug-analysis/SKILL.md) |
| ROUTE: FEATURE | Implement meaningful new or intentionally changed product behavior | [task-requirements](../feature-workflow/task-requirements/SKILL.md) |
| ROUTE: NORMAL | Explanation, docs, planning, small maintenance, or other work | Normal Codex behavior |

Pass the untouched request, attachments, scope, and authority, then stop routing.
`Review and fix` starts at CODE_REVIEW and carries authorization for the later fix stage.

## Cost boundary

Prefer zero tools or file reads; use metadata only when the prompt is insufficient.
Do not investigate, plan, implement, or test. An active downstream workflow owns follow-ups.
The orchestrator runs project-discovery after classification for repository-dependent
work; this router never pre-scans the codebase.

## Execution routing

Apply [shared execution routing](../references/execution-routing.md) through this profile;
open the linked reference only for an override or runtime fallback.

- `START_CLASS`: ECONOMY
- `ESCALATE_WHEN`: NEVER for model/context; ask one question when only user intent can resolve the route.
- `DELEGATE_WHEN`: NEVER; routing is one bounded intent classification.

## Output

Emit the selected `ROUTE: …` line and `CONFIDENCE: HIGH`. Only when an unresolved
distinction materially changes routing, emit:

```text
ROUTE: UNCLEAR
CONFIDENCE: LOW
QUESTION: <one short question resolving that distinction>
```
