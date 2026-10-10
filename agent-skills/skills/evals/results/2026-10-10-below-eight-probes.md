# Five-skill improvement probes — 2026-10-10

- Candidate baseline: `5328fd63bf339e2ab001e14ec4b0204991ae0d97+dirty`.
- Runtime: Codex CLI `0.162.0-alpha.17.2`, client-default model; fresh ephemeral
  read-only working directory per case.
- Isolation: `ISOLATION_UNVERIFIED`. The runner observed zero commands in every case,
  but did not independently restrict access to evaluator files. These are targeted
  decision observations, not a full isolated-suite or real repository workflow pass.
- Grading: Inspected each final response against the evaluator-only expectations in
  `behavioral-evals.md`. Raw packets and responses were not committed; the hashes below
  identify packet content but do not replace the missing raw artifacts.

| Case | Decision result | Input / cached / output tokens | Latency | Packet SHA-256 |
| --- | --- | --- | --- | --- |
| E2 | PASS — CHANGES_REQUIRED, confirmed tax defect and separate regional blocker | 18,436 / 12,288 / 665 | 24.876 s | `7bc18788d6902b24ecf80d13ac54d13d71b4b5cea0fbe6dfefa8bad3dfb51709` |
| E5 | PASS — READY_FOR_RE_REVIEW, BLK-1 OPEN, counters unchanged | 17,827 / 12,288 / 730 | 23.119 s | `6a2a8d2f2b30f0ed7d0cd12b89f9005f2af9a605f06edb81e1b2b5d10a45ab7d` |
| E6 | PASS — NEEDS_CLARIFICATION with one physical-order question | 17,925 / 12,288 / 548 | 19.382 s | `0e4d885e943a692dc80bff28a537db99d1b5e79d17e690122b841b39a7791a70` |
| E6-partial | PASS — digital answer retained, physical question remains | 17,940 / 12,288 / 523 | 18.653 s | `c0634aa3205438b17e995ca85065339f7ab06a5fbf93b6c361eff4808c638ccf` |
| E11 | PASS — required review BLOCKED for same-context limitation, copy-ready packet supplied | 18,871 / 12,288 / 885 | 19.948 s | `489444b5cee70a0b87765b6fb4fac22387ce5f6338c79d95bfa9ab8241f2b3a8` |
| E13 | PASS — PARTIAL context, narrow command refresh, stale Git state disclosed | 18,172 / 12,288 / 971 | 35.607 s | `b923a8090aac1a4e470d307238c3252e163ce8f5c678d8b5e4252ce2f7931b6c` |
| E16 | PASS — explicit CHECKPOINT, both unsaved documents returned, verification remains BLOCKED | 18,873 / 12,288 / 2,092 | 58.773 s | `26be8ad59356e8cc823e8001ec1027ce58ce2e37b8e3f753f33d6e3faf4b0e21` |

E16 exercised the read-only persistence fallback. It did not test creation of files in
a writable target or native client invocation policy. E11 exercised packet content and
the BLOCKED decision, not a completed independent approval. The seven runs were taken
at points during one dirty worktree edit; each packet hash, rather than the broad
`+dirty` label, identifies its exact candidate input.
