#!/usr/bin/env python3
"""Ensure Human Visibility cannot outlive the local rendered-review evidence."""

from __future__ import annotations

import tempfile
from pathlib import Path

from validate_human_visibility import Report, check_decision_quality_review


STATE = '''brief_review:
  author: "composer"
  quality_review_required: true
  quality_review_record: "evidence/rendered-review.md"
  quality_review_status: "approve"
  quality_review_reviewer: "independent-reviewer"
  quality_review_inputs: "rendered=stakeholder-brief.html@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
'''


def check(root: Path) -> list[str]:
    report = Report()
    check_decision_quality_review(root, STATE, report)
    return report.gate


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        evidence = root / "evidence"
        evidence.mkdir()
        review = evidence / "rendered-review.md"
        review.write_text("Reviewer: independent-reviewer\n", encoding="utf-8")
        findings = check(root)
        assert any("Preview URL" in finding for finding in findings), findings
        assert any("Preview environment" in finding for finding in findings), findings

        review.write_text(
            "Reviewer: independent-reviewer\n"
            "Preview URL: `http://127.0.0.1:4173/specs/001/stakeholder-brief.html?view=scope`\n"
            "Preview environment: `local loopback browser`\n",
            encoding="utf-8",
        )
        assert not check(root), check(root)

        review.write_text(
            review.read_text(encoding="utf-8").replace("127.0.0.1", "example.test", 1),
            encoding="utf-8",
        )
        assert any("Preview URL" in finding for finding in check(root)), check(root)
    print("Human Visibility preview-binding contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
