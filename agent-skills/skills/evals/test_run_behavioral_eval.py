"""Regression tests for measured Codex behavioral runs."""

import json
from pathlib import Path
import subprocess
import unittest
from unittest import mock

import run_behavioral_eval


ROOT = Path(__file__).resolve().parents[2]


class BehavioralRunnerTests(unittest.TestCase):
    def test_parse_metrics(self):
        events = [
            {"type": "item.completed", "item": {"type": "command_execution", "command": "pwd"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "BLOCKED"}},
            {"type": "turn.completed", "usage": {"input_tokens": 12, "output_tokens": 3}},
        ]
        usage, commands, response = run_behavioral_eval.extract_metrics(events)
        self.assertEqual(usage, {"input_tokens": 12, "output_tokens": 3})
        self.assertEqual(commands, ["pwd"])
        self.assertEqual(response, "BLOCKED")

    @mock.patch("run_behavioral_eval.get_baseline", return_value="abc123+dirty")
    @mock.patch("run_behavioral_eval.subprocess.run")
    def test_run_uses_fresh_read_only_ephemeral_context(self, execute, baseline):
        execute.return_value = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout="\n".join((
                json.dumps({"type": "item.completed", "item": {"type": "agent_message", "text": "ok"}}),
                json.dumps({"type": "turn.completed", "usage": {"input_tokens": 10, "output_tokens": 1}}),
            )),
            stderr="",
        )
        result = run_behavioral_eval.run_case(ROOT, "E4", model="candidate-model")
        command = execute.call_args.args[0]
        self.assertEqual(command[1:4], ["--ask-for-approval", "never", "exec"])
        self.assertIn("--ephemeral", command)
        self.assertIn("--ignore-user-config", command)
        self.assertIn("read-only", command)
        self.assertEqual(command[-3:], ["--model", "candidate-model", "-"])
        self.assertIn("# Candidate evaluation packet", execute.call_args.kwargs["input"])
        self.assertEqual(result["usage"]["input_tokens"], 10)
        self.assertEqual(result["response"], "ok")
        self.assertEqual(result["skill_baseline"], "abc123+dirty")
        self.assertEqual(result["isolation"], "ISOLATION_UNVERIFIED")
        baseline.assert_called_once_with(ROOT)

    def test_invalid_jsonl_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "line 2"):
            run_behavioral_eval.parse_events('{}\nnot-json\n')


if __name__ == "__main__":
    unittest.main()
