#!/usr/bin/env bash
# Print newline-delimited tracked and untracked changes without modifying the repo.
set -eu

if [ "$#" -gt 2 ]; then
  printf 'Usage: bash %s [repository-root] [base-ref]\n' "$0" >&2
  exit 2
fi

repo_root=${1:-.}
base_ref=${2:-HEAD}

if [ ! -d "$repo_root" ]; then
  printf 'ERROR: repository directory does not exist: %s\n' "$repo_root" >&2
  exit 2
fi
repo_root=$(CDPATH= cd -- "$repo_root" && pwd)

if ! git -C "$repo_root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'ERROR: not a Git worktree: %s\n' "$repo_root" >&2
  exit 2
fi

if git -C "$repo_root" rev-parse --verify --quiet "${base_ref}^{commit}" >/dev/null; then
  tracked_command=diff
else
  if [ "$base_ref" != HEAD ]; then
    printf 'ERROR: base ref is not a commit: %s\n' "$base_ref" >&2
    exit 2
  fi
  tracked_command=initial
fi

if [ "$tracked_command" = diff ]; then
  {
    git -C "$repo_root" diff --name-only "$base_ref" --
    git -C "$repo_root" ls-files --others --exclude-standard
  } | LC_ALL=C sort -u
else
  {
    git -C "$repo_root" ls-files --cached
    git -C "$repo_root" ls-files --others --exclude-standard
  } | LC_ALL=C sort -u
fi
