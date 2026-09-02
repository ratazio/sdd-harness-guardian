# Impact Map — SPEC 022

**Status:** draft · **Risk:** high / A2. The boundary is Guardian renderer,
state, templates and validation — never a consumer product implementation.

| Surface | Change | Risk/control |
|---|---|---|
| Promotion renderer | Stage canonical rendered state and allowlisted lifecycle markers through journal/backup/recovery before target write. | No partial/stale delivery; V-022-01/03. |
| Run-state/provenance | Bind rendered HTML blocks to current bytes and phase. | Do not alter domain source bindings; V-022-01. |
| Templates/guidance | Schema names each lifecycle marker; arbitrary narrative is not markable. | Unknown/duplicate marker rejects; V-022-01/04. |
| Human Visibility | Require distinct post-render review with current HTML digest. | No gate from pre-render review; V-022-05. |
| Regressions | Preserve Pearson, source isolation and semantic-hook boundaries. | No new semantic classifier; V-022-04. |

```txt
candidate + ready_to_render state -> in-memory rendered state/markers -> validation -> target HTML + rendered state -> post-render review
```

| ID | Risk event | Signal | Control/owner | Validation |
|---|---|---|---|---|
| IR-022-01 | Rendered target retains candidate phase/digest, including after interrupted commit. | HTML/current state mismatch or journal exists. | Temp/journal/backup recovery plus regression; renderer maintainer. | V-022-01/03 |
| IR-022-02 | Transformer edits arbitrary decision prose. | Domain text changes without source provenance, unknown/duplicate marker. | Closed lifecycle marker schema; reviewer. | V-022-01/04 |
| IR-022-03 | Pre-render approval is mistaken for post-render authority. | Missing/distorted rendered review metadata. | Distinct reviewer/record; delivery lead. | V-022-05 |
