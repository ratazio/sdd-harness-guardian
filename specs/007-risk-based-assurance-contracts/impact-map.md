# Impact Map: 007-risk-based-assurance-contracts

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex acting as Impact Mapper  
**Reviewed at:** 2026-08-20  
**Overall risk:** high

## 1. Change boundary

Evolve the Guardian's reusable specification-assurance contract. The work may
touch templates, rules, workflows, role/skill guidance, brief rendering,
validators, docs and fixtures. Consumer initiatives retain ownership of their
specifications, tools, evidence and regulatory obligations.

Preserve canonical Markdown/state/evidence ownership; Builder/Evaluator
separation; no implementation before readiness; v1/v2 compatibility; offline
vendor-neutral operation; and the boundary that structural checks never claim
semantic or safety approval.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Source templates | `spec.md`, `plan.md`, `tasks.md`, `validation-plan.md`, `evidence-pack.md`, `impact-map.md` | direct | Add proportionate fields within existing artifacts. | high | FR-001–009 |
| Brief contract | brief template/design/rule/validator | direct | Render delta, envelope, risks and task assurance without parallel truth. | high | FR-010, AC-007 |
| Rules/workflows | readiness, validation, evidence, visibility, lifecycle | direct | Profile, failure/waiver and escalation guidance. | high | FR-001, FR-009, FR-011 |
| Roles/skills | Planner, Guardian, Mapper, Builder, Evaluator | direct | Capability-based guidance; no permanent role by default. | medium | FR-006–008 |
| Validators | bundle/brief/readiness validators and fixtures | direct | Only minimal stable-field mirrors and negative cases. | high | FR-011–012, AC-008 |
| Theory docs | references, operating model and focused guidance | direct | Explain adopted references and non-certifying scope. | medium | FR-013 |
| Existing initiatives | 006 original plus fictional derivative fixture | indirect | Preserve history; use derivative to prove method. | medium | FR-014 |
| Consumer projects | install/enforcement/prompts | indirect | Explain profiles, local policy and adoption. | high | AC-009 |

## 3. Dependency and data flow

```txt
source facts + impact/risk + architecture baseline
  -> profile and assurance choices by Planner/Guardian
  -> existing plan/tasks/validation/evidence artifacts
  -> independent evaluation + conditional specialist/human review
  -> derived brief and minimum deterministic checks
  -> failure/revision or accountable waiver
  -> task done only after approved evidence
```

## 4. Compatibility and migration

- Historical 006 remains immutable evidence; only a clearly labelled fictional
  derivative becomes a positive fixture.
- Existing v1/v2 validator paths remain accepted.
- New fields need an explicit adoption boundary; upgrading the bundle must not
  silently fail old consumer initiatives.
- Start soft/optional wherever safe; promote only recurring critical omissions
  after negative-fixture and maintenance-cost review.

## 5. Regression risks

| ID | Risk | Trigger/surface | Mitigation | Validation ID |
|---|---|---|---|---|
| IR-001 | Ceremony increases for simple work. | Profile/template prompts. | Concise A1 fixture and human usability review. | V-001, V-008 |
| IR-002 | Validator overreaches into semantic judgment. | New hard mirrors. | Minimal-core register and stable negative tests. | V-006, V-008 |
| IR-003 | Brief hides material risks/tasks. | Lossy rendering. | Fictional 006 comparison and cross-role review. | V-002, V-007 |
| IR-004 | Compatibility breaks pinned consumers. | Mandatory field/lineage change. | v1/v2 fixtures and adoption boundary. | V-009 |
| IR-005 | Waiver silently authorizes unsafe work. | State/evidence changes. | Human-accountability and expiry fixture. | V-006 |
| IR-006 | Wording implies sectoral compliance. | Docs/prompts. | Specialist review and prohibited-claim checks. | V-010 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Exact profile names/triggers and whether critical is a bundle profile or local-policy escalation. | Controls complexity and claims. | Resolved by D-004. | no |
| U-002 | Whether v2 can carry conditional assurance fields without a new marker. | Compatibility and validator design. | Resolved by D-007; prove in T-003 fixture. | no |
| U-003 | Minimum machine-checkable fields that earn a hard mirror. | Prevents deterministic bloat. | Resolved by D-008; test in T-003. | no |
| U-004 | Fictional fixture location/provenance label. | Keeps 006 trustworthy. | T-002; State Keeper. | no |

## 7. Recommended reviewers and checks

- **Specialist/human:** architect; QA/test strategist; security-aware and
  accessibility reviewer; domain authority for critical fixtures.
- **Automated:** bundle/scaffolder/consumer regression plus focused positive/
  negative fixtures; no semantic auto-approval.
- **Manual:** cross-role judgement that A1 is concise while A2/A3 are complete,
  readable and honest.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes  
**Approval/evidence:** D-003 grants implementation authority in dependency
order; baseline tag is `v0.3.0`.  
**Conditions before implementation:** T-001 must resolve U-001–U-003 before
downstream template, validator or consumer changes; Builder/Evaluator remain
distinct identities.
