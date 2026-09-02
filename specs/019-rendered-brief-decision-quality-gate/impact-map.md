# Impact Map: 019-rendered-brief-decision-quality-gate

**Status:** mapped — pending independent planning review  
**Mapped by:** Codex / platform engineering  
**Reviewed at:** pending  
**Overall risk:** high

## 1. Change boundary

Change the reusable bundle's post-render decision-quality protocol, evidence
shape, lifecycle guidance and mock-lab verification. Preserve the existing
v1/v2 structural, provenance, Pearson, accessibility and freshness contracts.
The change must not turn a visual preference, word count, DOM arrangement or
model score into a universal creation blocker.

## 2. Affected surfaces

| Surface | Files/modules/contracts | Direct/indirect | Expected change | Risk | Evidence/source |
|---|---|---|---|---|---|
| Author/reviewer guidance | `.harness/rules/human-visibility.md`, `.harness/agents/spec-guardian.md`, `.harness/skills/spec-review/SKILL.md` | direct | Five-lens, source-to-render protocol and materiality policy. | high | FR-001–005; rejected M001–M008. |
| Reusable skill | `.harness/skills/rendered-brief-decision-review/` | direct | Local serving/inspection and evidence template for independent roles. | medium | FR-001, FR-002, FR-007. |
| Lifecycle/state | `.harness/workflows/sdd-lifecycle.md`, templates `run-state.yaml`, `decision-log.md` | direct | Quality-ready assertion and unresolved-review blocking semantics. | high | FR-002, FR-006, FR-008. |
| Deterministic validator | `scripts/validate_human_visibility.py` and focused tests | direct | Verify only review-record fields, identities, dispositions and digest anchors. | high | FR-006; non-goals. |
| Fixtures and mock lab | `scripts/fixtures/semantic-brief-review/`, `testes/mock-tests/`, mock-lab skill | direct | Negative/positive calibration and 8×5 qualitative matrix. | high | AC-001, AC-002, AC-005. |
| UI/client | generated `stakeholder-brief.html` | indirect | Better source-backed presentation only where review finds material loss. | medium | FR-003–005. |
| Service/backend/data/API/auth/deploy | not_applicable | — | Bundle-level process only; no runtime product service is changed. | low | change boundary. |
| Tests/docs | Python tests, fixture README and source documentation | direct | Separate structural PASS from qualitative approval. | medium | validation plan. |

## 3. Dependency and evidence flow

```txt
functional request + canonical artifacts
  -> source-backed generated HTML served locally
  -> five independent role reviews with locators/digests
  -> review record + decision-log disposition
  -> deterministic state/evidence verifier
  -> Human Visibility / delivery claim
```

## 4. Compatibility and migration

- **Backward compatibility:** Existing structural validation and legacy v1
  exception paths remain unchanged. The new quality state is additive and only
  asserted for newly reviewed v2 delivery claims.
- **Data migration:** no consumer or persistent data migration; templates gain
  optional review fields with explicit defaults.
- **Rollout:** fixtures first, then validator guidance, then mock-lab execution.
  Existing historical briefs are never restyled merely to satisfy the protocol.
- **Rollback:** remove the new assertion/check and keep the earlier Human
  Visibility contract; evidence records remain useful documentation.

## 5. Regression risks and controls

| ID | Risk event | Trigger/early signal | Likelihood/impact | Preventive control | Contingency/owner | Validation ID |
|---|---|---|---|---|---|---|
| IR-001 | Qualitative gate becomes fixed UI checklist | Valid non-software or concise fixture rejected for missing tabs/diagram | medium/high | Materiality/N-A rationale and varied positive fixture | revise protocol; platform owner | V-003, V-006 |
| IR-002 | Review is self-approval or untraceable | Same identity/missing input digest in record | medium/high | deterministic identity/record check | block state; delivery owner | V-002 |
| IR-003 | Structural PASS is reported as quality approval | Summary lacks role matrix/disposition | high/high | separate statuses and mock-lab report template | reject report; evaluator | V-005 |
| IR-004 | Review leaks request/source content | evidence includes bodies/PII rather than locators | low/high | locator-only record and redaction rule | remove/redact; security owner | V-004 |
| IR-005 | Findings do not repair canonical source | HTML-only edit or absent re-review link | medium/high | required source recovery/action/re-review fields | return task to revision | V-002, V-005 |

## 6. Unknowns

| ID | Unknown | Why it matters | Resolution task/owner | Blocks implementation? |
|---|---|---|---|---|
| U-001 | Minimal stable YAML shape compatible with existing parser | Must not break consumers or introduce a heavy dependency. | T-002 / builder | no — use additive fields and focused fixture. |
| U-002 | How many mock sources require source enrichment vs render repair | The generator may be losing facts or upstream source may be weak. | T-004 / mock-lab reviewers | no — must be recorded by each finding. |

## 7. Recommended reviewers and checks

- **Specialist/human:** architect, system designer, executive, general
  stakeholder and delivery manager with role-specific independent review.
- **Automated:** focused fixture tests, full bundle validation, Human Visibility
  state/freshness validation and regression suite.
- **Manual:** serve selected HTML locally, keyboard/focus and responsive check;
  compare request → Markdown → rendered page.

## 8. Impact decision

**Impact mapped:** yes  
**Human review required:** yes — review quality cannot be inferred by parser.  
**Conditions before implementation:** independent plan review accepts the
adaptive protocol; all source artifacts, preliminary tasks and evidence mapping
are synchronized.
