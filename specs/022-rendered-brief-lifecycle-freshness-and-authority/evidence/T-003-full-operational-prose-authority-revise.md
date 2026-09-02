# T-003 full operational-prose authority REVISE — D-022-050

## Finding

After the D-022-049 promotion, the structured lifecycle state and previously
declared lifecycle slots transitioned to rendered state. Two current-context
narratives remained unmarked in `progress.md` and
`handoffs/latest-handoff.md`, however, and instructed that the candidate was
eligible for guarded refresh. Those were active operational claims and
contradicted the rendered state.

## Repair boundary

The repair adds explicit `sdd-lifecycle-authority` declarations to those
current-context authority and next-step claims. The declaration carries only a
source binding, a closed projection and direct text. The renderer derives the
value from structured state and changes only declared direct text. Historical
decision and evidence prose remains outside that boundary.

## Recovery checkpoint

The promoted target is refused historical evidence. D-022-049 cannot bind a
candidate after this source change. Canonical state is reset to
`ready_to_render` / `render_pending`, review linkage is pending, and all
Human Visibility, Tasks Ready, delivery, baseline, T-004 and SPEC 021 gates
remain false or blocked.

## Regression evidence

`scripts/test_render_stakeholder_brief.py` now stages the real active
`progress.md` and `handoffs/latest-handoff.md` source surfaces from a
source-first pending checkpoint through a rendered transition. It verifies
each declared span binds the computed projection before and after promotion,
all active projections render, and no pending operational projection remains.
The test uses the generic opt-in protocol rather than a phrase matcher or
SPEC-specific production rule.
