# Impact Map: 006-stakeholder-brief-complete-decision-surface

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex acting as Impact Mapper  
**Reviewed at:** 2026-08-19  
**Overall risk:** high

## 1. Change boundary

Change the reusable bundle contract for how non-trivial initiatives build,
review, validate and refresh `stakeholder-brief.html`. The change spans source
templates, agent/skill guidance, lifecycle ordering, state/gates, consumer
validation, fixtures, documentation and examples.

Keep these boundaries intact:

- Markdown, state and evidence artifacts remain canonical;
- the bundle remains passive, portable and vendor-neutral;
- v1 historical/pinned briefs are not silently rewritten;
- Builder/Evaluator separation and terminal evidence gates are unchanged;
- the executive opening and visual language established in v1 are preserved.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Initiative source model | `.harness/templates/{spec,plan,tasks,impact-map,validation-plan,decision-log,run-state}.md|yaml` | direct | Add architecture readiness, task-draft/brief-coverage states and source coverage expectations where appropriate. | high | FR-003–017 |
| Brief UI/design | `.harness/templates/stakeholder-brief.html`, `stakeholder-brief-design.md` | direct | Add v2 lineage, progressive views, provenance, coverage and evolution surfaces while retaining v1 opening. | high | FR-001–006, FR-013–015, FR-020 |
| Human Visibility rule | `.harness/rules/human-visibility.md` | direct | Replace selective-summary completeness with principal-heading disposition and proportional depth. | high | FR-003–012 |
| Lifecycle/workflows | `.harness/workflows/sdd-lifecycle.md`, feature/bugfix/refactor workflows | direct | Move preliminary task breakdown before final brief; add coverage review and post-meeting propagation before Tasks Ready. | high | FR-007–009, FR-016 |
| Agent roles and skills | Spec Guardian, Delivery Orchestrator, Harness Planner, Impact Mapper, State Keeper; spec/task/validation/impact skills; new brief assembly/review guidance if justified | direct | Enforce architecture/source completeness and distinct coverage review. | high | FR-008–012, FR-016 |
| Validator | `scripts/validate_human_visibility.py`, `validate_bundle.py` | direct | Version-aware v1/v2 rules, expanded sources, heading coverage, provenance, freshness and review identity. | high | FR-017–018 |
| Scaffolding/manifest | `scripts/new_initiative.py`, `manifest.yaml`, templates README | direct | New initiatives receive v2 contract and state fields after release. | medium | FR-018–019 |
| Consumer integration | `docs/consumer-enforcement.md`, `INSTALL.md`, `prompts/use-in-consumer-project.md`, Factory fixture | indirect | Explain migration, new order, review identity and expanded freshness. | medium | FR-018–019 |
| Tests/fixtures | validator, scaffolder and Factory tests; initiative example(s) | direct | Add positive/negative v2, lifecycle, delta and compatibility cases. | high | AC-002–012 |
| Runtime application/service | not_applicable: bundle remains static files and scripts | none | No hosted UI, API or workflow engine. | low | NG-005 |
| Data/storage | local HTML metadata and hash baseline only | indirect | Expanded source hashes/coverage metadata; no database. | medium | FR-006, FR-015, FR-017 |
| Auth/security/privacy | docs/templates/diagram guidance | indirect | Add redaction/minimum-safe-abstraction rule; no new permissions. | medium | EC-008, NG-008 |
| Build/deploy/infra | package/release and consumer CI invocation | indirect | Versioned release and backward-compatible validator behavior. | medium | FR-018 |
| Observability/support | validator diagnostics and migration messaging | indirect | Precise missing coverage, stale source and v1/v2 diagnostics. | medium | FR-017–019 |

## 3. Dependency and data flow

```txt
canonical initiative sources
  -> heading inventory + task draft + prior baseline
  -> brief assembly plan with provenance/coverage disposition
  -> independent coverage review
  -> corrected final v2 HTML
  -> deterministic validation + rendered review
  -> stakeholder meeting and recorded decisions
  -> append-only decision log + affected source updates
  -> delta/coverage refresh
  -> Human Visibility Ready + Tasks Ready
  -> unchanged implementation/evidence/evaluation gates
```

Control boundary:

```txt
machine: existence, IDs, headings, provenance, hashes, order, identity
human/agent: meaning, synthesis, diagram fitness, contradiction judgment
```

## 4. Compatibility and migration

- **Backward compatibility:** version-aware validation accepts historical v1
  under its existing contract. Newly scaffolded non-trivial initiatives use v2
  after the bundle release. A material v1 refresh receives an explicit upgrade
  path or reviewed legacy exception.
- **Data migration:** no database. Local baselines may gain version, expanded
  source hashes, coverage and review metadata through an explicit writer.
- **Rollout/feature flag:** release as a bundle version with fixture-proved v1
  compatibility; consumer repositories opt in by updating the pinned bundle.
- **Rollback implications:** revert the bundle version/pin and restore v1
  scaffold/validator behavior. Do not delete v2 briefs or decision history;
  treat them as forward-authored artifacts readable as HTML.

## 5. Regression risks

| ID | Risk | Trigger/surface | Mitigation | Validation ID |
|---|---|---|---|---|
| IR-001 | Existing v1 briefs fail unexpectedly. | Version-unaware validator change. | Explicit lineage branch and legacy fixtures. | V-010, V-012 |
| IR-002 | Tasks become implicitly authorized before review. | Task draft moved earlier. | Separate `tasks_drafted` from `tasks_ready`; visible draft labels and state tests. | V-004, V-007 |
| IR-003 | Source coverage passes with empty/generic content. | Metadata-only enforcement. | Independent semantic coverage review and negative empty-heading fixtures. | V-002, V-003, V-006 |
| IR-004 | Brief becomes huge and unusable. | Verbatim copying or always-open deep content. | Progressive views, executive-path eval, expandable complete ledgers. | V-001, V-006, V-011 |
| IR-005 | Architecture views contain invented claims. | Diagram depth exceeds sources. | Plan Ready dimensions, provenance and block/discovery rule. | V-005, V-006 |
| IR-006 | Decision made in meeting exists only in HTML/transcript. | Post-meeting manual shortcut. | Append-log/source-propagation workflow and fixture. | V-009 |
| IR-007 | Print/no-script hides deep content. | UI tabs implemented as display-only JS. | Progressive enhancement and print/no-script tests. | V-011 |
| IR-008 | Frequent false freshness failures. | Every operational edit treated as material. | Explicit, reviewed non-material exception with delta diagnostic. | V-008, V-012 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Whether progressive views should use native `details`/anchors or a minimal accessible tab controller. | Affects accessibility, print and no-script behavior. | T-002 prototype and rendered evaluation; Builder/Evaluator. | no; decision bounded by AC-011 |
| U-002 | Exact machine-readable coverage representation: repeated `data-*` attributes only or attributes plus embedded JSON. | Affects validator complexity and authoring ergonomics. | T-001 contract fixture; Harness Planner. | no; must be decided before T-002 |
| U-003 | Material-change baseline schema evolution versus a separate v2 baseline key. | Affects compatibility with v1 baselines. | T-003 compatibility tests; State Keeper. | no; must be decided before release |
| U-004 | Whether a new permanent agent definition is necessary or two skills plus distinct runtime identities are sufficient. | Could add process weight without improving independence. | T-001 role/skill design review; Delivery Orchestrator. | no |

## 7. Recommended reviewers and checks

- **Specialist/human:** product/business stakeholder; software architect;
  accessibility-aware design reviewer; consumer integration maintainer.
- **Unit/integration/contract/E2E:** validator unit fixtures, scaffold smoke test,
  Factory consumer fixture, lifecycle/state contract tests, version compatibility
  and baseline/delta tests.
- **Manual/operational:** desktop, narrow, keyboard, no-script and print review;
  five-minute cross-role meeting eval; side-by-side v1/v2 comparison.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes  
**Approval/evidence:** source analysis and human direction recorded in
`decision-log.md`; execution approval pending review of the complete package.  
**Conditions before implementation:** approve the v2 scope and lifecycle;
resolve U-002 in T-001 before template/validator implementation; assign distinct
Builder/Evaluator identities; do not set any task to `ready` before human
approval is recorded.
