# Spec: 013-brief-dom-integrity-a11y-hardening

**Status:** draft · **Sequence:** 013 · **Owner:** platform-engineering · **Risk:** medium · **Assurance:** A2-elevated

## Problem

The first full mock-lab run independently found the same defects in M-006, M-007 and M-008: duplicate `coverage-register` IDs, non-whitespace content after `</html>`, and click-only tab UI in two briefs. The deterministic Human Visibility validator passed those defects. Packages were repaired manually; the reusable bundle has no regression protection.

## Outcome and boundary

Make a malformed v2 brief fail deterministically for duplicate HTML IDs, content after the closing document element, or a declared tab contract without keyboard/focus mechanics. Add focused fixtures and diagnostics. Preserve vendor-neutral/no-script/print behavior and keep architecture/prose quality as independent human judgment.

- **User outcome:** maintainers receive actionable failure before an invalid or keyboard-inaccessible brief reaches review.
- **Demonstrable increment:** failing fixtures for each defect; current canonical tabbed and non-tab v2 controls pass.
- **Non-goals:** browser crawling, visual/prose scoring, automatic source synthesis, application UI validation, or changing client identity profiles.

## Requirements and acceptance

| ID | Requirement | Acceptance / validation |
|---|---|---|
| FR-001 | Validator rejects every repeated non-empty HTML `id` in rendered markup, not only known shell ids. Discovery excludes `script`, `style`, and `template` subtrees. | AC-001 / V-001: duplicate `coverage-register` and arbitrary duplicate ids fail and name the id; literal duplicates in inert subtrees pass. |
| FR-002 | Validator rejects a non-comment, non-whitespace rendered token after the final rendered `</html>` boundary, including a tag, text, declaration, or processing instruction. It accepts trailing whitespace/comments and literal `</html>` strings or markup inside `script`, `style`, and `template` subtrees. | AC-002 / V-002: rendered tails fail; allowed tail/inert controls pass. |
| FR-003 | A v2 brief that declares `[role="tablist"]` must expose a complete static tab contract per tablist: each contained `[role="tab"]` has a unique id and reciprocal `aria-controls` reference to a contained `[role="tabpanel"]`; each panel names the tab with `aria-labelledby`; exactly one tab in that tablist is `aria-selected="true"`; the selected tab has `tabindex="0"` and every other tab has `tabindex="-1"`. The rendered script body, rather than visible prose, must contain semantic static evidence for click and `keydown` listeners, ArrowLeft, ArrowRight, Home, End, Enter, and Space, selection mutation, active-panel mutation, focus, and hash/history mutation. Multiple tablists must each satisfy this isolated contract or the validator fails. Native anchors, no-script fallback, and print semantics remain intact. | AC-003 / V-003: click-only tabs, prose-token click-only tabs, multiple selected tabs, broken reciprocal references, multiple-tablist ambiguity, and missing static keyboard-handler evidence fail with actionable diagnostics; canonical v2 passes. |
| FR-004 | A v1 brief and a v2 brief with no `[role="tablist"]` remain outside the tab-specific contract. | AC-004 / V-004: canonical tabbed v2, intentionally non-tabbed v2, and v1 controls each pass applicable checks. |
| FR-005 | Diagnostics identify the invariant and bounded remediation without leaking fixture payload or document bodies. | AC-005 / V-005: all negative fixtures have stable, specific messages and diagnostic-redaction passes. |

## Constraints, risks and unknowns

- Parse locally without executing brief JavaScript or loading network assets.
- Keep the new checks deterministic and bounded; no check certifies semantic usefulness.

| ID | Risk / unknown | Control / resolution |
|---|---|---|
| R-001 | Parser or checks misread valid/inert document content. | T-001 selects document-aware parser/fallback and fixtures for inert subtrees, permitted tails, no-tab v2, and v1. |
| R-002 | Valid proportional non-tab briefs are rejected. | Conditional activation plus non-tab control fixture. |
| R-003 | Diagnostics expose source content. | Report contract/ID only; independent security review. |
| U-001 | Parser source-location capability is unknown. | T-001 records bounded approach before implementation. |

## Evidence and decision

Trigger evidence: current-suite planning reviews for `m006-agentic`, `m007-kiosk`, and `m008-events` under `testes/mock-runs/20260827-full-suite/`. This is planning only: Outcome Ready and Spec Ready remain false until independent review.
