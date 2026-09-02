#!/usr/bin/env python3
"""Regression contract for source-only creation and guarded brief promotion."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from render_stakeholder_brief import (
    ALLOWED_BLOCK_SOURCES, COMMIT_POINTS, canonical_composition_manifest, decision_record_digest, lifecycle_authority_projection, lifecycle_error, recover_promotion,
    PRE_RENDER_PENDING_AUTHORITY_TEXT, PRE_RENDER_PENDING_NEXT_STEP_TEXT, PRE_RENDER_PENDING_REVIEW_STATUS_TEXT, PRE_RENDER_READY_AUTHORITY_TEXT, PRE_RENDER_READY_NEXT_STEP_TEXT, RENDERED_AUTHORITY_TEXT, RENDERED_NEXT_STEP_TEXT, RENDERED_REVIEW_STATUS_TEXT, RENDERED_STATE_CHECKPOINT_TEXT, RENDERED_STATE_SUMMARY_TEXT, render_lifecycle, rendered_lifecycle_state, review_record_content,
    declared_source_lifecycle_updates, pre_render_review_error, promote_bundle, rendered_source_lifecycle_content, source_lifecycle_error,
    provenance_error, render_provenance_digests, render_provenance_fragments,
    _declared_source_paths, scalar,
)
from brief_v2_sources import V2_REQUIRED_SOURCES


ROOT = Path(__file__).resolve().parent.parent
SCAFFOLDER = ROOT / "scripts" / "new_initiative.py"
RENDERER = ROOT / "scripts" / "render_stakeholder_brief.py"
SHELL = ROOT / ".harness" / "templates" / "stakeholder-brief.html"
RICH_CANDIDATE = ROOT / "specs" / "019-rendered-brief-decision-quality-gate" / "stakeholder-brief.html"
SPEC_022_CANDIDATE = ROOT / "specs" / "022-rendered-brief-lifecycle-freshness-and-authority" / "evidence" / "T-000-stakeholder-brief.candidate.html"
SPEC_022_INITIATIVE = SPEC_022_CANDIDATE.parent.parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run(*command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=False)


def ready_to_render(state_path: Path) -> None:
    state = state_path.read_text(encoding="utf-8")
    state = state.replace('status: "draft"', 'status: "executing"', 1)
    state = state.replace('brief_phase: "not_rendered"', 'brief_phase: "ready_to_render"', 1)
    state = state.replace('current_phase: "specify"', 'current_phase: "render_pending"', 1)
    state = state.replace('brief_lineage: null', 'brief_lineage: "v2"', 1)
    state = state.replace('brief_coverage_ready: false', 'brief_coverage_ready: true', 1)
    state = state.replace('author: null', 'author: "fixture-author"', 1)
    state = state.replace('coverage_reviewer: null', 'coverage_reviewer: "fixture-reviewer"', 1)
    state = state.replace('review_record: null', 'review_record: "decision-log.md#D-900"', 1)
    state = state.replace('reviewed_at: null', 'reviewed_at: "2026-08-29"', 1)
    state = state.replace('findings_status: "not_started"', 'findings_status: "pass"', 1)
    state = state.replace('quality_review_required: false', 'quality_review_required: true', 1)
    state_path.write_text(state, encoding="utf-8")


def valid_candidate_html() -> str:
    """Use a composed vendor-neutral decision brief, not the scaffold shell."""
    require(RICH_CANDIDATE.is_file(), "rich authored candidate fixture is missing")
    html = RICH_CANDIDATE.read_text(encoding="utf-8")
    html = html.replace(
        'data-client-identity-profile="pearson"',
        'data-client-identity-profile="vendor-neutral"',
        1,
    ).replace("data-harness-pearson-shell", "data-harness-brief-shell", 1)
    html = re.sub(r'<a class="brief-client-logo"[^>]*>.*?</a>', "", html, count=1)
    html = re.sub(r"\.brief-client-logo(?:\s+img)?\{[^}]*\}", "", html)
    html = html.replace(
        'data-brief-phase="authored"',
        'data-harness-template-kind="composed" data-composition-review-record="D-900" '
        'data-composition-provenance="reviewed" data-brief-phase="authored"',
        1,
    )
    html = html.replace(
        'data-source="run-state.yaml"',
        'data-source="run-state.yaml" data-lifecycle-marker="rendered-state-source-digest" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="final run-state SHA-256"', 1,
    )
    return html


def pearson_candidate_html() -> str:
    """A composed candidate that explicitly selects the Pearson profile."""
    html = RICH_CANDIDATE.read_text(encoding="utf-8")
    html = html.replace('alt="Pearson"', 'alt=""', 1).replace(
        ":root{", ":root{--navy:#0b004a;--lavender:#f3f2fe;", 1
    )
    html = html.replace(
        'data-brief-phase="authored"',
        'data-harness-template-kind="composed" data-composition-review-record="D-900" '
        'data-composition-provenance="reviewed" data-brief-phase="authored"',
        1,
    )
    return html.replace(
        'data-source="run-state.yaml"',
        'data-source="run-state.yaml" data-lifecycle-marker="rendered-state-source-digest" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="final run-state SHA-256"', 1,
    )


def candidate_with_block_digests(initiative: Path, html: str) -> str:
    """Bind every declared source block to this fixture initiative.

    Decision-record digest is filled after the first record is written because
    the record's candidate SHA is intentionally excluded from its own digest.
    """
    def bind(match: re.Match[str]) -> str:
        start, source, end = match.groups()
        if source == "decision-log.md":
            digest = "decision-record-sha256:PENDING"
            fragment = "D-900"
        else:
            source_content = (initiative / source).read_text(encoding="utf-8")
            digest = f"sha256:{hashlib.sha256((initiative / source).read_bytes()).hexdigest()}"
            fragment_match = re.search(r"[A-Za-z][A-Za-z0-9_-]{3,}", source_content)
            require(fragment_match is not None, f"fixture source {source} has no safe factual fragment")
            fragment = fragment_match.group(0)
        fragment_digest = hashlib.sha256(fragment.encode("utf-8")).hexdigest()
        return (
            f'{start} data-source-digest="{digest}" data-source-fragment="{fragment}" '
            f'data-source-fragment-sha256="sha256:{fragment_digest}"{end}{fragment}'
        )

    return re.sub(r'(<[^>]*\bdata-source="([^"]+)"[^>]*)(>)', bind, html)


def with_lifecycle_markers(html: str) -> str:
    """Add the closed renderer-owned surface without changing authored facts."""
    html = html.replace(
        "<html ",
        '<html data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml" '
        'data-lifecycle-fragment="brief_phase" ', 1,
    )
    html = html.replace(
        "<head>",
        '<head><meta data-lifecycle-marker="rendered-state-digest" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="candidate">', 1,
    ).replace(
        "</body>", '<p data-lifecycle-marker="rendered-authority" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" data-lifecycle-fragment="brief_phase: rendered">candidate</p>'
        '<p data-lifecycle-marker="rendered-review-status" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-review-status" data-lifecycle-fragment="review lifecycle status">'
        f'{PRE_RENDER_PENDING_REVIEW_STATUS_TEXT}</p></body>', 1,
    )
    return html


def fully_reviewed_candidate(initiative: Path, html: str) -> str:
    candidate = candidate_with_block_digests(initiative, with_lifecycle_markers(html))
    candidate = candidate.replace(">candidate</p>", f">{PRE_RENDER_READY_AUTHORITY_TEXT}</p>", 1)
    record_review(initiative, candidate)
    record = review_record_content(
        (initiative / "decision-log.md").read_text(encoding="utf-8"), "D-900"
    )
    require(record is not None, "fixture review record did not resolve")
    candidate = candidate.replace(
        "decision-record-sha256:PENDING",
        f"decision-record-sha256:{decision_record_digest(record)}",
    )
    record_review(initiative, candidate)
    return candidate


def record_review(initiative: Path, candidate_html: str) -> None:
    digest = hashlib.sha256(candidate_html.encode("utf-8")).hexdigest()
    source_digests = "\n".join(
        f"- {source.name}@sha256:{hashlib.sha256(source.read_bytes()).hexdigest()}"
        for source in (
            initiative / "spec.md",
            initiative / "impact-map.md",
            initiative / "plan.md",
            initiative / "tasks.md",
            initiative / "validation-plan.md",
        )
    )
    (initiative / "decision-log.md").write_text(
        "# Decision Log\n\n"
        "## D-900 — reviewed candidate composition\n\n"
        "Author: fixture-author\n"
        "Reviewer: fixture-reviewer\n"
        "Review outcome: approve\n"
        "Composition provenance: verified\n"
        "Human attestation: confirmed\n"
        f"Composition manifest SHA-256: {canonical_composition_manifest(initiative)}\n"
        f"Candidate SHA-256: {digest}\n"
        "Source digests:\n"
        f"{source_digests}\n",
        encoding="utf-8",
    )


def record_pending_signature(initiative: Path) -> None:
    """Create stable authored context before a reviewer signs the input."""
    (initiative / "decision-log.md").write_text(
        "# Decision Log\n\n"
        "## D-900 — candidate composition\n\n"
        "Author: fixture-author\n"
        "Reviewer: pending independent reviewer\n"
        "Review outcome: pending\n"
        "Composition provenance: pending\n"
        "Human attestation: pending\n"
        f"Composition manifest SHA-256: {canonical_composition_manifest(initiative)}\n"
        "Candidate SHA-256: pending exact binding\n"
        "Scope: immutable candidate input for independent signing.\n",
        encoding="utf-8",
    )


def sign_pending_candidate(initiative: Path, candidate_html: str) -> None:
    """Fill only the reviewer-owned envelope after candidate bytes are fixed."""
    digest = hashlib.sha256(candidate_html.encode("utf-8")).hexdigest()
    record = (initiative / "decision-log.md").read_text(encoding="utf-8")
    signed = (record
        .replace("Reviewer: pending independent reviewer", "Reviewer: fixture-reviewer", 1)
        .replace("Review outcome: pending", "Review outcome: approve", 1)
        .replace("Composition provenance: pending", "Composition provenance: verified", 1)
        .replace("Human attestation: pending", "Human attestation: confirmed", 1)
        .replace("Candidate SHA-256: pending exact binding", f"Candidate SHA-256: {digest}", 1))
    require(
        decision_record_digest(review_record_content(record, "D-900") or "")
        == decision_record_digest(review_record_content(signed, "D-900") or ""),
        "independent signature changed the candidate's stable decision context digest",
    )
    (initiative / "decision-log.md").write_text(signed, encoding="utf-8")


def main() -> int:
    require(ALLOWED_BLOCK_SOURCES == V2_REQUIRED_SOURCES, "renderer provenance admission must use the shared v2 source set")
    with tempfile.TemporaryDirectory(prefix="sdd-render-brief-") as temporary:
        consumer = Path(temporary)
        # A lifecycle span can be cited as part of a source-provenance
        # fragment.  Promotion changes that span in the source bundle, so the
        # fragment binding must move with it rather than leaving a digest-only
        # or stale-fragment HTML claim.  This deliberately uses arbitrary
        # source prose and no SPEC-specific path convention.
        fragment_root = consumer / "fragment-binding"
        fragment_root.mkdir()
        fragment_source = fragment_root / "progress.md"
        old_projection = "source says: review before refresh"
        new_projection = "source says: rendered review remains required"
        fragment_source.write_text(
            '<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-authority" fragment="arbitrary binding" -->'
            + old_projection
            + '<!-- /sdd-lifecycle-authority -->',
            encoding="utf-8",
        )
        (fragment_root / "run-state.yaml").write_text(
            '# sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-authority" fragment="state member" field="summary"\n'
            'summary: "source says: review before refresh"\n'
            '# /sdd-lifecycle-authority\n',
            encoding="utf-8",
        )
        require(
            {path.relative_to(fragment_root).as_posix() for path in _declared_source_paths(fragment_root)} == {"progress.md"},
            "run-state lifecycle declarations must remain the separately staged transaction member",
        )
        fragment_before = old_projection
        fragment_candidate = (
            '<article data-source="progress.md" data-source-section="arbitrary" '
            'data-coverage="represented" data-source-digest="sha256:stale" '
            f'data-source-fragment="{fragment_before}" '
            f'data-source-fragment-sha256="sha256:{hashlib.sha256(fragment_before.encode("utf-8")).hexdigest()}">'
            f'{new_projection}</article>'
        )
        fragment_after = fragment_source.read_text(encoding="utf-8").replace(old_projection, new_projection)
        fragment_manifest = {"progress.md": fragment_after.encode("utf-8")}
        fragment_rendered = render_provenance_digests(
            render_provenance_fragments(fragment_candidate, fragment_root, fragment_manifest),
            fragment_manifest,
        )
        expected_fragment = new_projection
        require(expected_fragment in fragment_rendered, "rendered provenance did not bind the promoted lifecycle fragment")
        require(
            provenance_error(fragment_root, fragment_rendered, "", fragment_manifest) is None,
            "rendered provenance fragment did not bind the final staged source",
        )
        # The pair's run-state is special only for its three declared root
        # transition scalars.  A candidate may cite one complete pre-render
        # scalar, and the final provenance must cite the final staged scalar;
        # a partial or unrelated value must never gain that rewrite privilege.
        state_fragment_root = consumer / "state-fragment-binding"
        state_fragment_root.mkdir()
        state_before = (
            'summary: "candidate summary"\n'
            'last_safe_checkpoint: "candidate checkpoint"\n'
            'next_safe_step: "guarded refresh"\n'
            'unrelated: "guarded refresh"\n'
        )
        state_after = rendered_lifecycle_state(
            'status: "executing"\nbrief_phase: "ready_to_render"\ncurrent_phase: "render_pending"\n'
            + state_before
        )
        (state_fragment_root / "run-state.yaml").write_text(
            'status: "executing"\nbrief_phase: "ready_to_render"\ncurrent_phase: "render_pending"\n' + state_before,
            encoding="utf-8",
        )
        old_scalar = 'next_safe_step: "guarded refresh"'
        state_candidate = (
            '<article data-source="run-state.yaml" data-source-section="next" '
            'data-coverage="represented" data-source-digest="sha256:stale" '
            f'data-source-fragment="{old_scalar.replace(chr(34), "&quot;")}" '
            f'data-source-fragment-sha256="sha256:{hashlib.sha256(old_scalar.encode("utf-8")).hexdigest()}">'
            f'{old_scalar}</article>'
        )
        state_manifest = {"run-state.yaml": state_after.encode("utf-8")}
        state_rendered = render_provenance_digests(
            render_provenance_fragments(state_candidate, state_fragment_root, state_manifest),
            state_manifest,
        )
        new_scalar = f'next_safe_step: "{RENDERED_NEXT_STEP_TEXT}"'
        require(new_scalar in state_rendered, "rendered provenance did not bind the final declared run-state scalar")
        require(
            provenance_error(state_fragment_root, state_rendered, "", state_manifest) is None,
            "rendered run-state provenance did not validate against the final staged state",
        )
        unrelated_candidate = state_candidate.replace(old_scalar, "guarded refresh", 2)
        unrelated_rendered = render_provenance_digests(
            render_provenance_fragments(unrelated_candidate, state_fragment_root, state_manifest),
            state_manifest,
        )
        require("guarded refresh" in unrelated_rendered, "partial run-state prose was rewritten as a lifecycle scalar")
        created = run(sys.executable, str(SCAFFOLDER), "render-guard", "--consumer-root", str(consumer))
        require(created.returncode == 0, created.stderr)
        initiative = consumer / "specs" / "001-render-guard"
        target = initiative / "stakeholder-brief.html"
        require(not target.exists(), "scaffolder created a delivered HTML path")
        state = initiative / "run-state.yaml"

        ready_to_render(state)
        scaffold_candidate = consumer / "scaffold-candidate.html"
        scaffold_candidate.write_text(SHELL.read_text(encoding="utf-8"), encoding="utf-8")
        record_review(initiative, scaffold_candidate.read_text(encoding="utf-8"))
        rejected = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(scaffold_candidate))
        require(rejected.returncode != 0, "renderer accepted the canonical empty shell")
        require(
            "lifecycle marker" in rejected.stderr or "requires initiative-local" in rejected.stderr,
            rejected.stderr,
        )
        require(not target.exists(), "rejected scaffold candidate created a brief")

        reclassified = consumer / "reclassified-shell.html"
        reclassified_html = (
            SHELL.read_text(encoding="utf-8")
            .replace(
                'data-harness-template-kind="scaffold"',
                'data-harness-template-kind="composed" data-composition-review-record="D-900" '
                'data-composition-provenance="reviewed"',
                1,
            )
            .replace('data-brief-phase="scaffold"', 'data-brief-phase="authored"', 1)
            .replace("Scaffolded — not ready for review, baseline or delivery", "Rendered fixture", 1)
            .replace("Author canonical sources, then render a decision brief.", "Rendered fixture", 1)
            .replace("{{initiative}}", "001-render-guard").replace("{{date}}", "2026-08-28")
            .replace("{{risk}}", "risk fixture").replace("{{size}}", "size fixture")
        )
        reclassified.write_text(
            fully_reviewed_candidate(initiative, reclassified_html), encoding="utf-8"
        )
        record_review(initiative, reclassified.read_text(encoding="utf-8"))
        cosmetic = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(reclassified))
        require(cosmetic.returncode != 0, "renderer accepted a cosmetically reclassified shell")
        require(
            "canonical scaffold provenance topology" in cosmetic.stderr
            or "lifecycle marker" in cosmetic.stderr
            or "candidate must declare source provenance" in cosmetic.stderr
            or "requires initiative-local" in cosmetic.stderr,
            cosmetic.stderr,
        )

        target.write_text("<html></html>", encoding="utf-8")
        premature = run(sys.executable, str(ROOT / "scripts" / "validate_human_visibility.py"), "--consumer-root", str(consumer), "--initiative", "specs/001-render-guard")
        require(premature.returncode != 0, "validator accepted an HTML before rendered state")
        require("exists before run-state brief_phase is rendered" in premature.stdout, premature.stdout)
        target.unlink()

        hotlink_candidate = consumer / "hotlink-candidate.html"
        hotlink_candidate.write_text(
            fully_reviewed_candidate(initiative, pearson_candidate_html()).replace(
                "../../.harness/assets/brand/pearson-logo-white.png", "https://example.test/pearson.png", 1
            ),
            encoding="utf-8",
        )
        record_review(initiative, hotlink_candidate.read_text(encoding="utf-8"))
        hotlink = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(hotlink_candidate))
        require(hotlink.returncode != 0, "renderer accepted a remote Pearson logo")
        require("Pearson identity policy" in hotlink.stderr, hotlink.stderr)

        stale_candidate = consumer / "stale-source-candidate.html"
        stale_candidate.write_text(
            fully_reviewed_candidate(initiative, valid_candidate_html()).replace(
                'data-source-digest="sha256:', 'data-source-digest="sha256:stale-', 1
            ),
            encoding="utf-8",
        )
        record_review(initiative, stale_candidate.read_text(encoding="utf-8"))
        stale = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(stale_candidate))
        require(stale.returncode != 0, "renderer accepted a stale per-block source digest")
        require("provenance digest does not bind" in stale.stderr, stale.stderr)

        foreign_candidate = consumer / "foreign-source-candidate.html"
        foreign_candidate.write_text(
            fully_reviewed_candidate(initiative, valid_candidate_html()).replace(
                'data-source="spec.md"', 'data-source="../foreign.md"', 1
            ),
            encoding="utf-8",
        )
        record_review(initiative, foreign_candidate.read_text(encoding="utf-8"))
        foreign = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(foreign_candidate))
        require(foreign.returncode != 0, "renderer accepted a source outside the initiative allowlist")
        require("provenance source is not allowed" in foreign.stderr, foreign.stderr)

        candidate = consumer / "reviewed-candidate.html"
        # A promotion may update arbitrary declared canonical lifecycle
        # sources.  Keep both common layouts in this integration fixture so
        # the final HTML digest has to be derived from staged, not predecessor,
        # bytes.
        lifecycle_span = (
            '\n<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-authority" fragment="fixture lifecycle" -->'
            'Authored candidate; exact pre-render review has passed; ready only for guarded refresh; not rendered/deliverable; Human Visibility and Tasks Ready false.'
            '<!-- /sdd-lifecycle-authority -->\n'
            '<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-next-safe-step" fragment="fixture next safe step" -->'
            'Guarded refresh may be considered only for this exact reviewed candidate; Human Visibility and Tasks Ready remain false.'
            '<!-- /sdd-lifecycle-authority -->\n'
        )
        progress = initiative / "progress.md"
        handoff = initiative / "handoffs" / "latest-handoff.md"
        progress.write_text(progress.read_text(encoding="utf-8") + lifecycle_span, encoding="utf-8")
        handoff.write_text(handoff.read_text(encoding="utf-8") + lifecycle_span, encoding="utf-8")
        fixture_state = state.read_text(encoding="utf-8")
        state.write_text(
            re.sub(
                r'(?m)^next_safe_step: "[^"]*"$',
                f'next_safe_step: "{PRE_RENDER_READY_NEXT_STEP_TEXT}"',
                fixture_state,
                count=1,
            ),
            encoding="utf-8",
        )
        candidate_html = fully_reviewed_candidate(initiative, valid_candidate_html())
        # Exercise the command's real promotion path, rather than only the
        # fragment helper: this run-state provenance block cites a complete
        # scalar that the pair transition changes.  The rendered HTML must
        # cite the staged final scalar before final provenance is checked.
        old_state_scalar = f'next_safe_step: "{PRE_RENDER_READY_NEXT_STEP_TEXT}"'
        old_fragment_digest = hashlib.sha256(old_state_scalar.encode("utf-8")).hexdigest()
        run_state_block = re.compile(
            r'(?s)(?P<opening><[a-z][a-z0-9:-]*\b(?P<attributes>[^>]*\bdata-source="run-state\.yaml"[^>]*)>)'
            r'(?P<body>schema_version)'
        )
        def bind_transitioning_state_fragment(match: re.Match[str]) -> str:
            attributes = match.group("attributes")
            attributes = attributes.replace(
                'data-source-fragment="schema_version"',
                f'data-source-fragment="{old_state_scalar.replace(chr(34), "&quot;")}"',
                1,
            ).replace(
                'data-source-fragment-sha256="sha256:' + hashlib.sha256(b"schema_version").hexdigest() + '"',
                f'data-source-fragment-sha256="sha256:{old_fragment_digest}"',
                1,
            )
            return match.group("opening").replace(match.group("attributes"), attributes, 1) + old_state_scalar
        candidate_html, bindings = run_state_block.subn(bind_transitioning_state_fragment, candidate_html, count=1)
        require(bindings == 1, "integration fixture did not locate its run-state provenance block")
        candidate.write_text(candidate_html, encoding="utf-8")
        record_review(initiative, candidate.read_text(encoding="utf-8"))
        # Findings are a closed lowercase enum.  Neither negative words,
        # substrings, unknown values, nor casing variants may create ready
        # authority; both the marker projection and pre-render gate reject
        # exactly the same invalid state.
        reviewed_state = state.read_text(encoding="utf-8")
        candidate_html = candidate.read_text(encoding="utf-8")
        candidate_digest = hashlib.sha256(candidate_html.encode("utf-8")).hexdigest()
        for outcome in ("not_passed", "compass", "unknown", "PASS"):
            invalid_state = reviewed_state.replace(
                'findings_status: "pass"', f'findings_status: "{outcome}"', 1
            )
            state.write_text(invalid_state, encoding="utf-8")
            pre_render_error = pre_render_review_error(
                initiative, invalid_state, candidate_html, candidate_digest
            ) or ""
            require(
                "must be exactly one of" in pre_render_error,
                f"pre-render validation accepted invalid findings outcome {outcome}: {pre_render_error}",
            )
            invalid = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate))
            require(invalid.returncode != 0, f"renderer accepted invalid findings outcome {outcome}")
            require("must be exactly one of" in invalid.stderr, invalid.stderr)
        state.write_text(reviewed_state, encoding="utf-8")
        # Use a candidate without decision-record provenance for this focused
        # parser test.  The full candidate binds the decision-record digest,
        # which would otherwise reject a modified record before the outcome
        # contract is reached.
        outcome_candidate = "<html></html>"
        outcome_digest = hashlib.sha256(outcome_candidate.encode("utf-8")).hexdigest()
        record_review(initiative, outcome_candidate)
        # The decision record has a narrower authoring contract than the
        # structured findings lifecycle enum: only literal `approve` grants
        # promotion.  Casing, whitespace, quotes, aliases and substrings do
        # not become approval through normalization.
        for outcome in ("APPROVE", " approve ", "'approve'", "approved", "pass", "passed", "preapprove"):
            decision_log = initiative / "decision-log.md"
            reviewed_log = decision_log.read_text(encoding="utf-8")
            decision_log.write_text(
                reviewed_log.replace("Review outcome: approve", f"Review outcome: {outcome}", 1),
                encoding="utf-8",
            )
            pre_render_error = pre_render_review_error(
                initiative, reviewed_state, outcome_candidate, outcome_digest
            ) or ""
            require(
                "Review outcome: approve exactly" in pre_render_error,
                f"pre-render validation accepted invalid decision record outcome {outcome!r}: {pre_render_error}",
            )
            decision_log.write_text(reviewed_log, encoding="utf-8")
        record_review(initiative, candidate_html)
        require(
            pre_render_review_error(initiative, reviewed_state, candidate_html, candidate_digest) is None,
            "literal decision record approval must remain valid",
        )
        # Exact evaluator P1 regression: a passed-looking marker must not
        # override pending structured review metadata, even when its referenced
        # decision record also binds a different candidate SHA.
        unsafe_state = state.read_text(encoding="utf-8")
        state.write_text(
            unsafe_state.replace('coverage_reviewer: "fixture-reviewer"', "coverage_reviewer: null", 1)
            .replace('reviewed_at: "2026-08-29"', "reviewed_at: null", 1)
            .replace('findings_status: "pass"', 'findings_status: "pending"', 1),
            encoding="utf-8",
        )
        decision_log = initiative / "decision-log.md"
        decision_log.write_text(
            decision_log.read_text(encoding="utf-8").replace(
                "Candidate SHA-256: ", "Candidate SHA-256: " + "0" * 64 + " # ", 1
            ),
            encoding="utf-8",
        )
        unsafe = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate))
        require(unsafe.returncode != 0, "renderer accepted passed marker over pending review metadata and mismatched record SHA")
        require("computed lifecycle authority projection" in unsafe.stderr, unsafe.stderr)
        state.write_text(unsafe_state, encoding="utf-8")
        record_review(initiative, candidate.read_text(encoding="utf-8"))
        digest = hashlib.sha256(candidate.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        decision_log.write_text(
            decision_log.read_text(encoding="utf-8").replace(
                f"Candidate SHA-256: {digest}", f"Candidate SHA-256: {'0' * 64}", 1
            )
            + f"\n## D-901 — unrelated digest\n\nCandidate SHA-256: {digest}\n",
            encoding="utf-8",
        )
        stray_digest = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate))
        require(stray_digest.returncode != 0, "renderer accepted a digest found only in another decision record")
        require("resolved pre-render review record does not bind" in stray_digest.stderr, stray_digest.stderr)
        record_review(initiative, candidate.read_text(encoding="utf-8"))
        pending_state = state.read_text(encoding="utf-8")
        state.write_text(
            pending_state.replace('current_phase: "render_pending"', 'current_phase: "specify"', 1),
            encoding="utf-8",
        )
        stale_phase = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate))
        require(stale_phase.returncode != 0, "renderer accepted a stale current_phase")
        require("current_phase must be \"render_pending\"" in stale_phase.stderr, stale_phase.stderr)
        require(not target.exists(), "stale current_phase exposed a delivered brief")
        state.write_text(pending_state, encoding="utf-8")
        promoted = run(sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate))
        require(promoted.returncode == 0, promoted.stderr)
        rendered_html = target.read_text(encoding="utf-8")
        require('data-brief-phase="rendered"' in rendered_html, "renderer did not materialize rendered phase")
        require(RENDERED_AUTHORITY_TEXT in rendered_html, "renderer did not materialize pending post-render authority")
        require(RENDERED_REVIEW_STATUS_TEXT in rendered_html, "renderer did not materialize the signed pre-render/post-render-pending view")
        require(rendered_html.count(RENDERED_AUTHORITY_TEXT) == 1, "renderer did not replace the declared authority surface")
        require("candidate</p>" not in rendered_html, "renderer did not replace only the declared authority marker")
        require(
            "represented: checkpoint e próximo passo seguro." in rendered_html,
            "coverage authority projection overwrote a required factual coverage disposition",
        )
        require("Esteira de decisão" in rendered_html, "renderer changed non-allowlisted authored bytes")
        state_digest = hashlib.sha256(state.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        require(f'content="{state_digest}"' in rendered_html, "rendered state digest does not bind final state bytes")
        final_state_scalar = f'next_safe_step: "{RENDERED_NEXT_STEP_TEXT}"'
        require(final_state_scalar in rendered_html, "main promotion retained a pre-render run-state provenance fragment")
        require(old_state_scalar not in rendered_html, "main promotion did not replace the cited pre-render run-state scalar")
        require('brief_phase: "rendered"' in state.read_text(encoding="utf-8"), "renderer did not update phase")
        require(
            'current_phase: "rendered_decision_review_pending"' in state.read_text(encoding="utf-8"),
            "renderer did not atomically update the declared current phase",
        )
        require(lifecycle_span in progress.read_text(encoding="utf-8") and lifecycle_span in handoff.read_text(encoding="utf-8"), "promotion rewrote progress or handoff narrative")
        progress_digest = hashlib.sha256(progress.read_bytes()).hexdigest()
        progress_block = re.search(r'<[^>]*data-source="progress\.md"[^>]*>', rendered_html)
        require(progress_block is not None and f'data-source-digest="sha256:{progress_digest}"' in progress_block.group(0), "rendered progress provenance digest did not bind the promoted source")
        require(not (consumer / ".harness" / "assets" / "brand" / "pearson-logo-white.png").exists(), "vendor-neutral promotion provisioned a Pearson logo")
        post_render = run(sys.executable, str(ROOT / "scripts" / "validate_human_visibility.py"), "--consumer-root", str(consumer), "--initiative", "specs/001-render-guard")
        require(post_render.returncode != 0, "rendering was incorrectly accepted as Human Visibility approval")
        require("decision-quality review" in post_render.stdout, post_render.stdout)

        selected_created = run(sys.executable, str(SCAFFOLDER), "pearson-render", "--consumer-root", str(consumer))
        require(selected_created.returncode == 0, selected_created.stderr)
        selected_initiative = consumer / "specs" / "002-pearson-render"
        selected_state = selected_initiative / "run-state.yaml"
        ready_to_render(selected_state)
        selected_candidate = consumer / "pearson-reviewed-candidate.html"
        selected_candidate.write_text(
            fully_reviewed_candidate(selected_initiative, pearson_candidate_html()), encoding="utf-8"
        )
        record_review(selected_initiative, selected_candidate.read_text(encoding="utf-8"))
        selected = run(sys.executable, str(RENDERER), str(selected_initiative), "--candidate", str(selected_candidate))
        require(selected.returncode == 0, selected.stderr)
        logo = consumer / ".harness" / "assets" / "brand" / "pearson-logo-white.png"
        require(logo.is_file(), "selected Pearson promotion did not provision its local logo")
        require(
            hashlib.sha256(logo.read_bytes()).hexdigest().upper()
            == "8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7",
            "selected Pearson promotion provisioned the wrong logo bytes",
        )

        # A declared source span remains authored context; it must never
        # become a third transaction member beside HTML and run-state.
        context_created = run(sys.executable, str(SCAFFOLDER), "ready-next-recovery", "--consumer-root", str(consumer))
        require(context_created.returncode == 0, context_created.stderr)
        context = consumer / "specs" / "003-ready-next-recovery"
        context_state_path = context / "run-state.yaml"
        ready_to_render(context_state_path)
        context_progress = context / "progress.md"
        context_progress.write_text(
            context_progress.read_text(encoding="utf-8")
            + '\n<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-next-safe-step" fragment="arbitrary source next step" -->'
            + PRE_RENDER_READY_NEXT_STEP_TEXT
            + '<!-- /sdd-lifecycle-authority -->\n',
            encoding="utf-8",
        )
        context_candidate = fully_reviewed_candidate(context, valid_candidate_html())
        context_state = context_state_path.read_text(encoding="utf-8")
        require(
            source_lifecycle_error(
                context_progress, context_progress.read_text(encoding="utf-8"), context_state,
                initiative=context, candidate_html=context_candidate,
            ) is None,
            "ready generic source next-step did not receive candidate context",
        )
        context_original_progress = context_progress.read_text(encoding="utf-8")
        context_rendered_state = rendered_lifecycle_state(context_state, context, context_candidate)
        context_updates = declared_source_lifecycle_updates(
            context, context_state, context_rendered_state, context_candidate,
        )
        require(context_progress in context_updates, "declared ready next-step source was not staged")
        try:
            promote_bundle(
                context / "stakeholder-brief.html", context_state_path, "NEW_HTML",
                context_rendered_state, context_updates, "rename_state",
            )
        except ValueError as error:
            require("only supports" in str(error), "multi-source promotion was refused for the wrong reason")
        else:
            raise AssertionError("multi-source promotion was accepted")
        require(context_progress.read_text(encoding="utf-8") == context_original_progress, "rejected multi-source promotion rewrote authored context")

        # V-022-01/03: the lifecycle surface is closed and every durable
        # commit/recovery boundary leaves only a recoverable old/new pair.
        marker_fixture = with_lifecycle_markers(valid_candidate_html()).replace(
            'data-lifecycle-fragment="final run-state SHA-256"',
            'data-lifecycle-fragment="final run-state SHA-256" data-source-digest="candidate"', 1,
        )
        require(lifecycle_error(marker_fixture) is None, "known lifecycle fixture was rejected")
        require("unknown lifecycle marker" in lifecycle_error(marker_fixture.replace("brief-phase", "invented", 1)), "unknown marker was accepted")
        require("duplicate HTML attributes" in lifecycle_error(marker_fixture.replace('data-lifecycle-marker="brief-phase"', 'data-lifecycle-marker="brief-phase" data-lifecycle-marker="invented"', 1)), "duplicate marker attribute was accepted")
        require("duplicate HTML attributes" in lifecycle_error(marker_fixture.replace('data-lifecycle-source="run-state.yaml"', 'data-lifecycle-source="run-state.yaml" data-lifecycle-source="foreign.yaml"', 1)), "conflicting lifecycle source was accepted")
        authority = '<p data-lifecycle-marker="rendered-authority" data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" data-lifecycle-fragment="brief_phase: rendered">candidate</p>'
        moved_authority = marker_fixture.replace(authority, "", 1).replace("<head>", f"<head>{authority}", 1)
        require("misplaced" in (lifecycle_error(moved_authority) or ""), "authority marker outside body was accepted")
        nested_authority = marker_fixture.replace(
            '>candidate</p>', '><span>candidate</span></p>', 1
        )
        require("raw direct" in (lifecycle_error(nested_authority) or ""), "nested authority content was accepted")
        missing_authority = marker_fixture.replace(authority, "", 1)
        require("at least once" in (lifecycle_error(missing_authority) or ""), "missing authority marker was accepted")
        extra_authority_attribute = marker_fixture.replace(
            'data-lifecycle-fragment="brief_phase: rendered"',
            'data-lifecycle-fragment="brief_phase: rendered" data-lifecycle-extra="x"', 1,
        )
        require("undeclared lifecycle attribute" in (lifecycle_error(extra_authority_attribute) or ""), "authority marker with an extra lifecycle attribute was accepted")
        coverage_authority = marker_fixture.replace(
            authority,
            '<table id="coverage-register"><tbody><tr><td>' + authority + '</td></tr></tbody></table>',
            1,
        )
        require("forbidden inside #coverage-register" in (lifecycle_error(coverage_authority) or ""), "authority marker inside the coverage register was accepted")
        require("undeclared lifecycle attribute" in lifecycle_error(marker_fixture.replace('data-lifecycle-fragment="brief_phase"', 'data-lifecycle-fragment="brief_phase" data-lifecycle-extra="x"', 1)), "undeclared lifecycle attribute was accepted")
        require("exactly once" in lifecycle_error(marker_fixture.replace("</head>", '<meta data-lifecycle-marker="rendered-state-digest" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="x"></head>')), "duplicate marker was accepted")
        old_state = (
            'summary: "candidate ready for guarded refresh"\n'
            'brief_phase: "ready_to_render"\ncurrent_phase: "render_pending"\n'
            'last_safe_checkpoint: "exact pre-render review complete"\n'
            'next_safe_step: "guarded refresh"\n'
        )
        new_state = rendered_lifecycle_state(old_state)
        require(
            new_state == (
                f'summary: "{RENDERED_STATE_SUMMARY_TEXT}"\n'
                'brief_phase: "rendered"\ncurrent_phase: "rendered_decision_review_pending"\n'
                f'last_safe_checkpoint: "{RENDERED_STATE_CHECKPOINT_TEXT}"\n'
                f'next_safe_step: "{RENDERED_NEXT_STEP_TEXT}"\n'
            ),
            "render lifecycle transition did not close the canonical operational scalars",
        )
        for refusing_phase in ("specify", "rendered_decision_review_pending", "blocked"):
            refusing_state = old_state.replace('current_phase: "render_pending"', f'current_phase: "{refusing_phase}"')
            try:
                rendered_lifecycle_state(refusing_state)
            except ValueError as error:
                require("current_phase" in str(error), f"{refusing_phase} was refused for the wrong reason")
            else:
                raise AssertionError(f"renderer accepted non-pending current_phase: {refusing_phase}")
        staged = render_lifecycle(marker_fixture, new_state)
        require("Esteira de decisão" in staged, "render lifecycle rewrote arbitrary authored prose")
        require(staged.count(RENDERED_AUTHORITY_TEXT) == 1, "render lifecycle omitted the generic authority projection")

        generic_layout_a = (
            '<html data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="brief_phase" data-brief-phase="authored">'
            '<head><meta data-lifecycle-marker="rendered-state-digest" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="candidate"></head>'
            '<body><aside data-lifecycle-marker="rendered-authority" data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" data-lifecycle-fragment="summary state">candidate</aside><p>unaltered A</p></body></html>'
        )
        generic_layout_b = (
            '<html data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="brief_phase" data-brief-phase="authored">'
            '<head><meta data-lifecycle-marker="rendered-state-digest" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="candidate"></head>'
            '<body><div class="different"><footer data-lifecycle-marker="rendered-authority" data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" data-lifecycle-fragment="footer state">candidate</footer></div><p>unaltered B</p></body></html>'
        )
        for generic_html, untouched in ((generic_layout_a, "unaltered A"), (generic_layout_b, "unaltered B")):
            require(lifecycle_error(generic_html) is None, "generic authority declaration was rejected")
            generic_rendered = render_lifecycle(generic_html, new_state)
            require(RENDERED_AUTHORITY_TEXT in generic_rendered and untouched in generic_rendered, "generic authority rendering changed non-marker bytes")

        # A composed decision view can opt in to the concise lifecycle status
        # needed inside its body.  The renderer changes that direct hook only;
        # an identical-looking unmarked sentence is authored context and must
        # remain byte-for-byte unchanged.
        review_status_hook = (
            '<aside data-lifecycle-marker="rendered-review-status" '
            'data-lifecycle-source="run-state.yaml" '
            'data-lifecycle-projection="lifecycle-review-status" '
            'data-lifecycle-fragment="review decision state">'
            f'{PRE_RENDER_PENDING_REVIEW_STATUS_TEXT}</aside>'
        )
        review_status_fixture = generic_layout_a.replace(
            '<p>unaltered A</p>',
            review_status_hook + '<p>pre-render review pending (unmarked historical note)</p>',
            1,
        )
        require(lifecycle_error(review_status_fixture) is None, "explicit review-status hook was rejected")
        review_status_rendered = render_lifecycle(review_status_fixture, new_state)
        require(RENDERED_REVIEW_STATUS_TEXT in review_status_rendered, "renderer did not project signed pre-review into rendered post-review status")
        require("pre-render review pending (unmarked historical note)" in review_status_rendered, "renderer rewrote arbitrary lifecycle-looking prose")
        wrong_review_projection = review_status_fixture.replace(
            'data-lifecycle-projection="lifecycle-review-status"',
            'data-lifecycle-projection="lifecycle-authority"', 1,
        )
        require("must bind its computed lifecycle projection" in (lifecycle_error(wrong_review_projection) or ""), "review-status hook accepted a foreign projection")

        # A run-state provenance block can opt in without inheriting any tag,
        # layout, or identifier convention. Only the explicit direct attribute
        # changes; a neighbouring unmarked source digest remains byte-identical.
        digest_marker = (
            ' data-lifecycle-marker="rendered-state-source-digest"'
            ' data-lifecycle-source="run-state.yaml"'
            ' data-lifecycle-fragment="state identity binding"'
        )
        generic_digest_fixture = (
            '<html data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="brief_phase" data-brief-phase="authored">'
            '<head><meta data-lifecycle-marker="rendered-state-digest" data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="candidate"></head>'
            '<body><article data-source="run-state.yaml" data-source-digest="sha256:pre-a"' + digest_marker + '><h2>identity</h2></article>'
            '<aside data-source="run-state.yaml" data-source-digest="sha256:pre-b"' + digest_marker + '>state</aside>'
            '<div data-source="run-state.yaml" data-source-digest="sha256:untouched">unaltered digest</div>'
            '<footer data-lifecycle-marker="rendered-authority" data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" data-lifecycle-fragment="footer state">candidate</footer></body></html>'
        )
        require(lifecycle_error(generic_digest_fixture) is None, "generic run-state digest markers were rejected")
        digest_rendered = render_lifecycle(generic_digest_fixture, new_state)
        final_digest = hashlib.sha256(new_state.encode("utf-8")).hexdigest()
        require(digest_rendered.count(f'data-source-digest="sha256:{final_digest}"') == 2, "declared run-state digests were not refreshed")
        require('data-source-digest="sha256:untouched"' in digest_rendered, "unmarked source digest was rewritten")
        require("<h2>identity</h2>" in digest_rendered and "unaltered digest" in digest_rendered, "digest refresh rewrote nested or neighbouring content")
        expected_digest_rendered = generic_digest_fixture.replace('data-brief-phase="authored"', 'data-brief-phase="rendered"', 1)
        expected_digest_rendered = expected_digest_rendered.replace('content="candidate"', f'content="{final_digest}"', 1)
        expected_digest_rendered = expected_digest_rendered.replace('data-source-digest="sha256:pre-a"', f'data-source-digest="sha256:{final_digest}"', 1)
        expected_digest_rendered = expected_digest_rendered.replace('data-source-digest="sha256:pre-b"', f'data-source-digest="sha256:{final_digest}"', 1)
        expected_digest_rendered = expected_digest_rendered.replace('candidate', RENDERED_AUTHORITY_TEXT, 1)
        require(digest_rendered == expected_digest_rendered, "render lifecycle changed bytes outside explicit marker values")
        foreign_digest_marker = generic_digest_fixture.replace('data-source="run-state.yaml" data-source-digest="sha256:pre-a"', 'data-source="progress.md" data-source-digest="sha256:pre-a"', 1)
        require("must bind data-source=run-state.yaml" in (lifecycle_error(foreign_digest_marker) or ""), "foreign source digest marker was accepted")
        empty_digest_fragment = generic_digest_fixture.replace('data-lifecycle-fragment="state identity binding"', 'data-lifecycle-fragment=""', 1)
        require("requires a non-empty provenance fragment" in (lifecycle_error(empty_digest_fragment) or ""), "unprovenanced digest marker was accepted")

        # Regression for the post-render P1: short authority labels alone are
        # insufficient when an operational paragraph still says that guarded
        # refresh is pending. SPEC 022 declares the only four such direct-text
        # slots. Coverage dispositions are factual source-projection records
        # and must remain literal, outside the rewrite surface.
        spec_022_candidate = SPEC_022_CANDIDATE.read_text(encoding="utf-8")
        require(lifecycle_error(spec_022_candidate) is None, "SPEC 022 candidate lifecycle slots are not closed and valid")
        # The checked-in candidate may be pending or independently reviewed.
        # This negative models the pending state explicitly, so it does not
        # rely on whichever legitimate pre-render checkpoint is current.
        pending_spec_022_candidate = spec_022_candidate.replace(
            PRE_RENDER_READY_AUTHORITY_TEXT, PRE_RENDER_PENDING_AUTHORITY_TEXT
        ).replace(PRE_RENDER_READY_NEXT_STEP_TEXT, PRE_RENDER_PENDING_NEXT_STEP_TEXT)
        # The retained SPEC 022 candidate is historical evidence from a
        # completed promotion.  Validate its marker grammar above, but never
        # combine it with a reverse-engineered pre-render state: that would
        # make its run-state provenance digest stale by construction.  Model
        # the input boundary with a disposable source-first manifest instead.
        source_first_state = (
            'status: "executing"\n'
            'summary: "pre-render candidate"\n'
            'brief_phase: "ready_to_render"\n'
            'current_phase: "render_pending"\n'
            'last_safe_checkpoint: "pre-render checkpoint"\n'
            'next_safe_step: "guarded refresh"\n'
            'brief_review:\n'
            '  author: null\n'
            '  coverage_reviewer: null\n'
            '  reviewed_at: null\n'
            '  review_record: null\n'
            '  findings_status: "not_started"\n'
        )
        source_first_candidate = marker_fixture.replace(
            authority,
            authority.replace("candidate", PRE_RENDER_PENDING_AUTHORITY_TEXT),
            1,
        )
        pre_render_authority = lifecycle_authority_projection(source_first_state)
        require(
            pre_render_authority == PRE_RENDER_PENDING_AUTHORITY_TEXT,
            "source-first fixture did not project pending lifecycle authority",
        )
        require(
            lifecycle_error(source_first_candidate, source_first_state) is None,
            "source-first candidate does not bind its computed pending lifecycle authority",
        )
        forged_ready_candidate = source_first_candidate.replace(
            PRE_RENDER_PENDING_AUTHORITY_TEXT, PRE_RENDER_READY_AUTHORITY_TEXT, 1,
        )
        require(
            lifecycle_error(forged_ready_candidate, source_first_state) is not None,
            "ready authority was accepted without an exact structured review linkage",
        )
        forged_next_step_candidate = pending_spec_022_candidate.replace(
            'data-lifecycle-fragment="progress next-safe-step lifecycle projection"\n          >\n'
            f'            {PRE_RENDER_PENDING_NEXT_STEP_TEXT}',
            'data-lifecycle-fragment="progress next-safe-step lifecycle projection"\n          >\n'
            f'            {PRE_RENDER_READY_NEXT_STEP_TEXT}',
            1,
        )
        require(
            "rendered-next-safe-step text does not bind" in (
                lifecycle_error(forged_next_step_candidate, source_first_state) or ""
            ),
            "declared next-safe-step marker was accepted with a stale lifecycle action",
        )
        post_render_state = rendered_lifecycle_state(source_first_state)
        rendered_spec_022 = render_lifecycle(spec_022_candidate, post_render_state)
        require(rendered_spec_022.count(RENDERED_AUTHORITY_TEXT) == 9, "rendered SPEC 022 omitted an operational authority projection")
        require(rendered_spec_022.count(RENDERED_NEXT_STEP_TEXT) == 2, "rendered SPEC 022 omitted a declared next-safe-step projection")
        # The coverage register is a factual source-projection record.  Its
        # wording can legitimately evolve with its sources, but promotion must
        # preserve the entire declared register byte-for-byte: lifecycle
        # markers are forbidden inside it and the renderer has no authority to
        # rewrite its dispositions.
        coverage_register = re.compile(
            r'(?is)<table\b[^>]*\bid\s*=\s*["\']coverage-register["\'][^>]*>.*?</table\s*>'
        )
        candidate_coverage = coverage_register.search(spec_022_candidate)
        rendered_coverage = coverage_register.search(rendered_spec_022)
        require(candidate_coverage is not None and rendered_coverage is not None, "SPEC 022 coverage register is missing")
        require(candidate_coverage.group(0) == rendered_coverage.group(0), "rendered SPEC 022 changed factual coverage dispositions")
        normalized_rendered_spec_022 = re.sub(r"\s+", " ", rendered_spec_022)
        require("exact pre-render review has passed" not in normalized_rendered_spec_022, "rendered SPEC 022 falsely reused a pre-render approval")
        rendered_operational = normalized_rendered_spec_022
        require("Pre-render candidate;" not in rendered_operational, "rendered SPEC 022 retained pre-render operational authority")
        require("exact confirmation before guarded refresh" not in rendered_operational, "rendered SPEC 022 retained pre-render promotion authority")
        # D-022-033's factual decision record retains its bounded
        # guarded-refresh statement.  It is not an authority marker and must
        # remain literal when lifecycle authority markers are rendered.
        # Empty one declared direct-text lifecycle marker without relying on a
        # particular projection sentence, marker ID, or document layout.  The
        # D-022-038 candidate correctly projects the pending pre-render state,
        # so removing a historical ready-state sentence would be a no-op.
        malformed_operational = pending_spec_022_candidate.replace(
            PRE_RENDER_PENDING_AUTHORITY_TEXT, "", 1,
        )
        require("non-empty raw direct authority text" in (lifecycle_error(malformed_operational) or ""), "empty operational authority marker was accepted")

        # Source lifecycle coordination is opt-in, layout-agnostic, and leaves
        # every unmarked byte alone. It is not a phrase matcher for one SPEC.
        source_a = '<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-authority" fragment="status A" -->Authored candidate; pre-render review pending; not rendered/deliverable; Human Visibility and Tasks Ready false.<!-- /sdd-lifecycle-authority -->\nuntouched A\n'
        source_b = 'prefix\n<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-authority" fragment="status B" -->Authored candidate; pre-render review pending; not rendered/deliverable; Human Visibility and Tasks Ready false.<!-- /sdd-lifecycle-authority -->\nsuffix\n'
        for name, source, untouched in (("alpha.md", source_a, "untouched A"), ("nested/layout.md", source_b, "prefix")):
            updated = rendered_source_lifecycle_content(Path(name), source, new_state)
            require(RENDERED_AUTHORITY_TEXT in updated and untouched in updated, "declared source lifecycle text did not preserve arbitrary layout")

        # Rendering closes the canonical operational state without rewriting
        # narrative sources.  The three root scalars are intentionally a
        # small, stable contract; nested prose and arbitrary source files stay
        # byte-preserved.
        operational_state = (
            'status: "executing"\nbrief_phase: "ready_to_render"\ncurrent_phase: "render_pending"\n'
            f'summary: "{PRE_RENDER_READY_AUTHORITY_TEXT}"\n'
            'last_safe_checkpoint: "exact candidate is ready for guarded refresh"\n'
            'execution:\n'
            f'  working_tree_summary: "{PRE_RENDER_PENDING_AUTHORITY_TEXT}"\n'
            f'next_safe_step: "{PRE_RENDER_READY_NEXT_STEP_TEXT}"\n'
        )
        operational_progress = (
            'Historical decision: guarded refresh was once considered.\n\n'
            '<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-next-safe-step" fragment="progress next safe step" -->'
            f'{PRE_RENDER_PENDING_NEXT_STEP_TEXT}<!-- /sdd-lifecycle-authority -->\n'
        )
        operational_handoff = (
            'Historical decision remains factual.\n\n'
            '<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-next-safe-step" fragment="handoff next safe step" -->'
            f'{PRE_RENDER_PENDING_NEXT_STEP_TEXT}<!-- /sdd-lifecycle-authority -->\n'
        )
        rendered_operational_state = rendered_lifecycle_state(operational_state)
        require(f'summary: "{RENDERED_STATE_SUMMARY_TEXT}"' in rendered_operational_state, "rendered state retained pre-render summary authority")
        require(f'last_safe_checkpoint: "{RENDERED_STATE_CHECKPOINT_TEXT}"' in rendered_operational_state, "rendered state retained a pre-render checkpoint")
        require(f'next_safe_step: "{RENDERED_NEXT_STEP_TEXT}"' in rendered_operational_state, "rendered state retained guarded refresh as its next step")
        require("guarded refresh" not in rendered_operational_state.lower(), "rendered state still names guarded refresh as an active step")
        require(f'  working_tree_summary: "{PRE_RENDER_PENDING_AUTHORITY_TEXT}"' in rendered_operational_state, "state rewrite changed an unrelated nested scalar")
        rendered_operational_html = render_lifecycle(source_first_candidate, rendered_operational_state)
        require(RENDERED_AUTHORITY_TEXT in rendered_operational_html, "HTML did not join the rendered operational projection")
        for source in (operational_progress, operational_handoff):
            rendered_source = rendered_source_lifecycle_content(Path("operational.md"), source, rendered_operational_state)
            require(RENDERED_NEXT_STEP_TEXT in rendered_source, "rendered source retained pre-render next-step authority")
            require(source.splitlines()[0] in rendered_source, "source rewrite changed historical prose")

        # End-to-end regression for the active operational narratives in the
        # real SPEC 022 sources.  A source-first reset makes every declared
        # current-lifecycle span pending; promotion must carry every one of
        # those explicit declarations to the rendered projection.  This
        # exercises the general opt-in contract, not a phrase scan or a
        # rewrite of retained decision history.
        current_spec_022_state = (SPEC_022_INITIATIVE / "run-state.yaml").read_text(encoding="utf-8")
        source_first_spec_022_state = rendered_source_lifecycle_content(
            Path("run-state.yaml"), current_spec_022_state, source_first_state,
        )
        source_first_spec_022_state = re.sub(
            r'(?m)^brief_phase: "(?:rendered|ready_to_render)"$',
            'brief_phase: "ready_to_render"', source_first_spec_022_state, count=1,
        )
        source_first_spec_022_state = re.sub(
            r'(?m)^current_phase: "(?:rendered_decision_review_pending|rendered_decision_review_recorded|render_pending)"$',
            'current_phase: "render_pending"', source_first_spec_022_state, count=1,
        )
        for field, value in (
            ("author", "null"), ("coverage_reviewer", "null"),
            ("reviewed_at", "null"), ("review_record", "null"),
            ("findings_status", '"not_started"'),
        ):
            source_first_spec_022_state = re.sub(
                rf'(?m)^(  {field}: ).*$', rf'\1{value}',
                source_first_spec_022_state, count=1,
            )
        require(
            source_lifecycle_error(Path("run-state.yaml"), source_first_spec_022_state, source_first_spec_022_state) is None,
            "SPEC 022 source-first state did not close its declared lifecycle fields",
        )
        promoted_spec_022_state = rendered_lifecycle_state(source_first_spec_022_state)
        active_operational_sources = (
            SPEC_022_INITIATIVE / "progress.md",
            SPEC_022_INITIATIVE / "handoffs" / "latest-handoff.md",
        )
        for active_source in active_operational_sources:
            current_content = active_source.read_text(encoding="utf-8")
            pending_content = rendered_source_lifecycle_content(
                active_source, current_content, source_first_spec_022_state,
            )
            require(
                pending_content == current_content,
                f"{active_source.name} was unexpectedly transformed before promotion",
            )
            promoted_content = rendered_source_lifecycle_content(
                active_source, pending_content, promoted_spec_022_state,
            )
            require(
                promoted_content == current_content,
                f"{active_source.name} was unexpectedly transformed after promotion",
            )
        require(
            "does not bind the computed lifecycle authority projection" in (source_lifecycle_error(Path("stale.md"), source_a.replace("pre-render review pending", "exact pre-render review has passed", 1), old_state) or ""),
            "stale declared source authority was accepted despite the computed projection",
        )
        # A retained post-render operational projection is not evidence that a
        # source-first candidate may advance.  The same declarative contract
        # must refuse the conflict before an atomic promotion can be staged;
        # this uses arbitrary paths and prose, rather than a fixture-specific
        # phrase, document, marker ID, or layout.
        post_render_operational = source_a.replace(
            PRE_RENDER_PENDING_AUTHORITY_TEXT, RENDERED_AUTHORITY_TEXT, 1,
        )
        with tempfile.TemporaryDirectory() as conflicting_root_name:
            conflicting_root = Path(conflicting_root_name)
            (conflicting_root / "any-operational-source.txt").write_text(
                post_render_operational + "unmarked retained history\n", encoding="utf-8",
            )
            try:
                declared_source_lifecycle_updates(conflicting_root, old_state, new_state)
            except ValueError as error:
                require(
                    "does not bind the computed lifecycle authority projection" in str(error),
                    "source-first conflict was refused for the wrong reason",
                )
            else:
                raise AssertionError("post-render operational authority was accepted for source-first state")
        blocked_state = old_state + 'status: "blocked"\n'
        blocked_authority = lifecycle_authority_projection(blocked_state)
        blocked_source = source_a.replace(PRE_RENDER_PENDING_AUTHORITY_TEXT, blocked_authority, 1)
        require(
            source_lifecycle_error(Path("blocked.md"), blocked_source, blocked_state) is None,
            "a declared source lifecycle authority did not project the blocked checkpoint",
        )
        historical_fact = "Historical pre-render review remains factual; it does not authorize current work."
        blocked_with_history = historical_fact + "\n" + blocked_source
        rendered_blocked = rendered_source_lifecycle_content(Path("blocked.md"), blocked_with_history, new_state)
        require(
            historical_fact in rendered_blocked,
            "source lifecycle rendering rewrote an unmarked historical record",
        )
        require(source_lifecycle_error(Path("x.md"), '<!-- sdd-lifecycle-authority source="run-state.yaml" projection="lifecycle-authority" fragment="x" --><b>nested</b><!-- /sdd-lifecycle-authority -->'), "nested source lifecycle text was accepted")
        require(source_lifecycle_error(Path("x.md"), '<!-- sdd-lifecycle-authority source="other.yaml" projection="lifecycle-authority" fragment="x" -->candidate<!-- /sdd-lifecycle-authority -->'), "foreign source lifecycle binding was accepted")
        with tempfile.TemporaryDirectory() as source_tmp:
            source_root = Path(source_tmp)
            (source_root / "progress.md").write_text(source_a, encoding="utf-8")
            (source_root / "nested").mkdir()
            (source_root / "nested" / "handoff.md").write_text(source_b, encoding="utf-8")
            (source_root / "evidence").mkdir()
            (source_root / "evidence" / "historical.md").write_text(source_a, encoding="utf-8")
            updates = declared_source_lifecycle_updates(source_root, old_state, new_state)
            require(set(path.relative_to(source_root).as_posix() for path in updates) == {"progress.md", "nested/handoff.md"}, "source discovery assumed a fixed SPEC layout or mutated evidence")
            bundle_target, bundle_state = source_root / "stakeholder-brief.html", source_root / "run-state.yaml"
            bundle_target.write_text("OLD_HTML", encoding="utf-8")
            bundle_state.write_text(old_state, encoding="utf-8")
            before_sources = {path: path.read_text(encoding="utf-8") for path in updates}
            # Authored source spans remain unchanged while the recoverable
            # pair survives every commit/recovery interruption.
            for point in COMMIT_POINTS:
                bundle_target.write_text("OLD_HTML", encoding="utf-8")
                bundle_state.write_text(old_state, encoding="utf-8")
                for path, content in before_sources.items():
                    path.write_text(content, encoding="utf-8")
                try:
                    promote_bundle(bundle_target, bundle_state, "NEW_HTML", new_state, {}, point)
                except RuntimeError:
                    pass
                if point.startswith("recovery_"):
                    # Seed a journal first; recovery-only interruptions happen
                    # after the transaction has durably begun.
                    bundle_target.write_text("OLD_HTML", encoding="utf-8")
                    bundle_state.write_text(old_state, encoding="utf-8")
                    for path, content in before_sources.items():
                        path.write_text(content, encoding="utf-8")
                    try:
                        promote_bundle(bundle_target, bundle_state, "NEW_HTML", new_state, {}, "rename_state")
                    except RuntimeError:
                        pass
                    require(recover_promotion(bundle_target, bundle_state, point) is not None, f"bundle recovery fault {point} was not surfaced")
                require(recover_promotion(bundle_target, bundle_state) is None, f"pair lifecycle transaction did not recover at {point}")
                recovered = (bundle_target.read_text(encoding="utf-8"), bundle_state.read_text(encoding="utf-8"))
                require(recovered in {("OLD_HTML", old_state), ("NEW_HTML", new_state)}, f"multi-source recovery exposed a contradictory HTML/state pair at {point}")
                require(all(path.read_text(encoding="utf-8") == before_sources[path] for path in updates), f"pair recovery rewrote authored source context at {point}")
        for point in COMMIT_POINTS:
            protocol = consumer / f"protocol-{point}"
            protocol.mkdir()
            pair_target, pair_state = protocol / "stakeholder-brief.html", protocol / "run-state.yaml"
            pair_target.write_text("OLD_HTML", encoding="utf-8")
            pair_state.write_text(old_state, encoding="utf-8")
            from render_stakeholder_brief import promote_pair
            try:
                promote_pair(pair_target, pair_state, staged, new_state, point)
            except RuntimeError:
                pass
            journal = pair_target.with_name(".stakeholder-brief.html.promotion-journal.json")
            if point.startswith("recovery_"):
                # No recovery fault is meaningful before a journal exists.
                try:
                    promote_pair(pair_target, pair_state, staged, new_state, "rename_state")
                except RuntimeError:
                    pass
                require(recover_promotion(pair_target, pair_state, point) is not None, f"recovery fault {point} was not surfaced")
            require(recover_promotion(pair_target, pair_state) is None, f"recovery did not finish after {point}")
            require(recover_promotion(pair_target, pair_state) is None, f"recovery was not idempotent after {point}")
            pair = (pair_target.read_text(encoding="utf-8"), pair_state.read_text(encoding="utf-8"))
            require(pair in {("OLD_HTML", old_state), (staged, new_state)}, f"{point} exposed contradictory pair: {pair!r}")
            require(not journal.exists(), f"journal survived completed recovery at {point}")
            require(not list(protocol.glob(".*.tmp")), f"orphaned temp survived {point}")

        legacy_target, legacy_state = consumer / "legacy.html", consumer / "legacy-state.yaml"
        legacy_target.write_text("OLD_HTML", encoding="utf-8")
        legacy_state.write_text(old_state, encoding="utf-8")
        legacy_journal = legacy_target.with_name(".legacy.html.promotion-journal.json")
        legacy_journal.write_text(json.dumps({"schema_version": 2, "nonce": "0" * 32, "artifacts": []}), encoding="utf-8")
        require(
            "legacy multi-source" in (recover_promotion(legacy_target, legacy_state) or ""),
            "legacy multi-source recovery was not refused",
        )
        require(legacy_journal.exists(), "refused legacy recovery deleted its journal")

        # Independent signing must not require a second edit of the candidate
        # or its run-state.  That old pattern was self-referential: every
        # attempt to mirror approval into the candidate changed the bytes that
        # the reviewer had just signed.  Exercise the generic pending-input
        # path end-to-end, including mismatched signature negatives.
        signing_consumer = consumer / "pending-signature"
        created = run(sys.executable, str(SCAFFOLDER), "pending-signature", "--consumer-root", str(signing_consumer))
        require(created.returncode == 0, created.stderr)
        signing_initiative = signing_consumer / "specs" / "001-pending-signature"
        signing_state_path = signing_initiative / "run-state.yaml"
        ready_to_render(signing_state_path)
        signing_state = signing_state_path.read_text(encoding="utf-8")
        signing_state_path.write_text(
            signing_state.replace('coverage_reviewer: "fixture-reviewer"', "coverage_reviewer: null", 1)
            .replace('reviewed_at: "2026-08-29"', "reviewed_at: null", 1)
            .replace('findings_status: "pass"', 'findings_status: "pending"', 1),
            encoding="utf-8",
        )
        record_pending_signature(signing_initiative)
        signing_candidate_html = candidate_with_block_digests(
            signing_initiative,
            with_lifecycle_markers(valid_candidate_html().replace(
                'data-composition-provenance="reviewed"',
                'data-composition-provenance="pending"', 1,
            )),
        )
        signing_candidate_html = signing_candidate_html.replace(
            ">candidate</p>", f">{PRE_RENDER_PENDING_AUTHORITY_TEXT}</p>", 1,
        )
        pending_record = review_record_content(
            (signing_initiative / "decision-log.md").read_text(encoding="utf-8"), "D-900"
        ) or ""
        signing_candidate_html = signing_candidate_html.replace(
            "decision-record-sha256:PENDING",
            f"decision-record-sha256:{decision_record_digest(pending_record)}",
        )
        signing_candidate = signing_consumer / "exact-pending-candidate.html"
        signing_candidate.write_text(signing_candidate_html, encoding="utf-8")
        # The renderer reads UTF-8 text (and therefore normalizes platform
        # line endings) before calculating the declared digest.
        signed_digest = hashlib.sha256(signing_candidate_html.encode("utf-8")).hexdigest()
        sign_pending_candidate(signing_initiative, signing_candidate_html)
        signed_state = signing_state_path.read_text(encoding="utf-8")
        require(
            pre_render_review_error(signing_initiative, signed_state, signing_candidate_html, signed_digest) is None,
            "independent signature did not authorize its exact immutable pending candidate",
        )
        require(
            lifecycle_authority_projection(signed_state, signing_initiative, signing_candidate_html) == PRE_RENDER_READY_AUTHORITY_TEXT,
            "valid external signature did not derive guarded refresh authority",
        )
        pending_marker_error = lifecycle_error(signing_candidate_html, signed_state, signing_initiative)
        require(
            pending_marker_error is None,
            f"signed pending candidate was forced to rewrite its conservative lifecycle marker: {pending_marker_error}",
        )
        signing_log = signing_initiative / "decision-log.md"
        approved_log = signing_log.read_text(encoding="utf-8")
        signing_log.write_text(approved_log.replace(signed_digest, "0" * 64, 1), encoding="utf-8")
        require(
            "exact candidate SHA-256" in (pre_render_review_error(
                signing_initiative, signed_state, signing_candidate_html, signed_digest,
            ) or ""),
            "mismatched external signature was accepted",
        )
        signing_log.write_text(approved_log.replace("Reviewer: fixture-reviewer", "Reviewer: fixture-author", 1), encoding="utf-8")
        require(
            "distinct from its author" in (pre_render_review_error(
                signing_initiative, signed_state, signing_candidate_html, signed_digest,
            ) or ""),
            "self-signature was accepted",
        )
        signing_log.write_text(approved_log, encoding="utf-8")
        promoted = run(sys.executable, str(RENDERER), str(signing_initiative), "--candidate", str(signing_candidate))
        require(promoted.returncode == 0, promoted.stderr)
        require(
            hashlib.sha256(signing_candidate.read_text(encoding="utf-8").encode("utf-8")).hexdigest() == signed_digest,
            "promotion rewrote the independently signed candidate",
        )
        require(
            scalar(signing_state_path.read_text(encoding="utf-8"), "brief_phase") == "rendered",
            "signed-pending candidate was not promoted as a rendered pair",
        )

        print("RESULT: source-only scaffold and guarded stakeholder brief promotion passed")
        return 0

        corrupt_target, corrupt_state = consumer / "corrupt.html", consumer / "corrupt-state.yaml"
        corrupt_state.write_text(old_state, encoding="utf-8")
        corrupt_target.with_name(".corrupt.html.promotion-journal.json").write_text("{not json", encoding="utf-8")
        require("cannot recover" in (recover_promotion(corrupt_target, corrupt_state) or ""), "corrupt journal was not refused")

        stale_target, stale_state = consumer / "stale-temp.html", consumer / "stale-temp-state.yaml"
        stale_state.write_text(old_state, encoding="utf-8")
        stale_temp = consumer / ".stale-temp.html.0123456789abcdef0123456789abcdef.tmp"
        stale_temp.write_text("uncommitted", encoding="utf-8")
        require(recover_promotion(stale_target, stale_state) is None and not stale_temp.exists(), "safe pre-journal temporary was not cleaned")
        unsafe_temp = consumer / ".stale-temp.html.not-a-uuid.tmp"
        unsafe_temp.write_text("unknown", encoding="utf-8")
        require("unsafe pre-journal" in (recover_promotion(stale_target, stale_state) or ""), "unsafe pre-journal temporary was not refused")

        victim_target, victim_state = consumer / "victim.html", consumer / "victim-state.yaml"
        victim_target.write_text("NEW_HTML", encoding="utf-8")
        victim_state.write_text(new_state, encoding="utf-8")
        victim = consumer / ".unrelated.tmp"
        victim.write_text("do not delete", encoding="utf-8")
        victim_journal = victim_target.with_name(".victim.html.promotion-journal.json")
        victim_journal.write_text(json.dumps({
            "schema_version": 1,
            "intended": {"target_sha256": hashlib.sha256(b"NEW_HTML").hexdigest(), "state_sha256": hashlib.sha256(new_state.encode("utf-8")).hexdigest()},
            "previous": {"target_existed": True, "state_existed": True, "target_sha256": "x", "state_sha256": "x"},
            "temps": [".unrelated.tmp", ".victim-state.yaml.0123456789abcdef0123456789abcdef.tmp"],
        }), encoding="utf-8")
        require("unsafe temporary path" in (recover_promotion(victim_target, victim_state) or ""), "foreign journal temp was accepted")
        require(victim.exists() and victim_journal.exists(), "recovery deleted unrelated temp or journal")

        # A v2 journal is untrusted recovery input.  These variants must fail
        # before moving, deleting, or rewriting even one unrelated file.
        with tempfile.TemporaryDirectory() as corrupt_root_name:
            corrupt_root = Path(corrupt_root_name)
            corrupt_target, corrupt_state = corrupt_root / "stakeholder-brief.html", corrupt_root / "run-state.yaml"
            marked = corrupt_root / "progress.md"
            evidence = corrupt_root / "evidence" / "T-001.md"
            evidence.parent.mkdir()
            marked.write_text(source_a, encoding="utf-8")
            evidence.write_text("immutable evidence", encoding="utf-8")
            unrelated = corrupt_root / "unrelated.txt"
            unrelated.write_text("do not touch", encoding="utf-8")
            source_update = declared_source_lifecycle_updates(corrupt_root, old_state, new_state)

            def corrupted_bundle(mutator, expected: str) -> None:
                corrupt_target.write_text("OLD_HTML", encoding="utf-8")
                corrupt_state.write_text(old_state, encoding="utf-8")
                marked.write_text(source_a, encoding="utf-8")
                try:
                    promote_bundle(corrupt_target, corrupt_state, "NEW_HTML", new_state, source_update, "rename_state")
                except RuntimeError:
                    pass
                journal_path = corrupt_target.with_name(".stakeholder-brief.html.promotion-journal.json")
                journal_data = json.loads(journal_path.read_text(encoding="utf-8"))
                mutator(journal_data)
                journal_path.write_text(json.dumps(journal_data), encoding="utf-8")
                tracked = (corrupt_target, corrupt_state, marked, evidence, unrelated)
                before = {path: path.read_bytes() if path.exists() else None for path in tracked}
                result = recover_promotion(corrupt_target, corrupt_state) or ""
                require(expected in result, f"corrupt bundle journal was not refused: {expected}")
                require(before == {path: path.read_bytes() if path.exists() else None for path in tracked}, f"corrupt journal {expected} mutated an artifact before refusal")

            def redirect_source(path: str):
                def mutate(data):
                    index = 2
                    nonce = data["nonce"]
                    data["artifacts"][index] = {
                        **data["artifacts"][index], "path": path,
                        "temp": f".{Path(path).name}.{nonce}.{index}.tmp",
                        "backup": f".{Path(path).name}.{nonce}.{index}.promotion-backup",
                    }
                return mutate

            corrupted_bundle(lambda data: data["artifacts"].append(dict(data["artifacts"][0])), "duplicate artifact")
            corrupted_bundle(redirect_source("evidence/T-001.md"), "undeclared source")
            corrupted_bundle(redirect_source("unrelated.txt"), "undeclared source")
            corrupted_bundle(lambda data: data["artifacts"].__setitem__(2, {**data["artifacts"][2], "path": "../unrelated.txt"}), "unsafe source promotion path")
            corrupted_bundle(lambda data: data.__setitem__("nonce", "f" * 32), "unsafe temporary or backup")
            corrupted_bundle(lambda data: data["artifacts"][0].__setitem__("intended_sha256", "0" * 64), "temporary digest mismatch")
            corrupted_bundle(lambda data: data["artifacts"][0].__setitem__("previous_sha256", "0" * 64), "backup digest mismatch")

        # A journal must not turn a pre-created symlink into authority to read,
        # replace, or delete an external file.  Exercise each mutable v2
        # representation; skip only where this platform forbids file links.
        with tempfile.TemporaryDirectory() as symlink_root_name, tempfile.TemporaryDirectory() as external_root_name:
            symlink_root = Path(symlink_root_name)
            external = Path(external_root_name) / "outside.txt"
            external.write_bytes(b"external bytes must remain unchanged")
            symlink_target, symlink_state = symlink_root / "stakeholder-brief.html", symlink_root / "run-state.yaml"
            symlink_source = symlink_root / "progress.md"
            symlink_source.write_text(source_a, encoding="utf-8")
            symlink_updates = declared_source_lifecycle_updates(symlink_root, old_state, new_state)

            def seed_symlink_journal() -> dict[str, object]:
                symlink_target.write_text("OLD_HTML", encoding="utf-8")
                symlink_state.write_text(old_state, encoding="utf-8")
                symlink_source.write_text(source_a, encoding="utf-8")
                try:
                    promote_bundle(symlink_target, symlink_state, "NEW_HTML", new_state, symlink_updates, "rename_state")
                except RuntimeError:
                    pass
                return json.loads(symlink_target.with_name(".stakeholder-brief.html.promotion-journal.json").read_text(encoding="utf-8"))

            try:
                probe = symlink_root / "symlink-probe"
                probe.symlink_to(external)
                probe.unlink()
            except OSError:
                print("SKIP: filesystem does not support file symlinks")
            else:
                for representation in ("source", "temporary", "backup"):
                    journal_data = seed_symlink_journal()
                    source_entry = next(entry for entry in journal_data["artifacts"] if entry["path"] == "progress.md")
                    if representation == "source":
                        linked = symlink_source
                    else:
                        linked = symlink_source.with_name(str(source_entry["temp" if representation == "temporary" else "backup"]))
                    linked.unlink(missing_ok=True)
                    linked.symlink_to(external)
                    before_external = external.read_bytes()
                    result = recover_promotion(symlink_target, symlink_state) or ""
                    require("symlink" in result, f"v2 {representation} symlink was accepted")
                    require(external.read_bytes() == before_external, f"v2 {representation} symlink changed external bytes")
                    linked.unlink()

    print("RESULT: source-only scaffold and guarded stakeholder brief promotion passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
