"""Regression tests for Claude Code plugin packaging and eval-suite structure."""

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_claude_package


ROOT = Path(__file__).resolve().parents[2]


class ClaudePackageTests(unittest.TestCase):
    def copy_package(self, destination):
        for name in (".claude-plugin", "agents", "skills", "evals"):
            shutil.copytree(
                ROOT / name,
                destination / name,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "results"),
            )

    def edit_json(self, path, change):
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_current_package_is_valid(self):
        self.assertEqual(validate_claude_package.validate(ROOT), [])

    def test_listing_default_skills_root_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            self.edit_json(root / ".claude-plugin/plugin.json",
                           lambda data: data["skills"].append("./skills/"))
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("by default" in error for error in errors))

    def test_missing_workflow_root_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            self.edit_json(root / ".claude-plugin/plugin.json",
                           lambda data: data["skills"].remove("./skills/bug-workflow/"))
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("not exposed to Claude" in error for error in errors))

    def test_invalid_version_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            self.edit_json(root / ".claude-plugin/plugin.json",
                           lambda data: data.update(version="next"))
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("MAJOR.MINOR.PATCH" in error for error in errors))

    def test_skill_without_trigger_case_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            shutil.rmtree(root / "evals/comment-asks-for-scope")
            shutil.rmtree(root / "evals/comment-named-file")
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("without a Claude trigger case: comment" in error for error in errors))

    def test_prompt_naming_skill_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            prompt = root / "evals/bug-report-intake/prompt.md"
            prompt.write_text(prompt.read_text(encoding="utf-8") + "\nUse bug-analysis.\n",
                              encoding="utf-8")
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("names skill bug-analysis" in error for error in errors))

    def test_unknown_prompt_key_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            prompt = root / "evals/bug-report-intake/prompt.md"
            text = prompt.read_text(encoding="utf-8")
            prompt.write_text(text.replace("max_turns:", "turns:", 1), encoding="utf-8")
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("unknown frontmatter keys" in error for error in errors))

    def test_ambiguous_skill_grader_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            grader = root / "evals/bug-report-intake/graders/skill-fired.md"
            grader.write_text(
                "---\ntype: tool_used\ntool: Skill\ninput_match: 'bug-'\n---\n",
                encoding="utf-8",
            )
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("exactly one skill" in error for error in errors))

    def test_unknown_grader_type_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            grader = root / "evals/bug-report-intake/graders/criteria.md"
            grader.write_text("---\ntype: script\n---\nPASS if ok. FAIL if not.\n",
                              encoding="utf-8")
            errors = validate_claude_package.validate(root)
            self.assertTrue(any("unknown grader type" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
