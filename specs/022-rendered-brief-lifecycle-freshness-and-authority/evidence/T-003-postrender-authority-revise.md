# T-003 post-render authority REVISE — D-022-034

Status: builder evidence only; independent evaluation required.

## Finding

The post-render review returned REVISE P1 because the refused rendered HTML
projected pending rendered-decision review while the active source state still
made the retained pre-render review record appear to authorize guarded refresh.
The visible target was historical, so it could not be the authority for the
active canonical lifecycle.

Classification: **2 — lack of proof.** Existing atomic source/HTML promotion
proved byte synchronization for declared spans, but did not prove that an
explicit recovery checkpoint takes precedence over historical candidate and
decision-record context.

## Minimal repair

- Restored `run-state.yaml` to the source-first candidate lifecycle
  (`ready_to_render` / `render_pending`) and set `status: blocked`.
- Added a closed, generic blocked lifecycle projection. It takes precedence
  over phase-derived text and prohibits refresh/delivery while retaining all
  gates as false.
- Refused renderer entry when an explicitly present run-state status is not
  `executing`.
- Kept historical decision text and the refused HTML unchanged. Only opt-in
  source lifecycle spans were updated to the declared blocked projection.

No semantic scoring, SPEC-specific identifiers, layout assumptions, arbitrary
prose rewrite, baseline, delivery approval or SPEC 021 modification was made.

## Validation run by builder

```text
python scripts/test_render_stakeholder_brief.py             PASS
python scripts/test_source_render_isolation.py              PASS
python scripts/test_validate_human_visibility.py            PASS
python scripts/test_decision_quality_review_contract.py     PASS
python scripts/validate_bundle.py                           PASS (272 checks)
```

The guarded renderer was also invoked with the retained candidate and
`--refresh`; it refused with `run-state status must be "executing" before
rendering`, without changing the historical target. The initiative-level Human
Visibility validator still reports structural source-digest/phase divergence
for that target plus the false human gates. Those are expected evidence that
the target is refused historical HTML, not a source-first candidate eligible
for delivery; no baseline was created.

## Independent-evaluation request

Verify that the blocked-state projection is generic and opt-in, that sources
with declared lifecycle spans report the blocked checkpoint, that historical
unmarked records stay factual and byte-preserved, and that no blocked state can
start guarded refresh. Until that evaluation approves, T-003 remains
`needs_evaluation`; T-004 remains pending.

## D-022-038 — stale candidate-binding REVISE

Status: builder/state-keeper evidence; distinct pre-render review required.

D-022-037 changed canonical sources after D-022-036 bound its candidate.
The old D-022-036 candidate is therefore historical review evidence only:
guarded refresh correctly refuses it because its provenance does not bind the
current `run-state.yaml`. The operational state surfaces had incorrectly kept
the passed-review / guarded-refresh projection, and the ledger still marked
T-003 `done`.

The source-first correction reopens T-003 as `needs_evaluation`, leaves all
Human Visibility and delivery gates false and T-004 pending, resets
`brief_review` to pending/null, and recomposes the candidate with pending
pre-render authority. The recomposed candidate SHA-256 is
`f09d58bf25779d841e40a7106e1b06ade7344cfb612dea0e5464f146c7f49d69`.
`stakeholder-brief.html` was not changed and remains refused historical
evidence at SHA-256
`50ea9542934bc8da3e6c637ddd636ac0132a30e69914be2e5d25cd88acf00363`.

Source provenance and declared lifecycle markers validate for the new
candidate; its pre-render linkage deliberately refuses with
`brief_review requires distinct author and coverage_reviewer`. This is the
required pending-review state, not a render authorization. No baseline,
delivery or SPEC 021 artifact was altered.

Validation run:

```text
python scripts/test_source_render_isolation.py              PASS
python scripts/test_validate_human_visibility.py            PASS
python scripts/test_decision_quality_review_contract.py     PASS
python scripts/validate_bundle.py                           PASS (272 checks)
python scripts/test_render_stakeholder_brief.py             FAIL: existing
  malformed operational-authority fixture was accepted (line 597)
```

The focal renderer failure is recorded rather than waived; this state-only
correction did not alter renderer production code. The exact next safe action
is a distinct independent pre-render review of the recomposed candidate and
its current manifest; until that review, do not invoke guarded refresh.
