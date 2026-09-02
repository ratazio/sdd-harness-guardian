#!/usr/bin/env python3
"""Regression checks for the minimal post-render review pair finalization."""

from __future__ import annotations

import hashlib
import html as html_module
import re
import tempfile
from pathlib import Path

from render_stakeholder_brief import (
    POST_REVIEW_RECORDED_AUTHORITY_TEXT,
    POST_REVIEW_RECORDED_NEXT_STEP_TEXT,
    RENDERED_AUTHORITY_TEXT,
    RENDERED_NEXT_STEP_TEXT,
    finalize_post_render_review,
    recover_promotion,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def state(inputs: str) -> str:
    return f'''schema_version: 1
initiative_id: "post-review-fixture"
status: "executing"
summary: "Stakeholder brief rendered; independent post-render review pending; not approved or deliverable."
brief_lineage: "v2"
brief_phase: "rendered"
current_phase: "rendered_decision_review_pending"
last_safe_checkpoint: "Rendered lifecycle transition committed; independent post-render review is pending."
quality_gates:
  human_visibility_ready: false
  tasks_ready: false
brief_review:
  author: "fixture-author"
  review_record: "decision-log.md#D-900"
  quality_review_required: true
  quality_review_record: "evidence/rendered-review.md"
  quality_review_status: "approve"
  quality_review_reviewer: "fixture-reviewer"
  quality_review_inputs: "{inputs}"
next_safe_step: "Record the initiative's independent post-render review before any delivery decision; Human Visibility and Tasks Ready remain false."
'''


def html(state_digest: str) -> str:
    fragment = 'initiative_id: "post-review-fixture"'
    fragment_digest = hashlib.sha256(fragment.encode("utf-8")).hexdigest()
    return f'''<html data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="brief_phase" data-brief-phase="rendered">
<head><meta data-lifecycle-marker="rendered-state-digest" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="{state_digest}"></head>
<body><p data-lifecycle-marker="rendered-authority" data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" data-lifecycle-fragment="authority">{RENDERED_AUTHORITY_TEXT}</p>
<p data-lifecycle-marker="rendered-next-safe-step" data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-next-safe-step" data-lifecycle-fragment="next">{RENDERED_NEXT_STEP_TEXT}</p>
<section data-source="run-state.yaml" data-source-section="identity" data-coverage="represented" data-source-digest="sha256:placeholder" data-source-fragment="{html_module.escape(fragment, quote=True)}" data-source-fragment-sha256="sha256:{fragment_digest}" data-lifecycle-marker="rendered-state-source-digest" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="identity">{fragment}</section>
<div data-fixture-unaltered="yes">AUTHORED BYTES MUST SURVIVE</div></body></html>'''


def seed(root: Path) -> tuple[Path, Path]:
    evidence = root / "evidence"
    evidence.mkdir()
    (root / "decision-log.md").write_text("## D-900\n\npre-render record\n", encoding="utf-8")
    # The rendered snapshot precedes the later review metadata, which is why
    # its lifecycle state digest is deliberately immutable rather than a claim
    # about the mutable final state.
    initial = state("rendered=stakeholder-brief.html@sha256:" + "0" * 64)
    target = root / "stakeholder-brief.html"
    target.write_text(html(hashlib.sha256(initial.encode("utf-8")).hexdigest()), encoding="utf-8")
    digest = hashlib.sha256(target.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
    (root / "run-state.yaml").write_text(state(f"rendered=stakeholder-brief.html@sha256:{digest}"), encoding="utf-8")
    (evidence / "rendered-review.md").write_text(
        "# review\n\n"
        "Reviewer: `fixture-reviewer`\n"
        "Outcome: `approve`\n"
        "Reviewed rendered artifact: `stakeholder-brief.html`\n"
        f"Rendered HTML SHA-256: `{digest}`\n"
        "Preview URL: `http://127.0.0.1:4173/specs/post-review-fixture/stakeholder-brief.html?view=scope`\n"
        "Preview environment: `local loopback browser`\n",
        encoding="utf-8",
    )
    return target, root / "run-state.yaml"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="post-render-finalization-") as name:
        root = Path(name)
        target, state_path = seed(root)
        old_html, old_state = target.read_text(encoding="utf-8"), state_path.read_text(encoding="utf-8")

        # Invalid evidence/digest must refuse before either member changes.
        evidence = root / "evidence" / "rendered-review.md"
        evidence.write_text(evidence.read_text(encoding="utf-8").replace("approve", "revise", 1), encoding="utf-8")
        try:
            finalize_post_render_review(root, target, state_path)
        except ValueError as error:
            require("Outcome" in str(error), "invalid evidence was refused for the wrong reason")
        else:
            raise AssertionError("invalid review record was accepted")
        require(target.read_text(encoding="utf-8") == old_html and state_path.read_text(encoding="utf-8") == old_state, "invalid evidence mutated the pair")
        evidence.write_text(evidence.read_text(encoding="utf-8").replace("revise", "approve", 1), encoding="utf-8")
        evidence.write_text(evidence.read_text(encoding="utf-8").replace("Preview URL: `http://127.0.0.1:4173/specs/post-review-fixture/stakeholder-brief.html?view=scope`\n", "", 1), encoding="utf-8")
        try:
            finalize_post_render_review(root, target, state_path)
        except ValueError as error:
            require("Preview URL" in str(error), "missing preview URL was refused for the wrong reason")
        else:
            raise AssertionError("file-only post-render review was accepted")
        evidence.write_text(
            evidence.read_text(encoding="utf-8")
            + "Preview URL: `http://127.0.0.1:4173/specs/post-review-fixture/stakeholder-brief.html?view=scope`\n",
            encoding="utf-8",
        )
        state_path.write_text(old_state.replace("sha256:", "sha256:0", 1), encoding="utf-8")
        try:
            finalize_post_render_review(root, target, state_path)
        except ValueError as error:
            require("inputs" in str(error), "invalid review digest was refused for the wrong reason")
        else:
            raise AssertionError("invalid review digest was accepted")
        state_path.write_text(old_state, encoding="utf-8")

        # A journalled fault restores the original coherent pair, then the same
        # approved evidence can be finalized normally.
        try:
            finalize_post_render_review(root, target, state_path, fault_at="rename_state")
        except RuntimeError:
            pass
        else:
            raise AssertionError("fault injection did not interrupt finalization")
        require(recover_promotion(target, state_path) is None, "post-review pair recovery failed")
        require(target.read_text(encoding="utf-8") == old_html and state_path.read_text(encoding="utf-8") == old_state, "recovery did not restore the original pair")

        final_html, final_state = finalize_post_render_review(root, target, state_path)
        require('current_phase: "rendered_decision_review_recorded"' in final_state, "final state did not record review")
        require("human_visibility_ready: false" in final_state and "tasks_ready: false" in final_state, "finalization released a delivery gate")
        require(POST_REVIEW_RECORDED_AUTHORITY_TEXT in final_html and POST_REVIEW_RECORDED_NEXT_STEP_TEXT in final_html, "final HTML lifecycle did not follow final state")
        require('data-fixture-unaltered="yes">AUTHORED BYTES MUST SURVIVE</div>' in final_html, "finalization rewrote non-lifecycle authored bytes")
        final_digest = hashlib.sha256(final_state.encode("utf-8")).hexdigest()
        snapshot = re.search(r'data-lifecycle-marker="rendered-state-digest"[^>]*content="([0-9a-f]{64})"', final_html, re.DOTALL)
        require(snapshot and snapshot.group(1) == final_digest, "rendered-state meta does not bind final run-state bytes")
        require(final_html.count(f'data-source-digest="sha256:{final_digest}"') == 1, "rendered state provenance does not bind final run-state bytes")

    print("Post-render review finalization contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
