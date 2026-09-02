#!/usr/bin/env python3
"""Focused integrity fixtures for minimal opt-in rendered-review evidence."""

from __future__ import annotations

import tempfile
from pathlib import Path

from validate_human_visibility import Report, check_decision_quality_review


HASH = "a" * 64


def state(*, status: str = "approve", reviewer: str = "reviewer-z", record: str = "evidence/review.md", rendered: str = f"rendered=stakeholder-brief.html@sha256:{HASH}", author: str = "author-z") -> str:
    return """brief_review:
  author: "%s"
  quality_review_required: true
  quality_review_record: "%s"
  quality_review_status: "%s"
  quality_review_reviewer: "%s"
  quality_review_inputs: "%s"
""" % (author, record, status, reviewer, rendered)


def errors(root: Path, content: str, *, create_record: bool = True, record_body: str = "Review ID: R-1\n") -> list[str]:
    (root / "evidence").mkdir(exist_ok=True)
    if create_record:
        (root / "evidence" / "review.md").write_text(
            record_body,
            encoding="utf-8",
        )
    report = Report()
    check_decision_quality_review(root, content, report)
    return report.gate


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="decision-quality-") as temp:
        root = Path(temp)
        assert not errors(root, state())
        # Gate outcomes are closed literals.  Quote delimiters in normal YAML
        # remain valid, but aliases, case variants, whitespace, nested quotes
        # and substrings must not authorize the quality review.
        for status in ("revise", "APPROVE", " approve ", "'approve'", "approved", "pass", "passed", "preapprove"):
            assert any("status must be exactly approve" in error for error in errors(root, state(status=status))), status
        assert any("distinct from brief_review.author" in error for error in errors(root, state(reviewer="author-z")))
        assert any("locate and digest the rendered artifact" in error for error in errors(root, state(rendered="rendered=stakeholder-brief.html@sha256:abc")))
        assert any("locate and digest the rendered artifact" in error for error in errors(root, state(rendered=f"request=mock.md@sha256:{HASH}")))
        outside = root.parent / "external" / "review.md"
        outside.parent.mkdir(exist_ok=True)
        outside.write_text("review", encoding="utf-8")
        assert any("must resolve inside evidence" in error for error in errors(root, state(record="evidence/../../external/review.md"), create_record=False))
        (root / "evidence" / "review.md").unlink()
        assert any("must resolve inside evidence" in error for error in errors(root, state(), create_record=False))
        assert any("record must be nonempty" in error for error in errors(root, state(), record_body="\n"))
    print("Decision-quality review integrity contract passed; semantic adequacy remains human judgment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
