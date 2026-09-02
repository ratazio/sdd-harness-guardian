# Rendered structural review — SPEC 022

**Status:** blocked pending a new human scope authorization. No task is
advanced and no HTML is approved or delivered.

## D-022-007 promotion result

The independently pre-reviewed D-022-007 candidate was promoted successfully
through T-001's repaired lifecycle. It materialized
`stakeholder-brief.html` with `brief_phase: rendered`; the renderer explicitly
reported that rendered-decision review remained mandatory.

`python scripts/validate_human_visibility.py --consumer-root . --initiative
specs/022-rendered-brief-lifecycle-freshness-and-authority` then blocked Human
Visibility before any human approval. Its material structural findings were:

- no human-readable `coverage-register` or one row for each v2 required
  source;
- two `ratchet.md` provenance blocks classified as unknown by the v2 validator;
- missing visible projections of `IR-022-02` and `IR-022-03` from
  `impact-map.md`.

## D-022-008 candidate review

The recomposed D-022-008 candidate added the coverage register and all three
impact risks, but a distinct human reviewer returned REVISE P1 because it
omitted material `ratchet.md` coverage. The unbound deferred ratchet card was
not truthful: `ratchet.md` is a current local canonical source and declares
`RATCHET-022-001` as proposed.

## Independent scope decision

`spec022_source_review` determined that the renderer admits `ratchet.md` but
`validate_human_visibility.py` excludes it from `V2_REQUIRED_SOURCES`, coverage
rows and baseline `source_set`. Projecting the ratchet through the decision log
would hide its canonical authority; a `not_applicable` disposition would be
false. The only adequate repair is a bounded reusable validator integration:

1. add only `ratchet.md` as a v2 required support source;
2. require its provenance block and coverage-register row, represented or
   synthesized in this use;
3. update baseline source-set migration and adversarial tests for absence,
   row absence, digest/fragment mismatch and invalid disposition;
4. do not broaden evidence/handoff paths, change the renderer allowlist, or
   add semantic classification/scoring.

The prior user-authorized bootstrap and D-022-004 deliberately cover only
T-001. The independent reviewer requires a fresh explicit user authorization
before this reusable T-002 integration change starts.

## Commands

```text
python scripts/render_stakeholder_brief.py ... D-022-007 candidate   PASS
python scripts/validate_human_visibility.py ...                        FAIL (23; material findings above)
python scripts/test_render_stakeholder_brief.py                        PASS
python scripts/test_validate_human_visibility.py                       PASS
python scripts/validate_bundle.py                                      PASS (272 checks)
```
