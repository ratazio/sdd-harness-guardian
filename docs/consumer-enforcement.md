# Consumer Human Visibility enforcement

Consumers invoke portable Python-standard-library mechanical validators from
their own runner/hooks/CI. Validators never upload project contents.
Brief doctrine and lineage dispatch live in
`.harness/rules/brief-contract.md` BC-001–BC-025.

## Contract 3 operational entrypoint

Use `.harness/templates/README.md` and BC-009: composition, content repair,
visual repair, report. Executor/identity records follow BC-010/BC-025.
Do not install a pre-render model review or another semantic review after B.
Task readiness and owner authority follow BC-018; concluded HTML is not task
or evidence approval. Source inputs are read-only during this operation.

## Mechanical validation

Optional local structural/integrity check, or consumer CI mirror:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/004-example
```

This checks declared lineage/structure/state, never stakeholder meaning or
visual usefulness. A CI mirror may enforce proportional mechanics before
implementation, but cannot create a third semantic stage in v3 or require
legacy review fields for it. New briefs declare `data-brief-contract="3"`;
historical 1/2 and shell metadata follow BC-002 without silent regeneration.

For historical v2 only, retain the two independent passes BC-009, loopback
BC-016, model/provenance BC-005/BC-008 and decision propagation BC-018.
Its semantic outcome is distinct from deterministic PASS. Pinned v1 keeps
its concise-brief-before-tasks path without new gates.

## Freshness and baselines

Optional CI diff comparison:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/004-example --base-ref origin/main
```

For existing legacy validator baselines:

```bash
python vendor/sdd-harness-guardian/scripts/validate_human_visibility.py --consumer-root . --initiative specs/004-example --write-baseline
```

These are mechanical utilities, not required post-B commands. Historical v1
uses its schema-v1 baseline; v2 uses schema-v2 after its own review gates.
Contract 3 records source snapshot/final artifact in existing `brief_repair`
state; integrity/freshness does not prove meaning. Unsupported Git/base ref
uses the validator's stated local baseline fallback/limitation. Do not invent
hashes or approval to satisfy a check.

## Explicit exceptions

Legacy `human-visibility-exception.yaml` is consumer-local, for
not_applicable work or reviewed non-material freshness change:

```yaml
scope: freshness # or not_applicable
reason: Formatting-only change to the source artifact.
owner: named reviewer or role
human_visibility_status: reviewed
```

It never silently disables protected task/evidence gates. v3 honest source
limitations use BC-015/BC-025, not a new reviewed-exception approval queue.

## Risk-based assurance adoption

Resolve assurance_profile A1/A2/A3 before Plan Ready. A1 records concise
validation disposition; A2 applies to high/unknown risk, public contracts,
migrations, trust boundaries or material UI with task assurance contract.
A3 escalates to named local authority, not Guardian certification. Pinned
initiatives without metadata remain readable.

`validate_assurance_contract.py` checks declared structure/rationale/source
links only; independent implementation evaluation remains mandatory.

## Local bridge pattern

Consumer-root instruction example:

```md
Dispatch Human Visibility by brief-contract BC-002. New generation follows
BC-009 contract 3 and ends with the repair report BC-025; historical 1/2
retains its recorded branch. Any local mechanical CI mirror checks only
structure/integrity. Do not add a semantic review after B.
Require source/owner task authorization and independent implementation
evaluation; brief completion never approves implementation.
```

A consumer-owned wrapper may expose `check:human-visibility` in CI and
return nonzero mechanical failure; it must respect version dispatch.

## Factory scaffold contract

Factory adoption may use root instruction bridge, wrapper/CI and
`guardian-lock.json` with immutable 40-character bundle commit.
`scripts/install_guardian.py` clones --no-checkout, checks that commit
detached and verifies HEAD. The historical fixture in
`scripts/fixtures/factory-guardian-consumer/` proves v1/v2 behavior;
it is not proof of contract-3 runtime acceptance or an instruction to migrate
existing consumers. Factory replaces its lock placeholders when generating.
