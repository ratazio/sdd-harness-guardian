---
name: spec-review
description: Use when reviewing a feature, bugfix, refactor or initiative spec for clarity, completeness, testability and readiness before implementation.
version: "0.2.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Spec Review

## When to use

- A spec needs approval before planning.
- A user asks whether a spec is ready.
- An agent is about to implement from a spec.

## When not to use

- The task is only formatting text.
- The task is brainstorming only and no initiative or decision brief is being reviewed.
- A human explicitly asks for brainstorming only.

## Procedure

1. Read the spec, stakeholder brief when present, and local rules.
2. Identify objective, product/user outcome, demonstrable increment, non-goals
   and assumptions.
3. Check acceptance criteria for testability.
4. Detect vague terms and hidden decisions.
5. Check whether the agent would need to infer commercial value or roadmap
   priority.
6. For v2, check the Plan Ready architecture profile: current/target context,
   responsibilities, contracts, data/trust, critical/failure flows, NFR,
   migration, observability, rollback, alternatives and unknowns. Missing
   material facts must block or become bounded discovery; do not infer them.
7. For a v2 brief, read `.harness/templates/stakeholder-brief-design.md` and
   check whether `stakeholder-brief.html` is present for non-trivial work,
   derived from the source artifacts, concise enough for review, and consistent
   with them. Use the conditional checklist in `human-visibility.md`: verify
   outcome/benefit, scope/anti-scope, affected surfaces, S/M/L rationale,
   smaller option, validation, risks and requested decision. Require
   architecture, impact or flow visuals only when their trigger applies; require
   a short omission reason otherwise. Reject generic or unreadable visuals.
   Confirm the canonical `v1` brief shell was populated rather than rebuilt;
   a material custom layout must have a reviewed rationale, owner and retained
   decision surfaces recorded in `decision-log.md`.
   For v2, inventory applicable source headings and require an existing-plan
   coverage disposition, locator, rendered target/reason and the three
   provenance attributes. Confirm core material headings are not link-only.
    Conduct the pre-render coverage pass as a distinct identity from the brief
    author; record the reviewer/author, findings and decision-log locator.
    Self-review does not qualify. Require named human review if no independent
    identity is available. Then conduct a distinct post-render, loss-aware
    reading: classify product, architecture/operations and delivery as
    `recoverable`, `superficial`, `absent` or justified `N/A`. Each finding
    names the canonical source, lost/weakened fact and source correction. Ask:
    “Which material decision remains impossible without opening Markdown?” This
    is qualitative independent judgment, never a score, prose parser or
    automatic semantic gate. Check each of the eight views against its
    conditional mission: value/scope recovers mission, material value/operating
    pillars, limits, main risk and authority; architecture and impact introduce
    their mission/vision without inventing technical detail; execution recovers
    the existing detailed task contract when it exists; validation recovers the
    AC/proof context and honest no-command/skip limit. Evolution, decision and
    coverage expose truthful state, authority and provenance. These are
    source-backed content contracts, not field quotas.
    For a missing fact, ask only if it changes or blocks a decision, AC, risk
    control, authority or next safe step. A material question states the exact
    fact needed, accountable owner, decision impact and resolution path in an
    existing canonical source. A non-material absence is concise justified N/A
    or omitted optional detail; never accept filler, a fake diagram/API or a
    vague “to be confirmed”.
   For a decision-quality delivery claim, use the rendered-brief-decision-review
   skill: compare the originating request, source locators and locally served
   HTML through architect, system designer, executive, general stakeholder and
   delivery lenses. Material relations need an accessible connected model or a
   justified proportional alternative; no tab/card/SVG quota is implied.
   When a review finding is recoverable from the request and canonical sources,
   return it directly to composition and repeat the relevant review in the same
   run. Do not turn ordinary completeness, diagram or wording repairs into a
   requester approval checkpoint; escalate only a new authority, scope, or
   genuinely absent material fact.
8. Classify issues as blocking or non-blocking.
9. Return Outcome Ready yes/no, Spec Ready yes/no and Human Visibility Ready
   yes/no.

## Output contract

Return a report with: summary, blocking issues, non-blocking issues, missing
fields, recommended rewrite, Outcome Ready status and Spec Ready status.
Include Human Visibility Ready status when the initiative is non-trivial. For
v2, also report `tasks_drafted`, `brief_coverage_ready`, review identity and
whether post-meeting propagation is still required before Tasks Ready. Separate
the pre-render coverage result from the post-render meaning result; include the
three lens judgments, justified `N/A` reasons, source → lost fact → recovery
action for every finding, and the decision-loss answer.

## Quality bar

A good review blocks vague or invisible work before code starts and gives
precise edits needed to make the spec executable and reviewable.
