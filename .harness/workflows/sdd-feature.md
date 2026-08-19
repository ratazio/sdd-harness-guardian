# Workflow: SDD Feature

## Entry condition

A consumer wants to add or change observable product behavior.

## Required artifacts

Use every artifact in the Common SDD Lifecycle. Feature acceptance criteria
must describe observable behavior without embedding unjustified implementation.
Non-trivial features also maintain `stakeholder-brief.html` for human review.

## Flow

1. Select the lifecycle lineage first. Pinned/historical v1 executes the legacy
   brief-before-task path; v2 executes `sdd-lifecycle.md` gates 1–12, including
   the unauthorised preliminary task draft, distinct coverage review and
   post-meeting propagation.
2. Confirm compatibility, migration and rollout impact where relevant.
3. For each ready task, Builder implements, drafts evidence and sets
   `needs_evaluation`; a distinct Evaluator must `approve` before State Keeper
   records `approved -> done`.
4. Run feature-level integration/regression checks.
5. Execute gates 13–15.

## Feature constraints

- contract, data or behavior changes are explicit in spec/plan;
- every feature task declares the outcome served, demonstrable increment,
  expected artifact and validation method;
- stakeholder brief remains derived; only for v2 it dispositiona applicable source
  headings and exposes draft task discussion before Tasks Ready without becoming
  a source of truth;
- the workflow asks for clarification instead of inferring business priority;
- rollout and rollback match the impact level;
- scope discovered during implementation returns to planning;
- process-only expansion of specs, docs or backlog is blocked unless it
  produces evidence, validation or named risk reduction;
- partial feature flags or migrations are documented;
- no task is `done` before its evidence pack has independent `approve`.

## Exit condition

`validation_done: true`, all tasks `done`, every AC covered, stakeholder brief
synchronized, outcome linkage preserved, evidence linked, decision log current,
final handoff written and no blocking risk open.
