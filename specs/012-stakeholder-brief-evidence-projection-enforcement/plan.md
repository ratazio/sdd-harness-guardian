# Technical Plan: 012-stakeholder-brief-evidence-projection-enforcement

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner / updated:** platform-engineering / 2026-08-26

## 1. Technical approach

Extend the existing `scripts/validate_human_visibility.py` pipeline rather than creating a second checker. Add bounded, v2-only pre-baseline validation stages: resolve source-declared local evidence paths safely; extract material `IR-*` IDs from the impact risk table; extract normalized HTTP method/path entries from the plan contract section; then prove those tokens occur in their allowed rendered brief views. Stage diagnostics by source and target so authors can repair exactly one omission. Keep the independent review warning unchanged because parser presence does not establish decision usefulness.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-001 | Add checks to the existing Human Visibility validator. | One entry point preserves current consumer invocation and baseline semantics. | New companion validator or manual-only rule. | Test existing compatibility paths. |
| D-002 | Resolve only initiative-relative `evidence/...` file locators cited in canonical planning/state sources. | Evidence must be recoverable without arbitrary filesystem reads. | Resolve any markdown link or ignore references. | Need explicit traversal/anchor tests. |
| D-003 | Derive minimum risk/API projection inventory from canonical source text, not a new sidecar manifest. | Avoid duplicate state that can drift. | A hand-maintained JSON/YAML inventory. | Parsers must be deliberately narrow. |
| D-004 | Require risks in Impact and HTTP method/path tokens in Architecture or Validation. | Matches current brief decision surfaces and source intent. | Search all HTML or demand every route in both views. | Structural token presence is not semantic completeness. |
| D-005 | Preserve a distinct independent semantic/rendered review gate. | Deterministic parsing cannot judge explanation quality, visual legibility or materiality outside supported patterns. | Automated quality score. | Guidance and evaluator evidence remain required. |

## 3. Size and proportionality

**Initiative size:** M.  
**Why:** one local Python validator, templates/guidance and regression fixtures change a reusable public bundle contract.  
**Smaller option considered:** documentation-only reminder is insufficient because the defect already passed deterministic validation.  
**Complexity deliberately excluded:** no service, database, web UI, telemetry, generic Markdown AST framework or quality-scoring system.

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** A2-elevated.  
**Rationale and trigger evidence:** reusable validator contract plus filesystem path boundary and false-positive risk, demonstrated by `reproduction.md`.  
**A2 source links/headings:** `spec.md#7-10`, `impact-map.md#5`, `validation-plan.md#1-7`.  
**Reapproval trigger:** support for a new source syntax, any consumer compatibility regression, or a path-boundary failure.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Validator checks structure/provenance/freshness. | Validator also enforces recoverable evidence and minimum material projections. | D-001–D-005; V-001–V-007. |
| Components/responsibilities | One Python entry point and tests. | Parser helpers, safe resolver, diagnostics and fixtures stay local. | T-001–T-004. |
| Interfaces/events/contracts | CLI options and PASS/fail wording exist. | Preserve options/exit codes; add deterministic failure rows only. | AC-004–AC-005. |
| Data ownership/lifecycle | Files are read transiently. | Local evidence paths resolve only within initiative. | AC-001, AC-006. |
| Security/trust boundaries | `--consumer-root` and initiative path select files. | Reject absolute/traversal locators before reading. | R-002, V-006. |
| Critical runtime flows | Source parse → structural check → optional baseline. | Insert integrity/projection checks before freshness baseline write. | V-001–V-004. |
| Failure behavior | Diagnostics group structural/gate/freshness issues. | Name source, missing token and required target view. | FR-004, V-001–V-003. |
| NFRs | Offline Python check. | Deterministic, bounded and compatible with existing tests. | V-005, V-007. |
| Compatibility/migration | v1 and existing valid v2 remain supported. | New checks run only after v2 determination; no file migration. | EC-005, V-005. |
| Observability | CLI text/test assertions. | No telemetry; failures are local evidence. | not_applicable — offline bundle. |
| Rollout/rollback | Bundle source changes ship together. | Revert one validator/template/fixture change set if compatibility fails. | T-004 evidence. |
| Alternatives/trade-offs | Coverage labels are declarative. | Source-derived tokens supply a narrow hard mirror. | D-003–D-005. |
| Unknowns | Exact parser patterns may vary. | Bound them to risk table IDs and method + `/api/` tokens; expand only with evidence. | U-001. |

### Current → target → delta and complexity envelope

| View | Current | Target | Delta/commitment | Reapproval trigger |
|---|---|---|---|---|
| Architecture/method | Structure + freshness validation. | Three source-to-brief integrity checks before baseline. | One script, helper-level tests, synthetic fixtures. | New source grammar. |
| Modules/classes/APIs/data/contracts | Existing CLI is stable. | No argument/exit-code change; added diagnostics. | 0 public API routes, 0 storage models. | CLI behavior change. |
| Process/tooling | Independent review exists. | Guidance names deterministic boundary and reviewer evidence. | Template/review checklist update only. | Review gate weakened. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Tests/fixtures and reproduction | Spec/plan/validation approved | Isolated failing tests expose baseline defect. | yes — fixture only. |
| 2 | `validate_human_visibility.py` safe evidence resolver | T-001 evidence | Missing/unsafe evidence fails pre-baseline. | yes — revert helper. |
| 3 | Validator source-to-brief inventory checks | T-002 evidence | Missing risks/routes fail with exact diagnostics. | yes — revert checks. |
| 4 | Templates, reviewer guidance, positive/negative fixtures | T-003 evidence | Future authors/reviewers understand scope and regressions stay fixed. | yes — revert coordinated change. |
| 5 | Bundle/baseline/review evidence | T-001–T-004 | Released local validation proof. | yes — do not publish external state. |

## 6. Contracts, data and compatibility

| Contract | Input | Success | Failure/compatibility |
|---|---|---|---|
| Evidence integrity | Canonical initiative text containing `evidence/<relative>.md` optionally followed by `#anchor`. | Existing in-initiative regular file is accepted; anchor remains informational. | Absolute, traversal, out-of-root or absent file adds an actionable error; v1 unchanged. |
| Risk projection | `IR-*` IDs in the impact risk table and v2 rendered Impact panel. | Every source ID appears in that panel. | Missing IDs report source ID/Impact target; no table IDs means no obligation. |
| API projection | Normalized HTTP method plus `/api/...` token in plan contracts and v2 rendered Architecture/Validation panels. | Every source token occurs in one allowed panel. | Missing route reports source token/allowed views; no token means no obligation. |
| Baseline | Existing `--write-baseline` flow. | Writes only after all integrity checks pass. | Any new error returns non-zero and does not treat a stale/new baseline as success. |

No database, network, consumer-source migration or client visual profile is involved.

## 7. Security, privacy and permissions

- Normalize evidence locators, remove anchors, reject absolute paths and `..`, resolve, then confirm the resolved path remains below the initiative directory before `is_file`/read.
- Do not include file contents, credentials or unrelated resolved paths in diagnostics.
- No privileged, destructive or external operation is needed; repository writes are standard task outputs.

## 8. Rollout, observability and rollback

- **Rollout:** land validator, unit/fixture tests, templates and reviewer guidance as one coherent bundle change; run baseline/write/recheck only against the synthetic fixture.
- **Success/failure signals:** targeted tests plus `validate_bundle.py` and Human Visibility commands return zero; diagnostics are asserted in negative tests.
- **Rollback trigger:** valid v1/v2 compatibility fixture fails, a false positive blocks a source pattern, or a resolver boundary issue appears.
- **Exact rollback/checkpoint:** revert the coordinated task commit; retain reproduction/ratchet evidence and re-open with the failing fixture. No consumer baseline is edited during rollback.

## 9. Brief coverage composition

| Source locator | Coverage | Rendered target | Reason |
|---|---|---|---|
| spec.md#1-10 | represented | Value, Architecture, Validation | Outcome, requirements and ACs are decision material. |
| reproduction.md#observed-expected-minimal-steps | represented | Impact/Validation | Shows actual blind spot and desired regression. |
| impact-map.md#1-8 | represented | Impact | Boundaries, risk controls and unknown must be visible. |
| plan.md#1-8 | represented | Architecture | Validation stages, boundary and rollback must be visible. |
| tasks.md#task-ledger | represented | Execution | No task is implementation-authorized until ready. |
| validation-plan.md#1-7 | represented | Validation | AC oracle/commands/reviewer proof must be visible. |
| decision-log.md#D-001-D-008 | represented | Evolution/Decision | Trade-offs, execution authority, coverage approval and retained review gates are visible. |
| progress.md#all | synthesized | Evolution | Current checkpoint and exact next step. |
| run-state.yaml#quality_gates | represented | Evolution/Coverage | Planning vs implementation state is explicit. |

**Author:** platform-engineering planner. **Coverage reviewer:** `spec012_coverage_review` (distinct). **Review date:** 2026-08-27. **Findings status:** pass after D-006/D-007 propagation repair. **Decision record:** D-008 approves coverage and Tasks Ready while preserving all evidence/evaluator gates.

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| U-001 | Which existing source patterns count as canonical HTTP contract syntax beyond tables/bullets? | validation maintainer | Inventory repository fixtures in T-001 and test only demonstrated forms. | yes for T-003 parser scope, no for T-001/T-002. |

## 11. Plan decision

**Plan Ready:** yes  
**Reviewer:** Harness Planner / user-authorized corrective planning  
**Reviewed at:** 2026-08-26  
**Conditions/links:** validation plan, negative fixtures and independent task evaluation remain mandatory before implementation completion.
