#!/usr/bin/env python3
"""Isolated fixtures for the consumer-facing Human Visibility validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "scripts" / "validate_human_visibility.py"
SOURCES = ("spec.md", "impact-map.md", "plan.md", "validation-plan.md")
V2_SOURCES = (
    "spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md",
    "decision-log.md", "progress.md", "run-state.yaml",
)


def run(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), "--consumer-root", str(root), "--initiative", "specs/001-example", *extra], text=True, capture_output=True, check=False)


def git(root: Path, *args: str) -> None:
    result = subprocess.run(["git", "-C", str(root), *args], text=True, capture_output=True, check=False)
    require(result.returncode == 0, result.stdout + result.stderr)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def write_fixture(root: Path) -> Path:
    initiative = root / "specs" / "001-example"
    initiative.mkdir(parents=True, exist_ok=True)
    for source in SOURCES:
        (initiative / source).write_text(f"# {source}\n", encoding="utf-8")
    (initiative / "run-state.yaml").write_text("quality_gates:\n  human_visibility_ready: true\n", encoding="utf-8")
    (initiative / "stakeholder-brief.html").write_text("""<html data-harness-brief-design="v1"><body class="brief-shell">
<header class="brief-header"></header><div id="decision-snapshot"></div><section id="scope"></section>
<section id="validation"></section><section id="decision"></section><section class="decision-register"></section><section class="impact-evidence"></section><section class="decision-actions"></section>
<a href="spec.md">spec</a><a href="impact-map.md">impact</a>
<a href="plan.md">plan</a><a href="validation-plan.md">validation</a>
</body></html>""", encoding="utf-8")
    return initiative


def write_v2_fixture(root: Path) -> Path:
    """A compact v2 surface with explicit provenance and review evidence."""
    initiative = root / "specs" / "001-example"
    initiative.mkdir(parents=True, exist_ok=True)
    for source in V2_SOURCES:
        (initiative / source).write_text(f"# {source}\n", encoding="utf-8")
    (initiative / "run-state.yaml").write_text("""brief_lineage: "v2"
quality_gates:
  tasks_drafted: true
  brief_coverage_ready: true
  human_visibility_ready: true
  tasks_ready: true
brief_review:
  author: "author-a"
  coverage_reviewer: "reviewer-b"
  reviewed_at: "2026-08-19"
  review_record: "decision-log.md#D-001"
  findings_status: "pass"
""", encoding="utf-8")
    (initiative / "decision-log.md").write_text("""# Decision Log

| ID | Status | Decision |
|---|---|---|
| D-001 | reviewed | Decision propagation completed before Tasks Ready. |
""", encoding="utf-8")
    blocks = "\n".join(
        f'<section id="v2-{index}" data-source="{source}" data-source-section="principal" data-coverage="represented"></section>'
        for index, source in enumerate(V2_SOURCES)
    )
    rows = "".join(f"<tr><td>{source} #principal</td><td><a href=\"#v2-{index}\">target</a></td><td>represented: fixture fact</td></tr>" for index, source in enumerate(V2_SOURCES))
    (initiative / "stakeholder-brief.html").write_text(f"""<html data-harness-brief-design="v2"><body class="brief-shell">
<header class="brief-header"></header><div id="decision-snapshot"></div>
<section id="scope"></section><section id="architecture"></section><section id="impact" class="impact-evidence"></section>
<section id="execution"></section><section id="validation"></section><section id="evolution" class="decision-register"></section>
<section id="decision" class="decision-actions"></section><section id="coverage"></section>
{blocks}<table id="coverage-register"><thead><tr><th>source</th></tr></thead><tbody>{rows}</tbody></table>
</body></html>""", encoding="utf-8")
    return initiative


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="sdd-human-visibility-") as temporary:
        root = Path(temporary)
        initiative = write_fixture(root)
        baseline = run(root, "--write-baseline")
        require(baseline.returncode == 0, baseline.stdout + baseline.stderr)
        clean = run(root)
        require(clean.returncode == 0 and "HUMAN REVIEW REQUIRED:" in clean.stdout, clean.stdout)

        (initiative / "stakeholder-brief.html").unlink()
        absent = run(root)
        require(absent.returncode == 1 and "missing stakeholder brief" in absent.stdout, absent.stdout)
        (initiative / "human-visibility-exception.yaml").write_text("scope: not_applicable\nreason: release administrative work\nowner: reviewer\nhuman_visibility_status: reviewed\n", encoding="utf-8")
        not_applicable = run(root)
        require(not_applicable.returncode == 0 and "not applicable under the explicit reviewed exception" in not_applicable.stdout, not_applicable.stdout)
        (initiative / "human-visibility-exception.yaml").unlink()
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-harness-brief-design="v1"', "", 1), encoding="utf-8")
        missing_lineage = run(root)
        require(missing_lineage.returncode == 1 and "missing stakeholder brief design-lineage marker" in missing_lineage.stdout, missing_lineage.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('class="decision-actions"', 'class="custom-actions"', 1), encoding="utf-8")
        missing_shell = run(root)
        require(missing_shell.returncode == 1 and "missing stakeholder brief canonical shell hook: decision-actions" in missing_shell.stdout, missing_shell.stdout)
        (initiative / "decision-log.md").write_text("""# Decision Log

| ID | Status | Decision | Rationale/evidence | Owner/approver |
|---|---|---|---|---|
| D-001 | reviewed | Layout exception: retained decision surfaces | Rationale: accessibility audience needs a custom layout | reviewer |
""", encoding="utf-8")
        accepted_layout = run(root)
        require(accepted_layout.returncode == 0 and "custom stakeholder brief layout accepted" in accepted_layout.stdout, accepted_layout.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('id="scope"', "", 1), encoding="utf-8")
        missing_id = run(root)
        require(missing_id.returncode == 1 and "missing stakeholder brief section id: scope" in missing_id.stdout, missing_id.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('href="plan.md"', 'href="plan-missing.md"', 1), encoding="utf-8")
        missing_link = run(root)
        require(missing_link.returncode == 1 and "missing stakeholder brief source link: plan.md" in missing_link.stdout, missing_link.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8") + "<initiative>", encoding="utf-8")
        placeholder = run(root)
        require(placeholder.returncode == 1 and "unresolved stakeholder brief placeholder" in placeholder.stdout, placeholder.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        (initiative / "impact-map.md").unlink()
        missing_source = run(root)
        require(missing_source.returncode == 1 and "missing required source artifact: impact-map.md" in missing_source.stdout, missing_source.stdout)
        write_fixture(root)
        run(root, "--write-baseline")

        (initiative / "spec.md").write_text("# changed\n", encoding="utf-8")
        stale = run(root)
        require(stale.returncode == 1 and "migrate to v2 or record a reviewed legacy exception" in stale.stdout, stale.stdout)
        (initiative / "human-visibility-exception.yaml").write_text("scope: legacy\nreason: pinned historical brief\nowner: reviewer\nhuman_visibility_status: reviewed\n", encoding="utf-8")
        legacy = run(root)
        require(legacy.returncode == 0 and "accepted by explicit reviewed freshness exception" in legacy.stdout, legacy.stdout)
        (initiative / "human-visibility-exception.yaml").write_text("scope: freshness # documented inline comment\nreason: formatting only\nowner: reviewer\nhuman_visibility_status: reviewed\n", encoding="utf-8")
        exception = run(root)
        require(exception.returncode == 0 and "accepted by explicit reviewed freshness exception" in exception.stdout, exception.stdout)

    with tempfile.TemporaryDirectory(prefix="sdd-human-visibility-git-") as temporary:
        root = Path(temporary)
        initiative = write_fixture(root)
        baseline = run(root, "--write-baseline")
        require(baseline.returncode == 0, baseline.stdout + baseline.stderr)
        git(root, "init")
        git(root, "config", "user.email", "fixture@example.test")
        git(root, "config", "user.name", "Fixture")
        git(root, "add", ".")
        git(root, "commit", "-m", "baseline")
        (initiative / "spec.md").write_text("# changed\n", encoding="utf-8")
        stale_git = run(root, "--base-ref", "HEAD")
        require(stale_git.returncode == 1 and "was not refreshed in Git diff" in stale_git.stdout, stale_git.stdout)
        (initiative / "stakeholder-brief.html").write_text((initiative / "stakeholder-brief.html").read_text(encoding="utf-8") + "<!-- refreshed -->", encoding="utf-8")
        refreshed_git = run(root, "--base-ref", "HEAD")
        require(refreshed_git.returncode == 0, refreshed_git.stdout)
        baseline_after_refresh = run(root, "--write-baseline")
        require(baseline_after_refresh.returncode == 0, baseline_after_refresh.stdout + baseline_after_refresh.stderr)
        fallback_git = run(root, "--base-ref", "missing-ref")
        require(fallback_git.returncode == 0 and "falling back to human-visibility-baseline.json" in fallback_git.stdout, fallback_git.stdout)

    with tempfile.TemporaryDirectory(prefix="sdd-human-visibility-v2-") as temporary:
        root = Path(temporary)
        initiative = write_v2_fixture(root)
        baseline = run(root, "--write-baseline")
        require(baseline.returncode == 0, baseline.stdout + baseline.stderr)
        clean = run(root)
        require(clean.returncode == 0 and "does not replace the required independent" in clean.stdout, clean.stdout)
        baseline_payload = json.loads((initiative / "human-visibility-baseline.json").read_text(encoding="utf-8"))
        require(baseline_payload["schema_version"] == 2 and baseline_payload["brief_lineage"] == "v2", str(baseline_payload))
        require(baseline_payload["source_set"] == list(V2_SOURCES), str(baseline_payload))
        require(
            all(baseline_payload.get(key) for key in ("reviewed_by", "reviewed_at", "coverage_reviewer", "prior_change_anchor")),
            str(baseline_payload),
        )

        (initiative / "tasks.md").unlink()
        missing_tasks = run(root)
        require(missing_tasks.returncode == 1 and "missing required source artifact: tasks.md" in missing_tasks.stdout, missing_tasks.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-source-section="principal"', 'data-source-section=""', 1), encoding="utf-8")
        missing_provenance = run(root)
        require(missing_provenance.returncode == 1 and "v2 provenance missing data-source-section for source spec.md" in missing_provenance.stdout, missing_provenance.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace("<td>tasks.md #principal</td>", "<td>omitted-source.md #principal</td>", 1), encoding="utf-8")
        missing_heading = run(root)
        require(missing_heading.returncode == 1 and "missing v2 coverage register entry: tasks.md" in missing_heading.stdout, missing_heading.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace("<td>tasks.md #principal</td>", "<td>tasks.md</td>", 1), encoding="utf-8")
        heading_locator = run(root)
        require(heading_locator.returncode == 1 and "v2 coverage row missing heading locator for source tasks.md" in heading_locator.stdout, heading_locator.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('href="#v2-3"', 'href="#missing-target"', 1), encoding="utf-8")
        target = run(root)
        require(target.returncode == 1 and "v2 coverage row target does not resolve for source tasks.md" in target.stdout, target.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace("represented: fixture fact</td>", "invented: fixture fact</td>", 1), encoding="utf-8")
        row_enum = run(root)
        require(row_enum.returncode == 1 and "v2 coverage row has invalid disposition for source spec.md" in row_enum.stdout, row_enum.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace("represented: fixture fact</td>", "link_only:</td>", 1), encoding="utf-8")
        row_reason = run(root)
        require(row_reason.returncode == 1 and "v2 coverage row missing reason for source spec.md" in row_reason.stdout, row_reason.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        state = initiative / "run-state.yaml"
        state.write_text(state.read_text(encoding="utf-8").replace('coverage_reviewer: "reviewer-b"', 'coverage_reviewer: "author-a"'), encoding="utf-8")
        same_reviewer = run(root)
        require(same_reviewer.returncode == 1 and "must be distinct identities" in same_reviewer.stdout, same_reviewer.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        state = initiative / "run-state.yaml"
        state.write_text(state.read_text(encoding="utf-8").replace("decision-log.md#D-001", "decision-log.md#D-404"), encoding="utf-8")
        missing_review = run(root)
        require(missing_review.returncode == 1 and "does not resolve in decision-log.md" in missing_review.stdout, missing_review.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-source="spec.md" data-source-section="principal" data-coverage="represented"', 'data-source="spec.md" data-source-section="principal" data-coverage="link_only"', 1), encoding="utf-8")
        core_link_only = run(root)
        require(core_link_only.returncode == 1 and "v2 core source cannot be link_only: spec.md" in core_link_only.stdout, core_link_only.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        (initiative / "tasks.md").write_text("# changed tasks\n", encoding="utf-8")
        stale_v2 = run(root)
        require(stale_v2.returncode == 1 and "v2 stakeholder brief is stale for changed source artifact(s): tasks.md" in stale_v2.stdout, stale_v2.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        baseline_path = initiative / "human-visibility-baseline.json"
        baseline_payload = json.loads(baseline_path.read_text(encoding="utf-8"))
        baseline_payload["schema_version"] = 1
        baseline_path.write_text(json.dumps(baseline_payload), encoding="utf-8")
        migration = run(root)
        require(migration.returncode == 1 and "v2 migration required: freshness baseline must use schema_version 2" in migration.stdout, migration.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        baseline_path = initiative / "human-visibility-baseline.json"
        baseline_payload = json.loads(baseline_path.read_text(encoding="utf-8"))
        del baseline_payload["reviewed_by"]
        baseline_path.write_text(json.dumps(baseline_payload), encoding="utf-8")
        metadata = run(root)
        require(metadata.returncode == 1 and "v2 freshness baseline metadata changed or missing: reviewed_by" in metadata.stdout, metadata.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        decision = initiative / "decision-log.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("Decision propagation completed", "Review completed").replace("</nothing>", "") + "| D-002 | reviewed | Decision propagation appears elsewhere. |\n", encoding="utf-8")
        false_positive = run(root)
        require(false_positive.returncode == 1 and "v2 Tasks Ready review record does not confirm decision propagation" in false_positive.stdout, false_positive.stdout)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        sentinel = "PRIVATE_SENTINEL_DO_NOT_EMIT"
        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-source="tasks.md"', f'data-source="{sentinel}"', 1), encoding="utf-8")
        privacy = run(root)
        require(privacy.returncode == 1 and "unknown v2 provenance source" in privacy.stdout and sentinel not in privacy.stdout, privacy.stdout)
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
