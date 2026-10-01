"""Run with: python3 -B -m unittest discover -s skills/evals -p 'test_*.py'."""

import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import build_packet


ROOT = Path(__file__).resolve().parents[2]


class PacketTests(unittest.TestCase):
    def test_exact_scope_and_forbidden_file_exclusion(self):
        original_read = Path.read_bytes
        for case_id, (stage, scenario) in build_packet.CASES.items():
            expected = {
                "AGENTS.md", *build_packet.STAGES[stage],
                f"skills/evals/{scenario}",
            }
            expected.add("skills/references/check-evidence.md")
            with self.subTest(case=case_id), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                all_inputs = {"AGENTS.md", "skills/references/check-evidence.md"}
                all_inputs.update(path for paths in build_packet.STAGES.values() for path in paths)
                all_inputs.update(f"skills/evals/case-0{i}.md" for i in range(1, 6))
                for relative in all_inputs:
                    path = root / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    if relative in expected:
                        content = "included:" + relative
                    else:
                        content = "FORBIDDEN_SENTINEL"
                    if relative == f"skills/evals/{scenario}":
                        content += "\n" + "\n".join(
                            old for old, _ in build_packet.SUBSTITUTIONS.get(case_id, ())
                        )
                    path.write_text(content, encoding="utf-8")
                for relative in (
                    "skills/evals/behavioral-evals.md", "skills/README.md", "skills/CHANGELOG.md",
                    "skills/evals/examples.md", "skills/unrelated/SKILL.md",
                ):
                    path = root / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text("FORBIDDEN_SENTINEL", encoding="utf-8")
                reads = []

                def read(path):
                    reads.append(str(path.relative_to(root)))
                    return original_read(path)

                with mock.patch.object(Path, "read_bytes", read):
                    packet, metadata = build_packet.build_packet(root, case_id)
                self.assertEqual(set(reads), expected)
                self.assertEqual(len(reads), len(expected))
                self.assertNotIn("FORBIDDEN_SENTINEL", packet)
                self.assertEqual(set(metadata["source_sha256"]), expected)

    def test_real_variants_and_metadata(self):
        required = {
            "E1-current": ("report v0 on S2", "accessible current-S2 execution evidence"),
            "E2-limit": ("Prior review_cycles=2;", "return amount * 0.02"),
            "E2-gap-only": ("Prior review_cycles=2;", "return amount * 0.20"),
            "E2-approved": ("return amount * 0.20", "def regional_tax(amount):", "return tax(amount)"),
            "E3-authorized": ("Review and fix this access check.",),
        }
        for case_id in build_packet.CASES:
            with self.subTest(case=case_id):
                packet, metadata = build_packet.build_packet(ROOT, case_id)
                for fragment in required.get(case_id, ()):
                    self.assertIn(fragment, packet)
                for old, _ in build_packet.SUBSTITUTIONS.get(case_id, ()):
                    self.assertNotIn(old, packet)
                self.assertEqual(metadata["packet_sha256"], hashlib.sha256(packet.encode()).hexdigest())
                for relative, digest in metadata["source_sha256"].items():
                    self.assertEqual(digest, hashlib.sha256((ROOT / relative).read_bytes()).hexdigest())

    def test_missing_or_ambiguous_substitutions_fail(self):
        for case_id, substitutions in build_packet.SUBSTITUTIONS.items():
            original = (ROOT / "skills/evals" / build_packet.CASES[case_id][1]).read_text()
            for old, _ in substitutions:
                for broken in (original.replace(old, "fixture drift"), original + "\n" + old):
                    with self.subTest(case=case_id, anchor=old), self.assertRaises(ValueError):
                        build_packet.apply_variant(case_id, broken)

    def test_invalid_cases_rejected_before_reading(self):
        for case_id in ("E0", "e1", "../behavioral-evals.md", "/tmp/secret", "E1/../../AGENTS.md"):
            with self.subTest(case=case_id), mock.patch.object(Path, "read_bytes") as read:
                with self.assertRaises(ValueError):
                    build_packet.build_packet(ROOT, case_id)
                read.assert_not_called()
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                build_packet.main(["--case", case_id])
            self.assertEqual(error.exception.code, 2)

    def test_symlink_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            hidden = root / "rubric.md"
            hidden.write_text("FORBIDDEN_SENTINEL")
            (root / "AGENTS.md").symlink_to(hidden)
            with mock.patch.object(Path, "read_bytes") as read, self.assertRaises(ValueError):
                build_packet.build_packet(root, "E1")
            read.assert_not_called()

    def test_cli_keeps_metadata_off_stdout(self):
        for enabled in (False, True):
            stdout, stderr = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                build_packet.main(["--case", "E1"] + (["--metadata"] if enabled else []))
            packet, metadata = build_packet.build_packet(ROOT, "E1")
            self.assertEqual(stdout.getvalue(), packet)
            self.assertEqual(json.loads(stderr.getvalue()) if enabled else stderr.getvalue(),
                             metadata if enabled else "")


if __name__ == "__main__":
    unittest.main()
