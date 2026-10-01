#!/usr/bin/env bash
# Build a narrow verification manifest, then optionally run one explicit command.
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=.
base_ref=HEAD

while [ "$#" -gt 0 ]; do
  case "$1" in
    --repo)
      [ "$#" -ge 2 ] || { printf 'ERROR: --repo requires a path\n' >&2; exit 2; }
      repo_root=$2
      shift 2
      ;;
    --base)
      [ "$#" -ge 2 ] || { printf 'ERROR: --base requires a ref\n' >&2; exit 2; }
      base_ref=$2
      shift 2
      ;;
    --)
      shift
      break
      ;;
    -h|--help)
      printf 'Usage: bash %s [--repo PATH] [--base REF] [-- command args...]\n' "$0"
      exit 0
      ;;
    *)
      printf 'ERROR: unknown argument: %s\n' "$1" >&2
      exit 2
      ;;
  esac
done

if [ ! -d "$repo_root" ]; then
  printf 'ERROR: repository directory does not exist: %s\n' "$repo_root" >&2
  exit 2
fi
repo_root=$(CDPATH= cd -- "$repo_root" && pwd)

printf 'Repository: %s\n' "$repo_root"
printf 'Base: %s\n' "$base_ref"
printf '\nChanged files:\n'
bash "$script_dir/changed-files.sh" "$repo_root" "$base_ref"
printf '\nName-based related test candidates:\n'
bash "$script_dir/related-tests.sh" "$repo_root" "$base_ref"

if [ "$#" -eq 0 ]; then
  printf '\nNo check command executed. Select commands from the READY contract, repository policy, and risk.\n'
  exit 0
fi

printf '\nExecuting explicit check:'
printf ' %q' "$@"
printf '\n'
(
  cd "$repo_root"
  "$@"
)
