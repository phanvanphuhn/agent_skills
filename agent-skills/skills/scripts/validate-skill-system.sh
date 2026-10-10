#!/usr/bin/env bash
# Read-only structural validation for the workspace skill system.
set -eu

if [ "$#" -gt 1 ]; then
  printf 'Usage: bash %s [workspace-root]\n' "$0" >&2
  exit 2
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
workspace_root=${1:-"$script_dir/../.."}
workspace_root=$(CDPATH= cd -- "$workspace_root" && pwd)
errors=0

fail() {
  printf 'ERROR: %s\n' "$*" >&2
  errors=$((errors + 1))
}

require_file() {
  [ -s "$workspace_root/$1" ] || fail "$1: required file is missing or empty"
}

require_heading() {
  awk -v wanted="$2" '$0 == wanted { found=1 } END { exit !found }' \
    "$workspace_root/$1" || fail "$1: missing heading '$2'"
}

require_pattern() {
  awk -v wanted="$2" '$0 ~ wanted { found=1 } END { exit !found }' \
    "$workspace_root/$1" || fail "$1: missing required marker: $3"
}

require_walk_it_down() {
  if ! awk '
    $0 == "## Walk It Down" { headings++; section=1; next }
    section && /^## / { section=0 }
    section && /^- (Start|Expand|Stop):[ ]+/ {
      field=$0; sub(/^- /, "", field); sub(/:.*/, "", field)
      seen[field]++
      value=$0; sub(/^- [^:]+:[ ]*/, "", value)
      normalized=toupper(value)
      if (length(value) >= 12 && normalized !~ /^(TBD|TODO|UNKNOWN|N\/A|NONE|PLACEHOLDER)([ .:-].*)?$/) valid[field]++
      next
    }
    section && $0 !~ /^[[:space:]]*$/ { extra=1 }
    END {
      required[1]="Start"; required[2]="Expand"; required[3]="Stop"
      for (i=1; i<=3; i++) if (seen[required[i]] != 1 || valid[required[i]] != 1) bad=1
      exit (bad || headings != 1 || extra)
    }
  ' "$workspace_root/$1"; then
    fail "$1: Walk It Down requires exactly one non-placeholder Start, Expand, and Stop field and no extra content"
  fi
}

reject_pattern() {
  if awk -v unwanted="$2" '$0 ~ unwanted { found=1 } END { exit !found }' \
    "$workspace_root/$1"; then
    fail "$1: contains removed prescriptive guidance: $3"
  fi
}

check_frontmatter() {
  if ! awk -v expected="$2" '
    NR == 1 { if ($0 != "---") bad=1; next }
    !closed && $0 == "---" { closed=1; next }
    !closed {
      if ($0 ~ /^name: [a-z0-9]+(-[a-z0-9]+)*$/) {
        names++; value=substr($0, 7)
        if (value != expected || length(value) > 64) bad=1
      } else if ($0 ~ /^description: "[^"\\]+"$/) {
        descriptions++
      } else { bad=1 }
    }
    END { exit (bad || !closed || names != 1 || descriptions != 1) }
  ' "$workspace_root/$1"; then
    fail "$1: frontmatter must contain only matching name and one-line description"
  fi
}

check_links() {
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

skills=(
  'skills/task-router/SKILL.md:task-router'
  'skills/project-discovery/SKILL.md:project-discovery'
  'skills/handoff/SKILL.md:handoff'
  'skills/feature-workflow/task-requirements/SKILL.md:task-requirements'
  'skills/feature-workflow/requirement-validator/SKILL.md:requirement-validator'
  'skills/feature-workflow/implementation/SKILL.md:implementation'
  'skills/feature-workflow/verification/SKILL.md:verification'
  'skills/bug-workflow/bug-analysis/SKILL.md:bug-analysis'
  'skills/bug-workflow/bug-reproduction/SKILL.md:bug-reproduction'
  'skills/bug-workflow/bug-root-cause/SKILL.md:bug-root-cause'
  'skills/bug-workflow/bug-fix/SKILL.md:bug-fix'
  'skills/bug-workflow/bug-verification/SKILL.md:bug-verification'
  'skills/code-review-workflow/code-review/SKILL.md:code-review'
  'skills/code-review-workflow/fix-code-review/SKILL.md:fix-code-review'
)

while IFS= read -r discovered; do
  relative=${discovered#"$workspace_root/"}
  registered=false
  for entry in "${skills[@]}"; do
    if [ "$relative" = "${entry%%:*}" ]; then
      registered=true
      break
    fi
  done
  [ "$registered" = true ] || fail "$relative: unregistered SKILL.md"
done < <(find "$workspace_root/skills" -name SKILL.md -type f -print)

templates=(
  skills/project-discovery/references/project-context-template.md
  skills/handoff/references/handoff-template.md
  skills/handoff/references/task-changelog-template.md
  skills/feature-workflow/task-requirements/references/task-contract-template.md
  skills/feature-workflow/requirement-validator/references/validation-report-template.md
  skills/feature-workflow/implementation/references/implementation-report-template.md
  skills/feature-workflow/verification/references/verification-report-template.md
  skills/feature-workflow/verification/references/fix-request-template.md
  skills/bug-workflow/bug-analysis/references/bug-contract-template.md
  skills/bug-workflow/bug-reproduction/references/reproduction-report-template.md
  skills/bug-workflow/bug-root-cause/references/root-cause-report-template.md
  skills/bug-workflow/bug-fix/references/bug-fix-report-template.md
  skills/bug-workflow/bug-verification/references/bug-verification-report-template.md
  skills/bug-workflow/bug-verification/references/bug-fix-request-template.md
  skills/code-review-workflow/code-review/references/code-review-report-template.md
  skills/code-review-workflow/fix-code-review/references/fix-code-review-report-template.md
)

documents=(
  AGENTS.md
  skills/README.md
  skills/CHANGELOG.md
  skills/references/check-evidence.md
  skills/evals/behavioral-evals.md
  skills/evals/case-01.md
  skills/evals/case-02.md
  skills/evals/case-03.md
  skills/evals/case-04.md
  skills/evals/case-05.md
  skills/evals/case-06.md
  skills/evals/case-07.md
  skills/evals/case-08.md
  skills/evals/case-09.md
  skills/evals/case-10.md
  skills/evals/case-11.md
  skills/evals/case-12.md
  skills/evals/case-13.md
  skills/evals/case-14.md
  skills/evals/case-15.md
  skills/evals/case-16.md
)
for entry in "${skills[@]}"; do documents+=("${entry%%:*}"); done
for template in "${templates[@]}"; do documents+=("$template"); done

for doc in "${documents[@]}"; do
  require_file "$doc"
  [ -s "$workspace_root/$doc" ] && check_links "$doc"
done

for entry in "${skills[@]}"; do
  doc=${entry%%:*}
  name=${entry##*:}
  [ -s "$workspace_root/$doc" ] || continue
  check_frontmatter "$doc" "$name"
  lines=$(awk 'END { print NR }' "$workspace_root/$doc")
  [ "$lines" -lt 200 ] || fail "$doc: must remain below 200 lines"
  require_heading "$doc" '## Walk It Down'
  require_walk_it_down "$doc"

  if [ "$name" = task-router ]; then
    for heading in Purpose Routes Output Boundaries; do
      require_heading "$doc" "## $heading"
    done
  else
    for heading in Purpose 'Use when' Inputs 'Required outcome' Boundaries Handoff; do
      require_heading "$doc" "## $heading"
    done
  fi

  reject_pattern "$doc" 'Execution routing|START_CLASS|ESCALATE_WHEN|DELEGATE_WHEN' 'model/agent routing profile'
  reject_pattern "$doc" 'Investigation strategy|Verification strategy|Review strategy' 'alternate reasoning strategy'
  reject_pattern "$doc" 'SLP review|### Supervisor|### Lead|### Peer' 'review role-play'
  reject_pattern "$doc" '(^|[^A-Z])[LRVPF][0-6]([^0-9]|$)' 'context-level ladder'
done

for route in FEATURE BUG CODE_REVIEW FIX_CODE_REVIEW NORMAL; do
  require_pattern skills/task-router/SKILL.md "$route" "router route $route"
done

for marker in task-requirements requirement-validator implementation verification \
  bug-analysis bug-reproduction bug-root-cause bug-fix bug-verification code-review \
  fix-code-review NEEDS_CLARIFICATION BLOCKED CHANGES_REQUIRED APPROVED PASS DONE; do
  require_pattern AGENTS.md "$marker" "workflow marker $marker"
done
require_pattern AGENTS.md 'third FAIL' 'three-failure stop condition'
require_pattern AGENTS.md 'third blocking review' 'three-review stop condition'
require_pattern AGENTS.md 'Do not deploy' 'external mutation boundary'
require_pattern AGENTS.md 'Task completion alone does not trigger the skill' 'manual-only handoff instruction'
require_pattern skills/handoff/SKILL.md 'HANDOFF[.]md' 'handoff artifact'
require_pattern skills/handoff/SKILL.md 'CHANGELOG[.]md' 'task changelog artifact'
require_pattern skills/handoff/SKILL.md 'Run only when the user explicitly' 'manual-only handoff trigger'
require_file skills/handoff/agents/openai.yaml
require_pattern skills/handoff/agents/openai.yaml '^[[:space:]]*allow_implicit_invocation: false[[:space:]]*$' 'disabled implicit handoff invocation'
require_heading skills/handoff/references/handoff-template.md '## Definition of Done'
require_heading skills/handoff/references/handoff-template.md '## Resume in a Fresh Session'
require_heading AGENTS.md '## Walk It Down'
require_pattern AGENTS.md 'Start.*Expand.*Stop' 'shared Walk It Down contract'

reject_pattern AGENTS.md 'Execution routing|START_CLASS|ESCALATE_WHEN|DELEGATE_WHEN' 'model/agent routing profile'
reject_pattern AGENTS.md 'Investigation strategy|Verification strategy|Review strategy' 'alternate reasoning strategy'
reject_pattern AGENTS.md 'SLP review|### Supervisor|### Lead|### Peer' 'review role-play'
reject_pattern AGENTS.md '(^|[^A-Z])[LRVPF][0-6]([^0-9]|$)' 'context-level ladder'

[ ! -e "$workspace_root/skills/references/execution-routing.md" ] || \
  fail 'skills/references/execution-routing.md: obsolete execution-routing policy must remain removed'

for template in "${templates[@]}"; do
  reject_pattern "$template" 'Context used|Context Escalation|Investigation Log|SLP Summary' 'prescribed process field'
  reject_pattern "$template" 'Highest level|Verification level|P0-P4|L0-L6|R0-R5|V0-V6|F0-F4' 'context-level field'
done

require_heading skills/references/check-evidence.md '## Record'
require_heading skills/references/check-evidence.md '## Reuse decision'

for report in \
  skills/feature-workflow/implementation/references/implementation-report-template.md \
  skills/feature-workflow/verification/references/verification-report-template.md \
  skills/bug-workflow/bug-reproduction/references/reproduction-report-template.md \
  skills/bug-workflow/bug-fix/references/bug-fix-report-template.md \
  skills/bug-workflow/bug-verification/references/bug-verification-report-template.md \
  skills/code-review-workflow/code-review/references/code-review-report-template.md \
  skills/code-review-workflow/fix-code-review/references/fix-code-review-report-template.md; do
  require_pattern "$report" 'references/check-evidence[.]md' 'shared check evidence reference'
done

require_heading skills/feature-workflow/task-requirements/references/task-contract-template.md '## Acceptance Criteria'
require_heading skills/feature-workflow/requirement-validator/references/validation-report-template.md '## Uncertainty Assessment'
require_heading skills/feature-workflow/implementation/references/implementation-report-template.md '## AC Mapping'
require_heading skills/feature-workflow/verification/references/verification-report-template.md '## AC Verification'
require_heading skills/bug-workflow/bug-analysis/references/bug-contract-template.md '## Evidence'
require_heading skills/bug-workflow/bug-reproduction/references/reproduction-report-template.md '## Attempts'
require_heading skills/bug-workflow/bug-root-cause/references/root-cause-report-template.md '## Confirmed Root Cause'
require_heading skills/bug-workflow/bug-fix/references/bug-fix-report-template.md '## Root Cause to Change Mapping'
require_heading skills/bug-workflow/bug-verification/references/bug-verification-report-template.md '## Original Failure Verification'
require_heading skills/code-review-workflow/code-review/references/code-review-report-template.md '## Issues'
require_heading skills/code-review-workflow/fix-code-review/references/fix-code-review-report-template.md '## Issue Disposition'

for script in skills/scripts/validate-skill-system.sh \
  skills/feature-workflow/verification/scripts/changed-files.sh \
  skills/feature-workflow/verification/scripts/related-tests.sh \
  skills/feature-workflow/verification/scripts/verify.sh; do
  require_file "$script"
  if [ -s "$workspace_root/$script" ] && ! bash -n "$workspace_root/$script"; then
    fail "$script: Bash syntax check failed"
  fi
done

require_file skills/evals/build_packet.py
require_file skills/evals/run_behavioral_eval.py
require_file skills/evals/test_build_packet.py
require_file skills/evals/test_validator.py
require_file skills/evals/test_run_behavioral_eval.py
require_file skills/evals/test_native_package.py
require_file skills/scripts/validate_native_package.py
require_file .codex-plugin/plugin.json
require_file .agents/plugins/marketplace.json
require_file .codex/config.toml

if [ "$errors" -ne 0 ]; then
  printf 'FAIL: %d structural error(s).\n' "$errors" >&2
  exit 1
fi

python3 "$workspace_root/skills/scripts/validate_native_package.py" "$workspace_root"

printf 'PASS: workflow routes, Walk It Down contracts, stage contracts, templates, links, evidence rules, and stop conditions validated.\n'
