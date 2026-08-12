# Validation Plan: 003-stakeholder-brief-enrichment

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-12

## 1. Strategy

Use the cheapest reliable oracle for each claim. Static checks cover stable
structure, source references and scaffold behavior. One semantic/visual pass by
the Spec Guardian covers meaning, proportionality and rendering. Do not require
screenshot evidence, a new report, LLM scoring or duplicated checklists.

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | scaffold smoke | Run scaffolder smoke with assertions for enriched IDs and rendered placeholders. | Brief is created with resolved initiative/date metadata. | evidence/T-002.md | builder |
| V-002 | AC-002 | template inspection | Inspect stable base sections and copy. | Every decision-critical base dimension is present. | evidence/T-001.md | evaluator |
| V-003 | AC-003, AC-004 | guidance inspection | Review the existing rule/skill/agent checklist and localized/non-trivial paths. | One conditional checklist; no new skill/artifact; diagrams can be omitted with reason. | evidence/T-001.md | evaluator |
| V-004 | AC-005 | visual/accessibility | Open static HTML at desktop and narrow width; inspect SVG text alternatives and overflow. | Readable, meaningful and independent of external assets. | evidence/T-001.md | Spec Guardian/evaluator |
| V-005 | AC-006, AC-007 | contract review | Inspect agent and lifecycle diffs against the existing gate matrix. | Author/reviewer are explicit; no gate or state added. | evidence/T-001.md | evaluator |
| V-006 | AC-008 | negative static fixtures | Exercise validator with a missing ID, placeholder and missing source link. | Each invalid case fails for a precise structural reason; prose is not scored. | evidence/T-002.md | builder/evaluator |
| V-007 | AC-009 | regression | Run existing bundle validation and scaffolder smoke. | Both exit 0. | evidence/T-002.md | builder/evaluator |
| V-008 | AC-010 | 60-second review | Review this initiative's rendered brief and answer the three decision-test questions. | Outcome/impact/architecture/size/exclusions/decision are recoverable; visuals reveal concrete relationships. | evidence/T-001.md | Spec Guardian |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | Passive/offline bundle | Search HTML for remote scripts/styles/assets. | No external dependency. | evidence/T-001.md |
| V-REG-002 | Token/process cost | Review generated brief and author workflow. | One synthesis pass, one review pass, no new state/artifact/gate. | evidence/T-001.md |
| V-REG-003 | Accessibility | Inspect semantic structure, table headers, SVG title/desc or text equivalent, contrast and narrow layout. | Essential content is readable without color or pointer interaction. | evidence/T-001.md |
| V-REG-004 | Backward compatibility | Run current validator/smoke and inspect paths. | Scaffold command and canonical paths are unchanged. | evidence/T-002.md |

## 4. Required commands

| Command | Working directory/environment | Expected exit/result | Applies to tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | bundle root | exit 0 | T-001, T-002 |
| `python scripts/smoke_test_scaffolder.py` | bundle root | exit 0 | T-002 |
| `rg -n "<initiative>|<YYYY-MM-DD>|Replace this|Product/user outcome to advance" .harness/templates/stakeholder-brief.html` | bundle root | no canonical filler remains in the released template, except explicitly documented authoring markers if adopted | T-001 |

## 5. Manual checks and artifacts

| ID | Preconditions/steps | Expected result | Artifact/location |
|---|---|---|---|
| M-001 | Open this initiative's `stakeholder-brief.html`; scan for 60 seconds. | Reviewer can state outcome, impact, architecture, size, excluded complexity and decision. | `stakeholder-brief.html` |
| M-002 | Inspect at desktop and narrow viewport. | No global overflow or clipping; local diagram scrolling is acceptable when evident and usable. | visual review note in evidence/T-001.md |
| M-003 | Ask whether each visual reveals a boundary, dependency or trade-off absent from its heading. | Decorative or generic visuals are revised or removed. | visual review note in evidence/T-001.md |

## 6. Evals

No scored eval is required. The three-question review in M-001/M-003 is the
qualitative oracle and is intentionally short. Evidence records only three short
answers: outcome/decision, impact/architecture and whether scope can be approved
or reduced.

## 7. Skipped or unavailable validation

| Check | Reason | Risk impact | Required approval/owner |
|---|---|---|---|
| Mandatory screenshot CI | Adds maintenance cost and catches pixels rather than meaning. | Reviewer must perform one rendered pass. | none; deliberate scope decision |
| Automated prose/value scoring | Brittle and expensive; may reward filler. | Meaning stays a Spec Guardian responsibility. | none; deliberate scope decision |
| Cross-file content hashing/freshness engine | Requires state/schema complexity disproportionate to MVP. | Orchestrator uses the material-change refresh rule. | revisit only after evidence of stale briefs |

## 8. Validation decision

**Validation Ready:** yes  
**All ACs mapped:** yes  
**Reviewer:** Codex  
**Blocking gaps:** none before implementation.
