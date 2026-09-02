# Validation Plan: 010-stakeholder-brief-composition-kit

**Status:** draft  
**Spec:** [spec.md](./spec.md)  
**Plan:** [plan.md](./plan.md)  
**Owner:** platform-engineering  
**Last updated:** 2026-08-26

## Strategy

Use deterministic fixture checks for stable DOM/provenance/fallback contracts
and independent rendered review for proportionality, source fidelity and visual
utility. Compare three input shapes: rich software, sparse/localized and
non-software. No test scores prose or declares aesthetics semantically correct.

## Acceptance traceability

| Validation | AC | Method / fixture | Oracle | Evidence |
|---|---|---|---|---|
| V-001 | AC-001 | Guidance/repository review. | Integrated composition entrypoint exists; no mandatory fixer agent. | evidence/T-001.md |
| V-002 | AC-002 | Rich architecture fixture + browser review. | Macro plus one supported focus cut has required relationship/text equivalent. | evidence/T-002.md |
| V-003 | AC-003 | Sparse and non-software fixtures. | No fake technical visual or empty row; concise omission is understandable. | evidence/T-002.md |
| V-004 | AC-004 | Rich/sparse task fixtures. | Every available source field projects; absent optional field does not become generic blank. | evidence/T-002.md |
| V-005 | AC-005 | Impact/coverage fixture + semantic table check. | Relationship composition and accessible source trace both recoverable. | evidence/T-003.md |
| V-006 | AC-006 | Screen-reader/keyboard/manual grayscale inspection. | Proof/limitation/state/authority have text/structure non-colour cues. | evidence/T-003.md |
| V-007 | AC-007 | Existing v2 tests + no-script/390/print browser tests. | No tab/provenance/fallback regression. | evidence/T-004.md |
| V-008 | AC-008 | Independent reviewer source-to-render trace. | Unsupported detail returns to source correction. | evidence/T-004.md |
| V-009 | AC-010 | Negative generic-profile fixture/source scan. | No client style/asset in vendor-neutral kit. | evidence/T-004.md |
| V-010 | AC-009 | Negative code/test review. | No score/LLM/word quota/mandatory diagram gate. | evidence/T-004.md |
| V-011 | AC-011 | Source-to-HTML parity fixture. | Every task ID in populated ledger and every AC in populated trace is recoverable in the appropriate rendered view; generic scaffold fails. | evidence/T-004.md |
| V-012 | AC-012 | Draft lifecycle fixture and independent review. | Unrendered scaffold is visibly draft and cannot pass visibility/readiness. | evidence/T-004.md |

## Required commands

| Command | Environment | Expected result | Tasks |
|---|---|---|---|
| python scripts/test_brief_v2_contracts.py | bundle root | existing v2 contracts pass | T-002–T-004 |
| python scripts/test_tabbed_brief_surface.py | bundle root | tab wiring/fallback remains valid | T-003–T-004 |
| python scripts/test_semantic_brief_review_calibration.py | bundle root | reviewer calibration fixtures remain valid | T-002–T-004 |
| python scripts/validate_bundle.py | bundle root | reusable bundle checks pass | T-004 |
| focused source-to-brief parity test | bundle root | populated task/AC identifiers agree with rendered Execution/Validation; scaffold-negative fixture fails | T-004 |

## Manual and independent checks

| ID | Steps / environment | Oracle | Evidence |
|---|---|---|---|
| M-001 | Open rich reference at desktop/390px; inspect macro and focused cut. | Cut answers a decision and has textual equivalent. | T-002 notes/screenshots as supplement. |
| M-002 | Compare rich and sparse task cards. | Rich card is complete; sparse card is concise and truthful. | T-002 review. |
| M-003 | Inspect impact/coverage at 320/390px, keyboard, print, no script. | Information order/semantic equivalent persists. | T-003 review. |
| M-004 | Disable colour perception or inspect text/structure. | State/authority/proof remain intelligible. | T-003 review. |
| E-001 | Independent reviewer reads the composition guidance. | Selection does not create a parallel author. | T-001 decision. |
| E-002 | Reviewer traces rich deeper blocks to sources. | Source-backed, proportional and decision-useful. | T-002 decision. |
| E-003 | Reviewer compares non-software/sparse source. | No software determinism or bureaucratic unknown. | T-002 decision. |
| E-004 | Final reviewer traces output/correction behavior. | Canonical correction, not HTML-only repair. | T-004 decision. |
| M-005 | Open a generated rich fixture after its sources are populated. | Execution visibly lists every source task and Validation visibly carries the source AC trace. | T-004 review. |
| E-005 | Reviewer checks source, state and linked HTML at draft and derived phases. | A scaffold was not represented as the stakeholder brief. | T-004 decision. |

## Skipped validation

No production load/security test is applicable: no service, credential, remote
asset or data boundary is added. This does not waive accessibility or source
fidelity review.

## Validation decision

**Validation Ready:** no — mappings are complete for draft review; execution
results do not exist.
