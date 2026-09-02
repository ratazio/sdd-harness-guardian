#!/usr/bin/env python3
"""Guard the structural visual commitment introduced by SPEC 025 T-005.

The checks deliberately verify route, slot and component presence only. They do
not decide whether prose, a diagram or a visual hierarchy is good; that remains
the responsibility of an independent desktop review.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / ".harness" / "templates" / "stakeholder-brief.html"
SKELETON = ROOT / "specs" / "025-brief-composition-handoff-skeleton" / "brief-candidates" / "stakeholder-brief.skeleton.html"
ROUTES = ("scope", "architecture", "impact", "execution", "validation", "evolution", "decision", "coverage")
SKELETON_IDS = (
    "scope-outcome", "scope-boundary", "architecture-landscape", "architecture-relationship-flow", "architecture-assurance",
    "architecture-state", "impact-footprint", "impact-risks", "impact-rollback",
    "impact-lab-boundary", "task-T-001", "task-T-002", "task-T-003", "task-T-004", "task-T-005",
    "proof-V-025-01", "proof-V-025-02", "proof-V-025-03", "proof-V-025-04",
    "proof-V-025-05", "proof-V-025-06", "proof-V-025-07", "proof-V-025-08", "proof-V-025-09",
    "validation-guarantees", "evolution-decisions", "evolution-state", "decision-call",
    "decision-audience", "coverage-register",
)


class Surface(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tabs: list[dict[str, str]] = []
        self.panels: list[dict[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
        if values.get("role") == "tab":
            self.tabs.append(values)
        if values.get("role") == "tabpanel":
            self.panels.append(values)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    template = TEMPLATE.read_text(encoding="utf-8")
    skeleton = SKELETON.read_text(encoding="utf-8")

    template_surface = Surface()
    template_surface.feed(template)
    skeleton_surface = Surface()
    skeleton_surface.feed(skeleton)

    require('data-harness-brief-structure="executive-brief-v3"' in template, "template structure version missing")
    require('data-harness-brief-structure="executive-brief-v3"' in skeleton, "skeleton does not declare template structure version")
    for token in (
        "route-hero", "topology", "brief-architecture-cut", "brief-impact-footprint",
        "brief-risk-chain", "brief-task-card", "brief-proof-card", "brief-decision-call",
        "brief-coverage-group", "data-repeat=\"task\"", "data-repeat=\"validation\"",
    ):
        require(token in template, f"template lost visual component contract: {token}")

    require('data-harness-template-kind="skeleton"' in skeleton, "skeleton identity missing")
    require('data-brief-phase="skeleton"' in skeleton, "skeleton lifecycle phase missing")
    require('data-client-identity-profile="pearson"' in skeleton, "SPEC 025 selected profile missing")
    require('data-harness-pearson-shell' in skeleton, "selected visual shell missing")
    require('data-harness-brief-profile-template="pearson-selected"' in skeleton, "selected profile lineage missing")
    require("a preencher" in skeleton, "skeleton must visibly retain unfinished slots")
    require("scrollIntoView" not in skeleton, "skeleton routes must not be anchor scrolling")
    require(
        ".brief-route[hidden]" in template and "display: none" in template,
        "current template routes must visually hide inactive runtime panels",
    )
    for token in ("history.pushState", "popstate", "beforeprint", "afterprint"):
        require(token in skeleton, f"skeleton route behaviour missing: {token}")
    require(
        re.search(r"routes\[index\]\.hidden\s*=\s*!selected", skeleton) is not None,
        "skeleton route behaviour missing: panel visibility toggle",
    )

    for name, surface in (("template", template_surface), ("skeleton", skeleton_surface)):
        require(len(surface.tabs) == len(ROUTES), f"{name}: expected {len(ROUTES)} tabs, got {len(surface.tabs)}")
        require(len(surface.panels) == len(ROUTES), f"{name}: expected {len(ROUTES)} panels, got {len(surface.panels)}")
        require(tuple(panel.get("id", "") for panel in surface.panels) == ROUTES, f"{name}: route order drifted")

    require(
        tuple(tab.get("id", "") for tab in template_surface.tabs)
        == tuple(tab.get("id", "") for tab in skeleton_surface.tabs),
        "template and skeleton tab identities diverged",
    )
    require(
        tuple(tab.get("aria-controls", "") for tab in template_surface.tabs)
        == tuple(tab.get("aria-controls", "") for tab in skeleton_surface.tabs),
        "template and skeleton route bindings diverged",
    )
    panel_ids = {panel.get("id", "") for panel in skeleton_surface.panels}
    for tab in skeleton_surface.tabs:
        route = tab.get("aria-controls", "")
        require(route in panel_ids, f"tab {tab.get('id')} does not control a route")
        require(tab.get("href") == f"?view={route}", f"tab {tab.get('id')} route target drifted")
    for target in SKELETON_IDS:
        require(target in skeleton_surface.ids, f"skeleton lost planned visual target: #{target}")
    for target in ("architecture-landscape", "architecture-relationship-flow"):
        require(target in template_surface.ids, f"template lost architecture model: #{target}")

    # The neutral shell and selected-profile instance may differ in logo and
    # lifecycle, but must retain the same visual information architecture.
    template_components = (
        "route-hero", "topology", "brief-architecture-cut", "brief-impact-footprint",
        "brief-risk-chain", "epics", "brief-task-card", "validation-flow",
        "brief-proof-card", "matrix", "timeline", "gateboard", "brief-decision-call",
        "brief-coverage-group",
    )
    skeleton_components = (
        "hero", "topology", "zoom", "footprint", "riskchain", "epics", "task",
        "validation-flow", "proof", "matrix", "timeline", "gateboard", "decision-call",
        "guarantees",
    )
    for token in template_components:
        require(token in template, f"template lost component family: {token}")
    for token in skeleton_components:
        require(token in skeleton, f"skeleton failed to materialize component family: {token}")

    print("SPEC 025 visual skeleton contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
