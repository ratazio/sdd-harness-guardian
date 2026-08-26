# Technical Plan: 007-risk-based-assurance-contracts

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** platform-engineering  
**Last updated:** 2026-08-20

## 1. Technical approach

Use a guidance-first, mirror-last evolution. Extend existing canonical
artifacts rather than adding a new test-management model. First define the
profile decision and task assurance contract in templates, rules and existing
Planner/Evaluator guidance; prove it in a fictional 006 derivative; only then
add the smallest validator checks justified by stable failures.

The approved assurance profiles are:

| Profile | Intended use | Method depth |
|---|---|---|
| A1 — local | reversible/local/low-risk change | Current concise contract plus rationale for N/A checks. |
| A2 — elevated | M/L, cross-boundary, API/data/UI material, high or unknown risk | Explicit delta, envelope, task assurance and independent review. |
| A3 — critical | local policy identifies safety, regulated, security or vital impact | A2 plus named accountable human and applicable sector/local policy; Guardian makes no compliance claim. |

D-004 resolves Q-001/U-001: A3 is an escalation marker to named local policy
and accountable authority, never a Guardian certification.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| AD-001 | Reuse plan, task, validation and evidence artifacts. | Keeps consumer workflow portable and comprehensible. | Required assurance sidecar/database. | More sections in existing files; templates must remain progressive. |
| AD-002 | Treat profile selection, test selection and semantic adequacy as guided human/agent judgment. | These depend on domain/risk context. | Universal deterministic checklist or LLM auto-approval. | Review quality matters and requires independent evaluation. |
| AD-003 | Add only a minimal deterministic core after fixture evidence. | Fields/links/state are stable; adequacy is not. | Early comprehensive validator. | Some semantic omissions rely on review/ratchet until recurring. |
| AD-004 | Make brief a loss-aware projection of ledgers, not a replacement source. | Avoids meeting surface becoming decorative. | Summary-only cards or duplicate authoring. | Dense material must use progressive disclosure. |
| AD-005 | Preserve 006 and use a labelled fictional derivative. | Historical evidence must stay trustworthy. | Editing old approved evidence. | Fixture needs clear provenance. |

## 3. Size and proportionality

**Initiative size:** L.  
**Why:** it changes the contract used across all consumer specs, templates,
guidance, visibility, validation and compatibility.  
**Smaller option considered:** guidance-only documentation. It does not make
the commitment visible in consumer artifacts or prevent unsafe task closure.  
**Complexity deliberately excluded:** new workflow engine, database, remote
test service, static universal taxonomy, mandatory tools, persistent agents and
unbounded machine validation.

## 4. Architecture readiness and proportionality

**Assurance profile:** A2-elevated — required by high risk and bundle-wide consumer impact; see D-004.  
**Architecture scope/size profile:** L/high — source-backed from `spec.md` and `impact-map.md`.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Guardian supplies portable artifacts to consumer agents. | Same boundary; richer contract stays in consumer artifacts. | AGENTS.md, spec §1. |
| Components/responsibilities | Templates/rules guide; validators check stable facts; people/agents judge semantics. | Existing roles gain assurance guidance; no permanent role by default. | AD-001–003. |
| Interfaces/events/contracts | Existing files/brief provenance/state gates. | Conditional assurance fields and brief views; new scaffolds start `unknown`, while historical/pinned sources remain compatible. | D-007; prove with T-003. |
| Data ownership/lifecycle | Consumer owns sources/evidence; bundle owns templates/scripts. | Unchanged; no assurance database. | spec §10. |
| Security/trust boundaries | Local repo and reviewer trust boundary. | Redaction and local-policy escalation for critical work. | spec EC-006, R-007. |
| Critical runtime flows | Spec → plan → validation → tasks → evidence → evaluation. | Profile/delta/assurance choices become explicit before task authorization. | spec O-001–008. |
| Failure behavior | Evidence/evaluator gate exists. | Blocking failure/waiver structure becomes explicit and auditable. | FR-009. |
| NFRs | Offline, vendor-neutral, accessible. | No remote dependency; validators remain local/fast. | spec §10. |
| Compatibility/migration | v1/v2 lineages exist. | Explicit adoption path; no retroactive break; manual omission remains independently reviewable until the focused mirror is proven. | D-007, AC-009. |
| Observability | Validator diagnostics/evidence packs. | Diagnostics limited to stable missing facts, never semantic claims. | AD-003. |
| Rollout/rollback | Versioned bundle pin. | Roll back by bundle pin; preserve fixture/history. | impact §4. |
| Alternatives/trade-offs | Current soft/hard rule split. | Guidance-first accepts some review dependence to avoid brittle enforcement. | AD-002–003. |
| Unknowns | Fixture location/provenance and empirical mirror cost. | Resolve through bounded task and fixtures before release. | U-004, D-008, T-003. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Profile/mirror decision record, rules and guidance draft | human scope review | agreed minimal-core boundary | yes |
| 2 | Existing templates and Planner/Evaluator guidance | step 1 | task assurance contract, delta/envelope and risk distinction | yes |
| 3 | Fictional 006 derivative and rendered brief | step 2 | positive/negative examples and usability findings | yes |
| 4 | Focused validator fixtures/scripts, only approved mirrors | step 3 | enforceable stable invariants | yes |
| 5 | Docs, consumer guidance, scaffold and regression proof | step 4 | adoptable versioned package | yes via pin |

## 6. Contracts, data and compatibility

- **API/events:** no runtime API; artifact headings/IDs and optional brief
  metadata are the contracts.
- **Database/storage:** none; fixture evidence stays in repository.
- **External systems:** none required; consumers select local tooling.
- **Compatibility/migration:** new scaffolds start with `assurance_profile:
  unknown`; the planner must select a profile before Plan Ready. Historical/pinned
  v1/v2 sources remain valid without retroactive rewrite. Do not create a v3
  marker; a manually omitted new field is an explicit semantic-review gap until
  T-003 proves the focused mirror.

## 7. Security, privacy and permissions

- **Authentication/authorization:** no new permission model.
- **Secrets/PII:** fixtures use safe abstractions and sentinel scans where
  required; diagnostics do not repeat sensitive values.
- **Required permission:** human approval for implementation, waivers and A3
  responsibility remains explicit.
- **Destructive operations:** none expected.

## 8. Rollout, observability and rollback

- **Rollout:** versioned bundle release after compatibility fixtures pass;
  consumers opt in by pin update.
- **Success/failure signals:** fixture outcome, A1 usability, A2/A3 recovery of
  decision data, absence of unjustified hard mirrors.
- **Rollback trigger:** compatibility regression, ceremony regression or
  validator false-positive not safely remediable.
- **Exact rollback/checkpoint:** restore prior bundle pin/version; retain
  canonical sources and fixtures.

## 9. Brief coverage composition

At render time, cover all material sections in spec, impact, plan, tasks,
validation, decision log and state. The fictional fixture must visibly
distinguish its provenance from real 006 history. Material risk/task/assurance
ledgers may be progressively disclosed but not compressed into generic cards.

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| Q-001 | What are the approved profiles and escalation triggers? | stakeholder/Spec Guardian | D-004: A1/A2/A3 with A3 local-policy escalation. | no |
| Q-002 | Can v2 add conditional contract fields without a new lineage marker? | bundle maintainer | D-007: new scaffolds start `unknown`; historical/pinned sources remain compatible; prove with fixture. | no |
| Q-003 | Which exact fields deserve hard mirrors initially? | Evaluator | D-008: one profile/source-structure mirror with explicit necessity, cost and removal conditions. | no |
| Q-004 | Which docs are canonical theory vs operational guidance? | docs owner | Source map in T-004. | no |

## 11. Plan decision

**Plan Ready:** yes  
**Reviewer:** stakeholder-human / Codex acting as Orchestrator  
**Reviewed at:** 2026-08-20  
**Conditions/links:** D-003 authorizes implementation. T-001 is deliberately
the first bounded implementation decision: it must resolve Q-001–Q-003 before
any downstream template or validator change.
