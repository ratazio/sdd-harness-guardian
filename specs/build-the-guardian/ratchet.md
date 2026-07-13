# Ratchet Log: build-the-guardian

## Index

| ID | Failure type | Severity | Status | Owner | Regression check |
|---|---|---|---|---|---|
| RG-001 | state_loss | medium | implemented | bundle maintainers | validator + scaffold smoke test |
| RG-002 | task_too_large/state_drift | high | implemented | bundle maintainers | evaluator cycle + state/readiness checks |

## RG-001 — State scaffold followed initial edits

The supplied build prompt functioned as the initial spec, but project-local
initiative state was not scaffolded before the first documentation edits.

Root cause: initial templates did not provide direct YAML or a safe,
single-command complete scaffold, and the build prompt did not explicitly
bootstrap source-maintenance state.

Prevention: canonical template guide, direct `run-state.yaml`, optional safe
scaffolder, entrypoint bootstrap instructions and source ratchet entry.

Regression check: validate the bundle, scaffold feature/bugfix initiatives in
isolated roots and confirm duplicate-target refusal.

## RG-002 — Integrated build bypassed dependency sequencing and drifted state

The first evaluator found that interdependent tasks were all implemented before
their dependencies were terminal, and progress/handoff lagged behind executed
checks.

Root cause: the source build began from a prompt before the initiative
lifecycle was bootstrapped, then evidence/state were assembled retrospectively.

Prevention:

- the build prompt now requires source-initiative bootstrap before edits;
- `release_candidate` replaces premature `ready`;
- a reproducible smoke command retains auditable output;
- dependency waivers must be explicit and terminal transitions stay ordered;
- validator checks ready status against the completed checklist.

Regression check: a fresh evaluator must reject contradictory state or an open
checklist before `ready`; source progress, handoff, tasks and run-state must
agree before reevaluation.
