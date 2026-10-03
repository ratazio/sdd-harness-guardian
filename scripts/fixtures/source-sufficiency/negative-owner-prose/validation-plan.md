# Validation Plan: fixture-positive

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | deterministic | `python -m pytest scripts/test_fixture_one.py` | test passes | evidence/T-001.md | Builder |
| V-002 | AC-002 | deterministic | `python -m pytest scripts/test_fixture_two.py` | test passes | evidence/T-001.md | Builder |
