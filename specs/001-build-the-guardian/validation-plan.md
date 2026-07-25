# Validation Plan: 001-build-the-guardian

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** Codex / Harness Planner role  
**Last updated:** 2026-07-13

## 1. Strategy

Use deterministic registry/content checks, Python syntax parsing, isolated
consumer scaffolding and independent semantic review.

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001/2/3/5 | structural | `python scripts/validate_bundle.py` | exit 0 | evidence/T-004.md | Builder |
| V-002 | AC-004 | smoke | scaffold feature and bugfix in temp roots | required files created | evidence/T-002.md | Builder |
| V-003 | AC-004 | safety | rerun same slug | nonzero/refusal, no overwrite | evidence/T-002.md | Builder |
| V-004 | AC-005 | syntax/content | parse scripts; inspect YAML contract keys | success | evidence/T-002.md | Builder |
| V-005 | AC-006/7 | semantic review | inspect README/INSTALL/entrypoint/manifest | complete and neutral | evidence/T-003.md | Evaluator |
| V-006 | AC-008 | independent evaluation | review all artifacts and evidence | approve or findings | evidence/T-004.md | Evaluator |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | accidental overwrite | duplicate scaffold | refusal | T-002 |
| V-REG-002 | external dependency | inspect Python imports | stdlib only | T-002 |
| V-REG-003 | missing terminal gate | validator workflow tokens | pass | T-004 |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | bundle root | exit 0 | T-001–T-004 |
| Python AST parse for `scripts/*.py` | bundle root | success | T-002 |
| temporary feature/bugfix scaffolds | isolated temp directory | success | T-002 |
| duplicate target scaffold | same temp directory | refusal | T-002 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | read final diff/status | only bundle-source changes | T-004 evidence |
| M-002 | evaluator checks criteria | independent decision | T-004 evidence |

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | spec + prompt acceptance criteria | repository and evidence | no blocking findings | independent agent |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| real remote submodule clone/tag | `origin` is configured, but no local HEAD/tag or authorized published release exists | post-release integration risk | maintainer pilot |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex / Harness Planner role  
**Blocking gaps:** independent evaluation pending
