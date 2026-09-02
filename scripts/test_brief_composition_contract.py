#!/usr/bin/env python3
"""Stable source-to-brief parity checks; never a prose or aesthetic judge."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "scripts" / "fixtures" / "brief-composition-parity"
IDS = re.compile(r"\b(?:T|AC)-\d{3}\b")


def ids(path: Path) -> set[str]:
    return set(IDS.findall(path.read_text(encoding="utf-8")))


def panel(html: str, identifier: str) -> str:
    match = re.search(rf'<section id="{identifier}"[\s\S]*?</section>', html)
    if match is None:
        raise AssertionError(f"missing {identifier} panel")
    return match.group(0)


def parity_errors(tasks: Path, validation: Path, brief: Path) -> list[str]:
    html = brief.read_text(encoding="utf-8")
    task_ids = {item for item in ids(tasks) if item.startswith("T-")}
    ac_ids = {item for item in ids(validation) if item.startswith("AC-")}
    execution = set(IDS.findall(panel(html, "execution")))
    proof = set(IDS.findall(panel(html, "validation")))
    errors = []
    if task_ids - execution:
        errors.append("missing task projection: " + ", ".join(sorted(task_ids - execution)))
    if ac_ids - proof:
        errors.append("missing AC projection: " + ", ".join(sorted(ac_ids - proof)))
    if "data-brief-phase=\"scaffold\"" in html and (task_ids or ac_ids):
        errors.append("scaffold cannot represent populated source projections")
    return errors


def main() -> int:
    positive = parity_errors(FIXTURE / "rich-tasks.md", FIXTURE / "rich-validation.md", FIXTURE / "rich-brief.html")
    assert positive == [], positive
    negative = parity_errors(FIXTURE / "rich-tasks.md", FIXTURE / "rich-validation.md", FIXTURE / "scaffold.html")
    assert "missing task projection: T-001, T-002, T-003, T-004" in negative, negative
    assert "missing AC projection: AC-001, AC-002, AC-003, AC-004" in negative, negative
    assert "scaffold cannot represent populated source projections" in negative, negative
    print("Brief composition parity fixtures passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
