# Source-package review — SPEC 022

**Reviewer:** `spec022_source_review` (independent of the future T-001
builder). **Final verdict:** APPROVE, 2026-08-28.

## Review history

The first review returned REVISE with three P1 findings: the original
temp/journal proposal lacked exact atomic recovery; the SPEC 021 replay did
not separately require the pre-render review; and the lifecycle-marker scope
was not a closed schema. Those were corrected in `spec.md`, `plan.md`,
`tasks.md`, `validation-plan.md` and `impact-map.md`.

The first corrected review then found a final P1: the original T-001 only
modeled the contract while T-002 implemented it, so the limited bootstrap could
not render this SPEC. T-001 was made the one atomic minimum repair, and T-002
was reduced to later integration/hardening.

## Final independent conclusion

The reviewer approved only the bootstrap below:

- start T-001 after state synchronization;
- scope: renderer, closed lifecycle-marker allowlist, temporary generation,
  journal/backup/renames/recovery, fixtures and directly necessary tests;
- prohibit domain prose/decisions, baseline or Tasks Ready, edits to blocked
  SPEC 021, and execution of T-002 through T-004;
- require a new independent implementation evaluator before T-001 is done.

The reviewer required V-022-01 to V-022-03 for T-001, including unknown and
duplicate marker refusal, unchanged non-allowlisted bytes, every commit/recovery
fault injection, and a HTML-first confirmation of the post-render authority.

## Commands

`python scripts/validate_bundle.py` — PASS (`272 checks`) after the source
package repairs.

## Locators reviewed

- `spec.md` — bootstrap limitation and FR/AC scope
- `plan.md` — closed schema, recovery protocol and D-022-05
- `tasks.md` — T-001 as the complete minimal repair
- `validation-plan.md` — V-022-01 through V-022-05b
- `run-state.yaml` — explicit user authorization and retained gates
