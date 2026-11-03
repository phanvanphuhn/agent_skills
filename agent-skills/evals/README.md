# Claude Code plugin evals

Cases for `claude plugin eval` (Claude Code v2.1.269 or later). Each case directory
holds a natural-language `prompt.md` that does not name a skill, a `tool_used: Skill`
grader that shows whether the intended skill fired, and a result grader. Negative cases
assert with `arm: both` that a skill does not fire. Scenarios are written from the decision
probes in [`../skills/evals/`](../skills/evals/behavioral-evals.md).

Run from the package root (the folder containing `.claude-plugin/plugin.json`).

Read-only smoke suite, no extra grants:

```bash
claude plugin eval . --tag smoke
```

Cases that seed a git repository and edit files or run tests:

```bash
claude plugin eval . --tag writes --scaffold \
  --allow-tools Edit Write "Bash(python3 *)" "Bash(git *)"
```

Iterate on one case with a single run and no baseline:

```bash
claude plugin eval . --case <case-name> --runs 1 --ablation none
```

CI gate, with pinned models and a cost ceiling:

```bash
claude plugin eval . --tag smoke --trust-plugin --json results.json \
  --threshold 0.8 --model <agent-model> --judge-model <judge-model> \
  --no-publish --max-cost-usd 20
```

Every run and judge vote is a billed model call; a full two-arm run makes roughly
cases × 3 × 2 agent runs. `results/` is ignored by Git.

Check the suite's structure without calling a model:

```bash
python3 skills/scripts/validate_claude_package.py
```
