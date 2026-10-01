"""Regression tests for contract-first skill validation."""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "skills/scripts/validate-skill-system.sh"
SKILL = Path("skills/project-discovery/SKILL.md")


class ContractValidationTests(unittest.TestCase):
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

    def test_current_contracts_pass(self):
        result = self.run_validator(ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_required_outcome_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            skill = root / SKILL
            text = skill.read_text(encoding="utf-8")
            skill.write_text(
                text.replace("## Required outcome", "## Result", 1),
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing heading '## Required outcome'", result.stderr)

    def test_execution_profile_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            skill = root / SKILL
            text = skill.read_text(encoding="utf-8")
            skill.write_text(
                text + "\n## Execution routing\n\n- `START_CLASS`: ECONOMY\n",
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("removed prescriptive guidance", result.stderr)

    def test_context_ladder_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            skill = root / SKILL
            text = skill.read_text(encoding="utf-8")
            skill.write_text(text + "\nL0 then L1 then L2\n", encoding="utf-8")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("context-level ladder", result.stderr)

    def test_prescriptive_agents_guidance_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            agents = root / "AGENTS.md"
            text = agents.read_text(encoding="utf-8")
            agents.write_text(
                text + "\n## Execution routing\n\n- `START_CLASS`: STANDARD\n",
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("removed prescriptive guidance", result.stderr)

    def test_unregistered_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_workspace(root)
            skill = root / "skills/unregistered/SKILL.md"
            skill.parent.mkdir()
            skill.write_text(
                '---\nname: unregistered\ndescription: "Unexpected skill."\n---\n',
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("unregistered SKILL.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
