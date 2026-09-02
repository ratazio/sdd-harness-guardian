# Handoff: 014-mandatory-pearson-brief-design

**From:** `build_t001_014`  
**Intended role/recipient:** distinct T-004 evaluator  
**Created at:** 2026-08-27  
**Current phase/status:** complete / `done`  
**Current task/status:** T-001/T-002/T-003/T-004 `done`  
**Last safe checkpoint:** D-021 records recaptured corrected-consumer evidence
after mobile H1/logo sizing assertions passed; baseline and `done` remain
deliberately withheld.

## Delivered builder evidence

- D-019 independently approved the fresh consumer’s local asset distribution.
- `evidence/T-004-render/` contains fresh-consumer screenshots at
  320/768/1024/1440 (plus 390), keyboard, 200% zoom, reduced motion and
  no-script captures; `pearson-default-print.pdf`; and `render-review.json`.
- JSON records the generated brief route, only same-origin requests and the
  provisioned logo response at HTTP 200. No hotlink/data URI/vendor path was
  used.
- Functional review passed: no overflow at required widths or 200% zoom;
  keyboard tabs, reduced motion, no-script panels and print output work.
- Inventory reconciliation passed: 9 rows, 7 `historical/legacy`, 2
  `scheduled`; each row has permitted classification, owner, date, resolving
  decision reference and rationale. Nothing was reclassified from visual style.

## Mandatory evaluation check

The resubmitted `render-review.json` measures H1 at **40px** and logo at
**128px** at both 320/390px. The fresh-consumer test now asserts those ranges;
at desktop widths it measures logo 144/144/172.797px, within 144–176px.
Verify this narrow correction independently. Do not treat builder assertions
as approval.

## Exact evaluator steps

1. Re-run `python scripts/test_client_identity_profile_render.py --evidence-dir
   specs/014-mandatory-pearson-brief-design/evidence/T-004-render` against a
   fresh consumer and inspect screenshots, PDF and JSON.
2. Verify the same-origin logo request, dimensions/hash contract, keyboard,
   200%, reduced motion, no-script and print results.
3. Reconcile all inventory rows against corpus, owner/date/decision/rationale;
   do not infer migration from CSS.
4. Verify the mobile assertions and recaptured evidence. Only after an
   independent approval may baseline/recheck and a `done` transition be considered.

## Do not do

- Do not write the Human Visibility baseline or mark T-004 `done` now.
- Do not use source-template-only screenshots as fresh-consumer proof.
- Do not restyle historical inventory rows or replace the local logo with a
  remote/data/vendor path.
