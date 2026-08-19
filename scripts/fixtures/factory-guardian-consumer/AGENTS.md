# Agent Instructions

Read `vendor/sdd-harness-guardian/.harness/AGENTS.md` and local project rules.

For a non-trivial initiative, run `python scripts/check_human_visibility.py
specs/NNN-slug` before task breakdown or implementation. Do not claim Human
Visibility Ready until it passes and an independent reviewer completes the
short semantic/rendered review. New v2 initiatives keep preliminary tasks as
meeting input: append the meeting decision to `decision-log.md`, propagate it
to affected canonical sources, revalidate and regenerate the brief before
declaring `tasks_ready`. Historical/pinned v1 briefs remain on their v1 path
until material migration or a reviewed legacy exception.
