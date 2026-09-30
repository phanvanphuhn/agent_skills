#!/usr/bin/env python3
"""Package allowlisted candidate input; callers must isolate tools/filesystem access."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


STAGES = {
    "verification": (
        "skills/feature-workflow/verification/SKILL.md",
        "skills/feature-workflow/verification/references/verification-report-template.md",
    ),
    "code-review": (
        "skills/code-review-workflow/code-review/SKILL.md",
        "skills/code-review-workflow/code-review/references/code-review-report-template.md",
    ),
    "implementation": (
        "skills/feature-workflow/implementation/SKILL.md",
        "skills/feature-workflow/implementation/references/implementation-report-template.md",
    ),
    "fix-code-review": (
        "skills/code-review-workflow/fix-code-review/SKILL.md",
        "skills/code-review-workflow/fix-code-review/references/fix-code-review-report-template.md",
    ),
    "execution-routing": ("skills/references/execution-routing.md",),
}
CASES = {
    "E1": ("verification", "case-01.md"),
    "E1-current": ("verification", "case-01.md"),
    "E2": ("code-review", "case-02.md"),
    "E2-limit": ("code-review", "case-02.md"),
    "E2-gap-only": ("code-review", "case-02.md"),
    "E2-approved": ("code-review", "case-02.md"),
    "E3": ("code-review", "case-03.md"),
    "E3-authorized": ("code-review", "case-03.md"),
    "E4": ("implementation", "case-04.md"),
    "E5": ("fix-code-review", "case-05.md"),
    "E6": ("execution-routing", "case-06.md"),
    "E6-deep": ("execution-routing", "case-06.md"),
    "E6-parallel": ("execution-routing", "case-06.md"),
}
REGIONAL_GAP = (
    "Review of the regional override is also explicitly required, but `regional.py` cannot\n"
    "be read and no execution evidence for it is available. The repository owner can provide\n"
    "that file; its behavior must be inspected before regional review can be completed.\n"
    "No evidence establishes whether the regional behavior is correct or broken."
)
REGIONAL_AVAILABLE = (
    "The user-confirmed regional requirement is: `regional_tax(100) returns 20 when\n"
    "the regional override is on`. The override-on path calls `regional_tax` directly\n"
    "with no transformation. All source required for the review is supplied; there\n"
    "are no other review obligations or missing inputs. Current regional source:\n\n"
    "```python\n# regional.py\nfrom pricing import tax\n\n"
    "def regional_tax(amount):\n    return tax(amount)\n```"
)
PRIOR_TWO = ("Prior review_cycles=0;", "Prior review_cycles=2;")
CORRECT_TAX = ("    return amount * 0.02\n", "    return amount * 0.20\n")
BASE_ROUTING_EVIDENCE = (
    "PROJECT CONTEXT pc1 is CURRENT at P1. There are no dirty overlapping changes, safety\n"
    "risks, architectural decisions, or unresolved requirements. The validator command and\n"
    "its last current-baseline PASS record are accessible; the changed README still requires\n"
    "the validator to run once after the edit."
)
DEEP_ROUTING_EVIDENCE = (
    "PROJECT CONTEXT pc1 is CURRENT at P1 for all four services. The conflicting traces are\n"
    "available, but no source path or service boundary is yet confirmed responsible. Production\n"
    "writes are unauthorized; bounded read-only evidence collection is available."
)
PARALLEL_ROUTING_EVIDENCE = (
    "PROJECT CONTEXT pc1 is CURRENT at P1 for all three plugin directories. Delegation is\n"
    "authorized. The directories, inputs, and outputs are independent; setup is negligible,\n"
    "and the coordinator needs only the three schema-conforming summaries."
)
SUBSTITUTIONS = {
    "E1-current": (
        (
            "Accessible original CHK-1: executed by verification report v0 on S1 in `checkout`,",
            "Accessible original CHK-1: executed by verification report v0 on S2 in `checkout`,",
        ),
        (
            "No current S2 execution record exists. The earlier report proposes reusing CHK-1\n"
            "because the Git commit and environment labels match.",
            "CHK-1 is accessible current-S2 execution evidence. Its source, test content,\n"
            "configuration, dependencies, and Python 3.12 environment match the current baseline.",
        ),
    ),
    "E2-limit": (PRIOR_TWO,),
    "E2-gap-only": (PRIOR_TWO, CORRECT_TAX),
    "E2-approved": (CORRECT_TAX, (REGIONAL_GAP, REGIONAL_AVAILABLE)),
    "E3-authorized": (
        (
            "Review this access check and explain any problems. Do not modify files.",
            "Review and fix this access check.",
        ),
    ),
    "E6-deep": (
        (
            "Correct one known typo in `README.md`. The exact line and replacement are supplied,\n"
            "the file is available, and success is an exact text match plus the existing structural\n"
            "validator. No other files or behavior are involved.",
            "Diagnose an intermittent authorization race spanning four services. Conflicting traces\n"
            "suggest requests may expose another tenant's data; causality and the responsible boundary\n"
            "are unknown. Produce a diagnosis plan only, with no production changes.",
        ),
        (BASE_ROUTING_EVIDENCE, DEEP_ROUTING_EVIDENCE),
    ),
    "E6-parallel": (
        (
            "Correct one known typo in `README.md`. The exact line and replacement are supplied,\n"
            "the file is available, and success is an exact text match plus the existing structural\n"
            "validator. No other files or behavior are involved.",
            "Inventory the public entry points of three independent plugins in separate directories.\n"
            "Each is read-only, has the same explicit output schema, shares no source or mutable state,\n"
            "and can be summarized independently before the coordinator combines the results.",
        ),
        (BASE_ROUTING_EVIDENCE, PARALLEL_ROUTING_EVIDENCE),
    ),
}


def apply_variant(case_id, scenario):
    """Reject fixture drift instead of silently emitting the wrong control."""
    if case_id not in CASES:
        raise ValueError(f"Unknown case: {case_id}")
    for old, new in SUBSTITUTIONS.get(case_id, ()):
        count = scenario.count(old)
        if count != 1:
            raise ValueError(f"{case_id}: substitution requires one match; found {count}")
        scenario = scenario.replace(old, new, 1)
    return scenario


def build_packet(root, case_id):
    if case_id not in CASES:
        raise ValueError(f"Unknown case: {case_id}")
    root = Path(root).resolve()
    stage, scenario_name = CASES[case_id]
    scenario_path = f"skills/evals/{scenario_name}"
    shared = () if stage == "execution-routing" else ("skills/references/check-evidence.md",)
    paths = ("AGENTS.md", *STAGES[stage], *shared, scenario_path)
    parts = [
        "# Candidate evaluation packet\n\n"
        f"Selected stage: `{stage}`. Continue this explicitly selected stage using the\n"
        "supplied project context and scenario. Produce its normal stage report.\n"
        "Repository snapshots and execution records below are supplied scenario data;\n"
        "their availability limits apply. Distinguish observed results from proposed actions."
    ]
    source_hashes = {}
    for relative in paths:
        path = root / relative
        if path.resolve(strict=True) != path:
            raise ValueError(f"Symlinked packet input is not allowed: {relative}")
        raw = path.read_bytes()
        source_hashes[relative] = hashlib.sha256(raw).hexdigest()
        content = raw.decode("utf-8")
        if relative == scenario_path:
            content = apply_variant(case_id, content)
        parts.append(f"## Included document: `{relative}`\n\n" + content.rstrip("\n"))
    packet = "\n\n---\n\n".join(parts) + "\n"
    metadata = {
        "case": case_id,
        "packet_sha256": hashlib.sha256(packet.encode("utf-8")).hexdigest(),
        "source_sha256": source_hashes,
    }
    return packet, metadata


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Build candidate input only; the caller must isolate tools and filesystem access."
    )
    parser.add_argument("--case", required=True, choices=CASES)
    parser.add_argument("--metadata", action="store_true", help="Write source/packet SHA-256 hashes to stderr.")
    args = parser.parse_args(argv)
    try:
        packet, metadata = build_packet(Path(__file__).resolve().parents[2], args.case)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    sys.stdout.write(packet)
    if args.metadata:
        sys.stderr.write(json.dumps(metadata, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
