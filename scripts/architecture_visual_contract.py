#!/usr/bin/env python3
"""Deterministic guard for source-backed *material* architecture visuals.

The guard verifies a declared structural promise only. It does not rate a
rendered diagram's aesthetics, factual completeness, or meeting usefulness;
those remain independent-review responsibilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from html.parser import HTMLParser


REQUIRED_LEGEND_STATES = frozenset({"proposed", "preserved", "out-of-scope", "discovery"})
VALID_ROUTE_MODES = frozenset({"material", "not-material", "not_applicable", "discovery"})
PROVENANCE_FIELDS = ("data-source", "data-source-section", "data-coverage")


@dataclass
class Node:
    tag: str
    attrs: dict[str, str]
    parent: int | None
    text: list[str] = field(default_factory=list)


class ArchitectureParser(HTMLParser):
    """Keep a small tree for the rendered descendants of ``#architecture``."""

    VOID = frozenset({"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"})

    def __init__(self) -> None:
        super().__init__()
        self.stack: list[tuple[str, bool, int | None]] = []
        self.declaration: dict[str, str] | None = None
        self.nodes: list[Node] = []

    def _start(self, tag: str, attrs: list[tuple[str, str | None]], *, push: bool) -> None:
        values = {name: value or "" for name, value in attrs}
        inside = values.get("id") == "architecture" or any(active for _, active, _ in self.stack)
        if values.get("id") == "architecture":
            self.declaration = values
        index: int | None = None
        if inside:
            parent = next((node for _, active, node in reversed(self.stack) if active and node is not None), None)
            index = len(self.nodes)
            self.nodes.append(Node(tag, values, parent))
        if push and tag not in self.VOID:
            self.stack.append((tag, inside, index))

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._start(tag, attrs, push=True)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._start(tag, attrs, push=False)

    def handle_data(self, data: str) -> None:
        if not data.strip():
            return
        for _, active, index in self.stack:
            if active and index is not None:
                self.nodes[index].text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()


def _text(node: Node) -> str:
    return " ".join(part.strip() for part in node.text if part.strip()).strip()


def _descendants(nodes: list[Node], root: int) -> list[Node]:
    result: list[Node] = []
    for node in nodes:
        parent = node.parent
        while parent is not None:
            if parent == root:
                result.append(node)
                break
            parent = nodes[parent].parent
    return result


def _projection_errors(kind: str, node: Node) -> list[str]:
    errors: list[str] = []
    missing = [field for field in PROVENANCE_FIELDS if not node.attrs.get(field)]
    if missing:
        errors.append(f"material architecture {kind} projection requires source-backed " + ", ".join(missing))
    if node.attrs.get("data-coverage") not in {"represented", "synthesized"}:
        errors.append(f"material architecture {kind} projection must be represented or synthesized")
    if node.attrs.get("data-architecture-source-backed") != "true":
        errors.append(f"material architecture {kind} projection must declare data-architecture-source-backed=\"true\"")
    return errors


def _svg_accessible(svg: Node, descendants: list[Node]) -> bool:
    if svg.attrs.get("role") != "img":
        return False
    if svg.attrs.get("aria-label", "").strip():
        return True
    return any(node.tag in {"title", "desc"} and _text(node) for node in descendants)


def _topology_errors(nodes: list[Node], index: int) -> list[str]:
    topology = nodes[index]
    descendants = _descendants(nodes, index)
    errors = _projection_errors("topology", topology)
    renderer = topology.attrs.get("data-architecture-renderer")
    if renderer not in {"svg", "semantic-html"}:
        return errors + ["material architecture topology must declare data-architecture-renderer=\"svg\" or \"semantic-html\""]

    equivalent = [node for node in descendants if node.attrs.get("data-architecture-text-equivalent") is not None]
    if not equivalent or any(not _text(node) for node in equivalent):
        errors.append("material architecture topology requires a non-empty data-architecture-text-equivalent")

    svg_nodes = [node for node in descendants if node.tag == "svg"]
    if renderer == "svg":
        if not svg_nodes or not any(_svg_accessible(svg, _descendants(nodes, nodes.index(svg))) for svg in svg_nodes):
            errors.append("SVG material architecture topology requires an accessible role=img SVG with aria-label or non-empty title/desc")

    named_nodes = [node for node in descendants if node.attrs.get("data-architecture-node", "").strip()]
    node_ids = {node.attrs.get("data-architecture-node-id", "").strip() for node in named_nodes}
    if len(named_nodes) < 2 or "" in node_ids or len(node_ids) < 2:
        errors.append("material architecture topology requires at least two named data-architecture-node entries with distinct data-architecture-node-id values")
    relations = [node for node in descendants if "data-architecture-relation" in node.attrs]
    for relation in relations:
        relation_name = relation.attrs.get("data-architecture-relation", "").strip()
        label = relation.attrs.get("data-architecture-relation-label", "").strip()
        origin = relation.attrs.get("data-architecture-relation-from", "").strip()
        destination = relation.attrs.get("data-architecture-relation-to", "").strip()
        if not relation_name:
            errors.append("material architecture topology requires each data-architecture-relation to be non-empty")
        if not label:
            errors.append("material architecture topology requires named data-architecture-relation-label entries")
        if not origin or not destination:
            errors.append("material architecture topology requires each relation to declare non-empty data-architecture-relation-from and data-architecture-relation-to")
        elif origin == destination:
            errors.append("material architecture topology relation endpoints must identify distinct declared node IDs")
        elif origin not in node_ids or destination not in node_ids:
            errors.append("material architecture topology relation endpoints must reference declared data-architecture-node-id values")
    if not relations:
        errors.append("material architecture topology requires a data-architecture-relation")

    states: dict[str, list[Node]] = {}
    for node in descendants:
        state = node.attrs.get("data-architecture-legend-state")
        if state:
            states.setdefault(state, []).append(node)
    missing_states = sorted(REQUIRED_LEGEND_STATES - states.keys())
    if missing_states:
        errors.append("material architecture topology legend is missing states: " + ", ".join(missing_states))
    for state in sorted(REQUIRED_LEGEND_STATES & states.keys()):
        if any(not _text(node) for node in states[state]):
            errors.append(f"material architecture topology legend state {state} must have non-empty visible text")
    return errors


def architecture_visual_errors(html: str) -> list[str]:
    """Return objective failures only when ``#architecture`` declares material depth."""
    parser = ArchitectureParser()
    try:
        parser.feed(html)
        parser.close()
    except Exception:
        return ["invalid HTML while reading architecture visual contract"]
    declaration = parser.declaration
    if declaration is None:
        return []
    mode = declaration.get("data-architecture-visual")
    if mode is None:
        return []
    if mode not in VALID_ROUTE_MODES:
        return ["architecture data-architecture-visual must be material, not-material, not_applicable, or discovery"]
    if mode != "material":
        return ([] if declaration.get("data-architecture-visual-reason", "").strip()
                else ["non-material architecture declaration requires data-architecture-visual-reason"])

    projections: dict[str, list[int]] = {}
    for index, node in enumerate(parser.nodes):
        kind = node.attrs.get("data-architecture-projection")
        if kind:
            projections.setdefault(kind, []).append(index)
    errors: list[str] = []
    for kind in ("topology", "surface-map", "zoom"):
        if kind not in projections:
            errors.append(f"material architecture requires a {kind} projection")

    for index in projections.get("topology", []):
        errors.extend(_topology_errors(parser.nodes, index))
    for index in projections.get("surface-map", []):
        surface = parser.nodes[index]
        errors.extend(_projection_errors("surface-map", surface))
        if not surface.attrs.get("data-architecture-unit", "").strip():
            errors.append("material architecture surface-map requires a non-empty data-architecture-unit")
        if not any(node.attrs.get("data-architecture-surface", "").strip() for node in _descendants(parser.nodes, index)):
            errors.append("material architecture surface-map requires at least one named data-architecture-surface inside its projection")
    for index in projections.get("zoom", []):
        zoom = parser.nodes[index]
        errors.extend(_projection_errors("zoom", zoom))
        status = zoom.attrs.get("data-architecture-zoom-status")
        if status == "supported":
            if not zoom.attrs.get("data-architecture-zoom-target", "").strip():
                errors.append("supported architecture zoom requires data-architecture-zoom-target")
        elif status in {"not_applicable", "discovery"}:
            if not zoom.attrs.get("data-architecture-absence-reason", "").strip():
                errors.append("N/A or discovery architecture zoom requires data-architecture-absence-reason")
        else:
            errors.append("material architecture zoom must declare supported, not_applicable, or discovery status")
    return errors
