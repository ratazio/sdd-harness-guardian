# Impact Map: 012-stakeholder-brief-evidence-projection-enforcement

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by / reviewed at:** Harness Planner / 2026-08-26  
**Overall risk:** medium

## 1. Change boundary

Change only Guardian validation, synthetic fixtures and guidance that govern v2
brief integrity. Keep consumer feature code, external systems, data stores,
task state machine, v1 compatibility and the distinction between a structural
PASS and independent human approval untouched.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| UI/client | `stakeholder-brief.html` template/example and brief contract docs | direct | State which view projects risks/routes and reviewer boundary. | medium | FR-002, FR-003, FR-005. |
| Service/backend | `scripts/validate_human_visibility.py` | direct | Safe evidence resolver and source-to-brief checks. | high | FR-001–FR-004. |
| Data/storage | not_applicable — no database or persistent format. | direct | None. | low | NG-004. |
| Public/API contract | Validator CLI/output and exit status | direct | Add failure diagnostics without option/exit-code break. | medium | AC-004–AC-005. |
| Auth/security/privacy | Consumer root/initiative filesystem boundary | direct | Reject unsafe evidence locators. | high | AC-006. |
| Build/deploy/infra | Local Python test/bundle commands | indirect | Additional fixture assertions only. | low | V-001–V-007. |
| Observability/support | Console diagnostics | direct | Name source, identifier and required target view. | medium | FR-004. |
| Tests/docs | `scripts/test_validate_human_visibility.py`, fixtures, templates/review guidance | direct | Positive/negative regressions and semantics reminder. | medium | FR-005–FR-006. |

## 3. Dependency and data flow

```txt
canonical source + run-state -> validator parser/safe resolver -> v2 brief panel tokens -> diagnostics/baseline gate -> author repair + independent reviewer
```

## 4. Compatibility and migration

- **Backward compatibility:** retain existing CLI arguments, group headings and v1/pinned bypass; valid v2 fixtures stay green.
- **Data migration:** none; no stored schema changes.
- **Rollout/feature flag:** ship source, tests and guidance together in the bundle; no flag or network deployment is justified.
- **Rollback:** revert the coordinated validator/template/fixture commit, preserve the failing regression fixture and ratchet record.

## 5. Regression risks and controls

| ID | Risk event | Trigger/early signal | Likelihood/impact | Preventive control | Contingency/owner | Validation ID |
|---|---|---|---|---|---|---|
| IR-001 | Resolver reads beyond selected initiative. | Absolute or `..` evidence locator reaches a file. | low/high | Normalize then containment-check before inspect/read. | Revert helper, add boundary fixture; security reviewer. | V-001,V-006 |
| IR-002 | Parser falsely extracts prose rather than a source contract. | Valid fixture fails on narrative `GET` text. | medium/medium | Limit patterns to risk table IDs and method + `/api/` contract grammar. | Narrow grammar and keep regression fixture; validation maintainer. | V-003,V-005 |
| IR-003 | Required item token appears but decision information is still poor. | Independent reviewer finds shallow/illegible projection. | medium/high | Keep distinct semantic/rendered review guidance and evidence. | Block task approval; reviewer. | V-007 |
| IR-004 | Existing v1 or no-contract initiative becomes blocked. | Compatibility fixture fails. | medium/medium | Gate new inventory checks by v2 and nonempty source set. | Revert/adjust scoped check; release owner. | V-005 |
| IR-005 | Baseline is written despite a new integrity failure. | Negative fixture writes/accepts baseline. | low/high | Execute new checks before freshness write path. | Delete synthetic baseline and return task to revision; test maintainer. | V-004 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Full set of established HTTP contract syntaxes in existing sources. | Overbroad parser would create false failures. | T-001 inventory / validation maintainer. | blocks T-003 only |
| U-002 | Whether evidence anchors warrant content/heading validation later. | File existence is enough for this incident; anchor semantics may overreach. | T-002 records explicit N/A / security reviewer. | no |

## 7. Recommended reviewers and checks

- **Specialist/human:** security reviewer for resolver containment; distinct semantic/rendered brief reviewer for boundaries of automation.
- **Unit/integration/contract/E2E:** Python unit/fixture tests for all positive, negative and compatibility cases; bundle validation.
- **Manual/operational:** inspect error messages and baseline non-write behavior in a temporary consumer fixture.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes — reusable validator behavior and filesystem boundary.  
**Approval/evidence:** `decision-log.md#D-003`; final task evidence required.  
**Conditions before implementation:** T-001 must bound parser grammar; every changed check needs negative and compatibility coverage; builder/evaluator identities must differ.
