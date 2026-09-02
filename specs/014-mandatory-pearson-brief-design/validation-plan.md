# Validation Plan: 014-mandatory-pearson-brief-design

**Status:** ready for independent planning review; no implementation validation has run · **Owner:** platform-engineering

| Validation | AC | Method / oracle | Evidence |
|---|---|---|---|
| V-001 | AC-001 | Scaffold a fresh fixture and manually copy the supported source; each asserts literal Pearson declaration, local guide path and semantic hooks. Historical dated-exception control remains allowed. | evidence/T-002.md |
| V-002 | AC-001/005 | Missing/non-Pearson post-cutover profile and selector-only/generic-rebuild fixtures fail. | evidence/T-003.md |
| V-003 | AC-002 | Asset path, exact hash `8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7`, 175 × 53/aspect, anchor semantics, no-hotlink and no-filter checks. | evidence/T-002.md |
| V-004 | AC-003 | Existing Human Visibility/provenance/tab/no-script/print suites pass. | evidence/T-003.md |
| V-005 | AC-004 | Rendered desktop/mobile/keyboard/zoom/motion/print review against guide. | evidence/T-004.md |
| V-006 | AC-005 | External asset/undocumented visual override fixtures fail with repair message. | evidence/T-003.md |
| V-007 | AC-006 | Canonical migration inventory schema, included corpus, exclusions and one truthful classification per row. | evidence/T-004.md |
| V-008 | AC-006 | A custom-layout exception fixture/record is rejected unless it names owner, reason, retained decision/accessibility surfaces, independent visual-review outcome and dated re-review target. | evidence/T-004.md |

Required commands after implementation: focused validator tests, `python scripts/validate_bundle.py`, fresh-fixture baseline/recheck, and independently reviewed screenshot/accessibility evidence. No command proves subjective design fidelity alone.
