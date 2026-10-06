# Project integration workflow skills

This package gives Codex a reusable path through an unfamiliar software project. It
defines stage boundaries, required inputs and outputs, authorization rules, evidence
contracts, and handoffs. Every skill uses a lightweight Walk It Down contract while
avoiding fixed model classes, numeric context ladders, role-play, or implementation algorithms.

## Layout

```text
agent-skills/
├── AGENTS.md
├── .codex-plugin/plugin.json
├── .agents/plugins/marketplace.json
├── .codex/config.toml
└── skills/
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

The `agent-skills` directory is the whole package. Clone this repository into another
project and use that directory: it holds `AGENTS.md`, `skills/`, the plugin manifest,
the local marketplace, and plugin enablement.

Open the workspace containing `AGENTS.md`, or explicitly supply that file when working
inside a child repository. The workspace routes every new top-level request through
`task-router`; repository-dependent work receives a reusable PROJECT CONTEXT before its
selected stage runs.

Opening the workspace uses `AGENTS.md`. The repo-local marketplace and Codex configuration
enable the plugin for trusted projects, while its manifest declares every skill root for
native `$skill-name` discovery. Structural validation proves package coverage; live
invocation still depends on the target client/version loading repo marketplaces. Explicit
discovery is currently smoke-tested on Codex CLI `0.160.0`; see the
[recorded result](evals/results/2026-10-05-walk-it-down-smoke.md).

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
The required code-review gate can APPROVE only from a fresh reviewer context separate
from implementation; when that context is unavailable, it records a blocker instead of
claiming independent approval and gives a copy-ready handoff to a separate reviewer.
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

The `evals/` directory contains 22 decision scenarios for workflow invariants such as
stale evidence, review authorization, unavailable contracts, blocker retention, bug
handoffs, reviewer provenance, and counter preservation. They test observable decisions,
not a required thought process or exact wording.

Build one candidate packet with:

```bash
python3 skills/evals/build_packet.py --case E1 --metadata
```

Run a measured fresh-context probe with:

```bash
python3 skills/evals/run_behavioral_eval.py --case E4 --model <model> --output /tmp/E4.json
```

The runner uses an ephemeral, read-only working directory, captures the JSONL-derived
response, command list, token usage, and wall-clock latency, and labels isolation
`ISOLATION_UNVERIFIED` until the runtime boundary is independently established. Packet
construction alone does not call a model. For a comparison with an archived package,
pass `--root /path/to/archive --baseline-label <revision>`; compare only matching cases,
models, and runtime conditions, and do not infer savings from a single run.

The current three-stage measured smoke and native discovery result is recorded in
[evals/results/2026-10-05-walk-it-down-smoke.md](evals/results/2026-10-05-walk-it-down-smoke.md).
The targeted bug/review probes, one paired cost comparison, and implicit discovery
check are recorded in
[evals/results/2026-10-06-bug-review-smoke.md](evals/results/2026-10-06-bug-review-smoke.md).
The required-gate review controls and four previously uncovered stage probes are
recorded in [evals/results/2026-10-06-gate-and-stage-smoke.md](evals/results/2026-10-06-gate-and-stage-smoke.md).

## Validation

Run from the workspace root:

```bash
bash skills/scripts/validate-skill-system.sh
python3 -m unittest discover -s skills/evals -p 'test_*.py'
```

The structural validator checks required files, frontmatter, exact Walk It Down fields,
stage contracts, links, templates, routes, stop conditions, and one-to-one native package
exposure. It rejects prescribed model classes, numeric context ladders, or review role-play
in active instructions. Structural PASS does not replace live behavioral or client tests.

## Maintenance

Keep active instructions focused on outcomes and non-negotiable constraints. Add a rule
only when it changes observable behavior, safety, authority, or handoff correctness.
Avoid generic engineering advice, fixed investigation algorithms, model-selection
policy, and duplicated guidance. Record material changes in
[CHANGELOG.md](CHANGELOG.md) and rerun validation.
