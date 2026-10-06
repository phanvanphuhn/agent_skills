#!/usr/bin/env python3
"""Validate that the Codex plugin manifest exposes every repository skill once."""

import json
from pathlib import Path
import sys
import tomllib


def validate(root):
    root = Path(root).resolve()
    manifest_path = root / ".codex-plugin/plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    marketplace = json.loads(
        (root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8")
    )
    config = tomllib.loads((root / ".codex/config.toml").read_text(encoding="utf-8"))
    errors = []
    if manifest.get("name") != "agent-skills":
        errors.append("plugin name must be agent-skills")
    entries = marketplace.get("plugins", [])
    if marketplace.get("name") != "agent-skills-local" or len(entries) != 1:
        errors.append("marketplace must contain one agent-skills-local entry")
    else:
        entry = entries[0]
        if entry.get("name") != "agent-skills" or entry.get("source") != {
            "source": "local", "path": "./"
        }:
            errors.append("marketplace entry must expose the repository-root agent-skills plugin")
    enabled = config.get("plugins", {}).get("agent-skills@agent-skills-local", {}).get("enabled")
    if enabled is not True:
        errors.append("repository Codex config must enable agent-skills@agent-skills-local")
    roots = manifest.get("skills")
    if not isinstance(roots, list) or not roots:
        errors.append("plugin skills must be a non-empty array")
        roots = []

    exposed = []
    for relative in roots:
        if not isinstance(relative, str) or not relative.startswith("./"):
            errors.append(f"invalid relative skill root: {relative!r}")
            continue
        directory = (root / relative).resolve()
        try:
            directory.relative_to(root)
        except ValueError:
            errors.append(f"skill root escapes package: {relative}")
            continue
        if not directory.is_dir():
            errors.append(f"skill root is missing: {relative}")
            continue
        exposed.extend(path.resolve() for path in directory.glob("*/SKILL.md"))

    expected = sorted(path.resolve() for path in (root / "skills").rglob("SKILL.md"))
    duplicates = sorted({path for path in exposed if exposed.count(path) > 1})
    if duplicates:
        errors.append(
            "skills exposed more than once: "
            + ", ".join(str(path.relative_to(root)) for path in duplicates)
        )
    missing = sorted(set(expected) - set(exposed))
    extra = sorted(set(exposed) - set(expected))
    if missing:
        errors.append("skills not exposed: " + ", ".join(str(path.relative_to(root)) for path in missing))
    if extra:
        errors.append("unexpected exposed skills: " + ", ".join(str(path.relative_to(root)) for path in extra))
    return errors


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    root = Path(args[0]) if args else Path(__file__).resolve().parents[2]
    try:
        errors = validate(root)
    except (OSError, UnicodeError, json.JSONDecodeError, tomllib.TOMLDecodeError) as error:
        errors = [str(error)]
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: Codex plugin manifest exposes every registered skill exactly once.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
