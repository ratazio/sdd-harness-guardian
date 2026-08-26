# Impact Map: 008-semantic-brief-review-calibration

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** Codex / Impact Mapper  
**Reviewed at:** 2026-08-25  
**Overall risk:** medium

## 1. Change boundary

The change calibrates the existing human/agent review path for v2 stakeholder briefs. It may change review instructions, lifecycle wording, the review-report template and static examples/fixtures. It must not turn prose quality into a numeric score, semantic parser, permanent service, new workflow engine or a compatibility-breaking v1 requirement.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Review guidance | `.harness/skills/spec-review/SKILL.md`, `.harness/agents/spec-guardian.md` | direct | Add three qualitative lenses and source → lost fact → recovery-action findings. | medium | FR-001, FR-002 |
| Lifecycle | `.harness/workflows/sdd-lifecycle.md` and feature/bugfix/refactor paths | direct | Name pre-render coverage separately from post-render decision-loss review. | medium | FR-003, FR-004 |
| Brief template | `.harness/templates/stakeholder-brief-design.md`, optional review wording | direct | Make review of decision loss and N/A rationale discoverable; preserve current shell. | medium | FR-004, FR-007 |
| Examples/fixtures | `scripts/fixtures/` and relevant tests | direct | Add one software and one non-software calibration case plus a shallow negative case. | medium | FR-005, AC-002–004 |
| Deterministic validator | `scripts/validate_human_visibility.py` | indirect | Retain structural/provenance role; at most check a review-record locator if proven necessary. | high | FR-006, FR-007 |
| Public/API contract | none | not_applicable | The bundle exposes no runtime API. | low | source boundary |
| Auth/security/privacy | none | not_applicable | Static fictional examples must contain no credentials, PII or sensitive topology. | low | plan §7 |
| Build/deploy/infra | none | not_applicable | No service, deployment, database or infrastructure change is in scope. | low | spec §3/§5 |
| Observability/support | reviewer report and fixture output | indirect | Use explicit findings and review records as the support/debug surface. | low | FR-002 |
| Tests/docs | docs, fixture tests and bundle validation | direct | Prove calibration examples and the absence of semantic scoring. | medium | validation plan |

## 3. Dependency and information flow

```txt
canonical MD sources
  -> author composition and pre-render coverage review
  -> rendered stakeholder brief
  -> distinct post-render decision-loss review
  -> decision log / corrective source edits
  -> refreshed brief and existing structural validator
```

Text equivalent: the author never makes the brief a source of truth. The reviewer traces a weak or omitted decision back to its Markdown source, asks for a correction there, and the brief is rendered again from the correction.

## 4. Compatibility and migration

- **Backward compatibility:** v1 historical briefs retain their lineage; they are not forced into v2 review lenses until a material refresh/migration.
- **Data migration:** none; examples are static files and existing decision logs remain append-only.
- **Rollout/feature flag:** ship guidance and fixtures in the bundle; users adopt them on new v2 or materially refreshed initiatives.
- **Rollback implications:** revert the changed guidance/template/fixtures as one bounded change; no stored data, task state or consumer initiative is transformed.

## 5. Regression risks and controls

| ID | Risk event | Trigger/early signal | Likelihood/impact | Preventive control | Contingency/owner | Validation ID |
|---|---|---|---|---|---|---|
| IR-001 | Qualitative lenses become an overfit checklist for a single software example. | Review output forces irrelevant API/architecture language on non-software work. | medium / high | Require justified N/A and paired software/non-software fixtures. | Revise wording and fixture before merge; Spec Guardian. | V-004, E-002 |
| IR-002 | Structural pass is misreported as semantic approval. | A brief has attributes/gates but cannot answer a material meeting decision. | medium / high | Separate pre-render coverage and post-render decision-loss review records. | Block Human Visibility and require source correction; Orchestrator. | V-002, M-001 |
| IR-003 | A semantic parser or score is added “for consistency.” | New thresholds, word counts or accept/reject scoring appear in diff. | low / high | FR-006/007 and explicit negative diff review. | Reject change; human approval required for any future mirror. | V-005 |
| IR-004 | Review becomes vague and non-actionable. | Finding lacks source, lost fact or recovery action. | medium / medium | Finding template is source → fact → action. | Return review for revision; reviewer. | V-001 |
| IR-005 | v1 consumers are accidentally gated by v2 rules. | Legacy fixture fails without material refresh. | low / high | Keep lineage branch and execute v1 compatibility fixture. | Restore legacy behavior; maintainer. | V-006 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Whether an existing review-report template is sufficient or needs a compact new section. | A duplicate template would add process cost. | T-001 / planner; inspect existing assets first. | no |
| U-002 | Whether a locator-only deterministic check adds value beyond existing state validation. | An unnecessary mirror would violate minimalism. | T-003 / maintainer; compare fixture failure modes. | no |
| U-003 | Whether the reference fixtures can reuse current helper tests. | A new harness should not be created for two static examples. | T-002 / builder. | no |

## 7. Recommended reviewers and checks

- **Specialist/human:** a distinct Spec Guardian/reviewer for semantic and rendered-meaning review; human only for a future hard mirror decision.
- **Unit/integration/contract/E2E:** focused fixture tests plus `python scripts/validate_bundle.py`.
- **Manual/operational:** 60-second read of each reference brief, including the question: “what material decision cannot be made without reopening Markdown?”

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes — only to approve a future deterministic mirror or a policy-level scope expansion.  
**Approval/evidence:** user-approved direction recorded in D-001; reviewer evidence is required before Human Visibility.  
**Conditions before implementation:** preserve v1 lineage; no semantic score/parser; keep review identity distinct; tasks remain drafts until meeting propagation.
