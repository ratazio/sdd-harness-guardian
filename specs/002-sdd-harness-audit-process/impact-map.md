# Impact Map: 002-sdd-harness-audit-process

**Status:** reviewed  
**Spec:** ./spec.md  
**Mapped by:** codex / Impact Mapper role  
**Reviewed at:** 2026-07-25  
**Overall risk:** medium

## 1. Change boundary

This changes the Guardian bundle's process surface: agents, rules, workflows,
skills, templates, docs, manifest and validator. It does not change consumer
product code or implement a hosted audit runtime.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| UI/client | not_applicable | none | no app UI | low | spec NG-001 |
| Service/backend | not_applicable | none | no service runtime | low | architecture boundary |
| Data/storage | docs/memory only | direct | stable audit principles recorded | low | docs/harness-audit-framework.md |
| Public/API contract | manifest.yaml | direct | audit artifacts registered | medium | validator |
| Auth/security/privacy | audit-policy, skill | direct | audit checks least privilege and hard mirrors | medium | rule/skill review |
| Build/deploy/infra | validate_bundle.py | direct | validation includes audit framework | low | V-004 |
| Observability/support | audit report template | direct | standard report supports gaps and roadmap | low | template review |
| Tests/docs | docs, README, AGENTS, workflow, skill | direct | audit process documented and discoverable | medium | V-001/V-002 |

## 3. Dependency and data flow

```txt
provided HTMLs -> docs/harness-audit-framework.md -> sdd-harness-audit skill
entrypoint/manifest -> workflow/agents/rules/templates -> audit-report.html
```

## 4. Compatibility and migration

- Backward compatibility: additive capability; existing workflows remain valid.
- Data migration: none.
- Rollout/feature flag: consumers receive this when they upgrade the bundle.
- Rollback implications: remove added audit artifacts and manifest entries.

## 5. Regression risks

| ID | Risk | Trigger/surface | Mitigation | Validation ID |
|---|---|---|---|---|
| IR-001 | Manifest references missing audit files | manifest edit | bundle validator | V-001/V-004 |
| IR-002 | Audit skill becomes unregistered or unreachable | entrypoint/manifest | AGENTS + manifest wiring | V-001 |
| IR-003 | Report template is too thin to guide consistent output | template | required report sections | V-003 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Whether future consumers need a deterministic graph parser. | Could improve hard mirror coverage. | Future initiative after audits are used. | no |

## 7. Recommended reviewers and checks

- Specialist/human: independent Evaluator Agent for process coherence.
- Unit/integration/contract/E2E: bundle validator and scaffolder smoke.
- Manual/operational: inspect audit skill, workflow and report template.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** no for additive bundle docs/process; yes before
release if policy requires independent evaluation.  
**Approval/evidence:** evidence/T-001.md  
**Conditions before implementation:** spec, plan and validation recorded.
