"""Tests for the brief-model.yaml schema (SPEC 029 T-001).

These tests exercise scripts/validate_brief_model.py against
schemas/brief-model.schema.json. They intentionally do NOT touch any
projector or HTML: T-001 is schema-only (out of scope: projection, HTML,
CSS, removal of any file).
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from validate_brief_model import validate  # noqa: E402

FIXTURES = ROOT / "scripts" / "fixtures" / "brief-model"


def _load(name: str):
    with (FIXTURES / name).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def valid_doc():
    return _load("valid.yaml")


def test_valid_model_passes():
    errors = validate(valid_doc())
    assert errors == [], f"expected no errors, got: {errors}"


def test_invalid_fixture_fails():
    errors = validate(_load("invalid.yaml"))
    assert errors, "the invalid fixture must fail validation"


def test_route_outside_enum_fails():
    doc = copy.deepcopy(valid_doc())
    doc["routes"][0]["id"] = "architecture.global"  # A-02: old SKILL vocabulary
    errors = validate(doc)
    assert errors
    assert any("routes/0/id" in e for e in errors)


def test_duplicate_route_id_fails():
    doc = copy.deepcopy(valid_doc())
    dup = copy.deepcopy(doc["routes"][0])
    doc["routes"].append(dup)
    errors = validate(doc)
    assert any("duplicate route id" in e for e in errors)


def test_form_without_reason_fails():
    doc = copy.deepcopy(valid_doc())
    block = doc["routes"][0]["blocks"][0]
    assert "form" in block
    del block["form_reason"]
    errors = validate(doc)
    assert errors
    assert any("form_reason" in e for e in errors)


def test_form_outside_enum_fails():
    doc = copy.deepcopy(valid_doc())
    doc["routes"][0]["blocks"][0]["form"] = "wordcloud"
    errors = validate(doc)
    assert errors
    assert any("form" in e for e in errors)


def test_edge_to_nonexistent_node_fails():
    doc = copy.deepcopy(valid_doc())
    doc["relations"][0]["edges"][0]["to"] = "nowhere"
    errors = validate(doc)
    assert errors
    assert any("does not match any node id" in e for e in errors)


def test_relation_ref_to_nonexistent_graph_fails():
    doc = copy.deepcopy(valid_doc())
    doc["routes"][1]["blocks"][0]["relation_ref"] = "no-such-graph"
    errors = validate(doc)
    assert errors
    assert any("relation_ref" in e for e in errors)


def test_represented_block_without_fragment_fails():
    doc = copy.deepcopy(valid_doc())
    block = doc["routes"][0]["blocks"][0]
    assert block["coverage"] == "represented"
    del block["fragment"]
    errors = validate(doc)
    assert errors
    assert any("fragment" in e for e in errors)


def test_not_applicable_without_absence_fails():
    doc = copy.deepcopy(valid_doc())
    block = {
        "id": "no-absence",
        "form": "prose",
        "form_reason": "test",
        "coverage": "not_applicable",
        "source": "spec.md",
        "source_section": "x",
    }
    doc["routes"][0]["blocks"].append(block)
    errors = validate(doc)
    assert errors
    assert any("absence" in e for e in errors)


def test_discovery_absence_requires_missing_fact_and_impact():
    doc = copy.deepcopy(valid_doc())
    block = {
        "id": "bad-discovery",
        "form": "prose",
        "form_reason": "test",
        "coverage": "not_applicable",
        "source": "decision-log.md",
        "source_section": "Q-002",
        "absence": {"kind": "discovery", "missing_fact": "prazo"},
    }
    doc["routes"][0]["blocks"].append(block)
    errors = validate(doc)
    assert errors
    assert any("decision_impact" in e for e in errors)


def test_domain_outside_enum_fails():
    doc = copy.deepcopy(valid_doc())
    doc["domain"] = "marketing"
    errors = validate(doc)
    assert errors


def test_profile_outside_enum_fails():
    doc = copy.deepcopy(valid_doc())
    doc["profile"] = "exhaustive"
    errors = validate(doc)
    assert errors


def test_missing_contract_version_fails():
    doc = copy.deepcopy(valid_doc())
    del doc["contract_version"]
    errors = validate(doc)
    assert errors


def test_no_digest_or_sha256_field_in_schema():
    """The agent never authors digests/SHA-256 -- the projector computes them
    from the canonical source (T-002 scope). The schema must have no field
    named/containing digest or sha256 anywhere."""
    import json

    schema_text = (ROOT / "schemas" / "brief-model.schema.json").read_text(encoding="utf-8")
    schema = json.loads(schema_text)

    def walk(node):
        if isinstance(node, dict):
            for key in node:
                if "digest" in key.lower() or "sha256" in key.lower():
                    if key not in ("description",):
                        pytest.fail(f"schema declares a digest/sha256 field: {key}")
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(schema.get("properties", {}))
    walk(schema.get("$defs", {}))
