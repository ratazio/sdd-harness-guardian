#!/usr/bin/env python3
"""Project a `brief-model.yaml` (SPEC 029 T-001 schema) into the stakeholder
brief HTML shell (SPEC 029 T-002).

Scope and boundary (plan.md PD-003, PD-004; spec.md FR-002, FR-003, NG-001,
NG-003):

  * The agent authors the model. This projector authors NOTHING semantic: it
    does not summarize Markdown, does not choose a visual form (that is
    T-003), does not write narrative, does not infer topology. Every word a
    reader sees in `text`/`fields`/`fragment` comes verbatim from the model
    or is copied verbatim from the canonical source. The projector's only
    "decisions" are mechanical: resolve a locator, read bytes, compute a
    digest, verify a fragment, emit markup.
  * It reads the canonical source **only** to resolve `source`/`source_section`
    (does the locator exist?) and `fragment` (does this literal text occur in
    the source and in the rendered block?) -- never to derive content.
  * `.harness/templates/stakeholder-brief.html` is the read-only template.
    Its `<style>` and `<script>` blocks are copied byte-for-byte into every
    projected page (PD-004): CSS, JS, a11y (focus-visible, tablist keyboard
    handling) and print (`@media print`) behavior are unchanged. The a11y
    evidence approved in SPECs 013/014 continues to apply to that shell
    unchanged (NG-003: no redesign here).
  * Visual forms (`topology`, `sequence`, `matrix`, `footprint`, `risk-chain`,
    `dossier`, `prose`) are enumerated in the schema; each has its own
    renderer in `FORM_RENDERERS` (T-003), calibrated against what real briefs
    in `testes/mock-runs/` actually use, reusing the shell's existing CSS
    classes (`.card`, `.brief-task-card`, `.brief-impact-footprint`,
    `.brief-risk-chain`, `.matrix`, `.diagram`) rather than inventing new
    visual identity (NG-003). `topology`/`sequence` (and `risk-chain` when it
    carries a `relation_ref`) render the model's node/edge `relations[]` as
    an accessible SVG (`role="img"`, non-empty `aria-label`/`title`, a
    `data-architecture-text-equivalent` and a visible text legend of the four
    edge states) instead of hand-authored markup (FR-004). `render_generic_block`
    remains a defensive fallback for a `form` value outside the schema's
    closed enum; it should not run against a schema-valid model.

Failing early (FR-003) is the point of this module: a locator that does not
resolve, or a fragment that is not literally present in the canonical source
(or not visible in its own rendered block), raises `ProjectionError` naming
the offending block, source and fragment -- it never silently degrades.
"""

from __future__ import annotations

import hashlib
import html
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from brief_v2_sources import V2_REQUIRED_SOURCES  # noqa: E402
from validate_brief_model import validate as validate_model  # noqa: E402

# Historical projection emits contract 2; the direct-authored default is 3.
# Its read-only shell remains packaged so upgrades cannot silently change
# legacy output or impose the contract 3 repair protocol on a model.
TEMPLATE_PATH = ROOT / "scripts" / "fixtures" / "tabbed-brief-surface" / "template-v2.html"

ROUTE_TITLES: dict[str, str] = {
    "scope": "Value & scope",
    "architecture": "Architecture",
    "impact": "Impact",
    "execution": "Execution",
    "validation": "Validation",
    "evolution": "Evolution",
    "decision": "Decision",
    "coverage": "Coverage",
}

# The only sources a block may cite. Reused, not redefined, from the
# render pipeline's own closed inventory -- one vocabulary, not two.
ALLOWED_BLOCK_SOURCES = set(V2_REQUIRED_SOURCES)


class ProjectionError(Exception):
    """Raised when the model cannot be projected without synthesizing
    content or without a verifiable provenance binding. The message always
    names the offending block, source and (when relevant) fragment, per
    FR-003 -- this is what makes divergence between the model and the HTML
    structurally impossible instead of merely discouraged."""


# ---------------------------------------------------------------------------
# Shell extraction (PD-004): copy CSS/JS byte-for-byte from the read-only
# template instead of re-declaring or re-deriving them.
# ---------------------------------------------------------------------------

def _extract_between(text: str, open_pattern: str, close_marker: str) -> str:
    match = re.search(open_pattern, text)
    if not match:
        raise ProjectionError(f"shell template is missing an expected block: {open_pattern!r}")
    start = match.end()
    end = text.index(close_marker, start)
    return text[match.start():end + len(close_marker)]


def load_shell(template_path: Path = TEMPLATE_PATH) -> dict[str, str]:
    """Return the byte-for-byte CSS and JS blocks from the read-only shell
    template. Never edit the template; only read it."""
    text = template_path.read_text(encoding="utf-8")
    style_block = _extract_between(text, r"<style[^>]*>", "</style>")
    script_block = _extract_between(text, r"<script[^>]*>", "</script>")
    return {"style": style_block, "script": script_block}


# ---------------------------------------------------------------------------
# Locator resolution (FR-003, first clause): does source/source_section
# resolve in the canonical source at all?
# ---------------------------------------------------------------------------

def _normalize_locator(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def _tokenize_locator(text: str) -> tuple[str, ...]:
    """Split into alnum word tokens (lowercased), dropping punctuation as a
    separator rather than deleting it. Used for the digit-bearing-ID prefix
    exception in `resolve_locator`, where token BOUNDARIES matter: "D-001"
    must prefix-match "D-001 -- scope freeze" (tokens d, 001, scope, freeze)
    without letting "Escopo" prefix-match into "Fora de escopo" (tokens
    fora, de, escopo) -- the latter is a real word appearing at a different
    token position, not a truncated version of the same id/heading.
    """
    return tuple(re.findall(r"[a-z0-9]+", text.lower()))


def _markdown_locators(text: str) -> set[str]:
    locators: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        match = re.match(r"^#{1,6}\s+(.*)$", stripped)
        if match:
            locators.add(match.group(1).strip())
            continue
        # Decision/task/validation records often use a bold-ish dash heading
        # rather than a Markdown heading, e.g. "### T-001 -- title" is
        # already covered above; but some ledgers use "## D-004 -- ..." only
        # at heading level, which the regex above already captures. No
        # additional heuristic is added here: only literal heading lines are
        # candidate locators, by design (a paragraph is not a locator).
    return locators


def _yaml_locators(doc: Any, prefix: str = "") -> set[str]:
    locators: set[str] = set()
    if isinstance(doc, dict):
        for key, value in doc.items():
            key_str = str(key)
            path = f"{prefix}.{key_str}" if prefix else key_str
            locators.add(key_str)
            locators.add(path)
            locators |= _yaml_locators(value, path)
    elif isinstance(doc, list):
        for item in doc:
            locators |= _yaml_locators(item, prefix)
    return locators


def _source_locators(path: Path, raw_text: str) -> set[str]:
    if path.suffix.lower() in (".yaml", ".yml"):
        import yaml

        try:
            doc = yaml.safe_load(raw_text)
        except Exception:
            return set()
        return _yaml_locators(doc)
    return _markdown_locators(raw_text)


def resolve_locator(path: Path, raw_text: str, section: str) -> str | None:
    """Return the literal candidate string the section resolves to, or None.

    Matching is on a normalized (lowercased, punctuation-stripped) form so
    that e.g. declared section "2 Objetivo" resolves against the heading
    "## 2. Objetivo" -- but the returned value is the literal, unnormalized
    text as it occurs in the source, so callers can use it verbatim as a
    guaranteed-literal fragment (used for `not_applicable`/absence blocks,
    which carry no positive `fragment` field of their own).

    An EXACT normalized match always resolves. There is deliberately no
    general substring/"partial" fallback: an earlier version accepted a
    candidate when the normalized target was a substring of it (or vice
    versa), which let e.g. a declared section "Escopo" silently resolve to a
    heading "Fora de escopo" when "Escopo" itself no longer existed in the
    source (substring containment in either direction, post
    punctuation-stripping, made "escopo" match "foradeescopo"). That is
    exactly the failure FR-003 exists to prevent: a source that changed
    since the model was authored (EC-001) must cause a refusal, not a
    silent resolution to a heading of opposite or unrelated meaning --
    especially dangerous on the `not_applicable` path, where the resolved
    locator becomes the displayed `data-source-fragment` (false provenance
    passing verification).

    The one narrow exception is a digit-bearing declared section (an ID like
    "D-001", "T-001", "V-004", "FR-001", or a numbered heading like "2
    Objetivo") token-prefix-matching a longer heading such as "D-001 --
    scope freeze": ledgers commonly title a record "<ID> -- <title>", and
    requiring the full title in `source_section` would make every model
    brittle to editorial title changes that do not change the record's
    identity. This is guarded on CONTENT, not length: it only fires when the
    declared section itself contains a digit (so a bare word like "Escopo"
    can never use it), and it refuses (returns None) instead of guessing
    when more than one DISTINCT heading shares that prefix -- an ambiguous
    prefix is a collision, not a resolution.

    If no match exists, or a prefix match is ambiguous, this returns None
    and the caller refuses the projection.
    """
    target_norm = _normalize_locator(section.lstrip("#").strip())
    if not target_norm:
        return None
    candidates = _source_locators(path, raw_text)

    exact = sorted({c for c in candidates if _normalize_locator(c) == target_norm})
    if exact:
        # Multiple literal headings can normalize identically only when they
        # are the same text modulo punctuation/case -- not a content
        # collision -- so picking the first in a stable sort is safe.
        return exact[0]

    target_tokens = _tokenize_locator(section)
    if not any(ch.isdigit() for ch in target_norm) or not target_tokens:
        return None
    prefix_matches = sorted({
        c for c in candidates
        if _tokenize_locator(c)[: len(target_tokens)] == target_tokens
    })
    if len(prefix_matches) == 1:
        return prefix_matches[0]
    # Zero matches: unresolved. Two-or-more DISTINCT headings sharing the
    # same id prefix: ambiguous -- refuse rather than pick one by length.
    return None


# ---------------------------------------------------------------------------
# Source resolution + provenance tuple computation
# ---------------------------------------------------------------------------

def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_source(initiative: Path, block_ref: str, source: str) -> tuple[Path, bytes, str]:
    if source not in ALLOWED_BLOCK_SOURCES:
        raise ProjectionError(
            f"block '{block_ref}': source '{source}' is not in the allowed source "
            f"inventory ({sorted(ALLOWED_BLOCK_SOURCES)})"
        )
    source_path = initiative / source
    if not source_path.is_file():
        raise ProjectionError(
            f"block '{block_ref}': canonical source '{source}' does not exist under {initiative}"
        )
    raw_bytes = source_path.read_bytes()
    try:
        raw_text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ProjectionError(f"block '{block_ref}': source '{source}' is not valid UTF-8: {exc}") from exc
    return source_path, raw_bytes, raw_text


def compute_provenance(initiative: Path, route_id: str, block: dict[str, Any]) -> dict[str, str]:
    """Resolve locator/digest/fragment for one block against the canonical
    source, per PD-003. Raises ProjectionError (naming block, source,
    fragment) on any of the two FR-003 failure modes."""
    block_ref = f"{route_id}/{block.get('id', '<missing id>')}"
    source = block.get("source", "")
    section = block.get("source_section", "")
    coverage = block.get("coverage", "")

    source_path, raw_bytes, raw_text = _read_source(initiative, block_ref, source)

    matched_locator = resolve_locator(source_path, raw_text, section)
    if matched_locator is None:
        raise ProjectionError(
            f"block '{block_ref}': source_section '{section}' does not resolve in "
            f"source '{source}' -- no heading/key in that source matches"
        )

    digest = _sha256_hex(raw_bytes)

    if coverage == "not_applicable":
        # An absence has no positive fragment to lift (schema comment on
        # `fragment`). Ground it in the literal locator text instead, which
        # is guaranteed to occur verbatim in the source because it was
        # extracted from that source's own heading/key list.
        fragment = matched_locator
    else:
        fragment = block.get("fragment", "")
        if not fragment:
            raise ProjectionError(f"block '{block_ref}': coverage '{coverage}' requires a fragment")
        if fragment not in raw_text:
            raise ProjectionError(
                f"block '{block_ref}': fragment {fragment!r} does not occur literally in "
                f"source '{source}' -- the agent must copy it verbatim from the canonical source"
            )

    fragment_digest = _sha256_hex(fragment.encode("utf-8"))

    return {
        "data-source": source,
        "data-source-section": section,
        "data-coverage": coverage,
        "data-source-digest": f"sha256:{digest}",
        "data-source-fragment": fragment,
        "data-source-fragment-sha256": f"sha256:{fragment_digest}",
    }


def _verify_fragment_visible(block_ref: str, fragment: str, rendered_text: str) -> None:
    if fragment not in rendered_text:
        raise ProjectionError(
            f"block '{block_ref}': fragment {fragment!r} is not visible in its own rendered "
            f"block -- the projector must render what it verified, verbatim"
        )


# ---------------------------------------------------------------------------
# Block rendering. `prose` is fully implemented; every other form uses the
# shared generic renderer below -- the explicit T-003 extension point.
# ---------------------------------------------------------------------------

def _esc(text: str) -> str:
    return html.escape(text, quote=True)


def _attrs(provenance: dict[str, str], extra: dict[str, str] | None = None) -> str:
    parts = [f'{name}="{_esc(value)}"' for name, value in provenance.items()]
    for name, value in (extra or {}).items():
        parts.append(f'{name}="{_esc(value)}"')
    return " ".join(parts)


def _render_absence(absence: dict[str, Any]) -> str:
    kind = absence.get("kind")
    if kind == "not_applicable":
        return f'<p class="absence-reason">{_esc(absence.get("reason", ""))}</p>'
    parts = [f'<p class="absence-discovery-fact">{_esc(absence.get("missing_fact", ""))}</p>',
             f'<p class="absence-discovery-impact">{_esc(absence.get("decision_impact", ""))}</p>']
    if absence.get("owner"):
        parts.append(f'<p class="absence-discovery-owner">Owner: {_esc(absence["owner"])}</p>')
    if absence.get("path"):
        parts.append(f'<p class="absence-discovery-path">Path: {_esc(absence["path"])}</p>')
    return "\n          ".join(parts)


def _render_fields(fields: list[dict[str, str]]) -> str:
    if not fields:
        return ""
    rows = "".join(
        f"\n            <dt>{_esc(f['label'])}</dt><dd>{_esc(f['value'])}</dd>" for f in fields
    )
    return f'<dl class="fields">{rows}\n          </dl>'


def _citation(provenance: dict[str, str]) -> str:
    """The visible citation line: makes the verified fragment human-visible,
    which is also what guarantees it is present in the rendered block
    (FR-003's second clause)."""
    return (
        f'<p class="source"><cite>{_esc(provenance["data-source"])}'
        f' &middot; {_esc(provenance["data-source-section"])}</cite>'
        f' &mdash; &ldquo;{_esc(provenance["data-source-fragment"])}&rdquo;</p>'
    )


def render_prose_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    body = []
    if block.get("coverage") == "not_applicable" and block.get("absence"):
        body.append(f'<div class="absence">{_render_absence(block["absence"])}</div>')
    elif block.get("text"):
        body.append(f'<p>{_esc(block["text"])}</p>')
    body.append(_render_fields(block.get("fields", [])))
    body.append(_citation(provenance))
    body_html = "\n          ".join(part for part in body if part)
    return (
        f'<article class="card" id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": "prose"})}>\n'
        f"          {body_html}\n        </article>"
    )


def render_generic_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """Fallback for a `form` value the schema enumerates but that has no
    dedicated renderer registered in FORM_RENDERERS (defensive only -- the
    schema's `form` enum is closed to the seven values T-003 implements, so
    this path is not expected to run for a schema-valid model). Renders
    authored text/fields plus the verified citation, tagged with
    `data-block-form` so nothing is silently lost."""
    form = block.get("form", "prose")
    body = []
    if block.get("coverage") == "not_applicable" and block.get("absence"):
        body.append(f'<div class="absence">{_render_absence(block["absence"])}</div>')
    else:
        if block.get("text"):
            body.append(f'<p>{_esc(block["text"])}</p>')
        body.append(_render_fields(block.get("fields", [])))
        if block.get("relation_ref"):
            body.append(f'<p class="relation-ref" data-relation-ref="{_esc(block["relation_ref"])}"></p>')
    body.append(_citation(provenance))
    body_html = "\n          ".join(part for part in body if part)
    return (
        f'<article class="card" id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": form})}>\n'
        f"          {body_html}\n        </article>"
    )


# ---------------------------------------------------------------------------
# Relation graphs -> accessible SVG (FR-004, AC-004). Shared by `topology`,
# `sequence` and `risk-chain` (when the latter carries a `relation_ref`):
# the schema comment on `relation_ref` names all three as consumers of
# relations[]. The layout is deliberately a single deterministic left-to-right
# row -- it is a text-equivalent-bearing diagram, not a design system (NG-003:
# no new visual identity), reusing the shell's own CSS custom properties
# (--violet/--green/--amber/--danger/--muted/--line) so it inherits the
# existing palette instead of inventing one.
# ---------------------------------------------------------------------------

STATE_LABELS: tuple[str, ...] = ("proposed", "preserved", "out-of-scope", "discovery")

_STATE_STROKE: dict[str, str] = {
    "proposed": "var(--violet)",
    "preserved": "var(--green)",
    "out-of-scope": "var(--amber)",
    "discovery": "var(--danger)",
}


def _relation_text_equivalent(graph: dict[str, Any]) -> str:
    """Plain-text description of every node and edge -- always non-empty for
    a schema-valid graph (minItems: 1 on nodes). This is what makes the
    diagram's meaning available to a reader who cannot see color or shape
    (FR-004: 'estados visíveis como texto -- nunca só por cor')."""
    nodes = graph.get("nodes", []) or []
    edges = graph.get("edges", []) or []
    node_desc = "; ".join(f"{n['id']} ({n['label']})" for n in nodes)
    if edges:
        edge_desc = "; ".join(
            f"{e.get('from')} -> {e.get('to')}: {e.get('label')} [{e.get('state')}]" for e in edges
        )
    else:
        edge_desc = "no relations declared between these nodes"
    return f"Nodes: {node_desc}. Relations: {edge_desc}."


def _render_relation_svg(graph: dict[str, Any], aria_label: str) -> str:
    nodes = graph.get("nodes", []) or []
    edges = graph.get("edges", []) or []
    node_w, node_h, gap, top = 170, 64, 70, 24
    count = max(len(nodes), 1)
    width = count * node_w + max(count - 1, 0) * gap + 40
    height = top * 2 + node_h + 40
    positions = {node["id"]: (20 + i * (node_w + gap), top) for i, node in enumerate(nodes)}

    parts = [
        f'<svg role="img" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'aria-label="{_esc(aria_label)}" focusable="false">',
        f"<title>{_esc(aria_label)}</title>",
        '<defs><marker id="brief-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" '
        'orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="var(--muted)" /></marker></defs>',
    ]
    for edge in edges:
        origin = positions.get(edge.get("from"))
        target = positions.get(edge.get("to"))
        if origin is None or target is None:
            continue
        x1, y1 = origin[0] + node_w, origin[1] + node_h / 2
        x2, y2 = target[0], target[1] + node_h / 2
        stroke = _STATE_STROKE.get(edge.get("state", ""), "var(--line)")
        mx, my = (x1 + x2) / 2, min(y1, y2) - 8
        parts.append(
            f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
            f'stroke="{stroke}" stroke-width="2" marker-end="url(#brief-arrow)" />'
        )
        parts.append(
            f'<text x="{mx:.0f}" y="{my:.0f}" font-size="11" text-anchor="middle">'
            f'{_esc(edge.get("label", ""))} ({_esc(edge.get("state", ""))})</text>'
        )
    for node in nodes:
        x, y = positions[node["id"]]
        parts.append(
            f'<rect x="{x}" y="{y}" width="{node_w}" height="{node_h}" rx="10" '
            f'fill="#fff" stroke="var(--violet)" stroke-width="2" />'
        )
        parts.append(
            f'<text x="{x + node_w / 2:.0f}" y="{y + node_h / 2:.0f}" font-size="13" '
            f'text-anchor="middle" dominant-baseline="middle">{_esc(node.get("label", ""))}</text>'
        )
    parts.append("</svg>")
    return "".join(parts)


def _render_state_legend() -> str:
    """A visible-text legend of the four edge states (FR-004): state meaning
    is never carried by color alone."""
    return '<p class="brief-relation-state-legend">States: ' + "; ".join(STATE_LABELS) + "</p>"


def _relation_graph_html(block: dict[str, Any], relations: dict[str, Any], *, kind: str) -> str:
    ref = block.get("relation_ref")
    if not ref or ref not in relations:
        raise ProjectionError(
            f"block '{block.get('id')}': form '{kind}' requires relation_ref to a graph "
            f"declared in the model's top-level relations[]"
        )
    graph = relations[ref]
    label = graph.get("label") or graph.get("id")
    text_equivalent = _relation_text_equivalent(graph)
    svg = _render_relation_svg(graph, label)
    return (
        f'<div class="diagram" data-relation-ref="{_esc(ref)}" '
        f'data-architecture-text-equivalent="{_esc(text_equivalent)}">'
        f"{svg}"
        f'<p class="brief-relation-text-equivalent">{_esc(text_equivalent)}</p>'
        f"{_render_state_legend()}"
        "</div>"
    )


def render_topology_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """FR-004/AC-004: a material relation renders as an accessible SVG
    (`role="img"`, non-empty `aria-label`/`title`) plus its text equivalent,
    never as a bare `data-architecture-node`/`-relation` pair a human has to
    reconstruct by reading markup."""
    body = [_relation_graph_html(block, relations, kind="topology")]
    if block.get("text"):
        body.append(f'<p>{_esc(block["text"])}</p>')
    body.append(_render_fields(block.get("fields", [])))
    body.append(_citation(provenance))
    body_html = "\n          ".join(part for part in body if part)
    return (
        f'<article class="card" id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": "topology"})}>\n'
        f"          {body_html}\n        </article>"
    )


def render_sequence_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """A temporal/ordering relation (e.g. a retry or redirect sequence). It
    shares topology's graph-to-SVG mechanics -- both are node/edge relations,
    the difference is what the relation *means* to the reader, which the
    block's own `text`/`form_reason` carries, not a different rendering
    engine (NG-003: no second diagram implementation to keep in sync)."""
    body = [_relation_graph_html(block, relations, kind="sequence")]
    if block.get("text"):
        body.append(f'<p>{_esc(block["text"])}</p>')
    body.append(_render_fields(block.get("fields", [])))
    body.append(_citation(provenance))
    body_html = "\n          ".join(part for part in body if part)
    return (
        f'<article class="card" id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": "sequence"})}>\n'
        f"          {body_html}\n        </article>"
    )


def render_risk_chain_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """A named risk's signal->consequence->control->owner chain. `fields` is
    the common shape (schema comment: risk-chain is a `fields` consumer); a
    `relation_ref` is accepted too when the risk is itself a graph (e.g. a
    cascading-failure path), reusing the same SVG renderer as topology."""
    inner: list[str] = []
    if block.get("relation_ref"):
        inner.append(_relation_graph_html(block, relations, kind="risk-chain"))
    if block.get("coverage") == "not_applicable" and block.get("absence"):
        inner.append(f'<div class="absence">{_render_absence(block["absence"])}</div>')
    else:
        if block.get("text"):
            inner.append(f'<p>{_esc(block["text"])}</p>')
        inner.append(_render_fields(block.get("fields", [])))
    inner.append(_citation(provenance))
    inner_html = "\n            ".join(part for part in inner if part)
    return (
        '<div class="brief-risk-chain">\n'
        f'          <article id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": "risk-chain"})}>\n'
        f'            <h3>{_esc(block["id"])}</h3>\n'
        f"            {inner_html}\n"
        "          </article>\n"
        "        </div>"
    )


def render_footprint_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """One affected-surface card, reusing the shell's `.brief-impact-footprint`
    grid (existing CSS -- no redesign, NG-003)."""
    inner: list[str] = []
    if block.get("coverage") == "not_applicable" and block.get("absence"):
        inner.append(f'<div class="absence">{_render_absence(block["absence"])}</div>')
    else:
        if block.get("text"):
            inner.append(f'<p>{_esc(block["text"])}</p>')
        inner.append(_render_fields(block.get("fields", [])))
    inner.append(_citation(provenance))
    inner_html = "\n            ".join(part for part in inner if part)
    return (
        '<div class="brief-impact-footprint">\n'
        f'          <article id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": "footprint"})}>\n'
        f'            <h3>{_esc(block["id"])}</h3>\n'
        f"            {inner_html}\n"
        "          </article>\n"
        "        </div>"
    )


def render_matrix_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """`fields` becomes a two-column Label/Value table (the shell's own
    `.matrix table` -- e.g. a scope crosswalk or compliance table -- reads
    better as rows than as a definition list."""
    fields = block.get("fields", [])
    table_html = ""
    if fields:
        rows = "".join(f"<tr><td>{_esc(f['label'])}</td><td>{_esc(f['value'])}</td></tr>" for f in fields)
        table_html = (
            '<table><thead><tr><th>Element</th><th>Value</th></tr></thead>'
            f"<tbody>{rows}</tbody></table>"
        )
    inner: list[str] = [f'<div class="matrix">{table_html}</div>'] if table_html else []
    if block.get("coverage") == "not_applicable" and block.get("absence"):
        inner.append(f'<div class="absence">{_render_absence(block["absence"])}</div>')
    elif block.get("text"):
        inner.append(f'<p>{_esc(block["text"])}</p>')
    inner.append(_citation(provenance))
    inner_html = "\n          ".join(part for part in inner if part)
    return (
        f'<article class="card" id="{_esc(block["id"])}" {_attrs(provenance, {"data-block-form": "matrix"})}>\n'
        f"          {inner_html}\n        </article>"
    )


def render_dossier_block(block: dict[str, Any], provenance: dict[str, str], relations: dict[str, Any]) -> str:
    """A multi-attribute record (task, decision, proof...), reusing the
    shell's `.brief-task-card` shape. `fields` is a free list of label/value
    pairs (T-001 finding: real briefs use different field sets for the same
    `form: dossier` -- the shape is fixed, the fieldset is not)."""
    inner: list[str] = []
    if block.get("coverage") == "not_applicable" and block.get("absence"):
        inner.append(f'<div class="absence">{_render_absence(block["absence"])}</div>')
    elif block.get("text"):
        inner.append(f'<p>{_esc(block["text"])}</p>')
    inner.append(_render_fields(block.get("fields", [])))
    inner.append(_citation(provenance))
    inner_html = "\n          ".join(part for part in inner if part)
    return (
        f'<article class="brief-task-card" id="{_esc(block["id"])}" '
        f'{_attrs(provenance, {"data-block-form": "dossier"})}>\n'
        f'          <h3>{_esc(block["id"])}</h3>\n'
        f"          {inner_html}\n        </article>"
    )


FORM_RENDERERS = {
    "prose": render_prose_block,
    "topology": render_topology_block,
    "sequence": render_sequence_block,
    "risk-chain": render_risk_chain_block,
    "footprint": render_footprint_block,
    "matrix": render_matrix_block,
    "dossier": render_dossier_block,
}


def render_block(
    initiative: Path, route_id: str, block: dict[str, Any], relations: dict[str, Any]
) -> tuple[str, dict[str, str]]:
    provenance = compute_provenance(initiative, route_id, block)
    renderer = FORM_RENDERERS.get(block.get("form", "prose"), render_generic_block)
    block_html = renderer(block, provenance, relations)
    _verify_fragment_visible(f"{route_id}/{block['id']}", provenance["data-source-fragment"], block_html)
    return block_html, provenance


# ---------------------------------------------------------------------------
# Route / page assembly
# ---------------------------------------------------------------------------

def render_route(
    initiative: Path, index: int, route: dict[str, Any], relations: dict[str, Any]
) -> tuple[str, str, list[dict[str, str]]]:
    """Return (nav_tab_html, tabpanel_html, coverage_rows) for one route."""
    route_id = route["id"]
    title = ROUTE_TITLES.get(route_id, route_id.title())
    is_first = index == 0
    tab_html = (
        f'<a id="tab-{route_id}" role="tab" href="?view={route_id}" '
        f'aria-controls="{route_id}" aria-selected="{"true" if is_first else "false"}" '
        f'tabindex="{0 if is_first else -1}">{_esc(title)}</a>'
    )
    blocks_html = []
    coverage_rows: list[dict[str, str]] = []
    for block in route.get("blocks", []):
        block_html, provenance = render_block(initiative, route_id, block, relations)
        blocks_html.append(block_html)
        coverage_rows.append({
            "route": route_id,
            "block": block["id"],
            **provenance,
        })
    panel_html = (
        f'<section id="{route_id}" class="tab-panel brief-route" role="tabpanel" '
        f'aria-labelledby="tab-{route_id}" tabindex="0">\n'
        f'        <h2 class="route-title">{_esc(title)}</h2>\n'
        + "\n        ".join(blocks_html)
        + "\n      </section>"
    )
    return tab_html, panel_html, coverage_rows


def render_coverage_table(coverage_rows: list[dict[str, str]]) -> str:
    header = (
        "<tr><th>Route</th><th>Block</th><th>Source</th><th>Section</th>"
        "<th>Coverage</th><th>Fragment</th></tr>"
    )
    rows = []
    for row in coverage_rows:
        rows.append(
            "<tr>"
            f"<td>{_esc(row['route'])}</td>"
            f"<td>{_esc(row['block'])}</td>"
            f"<td>{_esc(row['data-source'])}</td>"
            f"<td>{_esc(row['data-source-section'])}</td>"
            f"<td>{_esc(row['data-coverage'])}</td>"
            f"<td>{_esc(row['data-source-fragment'])}</td>"
            "</tr>"
        )
    return (
        '<div class="coverage-wrap"><table class="coverage">'
        f"<thead>{header}</thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


def project(initiative: Path, model: dict[str, Any], *, template_path: Path = TEMPLATE_PATH) -> str:
    """Project `model` (already loaded brief-model.yaml document, T-001
    schema) into final stakeholder-brief HTML. Raises ProjectionError,
    naming the offending block/source/fragment, on any FR-003 violation."""
    errors = validate_model(model)
    if errors:
        raise ProjectionError("model failed schema validation: " + "; ".join(errors))

    shell = load_shell(template_path)
    relations = {g["id"]: g for g in (model.get("relations") or []) if isinstance(g, dict) and g.get("id")}

    routes = model["routes"]
    if not any(route["id"] == "coverage" for route in routes):
        routes = list(routes) + [{
            "id": "coverage",
            "blocks": [],
        }]

    tabs, panels, coverage_rows = [], [], []
    for index, route in enumerate(routes):
        if route["id"] == "coverage" and not route.get("blocks"):
            continue
        tab_html, panel_html, rows = render_route(initiative, index, route, relations)
        tabs.append(tab_html)
        panels.append(panel_html)
        coverage_rows.extend(rows)

    coverage_index = len(tabs)
    coverage_tab = (
        f'<a id="tab-coverage" role="tab" href="?view=coverage" aria-controls="coverage" '
        f'aria-selected="false" tabindex="-1">Coverage</a>'
    )
    coverage_panel = (
        '<section id="coverage" class="tab-panel brief-route" role="tabpanel" '
        'aria-labelledby="tab-coverage" tabindex="0">\n'
        '        <h2 class="route-title">Coverage</h2>\n'
        f"        {render_coverage_table(coverage_rows)}\n"
        "      </section>"
    )
    tabs.append(coverage_tab)
    panels.append(coverage_panel)

    thesis = model["thesis"]
    title = _esc(model.get("domain", "") + " brief")
    header_html = (
        '<header class="brief-header">\n'
        '        <p class="eyebrow">Decision brief</p>\n'
        f'        <h1>{_esc(thesis["brief_thesis"])}</h1>\n'
        f'        <p class="lede">{_esc(thesis["decision_and_audience"])}</p>\n'
        "      </header>"
    )

    body = f"""<!doctype html>
<html lang="en" data-brief-contract="2" data-harness-template-kind="composed" data-brief-phase="composed" data-brief-model-schema-version="{_esc(model["contract_version"])}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>{title}</title>
    <style data-harness-brief-shell data-brief-base-stylesheet="v1">{_style_body(shell["style"])}</style>
  </head>
  <body class="brief-shell" data-tab-enhancement="fallback">
    <noscript>
      <aside class="brief-no-script" data-noscript-fallback="continuous-reading" role="status">
        <strong>Navegação por subpáginas indisponível.</strong> Este brief requer JavaScript para alternar as abas e recuperar a URL de cada visão. Abaixo está somente a alternativa de leitura contínua; ela não equivale à experiência de subpáginas.
      </aside>
    </noscript>
    <main class="shell">
      <div class="topbar"><span class="tag">{_esc(model.get("domain", ""))} &middot; {_esc(model.get("profile", ""))}</span></div>
      {header_html}
      <nav class="route-nav" aria-label="Brief decision views" role="tablist">
        {"".join(tabs)}
      </nav>
      {"".join(panels)}
    </main>
    <script data-brief-base-behavior="v1">{_script_body(shell["script"])}</script>
  </body>
</html>
"""
    return body


def _style_body(style_block: str) -> str:
    # style_block is "<style ...>...body...</style>"; return only the body.
    return style_block[style_block.index(">") + 1: style_block.rindex("<")]


def _script_body(script_block: str) -> str:
    return script_block[script_block.index(">") + 1: script_block.rindex("<")]


def project_file(initiative: Path, model_path: Path, *, template_path: Path = TEMPLATE_PATH) -> str:
    import yaml

    with model_path.open(encoding="utf-8") as fh:
        model = yaml.safe_load(fh)
    return project(initiative, model, template_path=template_path)


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: project_brief.py <initiative_dir> <brief-model.yaml> <output.html>", file=sys.stderr)
        return 2
    initiative = Path(argv[1])
    model_path = Path(argv[2])
    output_path = Path(argv[3])
    try:
        rendered = project_file(initiative, model_path)
    except ProjectionError as exc:
        print(f"PROJECTION REFUSED: {exc}", file=sys.stderr)
        return 1
    output_path.write_text(rendered, encoding="utf-8")
    print(f"WROTE {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
