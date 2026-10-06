"""Regression tests for Codex-native skill package exposure."""

import json
from pathlib import Path
import shutil
import tempfile
import unittest

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_native_package


ROOT = Path(__file__).resolve().parents[2]


class NativePackageTests(unittest.TestCase):
    def copy_package(self, destination):
        shutil.copytree(ROOT / ".codex-plugin", destination / ".codex-plugin")
        shutil.copytree(ROOT / ".agents", destination / ".agents")
        shutil.copytree(ROOT / ".codex", destination / ".codex")
        shutil.copytree(ROOT / "skills", destination / "skills")

    def test_current_package_exposes_all_skills_once(self):
        self.assertEqual(validate_native_package.validate(ROOT), [])

    def test_missing_workflow_root_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            manifest_path = root / ".codex-plugin/plugin.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["skills"].remove("./skills/bug-workflow/")
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            errors = validate_native_package.validate(root)
            self.assertTrue(any("skills not exposed" in error for error in errors))

    def test_duplicate_root_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            manifest_path = root / ".codex-plugin/plugin.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["skills"].append("./skills/feature-workflow/")
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            errors = validate_native_package.validate(root)
            self.assertTrue(any("exposed more than once" in error for error in errors))

    def test_disconnected_marketplace_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            marketplace_path = root / ".agents/plugins/marketplace.json"
            marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
            marketplace["plugins"][0]["source"]["path"] = "./plugins/other"
            marketplace_path.write_text(json.dumps(marketplace), encoding="utf-8")
            errors = validate_native_package.validate(root)
            self.assertTrue(any("repository-root" in error for error in errors))

    def test_disabled_project_plugin_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_package(root)
            (root / ".codex/config.toml").write_text(
                '[plugins."agent-skills@agent-skills-local"]\nenabled = false\n',
                encoding="utf-8",
            )
            errors = validate_native_package.validate(root)
            self.assertTrue(any("must enable" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
