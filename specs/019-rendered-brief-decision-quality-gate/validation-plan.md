# Validation Plan: 019-rendered-brief-decision-quality-gate

**Status:** validation_ready candidate  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform engineering  
**Last updated:** 2026-08-27

## 1. Strategy

Use two complementary oracles. Deterministic tests establish that a claimed
decision-quality gate has a complete, fresh and independently authored review
record. Independent reviewers establish whether content is decision-ready.
Neither test suite may convert word count, tabs, CSS, SVG, diagram syntax or a
model score into a semantic approval. Reviewers use the locally served page and
the request/source locators listed in the evidence record.

| Profile/task | Risk or claim | Technique selected/inapplicable rationale | Oracle and evidence | Executor | Evaluator | Failure/waiver behavior |
|---|---|---|---|---|---|---|
| T-001 / high | A valid-looking page can conceal material decisions | Fixture + five-lens qualitative calibration | role findings, source/render locators, expected blocking disposition | builder | independent evaluator | material `REVISE` returns task to revision |
| T-002 / high | State claims approval without independent evidence | focused deterministic parser tests | fixture records with missing identity, digest, finding disposition and stale render | builder | independent evaluator | reject claim; preserve legacy behavior |
| T-003 / medium | Agent protocol becomes rigid or unsafe | documentation/skill review plus manual served-page drill | adaptive positive fixture and locator-only example | builder | independent evaluator | revise instructions |
| T-004 / high | Mock suite masks shallow briefs | disposable full suite + 8×5 independent review matrix | per-mock role records, summary separating structural PASS from quality | builder | independent evaluator | no quality completion while any material finding unresolved |

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | fixture / independent review | Run calibration test; serve the negative HTML and review it through five lenses. | Structural-valid negative cannot claim quality approval; at least three material role findings. | `evidence/T-001.md` | T-001 builder/evaluator |
| V-002 | AC-002, AC-003 | unit/contract | Run new gate-record tests and Human Visibility regression tests. | Missing, stale, self-approved or unresolved evidence is rejected; resolved record accepted. | `evidence/T-002.md` | T-002 builder/evaluator |
| V-003 | AC-004 | fixture/manual | Inspect varied positive fixture with non-tab/non-diagram justified representation. | Valid concise alternative remains eligible; no fixed UI selector is required. | `evidence/T-001.md`, `evidence/T-003.md` | T-001/T-003 |
| V-004 | AC-003 | source-security inspection | Inspect serialized review record and documentation. | Locators/digests only; source bodies, secrets and PII absent. | `evidence/T-003.md` | T-003 |
| V-005 | AC-005 | end-to-end mock-lab | Generate all M001–M008 in disposable root, serve HTML and collect five-lens reviews. | 8×5 matrix, correction/re-review trail and explicit structural-versus-qualitative conclusion. | `evidence/T-004.md` | T-004 |
| V-006 | AC-004 | regression | Run full bundle validator and tests. | Existing Pearson, v2, accessibility, template and scaffolder tests remain green. | `evidence/T-004.md` | T-004 |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | Existing v1/v2 compatibility | `python scripts/test_validate_human_visibility.py` | Existing fixtures remain valid/invalid as asserted. | task evidence |
| V-REG-002 | Bundle coherence | `python scripts/validate_bundle.py` | Exit 0 after every material template/workflow change. | task evidence |
| V-REG-003 | Accessibility/local inspection | Serve review fixture and operate keyboard navigation where supplied. | No focus trap; text equivalent remains accessible; no network/hotlink requirement. | task evidence |
| V-REG-004 | No semantic scorer | Review implementation and test names. | Parser verifies record/state, never architecture/prose score. | evaluator report |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/test_semantic_brief_review_calibration.py` | bundle root | exit 0; calibration fixtures wired | T-001, T-004 |
| `python scripts/test_validate_human_visibility.py` | bundle root | exit 0; state/freshness regression passes | T-002, T-004 |
| `python scripts/validate_bundle.py` | bundle root | exit 0; bundle contract coherent | T-001–T-004 |
| `python -m http.server <port> --bind 127.0.0.1` | disposable mock root | local HTML is inspectable | T-003, T-004 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Reviewer opens local HTML, request locator and canonical sources; records five lenses independently. | Each role can approve/revise/N-A with concrete decision reasoning. | per-run review record |
| M-002 | For each material finding, repair canonical source, regenerate and reopen HTML. | Finding has source recovery and originating-role re-review; no HTML-only repair. | per-run review record |
| M-003 | Inspect a concise non-software or low-relation fixture. | It is not failed solely for missing tabs, cards or diagrams. | T-001/T-003 evidence |

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | Five-lens adaptive decision rubric | request locator, canonical source digests, locally served HTML digest/URL | Every material capability is recoverable or has accountable resolution; `insufficient` is blocking. | distinct architect/system designer/executive/stakeholder/delivery reviewers |
| E-002 | Task evidence review | implementation, tests and evidence pack | Builder/evaluator identities differ; no hidden rigid criterion or self-approval. | distinct evaluator agent |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| External browser cloud/device matrix | The artifact is static/local and this change governs review protocol, not browser engine compatibility. | Low; local rendered inspection remains required. | evaluator records limitation |

## 8. Validation decision

**Validation Ready:** pending independent planning review  
**All ACs mapped:** yes  
**Reviewer:** pending  
**Blocking gaps:** accept the adaptive review protocol and preliminary task set.
