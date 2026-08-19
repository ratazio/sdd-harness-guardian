# Consumer Human Visibility enforcement

The bundle supplies a portable validator; each consumer invokes it from its
own task runner, hook, or CI provider. It is Python-standard-library only and
never sends project contents anywhere.

Run it from the consumer root:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/004-example
```

Before task breakdown or implementation, the command must pass and an
independent reviewer must perform the short semantic/rendered brief review. A
pass checks stable structure, design lineage/shell, and declared state only; it is not approval of
prose, stakeholder usefulness, or visual legibility.

## Design-contract validation and compatibility

New non-trivial initiatives scaffolded by the current bundle use
`data-harness-brief-design="v2"`, expanded source freshness, local provenance,
the coverage register and distinct review metadata. Historical/pinned v1
briefs remain accepted under their four-source v1 contract; do not silently
rewrite them. A material v1 refresh must follow the validator's migration
diagnostic or record a reviewed legacy exception.

Both lineages retain the canonical shell hooks. The validator reports missing
lineage or hooks as deterministic design-contract failures; it does not score
rendered quality. A material custom layout needs a reviewed exception in the
initiative `decision-log.md`, stating rationale, owner and retained decision
surfaces; do not create a layout-exception sidecar.

## V2 order and post-meeting propagation

For v2, preliminary tasks are meeting input only. The required order is:

```txt
task draft -> coverage composition -> distinct coverage review -> final brief
-> meeting -> decision-log append -> affected canonical-source updates
-> revalidation/coverage refresh -> regenerated brief -> Tasks Ready
```

Do not set `tasks_ready` or begin implementation from an HTML-only decision or
transcript. The consumer owns extraction, source edits and brief regeneration;
the bundle supplies the contract and validator, not a meeting integration.

## Freshness

In CI, compare the current change to the provider's existing base ref:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/004-example --base-ref origin/main
```

If a tracked source changed in that diff but `stakeholder-brief.html` did
not, validation fails. If Git or that ref is unavailable, the command reports
the limitation and falls back to the local hash baseline; it fails only when
that fallback cannot validate freshness. The validator does not require a
particular CI system; the local wrapper supplies the appropriate base ref.

For offline or archive use, write the inspectable local hash baseline only
after the structural/gate check and independent review are complete. V2 writes
schema v2 in the same baseline file; pinned v1 remains schema v1:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/004-example --write-baseline
```

Later runs without `--base-ref` compare those hashes. A baseline is evidence
of a refresh point, never a replacement for independent review.

## Explicit exceptions

Use `human-visibility-exception.yaml` only for `not_applicable` work or a
reviewed non-material freshness change. It must be local to the initiative:

```yaml
scope: freshness # or not_applicable
reason: Formatting-only change to the source artifact.
owner: named reviewer or role
human_visibility_status: reviewed
```

The validator prints accepted exceptions as limitations. Missing fields or a
status other than `reviewed` fail; an exception cannot silently disable the
protected gate.

## Local bridge pattern

Place this contract in the consumer root `AGENTS.md`, adapting the command
name to its task runner:

```md
Before task breakdown or implementation for a non-trivial initiative, run
`python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/NNN-slug [--base-ref <CI base ref>]`.
Do not claim Human Visibility Ready until it passes and an independent reviewer
has completed the short semantic/rendered brief review.
```

A generic wrapper can expose the command as `check:human-visibility` and call
it from a pre-task step or CI job. The wrapper is consumer-owned and must
return the validator's non-zero result before work proceeds.

## Factory scaffold contract

A Factory template can make the adoption reproducible with a root instruction
bridge, `scripts/check_human_visibility.py`, a CI invocation point, and a
`guardian-lock.json`. The lock contains the bundle repository and an immutable
40-character commit. Its local `scripts/install_guardian.py` clones with
`--no-checkout`, checks out that commit detached, and verifies `HEAD` before
the wrapper runs. The template fixture under
`scripts/fixtures/factory-guardian-consumer/` is executable evidence of this
contract; Factory replaces its two lock placeholders with its selected URL and
commit when generating a consumer repository. The executable fixture proves
both historical v1 validation and a v2 source/review/propagation record.
