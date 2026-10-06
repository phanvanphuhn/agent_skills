# Required-gate and stage behavioral smoke — 2026-10-06

- Candidate baseline: `1af248e` plus the uncommitted changes documented here.
- Runtime: Codex CLI, `gpt-6-luna`; fresh ephemeral read-only working directory per run.
- Isolation: `ISOLATION_UNVERIFIED`; all seven passing candidates made zero commands,
  but their accessible filesystem boundary was not independently enforced. These are
  decision-level observations, not a full isolated-suite or real-workflow pass.

| Case | Decision grade | Input / cached / output tokens | Latency |
| --- | --- | --- | --- |
| E11 same-context gate | PASS — BLOCKED with OPEN independence blocker, cycle unchanged | 17,148 / 11,008 / 426 | 12.393 s |
| E11-fresh | PASS — APPROVED only with documented separate reviewer session | 17,150 / 11,008 / 364 | 11.228 s |
| E11-defect | PASS — CHANGES_REQUIRED, cycle 1, confirmed defect and separate independence blocker | 17,150 / 11,008 / 671 | 18.278 s |
| E12 task router | PASS — BUG route only, no downstream work | 15,718 / 13,056 / 14 | 4.900 s |
| E13 project discovery | PASS — PARTIAL, narrow command refresh, bug-analysis proceeds | 16,469 / 13,056 / 604 | 16.656 s |
| E14 task requirements | PASS — DRAFT preserving conflicting ACs | 16,347 / 11,008 / 986 | 28.064 s |
| E15 bug analysis | PASS — DRAFT separating report, payload, and unknowns | 16,243 / 11,008 / 1,009 | 17.871 s |

During development, the first E13 scenario ambiguously described pc1 as accessible
without supplying its full body. Its candidate reasonably returned PARTIAL. The final
packet clarifies the available evidence and produced the recorded PASS. One E11-defect
runner attempt exited before returning a response or usage; it is not counted as a
candidate decision. The successful rerun is recorded above.

Packet hashes, respectively: `e8647963e5c12f5f1235e8b696dbccebc9cf87ed00ff8bdd93d1d0fa862e208d`,
`1f5a9c53d186c054abe1a3a6f5dc02f4edd85ea4371ef1fcca1d92b86e6cb953`,
`61f0a19999b595a90255f7e90fd364667e509022fa6b55901675d717fe87a149`,
`a26fc1b32180a56d5c3b0797c178b66977ff1dea4d74c47d5e9649c76b4df954`,
`ec738f8c6b813acedd7cf820c38b21b6428b1f88f4370aa815483cd09a0eae6e`,
`4e623730c248519f8bb22f05b22a471a30e670030cce69cf408d321cc02d81ae`, and
`2153a4300d4830db846e221a8a0ee32f121c3b2f49a83f2e6cd61b7670ea961c`.

Only the targeted cases above were run against this baseline. Existing cases and real
repository workflows need independent testing before any reliability or savings claim.

## Later independent-review handoff probes

After adding a copy-ready reviewer handoff, three targeted controls were rerun on a
later `1af248e+dirty` skill baseline. Each returned the expected decision and made
zero commands; isolation remains `ISOLATION_UNVERIFIED`.

| Case | Decision and handoff grade | Input / cached / output tokens | Latency | Packet SHA-256 |
| --- | --- | --- | --- | --- |
| E11 | PASS — BLOCKED; copy-ready S1/r1/i1 request with open blocker | 17,515 / 13,056 / 616 | 17.187 s | `7177f0a224b6515b5ddedf92b23986339ad386d14a78c78f96e047eee1313a37` |
| E11-fresh | PASS — APPROVED; handoff N/A | 17,517 / 11,008 / 406 | 27.573 s | `53878d37a68e9b9b13805053bdf643856995b74406938eeff06d535317e65898` |
| E11-defect | PASS — CHANGES_REQUIRED; authorized correction precedes fresh review of resulting baseline | 17,515 / 13,056 / 992 | 22.495 s | `6c84114eeb7c230fdcfce5f8ea22f44e81f82ce9ebb58cee9de6901b264208f6` |

An intermediate E11-defect probe treated prose describing source as insufficient
actual code and returned BLOCKED. The scenario was corrected to supply the complete
scoped S1 source and test; the final passing result above uses that revised packet.
These observations do not demonstrate that a real client can start or attest a fresh
reviewer session automatically.
The final instruction edit clarified which baseline each decision hands off and
expanded the compact packet's evidence list; it was structurally checked but not
rerun through the model after the recorded probes.
