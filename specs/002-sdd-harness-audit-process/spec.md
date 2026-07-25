# Spec: 002-sdd-harness-audit-process

**Status:** spec_ready  
**Sequence:** 002  
**Slug:** sdd-harness-audit-process  
**Owner:** platform-engineering  
**Created:** 2026-07-25  
**Last updated:** 2026-07-25  
**Risk:** medium

## 1. Problem

The SDD Harness Guardian can govern delivery, but it lacks a first-class audit
process that judges whether a consumer repository actually has a usable SDD and
Harness Engineering structure. Without this, teams can accumulate process files
that are not reachable, not referenced, not enforceable or not sufficient for
agents to execute safely.

## 2. Objective

Make the bundle able to guide a deep SDD/harness audit that produces a stable
HTML report with graph reachability, evidence-backed findings and remediation.

## 3. Delivery outcome

- Product/user outcome: maintainers can ask for an audit and receive a
  rigorous, repeatable assessment of SDD/harness maturity.
- Demonstrable increment: new audit skill, agents, rule, workflow, HTML
  template, structured knowledge framework and manifest wiring.
- MVP/slice boundary: define the audit process and report contract; do not
  implement a fully deterministic graph parser.
- Priority source: human request

The harness validates that these are declared. It does not decide commercial
value or product priority.

Summarize these fields for human review in `stakeholder-brief.html`.

## 4. Users or actors

- Actor: repository maintainer requesting an audit.
- Actor: Harness Auditor synthesizing specialist findings.
- Actor: Harness Graph Mapper building reachability evidence.
- Actor: Evaluator Agent reviewing the audit report before closure.

## 5. Observable outcomes

- O-001: the bundle exposes a discoverable audit workflow and skill.
- O-002: the audit requires graph reachability analysis and artifact usefulness
  review.
- O-003: the report format is stable HTML with evidence, severity and roadmap.
- O-004: provided company knowledge is distilled into a structured local
  framework without copying live project knowledge into a skill.

## 6. Non-goals

- NG-001: build a hosted audit application.
- NG-002: replace agentic judgment with a fully scripted report generator.
- NG-003: mutate consumer repositories during audit.
- NG-004: store consumer-specific living knowledge inside the vendored bundle.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-001 | WHEN an audit is requested, THE BUNDLE SHALL provide a skill with triggers, boundaries, workflow, graph method, output contract and validation checklist. | Makes the audit repeatable across agents. |
| FR-002 | WHEN the audit workflow runs, THE BUNDLE SHALL require inventory and graph classification of harness artifacts. | Distinguishes operational files from decorative files. |
| FR-003 | WHEN audit findings are reported, THE BUNDLE SHALL require severity, evidence, impact and remediation. | Prevents vague critique. |
| FR-004 | WHEN a report is produced, THE BUNDLE SHALL provide a stable HTML structure. | Keeps outputs consistent while allowing agentic judgment. |
| FR-005 | WHEN source knowledge is internalized, THE BUNDLE SHALL store stable principles in docs/memory and keep live consumer knowledge external. | Preserves progressive disclosure and knowledge separation. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-001 | `manifest.yaml` registers the audit skill, agents, workflow, rule and HTML report template. | V-001 |
| AC-002 | `.harness/skills/sdd-harness-audit/SKILL.md` defines the complete audit procedure and validation checklist. | V-002 |
| AC-003 | `.harness/workflows/sdd-harness-audit.md` defines audit phases, roles, severity and output. | V-002 |
| AC-004 | `.harness/templates/audit-report.html` contains the stable report sections. | V-003 |
| AC-005 | `docs/harness-audit-framework.md` captures the structured baseline from the provided HTML knowledge sources. | V-002 |
| AC-006 | Bundle validation and scaffolder smoke tests pass after the change. | V-004 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-001 | Consumer has orphaned harness files. | Audit reports them as orphaned/weak instead of treating them as maturity. |
| EC-002 | Consumer lacks deterministic checks. | Audit reports missing hard mirrors by severity. |
| EC-003 | HTML source knowledge conflicts with local rules. | Safety and bundle invariants win; conflict is reported. |
| EC-004 | Audit target is unavailable. | Audit blocks or marks assumptions instead of fabricating findings. |

## 10. Constraints and non-functional requirements

- Architecture: keep the bundle passive and vendor-neutral.
- Security/privacy: do not copy private consumer knowledge into the bundle.
- Data: provided HTMLs inform stable audit principles only.
- Performance/reliability: audit starts from indexes/state and retrieves detail
  on demand.
- Compatibility/accessibility: HTML report is static and readable without a
  runtime.
- Operational: scripts may assist inventory, but not replace audit judgment.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| The provided HTMLs are approved internal knowledge inputs. | Human supplied them in the request. |
| Independent evaluation may occur after this builder pass. | State/evidence must keep the task at `needs_evaluation` until reviewed. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-001 | Audit becomes checklist theater. | medium | high | Require graph, evidence and remediation per finding. |
| R-002 | Skill becomes a knowledge dump. | low | medium | Store distilled baseline in docs and keep skill procedural. |
| R-003 | Report is generated mechanically. | medium | medium | Template permits structure, but skill requires agentic judgment. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| Provided HTML knowledge sources | available | human | no |
| Existing Guardian manifest and validator | available | platform-engineering | no |

## 14. Validation notes

`validation-plan.md` maps acceptance criteria to structural review and commands.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes  
**Reviewer:** codex / Spec Guardian role  
**Reviewed at:** 2026-07-25  
**Blocking issues:** none  
**Required revisions:** none  
**Decision evidence/link:** this spec defines outcome, scope, ACs, risks and validation paths.
