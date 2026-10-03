#!/usr/bin/env python3
"""Validate a brief-model.yaml document against schemas/brief-model.schema.json.

This is the authoring-time gate for SPEC 029 T-001: it checks that a model is
well-formed enough for a (future, T-002) deterministic projector to consume.
It does NOT read canonical Markdown sources and does NOT verify that a
`fragment` actually occurs in the cited source file -- that belongs to the
projector (FR-003), which resolves locator/digest/fragment against the real
source at projection time. This validator only checks internal consistency of
the model itself:

  * JSON Schema conformance (schemas/brief-model.schema.json), via `jsonschema`
    when it is importable, else a minimal hand-rolled structural check that
    covers the same required/enum/conditional rules.
  * No duplicate route ids.
  * Every block's `relation_ref` resolves to a declared relation graph.
  * Every edge's `from`/`to` resolves to a node declared in the same graph.

Usage:
    python scripts/validate_brief_model.py path/to/brief-model.yaml
    python -c "from validate_brief_model import validate; print(validate(doc))"
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "brief-model.schema.json"

ROUTE_IDS = ("scope", "architecture", "impact", "execution", "validation", "evolution", "decision", "coverage")
PROFILES = ("minimal", "standard", "deep")
DOMAINS = ("software", "ops", "docs", "policy", "research")
COVERAGE_VALUES = ("represented", "synthesized", "not_applicable", "link_only")
FORM_VALUES = ("topology", "sequence", "matrix", "footprint", "risk-chain", "dossier", "prose")
EDGE_STATES = ("proposed", "preserved", "out-of-scope", "discovery")


def _load_schema() -> dict[str, Any]:
    import json

    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _jsonschema_errors(doc: Any) -> list[str]:
    """Validate with the `jsonschema` library when available."""
    import jsonschema

    schema = _load_schema()
    validator_cls = jsonschema.Draft202012Validator
    validator_cls.check_schema(schema)
    validator = validator_cls(schema)
    errors = []
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "<root>"
        errors.append(f"schema: {loc}: {err.message}")
        # oneOf/anyOf collapse their sub-schema failures into one opaque
        # message; surface the most relevant nested reason too (e.g. which
        # required field was missing inside the matched absence.kind branch).
        if err.context:
            best = jsonschema.exceptions.best_match(err.context)
            if best is not None:
                sub_loc = "/".join(str(p) for p in best.path) or loc
                errors.append(f"schema: {loc}/{sub_loc}: {best.message}")
    return errors


def _minimal_errors(doc: Any) -> list[str]:
    """Hand-rolled fallback covering the same rules, used only if `jsonschema`
    is not importable in this environment."""
    errors: list[str] = []

    def fail(msg: str) -> None:
        errors.append(f"schema: {msg}")

    if not isinstance(doc, dict):
        return ["schema: <root>: document must be a mapping"]

    for key in ("contract_version", "profile", "domain", "thesis", "routes"):
        if key not in doc:
            fail(f"<root>: missing required field '{key}'")

    if "profile" in doc and doc["profile"] not in PROFILES:
        fail(f"profile: '{doc.get('profile')}' is not one of {PROFILES}")
    if "domain" in doc and doc["domain"] not in DOMAINS:
        fail(f"domain: '{doc.get('domain')}' is not one of {DOMAINS}")

    thesis = doc.get("thesis")
    if isinstance(thesis, dict):
        for key in ("decision_and_audience", "brief_thesis"):
            if not thesis.get(key):
                fail(f"thesis/{key}: missing or empty")
    elif "thesis" in doc:
        fail("thesis: must be a mapping")

    routes = doc.get("routes")
    if isinstance(routes, list):
        for i, route in enumerate(routes):
            if not isinstance(route, dict):
                fail(f"routes/{i}: must be a mapping")
                continue
            rid = route.get("id")
            if rid not in ROUTE_IDS:
                fail(f"routes/{i}/id: '{rid}' is not one of {ROUTE_IDS}")
            blocks = route.get("blocks")
            if not isinstance(blocks, list) or not blocks:
                fail(f"routes/{i}/blocks: must be a non-empty list")
                continue
            for j, block in enumerate(blocks):
                errors.extend(
                    (f"routes/{i}/blocks/{j}/" + e.split(": ", 1)[1] if e.startswith("schema: ") else e)
                    for e in _minimal_block_errors(block)
                )
    elif "routes" in doc:
        fail("routes: must be a list")

    relations = doc.get("relations")
    if relations is not None and not isinstance(relations, list):
        fail("relations: must be a list")

    return errors


def _minimal_block_errors(block: Any) -> list[str]:
    errors: list[str] = []

    def fail(msg: str) -> None:
        errors.append(f"schema: {msg}")

    if not isinstance(block, dict):
        return ["schema: must be a mapping"]

    for key in ("id", "form", "form_reason", "coverage", "source", "source_section"):
        if not block.get(key):
            fail(f"missing or empty required field '{key}'")

    if "form" in block and block["form"] not in FORM_VALUES:
        fail(f"form: '{block.get('form')}' is not one of {FORM_VALUES}")
    if "coverage" in block and block["coverage"] not in COVERAGE_VALUES:
        fail(f"coverage: '{block.get('coverage')}' is not one of {COVERAGE_VALUES}")

    if block.get("coverage") == "not_applicable":
        absence = block.get("absence")
        if not isinstance(absence, dict):
            fail("absence: required when coverage is not_applicable")
        else:
            kind = absence.get("kind")
            if kind == "not_applicable":
                if not absence.get("reason"):
                    fail("absence/reason: required for kind not_applicable")
            elif kind == "discovery":
                for key in ("missing_fact", "decision_impact"):
                    if not absence.get(key):
                        fail(f"absence/{key}: required for kind discovery")
            else:
                fail(f"absence/kind: '{kind}' is not one of ['not_applicable', 'discovery']")
    else:
        if not block.get("fragment"):
            fail("fragment: required unless coverage is not_applicable")
        if not block.get("text"):
            fail("text: required unless coverage is not_applicable")

    fields = block.get("fields")
    if fields is not None:
        if not isinstance(fields, list):
            fail("fields: must be a list")
        else:
            for k, pair in enumerate(fields):
                if not isinstance(pair, dict) or not pair.get("label") or not pair.get("value"):
                    fail(f"fields/{k}: must have non-empty 'label' and 'value'")

    return errors


def _semantic_errors(doc: Any) -> list[str]:
    """Cross-reference checks JSON Schema cannot express: duplicate route ids,
    relation_ref resolution, and edge node resolution."""
    errors: list[str] = []
    if not isinstance(doc, dict):
        return errors

    routes = doc.get("routes")
    seen_routes: set[str] = set()
    if isinstance(routes, list):
        for i, route in enumerate(routes):
            if not isinstance(route, dict):
                continue
            rid = route.get("id")
            if rid in seen_routes:
                errors.append(f"routes/{i}/id: duplicate route id '{rid}' — a route may appear at most once")
            elif isinstance(rid, str):
                seen_routes.add(rid)

    relations = doc.get("relations") or []
    graphs: dict[str, dict] = {}
    if isinstance(relations, list):
        for i, graph in enumerate(relations):
            if not isinstance(graph, dict):
                continue
            gid = graph.get("id")
            if isinstance(gid, str):
                if gid in graphs:
                    errors.append(f"relations/{i}/id: duplicate relation graph id '{gid}'")
                graphs[gid] = graph
            node_ids = {n.get("id") for n in graph.get("nodes", []) if isinstance(n, dict)}
            for j, edge in enumerate(graph.get("edges", []) or []):
                if not isinstance(edge, dict):
                    continue
                for endpoint in ("from", "to"):
                    val = edge.get(endpoint)
                    if val is not None and val not in node_ids:
                        errors.append(
                            f"relations/{i}/edges/{j}/{endpoint}: '{val}' does not match any node id "
                            f"declared in relation graph '{gid}'"
                        )

    # Duplicate topology detection (FR-004, T-003/AC-004): two DISTINCT
    # relation graphs that declare an identical node-id set and an identical
    # edge set (from/to/label/state) are the same architecture zoom authored
    # twice under different ids -- the real defect spec 028 reported
    # ("a mesma topologia em zooms distintos"). This is a set-diff, not a
    # name comparison, so renaming a graph never triggers it and copy-pasting
    # one always does. A graph with fewer than two nodes is skipped: a
    # single-node "graph" colliding with another is not the failure mode
    # this check exists for.
    signatures: dict[tuple, list[str]] = {}
    for gid, graph in graphs.items():
        if not isinstance(graph, dict):
            continue
        node_ids = frozenset(
            n.get("id") for n in graph.get("nodes", []) or [] if isinstance(n, dict) and n.get("id")
        )
        if len(node_ids) < 2:
            continue
        edge_sig = frozenset(
            (e.get("from"), e.get("to"), e.get("label"), e.get("state"))
            for e in graph.get("edges", []) or []
            if isinstance(e, dict)
        )
        signatures.setdefault((node_ids, edge_sig), []).append(gid)
    for gids in signatures.values():
        if len(gids) > 1:
            errors.append(
                "relations: graphs " + ", ".join(sorted(g for g in gids if isinstance(g, str))) +
                " declare an identical node/edge set -- duplicate topology (the same "
                "zoom content authored twice under different relation ids); merge them "
                "or change what one of them actually represents (FR-004)"
            )

    if isinstance(routes, list):
        for i, route in enumerate(routes):
            if not isinstance(route, dict):
                continue
            for j, block in enumerate(route.get("blocks", []) or []):
                if not isinstance(block, dict):
                    continue
                ref = block.get("relation_ref")
                if ref is not None and ref not in graphs:
                    errors.append(
                        f"routes/{i}/blocks/{j}/relation_ref: '{ref}' does not match any relations[].id"
                    )
                absence = block.get("absence")
                if isinstance(absence, dict):
                    prefix = f"routes/{i}/blocks/{j}/absence"
                    kind = absence.get("kind")
                    if kind == "discovery":
                        for key in ("missing_fact", "decision_impact"):
                            if not absence.get(key):
                                errors.append(f"{prefix}/{key}: required when absence.kind is 'discovery'")
                    elif kind == "not_applicable":
                        if not absence.get("reason"):
                            errors.append(f"{prefix}/reason: required when absence.kind is 'not_applicable'")
                    elif kind is not None:
                        errors.append(
                            f"{prefix}/kind: '{kind}' is not one of ['not_applicable', 'discovery']"
                        )

    return errors


def validate(doc: Any) -> list[str]:
    """Return a list of human-readable error strings. Empty list == valid."""
    try:
        import jsonschema  # noqa: F401

        errors = _jsonschema_errors(doc)
    except ImportError:
        errors = _minimal_errors(doc)
    errors.extend(_semantic_errors(doc))
    return errors


def _load_yaml(path: Path) -> Any:
    import yaml

    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_brief_model.py <brief-model.yaml>", file=sys.stderr)
        return 2
    doc = _load_yaml(Path(argv[1]))
    errors = validate(doc)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"INVALID: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
