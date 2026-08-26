# Technical Plan: 008-semantic-brief-review-calibration

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-25

## 1. Technical approach

Extend the existing review path instead of introducing a runtime. Make the review output assess product, architecture/operations and delivery through `recoverable`, `superficial`, `absent` or justified `N/A`; make every finding source → lost fact → recovery action. Then distinguish source-coverage review before rendering from a short post-render test of decision loss. Add paired examples and a shallow negative fixture. The validator remains structural only.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| AD-001 | Extend existing Spec Guardian/spec-review and lifecycle guidance. | The gap is operational clarity, not a missing service. | New permanent brief-quality agent. | Reviewers need concise instructions. |
| AD-002 | Keep pre-render coverage and post-render meaning as distinct records. | Heading coverage does not prove decision usefulness. | Treat structural pass as final review. | A second reading is required. |
| AD-003 | Use qualitative lenses with justified N/A. | Generalizes to software, policy, research and operations. | Numeric score or mandatory software checklist. | Judgment stays independent. |
| AD-004 | Add paired calibration examples and one negative fixture. | Examples teach proportional depth more safely than hard rules. | Semantic parser or new harness. | Fixtures remain fictional/static. |
| AD-005 | Add a hard mirror only after stable, low-cost evidence. | Prevents complexity from outrunning the problem. | Immediate semantic gate. | Some review remains human/agent work. |

## 3. Size and proportionality

**Initiative size:** M.  
**Why:** several guidance/fixture surfaces change, with no runtime service, migration, external integration or production rollout.  
**Smaller option considered:** one sentence in the review skill. Insufficient because it cannot distinguish the two review moments or calibrate non-software work.  
**Complexity deliberately excluded:** no LLM evaluator, semantic score, JSON sidecar, new agent role, schema, CI gate or persistent state.

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** A2-elevated.  
**Rationale and trigger evidence:** a governance regression can approve shallow briefs across projects, but recovery is code/document-only and reversible.  
**A2/A3 source links/headings:** spec §7 AC-002/AC-005; impact map IR-002/IR-003.  
**Reapproval trigger:** automatic semantic approval, persistent service, or v1 compatibility change.

### Architecture scope/size profile

**Profile:** M.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Markdown sources feed author/reviewer and offline HTML. | Same context; explicit two-review loop. | impact map §3; planner. |
| Components/responsibilities | Spec Guardian has general review responsibility. | Existing reviewer emits three lenses and finding contract. | AD-001; T-001. |
| Interfaces/events/contracts | File-based templates/rules and decision log. | Review record carries source, lost fact and recovery action. | FR-002; T-001. |
| Data ownership/lifecycle | Markdown canonical; HTML derived. | Same ownership; correct source then refresh HTML. | impact map §3. |
| Security/trust boundaries | Static artifacts; no credentials. | Fictional examples stay redacted/offline. | impact map §2. |
| Critical runtime flows | No runtime request path. | Review flow is critical operational path. | flow below. |
| Failure behavior | Structural pass can mask shallow synthesis. | Post-render decision-loss review blocks Human Visibility. | AD-002; IR-002. |
| NFRs | Guidance must be concise/readable. | 60-second scan and progressive recovery survive. | AC-007; M-001. |
| Compatibility/migration | v1 is lineage-aware. | Preserve v1; v2 guidance applies on refresh. | FR-006; V-006. |
| Observability | Decision log/state hold review facts. | Same records reveal weak review. | FR-002; D-003 planned. |
| Rollout/rollback | Bundle files versioned together. | One reversible bundle change. | impact map §4. |
| Alternatives/trade-offs | Generic review permits shallow pass. | Calibrate before hard mirror. | AD-003–005. |
| Unknowns | Template/mirror reuse undecided. | Resolve via bounded tasks. | U-001–003. |

### Critical review flow

```txt
MD sources → author composition → distinct coverage review
          → rendered brief → distinct meaning review
          → source correction (if needed) → refresh → meeting
```

Text equivalent: coverage proves the sources were considered. Meaning review asks whether a stakeholder can still decide from the brief; it corrects canonical Markdown, never HTML alone.

### Current → target → delta and complexity envelope

| View | Current | Target | Delta/commitment | Reapproval trigger |
|---|---|---|---|---|
| Architecture/method | General review + structural validator. | Two short qualitative review moments with examples. | Guidance/templates/fixtures only. | New service or role. |
| Modules/classes/APIs/data/contracts | No runtime contract. | Review-record vocabulary and fixture assertions. | No public API or storage. | Score/schema/parser. |
| Process/tooling | Existing lifecycle/state/log. | Reuse it; no sidecar. | One explicit post-render question. | Mandatory ceremony for A1 work. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | review skill, agent/workflow/template wording | D-001 and plan ready | Lenses and finding contract are discoverable. | yes |
| 2 | software/non-software/negative fixtures | Step 1 | Calibration captures sufficient and shallow synthesis. | yes |
| 3 | focused tests/validator review | Steps 1–2 | Structural checks stay structural; no score/parser. | yes |
| 4 | rendered reviews and bundle validation | all changes | Evidence of usefulness and bounded impact. | yes |

## 6. Contracts, data and compatibility

- **API/events:** no runtime API, event or database contract.
- **Database/storage:** no new storage; repository-owned Markdown, HTML, logs and fixtures remain canonical/derived as today.
- **External systems:** none; offline briefs use no remote assets.
- **Compatibility/migration:** v1 lineage stays untouched; any v1 failure needs explicit migration/review.

## 7. Security, privacy and permissions

- **Authentication/authorization:** not applicable; no authenticated runtime behavior.
- **Secrets/PII:** fixtures use invented roles/values; never include tokens, customer data or sensitive topology.
- **Required permission:** ordinary versioned-file changes only.
- **Destructive operations and approvals:** none; a future semantic mirror needs explicit human approval under AD-005.

## 8. Rollout, observability and rollback

- **Rollout:** versioned bundle update for new/materally refreshed v2 initiatives.
- **Success/failure signals:** shallow fixture is caught; no score/parser appears; commands and rendered review pass.
- **Rollback trigger:** irrelevant mandatory content, v1 regression, or unintended deterministic gate.
- **Exact rollback/checkpoint:** revert bounded guidance/template/fixture files; retain decision-log history.
- **Gate authority:** the distinct reviewer may block or clear `brief_coverage_ready` and `human_visibility_ready` through a named decision-log record; this is qualitative review, not an automatic validator result. The bundle maintainer accepts T-004 evidence for release. Human approval is not required for this bounded guidance change, but is required before any future semantic hard mirror under AD-005.

## 9. Brief coverage composition (v2)

Author: **Codex / brief author**. The independent reviewer and result are recorded after coverage review; this table is its review input, not self-approval. Until D-004 is accepted, no brief may present this composition as a completed coverage review.

| Source locator | Coverage | Rendered target | Reason when required |
|---|---|---|---|
| spec.md §1–3 problem/objective/outcome | synthesized | `#decision-snapshot`, `#scope` | Core decision context. |
| spec.md §4–5 actors/non-goals | represented | `#scope` | Scope boundaries recover directly. |
| spec.md §6–7 requirements/acceptance | represented | `#scope`, `#validation` | Stakeholder-material proof. |
| spec.md §8–10 constraints/risks/validation | synthesized | `#impact`, `#validation` | Condensed without hiding controls. |
| spec.md §11 guardian decision | represented | `#evolution`, `#decision` | Gate/authority provenance. |
| impact-map.md §1–4 boundary/surfaces/flow/compatibility | synthesized | `#impact`, `#architecture` | Impact and flow views. |
| impact-map.md §5 risks/controls | represented | `#impact` | Trigger/control/contingency are recoverable. |
| impact-map.md §6–8 unknowns/review/decision | represented | `#impact`, `#decision` | Conditions affect requested decision. |
| plan.md §1–4 approach/decisions/proportionality/architecture | synthesized | `#architecture`, `#decision-snapshot` | Progressive architecture depth. |
| plan.md §5–8 sequence/contracts/security/rollback | represented | `#architecture`, `#execution` | No runtime claim is hidden. |
| plan.md §9 composition | represented | `#coverage` | Human coverage register. |
| plan.md §10–11 questions/decision | represented | `#decision`, `#evolution` | Gate and unknowns explicit. |
| tasks.md ledger/T-001–T-004 | represented | `#execution` | Drafts visibly non-authorizing. |
| validation-plan.md §1–8 | represented | `#validation` | AC mapping and limits recoverable. |
| decision-log.md D-001 onward | represented | `#evolution`, `#decision` | Append-only rationale/status. |
| progress.md outcome/checkpoint/risks | synthesized | `#evolution` | State summary, not duplication. |
| run-state.yaml status/gates/risks | represented | `#decision-snapshot`, `#evolution` | Truthful authorization state. |

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | Is a standalone review-report template needed? | T-001 builder | Resolved D-007: existing skill, agent, rule, workflow and design guidance are sufficient; no new template. | no |
| Q-002 | Is a deterministic locator check worth its cost? | T-003 + reviewer | Resolved D-007: fixture wiring is enough; no locator/mirror added. | no |
| Q-003 | Who approves a future mirror? | human sponsor | Unchanged: no mirror exists; a future sponsor must be named before one is proposed. | no |

## 11. Plan decision

**Plan Ready:** yes  
**Reviewer:** Codex / Harness Planner  
**Reviewed at:** 2026-08-25  
**Conditions/links:** impact mapped; validation and preliminary tasks remain non-authorizing; independent coverage review is required before Human Visibility.
