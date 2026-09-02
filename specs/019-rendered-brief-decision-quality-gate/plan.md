# Technical Plan: 019-rendered-brief-decision-quality-gate

**Status:** plan_ready candidate  
**Owner:** platform engineering  
**Architecture profile:** high — the changed contract spans source composition,
post-render review, lifecycle state, fixtures and reusable agent guidance.

## 1. Decision and delivery strategy

Add a post-render decision-quality review beside—not inside—the deterministic
validators. The reviewer receives the originating functional request, the
canonical source set and the locally served `stakeholder-brief.html`. Five
independent lenses record whether the page is sufficient for their real
decision. A material `REVISE` blocks qualitative approval. A deterministic
check can only confirm the evidence shape, distinct identities, input locators,
disposition and freshness; it must never infer prose quality from counts,
keywords, DOM shape or an LLM score.

The delivery increment is a reusable protocol and enforcement path that turns
the M001–M008 observation into a repeatable gate. It does not promise that all
future briefs look alike: compact operations work may legitimately use prose;
architecture with material components, data, trust or failure relations needs
a connected accessible representation selected by the author.

## 2. Current → target architecture

```txt
functional request + canonical Markdown + run-state
    -> source-backed renderer -> locally served HTML
    -> five independent decision reviews -> accountable disposition
    -> deterministic evidence/state/freshness verifier -> lifecycle gate
```

**Current state.** v2 validation proves lineage, provenance, shell hooks,
coverage, state and freshness. Existing semantic calibration asks product,
architecture/operations and delivery questions, but does not require the five
decision lenses or make a material qualitative revision block the delivery
claim. The `20260827-spec018-t004` mock run therefore passed structural checks
while all eight HTML briefs were rejected by the roles.

**Target state.** A review record contains stable locators for the original
request, source inventory, locally served HTML and each role finding. The
reviewer names the missing decision, source fact weakened/lost, materiality,
recovery action in canonical sources and final disposition. The validator
rejects a claimed quality-ready state when that record is absent, stale,
self-approved or materially unresolved. It does not reject a different but
adequate presentation merely because tabs, cards, diagram type or stack differ.

## 3. Role protocol and adaptive representation policy

Every role answers its own decision question and may return `approve`,
`revise`, `N/A with reason`, or `escalate`:

| Lens | Decision it must recover from HTML | Material loss example |
|---|---|---|
| Architect | boundaries, contracts, data/trust/failure and safe rollback when applicable | prose arrows hide an integration, owner or failure path |
| System designer | information hierarchy, connected relationships and accessible recovery | a material flow is an unconnected list or depends on colour/hover |
| Executive / C-level | change, business perturbation, trade-offs, risk and authority | cost, decision owner or consequence is only in Markdown |
| Delivery manager | workfronts, dependency/order, increment, risk/authority, proof and next safe step | task titles conceal the executable slice and evidence |
| General stakeholder | intent, scope/anti-scope, affected people, success and meaningful unknowns | reader cannot tell what changes for whom or what is being decided |

Materiality drives the representation. A simple policy or operating action may
be a concise, source-backed textual explanation. When a reader must reason
about a relationship among components, state, trust, data or failure behavior,
the HTML uses a connected model with a text equivalent (for example semantic
HTML flow, accessible SVG, a labelled relationship table, or another reviewed
equivalent). Dense content may use tabs, accordions or sections when that helps
retrieval; no count or component is mandated.

## 4. Source, evidence and state contracts

The existing decision log remains canonical. A new evidence record (or an
explicitly linked per-run review record) contains only locators and summaries:
no copied request body, secrets or unredacted source data. Each role must cite:

1. input locators and render URL/path inspected;
2. decision question and disposition;
3. materiality and the source locator/fact, if revised;
4. what remains impossible without Markdown;
5. source recovery action and re-review result.

The state records the accountable author, five reviewer identities, review
record locator, digest/freshness anchor, `quality_gate` disposition and any
exception/dissent owner. A material revision sets the gate false. A dissent may
be accepted only by a named accountable owner with scope, rationale, residual
risk and expiry; it cannot be silently converted to pass. The disposition is
finding-specific and must name its authority, corrected-render evidence and a
re-review by the role that raised it.

For every capability, the reviewer declares `material`, `not_material` with a
reason, or `insufficient`. `insufficient` is a blocking revision. Operational
independence means reviewer identity/role differs from the source author and
the task builder; review metadata records the role scope, timestamp and local
browser/server environment. The evidence input section records request/source
digests and locators plus HTML URL/artifact digest, never source bodies.

## 5. Implementation sequence and rollback

1. Add the protocol, negative/positive calibration fixtures and tests proving
   that a structurally valid decision-poor page cannot claim quality approval.
2. Add lifecycle/state and deterministic evidence verification; preserve old
   v1/v2 structural behavior and keep qualitative judgment outside the parser.
3. Publish the reusable rendered-review skill and local-server inspection
   procedure; update Human Visibility/Spec Guardian guidance.
4. Run all eight mock requests in a disposable root, inspect request/sources/
   HTML through all five lenses, repair only source-backed defects, regenerate,
   re-review and record the outcome.

The negative fixture intentionally keeps lineage, provenance, freshness and
structural validity while hiding material relation, authority and execution
facts; at least three role findings must reject it. The positive fixture uses a
different domain and a justified non-tab/non-diagram alternative where such
widgets are not material. This calibrates adaptability instead of imposing a
visual house style.

Rollback is removing the new opt-in quality-ready assertion and its fixtures
while retaining existing Human Visibility behavior. No consumer data migration,
network call, logo/profile behavior, schema or external API changes occur.

## 6. Coverage composition

| Source / principal matter | Disposition | HTML target | Reason |
|---|---|---|---|
| `spec.md#problem-objective-outcomes` | represented | `#scope`, `#decision` | The rejected run and desired decision quality are the executive context. |
| `spec.md#functional-requirements` | represented | `#architecture`, `#validation`, `#execution` | Gate behavior and adaptive limits must be inspectable. |
| `spec.md#acceptance-criteria` | represented | `#validation` | Each acceptance proof is stakeholder-material. |
| `impact-map.md#change-boundary-risks` | represented | `#impact` | Cross-cutting lifecycle risk and controls affect approval. |
| `plan.md#current-target-role-protocol` | represented | `#architecture` | The changed review flow and role responsibilities are material. |
| `tasks.md#task-ledger` | represented | `#execution` | The executable increments, dependencies and evidence are material. |
| `validation-plan.md#traceability-evals` | represented | `#validation` | The separation of deterministic and qualitative proof is material. |
| `decision-log.md#D-001-D-004` | represented | `#evolution`, `#decision` | Scope and quality decisions remain visible. |
| `progress.md#current-status` | synthesized | `#decision` | The next safe step must be visible without duplicating the ledger. |
| `run-state.yaml#quality-gates` | synthesized | `#decision` | Gate state is summarized with provenance rather than treated as prose. |

## 7. Risks and controls

| Risk | Control | Residual / owner |
|---|---|---|
| A fixed visual rubric rejects valid unfamiliar work | Review capability, materiality and recovery—not UI components; N/A is reasoned. | Reviewer judgment remains fallible; platform owner calibrates fixtures. |
| “Agent review” becomes an uninspectable self-approval | Distinct named roles, locators, role findings and a separate evaluator for each implementation task. | Human escalation remains available. |
| Review evidence leaks functional request data | Store locators and concise findings only; reviewer follows existing redaction rules. | Source access remains governed by project. |
| Full mock suite is costly | Disposable local roots and targeted rerender/review loop; no external services. | Runtime remains a delivery cost; delivery manager owns it. |
| Review finding does not drive a repair | Require request/source/HTML locators, decision impact, canonical recovery action and originating-role re-review. | Reviewer can still disagree; accountable disposition is visible. |

## 8. Rendered-review correction D-005

The first independent rendered reading found a material synthesis loss in this
SPEC's own HTML. The coverage register claimed that `#impact` represented both
affected surfaces and risks, while it rendered only risks. The page also named
the five lenses without their decision questions, and condensed the
finding→source repair→rerender→originating-role re-review lifecycle.

Recovery is source-backed and deliberately compact: project the affected bundle
surfaces/contracts in `#impact`; project decision question plus materiality
outcome for each lens and the finding lifecycle in `#architecture`; project
task authority, command/evidence and the correction loop in `#execution` and
`#validation`; project compatibility, rollback and accountable dissent in
`#decision`. No new visual component, tab count or diagram technology is
required. The originating reviewer must re-read the served corrected HTML.

## Plan readiness decision

**Plan Ready:** pending independent planning review  
**Blocking condition:** reviewer must confirm that the protocol blocks decision-poor
briefs without mandating a visual or technical form.
