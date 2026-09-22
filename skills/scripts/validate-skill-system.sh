#!/usr/bin/env bash
# Read-only structural checks. Requires Bash and standard Unix utilities only.
set -eu

if [ "$#" -gt 1 ]; then
  printf 'Usage: bash %s [workspace-root]\n' "$0" >&2
  exit 2
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
workspace_root=${1:-"$script_dir/../.."}
if [ ! -d "$workspace_root" ]; then
  printf 'ERROR: workspace directory does not exist: %s\n' "$workspace_root" >&2
  exit 2
fi
workspace_root=$(CDPATH= cd -- "$workspace_root" && pwd)
errors=0

fail() {
  printf 'ERROR: %s\n' "$*" >&2
  errors=$((errors + 1))
}

require_file() {
  if [ ! -s "$workspace_root/$1" ]; then
    fail "$1: required file is missing or empty"
  fi
}

require_heading() {
  if ! awk -v wanted="$2" '$0 == wanted { found=1 } END { exit !found }' "$workspace_root/$1"; then
    fail "$1: missing heading '$2'"
  fi
}

require_pattern() {
  if ! awk -v wanted="$2" '$0 ~ wanted { found=1 } END { exit !found }' "$workspace_root/$1"; then
    fail "$1: missing orchestration rule: $3"
  fi
}

check_frontmatter() {
  # Deliberately restricted YAML: two scalar lines, no escapes/multiline values.
  if ! awk -v expected="$2" '
    NR == 1 { if ($0 != "---") bad=1; next }
    !closed && $0 == "---" { closed=1; next }
    !closed {
      if ($0 ~ /^name: [a-z0-9]+(-[a-z0-9]+)*$/) {
        names++; value=substr($0, 7)
        if (value != expected || length(value) > 64) bad=1
      } else if ($0 ~ /^description: "[^"\\]+"$/) {
        descriptions++; value=substr($0, 15, length($0)-15)
        if (value !~ /[^[:space:]]/ || length(value) > 1024 || value ~ /[[:cntrl:]]/) bad=1
      } else { bad=1 }
    }
    END { exit (bad || !closed || names != 1 || descriptions != 1) }
  ' "$workspace_root/$1"; then
    fail "$1: invalid frontmatter; require matching lowercase-hyphen name and a non-empty one-line double-quoted description (max 1024 characters), with no escapes or extra fields"
  fi
}

check_links() {
  # Check inline Markdown links in shipped documents, including links in examples.
  local doc=$1 target path
  while IFS= read -r target; do
    case "$target" in
      http://*|https://*|mailto:*|\#*) continue ;;
    esac
    path=${target%%#*}
    if [ -z "$path" ] || [ ! -f "$workspace_root/$(dirname -- "$doc")/$path" ]; then
      fail "$doc: local link target does not exist: $target"
    fi
  done < <(awk '
    {
      rest=$0
      while (match(rest, /\[[^]]+\]\([^)]*\)/)) {
        link=substr(rest, RSTART, RLENGTH)
        sub(/^[^]]*\]\(/, "", link); sub(/\)$/, "", link)
        print link
        rest=substr(rest, RSTART+RLENGTH)
      }
    }
  ' "$workspace_root/$doc")
}

documents=(
  AGENTS.md
  skills/README.md
  skills/CHANGELOG.md
  skills/task-requirements/SKILL.md
  skills/task-requirements/references/task-contract-template.md
  skills/requirement-validator/SKILL.md
  skills/requirement-validator/references/validation-report-template.md
  skills/implementation/SKILL.md
  skills/implementation/references/implementation-report-template.md
  skills/verification/SKILL.md
  skills/verification/references/verification-report-template.md
  skills/verification/references/fix-request-template.md
  skills/verification/scripts/changed-files.sh
  skills/verification/scripts/related-tests.sh
  skills/verification/scripts/verify.sh
  skills/examples/feature-workflow.md
)

for doc in "${documents[@]}"; do
  require_file "$doc"
  if [ -s "$workspace_root/$doc" ]; then check_links "$doc"; fi
done
require_file skills/scripts/validate-skill-system.sh

for script in skills/scripts/validate-skill-system.sh \
  skills/verification/scripts/changed-files.sh \
  skills/verification/scripts/related-tests.sh \
  skills/verification/scripts/verify.sh; do
  if [ -s "$workspace_root/$script" ] && ! bash -n "$workspace_root/$script"; then
    fail "$script: Bash syntax check failed"
  fi
done

for skill in task-requirements requirement-validator implementation verification; do
  doc="skills/$skill/SKILL.md"
  if [ ! -s "$workspace_root/$doc" ]; then continue; fi
  check_frontmatter "$doc" "$skill"
  lines=$(awk 'END {print NR}' "$workspace_root/$doc")
  if [ "$lines" -ge 500 ]; then fail "$doc: has $lines lines; must be below 500"; fi
  for heading in Responsibility Trigger 'When not to run' Inputs Procedure Outputs \
    'Completion criteria' 'Failure and blocked behavior' 'Human intervention'; do
    require_heading "$doc" "## $heading"
  done
done

require_heading skills/task-requirements/SKILL.md '## Context budget'
require_heading skills/requirement-validator/SKILL.md '## Investigation strategy — Walk It Down'
require_heading skills/implementation/SKILL.md '## Context reuse rule'
require_heading skills/implementation/SKILL.md '## Minimal change principle'
require_heading skills/verification/SKILL.md '## Verification strategy — Walk It Down'

for candidate in "$workspace_root"/skills/*/SKILL.md; do
  if [ ! -f "$candidate" ]; then continue; fi
  candidate_name=$(basename -- "$(dirname -- "$candidate")")
  case "$candidate_name" in
    task-requirements|requirement-validator|implementation|verification) ;;
    *) fail "skills/$candidate_name/SKILL.md: unexpected fifth skill; orchestration belongs in AGENTS.md" ;;
  esac
done

contract=skills/task-requirements/references/task-contract-template.md
if [ -s "$workspace_root/$contract" ]; then
  for heading in Task 'Business Intent' 'Current Behavior' 'Expected Behavior' \
    'Acceptance Criteria' 'Functional Requirements' 'Non-Functional Requirements' \
    'Relevant Files / Components' 'Existing Patterns' Dependencies 'Edge Cases' \
    Assumptions Unknowns 'Implementation Constraints' 'Verification Requirements' Handoff; do
    require_heading "$contract" "## $heading"
  done
fi

report=skills/requirement-validator/references/validation-report-template.md
if [ -s "$workspace_root/$report" ]; then
  for heading in 'Repository Evidence' 'Uncertainty Assessment' 'Resolved Decisions' \
    'Investigation Log' 'Questions and Required Actions' 'Readiness Assessment' Handoff; do
    require_heading "$report" "## $heading"
  done
fi
report=skills/implementation/references/implementation-report-template.md
if [ -s "$workspace_root/$report" ]; then
  for heading in Summary 'Files Changed' 'Implementation Decisions' 'AC Mapping' \
    'Assumptions Used' 'Developer Self-Review' 'Developer Checks' Risks 'Tests Needed' \
    'Context Escalation' 'Remaining Concerns' 'Repair Response' Handoff; do
    require_heading "$report" "## $heading"
  done
fi
report=skills/verification/references/verification-report-template.md
if [ -s "$workspace_root/$report" ]; then
  for heading in 'Verification Scope' 'AC Verification' 'Other Required Checks' 'Regression Risk' \
    'Code Quality' 'Architecture Compliance' 'Uncovered Edge Cases' 'Test Coverage' \
    'Commands Executed' Failures 'Cycle History' Handoff; do
    require_heading "$report" "## $heading"
  done
fi
report=skills/verification/references/fix-request-template.md
if [ -s "$workspace_root/$report" ]; then
  for heading in Defects Constraints 'Prior Attempts and Remaining Blockers' 'Required Handoff'; do
    require_heading "$report" "## $heading"
  done
fi

if [ -s "$workspace_root/AGENTS.md" ]; then
  for heading in 'Scope and routing' 'Applicability and authorization' \
    'Cost and context policy — Walk It Down' 'Shared handoff contract' 'State transitions' 'Loop limit and human intervention' \
    'Evidence and verification rules' 'Skill-system maintenance'; do
    require_heading AGENTS.md "## $heading"
  done
  for skill in task-requirements requirement-validator implementation verification; do
    require_pattern AGENTS.md "skills/$skill/SKILL[.]md" "route to $skill"
  done
  for artifact in 'TASK CONTRACT' 'VALIDATION REPORT' 'IMPLEMENTATION REPORT' \
    'VERIFICATION REPORT' 'FIX REQUEST'; do
    require_pattern AGENTS.md "$artifact" "handoff artifact $artifact"
  done
  for state in READY NEEDS_CLARIFICATION BLOCKED PASS FAIL NOT_RUN DONE; do
    require_pattern AGENTS.md "(^|[^A-Z_])$state([^A-Z_]|$)" "status $state"
  done
  require_pattern AGENTS.md 'INPUT.*TASK CONTRACT.*REQUIREMENT VALIDATION' 'requirements entry flow'
  require_pattern AGENTS.md 'READY.*IMPLEMENTATION.*VERIFICATION.*PASS.*DONE' 'READY/PASS gates'
  require_pattern AGENTS.md 'NEEDS_CLARIFICATION.*HUMAN CLARIFICATION.*REQUIREMENT VALIDATION' 'clarification loop'
  require_pattern AGENTS.md 'VERIFICATION FAIL.*FIX REQUEST.*IMPLEMENTATION.*VERIFICATION' 'repair loop'
  require_pattern AGENTS.md 'VERIFICATION BLOCKED.*STOP' 'blocked verification stop'
  require_pattern AGENTS.md 'Only PASS permits DONE' 'completion gate'
  require_pattern AGENTS.md 'Stop at the third' 'three-failure limit'
  require_pattern AGENTS.md 'failed_cycles' 'persistent failed-cycle count'
  require_pattern AGENTS.md 'including the initial verification' 'initial FAIL counts toward limit'
  require_pattern AGENTS.md 'L0.*existing trusted structured artifact' 'L0 context level'
  require_pattern AGENTS.md 'L5.*broad repository exploration' 'L5 context level'
  require_pattern AGENTS.md 'Every escalation must name' 'evidence-based context escalation'
  require_pattern AGENTS.md '### Handoff economy' 'compact handoff policy'
  require_pattern AGENTS.md 'repair consumes only failed ACs' 'targeted repair handoff'
fi

if [ "$errors" -gt 0 ]; then
  printf 'FAIL: %s structural error(s).\n' "$errors" >&2
  exit 1
fi
printf 'PASS: four skills, templates, links, line limits, and orchestration structure validated.\n'
printf 'Semantic behavior and native client discovery require separate review.\n'
