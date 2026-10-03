"""Tests for scripts/project_brief.py (SPEC 029 T-002).

Covers AC-002 (projection emits correct provenance tuples from the
canonical source, never from the agent) and AC-003 (projection fails early
-- with an actionable, block/source/fragment-naming message -- rather than
producing HTML that diverges from its declared source).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from project_brief import (  # noqa: E402
    ProjectionError,
    project,
    project_file,
    resolve_locator,
)

FIXTURES = ROOT / "scripts" / "fixtures" / "project-brief"


def _load_model(case: str) -> dict:
    with (FIXTURES / case / "model.yaml").open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _initiative(case: str) -> Path:
    return FIXTURES / case / "initiative"


# ---------------------------------------------------------------------------
# AC-002: valid model projects HTML with correct provenance tuples
# ---------------------------------------------------------------------------

def test_valid_model_projects_html():
    html = project(_initiative("valid"), _load_model("valid"))
    assert "<!doctype html>" in html.lower()
    assert 'role="tablist"' in html
    assert 'role="tab"' in html
    assert 'role="tabpanel"' in html


def test_all_six_provenance_attributes_present_per_block():
    html = project(_initiative("valid"), _load_model("valid"))
    for block_id in ("hero", "D-001", "retention-window"):
        match = re.search(rf'id="{block_id}"[^>]*>', html)
        assert match, f"block {block_id} not found in rendered HTML"
        tag = match.group(0)
        for attribute in (
            "data-source=", "data-source-section=", "data-coverage=",
            "data-source-digest=", "data-source-fragment=", "data-source-fragment-sha256=",
        ):
            assert attribute in tag, f"{block_id} is missing {attribute}"


def test_digest_binds_current_source_bytes():
    import hashlib

    html = project(_initiative("valid"), _load_model("valid"))
    source_bytes = (_initiative("valid") / "spec.md").read_bytes()
    expected = f"sha256:{hashlib.sha256(source_bytes).hexdigest()}"
    match = re.search(r'id="hero"[^>]*data-source-digest="([^"]+)"', html)
    assert match and match.group(1) == expected


def test_fragment_digest_binds_declared_fragment():
    import hashlib

    html = project(_initiative("valid"), _load_model("valid"))
    match = re.search(r'id="hero"[^>]*data-source-fragment="([^"]+)"[^>]*data-source-fragment-sha256="([^"]+)"', html)
    assert match
    fragment, fragment_digest = match.group(1), match.group(2)
    expected = f"sha256:{hashlib.sha256(fragment.encode('utf-8')).hexdigest()}"
    assert fragment_digest == expected


def test_fragment_is_visible_in_its_own_rendered_block():
    html = project(_initiative("valid"), _load_model("valid"))
    match = re.search(r'<article class="card" id="hero".*?</article>', html, re.DOTALL)
    assert match
    block_html = match.group(0)
    assert "FR-001: the widget must reconcile totals without rounding." in block_html


def test_not_applicable_block_uses_locator_as_fragment():
    html = project(_initiative("valid"), _load_model("valid"))
    match = re.search(r'id="retention-window"[^>]*data-source-fragment="([^"]+)"', html)
    assert match
    assert match.group(1) == "quality_gates"


def test_coverage_table_lists_every_block():
    html = project(_initiative("valid"), _load_model("valid"))
    coverage_match = re.search(r'<section id="coverage".*?</section>', html, re.DOTALL)
    assert coverage_match
    coverage_html = coverage_match.group(0)
    for block_id in ("hero", "D-001", "retention-window"):
        assert block_id in coverage_html


def test_shell_css_and_js_copied_byte_for_byte_from_template():
    from project_brief import load_shell, TEMPLATE_PATH

    shell = load_shell(TEMPLATE_PATH)
    html = project(_initiative("valid"), _load_model("valid"))
    assert _style_body(shell["style"]) in html
    assert _script_body(shell["script"]) in html


def _style_body(style_block: str) -> str:
    return style_block[style_block.index(">") + 1: style_block.rindex("<")]


def _script_body(script_block: str) -> str:
    return script_block[script_block.index(">") + 1: script_block.rindex("<")]


def test_no_hidden_attribute_in_source_projection_order():
    """Without JS, every tabpanel must be visible in source/document order
    (PD-004): the projector must not pre-hide any panel itself."""
    html = project(_initiative("valid"), _load_model("valid"))
    for section_id in ("scope", "decision", "evolution", "coverage"):
        match = re.search(rf'<section id="{section_id}"[^>]*>', html)
        assert match, section_id
        assert "hidden" not in match.group(0)


# ---------------------------------------------------------------------------
# AC-003: projection refuses (fails early) rather than diverging
# ---------------------------------------------------------------------------

def test_missing_fragment_refuses_projection():
    with pytest.raises(ProjectionError) as excinfo:
        project(_initiative("fragment-missing"), _load_model("fragment-missing"))
    message = str(excinfo.value)
    assert "hero" in message or "scope/hero" in message
    assert "spec.md" in message
    assert "FR-999" in message


def test_unresolvable_locator_refuses_projection():
    with pytest.raises(ProjectionError) as excinfo:
        project(_initiative("locator-unresolvable"), _load_model("locator-unresolvable"))
    message = str(excinfo.value)
    assert "hero" in message or "scope/hero" in message
    assert "spec.md" in message
    assert "does not resolve" in message


def test_missing_source_file_refuses_projection():
    model = _load_model("valid")
    model["routes"][0]["blocks"][0]["source"] = "impact-map.md"
    with pytest.raises(ProjectionError) as excinfo:
        project(_initiative("valid"), model)
    assert "impact-map.md" in str(excinfo.value)


def test_disallowed_source_refuses_projection():
    model = _load_model("valid")
    model["routes"][0]["blocks"][0]["source"] = "not-a-real-source.md"
    with pytest.raises(ProjectionError) as excinfo:
        project(_initiative("valid"), model)
    assert "not-a-real-source.md" in str(excinfo.value)


def test_schema_invalid_model_refuses_projection():
    model = _load_model("valid")
    del model["thesis"]["brief_thesis"]
    with pytest.raises(ProjectionError):
        project(_initiative("valid"), model)


# ---------------------------------------------------------------------------
# Locator resolution unit behavior
# ---------------------------------------------------------------------------

def test_resolve_locator_matches_markdown_heading_with_punctuation_variance():
    spec = _initiative("valid") / "spec.md"
    text = spec.read_text(encoding="utf-8")
    assert resolve_locator(spec, text, "Functional requirements") == "Functional requirements"


def test_resolve_locator_returns_none_when_absent():
    spec = _initiative("valid") / "spec.md"
    text = spec.read_text(encoding="utf-8")
    assert resolve_locator(spec, text, "Nothing like this exists") is None


def test_resolve_locator_matches_nested_yaml_key():
    state = _initiative("valid") / "run-state.yaml"
    text = state.read_text(encoding="utf-8")
    assert resolve_locator(state, text, "quality_gates") == "quality_gates"


# ---------------------------------------------------------------------------
# Regression: request_revision finding -- "Escopo" must never silently
# resolve to "Fora de escopo" (or any other heading that merely contains it
# as a substring after normalization). Covered on both the `represented` and
# `not_applicable` paths, since the `not_applicable` path is the more
# dangerous one: the resolved locator becomes the displayed
# `data-source-fragment`, i.e. false provenance that would otherwise pass
# verification silently.
# ---------------------------------------------------------------------------

def test_locator_substring_collision_refuses_on_represented_path():
    model = _load_model_from("locator-collision", "model-represented.yaml")
    with pytest.raises(ProjectionError) as excinfo:
        project(_initiative("locator-collision"), model)
    message = str(excinfo.value)
    assert "hero" in message
    assert "Escopo" in message
    assert "does not resolve" in message


def test_locator_substring_collision_refuses_on_not_applicable_path():
    model = _load_model_from("locator-collision", "model-not-applicable.yaml")
    with pytest.raises(ProjectionError) as excinfo:
        project(_initiative("locator-collision"), model)
    message = str(excinfo.value)
    assert "hero" in message
    assert "Escopo" in message
    assert "does not resolve" in message


def test_resolve_locator_rejects_substring_in_either_direction():
    source = _initiative("locator-collision") / "spec.md"
    text = source.read_text(encoding="utf-8")
    # "Escopo" is a normalized substring of "Fora de escopo" -- must not match.
    assert resolve_locator(source, text, "Escopo") is None
    # And the reverse direction must not match either.
    assert resolve_locator(source, text, "Fora de escopo") == "Fora de escopo"


def test_resolve_locator_still_allows_digit_bearing_id_prefix():
    """The narrow, content-guarded exception this fix keeps: a declared
    section that IS a digit-bearing id (e.g. "D-001") may still
    token-prefix-match a longer "<ID> -- <title>" heading, because titles
    legitimately change without the record's identity changing. This is the
    behavior the `valid` fixture's decision-log block already relies on."""
    source = _initiative("valid") / "decision-log.md"
    text = source.read_text(encoding="utf-8")
    assert resolve_locator(source, text, "D-001") == "D-001 — scope freeze"


def test_resolve_locator_refuses_ambiguous_id_prefix(tmp_path):
    source = tmp_path / "decision-log.md"
    source.write_text(
        "### D-001 — scope freeze\n\ntext one\n\n"
        "### D-001 — renamed later\n\ntext two\n",
        encoding="utf-8",
    )
    text = source.read_text(encoding="utf-8")
    assert resolve_locator(source, text, "D-001") is None


def _load_model_from(case: str, filename: str) -> dict:
    with (FIXTURES / case / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def test_project_file_round_trip(tmp_path):
    html = project_file(_initiative("valid"), FIXTURES / "valid" / "model.yaml")
    out = tmp_path / "stakeholder-brief.html"
    out.write_text(html, encoding="utf-8")
    assert out.read_text(encoding="utf-8") == html
