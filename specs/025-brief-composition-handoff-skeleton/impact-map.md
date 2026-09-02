# Impact map — SPEC 025

## Outcome and boundary

The change makes the existing v2 composition handoff operational. It does not
replace canonical Markdown, invent content or retrofit history.

| Surface | Delta | Control / owner | Risk |
|---|---|---|---|
| `plan.md` composition | free coverage table → route/block editorial plan | composer + distinct coverage reviewer | missing/duplicated source mapping |
| Candidate lifecycle | manual external HTML → instantiated skeleton then composed candidate | visual builder + renderer | scaffold misrepresented as deliverable |
| Render promotion | slot/parity checks before safe promotion | renderer maintainer | generic content passes structurally |
| Human Visibility | judgment review with clearer inputs | executive brief reviewer | deterministic score replaces judgment |
| Workflow/roles | explicit handoffs, existing roles reused | orchestrator | competing paths / agent confusion |
| Laboratory references | preserve, mark non-canonical | mock-lab maintainer | accidental adoption/mutation |
| Consumer briefs | future v2 candidates gain continuity | consumer author | unexpected history rewrite |

## Dependency and data flow

```txt
spec.md + impact-map.md + plan.md + tasks.md + validation-plan.md + state/decisions
  → plan.md: reviewed editorial map
  → candidate skeleton (slots, no claims, not promotable)
  → composed candidate (source-backed content and visual form)
  → exact pre-render candidate attestation (hash + manifest)
  → guarded promotion to stakeholder-brief.html
  → independent rendered review
```

## Negative boundary

- `build_spec024_heterogeneous_references.py` remains evidence-only.
- `testes/mock-runs/` and historical briefs are never bulk refreshed.
- HTML never becomes a canonical decision or task record.
