# PROJECT CONTEXT

- Target: <absolute or workspace-relative repository/workspace identity>
- Revision: <pc1; increment for material context changes>
- Status: <CURRENT / PARTIAL / BLOCKED>
- Selected route / scope: <route and repository-dependent purpose>
- Repository baseline: <Git root(s), branch/commit or non-Git identity, worktree state>
- Sources: <instructions, manifests, docs, entry points, representative source paths>
- Discovery depth: <P0-P4; question justifying P3/P4, or none>
- Freshness basis: <instructions/manifests/baseline/architecture files checked>
- Prior revision / changes: <initial or material reason for refresh>

## Repository Topology

- <root or nested repository>: <role, boundary, relevant status>
- Excluded areas: <generated/vendor/build/unrelated roots and reason>

## Governing Instructions

- <path or runtime source>: <scope and material rules for downstream work>

## Technology and Tooling

- Languages/runtimes: <evidence>
- Frameworks/platforms: <evidence>
- Package/workspace/build tools: <evidence>
- Infrastructure/storage/external systems: <evidence or unknown>

## Structure and Responsibilities

- <path/module>: <evidence-backed responsibility and public boundary>

## Architecture and Flows

- Style/pattern: <layered, modular, service, event-driven, plugin, library, CLI, etc.; evidence>
- Dependency direction: <major relationships with source evidence>
- Runtime/control flow: <entry to important boundary; unknown if not established>
- Data/state flow: <source, transformation, persistence/external boundary; if applicable>

## Entry Points and Interfaces

- <path/symbol/interface>: <role and consumers>

## Commands and Conventions

- Build/run: <observed command and source, or unknown>
- Test: <observed command and source, or unknown>
- Lint/typecheck/static/security: <observed command and source, or unknown>
- Conventions: <naming, layout, generated-code, migration, or test patterns with evidence>
- Command status: <discovered only; identify any read-only command actually executed>

## Task-Relevant Map

- <selected route concern>: <likely component and why; defer detailed task analysis>

## Risks and Unknowns

- R1: <risk, evidence, downstream impact>
- U1: <unknown, searches/evidence checked, whether it blocks the selected route>

## Handoff

- Context disposition: <reuse / refresh condition / stop reason>
- Next stage / owner: <selected feature, bug, review, or repository-dependent NORMAL work>
- Required refresh triggers: <target, instructions, manifest, baseline, or architecture change>
- Remaining action: <none or exact owner/action/resume condition>

Keep this artifact architectural and reusable. Cite paths and symbols instead of
copying source or embedding task-specific requirements, diagnoses, or review findings.
