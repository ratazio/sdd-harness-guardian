#!/usr/bin/env python3
"""Focused T-001 contract fixtures, deliberately not a production HTML validator."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CORE_SOURCES = {
    "spec.md",
    "impact-map.md",
    "plan.md",
    "tasks.md",
    "validation-plan.md",
    "decision-log.md",
}
ALLOWED_COVERAGE = {"represented", "synthesized", "not_applicable", "link_only"}
PROFILES = ("localized/S", "M", "L", "high", "unknown")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def coverage_errors(records: list[dict[str, str]]) -> list[str]:
    """Model the documented source-heading policy without parsing/rendering HTML."""
    errors: list[str] = []
    for record in records:
        coverage = record["coverage"]
        if coverage not in ALLOWED_COVERAGE:
            errors.append(f"unsupported coverage: {coverage}")
        if coverage in {"not_applicable", "link_only"} and not record.get("reason"):
            errors.append(f"missing reason: {record['source']}")
        if record["source"] in CORE_SOURCES and record["material"] == "yes" and coverage == "link_only":
            errors.append(f"core source is link-only: {record['source']}")
        if coverage in {"represented", "synthesized"} and not record.get("target"):
            errors.append(f"missing rendered target: {record['source']}")
    return errors


def v2_gate_errors(state: dict[str, object]) -> list[str]:
    """Exercise lifecycle fixtures only; production enforcement remains T-003."""
    if state["lineage"] == "v1":
        return []

    errors: list[str] = []
    author = state.get("author")
    reviewer = state.get("reviewer")
    composition = state.get("composition")
    review_record = state.get("review_record")
    if state.get("brief_coverage_ready"):
        if not composition:
            errors.append("brief_coverage_ready requires coverage composition")
        if not review_record:
            errors.append("brief_coverage_ready requires review record")
        if not author or not reviewer or author == reviewer:
            errors.append("brief_coverage_ready requires distinct author and reviewer")
    if state.get("tasks_ready"):
        if not state.get("human_visibility_ready"):
            errors.append("tasks_ready requires Human Visibility")
        if not state.get("decisions_propagated"):
            errors.append("tasks_ready requires post-meeting decision propagation")
        if not state.get("brief_regenerated"):
            errors.append("tasks_ready requires regenerated brief")
    return errors


def architecture_outcome(profile: str, *, source_complete: bool, discovery_task: bool) -> str:
    """Missing architecture is blocked or bounded discovery for every profile."""
    assert profile in PROFILES
    if source_complete:
        return "ready"
    return "discovery" if discovery_task else "blocked"


def assert_contains(content: str, *tokens: str) -> None:
    for token in tokens:
        assert token in content, f"missing contract token: {token}"


def test_coverage_policy() -> None:
    valid = [
        {"source": "spec.md", "material": "yes", "coverage": "represented", "target": "#scope", "reason": ""},
        {"source": "tasks.md", "material": "yes", "coverage": "synthesized", "target": "#execution", "reason": ""},
        {"source": "ratchet.md", "material": "no", "coverage": "not_applicable", "target": "", "reason": "No stakeholder-material entry."},
        {"source": "handoffs/latest-handoff.md", "material": "no", "coverage": "link_only", "target": "", "reason": "Archive context only."},
    ]
    assert coverage_errors(valid) == []
    assert "core source is link-only: plan.md" in coverage_errors([
        {"source": "plan.md", "material": "yes", "coverage": "link_only", "target": "", "reason": "Too long."},
    ])
    assert "missing reason: progress.md" in coverage_errors([
        {"source": "progress.md", "material": "no", "coverage": "not_applicable", "target": "", "reason": ""},
    ])


def test_lifecycle_fixtures() -> None:
    positive_v2 = {
        "lineage": "v2", "composition": True, "author": "author-a",
        "reviewer": "reviewer-b", "review_record": True,
        "brief_coverage_ready": True, "human_visibility_ready": True,
        "decisions_propagated": True, "brief_regenerated": True, "tasks_ready": True,
    }
    assert v2_gate_errors(positive_v2) == []

    same_identity = positive_v2 | {"reviewer": "author-a"}
    assert "brief_coverage_ready requires distinct author and reviewer" in v2_gate_errors(same_identity)

    missing_composition = positive_v2 | {"composition": False, "review_record": False, "tasks_ready": False}
    errors = v2_gate_errors(missing_composition)
    assert "brief_coverage_ready requires coverage composition" in errors
    assert "brief_coverage_ready requires review record" in errors

    before_propagation = positive_v2 | {"decisions_propagated": False, "brief_regenerated": False}
    errors = v2_gate_errors(before_propagation)
    assert "tasks_ready requires post-meeting decision propagation" in errors
    assert "tasks_ready requires regenerated brief" in errors

    legacy_v1 = {"lineage": "v1", "tasks_ready": True}
    assert v2_gate_errors(legacy_v1) == [], "legacy v1 must retain its lifecycle"


def test_architecture_fixtures() -> None:
    for profile in PROFILES:
        assert architecture_outcome(profile, source_complete=True, discovery_task=False) == "ready"
        assert architecture_outcome(profile, source_complete=False, discovery_task=False) == "blocked"
        assert architecture_outcome(profile, source_complete=False, discovery_task=True) == "discovery"


def test_repository_contract() -> None:
    visibility = read(".harness/rules/human-visibility.md")
    assert_contains(
        visibility,
        '`data-harness-brief-design="v2"`',
        "Historical or pinned v1 briefs keep",
        "`data-source`, `data-source-section`",
        "`data-coverage`",
        "human-readable coverage table",
        "embedded JSON and a separate coverage sidecar are not",
        "Material headings from `spec.md`",
    )

    lifecycle = read(".harness/workflows/sdd-lifecycle.md")
    assert_contains(lifecycle, "historical/pinned", "brief retains the legacy", "sequence: source artifacts ready", "validation_ready → tasks_drafted (v2)", "validation_ready → human_visibility_ready (v1)")
    ordered = [
        "**Preliminary Task Draft**", "**Coverage Composition**", "**Independent Coverage Review**",
        "**Stakeholder Brief**", "**Decision Meeting and Propagation**", "**Tasks Ready**", "**Implementation**",
    ]
    positions = [lifecycle.index(token) for token in ordered]
    assert positions == sorted(positions), "v2 lifecycle order regressed"

    plan = read(".harness/templates/plan.md")
    assert_contains(plan, "## 4. Architecture readiness and proportionality", "System context", "Data ownership/lifecycle", "Failure behavior", "Rollout/rollback", "## 9. Brief coverage composition (v2 when applicable)")

    state = read(".harness/templates/run-state.yaml")
    assert_contains(state, "brief_lineage: null", "tasks_drafted: false", "brief_coverage_ready: false", "brief_review:", "coverage_reviewer: null")


def main() -> int:
    test_coverage_policy()
    test_lifecycle_fixtures()
    test_architecture_fixtures()
    test_repository_contract()
    print("Brief v2 T-001 contract fixtures passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
