---
name: executive-brief-experience-review
description: Independently assess whether an executive stakeholder brief and its architecture explanation are source-grounded, decision-ready and visually proportional; use after a distinct composer has produced a candidate.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Executive Brief Experience Review

## Purpose

Judge a composed executive brief as a separate evaluator. This is a
source-and-experience reading, not a semantic scoring program and not a
license to repair the candidate during review.

## Pre-skeleton construction-plan review

When no candidate exists, review the construction record in the existing
`plan.md` before skeleton instantiation. Read requester intent and canonical
sources, then confirm that coverage is not being used as a substitute for
storytelling/visual decisions: the thesis/audience, each of the eight routes,
material relationships, selected form with reason, repeated components,
limits/discoveries and closing actions are all either source-grounded or
explicitly N/A.

Return `APPROVE` or `REVISE`. For every `REVISE` finding, write **source → loss
or ambiguity → decision prejudiced → canonical correction**. Do not require
any fixed number of cards, diagrams, SVGs, views or words, and do not edit the
plan during this assessment. `APPROVE` authorizes skeleton instantiation only;
it is not an approval of the future candidate or a shortcut around the later
desktop review.

## Required comparison

Read the requester intent, applicable canonical sources, reviewed construction
record, candidate/rendered artifact and task validation plan. Record hashes and
locators for the reviewed artifacts when they are evidence. The reviewer must
not be the composer or builder.

## Review lenses

Use only the lenses material to the case, and name why each is material or not:

- executive decision: purpose, perimeter, trade-off and next action are
  recoverable without reopening Markdown;
- narrative: thesis and pillars are a faithful synthesis rather than a generic
  route preamble;
- architecture/operations: topology, surface status, quantity and zoom (or a
  proportional N/A/discovery) do not manufacture detail;
- visual and access experience: the chosen route presentation helps the
  decision and does not make colour, a diagram or a polished shell its only
  carrier;
- trust: source, locator, limitation and lifecycle remain visible enough to
  challenge a claim.

For a rendered desktop brief, visit each of its eight route URLs rather than
reviewing source order or a single landing view. Treat untouched scaffold prose
as a material `REVISE` finding when it remains stakeholder-visible: a polished
architecture or task dossier does not compensate for generic impact,
validation, evolution, decision or coverage content. The finding is about the
lost source-specific decision surface, never a rule that every route needs a
fixed visual form or amount of copy.

Apply that test to editorial claims, explanations and diagrams—not to stable
interaction/lifecycle chrome. Repeated tab names, accessibility affordances,
fixed provenance marks and an honest common gate-false status are permitted
when they make no initiative-specific claim. Their adjacent explanatory copy
must still let a stakeholder understand the consequence in this initiative.

For every material finding, provide request/source/map/artifact locators, the
lost or invented fact, decision impact, canonical recovery action and the
originating reviewer needed after repair. `APPROVE` and `REVISE` are human/
agentic evidence, never a deterministic program conclusion.

## Boundaries

- Do not edit HTML, Markdown, fixtures, CSS or scripts during the assessment.
- Do not demand a universal SVG, card grid, quantity, frontend view or prose
  length.
- A structurally valid artifact can still receive `REVISE` for shallow,
  misleading or unsupported explanation.
- A missing material fact must state the missing fact and decision impact. When
  the source supports a discovery owner/path, require both; when it does not,
  require the artifact to say explicitly that owner/path are not established.
  “To be confirmed” without this distinction is insufficient.

## Output

Write an evaluation report with reviewer identity, reviewed inputs/locators,
lens materiality, findings, verdict, residual risk and next safe action. An
approval permits the State Keeper to move the task through its normal evidence
gate; it never lets the reviewer mark it done.
