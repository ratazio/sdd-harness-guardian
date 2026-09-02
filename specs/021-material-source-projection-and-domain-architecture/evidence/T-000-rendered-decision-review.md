# Rendered-decision review — SPEC 021

**URL:** `http://127.0.0.1:8878/specs/021-material-source-projection-and-domain-architecture/stakeholder-brief.html`
· **HTML SHA-256:**
`cb68a38a6389830ca57745e4f8296d0540f11dcb17332feeed7910794c581d6f`
· **Date:** 2026-08-28.

## Independent lenses

| Lens / identity | Verdict | Result |
|---|---|---|
| Architect / `/root/spec021_quality_architect` | APPROVE | The source→hook→disposition→composition→review relationship and boundaries are structurally recoverable. |
| System designer / `/root/spec021_quality_system` | REVISE P1 | HTML says `data-brief-phase="authored"` and binds a stale `run-state.yaml` digest although current state is rendered; post-render ownership is ambiguous. |
| Executive / `/root/spec021_quality_executive` | APPROVE | Outcome, anti-scope, automatic-seal risk and current authority are recoverable. |
| General stakeholder / `/root/spec021_quality_stakeholder` | REVISE P1 | Header/coverage/decision still present a candidate awaiting promotion, contradicting canonical rendered state. |
| Delivery manager / `/root/spec021_quality_delivery` | REVISE P1 | Cannot decide whether the served file is an approved post-promotion review object or the candidate; gates cannot advance. |

## Material finding and disposition

**F-021-RD-01 — promoted HTML retains pre-render lifecycle/provenance.** The
renderer copies candidate bytes and then updates `run-state.yaml` to rendered.
Consequently the output retains authored/candidate text, pre-render reviewer
wording and the pre-render source digest. This is a reusable lifecycle defect,
not an isolated HTML repair.

Human Visibility, Tasks Ready and baseline remain blocked. SPEC 022 owns the
reusable lifecycle repair; after it, SPEC 021 must recompose and repeat both
independent review phases.

`validate_human_visibility.py` failed 18 gates in this incomplete state. That
deterministic failure neither overrides nor replaces the material review.
