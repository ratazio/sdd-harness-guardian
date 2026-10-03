# Rule: Human Visibility

## Soft rule

Use `.harness/rules/brief-contract.md` (BC-001–BC-025) as the single
normative source. Dispatch lineage under BC-002 before choosing the protocol:
new generation uses BC-009 v3; pinned 1/2 uses its historical branch.
Authority, actors and completion are governed by BC-001/BC-010/BC-025.
This pointer creates no additional brief review.

## Hard mirror recommendation

Version-aware structural checks should preserve historical 1/2 and inspect
v3 structure/integrity proportionally (BC-020/BC-021/BC-024). Legacy
`validate_brief_model.py`, `validate_source_sufficiency.py` and
`test_brief_v2_contracts.py` apply to their historical branch. Mechanical
PASS never supplies semantic approval or a third validation after B.

Recommended check: `validate-human-visibility` (version-aware mechanics).
