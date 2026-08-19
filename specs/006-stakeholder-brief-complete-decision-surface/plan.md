# Technical Plan: 006-stakeholder-brief-complete-decision-surface

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-19

## 1. Technical approach

Deliver v2 as a coordinated contract change rather than a template-only edit.
First define the source inventory, coverage/provenance model, review identity and
new lifecycle states. Then extend the plan/readiness guidance for proportional
architecture. Only after those contracts are fixture-testable should the visual
template, validator, scaffolder and consumer guidance change.

The final page remains a derived, static artifact. It exposes a short executive
path and progressively disclosed complete decision content. Deterministic code
enumerates stable sources/headings, verifies provenance/coverage/freshness and
checks that author/reviewer identities differ. Agents and humans continue to
choose synthesis, diagram depth and whether the page is decision-useful.

This is the smallest safe approach because changing only the HTML would leave
the lifecycle unable to include tasks, while changing only instructions would
leave the completeness contract unenforced.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| AD-001 | Introduce `data-harness-brief-design="v2"` for new briefs and validate v1/v2 by lineage. | The content and lifecycle contract changes materially. | Reuse v1 marker; would hide incompatible semantics. | Requires migration and dual fixtures. |
| AD-002 | Keep canonical source artifacts authoritative; make HTML the single meeting-reading projection. | Preserves spec-driven traceability and safe regeneration. | Edit decisions directly in HTML; creates drift and ambiguous authority. | Post-meeting propagation is mandatory. |
| AD-003 | Represent coverage through block-level `data-source`, `data-source-section`, `data-coverage` and stable target IDs plus the human coverage table; do not embed a JSON index. | Gives DOM-local provenance and human inspection without duplicate state. | Embedded JSON index and separate permanent checklist sidecar; both add duplicate/fragmented state. | D-010 resolves the minimal form before T-002/T-003. |
| AD-004 | Require full disposition of principal headings, but permit synthesis and justified N/A; prohibit link-only treatment for material core headings. | Completeness without verbatim duplication. | Word counts or copy-all generation; reward filler and harm readability. | Reviewer judgment remains essential. |
| AD-005 | Use progressive enhancement: semantic sections/anchors/details are the baseline; minimal inline tab behavior is allowed only if print, keyboard and no-script retain all content. | Supports one-page depth and offline accessibility. | JS-only tabs or external framework; can hide content and break portability. | UI choice is validated, not prescribed prematurely. |
| AD-006 | Add `tasks_drafted` and `brief_coverage_ready` before `human_visibility_ready`; keep `tasks_ready` after meeting decisions are propagated. | Makes tasks visible without authorizing execution. | Keep current order; cannot cover tasks. Put Tasks Ready before meeting; risks premature execution. | State, workflows and docs must migrate together. |
| AD-007 | Require a distinct brief coverage reviewer before final render and retain the existing independent rendered review. | Separates source completeness from visual/meeting quality. | Author self-check only; repeats normalized omissions. | Runtime needs a second identity or named human. |
| AD-008 | Replace the one-view cap with risk/size architecture profiles and explicit applicability. | Allows architect-grade depth without universal ceremony. | Mandatory fixed C4 set; disproportionate for local changes. | Plan Ready becomes more demanding for M/L/high/unknown work. |
| AD-009 | Build the change/evolution view from append-only decisions plus Git/base-ref or local hash baseline. | Makes repeated meetings intelligible and auditable. | Narrative maintained only by the author; easy to omit or stale. | Baseline compatibility needs tests. |
| AD-010 | Ship all contract surfaces in one versioned release with v1 legacy acceptance. | Avoids template/workflow/validator skew. | Gradual incompatible rollout; consumers can enter impossible states. | Larger atomic change, hence task/evidence discipline. |

## 3. Size and proportionality

**Initiative size:** L.  
**Why:** it changes public templates, lifecycle/state semantics, validator,
scaffolding, agent guidance, consumer integration and backward compatibility.  
**Smaller option considered:** extend only the HTML and add source links. It is
insufficient because tasks are currently created after the brief and links do
not prove principal-heading coverage.  
**Complexity deliberately excluded:** hosted editing, database, remote assets,
semantic auto-approval, screenshot CI, mandatory fixed diagram count and mass
historical migration.

## 4. Architecture readiness profile

The initiative itself is L/high and therefore requires the following source
coverage before implementation:

| Dimension | Current state | Target/decision | Proof or owner |
|---|---|---|---|
| System context | Passive bundle copied/pinned into consumer repos; agents read Markdown and generate HTML. | Same trust boundary; v2 changes only portable files/scripts and derived HTML. | `docs/architecture.md`, AD-002 |
| Components/responsibilities | Templates define shape; rules/workflows guide; Python validators check stable facts; agents judge semantics. | Add coverage inventory/review and version-aware validation without moving semantic approval into code. | AD-003, AD-007 |
| Interfaces/contracts | v1 marker, shell hooks, four required sources, run-state gates. | v2 lineage, expanded sources, provenance/coverage attributes, two pre-execution states and review identity. | AD-001, AD-003, AD-006 |
| Data ownership/lifecycle | Markdown/state/evidence canonical; HTML and hash baseline derived. | Same ownership; expanded baseline and change view derived from canonical history. | AD-002, AD-009 |
| Security/trust | Consumer repository and local reviewer trust boundary; no network. | Same; expanded diagrams require minimum-safe abstraction/redaction guidance. | spec EC-008 |
| Critical runtime flow | Sources → one synthesis → validator/review → tasks. | Sources → task draft → coverage plan/review → final brief → meeting → propagation → Tasks Ready. | AD-006 |
| Failure behavior | Missing/stale base sources fail; semantics rely on review. | Missing heading/provenance/reviewer fails; contradictions return to owning gate; unavailable reviewer blocks. | FR-008–009, FR-017 |
| NFRs | Offline, responsive, accessible, stdlib validator. | Preserve plus print/no-script/deep-content accessibility. | AC-011 |
| Compatibility/migration | Consumers pin versions; v1 marker exists. | Dual validator behavior and v2-only new scaffold after release. | AD-001, AD-010 |
| Observability | CLI diagnostics. | Versioned, source/heading-specific coverage and freshness diagnostics. | FR-017 |
| Rollout/rollback | Bundle release/pin. | One coordinated release; rollback pin; no destructive document migration. | AD-010 |
| Alternatives/trade-offs | Concise/selective v1 minimizes ceremony but omits execution/history depth. | Complete disposition + progressive depth adds process but matches meeting role. | spec Problem, R-001–004 |

No material architecture dimension is currently unknown. The implementation
choices U-001–U-004 are bounded and assigned in the impact map.

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Rules, workflow, state/template contracts, role/skill guidance | Human execution approval; AD-003 representation chosen | Coherent v2 semantic contract and lifecycle. | yes, Git revert |
| 2 | Canonical HTML/design standard and populated 006/example brief | Step 1 contracts; task draft available | Progressive v2 meeting surface with provenance and architecture profiles. | yes |
| 3 | Validator, baseline/version handling and unit fixtures | Steps 1–2 stable | Deterministic coverage/freshness/reviewer enforcement with v1 compatibility. | yes |
| 4 | Scaffolder, manifest, prompts, docs and Factory fixture | Step 3 passing | Consumers can adopt the complete contract reproducibly. | yes |
| 5 | Rendered/eval/regression review and release evidence | Steps 1–4 complete | Independent proof, migration notes and releasable package. | yes until external release/pin |

## 6. Contracts, data and compatibility

- **DOM/provenance:** v2 root marker; stable view IDs; block-level source,
  section/ID and coverage attributes; human coverage register; no embedded JSON
  or duplicate sidecar unless a later approved fixture proves the attributes
  cannot express the contract.
- **State:** add `tasks_drafted` and `brief_coverage_ready`; preserve existing
  gates and forbid implementation until `human_visibility_ready` and
  `tasks_ready` are both true.
- **Baseline:** version field, reviewed-at/by metadata, source hashes for the
  applicable set, coverage review identity and prior decision/change anchor.
- **External systems:** none. Git/base-ref is optional with local-hash fallback.
- **Compatibility:** historical v1 validation branch; newly scaffolded v2 after
  release; explicit diagnostic for material v1 refresh/migration.

## 7. Security, privacy and permissions

- **Authentication/authorization:** not applicable; local files only.
- **Secrets/PII:** do not copy secrets, tokens, personal data or sensitive
  production topology into HTML, metadata, diagnostics or fixtures.
- **Required permission:** normal repository write access for implementation;
  explicit human approval before tasks become ready; release/publish remains a
  separate authorization.
- **Destructive operations and approvals:** no destructive migration. Do not
  overwrite historical briefs or baselines without explicit, reviewable update.

## 8. Rollout, observability and rollback

- **Rollout:** implement on a feature branch/change set, prove v1/v2 fixtures,
  update bundle version/release notes, then let consumers adopt by pin update.
- **Success signals:** all deterministic suites pass; v2 example passes desktop,
  narrow, keyboard, no-script and print review; three audience evals recover the
  decision packet; v1 fixture remains valid.
- **Failure signals:** old briefs fail, draft tasks appear authorized, coverage
  register disagrees with DOM, print/no-script loses content, validator claims
  semantic approval or source changes do not stale the brief.
- **Rollback trigger:** any high-severity compatibility, authority or data-loss
  regression; inability to preserve executive readability; false Tasks Ready.
- **Exact rollback/checkpoint:** revert the coordinated v2 change or pin the
  previous bundle release. Preserve initiative 006 sources and decision history;
  reset no consumer data.

## 9. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | Attributes only or attributes plus embedded JSON coverage index? | root Orchestrator | Resolved by D-010: attributes plus human table only; no JSON index. | no |
| Q-002 | Native details/anchors or minimally scripted accessible tabs? | T-002 Builder/Evaluator | Prototype against keyboard/no-script/print AC-011; retain semantic fallback. | no |
| Q-003 | Extend current baseline schema in place or add an explicit v2 section? | T-003 State Keeper/Evaluator | Resolved by D-015: evolve the same baseline file to schema v2 only for v2 lineage; retain schema v1 unchanged for historical/pinned v1. | no |
| Q-004 | Dedicated permanent agent or reusable assembly/review skills with distinct identities? | root Orchestrator | Resolved by D-011: extend existing Spec Guardian/spec-review and runtime identities; no permanent agent/skill. | no |

## 10. Plan decision

**Plan Ready:** yes  
**Reviewer:** Codex acting as Harness Planner  
**Reviewed at:** 2026-08-19  
**Conditions/links:** D-009 approved execution and D-010/D-011 resolve the
T-001 contract choices; every task requires a distinct Evaluator and evidence
pack; release/publishing is not authorized by plan approval.
