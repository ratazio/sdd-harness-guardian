# Impact Map: 018-derived-brief-completeness-and-delivery-integrity

**Status:** reviewed  
**Mapped by:** root (builder)  
**Overall risk:** medium

## 1. Change boundary

Change only the Guardian bundle's scaffold, source-to-brief validation,
workflow state and regression fixtures. Preserve Markdown as canonical source,
the v2 evidence gates, Pearson opt-in/local-asset policy, and a consumer's
freedom to use any domain-specific information architecture.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| UI/client | `.harness/templates/stakeholder-brief.html` | direct | Honest scaffold state; no generic delivery appearance. | medium | FR-001, V-001 |
| Service/backend | not_applicable — no service runtime | direct | None. | low | plan §4 |
| Data/storage | Initiative source Markdown + `run-state.yaml` | direct | Additive lifecycle/coverage records. | medium | FR-005 |
| Public/API contract | Validator CLI diagnostics/exit status | direct | Additive failure categories. | medium | FR-001–004 |
| Auth/security/privacy | Validator output and local asset rules | indirect | Avoid source-body leakage/network assets. | medium | V-003 |
| Build/deploy/infra | `scripts/new_initiative.py`, test commands | direct | Scaffolds visibly incomplete, not deliverable. | medium | V-001 |
| Observability/support | progress, evidence, decision log, handoff | direct | Recoverable state and reviewer outcome. | low | FR-005 |
| Tests/docs | fixtures, rules/workflow, mock lab guidance | direct | Positive/negative flexible regression matrix. | medium | V-002–004 |

## 3. Dependency and data flow

```txt
new_initiative.py -> source artifacts + lifecycle state -> template shell (today)
  -> compositor/refresh path defined in T-002 -> rendered HTML
  -> human-visibility / bundle validators -> gate state -> delivery link (HTML)
                         ^                         |
                     fixtures + mock suite --------+
```

## 4. Compatibility and migration

- **Backward compatibility:** historical/pinned v1 briefs remain readable;
  v2-only enforcement applies after material regeneration or explicit
  migration.
- **Data migration:** no source rewrite; add fields with defaults that make a
  scaffold visibly `scaffolded`.
- **Rollout:** ship script/template/validator/tests atomically in the bundle.
- **Rollback:** revert that coherent patch; retain prior consumer files and
  diagnostic evidence.

## 5. Regression risks and controls

| ID | Risk event | Trigger/early signal | Likelihood/impact | Preventive control | Contingency/owner | Validation ID |
|---|---|---|---|---|---|---|
| IR-018-01 | A generic scaffold crosses a delivery gate. | Template prose or missing provenance accepted. | medium/high | Negative fixture + fail-closed v2 state rule. | Revert gate and fix fixture; maintainer. | V-001,V-003 |
| IR-018-02 | A deterministic check imposes a software/layout shape. | Valid mock domain fails for missing tabs/tech fields. | medium/high | Category/owned-unknown contract; eight-domain suite. | Relax only unjustified rule; maintainer. | V-002,V-004 |
| IR-018-03 | Valid older brief is blocked unexpectedly. | v1/pinned package fails new rule. | medium/medium | Lineage/material-refresh branch fixture. | Record migration decision; maintainer. | V-REG-002 |
| IR-018-04 | Brief leaks source fixture content or makes network request. | Diagnostic prints body or browser requests external asset. | low/high | Sanitised diagnostic test and local-browser request check. | Remove leakage/hotlink; maintainer. | V-003,V-REG-003 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-018-01 | Actual permissive path(s) in current validators. | A partial fix could leave the bypass open. | T-001 builder | yes |
| U-018-02 | Minimal domain-neutral category inference. | Overreach would make Guardian brittle. | T-002 builder | yes |

## 7. Recommended reviewers and checks

- **Independent evaluator:** inspect source/HTML trace, fixtures and whether
  the implementation accidentally fixes layout/domain details.
- **Deterministic:** unit/CLI negative+positive fixtures, full bundle suite,
  fresh mock suite.
- **Manual:** local-server rendered HTML review at desktop and narrow viewport;
  keyboard/no-script/print where a brief is materially changed.

## 8. Impact decision

**Impact mapped:** approved  
**Human review required:** no; independent evaluator required  
**Conditions before implementation:** D-018-03 accepted; preserve flexible
coverage semantics while T-001 reproduces the bypass.
