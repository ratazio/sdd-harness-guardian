#!/usr/bin/env python3
"""Exercise rendering a complete candidate before qualitative approval.

The fixture keeps source/provenance bindings intact but converts the lifecycle
back to a pre-render `REVISE`. The renderer must write a final review surface,
retain both readiness gates as false, and never claim approval.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import tempfile
from pathlib import Path

from render_stakeholder_brief import decision_record_digest, review_record_content
from test_render_stakeholder_brief import (
    RENDERER,
    SCAFFOLDER,
    fully_reviewed_candidate,
    ready_to_render,
    valid_candidate_html,
)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="unapproved-brief-render-") as directory:
        root = Path(directory)
        created = subprocess.run(
            ["python", str(SCAFFOLDER), "001-autonomous-render", "--consumer-root", str(root)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert created.returncode == 0, created.stderr
        initiative = root / "specs" / "001-autonomous-render"
        state_path = initiative / "run-state.yaml"
        ready_to_render(state_path)

        # Reproduce the useful-but-unapproved state. The candidate remains
        # source-bound; its review outcome may not prevent the final from being
        # made available for recovery and HTTP review.
        state = state_path.read_text(encoding="utf-8")
        state = state.replace('brief_phase: "ready_to_render"', 'brief_phase: "not_rendered"', 1)
        state = state.replace('current_phase: "render_pending"', 'current_phase: "ready_to_compose"', 1)
        state = state.replace('brief_coverage_ready: true', 'brief_coverage_ready: false', 1)
        state = state.replace('findings_status: "pass"', 'findings_status: "revise"', 1)
        state_path.write_text(state, encoding="utf-8")
        candidate = fully_reviewed_candidate(initiative, valid_candidate_html())
        candidate_path = initiative / "brief-candidates" / "stakeholder-brief.candidate.html"
        candidate_path.parent.mkdir(exist_ok=True)
        candidate_path.write_text(candidate, encoding="utf-8")

        # A stale `approve` record cannot be relabelled as a `revise` recovery
        # merely by changing run-state. The recovery finding itself must be
        # bound to the candidate before an unapproved review surface can exist.
        mismatch = subprocess.run(
            ["python", str(RENDERER), str(initiative), "--candidate", str(candidate_path), "--render-unapproved"],
            text=True,
            capture_output=True,
            check=False,
        )
        assert mismatch.returncode == 1, mismatch.stdout
        assert "bound composition record to state Review outcome: revise" in mismatch.stderr, mismatch.stderr

        recovery_log = (initiative / "decision-log.md").read_text(encoding="utf-8") + (
            "\n## D-901 — recovery review for the composed candidate\n\n"
            "Author: fixture-author\n"
            "Reviewer: fixture-reviewer\n"
            "Review outcome: revise\n"
            "Recovery action: Recompose the affected candidate blocks and request a new independent review.\n"
            "Composition provenance: verified\n"
            "Human attestation: confirmed\n"
            "Candidate SHA-256: recovery surface binding is pending\n"
        )
        (initiative / "decision-log.md").write_text(recovery_log, encoding="utf-8")
        record = review_record_content(recovery_log, "D-901")
        assert record is not None
        candidate = candidate.replace("D-900", "D-901")
        candidate = candidate.replace(
            f'data-source-fragment-sha256="sha256:{hashlib.sha256(b"D-900").hexdigest()}"',
            f'data-source-fragment-sha256="sha256:{hashlib.sha256(b"D-901").hexdigest()}"',
            1,
        )
        candidate = re.sub(
            r"decision-record-sha256:[0-9a-f]+",
            f"decision-record-sha256:{decision_record_digest(record)}",
            candidate,
            count=1,
        )
        candidate_path.write_text(candidate, encoding="utf-8")
        old_state_digest = hashlib.sha256(state_path.read_bytes()).hexdigest()
        state = state.replace('review_record: "decision-log.md#D-900"', 'review_record: "decision-log.md#D-901"', 1)
        state_path.write_text(state, encoding="utf-8")
        new_state_digest = hashlib.sha256(state_path.read_bytes()).hexdigest()
        candidate = candidate.replace(
            f'data-source-digest="sha256:{old_state_digest}"',
            f'data-source-digest="sha256:{new_state_digest}"',
        )
        candidate_path.write_text(candidate, encoding="utf-8")

        rendered = subprocess.run(
            ["python", str(RENDERER), str(initiative), "--candidate", str(candidate_path), "--render-unapproved"],
            text=True,
            capture_output=True,
            check=False,
        )
        assert rendered.returncode == 0, rendered.stderr
        final = (initiative / "stakeholder-brief.html").read_text(encoding="utf-8")
        final_state = state_path.read_text(encoding="utf-8")
        assert 'data-brief-phase="rendered"' in final
        assert "autonomous decision review or recovery pending" in final
        assert 'brief_phase: "rendered"' in final_state
        assert 'current_phase: "rendered_autonomous_review_pending"' in final_state
        assert "human_visibility_ready: false" in final_state
        assert "tasks_ready: false" in final_state
    print("Unapproved final brief render passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
