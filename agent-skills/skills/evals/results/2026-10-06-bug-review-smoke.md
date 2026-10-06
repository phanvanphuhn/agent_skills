# Bug and review behavioral smoke — 2026-10-06

- Candidate baseline: `ce68baa` plus the uncommitted changes documented here.
- Runtime: Codex CLI, `gpt-6-luna`; fresh ephemeral read-only working directory per case.
- Isolation: `ISOLATION_UNVERIFIED`. All five candidates made zero commands, but the
  filesystem boundary was not independently established. Results are decision-level
  observations, not an isolated-suite pass.

| Case | Decision grade | Input / cached / output tokens | Latency |
| --- | --- | --- | --- |
| E7 reproduction | PASS — EVIDENCE_CONFIRMED without invented local replay or cause | 16,561 / 11,008 / 395 | 13.365 s |
| E8 root cause | PASS — INSUFFICIENT_EVIDENCE, competing explanations retained | 16,502 / 11,008 / 561 | 13.921 s |
| E9 bug fix | PASS — BLOCKED, no edit against contradicted cause | 16,507 / 11,008 / 526 | 13.998 s |
| E10 bug verification | PASS — FAIL, both counters incremented, integration gap retained, separate BUG FIX REQUEST | 17,171 / 11,008 / 844 | 20.171 s |
| E11 code review | PASS — same-context limitation disclosed, no invented execution | 17,057 / 11,008 / 512 | 13.858 s |

E10 failed twice during development: first without the fix-request template in its
packet, then with the template but with only a future-request handoff. The final
passing run followed an explicit same-response output rule. These failures are retained
as development history, not counted as passing runs. Other cases and end-to-end
repository behavior were not run for this change.

## Paired E1 cost sample

The runner used the same E1 scenario and model against archived `f62c1f0` and the
current working tree, with zero commands in both runs. Both returned the required
BLOCKED decision and retained `failed_cycles=1`.

| Baseline | Input / cached / output tokens | Latency |
| --- | --- | --- |
| `f62c1f0` | 16,986 / 13,056 / 559 | 8.749 s |
| Current working tree | 17,078 / 11,008 / 402 | 9.900 s |

The current packet used 92 more total input tokens and 157 fewer output tokens; its
single-run latency was 1.151 seconds higher. Cache exposure differed, so this sample
does not establish a cost or latency improvement. Packet hashes were
`c97450369eca2c28004e384b600de1b51d998e93ef66ee0da7b13848d7f001d9`
and `03ec5e7a4b41a09760d049fa4f398310e2b2bad74193321d39a2d3f3c6fd1186`,
respectively.

## Implicit native discovery

From `/tmp`, outside the repository, a request to review a diff without naming a
skill caused Codex to read the installed `code-review/SKILL.md` from the plugin cache.
The final answer was BLOCKED because no repository or diff was supplied; the observed
discovery result is limited to implicit selection of that skill on this client setup.
It does not prove correct implicit selection for all skills or clients.
