"""Regression tests for validator-enforced execution profiles."""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "skills/scripts/validate-skill-system.sh"
PROFILE = Path("skills/project-discovery/SKILL.md")


class ExecutionProfileValidationTests(unittest.TestCase):
    def run_validator(self, root):
        return subprocess.run(
            ["bash", str(VALIDATOR), str(root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def copy_workspace(self, destination):
        shutil.copy2(ROOT / "AGENTS.md", destination / "AGENTS.md")
        shutil.copytree(
            ROOT / "skills",
            destination / "skills",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    def test_current_profiles_pass(self):
        result = self.run_validator(ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_start_class_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            profile = root / PROFILE
            text = profile.read_text(encoding="utf-8")
            profile.write_text(
                text.replace("- `START_CLASS`: ECONOMY", "- `START`: ECONOMY", 1),
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("execution profile requires", result.stderr)

    def test_placeholder_escalation_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            profile = root / PROFILE
            text = profile.read_text(encoding="utf-8")
            start = text.index("- `ESCALATE_WHEN`:")
            end = text.index("\n", start)
            profile.write_text(
                text[:start] + "- `ESCALATE_WHEN`: placeholder: decide later" + text[end:],
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("execution profile requires", result.stderr)

    def test_duplicate_profile_field_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            profile = root / PROFILE
            text = profile.read_text(encoding="utf-8")
            profile.write_text(
                text.replace(
                    "- `START_CLASS`: ECONOMY",
                    "- `START_CLASS`: ECONOMY\n- `START_CLASS`: STANDARD",
                    1,
                ),
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("execution profile requires", result.stderr)


if __name__ == "__main__":
    unittest.main()
