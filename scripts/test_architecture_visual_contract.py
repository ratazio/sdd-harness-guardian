#!/usr/bin/env python3
"""Fixtures for the material-architecture visual contract (SPEC 024 T-002)."""

from __future__ import annotations

from architecture_visual_contract import architecture_visual_errors


PROVENANCE = ('data-source="plan.md" data-source-section="Architecture" '
              'data-coverage="represented" data-architecture-source-backed="true"')


def material_fixture() -> str:
    return f'''<!doctype html><html data-harness-brief-design="v2"><body>
<section id="architecture" data-architecture-visual="material">
  <figure class="brief-architecture-topology" data-architecture-projection="topology" data-architecture-renderer="svg" {PROVENANCE}>
    <svg role="img" aria-label="API de origem envia lote ao serviço, que publica pela API de destino">
      <rect data-architecture-node="API de origem" data-architecture-node-id="source"></rect><rect data-architecture-node="Serviço local" data-architecture-node-id="service"></rect>
      <path data-architecture-relation="ingress" data-architecture-relation-label="envia lote" data-architecture-relation-from="source" data-architecture-relation-to="service"></path>
    </svg>
    <p data-architecture-text-equivalent>A API de origem envia o lote ao serviço local.</p>
    <figcaption class="brief-architecture-legend"><span data-architecture-legend-state="proposed">Proposto</span><span data-architecture-legend-state="preserved">Preservado</span><span data-architecture-legend-state="out-of-scope">Fora do escopo</span><span data-architecture-legend-state="discovery">Descoberta</span></figcaption>
  </figure>
  <section class="brief-architecture-surface-map" data-architecture-projection="surface-map" data-architecture-unit="superfícies declaradas" {PROVENANCE}><div class="brief-architecture-surface" data-architecture-surface="serviço local">Serviço local</div></section>
  <section class="brief-architecture-zoom" data-architecture-projection="zoom" data-architecture-zoom-status="not_applicable" data-architecture-absence-reason="A fonte não define frontend." {PROVENANCE}>Frontend: N/A fonte-apoiado.</section>
</section></body></html>'''


def textual_fallback_fixture() -> str:
    return '''<!doctype html><html data-harness-brief-design="v2"><body>
<section id="architecture" data-architecture-visual="material">
  <p>API de origem → serviço → modelo → API de destino. A fonte descreve as relações.</p>
  <div class="diagram">Topologia textual, sem projeção estrutural.</div>
</section></body></html>'''


def disconnected_svg_bypass_fixture() -> str:
    return (material_fixture()
            .replace(' data-architecture-relation-from="source" data-architecture-relation-to="service"', "")
            .replace('>Proposto</span>', '></span>').replace('>Preservado</span>', '></span>')
            .replace('>Fora do escopo</span>', '></span>').replace('>Descoberta</span>', '></span>'))


def empty_semantic_html_bypass_fixture() -> str:
    return (material_fixture()
            .replace('data-architecture-renderer="svg"', 'data-architecture-renderer="semantic-html"')
            .replace('>A API de origem envia o lote ao serviço local.</p>', '></p>')
            .replace('>Proposto</span>', '></span>').replace('>Preservado</span>', '></span>')
            .replace('>Fora do escopo</span>', '></span>').replace('>Descoberta</span>', '></span>'))


def additional_missing_endpoint_bypass_fixture() -> str:
    return material_fixture().replace(
        '</svg>',
        '<path data-architecture-relation="unknown" data-architecture-relation-label="publica" data-architecture-relation-from="missing" data-architecture-relation-to="service"></path></svg>',
    )


def self_relation_bypass_fixture() -> str:
    return material_fixture().replace(
        'data-architecture-relation-from="source" data-architecture-relation-to="service"',
        'data-architecture-relation-from="source" data-architecture-relation-to="source"',
    )


def main() -> int:
    positive = architecture_visual_errors(material_fixture())
    assert positive == [], positive

    negative = architecture_visual_errors(textual_fallback_fixture())
    for expected in (
        "material architecture requires a topology projection",
        "material architecture requires a surface-map projection",
        "material architecture requires a zoom projection",
    ):
        assert expected in negative, negative

    disconnected = architecture_visual_errors(disconnected_svg_bypass_fixture())
    require_disconnected = (
        "material architecture topology requires each relation to declare non-empty data-architecture-relation-from and data-architecture-relation-to",
        "material architecture topology legend state proposed must have non-empty visible text",
    )
    for expected in require_disconnected:
        assert expected in disconnected, disconnected

    semantic_empty = architecture_visual_errors(empty_semantic_html_bypass_fixture())
    for expected in (
        "material architecture topology requires a non-empty data-architecture-text-equivalent",
        "material architecture topology legend state discovery must have non-empty visible text",
    ):
        assert expected in semantic_empty, semantic_empty

    missing_endpoint = architecture_visual_errors(additional_missing_endpoint_bypass_fixture())
    assert "material architecture topology relation endpoints must reference declared data-architecture-node-id values" in missing_endpoint, missing_endpoint

    self_relation = architecture_visual_errors(self_relation_bypass_fixture())
    assert "material architecture topology relation endpoints must identify distinct declared node IDs" in self_relation, self_relation

    # A local/non-software brief remains free from decorative SVG obligations.
    immaterial = '''<section id="architecture" data-architecture-visual="not-material" data-architecture-visual-reason="No source-backed architecture affects the decision.">Policy wording only.</section>'''
    assert architecture_visual_errors(immaterial) == []
    print("Architecture visual contract fixtures: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
