#!/usr/bin/env python3
"""Regression checks for the non-authoring candidate inheritance guard."""

from __future__ import annotations

import tempfile
import hashlib
from pathlib import Path

from validate_brief_candidate_inheritance import errors


ROOT = Path(__file__).resolve().parent.parent
SKELETON = ROOT / "specs" / "025-brief-composition-handoff-skeleton" / "brief-candidates" / "stakeholder-brief.skeleton.html"
CANDIDATE = ROOT / "specs" / "025-brief-composition-handoff-skeleton" / "brief-candidates" / "stakeholder-brief.candidate.html"
TEMPLATE = ROOT / ".harness" / "templates" / "stakeholder-brief.html"


def marked_skeleton_case(directory: Path) -> tuple[Path, Path, Path]:
    initiative = directory / "initiative"
    skeleton = initiative / "brief-candidates" / "stakeholder-brief.skeleton.html"
    skeleton.parent.mkdir(parents=True)
    skeleton.write_bytes(TEMPLATE.read_bytes())
    skeleton_text = skeleton.read_text(encoding="utf-8")
    candidate = initiative / "brief-candidates" / "stakeholder-brief.candidate.html"
    candidate_text = skeleton_text.replace('data-harness-template-kind="scaffold"', 'data-harness-template-kind="composed"').replace(
        'data-brief-phase="scaffold"', 'data-brief-phase="authored"'
    )
    candidate_text = candidate_text.replace(
        'data-composition-extension="inside-slot-only"',
        'data-composition-extension="inside-slot-only"\n  data-composition-base="brief-candidates/stakeholder-brief.skeleton.html"\n  data-composition-base-sha256="'
        + hashlib.sha256(skeleton.read_bytes()).hexdigest()
        + '"',
    )
    head, body = candidate_text.split("</style>", 1)
    candidate_text = head + "</style>" + body.replace("a preencher", "source-backed")
    candidate.write_text(candidate_text, encoding="utf-8")
    return initiative, skeleton, candidate


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        fixture_root = Path(directory)
        marked_initiative, marked_skeleton, in_situ = marked_skeleton_case(fixture_root)
        assert errors(in_situ, marked_skeleton, marked_initiative) == [], errors(in_situ, marked_skeleton, marked_initiative)

        signed_candidate = marked_initiative / "brief-candidates" / "signed-candidate.html"
        signed_candidate.write_text(
            in_situ.read_text(encoding="utf-8").replace(
                'data-composition-base="brief-candidates/stakeholder-brief.skeleton.html"',
                'data-composition-review-record="D-900" data-composition-provenance="reviewed" '
                'data-composition-base="brief-candidates/stakeholder-brief.skeleton.html"',
                1,
            ),
            encoding="utf-8",
        )
        assert errors(signed_candidate, marked_skeleton, marked_initiative) == [], errors(
            signed_candidate, marked_skeleton, marked_initiative
        )

        provenance_on_slot = marked_initiative / "brief-candidates" / "provenance-on-slot.html"
        provenance_on_slot.write_text(
            in_situ.read_text(encoding="utf-8").replace(
                'data-composition-slot="scope-route-title"',
                'data-composition-slot="scope-route-title" data-source="spec.md"',
                1,
            ),
            encoding="utf-8",
        )
        findings = errors(provenance_on_slot, marked_skeleton, marked_initiative)
        assert any("provenance directly to an immutable composition slot" in finding for finding in findings), findings

        legacy_findings = errors(CANDIDATE, SKELETON)
        assert any("lacks the immutable shell contract" in finding for finding in legacy_findings), legacy_findings

        outside_slot_skeleton = marked_initiative / "brief-candidates" / "outside-slot-skeleton.html"
        outside_slot_skeleton.write_text(
            marked_skeleton.read_text(encoding="utf-8").replace(
                'class="question slot"', 'class="question"', 1
            ),
            encoding="utf-8",
        )
        findings = errors(in_situ, outside_slot_skeleton, marked_initiative)
        assert any("outside a composition slot" in finding for finding in findings), findings

        # A source package may legitimately have more than the template's
        # illustrative task count. The parent dossier container, rather than
        # a fixed child card, is the composable unit.
        multi_task = marked_initiative / "brief-candidates" / "multi-task.html"
        task_anchor = (
            '            </dl>\n'
            '          </article>\n'
            '        </div>\n'
            '      </section>\n'
            '      <section\n'
            '        id="validation"'
        )
        extra_task = (
            '            </dl>\n'
            '          </article>\n'
            '          <article class="brief-task-card"><h3>T-006 — source-backed additional increment</h3>'
            '<p>Independent outcome, boundary and proof.</p></article>\n'
            '        </div>\n'
            '      </section>\n'
            '      <section\n'
            '        id="validation"'
        )
        multi_text = in_situ.read_text(encoding="utf-8")
        assert task_anchor in multi_text
        multi_task.write_text(multi_text.replace(task_anchor, extra_task, 1), encoding="utf-8")
        assert errors(multi_task, marked_skeleton, marked_initiative) == [], errors(multi_task, marked_skeleton, marked_initiative)

        slot_placeholder = marked_initiative / "brief-candidates" / "slot-placeholder.html"
        slot_placeholder.write_text(
            in_situ.read_text(encoding="utf-8").replace(
                "source-backed — beneficiary", "source-backed detail — beneficiary", 1
            ),
            encoding="utf-8",
        )
        findings = errors(slot_placeholder, marked_skeleton, marked_initiative)
        assert any("raw scaffold placeholder" in finding for finding in findings), findings

        # It carries the declared base, hash and the familiar route IDs, but
        # replaces the physical shell with a small parallel page.
        parallel = marked_initiative / "brief-candidates" / "parallel.html"
        route_markup = "".join(
            f'<a class="route-nav" role="tab" aria-controls="{route}">{route}</a><section id="{route}" role="tabpanel"></section>'
            for route in ("scope", "architecture", "impact", "execution", "validation", "evolution", "decision", "coverage")
        )
        parallel.write_text(
            '<html data-harness-template-kind="composed" data-brief-phase="authored" '
            'data-harness-brief-structure="executive-brief-v3" data-harness-brief-design="v2" '
            'data-client-identity-profile="vendor-neutral" data-brief-shell-contract="v1" '
            'data-composition-slot-class="slot" data-composition-extension="inside-slot-only" '
            'data-composition-base="brief-candidates/stakeholder-brief.skeleton.html" '
            f'data-composition-base-sha256="{hashlib.sha256(marked_skeleton.read_bytes()).hexdigest()}">' + route_markup + '</html>',
            encoding="utf-8",
        )
        findings = errors(parallel, marked_skeleton, marked_initiative)
        assert any("base stylesheet" in finding for finding in findings), findings
        assert any("base navigation behavior" in finding for finding in findings), findings
        assert any("immutable skeleton shell" in finding for finding in findings), findings

        miniature = Path(directory) / "parallel.html"
        miniature.write_text(
            '<html data-harness-template-kind="composed" data-brief-phase="authored" '
            'data-harness-brief-structure="executive-brief-v3"></html>', encoding="utf-8"
        )
        findings = errors(miniature, marked_skeleton, marked_initiative)
        assert any("immutable skeleton shell" in finding for finding in findings), findings
        assert any("SHA-256" in finding for finding in findings), findings
        duplicate = Path(directory) / "duplicate.html"
        duplicate.write_text(
            '<html data-harness-template-kind="composed" data-brief-phase="authored" '
            'data-harness-brief-structure="executive-brief-v3"><div id="x"></div><span id="x"></span></html>',
            encoding="utf-8",
        )
        findings = errors(duplicate, marked_skeleton, marked_initiative)
        assert any("duplicate IDs" in finding for finding in findings), findings
        unfinished = Path(directory) / "unfinished.html"
        unfinished.write_text(
            '<html data-harness-template-kind="composed" data-brief-phase="authored" '
            'data-harness-brief-structure="executive-brief-v3">Composição M-099</html>', encoding="utf-8"
        )
        findings = errors(unfinished, marked_skeleton, marked_initiative)
        assert any("raw scaffold placeholder" in finding for finding in findings), findings
    print("Brief candidate inheritance guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
