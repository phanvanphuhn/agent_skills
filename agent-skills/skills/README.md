# Project integration workflow skills

This Claude Code plugin gives a reusable path through an unfamiliar software project. It
defines stage boundaries, required inputs and outputs, authorization rules, evidence
contracts, and handoffs. Every skill uses a lightweight Walk It Down contract while
avoiding fixed model classes, numeric context ladders, role-play, or implementation algorithms.

## Layout

```text
agent-skills/
├── AGENTS.md
├── project-contexts/README.md (saved PROJECT CONTEXT Markdown files)
├── handoffs/<taskID>-<description>/{HANDOFF.md,CHANGELOG.md}
├── .claude-plugin/{plugin.json,marketplace.json}
├── agents/fresh-reviewer.md (Claude Code subagent for the required review gate)
├── evals/<case>/{prompt.md,graders/} (Claude Code plugin evals)
└── skills/
    ├── task-router/SKILL.md
    ├── project-discovery/{SKILL.md,references/project-context-template.md}
    ├── handoff/{SKILL.md,references/}
    ├── comment/{SKILL.md,references/comment-examples.md}
    ├── feature-workflow/
    │   ├── task-requirements/{SKILL.md,references/task-contract-template.md}
    │   ├── requirement-validator/{SKILL.md,references/validation-report-template.md}
    │   ├── implementation/{SKILL.md,references/implementation-report-template.md}
    │   └── verification/{SKILL.md,references/,scripts/}
    ├── bug-workflow/
    │   ├── bug-analysis/{SKILL.md,references/bug-contract-template.md}
    │   ├── bug-reproduction/{SKILL.md,references/reproduction-report-template.md}
    │   ├── bug-root-cause/{SKILL.md,references/root-cause-report-template.md}
    │   ├── bug-fix/{SKILL.md,references/bug-fix-report-template.md}
    │   └── bug-verification/{SKILL.md,references/}
    ├── code-review-workflow/
    │   ├── code-review/{SKILL.md,references/code-review-report-template.md}
    │   └── fix-code-review/{SKILL.md,references/fix-code-review-report-template.md}
    ├── references/{check-evidence.md,state-storage.md}
    ├── evals/
    └── scripts/validate-skill-system.sh
```

## Invocation

The `agent-skills` directory is the whole plugin. Load it with
`claude --plugin-dir ./agent-skills`, or add it as a marketplace with
`claude plugin marketplace add ./agent-skills` and install
`agent-skills@agent-skills-local`. Do not copy its files into the host project's root.

Claude Code does not load `AGENTS.md`; each skill's description decides when it fires,
and `task-router` routes requests whose workflow is unclear before continuing into the
selected stage. Repository-dependent work receives a reusable PROJECT CONTEXT before
its selected stage runs.

Project discovery saves a reusable Markdown snapshot for each target repository, in
[`project-contexts/`](../project-contexts/README.md) when the package is vendored or in
the plugin data directory when it is installed, following the
[saved state location](references/state-storage.md) rule. The
snapshot records high-level architecture, important flows, project notes, edge cases,
evidence, and unknowns. It is refreshed only when relevant facts change; each target
gets a distinct filename. Discovery uses a compact folder tree and, where they clarify
the project, Mermaid component and workflow diagrams with source paths beside them.

Only when the user explicitly requests a handoff, `handoff` writes one
`handoffs/<taskID>-<description>/` folder per task under the same saved-state root,
containing `HANDOFF.md` and `CHANGELOG.md`. Task completion alone does not invoke the
skill. Its description limits it to explicit requests, which keeps natural-language
requests such as "create a handoff" working, and a negative eval checks it does not
fire on its own. It uses the supplied task ID or a stable local ID if none
was supplied. The handoff records inputs, outputs, Definition of Done and evidence,
implementation flow, exact baseline, and
fresh-session resume instructions. An explicit unfinished checkpoint remains labeled
CHECKPOINT with blockers. Fresh sessions compare the saved baseline with the current
worktree before relying on the summary.

Only when the user explicitly invokes `/comment`, or asks to comment a named scope,
`comment` adds or revises comments that explain why code exists. It skips redundant
narration of self-explanatory variables and functions. Its description and negative
evals keep it from firing on its own.

The manifest adds the three workflow folders to Claude Code's default `skills/` scan,
so every skill loads once. Structural validation proves that coverage; live loading
and triggering are measured with `claude plugin validate .` and `claude plugin eval .`.

## Workflow paths

```text
FEATURE
  TASK CONTRACT → VALIDATION → IMPLEMENTATION → CODE REVIEW → VERIFICATION → DONE

BUG
  BUG CONTRACT → REPRODUCTION → ROOT CAUSE → FIX → CODE REVIEW → VERIFICATION → DONE

MANUAL REVIEW
  CODE REVIEW → report only

AUTHORIZED REVIEW FIX
  FIX CODE REVIEW → CODE REVIEW → applicable verification

HANDOFF (explicit mention only)
  HANDOFF.md + CHANGELOG.md

COMMENT (explicit mention only, named scope required)
  necessary why-comments in the authorized scope
```

The files define contracts between these stages. The model remains responsible for
choosing suitable repository inspection, engineering, debugging, and testing methods.
The required code-review gate can APPROVE only from a fresh reviewer context separate
from implementation; when that context is unavailable, it records a blocker instead of
claiming independent approval and gives a copy-ready handoff to a separate reviewer.
The [independent review packet guide](code-review-workflow/code-review/references/independent-review.md)
describes the evidence to carry and one fresh local CLI launch pattern.
The handoff references the exact baseline and accessible artifacts without copying the
implementation conversation. Manual reviews can disclose same-context limitations.
If a feature ticket or acceptance criterion cannot be implemented safely, validation
stops and puts specific, forwardable questions for the PM/PO, SM, or actual technical
owner at the top of the response. Each question identifies the decision or evidence
needed and the criterion it unblocks.

## Skill contract

Each `SKILL.md` contains:

- a discriminating name and trigger description;
- the stage purpose and when it applies;
- required inputs;
- a stage-specific `Walk It Down` section with `Start`, `Expand`, and `Stop`;
- the required observable output;
- boundaries that protect scope, evidence, authorization, and safety; and
- the next-stage handoff.

Detailed output schemas live in linked templates. Deterministic scripts are used only
for repeatable mechanical operations such as changed-file discovery and structural
validation.

Walk It Down starts with the smallest relevant evidence set, expands only for a named
unresolved question, and stops once the stage can produce its required outcome. The
stage sections define evidence boundaries, not a hidden reasoning transcript or fixed
number of investigation steps.

## Artifact contract

PROJECT CONTEXT is saved as Markdown in `project-contexts/`; completed-task handoffs
are saved in `handoffs/`. Other artifacts are Markdown in the active conversation
unless the user requests files.
They identify the target, input revisions, status, exact baseline, evidence, unresolved
items, counters, and next owner. Requirements and bug evidence retain their source
provenance. Reports cite actual code and executed checks rather than restating analysis.

The feature baseline is the READY TASK CONTRACT. The bug baseline is the BUG CONTRACT
plus a CONFIRMED ROOT CAUSE REPORT. Any later code, test, fixture, snapshot, or
behavior-affecting configuration change requires code review of the new baseline.

## Evidence

Use [check-evidence](references/check-evidence.md) to record commands and manual checks.
A proposed command is NOT_RUN. A mock proves only its mocked boundary. Unavailable
required evidence is BLOCKED unless an observed defect independently requires FAIL.

The verification helper scripts accept an explicit repository path. Call them by
absolute path; in Claude Code, prefix them with `${CLAUDE_PLUGIN_ROOT}/`:

```bash
bash skills/feature-workflow/verification/scripts/changed-files.sh /path/to/repository
bash skills/feature-workflow/verification/scripts/related-tests.sh /path/to/repository
bash skills/feature-workflow/verification/scripts/verify.sh --repo /path/to/repository -- npm test
```

They provide deterministic inputs; they do not decide what evidence is sufficient.

## Behavioral evaluations

The package-root [`evals/`](../evals/README.md) suite runs with
`claude plugin eval .`. It has 24 cases: at least one natural-language trigger case per
skill, three negative cases asserting that a skill does not fire, and four
scaffolded cases that edit files or run tests. Each case scores both whether the
intended skill fired and whether the outcome meets a PASS/FAIL rubric, and is compared
against a no-plugin baseline.

The `skills/evals/` directory keeps the 24 source decision scenarios for workflow
invariants such as stale evidence, review authorization, unavailable contracts,
blocker retention, bug handoffs, reviewer provenance, and counter preservation; the
plugin eval cases are written from them. Build one self-contained scenario packet,
without calling a model, with:

```bash
python3 skills/evals/build_packet.py --case E1 --metadata
```

Historical measured results from the earlier Codex packaging remain in
[evals/results/](evals/results/2026-10-10-below-eight-probes.md) for reference; they do
not describe Claude Code behavior.

## Validation

Run from the workspace root:

```bash
bash skills/scripts/validate-skill-system.sh
python3 -m unittest discover -s skills/evals -p 'test_*.py'
```

The structural validator checks required files, frontmatter, exact Walk It Down fields,
stage contracts, links, templates, routes, stop conditions, one-to-one skill exposure in
the plugin manifest, and the eval suite's case, grader, and trigger coverage. It rejects prescribed model classes, numeric context ladders, or review role-play
in active instructions. Structural PASS does not replace live behavioral or client tests.

## Maintenance

Keep active instructions focused on outcomes and non-negotiable constraints. Add a rule
only when it changes observable behavior, safety, authority, or handoff correctness.
Avoid generic engineering advice, fixed investigation algorithms, model-selection
policy, and duplicated guidance. Record material changes in
[CHANGELOG.md](CHANGELOG.md) and rerun validation.
