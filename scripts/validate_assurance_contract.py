"""Focused structural mirror for declared assurance profiles; not a semantic approval."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    profile = next((line for line in text.splitlines() if line.startswith("**Assurance profile:**")), None)
    if profile is None:
        return errors  # lineage-aware: legacy sources are not opted in.
    selected = profile.removeprefix("**Assurance profile:**").strip()
    if selected not in {"A1-local", "A2-elevated", "A3-critical-local-policy"}:
        errors.append("declared assurance profile must be A1-local, A2-elevated or A3-critical-local-policy")
        return errors
    rationale = re.search(r"(?m)^\*\*Rationale and trigger evidence:\*\*\s*(.+)$", text)
    if not rationale or not rationale.group(1).strip():
        errors.append("declared assurance profile lacks rationale and trigger evidence")
    if selected in {"A2-elevated", "A3-critical-local-policy"}:
        links = re.search(r"(?m)^\*\*A2/A3 source links/headings \(or A1 N/A reason\):\*\*\s*(.+)$", text)
        if not links or not links.group(1).strip() or links.group(1).strip().lower() == "not_applicable":
            errors.append("declared A2/A3 profile lacks source links/headings")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    failures = validate(args.plan)
    if failures:
        print("Assurance contract structural failure(s):")
        print("\n".join(f"- {failure}" for failure in failures))
        raise SystemExit(1)
    print("Assurance contract structural pass; semantic adequacy requires independent review.")
