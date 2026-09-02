# Validation Plan — SPEC 022

**Status:** draft · **Strategy:** A2 lifecycle integrity plus independent
rendered-decision review.

| ID | AC | Method/oracle | Evidence |
|---|---|---|---|
| V-022-01 | AC-022-01 | Fixture declares allowlist/schema; promote and assert phase/current digest for each listed marker, while unknown/duplicate markers refuse and non-allowlisted bytes remain unchanged. | T-001 |
| V-022-02 | AC-022-02 | HTML-first reviewer distinguishes pre-render approval from pending post-render review and Tasks Ready false. | T-001/T-002 |
| V-022-03 | AC-022-03 | Inject failure at every temp/journal/backup/rename/recovery point; assert only documented recoverable pair, then repair/refuse before exposure. | T-001/T-003 |
| V-022-04 | AC-022-04 | Negative/inspection prove allowlist is lifecycle-only, with no prose score, domain taxonomy or semantic approval. | T-003 |
| V-022-05a | AC-022-05 | Fresh SPEC 021 candidate receives distinct pre-render APPROVE bound to its exact digest and source manifest. | T-004 |
| V-022-05b | AC-022-05 | Promoted exact HTML receives architect, system designer, executive, general stakeholder and delivery-manager APPROVE records, each with digest/locators; any material REVISE blocks all 021 gates. | T-004 |

Required regressions: `python scripts/test_render_stakeholder_brief.py`,
`python scripts/test_source_render_isolation.py`,
`python scripts/test_validate_human_visibility.py`,
`python scripts/test_decision_quality_review_contract.py` and
`python scripts/validate_bundle.py`.

The deterministic oracle proves state/byte/lifecycle binding only. The
post-render reviewer decides whether the HTML communicates the correct current
authority and all material decisions for the initiative.
