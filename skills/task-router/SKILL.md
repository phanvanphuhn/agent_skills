---
name: task-router
description: "Classifies each new top-level request as FEATURE, BUG, or NORMAL and routes it once. Use automatically before selecting a structured development workflow."
---

# Task router

## Responsibility

CLASSIFY → ROUTE → STOP. Use user intent and immediately available context only.

## Classification

- FEATURE — meaningful new or intentionally changed product/application behavior that
  needs requirements analysis. Route the untouched input and attachments to
  [task-requirements](../feature-workflow/task-requirements/SKILL.md), then stop.
- BUG — expected existing behavior is broken, incorrect, regressed, crashing, or
  failing and the user wants investigation or a fix. Route the untouched input and
  attachments to [bug-analysis](../bug-workflow/bug-analysis/SKILL.md), then stop.
- NORMAL — explanation, review, documentation, formatting, Git/shell help, research,
  discussion, planning, simple refactor/configuration, or other work needing neither
  structured workflow. Continue with normal Codex behavior, then stop routing.

Explicit user intent wins. Asking to explain a bug or story is NORMAL; asking to fix
the bug is BUG; asking to implement the story is FEATURE. When signals conflict, use:
explicit intent → restore existing behavior → introduce/change behavior → NORMAL.

## Cost boundary

Prefer zero tools, repository reads, and attachment reads. Do not analyze requirements,
debug, inspect code, plan implementation, write tests, or process attachments deeply.
Use filenames/metadata only if the prompt itself is insufficient. Run once per new
top-level task; an active downstream workflow owns follow-ups.

## Output

Emit exactly one of:

```text
ROUTE: FEATURE
CONFIDENCE: HIGH
```

```text
ROUTE: BUG
CONFIDENCE: HIGH
```

```text
ROUTE: NORMAL
CONFIDENCE: HIGH
```

If the distinction genuinely changes the workflow and cannot be inferred, emit only:

```text
ROUTE: UNCLEAR
CONFIDENCE: LOW
QUESTION: Should this behavior already work and is broken, or is it new behavior?
```
