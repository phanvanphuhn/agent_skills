# Execution routing

Use this reference only when choosing or changing an agent, model class, or reasoning
budget. The selected skill's local profile supplies the normal starting class.

## Walk It Down

Choose context depth, agent topology, and model capability separately. Start with
deterministic tools, the current agent, and the lowest class that can safely make the
next decision. Escalate one dimension only to answer a named material question; stop
or step down when it is answered. Required checks, independence, and safety gates are
never waived to reduce cost.

Do not route from file count or workflow stage alone. Consider ambiguity, coupling,
reversibility, security/privacy/data-loss impact, concurrency, external-state risk,
evidence quality, and prior failed attempts.

Apply every matching row and choose the highest minimum class. A repository rule may
raise the class. If a material risk cannot yet be ruled out, use the next higher class
until evidence resolves it; task size alone never lowers the minimum.

| Decisive condition | Minimum class |
| --- | --- |
| Exact, bounded, reversible operation with deterministic acceptance and no unresolved risk | ECONOMY |
| Engineering judgment, multiple coupled files, or an uncertain but local behavior boundary | STANDARD |
| Security, privacy, authorization, tenant isolation, credentials, data loss, irreversible external effects, or safety impact | DEEP |
| Unresolved concurrency/distributed-state behavior, contradictory cross-system evidence, or a public-contract decision spanning systems | DEEP |
| Two unsuccessful reasoning attempts on the same unresolved question | DEEP |

When conditions tie within a class, prefer the cheaper model and lower reasoning effort.
After the forcing condition is resolved, recompute the table for the next bounded task
instead of retaining the highest class for the whole workflow.

## Agent selection

Stay with one agent for short tasks, ordered dependencies, shared mutable state, or a
single write scope. Delegate only when the runtime and user authority permit it and a
bounded subtask is independently useful, such as isolated research, non-overlapping
components, an expensive check, or independent review.

Before delegating, confirm that expected quality or latency benefit exceeds the extra
prompt, context, reconciliation, and coordination cost. Give each agent one objective,
one owned scope, the applicable instruction/skill, only relevant artifacts and evidence
IDs, and an explicit output. Never make one agent per stage by default. One owner writes
each path or executes each check; the coordinator reconciles results before review.

## Model classes

Map these capability classes to the models actually available in the runtime. Names are
examples, not permanent requirements.

| Class | Use when | Typical runtime mapping |
| --- | --- | --- |
| ECONOMY | Mechanical classification, extraction, known commands, localized edits, or bounded checks with clear acceptance rules | Fast/low-cost model such as Luna; low reasoning |
| STANDARD | Normal implementation, validation, debugging, review, or verification requiring engineering judgment | Balanced model such as Sol; medium reasoning |
| DEEP | Ambiguous cross-system architecture, security or data-loss risk, concurrency/distributed state, contradictory evidence, or repeated failed reasoning | Strongest suitable model such as Astra; high reasoning only as needed |

Use deterministic scripts instead of a model for exact listing, hashing, formatting,
or validation when possible. A large but mechanical task remains ECONOMY; a small but
irreversible security decision may require DEEP.

## Escalation and fallback

Escalate ECONOMY → STANDARD → DEEP only when the current class cannot resolve a named
question or the risk class requires stronger judgment. Do not repeat the same work after
escalation: pass decisive evidence and the unresolved question. After a DEEP decision,
route bounded implementation or checks back to ECONOMY/STANDARD when safe.

If model selection is unavailable, continue with the current model when it is capable
and disclose material limitations. If it is not capable of a high-risk decision, stop
for a stronger model or human direction rather than silently lowering quality. If
delegation is unavailable or costs more than it saves, stay single-agent and use a
fresh separated pass where independence is required.

Record an `EXECUTION ROUTE` only when delegating, overriding the stage default, or an
audit requires it: task/stage, context start and ceiling, class/reasoning, agent owner,
delegated scope, and escalation/de-escalation trigger. Routine default choices need no
extra artifact.
