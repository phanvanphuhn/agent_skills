#!/usr/bin/env python3
"""Validate the Claude Code plugin manifest, subagents, and plugin eval suite offline."""

import json
from pathlib import Path
import re
import subprocess
import sys

PLUGIN_NAME = "agent-skills"
PROMPT_KEYS = {
    "schema_version", "name", "description", "tags", "plugins", "runs",
    "expected_outcome", "model", "max_turns", "timeout_seconds", "allowed_tools",
    "append_system_prompt", "env",
}
GRADER_KEYS = {
    "regex": {"pattern", "flags", "match", "target"},
    "tool_used": {"tool", "input_match", "min", "max"},
    "tool_order": {"before", "after"},
    "file_exists": {"path", "exists"},
    "llm": {"criteria", "focus"},
    "baseline": {"baseline_file", "criteria"},
}
COMMON_GRADER_KEYS = {"type", "weight", "arm"}
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


def parse_frontmatter(text):
    match = FRONTMATTER.match(text)
    if not match:
        return None, text
    fields = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = parse_value(value.strip())
    return fields, match.group(2)


def parse_value(value):
    if value.startswith("[") and value.endswith("]"):
        return [item.strip() for item in value[1:-1].split(",") if item.strip()]
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def skill_names(root):
    return sorted(path.parent.name for path in (root / "skills").rglob("SKILL.md"))


def validate_manifest(root, errors):
    manifest = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if manifest.get("name") != PLUGIN_NAME:
        errors.append(f"Claude plugin name must be {PLUGIN_NAME}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        errors.append("Claude plugin version must be MAJOR.MINOR.PATCH")

    exposed = [path.resolve() for path in (root / "skills").glob("*/SKILL.md")]
    for relative in manifest.get("skills", []):
        if not isinstance(relative, str) or not relative.startswith("./"):
            errors.append(f"invalid Claude skill root: {relative!r}")
            continue
        directory = (root / relative).resolve()
        if directory == (root / "skills").resolve():
            errors.append("Claude scans ./skills/ by default; listing it exposes skills twice")
            continue
        if not directory.is_dir() or root.resolve() not in directory.parents:
            errors.append(f"Claude skill root is missing or outside the package: {relative}")
            continue
        exposed.extend(path.resolve() for path in directory.glob("*/SKILL.md"))
    expected = {path.resolve() for path in (root / "skills").rglob("SKILL.md")}
    duplicates = sorted({path for path in exposed if exposed.count(path) > 1})
    if duplicates:
        errors.append("Claude exposes skills more than once: "
                      + ", ".join(str(path.relative_to(root)) for path in duplicates))
    missing = sorted(expected - set(exposed))
    if missing:
        errors.append("skills not exposed to Claude: "
                      + ", ".join(str(path.relative_to(root)) for path in missing))

    for relative in manifest.get("agents", []):
        path = root / relative
        if not relative.startswith("./") or path.suffix != ".md" or not path.is_file():
            errors.append(f"Claude agent entry must be an existing ./*.md file: {relative}")
            continue
        fields, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not fields or not fields.get("name") or not fields.get("description") or not body.strip():
            errors.append(f"{relative}: agent needs name, description, and instructions")

    marketplace = json.loads(
        (root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
    )
    entries = marketplace.get("plugins", [])
    if len(entries) != 1 or entries[0].get("name") != PLUGIN_NAME or entries[0].get("source") != "./":
        errors.append("Claude marketplace must list agent-skills once with source ./")


def compile_pattern(pattern, flags, where, errors):
    try:
        return re.compile(pattern, re.I if "i" in str(flags or "") else 0)
    except re.error as error:
        errors.append(f"{where}: regex does not compile: {error}")
        return None


def validate_grader(root, path, errors):
    where = str(path.relative_to(root))
    fields, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fields is None:
        errors.append(f"{where}: grader needs YAML frontmatter")
        return None
    kind = fields.get("type")
    if kind not in GRADER_KEYS:
        errors.append(f"{where}: unknown grader type {kind!r}")
        return None
    unknown = set(fields) - COMMON_GRADER_KEYS - GRADER_KEYS[kind]
    if unknown:
        errors.append(f"{where}: unknown grader keys {sorted(unknown)}")
    if fields.get("arm") not in (None, "with-only", "both"):
        errors.append(f"{where}: arm must be with-only or both")
    if kind == "tool_used" and not fields.get("tool"):
        errors.append(f"{where}: tool_used grader needs tool")
    if kind == "regex":
        if not fields.get("pattern"):
            errors.append(f"{where}: regex grader needs pattern")
        else:
            compile_pattern(fields["pattern"], fields.get("flags"), where, errors)
    if kind == "llm" and not (body.strip() or fields.get("criteria")):
        errors.append(f"{where}: llm grader needs PASS/FAIL criteria")
    if kind == "llm" and body.strip() and not ("PASS" in body and "FAIL" in body):
        errors.append(f"{where}: llm rubric must state PASS and FAIL conditions")
    if kind == "tool_used" and fields.get("input_match"):
        fields["_compiled"] = compile_pattern(fields["input_match"], None, where, errors)
    return fields


def fired_skills(grader, names):
    pattern = grader.get("_compiled")
    if not pattern:
        return set()
    return {
        name for name in names
        if pattern.search(json.dumps({"skill": f"{PLUGIN_NAME}:{name}"}))
        and pattern.search(json.dumps({"skill": name}))
    }


def validate_evals(root, errors):
    suite = root / "evals"
    names = skill_names(root)
    hyphenated = [name for name in names if "-" in name]
    covered = set()
    cases = sorted(
        path for path in suite.rglob("*")
        if path.is_dir() and "results" not in path.relative_to(suite).parts
        and ((path / "prompt.md").is_file() or (path / "case.yaml").is_file())
    )
    if not cases:
        errors.append("evals/: no Claude eval cases found")
    seen = set()
    for case in cases:
        where = str(case.relative_to(root))
        if case.name in seen:
            errors.append(f"{where}: duplicate case name")
        seen.add(case.name)

        prompt_path = case / "prompt.md"
        if not prompt_path.is_file():
            errors.append(f"{where}: missing prompt.md")
            continue
        fields, body = parse_frontmatter(prompt_path.read_text(encoding="utf-8"))
        fields = fields or {}
        unknown = set(fields) - PROMPT_KEYS
        if unknown:
            errors.append(f"{where}/prompt.md: unknown frontmatter keys {sorted(unknown)}")
        if not body.strip():
            errors.append(f"{where}/prompt.md: empty prompt")
        for name in hyphenated:
            if re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", body):
                errors.append(f"{where}/prompt.md: prompt names skill {name}; phrase it as a user would")
        if not isinstance(fields.get("allowed_tools", []), list):
            errors.append(f"{where}/prompt.md: allowed_tools must be a list")
        max_turns = fields.get("max_turns", 10)
        if not isinstance(max_turns, int) or not 1 <= max_turns <= 200:
            errors.append(f"{where}/prompt.md: max_turns must be 1-200")

        case_yaml = case / "case.yaml"
        if case_yaml.is_file():
            text = case_yaml.read_text(encoding="utf-8")
            if 'schema_version: "1.1"' not in text or f"name: {case.name}" not in text:
                errors.append(f"{where}/case.yaml: needs schema_version \"1.1\" and name {case.name}")
            script = re.search(r"scaffold_script:\s*(\S+)", text)
            if script:
                script_path = case / script.group(1)
                if not script_path.is_file():
                    errors.append(f"{where}: scaffold script {script.group(1)} is missing")
                elif subprocess.run(["bash", "-n", str(script_path)], check=False).returncode:
                    errors.append(f"{where}: scaffold script fails bash -n")

        graders = sorted((case / "graders").glob("*.md"))
        if not graders:
            errors.append(f"{where}: case needs at least one grader")
        for grader_path in graders:
            grader = validate_grader(root, grader_path, errors)
            if not grader or grader.get("type") != "tool_used" or grader.get("tool") != "Skill":
                continue
            if grader.get("max") == 0:
                continue
            matched = fired_skills(grader, names)
            if len(matched) != 1:
                errors.append(f"{grader_path.relative_to(root)}: skill grader must match exactly one skill, got {sorted(matched)}")
            covered |= matched

    uncovered = sorted(set(names) - covered)
    if uncovered:
        errors.append("skills without a Claude trigger case: " + ", ".join(uncovered))


def validate(root):
    root = Path(root).resolve()
    errors = []
    validate_manifest(root, errors)
    validate_evals(root, errors)
    return errors


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    root = Path(args[0]) if args else Path(__file__).resolve().parents[2]
    try:
        errors = validate(root)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        errors = [str(error)]
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: Claude plugin manifest, subagents, and eval suite are structurally valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
