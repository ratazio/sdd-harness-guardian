#!/usr/bin/env python3
"""Structural integrity check for SPEC 021 T-004 review evidence.

This deliberately validates only the recorded review envelope: identity/group,
scope, pass coverage and final manifest bindings.  It does not judge whether a
human APPROVE is semantically correct or sufficient.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "specs" / "021-material-source-projection-and-domain-architecture" / "evidence" / "T-004-review-records.json"
MANIFEST = ROOT / "testes" / "mock-runs" / "20260830-spec021-t004-r15" / "run-manifest.json"
LENSES = {
    "architect", "system_designer", "developer", "delivery_manager",
    "director", "c_level", "general_stakeholder",
}
PASSES = {"P1", "P2"}
REQUIRED = {
    "id", "cycle", "reviewer", "lens", "pass", "disposition",
    "request_sha256", "source_set_sha256", "html_sha256", "locator",
    "finding_id", "finding", "decision_impact", "required_repair",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    payload = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    binding = {
        item["mock"]: (item["request_sha256"], item["sources_sha256"], item["html_sha256"])
        for item in manifest["cases"]
    }
    records = payload["records"]
    require(payload["record_count"] == 112 and len(records) == 112, "T-004 must record exactly 112 final reviews")
    require(set(payload["reviewer_groups"]) == {"architecture_system_developer", "delivery_director_c_level", "general_stakeholder"}, "reviewer groups are incomplete")
    ids: set[str] = set()
    coverage: set[tuple[str, str, str]] = set()
    restart = 0
    for record in records:
        require(set(record) == REQUIRED, f"record fields are incomplete: {record.get('id')}")
        require(record["id"] not in ids, f"duplicate review id: {record['id']}")
        ids.add(record["id"])
        case = next((item for item in binding if f"-{item.lower()}-" in record["id"]), None)
        require(case is not None, f"record id lacks a known case: {record['id']}")
        require(record["lens"] in LENSES and record["pass"] in PASSES, f"invalid lens/pass: {record['id']}")
        require(record["disposition"] == "APPROVE", f"final matrix contains a non-APPROVE: {record['id']}")
        require((record["request_sha256"], record["source_set_sha256"], record["html_sha256"]) == binding[case], f"manifest binding mismatch: {record['id']}")
        require(record["reviewer"].startswith("/root/"), f"reviewer identity is not an actual agent group: {record['id']}")
        require(f"case={case}" in record["locator"] and "stakeholder-brief.html#" in record["locator"], f"stable locator missing: {record['id']}")
        require(record["finding"] == "nenhum" and record["required_repair"] == "nenhum", f"final APPROVE needs explicit no-finding/no-repair: {record['id']}")
        coverage.add((case, record["lens"], record["pass"]))
        if record["cycle"] == "r15-a3-restart":
            require(case in {"M-005", "M-006"}, f"restart cycle outside M-005/M-006: {record['id']}")
            restart += 1
        else:
            require(record["cycle"] == "r15-final-unchanged", f"unknown final cycle: {record['id']}")
    require(len(coverage) == 112, "case/lens/pass coverage is incomplete")
    require(restart == 28, f"expected 28 final A3 restart reviews, got {restart}")
    historical = payload["historical_cycles"]
    require(all(entry["status"].startswith("superseded") for entry in historical), "historical REVISE cycles must not be current records")
    print("SPEC 021 T-004 review-matrix structural contract passed: 112 records, 28 final A3 restart records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
