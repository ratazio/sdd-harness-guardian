# Rule: Spec Indexing and Numbering

## Soft rule

Initiatives must live under `specs/NNN-slug/`, where `NNN` is a zero-padded,
monotonic sequence and `slug` is a lowercase stable identifier. The number is
chronology and identity, not business priority. Do not reuse a sequence after a
spec is deleted, superseded or abandoned.

`specs/INDEX.md` is the first-read map for humans, agents and retrieval systems.
It should contain one compact row per initiative with sequence, initiative ID,
kind, status, outcome summary, owner, last update and spec path.

Agents should start from:

```txt
1. specs/INDEX.md
2. the active initiative run-state.yaml
3. progress.md and latest handoff
4. only the specific source artifacts needed for the current gate
```

Full-repository semantic search or embeddings may be used as an optional
retrieval layer, but they do not replace deterministic index and state files.

## Legacy or out-of-standard projects

When a consumer has unnumbered initiatives, an agent must not silently create a
parallel numbered copy. First build an inventory, propose a deterministic rename
map, identify broken references, request human approval when renames are risky,
then update `specs/INDEX.md`, `run-state.yaml`, handoffs and references.

Recommended migration shape:

```txt
specs/login-flow/      -> specs/001-login-flow/
specs/payment-webhook/ -> specs/002-payment-webhook/
```

If chronology cannot be inferred from Git history, file metadata or human
notes, preserve current lexical order and record the uncertainty in
`decision-log.md`.

## Hard mirror recommendation

Validate that initiative directories match `^[0-9]{3}-[a-z0-9][a-z0-9._-]*$`,
that `run-state.yaml` agrees with the directory sequence and slug, and that
`specs/INDEX.md` contains exactly one row for each non-archived initiative.

Recommended check: `validate-spec-index`.
