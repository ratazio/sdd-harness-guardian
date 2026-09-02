#!/usr/bin/env python3
"""Verify stable, non-semantic contracts of the v2 tabbed brief surface.

This intentionally checks markup and fallback invariants only. It does not
score wording, infer missing source facts, or decide whether a brief is useful;
those questions remain with the independent rendered review.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
TARGETS = (
    ".harness/templates/stakeholder-brief.html",
    "scripts/fixtures/tabbed-brief-surface/reference-v2.html",
)
TAB_IDS = (
    "tab-scope", "tab-architecture", "tab-impact", "tab-execution",
    "tab-validation", "tab-evolution", "tab-decision", "tab-coverage",
)


class SurfaceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tabs: list[dict[str, str]] = []
        self.panels: list[dict[str, str]] = []
        self.tablists: list[dict[str, str]] = []
        self.snapshot_panel_ids: list[str | None] = []
        self._stack: list[tuple[str, dict[str, str]]] = []
        self._tab_parts: list[str] | None = None
        self._tab_attrs: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        if values.get("id") == "decision-snapshot":
            parent_panel = next(
                (parent for _, parent in reversed(self._stack) if parent.get("role") == "tabpanel"),
                None,
            )
            self.snapshot_panel_ids.append(parent_panel.get("id") if parent_panel else None)
        if values.get("role") == "tablist":
            self.tablists.append(values)
        if values.get("role") == "tab":
            self._tab_parts = []
            self._tab_attrs = values
        if values.get("role") == "tabpanel":
            self.panels.append(values)
        self._stack.append((tag, values))

    def handle_data(self, data: str) -> None:
        if self._tab_parts is not None:
            self._tab_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._tab_attrs is not None and self._tab_parts is not None:
            self._tab_attrs["label"] = " ".join("".join(self._tab_parts).split())
            self.tabs.append(self._tab_attrs)
            self._tab_parts = None
            self._tab_attrs = None
        for index in range(len(self._stack) - 1, -1, -1):
            if self._stack[index][0] == tag:
                del self._stack[index:]
                break


def errors_for(relative: str, text_override: str | None = None) -> list[str]:
    path = ROOT / relative
    text = text_override if text_override is not None else path.read_text(encoding="utf-8")
    parser = SurfaceParser()
    parser.feed(text)
    errors: list[str] = []

    if 'data-harness-brief-design="v2"' not in text:
        errors.append("missing v2 lineage marker")
    if len(parser.tabs) != 8:
        errors.append(f"expected 8 tabs, found {len(parser.tabs)}")
    if len(parser.panels) != 8:
        errors.append(f"expected 8 tabpanels, found {len(parser.panels)}")
    tab_ids = tuple(tab.get("id", "") for tab in parser.tabs)
    if tab_ids != TAB_IDS:
        errors.append(f"unexpected tab order/ids: {tab_ids!r}")

    panel_by_id = {panel.get("id", ""): panel for panel in parser.panels}
    for tab in parser.tabs:
        control = tab.get("aria-controls", "")
        panel = panel_by_id.get(control)
        if not control or panel is None:
            errors.append(f"tab {tab.get('label', '?')!r} lacks a resolvable aria-controls panel")
        elif "hidden" in panel:
            errors.append(f"panel {control!r} is statically hidden; fallback must remain complete")
        elif "brief-route" not in panel.get("class", "").split():
            errors.append(f"panel {control!r} is not declared as a complete internal route")
        if tab.get("href") != f"?view={control}":
            errors.append(f"tab {tab.get('label', '?')!r} has inconsistent internal route target")

    if len(parser.tablists) != 1:
        errors.append("expected exactly one tablist")
    if 'data-tab-enhancement="fallback"' not in text:
        errors.append("missing pre-enhancement fallback state")
    if relative == TARGETS[0] and 'data-noscript-fallback="continuous-reading"' not in text:
        errors.append("missing honest no-script continuous-reading notice")
    if "@media print" not in text or not re.search(
        r"\.tab-panel\[hidden\]\s*\{\s*display\s*:\s*block\s*!important\s*;?\s*\}",
        text,
    ):
        errors.append("missing print rule that reveals runtime-hidden panels")
    if "<script src=" in text or "<script src='" in text:
        errors.append("external script is not allowed for the offline surface")
    if not re.search(r"panels\[index\]\.hidden\s*=\s*!selected", text):
        errors.append("missing progressive-enhancement contract: panel visibility toggle")
    for token in ("aria-current", "history.pushState", "popstate", "ArrowRight", "ArrowLeft", "beforeprint", "afterprint"):
        if token not in text:
            errors.append(f"missing progressive-enhancement contract: {token}")
    if "scrollIntoView" in text:
        errors.append("primary route surface must not scroll to an anchor")
    if len(parser.snapshot_panel_ids) != 1:
        errors.append(f"expected exactly one decision snapshot, found {len(parser.snapshot_panel_ids)}")
    elif parser.snapshot_panel_ids[0] != "scope":
        errors.append("decision snapshot must be nested in the Scope route")
    return errors


def main() -> int:
    failures: list[str] = []
    for relative in TARGETS:
        for error in errors_for(relative):
            failures.append(f"{relative}: {error}")
    template = (ROOT / TARGETS[0]).read_text(encoding="utf-8")
    missing = re.sub(r'\s+id="decision-snapshot"', "", template, count=1)
    if not any("expected exactly one decision snapshot" in error for error in errors_for(TARGETS[0], missing)):
        failures.append("negative missing-snapshot case was not rejected")
    scope_start = template.find('id="scope"')
    scope_role = template.find('role="tabpanel"', scope_start)
    if min(scope_start, scope_role) < 0:
        failures.append("negative outside-snapshot fixture could not be constructed")
    else:
        outside = template[:scope_role] + 'role="section"' + template[scope_role + len('role="tabpanel"'):]
        if not any("decision snapshot must be nested" in error for error in errors_for(TARGETS[0], outside)):
            failures.append("negative outside-snapshot case was not rejected")
    if failures:
        print("Tabbed brief surface contract failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Tabbed brief surface contracts passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
