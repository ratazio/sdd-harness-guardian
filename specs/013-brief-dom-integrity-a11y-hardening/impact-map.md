# Impact Map: 013-brief-dom-integrity-a11y-hardening

**Status:** mapped — independent plan review still pending · **Overall risk:** medium

## Change footprint

| Surface | Change | Why it is affected | Guardrail |
|---|---|---|---|
| Local validator | `scripts/validate_human_visibility.py` gains rendered-ID, post-document and conditional-tab checks. | Observed false passes occur in this deterministic gate. | No browser execution; bounded reports. |
| Parser model | `BriefParser` records rendered/inert state and document closure facts. | Checks need structural facts rather than broad source regex. | Inert-subtree/comment controls. |
| Focused Python suite | `scripts/test_validate_human_visibility.py` gains negative/compatibility fixtures. | Each acceptance rule needs reproducible oracle. | v1, non-tab v2 and canonical tabbed controls. |
| Existing v2 template/briefs | Indirect compatibility target only. | Their DOM/static handler remains reference. | No template change in scope. |
| Guidance/evidence/baselines | Record contract, diagnostics and release proof. | Future maintainers need recoverable boundary. | Baseline refresh only after evaluator approval. |
| APIs/storage/client identity | not_applicable. | No application, persistence, service or asset/profile change. | Explicit exclusion. |

```text
local v2 brief
   ├─ rendered DOM facts ──> duplicate/tail contract ──> bounded report
   └─ declared tablist ────> static tab contract ──────> bounded report
v1 or v2 without tabs ─────────────────────────────────> compatibility pass
```

## Risks and controls

| ID | Risk | Consequence | Signal/control | Validation | Owner |
|---|---|---|---|---|---|
| IR-001 | Inert text/comments read as rendered defects. | False failure. | Parser probe and inert/comment controls. | V-001/V-002 | T-001/T-002 + evaluator |
| IR-002 | Valid v1/non-tab v2 subject to tab checks. | Compatibility regression. | Activate only on declared v2 tablist. | V-004 | T-003 + evaluator |
| IR-003 | Static check accepts click-only/miswired tabs. | Keyboard defect passes. | Reciprocal ARIA/roving state + handler fixtures. | V-003 | T-003 + evaluator |
| IR-004 | Failure output contains payload. | Log disclosure. | Rule/ID-only diagnostics + redaction assertion. | V-005 | T-004 + evaluator |
| IR-005 | Change drifts from fallback/print behaviour. | Access regression. | Canonical tab control and human review. | V-003/V-004 | T-004 evaluator |

## Dependency and rollback map

| Dependency | Required before | If it fails | Recovery |
|---|---|---|---|
| T-001 contract | T-002/T-003 | Brittle/undefined oracle. | Revise boundary; no heuristic patch. |
| T-002 DOM check | T-004 | Integrity gap remains. | Return to T-002. |
| T-003 tab check | T-004 | A11y contract incomplete. | Return to T-003. |
| Distinct evaluation | `done`/baseline | False confidence. | Keep `needs_evaluation`; no baseline promotion. |
