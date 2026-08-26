# Spec: 007-risk-based-assurance-contracts

**Status:** spec_ready  
**Sequence:** 007  
**Slug:** risk-based-assurance-contracts  
**Owner:** platform-engineering  
**Created:** 2026-08-20  
**Last updated:** 2026-08-20  
**Risk:** high

## 1. Problem

The Guardian is a reusable SDD governance bundle used by agents in consumer
repositories. It protects outcome linkage, traceability, independent evaluation
and task evidence; initiative 006 added source coverage, architecture
proportionality and a stakeholder decision surface.

For complex, high-impact or vital work, its contracts still do not make the
implementation commitment and assurance strategy inspectable per task: what
changes from the current architecture, what complexity is accepted, which
quality/risk claim is proved, which test technique/oracle/environment applies,
who is accountable, what evidence suffices and what happens after failure.

The 006 reference brief demonstrates the gap. Its plan has a current/target
architecture matrix and its sources have risk registers, but the rendered
architecture mostly presents a target flow, impact/risk summarizes controls
rather than a risk ledger, three tasks are collapsed, and validation omits the
full task-level assurance contract. Structural coverage detects missing source
links; it cannot safely infer that a synthesis retained every material decision.

The remedy must not make the Guardian a heavyweight deterministic workflow
engine or an unbounded checklist. Consumer projects vary by domain, stack,
regulation and risk. Agent/skill guidance and independent human/agent judgment
should perform semantic selection and review; deterministic checks remain a
minimal core for unambiguous missing structure, invalid states, absent
traceability and unsafe closure.

## 2. Objective

Enable consumer-project agents to construct proportionate, risk-based
assurance contracts inside existing SDD artifacts, so stakeholders approve the
architecture and validation commitment before implementation without unnecessary
process or technology complexity.

## 3. Delivery outcome

- **Product/user outcome:** stakeholder, architect, builder, evaluator and
  specialist see what changes, why its risk warrants assurance, how each claim
  is proved and whether residual risk was accepted.
- **Demonstrable increment:** templates, rules, workflows, role/skill guidance,
  validator boundaries, docs and fixtures support assurance profiles and
  task-level contracts; a fictional 006 derivative demonstrates the result
  without changing historical evidence.
- **MVP/slice boundary:** evolve existing `spec.md`, `impact-map.md`, `plan.md`,
  `tasks.md`, `validation-plan.md`, evidence and derived brief. Do not add a
  workflow service, database, generic test framework, mandatory new agent,
  mandatory sidecar artifact or universal brief lineage without a proven need.
- **Priority source:** explicit human direction on 2026-08-20 to increase
  proof quality while avoiding deterministic process bloat. Execution requires
  a subsequent explicit approval of the planned package.

## 4. Users or actors

- Product/business stakeholder accepting value, scope and residual business risk.
- Architect accepting architecture delta, trade-offs and complexity envelope.
- Harness Planner selecting risk-proportionate validation.
- Builder, Evaluator and conditional security/data/accessibility/performance/
  operations/domain-safety specialist.
- Named accountable human for waivers and regulated/safety-critical work.
- Consumer-project agent asking the Guardian for specification help.

## 5. Observable outcomes

- **O-001:** every new initiative declares an assurance profile and rationale;
  the profile controls depth, not an artificial effort estimate.
- **O-002:** M/L, high-risk or unknown work records source-backed as-is, target,
  architecture delta and complexity/change envelope before Plan Ready.
- **O-003:** impact, risk and controls stay distinct. Material risks expose
  trigger, impact, mitigation, contingency, owner and validation link.
- **O-004:** every material task carries an assurance contract: claim/risk,
  selected technique/rationale, oracle, environment/data, executor/evaluator/
  specialist, evidence, entry/exit criteria and failure/exception path.
- **O-005:** test selection is risk-based; no fixed coverage percentage,
  Gherkin, mutation test, screenshot or LLM evaluation is imposed when unfit.
- **O-006:** a UI change has a visual/interaction decision; when visual proof
  is needed, screenshots pair with trace, test report or documented manual
  steps so appearance is not confused with behavior.
- **O-007:** existing skills and roles perform most reasoning; hard mirrors are
  limited to protected, clearly decidable invariants and never claim semantic,
  safety or regulatory certification.
- **O-008:** blocking failure leads to revision or block. A waiver has a named
  human, reason, residual risk, compensating control and expiry/review trigger.
- **O-009:** the brief exposes current/target/delta, change envelope, top risks,
  individual task assurance and planned/executed/proved/waived/uncertain state.
- **O-010:** historical and pinned v1/v2 artifacts remain usable through an
  explicit, version-aware adoption path.

## 6. Non-goals

- **NG-001:** certify ISO, IEC, NIST, OWASP or sectoral safety compliance, or
  use agent evaluation in place of a regulated human authority.
- **NG-002:** require every task to run every test type, meet universal code
  coverage, use BDD/Gherkin, mutation testing, screenshots or a named tool.
- **NG-003:** add hosted test management, database, workflow engine, remote
  service, result warehouse or persistent agent fleet.
- **NG-004:** auto-judge semantic adequacy, visual quality, risk completeness
  or human acceptance from metadata.
- **NG-005:** add permanent roles when current roles plus conditional specialist
  capability suffice.
- **NG-006:** rewrite historical 006 facts; a labelled fictional derivative is
  permitted as a fixture.
- **NG-007:** expose secrets, production topology, PII or sensitive safety data.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | THE method SHALL define proportionate assurance profiles with escalation triggers and source-backed rationale. | Depth follows risk, not ceremony. |
| FR-002 | THE profile mechanism SHALL reuse existing canonical artifacts by default and avoid a required sidecar or lifecycle service. | Keep the bundle portable and small. |
| FR-003 | FOR applicable M/L, high or unknown work, THE plan SHALL record as-is, target, architecture delta, sources/confidence, unknowns and a change/complexity envelope. | Stakeholders approve the actual commitment. |
| FR-004 | THE envelope SHALL cover applicable modules, APIs/events/contracts, data/migrations, trust boundaries, dependencies, operations, agentic/process surfaces and a re-approval trigger. Code counts are optional indicators, not architecture itself. | Prevent hidden layer growth. |
| FR-005 | THE method SHALL distinguish impact map, risk register and controls. A material risk SHALL identify event, trigger, likelihood, impact, early signal where known, mitigation, contingency/rollback, owner and validation link. | Controls alone do not reveal risk. |
| FR-006 | EACH material task SHALL declare a proportionate assurance contract linking objective/AC/risk to method/level/technique, oracle, environment/data, executor, independent evaluator, conditional specialist, evidence, entry/exit criteria and failure/exception handling. | Generic validation IDs are insufficient proof planning. |
| FR-007 | Harness Planner guidance SHALL select static, unit/property/mutation, integration/contract, E2E/BDD, visual/accessibility, migration/recovery, security and operational checks only when risk and changed surface justify them. | Test technique is a decision. |
| FR-008 | THE method SHALL require a visual assurance decision for user-facing change and distinguish visual appearance from interaction/correct behavior. | A screenshot alone does not prove a flow. |
| FR-009 | A blocking validation failure SHALL prevent `done`; an exception SHALL be explicit, risk-linked, human-accountable and time-bounded where appropriate. | Failed tests cannot silently become proof. |
| FR-010 | THE brief SHALL progressively disclose architecture delta, envelope, material risk ledger, individual task assurance and proof states. | Human review must recover commitments. |
| FR-011 | Skills/roles SHALL own semantic selection and review. Deterministic mirrors SHALL be restricted to profile presence, cross-links, identity/state separation, failure/waiver structure and unambiguous completeness. | Avoid a deterministic labyrinth. |
| FR-012 | Every new mirror SHALL document failure class, why review alone is insufficient, maintenance/false-positive cost, failure behavior and deletion/downgrade condition. | Hard enforcement must earn its cost. |
| FR-013 | Theory docs SHALL explain the non-certifying relationship to ISO/IEC/IEEE 29148 and 29119, ISO/IEC 25010, ATAM/QAW, arc42/ADR, NIST SSDF and OWASP ASVS. | Give consumer agents grounded reasoning. |
| FR-014 | The implementation SHALL include fictional positive/negative fixtures derived from 006, compatibility fixtures and independent proportionate-process evaluation. | Test the method without rewriting history. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | A high-risk fixture expresses profile, as-is/target/delta and envelope within existing artifact classes. | V-001 |
| AC-002 | A reviewer distinguishes impact, risk and control and recovers material risk fields from sources and brief. | V-002 |
| AC-003 | Every material fixture task has a traceable assurance contract; an incomplete one blocks through the defined review. | V-003 |
| AC-004 | Technique selection demonstrates required and deliberately inapplicable checks with rationale; no universal test mandate is introduced. | V-004 |
| AC-005 | A visual fixture requires behavior and visual evidence separately; a non-UI fixture acquires no UI overhead. | V-005 |
| AC-006 | Failure and waiver fixtures preserve state/evaluator separation; missing accountable waiver data blocks closure. | V-006 |
| AC-007 | The brief exposes individual task assurance, delta, envelope and risk ledger without claiming structural semantic proof. | V-007 |
| AC-008 | Any hard mirror has a minimal-core justification and precise negative fixture; rejected mirrors remain guidance. | V-008 |
| AC-009 | Historical/pinned fixture behavior remains compatible under a documented adoption path. | V-009 |
| AC-010 | Theory docs accurately position market references without compliance claims. | V-010 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Small/local reversible change | A1 remains concise; source-backed N/A replaces empty bureaucracy. |
| EC-002 | High risk but unknown baseline | Block Plan Ready or create bounded discovery; never fabricate architecture. |
| EC-003 | Tool, environment or specialist unavailable | Record the gap, risk effect and human decision; do not silently lower profile. |
| EC-004 | Check fails | Record finding, move to `needs_revision` or `blocked`, and repeat relevant checks after correction. |
| EC-005 | Waiver proposed | Require accountable human, residual risk, compensating control, scope and expiry/review trigger. |
| EC-006 | Regulated/safety-critical domain | Escalate to applicable local/sectoral standard and human authority; Guardian claims no certification. |
| EC-007 | Dense brief harms readability | Preserve executive path and progressive disclosure; material ledger cannot become generic summary. |

## 10. Constraints and non-functional requirements

- **Architecture:** passive portable bundle; canonical artifacts remain
  consumer-owned; brief is derived.
- **Security/privacy:** minimum-safe abstraction/redaction; no sensitive output
  in diagnostics or fixtures.
- **Data:** no database or remote telemetry.
- **Performance/reliability:** validators stay fast, local and limited to stable
  facts; semantic review is not simulated in CI.
- **Compatibility/accessibility:** preserve v1/v2 reading paths; progressive
  disclosure remains keyboard, no-script and print accessible.
- **Operational:** consumers choose tools; bundle records capability/evidence,
  not vendor lock-in.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| Existing artifacts can carry assurance without a database. | T-001 architecture/compatibility review. |
| Existing roles plus conditional specialists suffice. | T-001 role review. |
| 006 can be fictionalized without obscuring historical evidence. | T-002 provenance review. |
| A minimal mirror set catches unsafe closure without semantic pretense. | T-003 negative fixtures/evaluation. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Assurance becomes mandatory checklist bureaucracy. | medium | high | Profiles, N/A rationale and concise A1 fixture; Orchestrator. |
| R-002 | New deterministic validation is brittle or duplicates judgment. | medium | high | Minimal-core test and downgrade/delete condition; bundle maintainer. |
| R-003 | Guidance varies too much and omissions pass review. | medium | high | Independent evaluation, examples and ratchet; Spec Guardian. |
| R-004 | Fictional 006 is mistaken for historical fact. | low | medium | Clear label and original untouched; State Keeper. |
| R-005 | “Critical” implies regulatory assurance. | medium | high | Explicit non-goal, standard escalation and human authority; Spec Guardian. |
| R-006 | Dense brief hurts readability/accessibility. | medium | medium | Progressive disclosure and cross-role render review; design reviewer. |
| R-007 | Evidence exposes sensitive architecture/data. | low | high | Redaction review; security reviewer. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Human approval of profile taxonomy and implementation package | pending | stakeholder | yes |
| v2 brief/validator compatibility analysis | pending | bundle maintainer | yes before enforcement |
| Distinct Builder/Evaluator for execution | pending | Delivery Orchestrator | yes before task ready |
| Specialist availability policy for high/critical work | pending | stakeholder | yes before release |

## 14. Validation notes

`validation-plan.md` is authoritative. It must prove proportionality and safe
failure behavior, not merely field presence. Deterministic checks only cover
stable facts and explicitly disclaim semantic approval.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** stakeholder-human / Codex acting as Spec Guardian  
**Reviewed at:** 2026-08-20  
**Blocking issues:** none for implementation; T-001 resolves the detailed
profile, compatibility and mirror-boundary decisions before downstream work.  
**Required revisions:** none before T-001.  
**Decision evidence/link:** decision-log.md#D-003
