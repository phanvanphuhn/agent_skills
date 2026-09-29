---
name: task-router
description: "Classifies each new top-level request as FEATURE, BUG, CODE_REVIEW, FIX_CODE_REVIEW, or NORMAL and routes it once before downstream work."
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
- CODE_REVIEW — the user explicitly asks to review a file, diff, staged changes,
  commit, branch, PR, or supplied code. Route the untouched request and scope to
  [code-review](../code-review-workflow/code-review/SKILL.md) in MANUAL REVIEW mode,
  then stop.
- FIX_CODE_REVIEW — the user explicitly asks to fix issues from an existing CODE
  REVIEW REPORT. Route the request, report, and authorization to
  [fix-code-review](../code-review-workflow/fix-code-review/SKILL.md), then stop.
- NORMAL — explanation, documentation, formatting, Git/shell help, research,
  discussion, planning, simple refactor/configuration, or other work needing no
  specialized workflow. Continue with normal Codex behavior, then stop routing.

Explicit user intent wins. Asking to explain code is NORMAL; asking to review it is
CODE_REVIEW; asking to fix an existing review report is FIX_CODE_REVIEW; asking to fix
broken behavior without that report is BUG; asking to implement new behavior is FEATURE.
`Review and fix` starts at CODE_REVIEW and carries explicit authorization for the later
fix stage. When signals conflict, use: review-report fix → review → restore behavior →
introduce/change behavior → NORMAL.

## Cost boundary

Prefer zero tools, repository reads, and attachment reads. Do not analyze requirements,
debug, inspect code, plan implementation, write tests, or process attachments deeply.
Use filenames/metadata only if the prompt itself is insufficient. Run once per new
top-level task; an active downstream workflow owns follow-ups.

The orchestrator, not this router, runs project-discovery after classification for a
repository-dependent route. The router must not pre-scan the codebase because the
selected intent and target are inputs to bounded discovery.

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
ROUTE: CODE_REVIEW
CONFIDENCE: HIGH
```

```text
ROUTE: FIX_CODE_REVIEW
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
