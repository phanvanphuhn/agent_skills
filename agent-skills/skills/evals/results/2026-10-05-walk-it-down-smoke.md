# Walk It Down behavioral smoke — 2026-10-05

- Skill baseline: `f62c1f0` plus the dirty evaluation-runner and native-package changes
- Runtime: Codex CLI `0.160.0`, `gpt-6-luna`
- Candidate context: fresh ephemeral read-only working directory per run
- Isolation: `ISOLATION_UNVERIFIED`; evaluator files were outside the working directory,
  no candidate command executions occurred, but the filesystem boundary was not independently proven

| Run | Decision result | Scope result | Input / cached / output tokens | Latency |
| --- | --- | --- | --- | --- |
| E1 verification | PASS | Rejected stale evidence, returned BLOCKED, retained `failed_cycles=1`, and named the current-baseline check owner/action | 16,982 / 11,008 / 373 | 11.868 s |
| E3 code review | PASS | Reported the access defect, returned CHANGES_REQUIRED with `review_cycles=1`, made no edits, and stopped for authorization | 16,854 / 11,008 / 534 | 13.508 s |
| E4 implementation | PASS | Returned BLOCKED for the missing r7 body, retained both counters, avoided the failed lookup, and requested the exact artifact | 16,492 / 11,008 / 328 | 10.871 s |

All three responses met their evaluator-only expectations and performed zero commands.
This is a targeted cross-stage smoke result, not the ten-case isolated-suite pass. It
establishes measured current-run cost and latency, but no token-savings claim is valid
until the same cases run against a comparator baseline under equivalent cache conditions.

## Native discovery smoke

- Registered repository marketplace: `agent-skills-local`.
- Installed and enabled: `agent-skills@agent-skills-local`, version `1.0.0`.
- From `/tmp`, outside this repository, an explicit `$task-router` request caused Codex
  to read the installed `skills/task-router/SKILL.md` from its plugin cache and return
  `ROUTE: NORMAL` with `CONFIDENCE: HIGH`.
- Discovery-run usage: 28,816 input, 24,064 cached input, and 101 output tokens.
- Result: PASS for explicit native discovery on Codex CLI `0.160.0`. Implicit selection
  and other client versions remain separate test targets.
