# Rule: Builder and Evaluator Separation

## Soft rule

The builder may report implementation complete and draft evidence, but only a
distinct evaluator may judge acceptance.

```txt
Builder implements -> Evaluator judges -> State Keeper advances or reopens
```

“Distinct” means a different accountable identity or a human reviewer with
fresh review context. Renaming the same self-review does not qualify.

## Risk policy

Independent evaluation is mandatory for every behavioral task. Medium/high
risk work should use a separate agent/session plus human review where required.
If no evaluator is available, leave the task `needs_evaluation`.

## Blocking conditions

Block when:

- builder and evaluator IDs match or are absent;
- the builder marks its task `approved` or `done`;
- evaluation is only the builder summary;
- evaluator cannot inspect spec, task, diff, validation and evidence;
- the evaluator edits the implementation during the same judgment.

Corrections return to the builder as `needs_revision` and require reevaluation.

## Hard mirror recommendation

Track immutable `builder_id` and `evaluator_id` in run-state and evidence.
Reject matching IDs and require evaluator decision before the terminal
transition.

Recommended check: `validate-independent-evaluation`.
