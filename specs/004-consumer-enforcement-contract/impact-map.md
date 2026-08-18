# Impact Map: 004-consumer-enforcement-contract

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex acting as Impact Mapper  
**Reviewed at:** 2026-08-18  
**Overall risk:** medium

## 1. Change boundary

Add a consumer-facing validation command, its fixtures and portable adoption
guidance. The bundle remains a static vendor dependency: consumers and the
future Factory choose how to invoke it. No hosted service, CI-provider adapter
or automated semantic-quality judge is introduced.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Bundle scripts | `scripts/validate_human_visibility.py` | direct | Consumer-root validator and safe exit codes. | medium | FR-001–004 |
| Templates/state | `run-state.yaml`, scaffold output | direct | Explicit Human Visibility state/baseline or exception contract where needed. | medium | FR-002, FR-008 |
| Agent guidance | consumer prompt, install guide, rules | direct | Invocation and human-review instructions. | medium | FR-005, FR-007 |
| Factory adoption | documented contract/fixture | indirect | Future scaffold can install, bridge and invoke the bundle. | medium | FR-006 |
| CI/task runner | consumer-local wrapper | indirect | Generic invocation point, owned by consumer. | medium | FR-005 |
| Tests/docs | script tests, smoke/validation | direct | Fixtures prove failures and regression safety. | low | AC-001–008 |

## 3. Dependency and data flow

```txt
source artifacts + run-state + brief -> consumer validator -> local wrapper/CI
                                                   -> Human Visibility review -> task readiness
```

## 4. Compatibility and migration

- Backward compatibility: existing bundles and initiatives retain their files;
  validator gives actionable diagnostics for missing new optional freshness data.
- Data migration: no central data. A local baseline/exception is created only
  when the consumer selects that fallback.
- Rollout: document the command first, then consumers opt it into their native
  task runner or CI.
- Rollback implications: remove the local invocation/wrapper; no production
  data or service is changed.

## 5. Regression risks

| ID | Risk | Trigger/surface | Mitigation | Validation ID |
|---|---|---|---|---|
| IR-001 | Green structural check is mistaken for full approval. | Validator output and docs. | Explicit HUMAN REVIEW section and separate gate check. | V-004 |
| IR-002 | Freshness reports false success/offline ambiguity. | Git unavailable or source edit. | Git diff first, hash-baseline fallback, reviewed exception. | V-003 |
| IR-003 | Consumer cannot invoke the vendor script consistently. | Different OS/task runners. | Stdlib-only CLI, consumer-root option and generic wrapper examples. | V-005 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Which concrete task runner/CI the future Factory emits. | Vendor must not hard-code it. | Document neutral contract; Factory owner later. | no |

## 7. Recommended reviewers and checks

- Specialist/human: bundle maintainer and future Factory owner.
- Unit/integration/contract/E2E: validator fixtures, bundle validator and smoke scaffolder.
- Manual/operational: run CLI against a generated consumer fixture; rendered brief review.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes  
**Approval/evidence:** this map and independent evaluation after implementation.  
**Conditions before implementation:** plan and validation mapping approved below.
