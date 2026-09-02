# Technical Plan: 018-derived-brief-completeness-and-delivery-integrity

**Status:** plan_ready  
**Owner:** Harness maintainer  
**Last updated:** 2026-08-27

## 1. Technical approach

Make the stakeholder brief a derived delivery artifact, rather than an optional
template created beside the sources. The implementation has four small,
separable layers:

1. classify the package lifecycle (`scaffolded`, `authored`, `rendered`,
   `reviewed`, `delivered`) from existing artifacts and evidence;
2. inspect the rendered HTML for unresolved template tokens/instructions and
   for the decision categories that are material to this package;
3. preserve a flexible coverage manifest in the sources: each material source
   heading says whether it is represented, synthesized, not applicable, or an
   owned unknown; and
4. make the existing validators and workflow reject an unsafe transition while
   still allowing any domain, vocabulary, layout, navigation pattern or number
   of sections.

There is no renderer today: `new_initiative.py` copies a template shell. T-002
defines the smallest explicit composition/refresh path; until then the shell
must never be called rendered. The validator checks provenance and honest state, not whether a project uses a
database, browser, Kafka, a diagram, tabs, cards, or a particular architecture.
Quality of reasoning stays with an independent rendered review.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-018-01 | Add a lifecycle/completeness gate to the existing validation path. | A scaffold can currently look like a brief. | New generator/runtime service. | Validator semantics must remain backwards-compatible for historical v1 briefs. |
| D-018-02 | Derive checks from source categories and provenance rather than fixed UI sections. | A good brief differs across domains. | Requiring a standard tab/card/schema layout. | Deterministic checks deliberately cannot certify narrative quality. |
| D-018-03 | Keep an independent rendered review as a separate gate. | HTML readability and decision usefulness need judgment. | Treating string checks as a design review. | A reviewer must be available before delivery. |
| D-018-04 | Preserve Pearson enforcement only for new/materially regenerated v2 briefs. | Brand policy is valid but should not invalidate historical briefs by surprise. | Globally rewriting legacy briefs. | Validator needs lineage-aware diagnostics. |

## 3. Size and proportionality

**Initiative size:** M.  
**Why:** changes touch package creation, validation, workflow state, fixtures
and rendered verification, but introduce no production application runtime.
**Smaller option considered:** detect only a known template sentence. It would
miss empty or differently worded scaffolds and would not prove source-to-brief
integrity. **Excluded:** mandatory information architecture, product-domain
schemas, hosted services, or automatic prose scoring.

## 4. Architecture readiness and proportionality

**Assurance profile:** A2-elevated. **Rationale:** delivery gating and public
decision artifacts are cross-cutting; a false pass is the observed failure.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Initiative Markdown and optional HTML can diverge. | HTML is a traceable projection with lifecycle status. | T-001 inventory; harness maintainer. |
| Components/responsibilities | Scaffolder, template, validator and workflow have separate behavior. | Explicit handoff among those existing surfaces. | T-001/T-003. |
| Interfaces/events/contracts | File/state contract only. | Additive lifecycle and diagnostics contract. | T-002 fixtures. |
| Data ownership/lifecycle | Sources are canonical; brief is derived. | Brief never becomes a hidden second source. | provenance attributes and coverage table. |
| Security/trust boundaries | No new network or secret boundary. | Local validation only. | not_applicable — no runtime service. |
| Failure behavior | Generic brief may pass/appear delivered. | Fail closed for new v2 transition with actionable cause. | V-001/V-003. |
| NFRs | Brief must stay accessible and inspectable. | Keep existing responsive/print/no-script semantics. | V-REG-003. |
| Compatibility/migration | Historical v1 may be pinned. | Do not force v2 checks absent a material refresh. | V-REG-002. |
| Rollout/rollback | Bundle scripts/templates release together. | Revert the additive validator/workflow patch. | T-003 evidence. |
| Unknowns | Exact bypass paths and existing fixture coverage. | Bound by T-001 before behavior is changed. | T-001 exit criteria. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | scaffold/template/validator inventory + fixtures | Spec Ready | Proven root-cause and acceptance fixtures. | yes |
| 2 | lifecycle/coverage contract + source records | T-001 approved | Additive, domain-neutral contract. | yes |
| 3 | validator/workflow/scaffolder implementation | T-002 approved | Unsafe v2 delivery transitions fail. | yes |
| 4 | fresh mock suite and HTML review | T-003 approved | Evidence that broad domains remain possible. | yes |

## 6. Contracts, security and operations

- **Contract:** lifecycle metadata and HTML `data-*` provenance are additive;
  existing source Markdown remains canonical.
- **Compatibility:** a v1 historical/pinned brief is diagnosed but not forced
  into v2 until a material regeneration/migration decision.
- **Privacy/security:** validators must not echo source bodies, secrets or
  fixture content in diagnostics; no network request is introduced.
- **Rollback:** revert the new gate and its tests as one change; do not remove
  evidence or rewrite a consumer package.
- **Signals:** validator exit code, fixture matrix and a rendered screenshot/
  browser review; failures name artifact/category, never claim prose quality.

## 7. Brief coverage composition (v2)

| Source locator | Coverage | Rendered target | Reason |
|---|---|---|---|
| spec.md §§1–8 | represented | Executive, change and outcome views | Core problem, scope, FR/AC. |
| plan.md §§1–6 | represented | Architecture and operating-model views | Decision, delta and rollback. |
| impact-map.md §§1–6 | represented | Impact/risk view | Affected boundaries and unknowns. |
| validation-plan.md §§1–6 | represented | Validation view | Proof and independent review. |
| tasks.md task fields | represented | Execution view | Work, authority and evidence. |
| decision-log.md | represented | Decision/next-step view | Traceable gate decisions. |
| progress.md | represented | Evolution/next-safe-step view | Checkpoint and exact next action. |
| run-state.yaml | represented | State/authority view | Truthful lifecycle and gate state. |
| domain-specific diagram | not_applicable | N/A | This harness change has no runtime topology to invent. |

**Author:** root (builder). **Coverage reviewer:** independent evaluator,
pending. **Decision record:** D-018-02, pending independent review.

## 8. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-018-01 | Which current validator path admits the generic brief? | T-001 builder | Reproduction fixture and code trace. | yes |
| Q-018-02 | What is the smallest stable representation of material coverage? | T-002 builder | Fixture-backed contract. | yes |

## 9. Plan decision

**Plan Ready:** approved  
**Reviewer:** audit_018_root_cause (independent)  
**Conditions:** D-018-03 accepted; T-001 is the only ready task.
