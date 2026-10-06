#!/usr/bin/env bash
# Print conservative name-based test candidates for the current Git changes.
set -eu

if [ "$#" -gt 2 ]; then
  printf 'Usage: bash %s [repository-root] [base-ref]\n' "$0" >&2
  exit 2
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=${1:-.}
base_ref=${2:-HEAD}

if [ ! -d "$repo_root" ]; then
  printf 'ERROR: repository directory does not exist: %s\n' "$repo_root" >&2
  exit 2
fi
repo_root=$(CDPATH= cd -- "$repo_root" && pwd)

temp_dir=$(mktemp -d "${TMPDIR:-/tmp}/related-tests.XXXXXX")
trap 'rm -rf "$temp_dir"' EXIT HUP INT TERM
changed_file="$temp_dir/changed"
tests_file="$temp_dir/tests"
matches_file="$temp_dir/matches"

bash "$script_dir/changed-files.sh" "$repo_root" "$base_ref" > "$changed_file"

if command -v rg >/dev/null 2>&1; then
  if (cd "$repo_root" && rg --files \
      -g '*.spec.*' -g '*.test.*' -g '*_test.*' -g 'test_*.*' \
      -g '**/__tests__/**' -g 'test/**' -g 'tests/**') > "$tests_file"; then
    :
  else
    status=$?
    [ "$status" -eq 1 ] || exit "$status"
  fi
else
  git -C "$repo_root" ls-files | awk '
    /(^|\/)__tests__\// || /(^|\/)(test|tests)\// ||
    /[.]spec[.]/ || /[.]test[.]/ || /_test[.]/ || /(^|\/)test_[^/]+[.]/
  ' > "$tests_file"
fi
: > "$matches_file"

normalize_name() {
  local value name
  value=$1
  name=${value##*/}
  name=${name%.*}
  name=${name%.spec}
  name=${name%.test}
  name=${name%_test}
  name=${name#test_}
  printf '%s\n' "$name"
}

is_test_path() {
  case "$1" in
    */__tests__/*|test/*|tests/*|*/test/*|*/tests/*|*.spec.*|*.test.*|*_test.*|test_*.*) return 0 ;;
    *) return 1 ;;
  esac
}

while IFS= read -r changed; do
  [ -n "$changed" ] || continue
  if is_test_path "$changed" && [ -f "$repo_root/$changed" ]; then
    printf '%s\n' "$changed" >> "$matches_file"
    continue
  fi
  changed_name=$(normalize_name "$changed")
  while IFS= read -r test_path; do
    [ -n "$test_path" ] || continue
    test_name=$(normalize_name "$test_path")
    if [ "$test_name" = "$changed_name" ]; then
      printf '%s\n' "$test_path" >> "$matches_file"
    fi
  done < "$tests_file"
done < "$changed_file"

LC_ALL=C sort -u "$matches_file"
