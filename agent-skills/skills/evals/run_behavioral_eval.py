#!/usr/bin/env python3
"""Run one isolated-input Codex decision probe and capture trace metrics."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import build_packet


def parse_events(stdout):
    events = []
    for number, line in enumerate(stdout.splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid JSONL event at line {number}: {error}") from error
    return events


def extract_metrics(events):
    usage = {}
    final_response = None
    commands = []
    for event in events:
        if event.get("type") == "turn.completed":
            usage = event.get("usage") or event.get("turn", {}).get("usage") or usage
        item = event.get("item") or {}
        if item.get("type") == "command_execution" and item.get("command"):
            commands.append(item["command"])
        if item.get("type") == "agent_message" and item.get("text"):
            final_response = item["text"]
    return usage, commands, final_response


def get_baseline(root):
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=False
    )
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=root, capture_output=True, text=True, check=False
    )
    if revision.returncode or status.returncode:
        return "UNKNOWN"
    suffix = "+dirty" if status.stdout.strip() else "+clean"
    return revision.stdout.strip() + suffix


def run_case(root, case_id, model=None, codex="codex"):
    baseline = get_baseline(root)
    packet, metadata = build_packet.build_packet(root, case_id)
    with tempfile.TemporaryDirectory(prefix="skill-eval-") as directory:
        command = [
            codex,
            "--ask-for-approval",
            "never",
            "exec",
            "--json",
            "--ephemeral",
            "--ignore-user-config",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--cd",
            directory,
        ]
        if model:
            command.extend(("--model", model))
        command.append("-")
        started = time.monotonic()
        result = subprocess.run(command, input=packet, capture_output=True, text=True, check=False)
        latency = time.monotonic() - started
    events = parse_events(result.stdout)
    usage, commands, response = extract_metrics(events)
    return {
        "case": case_id,
        "skill_baseline": baseline,
        "model": model or "client-default",
        "packet_sha256": metadata["packet_sha256"],
        "exit_code": result.returncode,
        "latency_seconds": round(latency, 3),
        "usage": usage or "UNKNOWN",
        "command_count": len(commands),
        "commands": commands,
        "response": response,
        "isolation": "ISOLATION_UNVERIFIED",
        "isolation_note": (
            "Fresh ephemeral read-only working directory; trace must be checked for "
            "unexpected access before grading."
        ),
        "stderr": result.stderr,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Run one fresh-context Codex behavioral case and emit measured JSON."
    )
    parser.add_argument("--case", required=True, choices=build_packet.CASES)
    parser.add_argument("--model", help="Explicit candidate model; omit to use the client default.")
    parser.add_argument("--output", type=Path, help="Optional JSON result path.")
    args = parser.parse_args(argv)
    try:
        result = run_case(Path(__file__).resolve().parents[2], args.case, args.model)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0 if result["exit_code"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
