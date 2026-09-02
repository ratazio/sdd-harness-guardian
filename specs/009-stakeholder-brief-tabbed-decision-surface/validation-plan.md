# Validation Plan: 009-stakeholder-brief-tabbed-decision-surface

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-26

## 1. Strategy

Use deterministic checks only for stable HTML, contract, fallback and provenance invariants. Cross-context fixtures prove that rich information is projected when present and N/A/question/unknown behavior is proportional when absent. A distinct rendered review judges decision usefulness, accessibility and meaningful depth; no check scores prose or asserts “enough detail”.

### Assurance selection

| Profile/task | Risk or claim | Technique selected/inapplicable rationale | Oracle and evidence | Executor | Evaluator | Failure/waiver behavior |
|---|---|---|---|---|---|---|
| A2 / T-001 | Interaction may violate no-script/keyboard/print. | Native prototype plus manual behavior review. | Focus sequence, visible state, no-script and print observations. | builder | accessibility reviewer | Return to discovery; no waiver for inaccessible content. |
| A2 / T-002–004 | Tab/content projection can hide or fabricate facts. | Static fixture contract plus rendered recovery review. | Source-to-panel mapping and rich/sparse fixture record. | builder | Spec Guardian | Correct canonical source/template and regenerate. |
| A2 / T-005 | v1/provenance lifecycle can regress. | Existing contracts plus smallest focused regression test. | Commands below, v1 fixture and diff scope. | builder | maintainer | Reject release; human decision for scope breach. |

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | static contract | Run focused tabbed-brief test and inspect fixture paths. | Eight tab controls/panels in one HTML; no multi-file navigation. | evidence/T-002.md | builder |
| V-002 | AC-002 | fixture + review | Compare source locator, tab mission and panel facts in rich/sparse fixtures. | Every panel fact is sourced, N/A reasoned or an owned question/unknown. | evidence/T-003.md | planner/reviewer |
| V-003 | AC-003 | rendered review | Read Value & scope in rich fixture and news/blog sandbox. | Mission, value/technical pillars when material, outcome, limit, main risk and authority recover. | evidence/T-003.md | reviewer |
| V-004 | AC-004 | paired fixture/eval | Compare software M-profile with non-software/localized profile. | Architecture/impact intro and visual depth are proportional; no fake technical detail. | evidence/T-003.md | reviewer |
| V-005 | AC-005 | source/HTML contract | Map each material task field to execution card. | Objective, scope, dependencies, validation, evidence and exit conditions recover. | evidence/T-004.md | builder/reviewer |
| V-006 | AC-006 | source/HTML contract | Map AC matrix to validation view, including a no-command case. | AC, method, environment/command, oracle and evidence/skip reason recover. | evidence/T-004.md | builder/reviewer |
| V-007 | AC-007 | negative fixture/eval | Render one material missing fact and one non-material absence. | First yields exact owner/impact/resolution question; second compact N/A/no question. | evidence/T-003.md | reviewer |
| V-008 | AC-008 | manual accessibility | Desktop, 390px, keyboard, no-script and print checks on final fixture. | All panels/content remain reachable; no focus loss or global overflow. | evidence/T-002.md, evidence/T-005.md | accessibility reviewer |
| V-009 | AC-009 | regression | Run existing v1/v2 contracts and Human Visibility fixtures. | v1 path untouched; v2 provenance/coverage/gates retain contract. | evidence/T-005.md | maintainer |
| V-010 | AC-010 | negative diff review | Search changed files for score/parser/LLM judge/semantic pass claims. | No deterministic semantic evaluator or new canonical sidecar. | evidence/T-005.md | evaluator |
| V-011 | NFR security/privacy | manual/diff review | Inspect fixtures and examples for PII, secrets and sensitive topology. | Fictional/redacted facts only. | evidence/T-005.md | reviewer |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | v1/v2 lifecycle/provenance | `python scripts/test_brief_v2_contracts.py`; `python scripts/test_validate_human_visibility.py` | PASS; legacy fixture unaffected and v2 contract valid. | evidence/T-005.md |
| V-REG-002 | No semantic gate | Focused test/diff review of new template/rule/script. | PASS; no score, parser, semantic schema or LLM judge. | evidence/T-005.md |
| V-REG-003 | Bundle integrity | `python scripts/validate_bundle.py` | PASS. | evidence/T-005.md |
| V-REG-004 | Reference consumer | `python scripts/validate_human_visibility.py --consumer-root testes/news-blog-spec-sandbox --initiative specs/001-news-blog-auth` | PASS after candidate refresh/baseline discipline. | evidence/T-005.md |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/test_tabbed_brief_surface.py` | bundle root; new focused fixture script only if T-005 proves need | PASS for tab/panel/fallback/locator invariants; no prose score. | T-002–T-005 |
| `python scripts/test_brief_v2_contracts.py` | bundle root | PASS for v2 and legacy v1 contracts. | T-002–T-005 |
| `python scripts/test_validate_human_visibility.py` | bundle root | PASS for validator fixtures. | T-002–T-005 |
| `python scripts/test_semantic_brief_review_calibration.py` | bundle root | PASS; qualitative review remains separate. | T-003–T-005 |
| `python scripts/validate_human_visibility.py --consumer-root testes/news-blog-spec-sandbox --initiative specs/001-news-blog-auth` | bundle root; ignored fixture consumer | PASS after refresh. | T-004–T-005 |
| `python scripts/validate_bundle.py` | bundle root | PASS. | T-005 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Open rich fixture; select Value & scope and inspect source recovery. | Mission and requested value decision understandable in 60 seconds. | evidence/T-003.md |
| M-002 | Open rich execution view; compare cards with `tasks.md`. | Each material task is concrete enough to distinguish good/poor implementation. | evidence/T-004.md |
| M-003 | Open validation view with normal and skipped/no-command validation. | Proof, oracle and limitation are clear without asserting nonexistent test. | evidence/T-004.md |
| M-004 | Final brief at desktop, 390px, keyboard, JavaScript disabled and print preview. | Every panel is reachable/readable; print includes collapsed/hidden content. | evidence/T-002.md, evidence/T-005.md |
| M-005 | Review sparse/non-software fixture. | It asks only material questions and states justified N/A without fake architecture. | evidence/T-003.md |

## 6. Evals

| ID | Rubric/oracle | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-001 | Per-tab mission and decision-loss rubric: product, architecture/operations and delivery are recoverable, superficial, absent or N/A justified. | Rich v2 fixture. | Reviewer can state each tab’s decision and no source fact is silently weakened. | distinct Spec Guardian |
| E-002 | Proportionality rubric. | Non-software/localized and sparse fixtures. | No technical fiction or mandatory filler; absence is N/A or owned question only when material. | distinct reviewer |
| E-003 | Discovery specificity rubric. | Missing-detail fixture and source log. | Every prompt says needed fact, owner, **decision impact** and resolution; no generic “a confirmar”. | distinct planner/reviewer |
| E-004 | Accessibility/visual behavior rubric. | Final rendered HTML. | Tab selection is discoverable and fallback preserves reading/print; screenshot alone is not behavior proof. | accessibility reviewer |

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Application E2E/load test | Bundle has no running application/network behavior. | Low; UI behavior is checked locally and manually. | Not applicable — planner records source boundary. |
| Universal screenshot baseline | Appearance varies across consumer content and cannot prove tab behavior. | Medium; use behavior plus rendered review. | Not applicable — evaluator confirms no false visual claim. |
| Automatic semantic adequacy score | Context-specific depth is not stable/deterministic. | High if added; intentionally excluded. | Human approval required for any future proposal. |

## 8. Validation decision

**Validation Ready:** complete — D-030  
**All ACs mapped:** yes  
**Reviewer:** Codex / Harness Planner  
**Blocking gaps:** none. D-030 accepts the focused structural test and release evidence; rendered meaning remains an independently reviewed, non-deterministic judgment.
