#!/usr/bin/env python3
"""Minimal fixture for the required v2 post-meeting propagation order.

This is deliberately a fixture, not a meeting service or a general brief
generator. Consumers remain responsible for extracting decisions and updating
their canonical artifacts; the fixture proves the non-negotiable ordering.
"""

from __future__ import annotations

import tempfile
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def regenerate_brief(initiative: Path) -> None:
    """Test-local stand-in for populating the derived brief from canonical data."""
    decision_log = (initiative / "decision-log.md").read_text(encoding="utf-8")
    spec = (initiative / "spec.md").read_text(encoding="utf-8")
    require("D-002" in decision_log, "cannot regenerate before the meeting decision is logged")
    require("D-002" in spec, "cannot regenerate before affected canonical sources are updated")
    (initiative / "stakeholder-brief.html").write_text(
        "<html data-harness-brief-design=\"v2\"><body>"
        "Derived after canonical propagation: D-002."
        "</body></html>\n",
        encoding="utf-8",
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="sdd-post-meeting-") as temporary:
        initiative = Path(temporary) / "specs" / "001-example"
        initiative.mkdir(parents=True)
        (initiative / "spec.md").write_text("# Spec\n\n## Scope\nInitial scope.\n", encoding="utf-8")
        (initiative / "decision-log.md").write_text(
            "# Decision log\n\n| ID | Decision |\n|---|---|\n| D-001 | Initial proposal. |\n",
            encoding="utf-8",
        )
        (initiative / "run-state.yaml").write_text(
            "brief_lineage: \"v2\"\nquality_gates:\n  tasks_drafted: true\n"
            "  brief_coverage_ready: true\n  human_visibility_ready: true\n"
            "  tasks_ready: false\n",
            encoding="utf-8",
        )
        events = ["meeting decision extracted"]

        # Append-only meeting record, then propagate to every affected source.
        with (initiative / "decision-log.md").open("a", encoding="utf-8") as log:
            log.write("| D-002 | Accepted scope change from meeting; propagate before Tasks Ready. |\n")
        events.append("decision appended")
        with (initiative / "spec.md").open("a", encoding="utf-8") as spec:
            spec.write("\n## Accepted meeting decision\nD-002 narrows the scope.\n")
        events.append("canonical source updated")

        regenerate_brief(initiative)
        events.append("brief regenerated")
        state = (initiative / "run-state.yaml").read_text(encoding="utf-8")
        require("tasks_ready: false" in state, "Tasks Ready was enabled before propagation/regeneration")
        require(events == [
            "meeting decision extracted", "decision appended", "canonical source updated", "brief regenerated",
        ], f"post-meeting order regressed: {events!r}")
        require("D-002" in (initiative / "stakeholder-brief.html").read_text(encoding="utf-8"), "regenerated brief missed the logged decision")

        # Only the Orchestrator may make this final state change after the flow.
        (initiative / "run-state.yaml").write_text(state.replace("tasks_ready: false", "tasks_ready: true"), encoding="utf-8")
        require("tasks_ready: true" in (initiative / "run-state.yaml").read_text(encoding="utf-8"), "Tasks Ready was not enabled after propagation/regeneration")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
