# T-003 systemic operational-source projection REVISE — D-022-043

Status: builder evidence; independent evaluation required.

## Finding and bounded repair

The prior declarative source projection covered direct authority labels but
left `run-state.yaml` operational scalars (`summary`, checkpoint,
`working_tree_summary`, and `next_safe_step`) and the canonical progress/handoff
next-step claims outside the atomic transition. That left a reproducible
post-render P1: scalar rendered state could coexist with pre-render operational
instructions.

The repair adds no phrase matcher, SPEC ID, layout rule, semantic judgment or
arbitrary rewrite. An opted-in YAML field is delimited by lifecycle comments
and explicitly names its own scalar field. Markdown retains the existing
direct-text declaration. Two closed projections derive only from structured
state: `lifecycle-authority` and `lifecycle-next-safe-step`. All declared
sources, run-state and HTML remain in the same journal/backup transaction;
unmarked historical decision text remains byte-preserved.

## Source-first restoration

The active SPEC 022 sources are restored to `ready_to_render` /
`render_pending` with a pending review, every human/delivery gate false,
T-003 `needs_evaluation` and T-004 pending. D-022-042 is historical review
evidence because the repair changes the source manifest. No baseline, delivery
artifact or SPEC 021 state was changed. The existing rendered HTML remains
refused historical evidence at SHA-256
`50ea9542934bc8da3e6c637ddd636ac0132a30e69914be2e5d25cd88acf00363`.

## Validation

`scripts/test_render_stakeholder_brief.py` now exercises a D022-equivalent,
layout-agnostic arrangement of declared YAML operational fields and declared
progress/handoff next-step spans. It proves that rendering projects every
declared operational claim, preserves unmarked historical bytes, and retains
the multi-artifact fault/recovery invariant (only all-old or all-new state,
sources and HTML survive recovery).

Independent evaluation must rerun the five required suites and inspect the
source-first candidate before any guarded refresh. This is not approval of a
candidate, rendered artifact, Human Visibility, Tasks Ready, T-004, delivery,
baseline or SPEC 021.
