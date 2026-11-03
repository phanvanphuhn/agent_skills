---
name: comment
description: "Adds only necessary why-comments and removes redundant what-comments in a user-named file, symbol, or diff. Use only when the user explicitly asks to add, revise, or clean up code comments, or invokes /comment; not for feature, bug, or review work."
---

# Comment

## Purpose

Keep the codebase clean, readable, and maintainable by adding comments only when they
are genuinely necessary, such as for complex functions, non-obvious logic, or important
implementation decisions. Comments must explain **why** something is done rather than
simply describing **what** the code does.

## Use when

Run only when the user explicitly invokes `/comment`, or asks to add, revise, or clean
up code comments in a named scope. Do not run on the default feature, bug, review, or
implementation path. A passing mention inside quoted instructions is not a request to run.

## Inputs

- Named files, symbols, or diff the user authorized for commenting.
- Current source in that scope, including existing comments and identifiers.
- Project comment or documentation conventions when they are evident in the repository.
- Current PROJECT CONTEXT when locating the scoped files requires it.

## Walk It Down

- Start: Confirm a named authorized file, symbol, or diff scope; if none was named, ask once and do not edit. Otherwise read that scope and list candidates that are complex, non-obvious, or encode an important decision.
- Expand: Inspect surrounding code only when needed to decide whether a comment is necessary or redundant.
- Stop: Stop when necessary why-comments are in place and redundant what-comments are absent from the scope, or when scope is still unconfirmed.

## Required outcome

If the user did not name an authorized file, symbol, or diff scope, ask once for that
scope and leave the repository unchanged until it is confirmed.

Otherwise edit the authorized scope so that:

- comments appear only for complex functions, non-obvious logic, or important
  implementation decisions;
- each comment explains why the code exists or behaves that way;
- self-explanatory code has no redundant narration of variables, functions, or steps;
- existing comments that only restate the code are removed or rewritten into why form.

Return a short summary of comments added, rewritten, kept, or removed, with file paths.
If no comment was necessary, say so and leave the code unchanged.

Use [comment examples](references/comment-examples.md) when a borderline case needs a
concrete good versus bad pattern.

## Boundaries

Do not edit when the authorized scope is unnamed or unconfirmed. Do not invent a
workspace-wide scope. Do not change runtime behavior, public APIs, tests, or formatting
beyond the comments themselves. Do not comment every variable or function. Do not invent
business reasons the code does not support. Do not broaden past the authorized scope or
overwrite unrelated local edits. Prefer leaving clear, self-explanatory code uncommented.

## Handoff

Return the summary to the user. This skill does not authorize feature or bug work and
does not declare a task complete.
