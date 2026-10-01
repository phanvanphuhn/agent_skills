# Project integration workflow skills

This package gives Codex a reusable path through an unfamiliar software project. It
defines stage boundaries, required inputs and outputs, authorization rules, evidence
contracts, and handoffs. It intentionally does not prescribe a reasoning method, model
class, context ladder, role-play perspective, or implementation algorithm.

## Layout

```text
AGENTS.md
skills/
├── task-router/SKILL.md
├── project-discovery/{SKILL.md,references/project-context-template.md}
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
├── references/check-evidence.md
├── evals/
└── scripts/validate-skill-system.sh
```

## Invocation

Open the workspace containing `AGENTS.md`, or explicitly supply that file when working
inside a child repository. The workspace routes every new top-level request through
`task-router`; repository-dependent work receives a reusable PROJECT CONTEXT before its
selected stage runs.

`skills/` is a workspace-selected directory, not a standard native skill-discovery
location. These skills may not appear in a client skill picker or support `$skill-name`
invocation unless installed separately.

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
```

The files define contracts between these stages. The model remains responsible for
choosing suitable repository inspection, engineering, debugging, and testing methods.

## Skill contract

Each `SKILL.md` contains:

- a discriminating name and trigger description;
- the stage purpose and when it applies;
- required inputs;
- the required observable output;
- boundaries that protect scope, evidence, authorization, and safety; and
- the next-stage handoff.

Detailed output schemas live in linked templates. Deterministic scripts are used only
for repeatable mechanical operations such as changed-file discovery and structural
validation.

## Artifact contract

Artifacts are Markdown in the active conversation unless the user requests files.
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

The verification helper scripts accept an explicit repository path:

```bash
bash skills/feature-workflow/verification/scripts/changed-files.sh /path/to/repository
bash skills/feature-workflow/verification/scripts/related-tests.sh /path/to/repository
bash skills/feature-workflow/verification/scripts/verify.sh --repo /path/to/repository -- npm test
```

They provide deterministic inputs; they do not decide what evidence is sufficient.

## Behavioral evaluations

The `evals/` directory contains isolated decision scenarios for workflow invariants
such as stale evidence, review authorization, unavailable contracts, blocker retention,
and counter preservation. They test observable decisions, not a required thought
process or exact wording.

Build one candidate packet with:

```bash
python3 skills/evals/build_packet.py --case E1 --metadata
```

Packet construction does not call a model. Candidate isolation must be enforced by the
runtime; a shared writable workspace is not an isolated evaluation.

## Validation

Run from the workspace root:

```bash
bash skills/scripts/validate-skill-system.sh
python3 -m unittest discover -s skills/evals -p 'test_*.py'
```

The structural validator checks required files, frontmatter, stage contracts, links,
templates, routes, and stop conditions. It rejects reintroduction of prescribed model
classes, context ladders, or review role-play in active instructions. Structural PASS
does not prove application behavior or native client discovery.

## Maintenance

Keep active instructions focused on outcomes and non-negotiable constraints. Add a rule
only when it changes observable behavior, safety, authority, or handoff correctness.
Avoid generic engineering advice, fixed investigation algorithms, model-selection
policy, and duplicated guidance. Record material changes in
[CHANGELOG.md](CHANGELOG.md) and rerun validation.
