# Material relation composition fixtures

These are two deliberately different source corpora for SPEC 021 T-002. They
are calibration evidence for a human semantic reviewer, not a representation
taxonomy and not a production selection algorithm. Each reviewer names why this
case's source relationship calls for the chosen structure; the Python check
only preserves declared locators, digests and the fact that the positive and
negative records remain distinguishable.

| Case | Corpus relationship | Chosen source-backed representation |
|---|---|---|
| `clearing-boundary` | A settlement instruction must cross a segregated trust boundary before it can become a ledger posting. | Boundary handoff table, because the source names sender, receiver, allowed payload and refusal authority. |
| `reservoir-recovery` | A physical reservoir moves through alarm, hold, confirm and recovery states under an operations owner. | Recovery state progression, because the source defines transitions and an unsafe restart condition. |

The `*-lost` records intentionally remain structurally plausible while a
material relation is absent. Their human verdict is `REVISE`; they demonstrate
that no visual shell, fixed number of nodes, or generic arrows substitutes for
the source-derived relationship.
