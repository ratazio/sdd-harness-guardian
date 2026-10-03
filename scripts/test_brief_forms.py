"""Tests for the enumerated presentation forms and profile x domain route
selection (SPEC 029 T-003).

Covers:
  * AC-004 -- a model with a material relation produces an accessible SVG
    with a non-empty text equivalent; two relation graphs with the same
    node/edge set are detected and reported.
  * AC-005 -- `profile: minimal` + `domain: docs` produces a brief with a
    subset of routes, without requiring eight `not_applicable`
    dispositions, and the coverage table (the reviewer's view) lists exactly
    the routes the compositor selected.
  * IR-003 -- a synthetic non-software (`domain: docs`) fixture is the only
    empirical proof in the repository that the schema/projector were not
    optimized for a software domain (all eight `testes/mock-runs/` mocks are
    `domain: software`).

Each of the six non-`prose` forms (`topology`, `sequence`, `matrix`,
`footprint`, `risk-chain`, `dossier`) is exercised at least once.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from project_brief import ProjectionError, project  # noqa: E402
from validate_brief_model import validate as validate_model  # noqa: E402

FIXTURES = ROOT / "scripts" / "fixtures" / "project-brief"


def _load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


FORMS_MODEL = FIXTURES / "forms" / "model.yaml"
FORMS_INITIATIVE = FIXTURES / "forms" / "initiative"
DUP_MODEL = FIXTURES / "forms" / "model-duplicate-topology.yaml"
NON_SOFTWARE_MODEL = FIXTURES / "non-software" / "model.yaml"
NON_SOFTWARE_INITIATIVE = FIXTURES / "non-software" / "initiative"


@pytest.fixture(scope="module")
def forms_html() -> str:
    return project(FORMS_INITIATIVE, _load(FORMS_MODEL))


@pytest.fixture(scope="module")
def non_software_html() -> str:
    return project(NON_SOFTWARE_INITIATIVE, _load(NON_SOFTWARE_MODEL))


# ---------------------------------------------------------------------------
# AC-004: topology/sequence -> accessible SVG with a text equivalent
# ---------------------------------------------------------------------------


def test_topology_block_renders_svg_with_role_img_and_nonempty_aria_label(forms_html):
    match = re.search(r'<article class="card" id="zoom-checkout".*?</article>', forms_html, re.DOTALL)
    assert match, "topology block not found"
    block_html = match.group(0)
    svg_match = re.search(r'<svg role="img"[^>]*aria-label="([^"]+)"', block_html)
    assert svg_match, "expected an <svg role=\"img\"> with an aria-label"
    assert svg_match.group(1).strip(), "aria-label must not be empty"
    assert "<title>" in block_html


def test_topology_block_carries_nonempty_text_equivalent(forms_html):
    match = re.search(r'data-architecture-text-equivalent="([^"]+)"', forms_html)
    assert match, "expected data-architecture-text-equivalent on the diagram"
    assert match.group(1).strip()
    # every node label the model declared for this graph must be recoverable
    # from the text equivalent alone -- that is what "text equivalent" means.
    assert "checkout-service" in match.group(1)
    assert "retry queue" in match.group(1)


def test_topology_legend_states_are_visible_text_not_only_color(forms_html):
    assert "brief-relation-state-legend" in forms_html
    for state in ("proposed", "preserved", "out-of-scope", "discovery"):
        assert state in forms_html, f"state '{state}' must be visible as text somewhere in the page"


def test_sequence_block_reuses_the_same_accessible_svg_mechanism(forms_html):
    match = re.search(r'<article class="card" id="zoom-sequence".*?</article>', forms_html, re.DOTALL)
    assert match
    block_html = match.group(0)
    assert 'data-block-form="sequence"' in block_html
    assert re.search(r'<svg role="img"[^>]*aria-label="[^"]+"', block_html)
    assert "data-architecture-text-equivalent=" in block_html


def test_relation_ref_to_missing_graph_refuses_projection():
    model = _load(FORMS_MODEL)
    model["routes"][0]["blocks"][0]["relation_ref"] = "does-not-exist"
    with pytest.raises(ProjectionError, match="relation_ref"):
        project(FORMS_INITIATIVE, model)


# ---------------------------------------------------------------------------
# AC-004: duplicate topology detection
# ---------------------------------------------------------------------------


def test_duplicate_relation_graphs_are_detected_and_reported():
    model = _load(DUP_MODEL)
    errors = validate_model(model)
    assert errors, "two graphs with an identical node/edge set must be reported"
    joined = " ".join(errors)
    assert "duplicate topology" in joined
    assert "graph-a" in joined and "graph-b" in joined


def test_duplicate_relation_graphs_block_projection():
    model = _load(DUP_MODEL)
    with pytest.raises(ProjectionError, match="duplicate topology"):
        project(FORMS_INITIATIVE, model)


def test_renaming_a_graph_alone_is_not_a_duplicate():
    """A set-diff check, not a name comparison: distinct content under
    distinct ids must never false-positive."""
    model = _load(FORMS_MODEL)
    errors = validate_model(model)
    assert not any("duplicate topology" in e for e in errors)


# ---------------------------------------------------------------------------
# Remaining forms: matrix, footprint, risk-chain, dossier
# ---------------------------------------------------------------------------


def test_matrix_block_renders_a_label_value_table(forms_html):
    match = re.search(r'<article class="card" id="compliance-matrix".*?</article>', forms_html, re.DOTALL)
    assert match
    block_html = match.group(0)
    assert 'data-block-form="matrix"' in block_html
    assert "<table>" in block_html
    assert "checkout-service" in block_html and "payment-gateway-client" in block_html


def test_footprint_block_renders_in_the_impact_footprint_container(forms_html):
    match = re.search(
        r'<div class="brief-impact-footprint">\s*<article id="footprint-surfaces".*?</div>',
        forms_html,
        re.DOTALL,
    )
    assert match, "expected the footprint block wrapped in .brief-impact-footprint"
    assert 'data-block-form="footprint"' in match.group(0)


def test_risk_chain_block_renders_in_the_risk_chain_container(forms_html):
    match = re.search(
        r'<div class="brief-risk-chain">\s*<article id="risk-duplicate-charge".*?</div>',
        forms_html,
        re.DOTALL,
    )
    assert match, "expected the risk-chain block wrapped in .brief-risk-chain"
    block_html = match.group(0)
    assert 'data-block-form="risk-chain"' in block_html
    for field_value in ("double debit", "Idempotency key"):
        assert field_value in block_html


def test_dossier_block_renders_as_a_task_card_with_free_fieldset(forms_html):
    match = re.search(r'<article class="brief-task-card" id="D-002".*?</article>', forms_html, re.DOTALL)
    assert match
    block_html = match.group(0)
    assert 'data-block-form="dossier"' in block_html
    assert "Key every retry attempt by order id" in block_html


def test_all_six_nonprose_forms_carry_full_provenance(forms_html):
    for block_id in (
        "zoom-checkout", "zoom-sequence", "footprint-surfaces",
        "risk-duplicate-charge", "compliance-matrix", "D-002",
    ):
        match = re.search(rf'id="{re.escape(block_id)}"[^>]*>', forms_html)
        assert match, f"block {block_id} not found"
        tag = match.group(0)
        for attribute in (
            "data-source=", "data-source-section=", "data-coverage=",
            "data-source-digest=", "data-source-fragment=", "data-source-fragment-sha256=",
        ):
            assert attribute in tag, f"{block_id} is missing {attribute}"


# ---------------------------------------------------------------------------
# AC-005: profile x domain selects routes; IR-003 non-software fixture
# ---------------------------------------------------------------------------


def test_minimal_docs_model_is_schema_valid():
    model = _load(NON_SOFTWARE_MODEL)
    assert model["profile"] == "minimal"
    assert model["domain"] == "docs"
    errors = validate_model(model)
    assert errors == [], f"non-software fixture must validate cleanly: {errors}"


def test_minimal_docs_selects_a_subset_of_routes_without_na_dispositions(non_software_html):
    for route_id in ("scope", "impact", "decision", "coverage"):
        assert f'id="tab-{route_id}"' in non_software_html
    for route_id in ("architecture", "execution", "validation", "evolution"):
        assert f'id="tab-{route_id}"' not in non_software_html
        assert f'id="{route_id}"' not in non_software_html, (
            f"route '{route_id}' was not selected; it must not appear as a section "
            f"(e.g. an N/A disposition) either -- absence, not eight dispositions (NG-002)"
        )


def test_reviewer_sees_the_same_route_set_the_compositor_selected(non_software_html):
    """The coverage table is the reviewer's view of what was selected; it
    must not silently add or drop a route relative to the model."""
    model = _load(NON_SOFTWARE_MODEL)
    selected = {route["id"] for route in model["routes"]} | {"coverage"}
    tabs = set(re.findall(r'id="tab-([a-z]+)"', non_software_html))
    assert tabs == selected


def test_non_software_fixture_exercises_multiple_forms_without_topology(non_software_html):
    # This domain has no material spatial/structural relation -- `topology`
    # is legitimately unused here, while `sequence` (a temporal relation)
    # still applies and reuses the identical SVG mechanism.
    used_forms = set(re.findall(r'data-block-form="([a-z-]+)"', non_software_html))
    assert used_forms >= {"prose", "footprint", "sequence", "risk-chain", "matrix", "dossier"}
    assert "topology" not in used_forms


def test_non_software_sequence_block_still_produces_accessible_svg(non_software_html):
    match = re.search(r'<article class="card" id="redirect-sequence".*?</article>', non_software_html, re.DOTALL)
    assert match
    block_html = match.group(0)
    assert re.search(r'<svg role="img"[^>]*aria-label="[^"]+"', block_html)
    assert "data-architecture-text-equivalent=" in block_html


def test_non_software_not_applicable_block_still_projects(non_software_html):
    match = re.search(r'id="compliance-notapplicable"[^>]*data-coverage="not_applicable"', non_software_html)
    assert match
    assert "No compliance-scoped data moves with this migration" in non_software_html
