#!/usr/bin/env python3
"""Build the fresh SPEC 021 T-004 laboratory without reusing r5 outcomes.

The base builder is intentionally reused only for source-only scaffolding and
the guarded renderer.  This wrapper replaces the candidate composition with
case-derived governance and relationship surfaces.  It never writes a
baseline or a qualitative approval.
"""
from __future__ import annotations

import hashlib
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
OLD = ROOT / "specs" / "020-source-render-isolation-and-canonical-brief-composition" / "evidence" / "build_mock_lab.py"
RUN_ROOT = ROOT / "testes" / "mock-runs" / "20260830-spec021-t004-r15"

spec = importlib.util.spec_from_file_location("spec020_mock_lab", OLD)
assert spec and spec.loader
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
renderer_spec = importlib.util.spec_from_file_location("guardian_renderer", ROOT / "scripts" / "render_stakeholder_brief.py")
assert renderer_spec and renderer_spec.loader
renderer = importlib.util.module_from_spec(renderer_spec)
renderer_spec.loader.exec_module(renderer)
ORIGINAL_COMPOSE = base.complete_candidate
ORIGINAL_RUN = base.run
ORIGINAL_RECORD = base.record_text
ORIGINAL_STATE = base.fresh_state


def source_backed_assurance(initiative: Path) -> str:
    """Recover the authored assurance declaration without a domain taxonomy.

    The source corpus owns the value and wording.  This parser only locates
    the explicit labelled declaration already emitted by the specification;
    it neither assigns an assurance tier nor supplies a fallback tier.
    """
    source = (initiative / "spec.md").read_text(encoding="utf-8")
    match = re.search(r"\*\*Risco(?:/assurance)?\s*:\*\*\s*(.+?)(?=\s+\*\*|\n|$)", source)
    if not match:
        raise ValueError("spec.md must declare an explicit Risco/assurance source value")
    return match.group(1)


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def material_ratchet(initiative: Path) -> tuple[str, str]:
    source = initiative / "ratchet.md"
    raw = source.read_text(encoding="utf-8")
    anchor = base.source_anchor(source)
    provenance = (
        f'data-source="ratchet.md" data-source-section="Ratchet" data-coverage="synthesized" data-source-digest="sha256:{base.file_digest(source)}" '
        f'data-source-fragment="{html.escape(anchor, quote=True)}" '
        f'data-source-fragment-sha256="sha256:{digest(anchor)}"'
    )
    body = html.escape(raw)
    if "no entries" in raw.lower() or "sem entradas" in raw.lower():
        summary = "Estado vazio justificado: não há regra preventiva específica nesta fonte; a ausência não autoriza inventar um gate."
    else:
        summary = "Regra preventiva material recuperada abaixo: gatilho, check, owner e consequência permanecem decisão de fonte, não inferência do renderizador."
    return provenance, f"<section id=\"conditional-governance\" {provenance}><h2>Governança condicional da fonte</h2><p>{summary}</p><pre class=\"source-extract\">{body}</pre><span class=\"provenance-anchor\">Fonte condicional: ratchet.md — {html.escape(anchor)}</span></section>"


def relation(mock_id: str, initiative: Path) -> str:
    item = base.CASE_CONTENT[mock_id]
    source = initiative / "plan.md"
    anchor = base.source_anchor(source)
    attrs = (
        f'data-source="plan.md" data-source-section="Architecture and operations" data-coverage="synthesized" data-source-digest="sha256:{base.file_digest(source)}" '
        f'data-source-fragment="{html.escape(anchor, quote=True)}" '
        f'data-source-fragment-sha256="sha256:{digest(anchor)}"'
    )
    # The relationship wording comes from the effective case corpus.  There is
    # deliberately no mock/domain classifier or fixed choice of diagram type.
    rows = "".join(
        f"<tr><th>{label}</th><td>{html.escape(text)}</td></tr>"
        for label, text in (("Fluxo e fronteiras", item["flow"]), ("Dados e posse", item["data"]), ("Falha e recuperação", item["risk"]), ("Operação", item["operations"]))
    )
    return f"<section id=\"source-driven-relations\" {attrs}><h2>Relações materiais recuperáveis</h2><p>Esta estrutura registra as relações que este corpus torna materiais; não representa uma taxonomia nem uma forma obrigatória.</p><table><tbody>{rows}</tbody></table><span class=\"provenance-anchor\">Relação derivada de plan.md — {html.escape(anchor)}</span></section>"


def composed(mock_id: str, initiative: Path, decision: str) -> str:
    candidate = ORIGINAL_COMPOSE(mock_id, initiative, decision)
    assurance = source_backed_assurance(initiative)
    candidate, replacements = re.subn(
        r"(<strong>Risco/assurance</strong><br>)[^<]+",
        lambda match: match.group(1) + html.escape(assurance),
        candidate,
        count=1,
    )
    if replacements != 1:
        raise ValueError("base candidate lacks the declared assurance projection slot")
    attrs, governance = material_ratchet(initiative)
    candidate = candidate.replace("</main>", relation(mock_id, initiative) + governance + "</main>", 1)
    candidate = candidate.replace(
        "</tbody></table></section>",
        '<tr><td>ratchet.md § conditional preventive state</td><td><a href="#conditional-governance">#conditional-governance</a></td><td>synthesized</td></tr></tbody></table></section>',
        1,
    )
    candidate = candidate.replace(
        'data-brief-phase="authored"',
        'data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml" '
        'data-lifecycle-fragment="brief_phase" data-brief-phase="authored" '
        'data-spec021-conditional-source="ratchet"', 1)
    candidate = candidate.replace(
        "<head>",
        '<head><meta data-lifecycle-marker="rendered-state-digest" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" content="pending-render" />', 1)
    candidate = candidate.replace(
        "<main>",
        '<main><p class="eyebrow" data-lifecycle-marker="rendered-authority" '
        'data-lifecycle-source="run-state.yaml" data-lifecycle-projection="lifecycle-authority" '
        'data-lifecycle-fragment="T-004 lifecycle authority">'
        'Authored candidate; exact pre-render review has passed; ready only for guarded refresh; not rendered/deliverable; Human Visibility and Tasks Ready false.</p>', 1)
    return candidate


def guarded_run(command: list[str]) -> None:
    """Adapt the historical fixture state to the current renderer lifecycle."""
    ORIGINAL_RUN(command)


def record_text(initiative: Path, candidate_digest: str) -> str:
    return (ORIGINAL_RECORD(initiative, candidate_digest)
            + f"Composition manifest SHA-256: {renderer.canonical_composition_manifest(initiative)}\n"
            + "Human attestation: confirmed\n")


def fresh_state(name: str, mock_id: str) -> str:
    return (ORIGINAL_STATE(name, mock_id)
            .replace('status: "rendered_pending_independent_review"', 'status: "executing"')
            .replace('current_phase: "human_visibility_review"', 'current_phase: "render_pending"')
            .replace('findings_status: "pass; source coverage reviewed before rendering"', 'findings_status: "pass"'))


def rebuild_existing_case(mock_id: str, case_dir: str, slug: str) -> dict[str, str]:
    """Recompose one disposable r15 consumer from its canonical sources.

    This intentionally recreates the candidate, exact D-100 binding and
    guarded render rather than patching delivered HTML.  It is restricted to
    an already-created r15 consumer selected by the caller.
    """
    consumer = RUN_ROOT / case_dir
    initiative = consumer / "specs" / f"001-{slug}"
    if not initiative.is_dir():
        raise FileNotFoundError(f"missing r15 initiative for {mock_id}: {initiative}")
    (initiative / "run-state.yaml").write_text(
        fresh_state(initiative.name, mock_id), encoding="utf-8"
    )
    log_path = initiative / "decision-log.md"
    old_log = log_path.read_text(encoding="utf-8")
    record_row = base.record_index_row()
    prefix, separator, _ = old_log.partition(record_row)
    if not separator:
        raise ValueError(f"{mock_id} has no replaceable D-100 record row")
    prefix = prefix.rstrip() + "\n\n"
    log_path.write_text(prefix + record_row + record_text(initiative, "PENDING"), encoding="utf-8")
    candidate_html = composed(mock_id, initiative, record_text(initiative, "PENDING"))
    candidate_digest = hashlib.sha256(candidate_html.encode("utf-8")).hexdigest()
    log_path.write_text(prefix + record_row + record_text(initiative, candidate_digest), encoding="utf-8")
    candidate = consumer / "reviewed-candidate.html"
    candidate.write_text(candidate_html, encoding="utf-8")
    base.run([sys.executable, str(base.RENDERER), str(initiative), "--candidate", str(candidate), "--refresh"])
    return {
        "mock": mock_id,
        "consumer_root": str(consumer.relative_to(ROOT)).replace("\\", "/"),
        "initiative": str(initiative.relative_to(consumer)).replace("\\", "/"),
        "request_sha256": base.file_digest(base.REQUESTS[mock_id]),
        "sources_sha256": hashlib.sha256(
            b"".join((initiative / source).read_bytes() for source in base.CANONICAL)
        ).hexdigest(),
        "html_sha256": base.file_digest(initiative / "stakeholder-brief.html"),
    }


def rebuild_selected_existing(mock_ids: set[str]) -> dict[str, dict[str, str]]:
    allowed = {"M-005", "M-006"}
    if not mock_ids or not mock_ids <= allowed:
        raise ValueError("only the scoped M-005/M-006 assurance repair may rebuild existing r15 consumers")
    by_id = {case[0]: case for case in base.CASES}
    manifest_path = RUN_ROOT / "run-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    records = {entry["mock"]: entry for entry in manifest["cases"]}
    rebuilt = {}
    for mock_id in sorted(mock_ids):
        rebuilt[mock_id] = rebuild_existing_case(*by_id[mock_id])
        records[mock_id] = rebuilt[mock_id]
    manifest["cases"] = [records[case[0]] for case in base.CASES]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return rebuilt


def main() -> int:
    if RUN_ROOT.exists():
        raise SystemExit(f"refusing to reuse fresh run root: {RUN_ROOT}")
    base.RUN_ROOT = RUN_ROOT
    base.complete_candidate = composed
    base.run = guarded_run
    base.record_text = record_text
    base.fresh_state = fresh_state
    records = [base.build_case(*case) for case in base.CASES]
    manifest = {"run_id": RUN_ROOT.name, "kind": "SPEC-021-T-004", "baseline": False, "cases": records}
    (RUN_ROOT / "run-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    selected = set(sys.argv[1:])
    if selected:
        print(json.dumps(rebuild_selected_existing(selected), indent=2))
    else:
        raise SystemExit(main())
