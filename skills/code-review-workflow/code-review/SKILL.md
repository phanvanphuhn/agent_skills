---
name: code-review
description: "Reviews actual code read-only at the required gate or on explicit review requests, using Supervisor, Lead, and Peer perspectives."
---

# Code review

## Responsibility

Independently challenge actual code for correctness, architecture, security,
regressions, maintainability, conventions, and test adequacy. Never modify code.

## Trigger

- REQUIRED GATE — after implementation, bug fixes, or later code/test/fixture/snapshot/
  behavior-affecting configuration changes, including verification-authored tests
  and fixes returning READY_FOR_RE_REVIEW.
- MANUAL REVIEW — explicit review of files, diffs, staged changes, commits, branches,
  PRs, or supplied code; does not start feature/bug analysis.

## When not to run

Skip ordinary NORMAL requests without review intent. Explicit manual scope may include
unchanged files. Do not fix issues, replace validation/root-cause analysis, or approve
from reports alone.

## Inputs

Start with current PROJECT CONTEXT, applicable instructions, scoped code/diff and
related tests, exact baseline, and review-cycle history. Load only the applicable bundle:

- Feature gate: READY TASK CONTRACT, VALIDATION REPORT, IMPLEMENTATION REPORT.
- Bug gate: BUG CONTRACT, REPRODUCTION REPORT, ROOT CAUSE REPORT, BUG FIX REPORT.
- Re-review: prior CODE REVIEW REPORT plus the FIX CODE REVIEW REPORT or verification
  report explaining the new diff. Reuse accessible unchanged governing artifacts.
- Manual: user-selected scope and directly relevant evidence; unknown product behavior
  is NEEDS_CONTEXT, not an invented requirement.

Do not load the skills/templates that produced these inputs. Preserve unrelated changes
and keep secrets out of reports.

## Review strategy — Walk It Down

R0 diff/supplied code → R1 scoped files → R2 affected interfaces/types/tests →
R3 callers/dependencies → R4 analogous patterns → R5 broader architecture.
Search first; name the unresolved question justifying expansion and stop when answered.
Gather evidence once for all three perspectives, not three repository scans.

## SLP review

### Supervisor

Check intent, scope, AC/expected-behavior coverage, compatibility, operations, errors,
and regression risk. Bug fixes must address the confirmed cause, not hide symptoms.

### Lead

Check architecture, abstractions, state/data flow, lifecycle/concurrency, APIs/types,
resource management, security, relevant performance, testability, and maintainability.
Preference-only refactors are not defects.

### Peer

Inspect logic/mappings, stale state, off-by-one errors, races, await/cleanup, fallbacks,
copy/paste mistakes, dead code, accidental changes, weak tests, and edges.
Consolidate duplicate observations after all perspectives; zero findings is valid.

## Issue contract and decision

Each issue needs ID, SEVERITY, FOUND_BY, FILE / LOCATION, PROBLEM, EVIDENCE, IMPACT,
and RECOMMENDED ACTION.

- HIGH — requirement/cause failure, security/data risk, serious regression, or major
  architectural defect; blocking.
- MEDIUM — concrete correctness, reliability, test, or maintainability defect; blocking.
- LOW — limited-risk improvement; blocking only by repository policy or concrete
  completion risk.

Unproven concerns are NEEDS_CONFIRMATION; unknown product behavior is NEEDS_CONTEXT.
Choose the first applicable decision, in this order:

1. Confirmed blocking finding(s): increment `review_cycles` once for this issued report,
   even if review coverage is incomplete. Return CHANGES_REQUIRED below 3, otherwise
   REVIEW_ESCALATION. Missing evidence never downgrades a confirmed defect to BLOCKED.
2. No confirmed blocking findings, but required scope, evidence, access, or reviewer
   independence is missing: return BLOCKED and preserve `review_cycles`.
3. Sufficient evidence and no blocking findings: return APPROVED and preserve the count.

Keep confirmed findings and unresolved review blockers separate in every outcome.
Give each blocker a stable task-scoped BLK-* ID. Record scope, missing evidence, owner,
action, resume condition, and status: OPEN, EVIDENCE_SUPPLIED, or RESOLVED. Preserve IDs
across fixes, re-review, and context recovery; closing or reopening retains its history.
Only code-review marks RESOLVED after inspecting closure evidence. Reconcile every
inherited unresolved ID before deciding; missing blocker history must be recovered.
Fixing findings does not clear blockers. OPEN/EVIDENCE_SUPPLIED prevent approval;
without confirmed blocking findings, unresolved required gaps yield BLOCKED.

Count the initial blocking report. APPROVED/BLOCKED, fixes, unproven concerns, and
rereading a report never increment or reset the count. At the limit, further attempts
require human direction with history retained. Verification failure counters are unchanged.

CHANGES_REQUIRED stops for explicit fix authorization. An original `review and fix`
request supplies it after the report exists; otherwise never invoke fix-code-review
automatically.

## Execution routing

Apply [shared execution routing](../../references/execution-routing.md) through this profile;
open the linked reference only for an override, delegation, or runtime fallback.

- `START_CLASS`: STANDARD
- `ESCALATE_WHEN`: Security, data loss, concurrency, public-contract, or cross-system risk requires DEEP; a small complete low-risk diff may use ECONOMY.
- `DELEGATE_WHEN`: A distinct capable reviewer is authorized and available; SLP perspectives never require three agents.

## Independence and routing

Use a distinct reviewer when authorized/available; otherwise conduct a fresh separated
pass and disclose that limitation. SLP means perspectives, not three agents. Inspect
actual code independently of implementer conclusions.

Only invalidated upstream assumptions route backward: requirements contradictions to
requirement-validator, incorrect causes to bug-root-cause, missing authority/product
decisions to the human. Ordinary defects stay with explicitly authorized fix-code-review;
all resulting behavior-affecting changes return for review.

## Procedure

1. Establish mode, inputs, independence, and cycle count; read the
   [report template](references/code-review-report-template.md).
2. Inspect scoped code through SLP using the context ladder. On re-review, focus on
   the new diff/affected boundaries and reuse unaffected approved findings. Challenge
   changed test oracles/coverage; new evidence can reopen prior conclusions.
3. Consolidate issues, update counters, and emit the decision with baseline, evidence,
   read-only checks, risks, history, and next owner. Do not modify files.

## Outputs

CODE REVIEW REPORT. Gate approval hands the exact baseline to verification or
bug-verification; manual review returns findings without starting those workflows.

## Completion criteria

All perspectives assessed actual scoped code; findings and checks have evidence,
no files changed, and the next owner is explicit. Only APPROVED permits verification
of the exact current baseline; later code/test/fixture/snapshot/config changes invalidate it.

## Failure and blocked behavior

Name missing evidence, owner, action, and resume condition. Never hide a defect because
fixing it lacks authorization or approve solely from upstream reports.

## Human intervention

CHANGES_REQUIRED without fix authority, BLOCKED, and REVIEW_ESCALATION stop with
prioritized issues, uncertainty, cycle history, and the required human action.
