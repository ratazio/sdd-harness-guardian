# Technical Plan: 013-brief-dom-integrity-a11y-hardening

**Status:** approved and executed — distinct coverage review D-006; release closure D-016  
**Spec:** [spec.md](./spec.md) · **Impact:** [impact-map.md](./impact-map.md) · **Validation:** [validation-plan.md](./validation-plan.md)  
**Owner:** platform-engineering · **Last updated:** 2026-08-27

## 1. Technical approach

Add two bounded structural checks to the existing local `HTMLParser`-based Human Visibility validator; do not turn it into a browser, an accessibility scanner, or a semantic-quality scorer.

1. Make `BriefParser` distinguish rendered markup from inert `script`, `style`, and `template` subtrees, and record non-empty rendered IDs plus the final rendered document close boundary.
2. Add a DOM-integrity check for all repeated non-empty rendered `id` values and rendered material after the final `</html>`. Diagnostics name only the invariant and duplicate ID, never captured document text.
3. Activate the tab check only when a v2 document declares a tablist. Verify reciprocal tab/panel wiring, one selected tab, roving `tabindex`, and canonical static evidence for keyboard, focus, active-panel and hash handling. This proves a maintained static contract; it does not execute JavaScript or certify assistive-technology behaviour.
4. Extend the focused Python fixture suite with invalid and compatibility controls, then run the existing bundle and Human Visibility commands.

The approach changes neither the v1 path nor client identity/profile code.

## 2. Architecture decisions

| ID | Decision | Rationale | Alternatives rejected | Consequence/risk |
|---|---|---|---|---|
| D-004 | Retain local parsing and model only rendered structural facts. | Defects are deterministic markup/contract defects; local parsing is fast, offline and compatible with the current validator. | Browser launch or full-source regex. | Parser boundary needs inert-subtree and comment controls. |
| D-005 | Treat declared tabs as a static-contract check, conditional on `role="tablist"`. | Catches click-only/wiring defects without rejecting v1 or proportional non-tab v2 briefs. | Require tabs everywhere; claim runtime accessibility from source text. | Human review still owns behaviour and semantic quality. |
| D-006 | Use bounded diagnostics with identifiers/rules only. | Failures must be actionable without returning customer/source payload. | Source dumps or generic pass/fail. | Source-location precision is deliberately not promised. |

## 3. Size and proportionality

**Initiative size:** localized/S.  
**Why:** one Python validator and focused suite are implementation surfaces; consumer output is checked indirectly.  
**Smaller option considered:** check only `coverage-register`; insufficient because the defect is arbitrary duplicate IDs.  
**Complexity deliberately excluded:** no browser runtime, package dependency, new schema, CI service, profile/asset work, application change, or visual/prose score.

### Client visual profile selection

**Profile:** `none`. This validator correction does not select a client profile, load an asset, or change visual tokens.

## 4. Architecture readiness and proportionality

### Assurance choice

**Profile:** A2-elevated.  
**Rationale and trigger evidence:** a false pass permits a malformed or keyboard-inaccessible governance artifact; a false fail can block valid v1/non-tab briefs.  
**A2 sources:** `spec.md` FR-001–FR-005/R-001–R-003 and `reproduction.md` M-006–M-008.  
**Reapproval trigger:** parser scope, tab grammar, v1/v2 activation, diagnostic payload, or runtime dependency changes.

**Architecture scope/size profile:** localized/S.

| Dimension | Current state | Target/decision | Proof, owner or N/A reason |
|---|---|---|---|
| System context | Offline Python validation of local initiative artifacts. | Same boundary; one stricter v2 structural stage. | `scripts/validate_human_visibility.py`; platform-engineering. |
| Components | `BriefParser`, v2 shell checks, focused test module. | Parser exposes rendered facts; separate checks consume them. | Plan §§1,5. |
| Interfaces/contracts | HTML IDs/roles/ARIA/static handler tokens. | Explicit conditional v2 grammar; no API/event change. | FR-001–FR-004. |
| Data/security | Brief read locally; report transient. | No script execution or payload echo. | D-004/D-006. |
| Runtime/failure | `validate()` aggregates a report. | Stable bounded rules; controls pass. | V-001–V-005. |
| NFRs | Deterministic, offline, bounded. | Preserve command/runtime shape. | T-004. |
| Compatibility | v1 and tabless v2 may exist. | Explicit exemptions; no migration. | AC-004/V-004. |
| Rollout/rollback | Repository script release only. | Isolated checker/fixture revert. | §8. |
| Unknowns | Parser/token exactness. | T-001 resolves U-001/U-002 before code. | §10. |

## 5. Change sequence

| Step | Surface/files | Preconditions | Result | Reversible? |
|---|---|---|---|---|
| 1 | Parser contract and focused fixtures/tests | T-001 ready | Inert/tail/tab static grammar explicit and testable. | Yes. |
| 2 | `scripts/validate_human_visibility.py` | T-001 approved | Rendered duplicate-ID and tail checks. | Yes. |
| 3 | Same validator and test suite | T-001 approved | Conditional declared-tab contract check. | Yes. |
| 4 | Guidance/tests/evidence/state/baseline | T-002/T-003 approved | Redacted diagnostics and regression release proof. | Yes; baseline only after review. |

## 6. Contracts, data and compatibility

- **API/events:** none; public contract is local CLI diagnostics.
- **DOM:** rendered non-empty IDs are globally unique; material after final rendered `</html>` is forbidden; a declared tablist uses reciprocal unique tab/panel IDs, one selected tab and roving `tabindex`.
- **Static handler:** evidence covers `ArrowLeft`, `ArrowRight`, `Home`, `End`, `Enter`, `Space`/`' '`, selection mutation, focus and hash/active-panel mutation. It is not runtime proof.
- **Compatibility:** v1 and v2 without tablist gain no tab duty. Canonical v2 tabs retain native anchors, no-script/source-order recovery and print expansion semantics.

## 7. Security, privacy and permissions

- No authentication, authorization, network or destructive operation.
- Parser must not execute inline script or emit document/fixture bodies. Only a duplicate ID needed for remediation may appear in diagnostics.
- Baseline writing is recoverable and remains review-gated.

## 8. Rollout, observability and rollback

- **Rollout:** merge only after T-004 evidence, focused/bundle commands and a distinct evaluator approval.
- **Signals:** expected negatives fail with stable rules; v1, non-tab v2 and tabbed v2 controls pass.
- **Rollback trigger:** valid control fails, diagnostic leaks payload, or static grammar conflicts with canonical handler.
- **Rollback:** revert only isolated checker/fixture changes from the last safe commit; preserve reproduction/decision evidence for repair.

## 9. Brief coverage composition

| Source locator | Coverage | Rendered target | Reason |
|---|---|---|---|
| `spec.md` problem/outcome/FR/AC/risks | represented | `#scope`, `#validation` | Scope and boundary. |
| `impact-map.md` footprint/risks | represented | `#impact` | Change and control chain. |
| this plan §§1–8 | represented | `#architecture`, `#execution` | Method, contract, rollout. |
| `tasks.md` ledger/T-001–T-004 | represented | `#execution` | Authorization/increments. |
| `validation-plan.md` V-001–V-005 | represented | `#validation` | Proof path. |
| `decision-log.md` D-001–D-016 | represented | `#evolution`, `#decision` | Authority, release matrix and independent closure. |
| `run-state.yaml` gates/ledger | represented | `#evolution` | Truthful readiness. |
| `reproduction.md` M-006–M-008 | link_only | `#scope` | The brief summarizes the trigger from `spec.md`/`impact-map.md`; the detailed reproduction remains a linked source to avoid inventing a second provenance contract before T-001. |

**Author:** Codex / planning author. **Coverage reviewer:** `review_brief013 / independent evaluator`. **Review record:** D-006.

## 10. Open questions

| ID | Question | Owner | Resolution | Blocking? |
|---|---|---|---|---|
| U-001 | Which `HTMLParser` events delimit rendered post-`html` material while excluding inert lexical content? | T-001 builder | Parser probe + fixture evidence. | yes |
| U-002 | Which static token grammar matches the canonical tab script without accepting click-only imitation? | T-001 builder | Compare canonical template and controls. | yes |

## 11. Plan decision

**Plan Ready:** yes — D-006 independently approved plan/coverage and propagation preceded task authorization.  
**Reviewer:** `review_brief013 / independent evaluator`.  
**Closure:** D-016 independently approved the completed release matrix.
