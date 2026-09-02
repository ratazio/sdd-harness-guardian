#!/usr/bin/env python3
"""Validate the bounded integrity envelope of a human semantic review.

This is deliberately *not* a semantic-review engine.  It checks only the
reviewer-declared identity, files, locators/scopes and SHA-256 values in a
record.  In particular, a structurally valid ``APPROVE`` is not an approval
decision made by this program; the human verdict remains evidence for a
separate evaluator to consider.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "contract_version", "record_scope", "composer_identity", "reviewer_identity",
    "candidate", "rendered", "corpus_manifest", "human_verdict",
}
REQUIRED_BINDING = {"path", "locator", "sha256"}


def fail(message: str) -> None:
    raise ValueError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_file(root: Path, declared: object, label: str) -> Path:
    if not isinstance(declared, str) or not declared or Path(declared).is_absolute():
        fail(f"{label}.path must be a non-empty relative path")
    path = (root / declared).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        fail(f"{label}.path escapes the declared review root")
    if not path.is_file():
        fail(f"{label}.path does not name a file: {declared}")
    return path


def binding(root: Path, value: object, label: str) -> None:
    if not isinstance(value, dict) or set(value) != REQUIRED_BINDING:
        fail(f"{label} must contain exactly path, locator and sha256")
    if not isinstance(value["locator"], str) or not value["locator"].strip():
        fail(f"{label}.locator must be non-empty reviewer-declared scope")
    path = relative_file(root, value["path"], label)
    expected = f"sha256:{digest(path)}"
    if value["sha256"] != expected:
        fail(f"{label}.sha256 does not bind the declared file")


def validate(root: Path, record_path: Path) -> None:
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"record is not valid JSON: {error.msg}")
    if not isinstance(record, dict) or set(record) != REQUIRED_TOP_LEVEL:
        fail("record must contain exactly the bounded semantic-review contract fields")
    if record["contract_version"] != "semantic-review-integrity/v1":
        fail("unsupported semantic review contract version")
    if record["record_scope"] != "candidate_and_rendered_artifact":
        fail("record_scope must explicitly bind candidate_and_rendered_artifact")
    composer = record["composer_identity"]
    reviewer = record["reviewer_identity"]
    if not isinstance(composer, str) or not composer or not isinstance(reviewer, str) or not reviewer:
        fail("composer_identity and reviewer_identity must be non-empty")
    if composer == reviewer:
        fail("reviewer_identity must be distinct from composer_identity")
    binding(root, record["candidate"], "candidate")
    binding(root, record["rendered"], "rendered")
    manifest = record["corpus_manifest"]
    if not isinstance(manifest, list) or not manifest:
        fail("corpus_manifest must declare at least one reviewed input")
    seen: set[str] = set()
    for index, entry in enumerate(manifest):
        binding(root, entry, f"corpus_manifest[{index}]")
        path = entry["path"]
        if path in seen:
            fail("corpus_manifest must not duplicate a declared path")
        seen.add(path)
    if record["candidate"]["path"] in seen or record["rendered"]["path"] in seen:
        fail("candidate/rendered artifacts belong to review scope, not corpus_manifest")
    if record["human_verdict"] not in {"APPROVE", "REVISE"}:
        fail("human_verdict must be the reviewer-declared APPROVE or REVISE")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, required=True, help="root relative to which declared paths resolve")
    args = parser.parse_args()
    try:
        validate(args.root, args.record)
    except ValueError as error:
        print(f"Semantic review integrity refused: {error}")
        return 1
    print("Semantic review integrity passed; human verdict remains decisive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
