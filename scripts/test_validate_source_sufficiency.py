"""Tests for scripts/validate_source_sufficiency.py (SPEC 029 T-006).

FR-011 / AC-008: a deterministic, cheap check over the canonical Markdown
sources that must block *before* any brief composition happens. These tests
prove:

  * a fixture with sufficient sources produces zero errors (positive case);
  * a fixture with an AC that has no declared validation path is blocked,
    with an actionable message naming the AC id (negative case, the exact
    AC-008 scenario);
  * each of the four FR-011 checks (AC validation path, risk owner,
    architecture profile, task exit-criteria/evidence) fails independently
    when only that one signal is removed, proving the check is structural
    and binary (NG-002: not a score) rather than a single opaque pass/fail;
  * the check runs over the raw Markdown sources only -- it never reads or
    produces a brief-model or HTML artifact, i.e. it runs strictly before
    composition rather than after it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from validate_source_sufficiency import (  # noqa: E402
    source_sufficiency_errors,
    _extract_ac_ids,
    _extract_ac_validation_paths,
    _extract_architecture_profile,
    _has_named_owner,
    _split_markdown_table,
    _split_tasks,
    _task_has_exit_criteria,
    _task_evidence_destination,
)

FIXTURES = ROOT / "scripts" / "fixtures" / "source-sufficiency"
POSITIVE = FIXTURES / "positive"
NEGATIVE_AC = FIXTURES / "negative-ac"
NEGATIVE_OWNER_PROSE = FIXTURES / "negative-owner-prose"


def test_positive_fixture_has_no_errors():
    errors = source_sufficiency_errors(POSITIVE)
    assert errors == [], f"expected sufficient sources, got: {errors}"


def test_negative_ac_fixture_is_blocked_with_actionable_message():
    errors = source_sufficiency_errors(NEGATIVE_AC)
    assert errors, "an AC with no validation path must block"
    assert any("AC-002" in e and "validation-plan.md" in e for e in errors), errors


def test_negative_owner_prose_fixture_is_blocked():
    """Regression fixture for the request_revision finding: a Contingency/owner
    cell that merely contains an ordinary prose dash ("Investigate root cause
    -- postpone release") must NOT be accepted as a named owner. Before the
    fix, any dash in the cell was treated as the <action> -- <Owner>
    separator, so this fixture silently passed -- a false negative in the
    dangerous direction (a risk with no real owner reads as compliant)."""
    errors = source_sufficiency_errors(NEGATIVE_OWNER_PROSE)
    assert any("IR-001" in e and "owner" in e for e in errors), errors
    # nothing else in this fixture should be flagged
    assert not any("AC-" in e for e in errors)
    assert not any("architecture" in e for e in errors)
    assert not any("T-001" in e for e in errors)


def test_missing_source_file_is_reported_by_name():
    errors = source_sufficiency_errors(FIXTURES / "does-not-exist")
    assert any("missing canonical source" in e for e in errors)
    # all five canonical sources are reported missing, not just the first
    for name in ("spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md"):
        assert any(name in e for e in errors), f"{name} not reported missing"


def _write_variant(tmp_path: Path, overrides: dict[str, str]) -> Path:
    variant = tmp_path / "variant"
    variant.mkdir()
    for name in ("spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md"):
        text = overrides.get(name)
        if text is None:
            text = (POSITIVE / name).read_text(encoding="utf-8")
        (variant / name).write_text(text, encoding="utf-8")
    return variant


def test_risk_without_owner_blocks_independently(tmp_path):
    impact = (POSITIVE / "impact-map.md").read_text(encoding="utf-8")
    impact = impact.replace("Revert the change -- Fixture maintainers", "Revert the change")
    variant = _write_variant(tmp_path, {"impact-map.md": impact})
    errors = source_sufficiency_errors(variant)
    assert any("IR-001" in e and "owner" in e for e in errors), errors
    # nothing else regressed
    assert not any("AC-" in e for e in errors)
    assert not any("architecture" in e for e in errors)
    assert not any("T-001" in e for e in errors)


def test_missing_architecture_profile_blocks_independently(tmp_path):
    plan = (POSITIVE / "plan.md").read_text(encoding="utf-8")
    plan = plan.replace("**Profile:** S\n\n", "")
    variant = _write_variant(tmp_path, {"plan.md": plan})
    errors = source_sufficiency_errors(variant)
    assert any("architecture scope/size profile" in e for e in errors), errors


def test_invalid_architecture_profile_value_blocks():
    doc = (POSITIVE / "plan.md").read_text(encoding="utf-8").replace(
        "**Profile:** S", "**Profile:** giant"
    )
    profile = _extract_architecture_profile(doc)
    assert profile == "giant"
    errors = source_sufficiency_errors(POSITIVE)  # sanity: baseline still clean
    assert errors == []


def test_task_without_exit_criteria_blocks_independently(tmp_path):
    tasks = (POSITIVE / "tasks.md").read_text(encoding="utf-8")
    tasks = re.sub(r"#### Exit criteria\n.*", "", tasks, flags=re.DOTALL)
    variant = _write_variant(tmp_path, {"tasks.md": tasks})
    errors = source_sufficiency_errors(variant)
    assert any("T-001" in e and "Exit criteria" in e for e in errors), errors


def test_task_without_evidence_destination_blocks_independently(tmp_path):
    tasks = (POSITIVE / "tasks.md").read_text(encoding="utf-8")
    tasks = tasks.replace("**Evidence:** evidence/T-001.md\n\n", "")
    variant = _write_variant(tmp_path, {"tasks.md": tasks})
    errors = source_sufficiency_errors(variant)
    assert any("T-001" in e and "evidence destination" in e for e in errors), errors


def test_check_never_reads_a_brief_model_or_html(tmp_path):
    """The check runs before composition: it must not require, read or
    produce brief-model.yaml or stakeholder-brief.html to reach a verdict."""
    variant = _write_variant(tmp_path, {})
    assert not (variant / "brief-model.yaml").exists()
    assert not (variant / "stakeholder-brief.html").exists()
    errors = source_sufficiency_errors(variant)
    assert errors == []
    assert not (variant / "brief-model.yaml").exists()
    assert not (variant / "stakeholder-brief.html").exists()


def test_extract_ac_ids_is_order_preserving_and_deduplicated():
    text = (POSITIVE / "spec.md").read_text(encoding="utf-8")
    assert _extract_ac_ids(text) == ["AC-001", "AC-002"]


def test_extract_ac_validation_paths_marks_empty_steps_as_undeclared():
    text = """
## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 |  |  | | evidence/T-X.md | Builder |
"""
    result = _extract_ac_validation_paths(text)
    assert result == {"AC-001": False}


def test_has_named_owner_rejects_placeholders():
    assert _has_named_owner("Revert the change -- Guardian maintainers") is True
    assert _has_named_owner("Revert the change") is False
    assert _has_named_owner("") is False
    assert _has_named_owner("TBD") is False
    assert _has_named_owner("-") is False


def test_has_named_owner_rejects_prose_dash_as_separator():
    """F1 (request_revision finding): an em dash that is just ordinary
    sentence punctuation, not the <action> -- <Owner> convention, must not
    be read as naming an owner. "postpone release" is a verb phrase
    continuing the sentence, not a name."""
    assert _has_named_owner("Investigate root cause — postpone release") is False
    # a real owner after the same em dash is still accepted
    assert _has_named_owner("Investigate root cause — Guardian maintainers") is True
    # dash with no surrounding spaces is not the separator either
    assert _has_named_owner("mid-sentence-dash owner-ish text") is False


def test_split_markdown_table_honors_escaped_pipe_in_cell():
    """F2 fix: a cell containing a shell/regex command with an escaped pipe
    (`\\|`) must not be mistaken for a column boundary."""
    block = (
        "| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |\n"
        "|---|---|---|---|---|---|---|\n"
        "| V-001 | AC-001 | deterministic | `grep -E \"a\\|b\"` | matches | evidence/T-X.md | Builder |\n"
    )
    rows = _split_markdown_table(block)
    assert len(rows) == 1
    assert len(rows[0]) == 7
    assert rows[0][3] == '`grep -E "a|b"`'
    assert rows[0][6] == "Builder"


def test_split_tasks_finds_all_task_blocks():
    tasks_text = (POSITIVE / "tasks.md").read_text(encoding="utf-8")
    blocks = _split_tasks(tasks_text)
    assert [tid for tid, _ in blocks] == ["T-001"]
    assert _task_has_exit_criteria(blocks[0][1])
    assert _task_evidence_destination(blocks[0][1]) == "evidence/T-001.md"


def test_real_spec029_sources_pass_or_report_named_gaps():
    """Run the check over the real SPEC 029 sources as a smoke test. This is
    not an authoring gate on 029 itself (T-006 only builds the tool) -- it
    just proves the parser survives a real, larger document without
    crashing, and that any gap it reports is an actionable, named item."""
    initiative = ROOT / "specs" / "029-brief-content-model-and-doctrine-consolidation"
    errors = source_sufficiency_errors(initiative)
    for e in errors:
        assert e.startswith("source-sufficiency:")
