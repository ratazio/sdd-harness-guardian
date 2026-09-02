#!/usr/bin/env python3
"""Isolated fixtures for the consumer-facing Human Visibility validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import hashlib
import json
import re
from pathlib import Path

from validate_human_visibility import Report, check_v2_provenance, decision_record
from brief_v2_sources import V2_REQUIRED_SOURCES


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "scripts" / "validate_human_visibility.py"
SOURCES = ("spec.md", "impact-map.md", "plan.md", "validation-plan.md")
V2_SOURCES = V2_REQUIRED_SOURCES

# T-001 grammar inventory.  These helpers are test-fixture oracles, not
# production validation code; T-003 will implement the approved subset in the
# validator.  The boundary keeps product specs free to use arbitrary prose:
# only the two explicit contract forms below create a future obligation.
RISK_TABLE_ROW = re.compile(r"^\|\s*(IR-[A-Za-z0-9][A-Za-z0-9_-]*)\s*\|.+\|\s*$")
HTTP_ROUTE = re.compile(
    r"\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(/api/[A-Za-z0-9._~!$&'()*+,;=:@%{}\-/]+)(?:\?[^`|\s]*)?"
)


def inventory_risk_ids(impact_map: str) -> set[str]:
    """Return only first-column IR IDs from Markdown table rows."""
    return {match.group(1) for line in impact_map.splitlines() if (match := RISK_TABLE_ROW.match(line))}


def inventory_http_routes(plan: str) -> set[str]:
    """Return routes from explicit table/list contract syntax, never prose.

    A table is a contract only under an API/contract heading or when its header
    explicitly names a Route or Method column.  This permits diverse plans
    without treating a roadmap, example matrix or narrative table as an API.
    """
    routes: set[str] = set()
    in_contract_heading = False
    table_contract = False
    for line in plan.splitlines():
        if not line.strip():
            table_contract = False
            continue
        heading = re.match(r"^#{1,6}\s+(.+)$", line)
        if heading:
            in_contract_heading = bool(re.search(r"\b(api|contract)s?\b", heading.group(1), re.IGNORECASE))
            table_contract = False
            continue
        is_table = line.lstrip().startswith("|")
        if is_table:
            cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
            is_separator = all(not cell or set(cell) <= {"-", ":", " "} for cell in cells)
            has_contract_column = any(re.fullmatch(r"(?:api )?(?:route|method)", cell) for cell in cells)
            # An API/contract heading supplies the context even when authors
            # choose a domain-appropriate header such as Endpoint.  Outside
            # that context, retain the explicit Route/Method header boundary.
            if (in_contract_heading or has_contract_column) and not table_contract:
                table_contract = True
                continue
            if is_separator:
                continue
        is_table_contract = is_table and table_contract
        is_list_contract = in_contract_heading and re.match(r"^\s*[-*]\s+`", line) is not None
        if not (is_table_contract or is_list_contract):
            continue
        routes.update(f"{match.group(1)} {match.group(2)}" for match in HTTP_ROUTE.finditer(line))
    return routes


def test_t001_projection_grammar_inventory() -> None:
    """Keep the future parser narrow while allowing varied, real spec domains."""
    impact_map = """# Impact map

Narrative IR-999 is a discussion label, not a risk-table obligation.

| ID | Risk | Control |
|---|---|---|
| IR-001 | Draft leakage | Predicate |
| IR-auth_2 | Admin action | Session |
| R-003 | Legacy style | Ignore |
"""
    plan = """# Plan

The client calls `GET /api/v1/narrative-only`; this prose is deliberately not a contract.

## API contracts

| Route | Auth |
|---|---|
| `GET /api/v1/posts?limit=20` | public |
| `PATCH /api/v1/admin/posts/:id` | admin |

## External API

| Endpoint | Owner |
|---|---|
| `HEAD /api/v1/health` | platform |

## Integration contracts

- `POST /api/v2/jobs/{jobId}` creates a job.
- `DELETE /api/v2/jobs/{jobId}` removes a job.

## Notes

- `PUT /api/v1/not-a-contract` remains ordinary prose outside a contract heading.

## Delivery matrix

| Milestone | Example |
|---|---|
| Alpha | `GET /api/v9/not-a-contract?draft=true` |

- `PATCH /api/v9/not-a-contract/:id?force=true` remains ordinary prose outside a contract heading.

## Capability register

| Route | Purpose |
|---|---|
| `OPTIONS /api/v3/discovery` | Capability discovery |
"""
    require(inventory_risk_ids(impact_map) == {"IR-001", "IR-auth_2"}, "T-001 risk grammar inventory drifted")
    require(
        inventory_http_routes(plan)
        == {
            "GET /api/v1/posts",
            "PATCH /api/v1/admin/posts/:id",
            "HEAD /api/v1/health",
            "POST /api/v2/jobs/{jobId}",
            "DELETE /api/v2/jobs/{jobId}",
            "OPTIONS /api/v3/discovery",
        },
        "T-001 HTTP grammar inventory drifted",
    )
    require(inventory_risk_ids("# Impact map\n\nNo risks are declared.\n") == set(), "empty risk inventory must stay empty")
    no_contracts = """# Plan

`GET /api/v1/narrative?cursor=x` is a prose example.

## Delivery matrix

| Milestone | Example |
|---|---|
| Alpha | `PATCH /api/v1/example/:id?force=true` |

- `DELETE /api/v1/example/{id}?hard=true` is not under a contract heading.
"""
    require(inventory_http_routes(no_contracts) == set(), "empty API inventory must exclude prose and unrelated tables")


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
    (initiative / "ratchet.md").write_text("# ratchet.md\n\n## principal\nfixture fact\n", encoding="utf-8")
    (initiative / "run-state.yaml").write_text("""brief_lineage: "v2"
brief_phase: "rendered"
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
    ratchet_digest = hashlib.sha256((initiative / "ratchet.md").read_bytes()).hexdigest()
    ratchet_fragment_digest = hashlib.sha256(b"fixture fact").hexdigest()
    blocks = "\n".join(
        (
            f'<section id="v2-{index}" data-source="{source}" data-source-section="principal" '
            f'data-coverage="represented" data-source-digest="sha256:{ratchet_digest}" '
            f'data-source-fragment="fixture fact" data-source-fragment-sha256="sha256:{ratchet_fragment_digest}">fixture fact</section>'
            if source == "ratchet.md" else
            f'<section id="v2-{index}" data-source="{source}" data-source-section="principal" data-coverage="represented" '
            f'data-source-digest="sha256:{hashlib.sha256((initiative / source).read_bytes()).hexdigest()}"></section>'
            if source != "decision-log.md" else
            f'<section id="v2-{index}" data-source="{source}" data-source-section="principal" data-coverage="represented"></section>'
        )
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


def tab_contract_errors(html: str) -> list[str]:
    """Keep the T-003 oracle focused despite unrelated v2 fixture checks."""
    report = Report()
    check_v2_provenance(html, report)
    return [error for error in report.structural if error.startswith("v2 tab")]


def tab_contract_fixture(*, script: str | None = None, second_tablist: bool = False) -> str:
    """Return a minimal rendered v2 tab surface with optional isolated group."""
    handler = script if script is not None else """
function initializeTablist(tablist) {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const panels = tabs.map(tab => document.getElementById(tab.getAttribute('aria-controls')));
  let active = tabs[0];
  const activate = tab => {
    active = tab;
    tabs.forEach((candidate, index) => {
      const selected = candidate === tab;
      candidate.setAttribute('aria-selected', String(selected));
      candidate.tabIndex = selected ? 0 : -1;
      panels[index].hidden = !selected;
    });
    history.replaceState(null, '', tab.hash);
  };
  tabs.forEach(tab => {
    tab.addEventListener('click', event => { event.preventDefault(); activate(tab); });
    tab.addEventListener('keydown', event => {
      if (event.key === 'ArrowLeft') {} if (event.key === 'ArrowRight') {}
      if (event.key === 'Home') {} if (event.key === 'End') {}
      if (event.key === 'Enter' || event.key === ' ') {}
      document.getElementById(tab.getAttribute('aria-controls')).focus();
    });
  });
}
document.querySelectorAll('[role="tablist"]').forEach(initializeTablist);
"""
    first = """
<nav role="tablist"><a id="tab-scope" role="tab" href="#scope" aria-controls="scope" aria-selected="true" tabindex="0">Scope</a><a id="tab-plan" role="tab" href="#plan" aria-controls="plan" aria-selected="false" tabindex="-1">Plan</a></nav>
<section id="scope" role="tabpanel" aria-labelledby="tab-scope" tabindex="0"></section><section id="plan" role="tabpanel" aria-labelledby="tab-plan" tabindex="0"></section>
"""
    second = """
<nav role="tablist"><a id="tab-secondary" role="tab" href="#secondary" aria-controls="secondary" aria-selected="true" tabindex="0">Secondary</a></nav>
<section id="secondary" role="tabpanel" aria-labelledby="tab-secondary" tabindex="0"></section>
""" if second_tablist else ""
    return f'<html data-harness-brief-design="v2"><body>{first}{second}<script>{handler}</script></body></html>'


def write_projection_sources(initiative: Path) -> None:
    """Install only grammar-recognized source obligations for T-003 tests."""
    (initiative / "impact-map.md").write_text("""# Impact

Narrative IR-999 must not become an obligation.

| ID | Risk |
|---|---|
| IR-001 | Publication leak |
| IR-auth_2 | Authorization boundary |
""", encoding="utf-8")
    (initiative / "plan.md").write_text("""# Plan

`GET /api/v1/narrative` remains prose, not a contract.

## API contracts

| Endpoint | Auth |
|---|---|
| `GET /api/v1/posts?limit=20` | public |
| `PATCH /api/v1/admin/posts/:id` | admin |

## Integration contracts

- `POST /api/v2/jobs/{jobId}` creates a job.

## Capability register

| Route | Purpose |
|---|---|
| `OPTIONS /api/v3/discovery` | Capability discovery |

## Delivery matrix

| Milestone | Example |
|---|---|
| Alpha | `DELETE /api/v1/not-a-contract` |
""", encoding="utf-8")


def write_projection_brief(initiative: Path, *, include_risks: bool = True, route_view: str | None = "architecture") -> None:
    """Project recognized tokens into allowed views without changing shell fixtures."""
    brief = initiative / "stakeholder-brief.html"
    html = brief.read_text(encoding="utf-8")
    risks = "IR-001 IR-auth_2" if include_risks else "risk summary only"
    html = html.replace('<section id="impact" class="impact-evidence"></section>', f'<section id="impact" class="impact-evidence">{risks}</section>')
    route_text = "GET /api/v1/posts PATCH /api/v1/admin/posts/:id POST /api/v2/jobs/{jobId} OPTIONS /api/v3/discovery"
    if route_view is not None:
        html = html.replace(f'<section id="{route_view}"></section>', f'<section id="{route_view}">{route_text}</section>')
    def refresh_digest(match: re.Match[str]) -> str:
        prefix, source = match.groups()
        return prefix + hashlib.sha256((initiative / source).read_bytes()).hexdigest()
    html = re.sub(
        r'(<[^>]*\bdata-source="([^"]+)"[^>]*\bdata-source-digest="sha256:)[^"]+',
        refresh_digest, html,
    )
    brief.write_text(html, encoding="utf-8")


def refresh_represented_digests(initiative: Path) -> None:
    """Refresh fixture provenance after an intentional source mutation."""
    brief = initiative / "stakeholder-brief.html"
    html = brief.read_text(encoding="utf-8")
    def refresh(match: re.Match[str]) -> str:
        prefix, source = match.groups()
        return prefix + hashlib.sha256((initiative / source).read_bytes()).hexdigest()
    brief.write_text(re.sub(
        r'(<[^>]*\bdata-source="([^"]+)"[^>]*\bdata-source-digest="sha256:)[^"]+', refresh, html,
    ), encoding="utf-8")


def main() -> int:
    test_t001_projection_grammar_inventory()
    # A record ID is an exact heading token: a longer hyphenated identifier
    # must not satisfy a request for its prefix.
    with tempfile.TemporaryDirectory(prefix="sdd-decision-record-") as temporary:
        decision_log = Path(temporary) / "decision-log.md"
        decision_log.write_text("## D-001-extra — unrelated\n", encoding="utf-8")
        require(
            decision_record(decision_log, "D-001") is None,
            "decision record lookup accepted a longer hyphenated heading ID",
        )
        decision_log.write_text("## D-001 — exact record\n", encoding="utf-8")
        require(
            decision_record(decision_log, "D-001") is not None,
            "decision record lookup must retain exact headed records",
        )
    with tempfile.TemporaryDirectory(prefix="sdd-human-visibility-") as temporary:
        root = Path(temporary)
        initiative = write_fixture(root)
        baseline = run(root, "--write-baseline")
        require(baseline.returncode == 0, baseline.stdout + baseline.stderr)
        clean = run(root)
        require(clean.returncode == 0 and "HUMAN REVIEW REQUIRED:" in clean.stdout, clean.stdout)

        # Evidence references are a v2-only contract. Existing v1 initiatives
        # may mention an ordinary evidence path without gaining a new gate.
        (initiative / "plan.md").write_text("# plan\nSee evidence/missing-v1.md\n", encoding="utf-8")
        v1_compatibility = run(root, "--write-baseline")
        require(v1_compatibility.returncode == 0, v1_compatibility.stdout + v1_compatibility.stderr)
        require(run(root).returncode == 0, "v1 evidence references must remain compatible")
        write_fixture(root)
        run(root, "--write-baseline")

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

        # The renderer and Human Visibility validator must resolve the same
        # explicit review-record form.  A headed record is not a substring
        # match: only the exact ID heading can satisfy this lifecycle link.
        decision = initiative / "decision-log.md"
        decision.write_text("""# Decision Log

## D-001 — reviewed composition

Decision propagation completed before Tasks Ready.

## D-001-extra — unrelated record

This must not become the D-001 record.
""", encoding="utf-8")
        headed_record = run(root, "--write-baseline")
        require(headed_record.returncode == 0, headed_record.stdout + headed_record.stderr)
        require(run(root).returncode == 0, "exact headed v2 review record must resolve cleanly")
        write_v2_fixture(root)
        run(root, "--write-baseline")

        baseline_payload = json.loads((initiative / "human-visibility-baseline.json").read_text(encoding="utf-8"))
        require(baseline_payload["schema_version"] == 2 and baseline_payload["brief_lineage"] == "v2", str(baseline_payload))
        require(baseline_payload["source_set"] == list(V2_SOURCES), str(baseline_payload))
        require(
            all(baseline_payload.get(key) for key in ("reviewed_by", "reviewed_at", "coverage_reviewer", "prior_change_anchor")),
            str(baseline_payload),
        )

        ratchet = initiative / "ratchet.md"
        previous_digest = hashlib.sha256(ratchet.read_bytes()).hexdigest()
        ratchet.write_text(ratchet.read_text(encoding="utf-8") + "\nIgnored path: evidence/../outside.md\n", encoding="utf-8")
        current_digest = hashlib.sha256(ratchet.read_bytes()).hexdigest()
        brief = initiative / "stakeholder-brief.html"
        brief.write_text(
            brief.read_text(encoding="utf-8").replace(
                f'data-source-digest="sha256:{previous_digest}"',
                f'data-source-digest="sha256:{current_digest}"',
                1,
            ),
            encoding="utf-8",
        )
        ratchet_evidence_text = run(root, "--write-baseline")
        require(
            ratchet_evidence_text.returncode == 0,
            "ratchet.md must not enter v2 evidence-reference path validation:\n" + ratchet_evidence_text.stdout + ratchet_evidence_text.stderr,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        baseline_payload["source_set"] = [source for source in V2_SOURCES if source != "ratchet.md"]
        (initiative / "human-visibility-baseline.json").write_text(json.dumps(baseline_payload), encoding="utf-8")
        stale_source_set = run(root)
        require(
            stale_source_set.returncode == 1 and "expanded v2 source_set metadata" in stale_source_set.stdout,
            stale_source_set.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-source="ratchet.md"', 'data-source="spec.md"', 1), encoding="utf-8")
        missing_ratchet_block = run(root)
        require(
            missing_ratchet_block.returncode == 1 and "missing v2 provenance block for required support source: ratchet.md" in missing_ratchet_block.stdout,
            missing_ratchet_block.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace("<td>ratchet.md #principal</td>", "<td>omitted-source.md #principal</td>", 1), encoding="utf-8")
        missing_ratchet_row = run(root)
        require(
            missing_ratchet_row.returncode == 1 and "missing v2 coverage register entry: ratchet.md" in missing_ratchet_row.stdout,
            missing_ratchet_row.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace(
            'data-source="ratchet.md" data-source-section="principal" data-coverage="represented" data-source-digest=',
            'data-source="ratchet.md" data-source-section="principal" data-coverage="not_applicable" data-source-digest=', 1,
        ), encoding="utf-8")
        invalid_ratchet_disposition = run(root)
        require(
            invalid_ratchet_disposition.returncode == 1 and "v2 support source must be represented or synthesized: ratchet.md" in invalid_ratchet_disposition.stdout,
            invalid_ratchet_disposition.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        ratchet_digest = hashlib.sha256((initiative / "ratchet.md").read_bytes()).hexdigest()
        brief.write_text(brief.read_text(encoding="utf-8").replace(f'data-source-digest="sha256:{ratchet_digest}"', 'data-source-digest="sha256:' + "0" * 64 + '"', 1), encoding="utf-8")
        stale_ratchet_digest = run(root)
        require(
            stale_ratchet_digest.returncode == 1 and "v2 support provenance digest does not bind the current local source: ratchet.md" in stale_ratchet_digest.stdout,
            stale_ratchet_digest.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        ratchet_fragment_digest = hashlib.sha256(b"fixture fact").hexdigest()
        brief.write_text(brief.read_text(encoding="utf-8").replace(f'data-source-fragment-sha256="sha256:{ratchet_fragment_digest}"', 'data-source-fragment-sha256="sha256:' + "0" * 64 + '"', 1), encoding="utf-8")
        stale_ratchet_fragment_digest = run(root)
        require(
            stale_ratchet_fragment_digest.returncode == 1 and "v2 support provenance fragment digest does not bind the declared source fragment: ratchet.md" in stale_ratchet_fragment_digest.stdout,
            stale_ratchet_fragment_digest.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        brief = initiative / "stakeholder-brief.html"
        brief.write_text(brief.read_text(encoding="utf-8").replace('data-source="tasks.md"', 'data-source="arbitrary.md"', 1), encoding="utf-8")
        unexpected_source = run(root)
        require(
            unexpected_source.returncode == 1 and "unknown v2 provenance source" in unexpected_source.stdout,
            unexpected_source.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        # T-003: only grammar-recognized tokens create obligations, but every
        # such risk and route must be visible in the prescribed view.
        write_v2_fixture(root)
        write_projection_sources(initiative)
        write_projection_brief(initiative)
        projected = run(root, "--write-baseline")
        require(projected.returncode == 0, projected.stdout + projected.stderr)
        require(run(root).returncode == 0, "projected risk/API fixture must recheck cleanly")

        write_v2_fixture(root)
        write_projection_sources(initiative)
        write_projection_brief(initiative, include_risks=False)
        missing_risks = run(root)
        require(
            missing_risks.returncode == 1
            and "missing v2 risk projection: IR-001 from impact-map.md must appear in #impact" in missing_risks.stdout
            and "IR-auth_2" in missing_risks.stdout,
            missing_risks.stdout,
        )
        missing_risks_baseline = run(root, "--write-baseline")
        require(missing_risks_baseline.returncode == 1, missing_risks_baseline.stdout)

        # Inert/source-only nodes are not stakeholder-visible projection.
        write_v2_fixture(root)
        write_projection_sources(initiative)
        write_projection_brief(initiative, include_risks=False, route_view=None)
        brief = initiative / "stakeholder-brief.html"
        html = brief.read_text(encoding="utf-8")
        html = html.replace(
            "risk summary only</section>",
            "<script>IR-001 IR-auth_2</script><style>.tokens{content:'IR-001 IR-auth_2'}</style><template>IR-001 IR-auth_2</template></section>",
        )
        html = html.replace(
            '<section id="architecture"></section>',
            '<section id="architecture"><script>GET /api/v1/posts PATCH /api/v1/admin/posts/:id POST /api/v2/jobs/{jobId} OPTIONS /api/v3/discovery</script><template>GET /api/v1/posts</template></section>',
        )
        brief.write_text(html, encoding="utf-8")
        inert_only = run(root, "--write-baseline")
        require(
            inert_only.returncode == 1
            and "missing v2 risk projection: IR-001 from impact-map.md must appear in #impact" in inert_only.stdout
            and "missing v2 API projection: GET /api/v1/posts from plan.md must appear in #architecture or #validation" in inert_only.stdout,
            inert_only.stdout,
        )

        write_v2_fixture(root)
        write_projection_sources(initiative)
        write_projection_brief(initiative, route_view=None)
        missing_routes = run(root)
        require(
            missing_routes.returncode == 1
            and "missing v2 API projection: GET /api/v1/posts from plan.md must appear in #architecture or #validation" in missing_routes.stdout
            and "PATCH /api/v1/admin/posts/:id" in missing_routes.stdout,
            missing_routes.stdout,
        )

        write_v2_fixture(root)
        write_projection_sources(initiative)
        write_projection_brief(initiative, route_view="validation")
        validation_projection = run(root, "--write-baseline")
        require(validation_projection.returncode == 0, validation_projection.stdout + validation_projection.stderr)
        write_v2_fixture(root)
        run(root, "--write-baseline")

        # T-002: a fragment is not part of the evidence filename. A valid
        # initiative-relative evidence pack therefore passes both baseline and
        # ordinary validation.
        evidence_dir = initiative / "evidence"
        evidence_dir.mkdir(exist_ok=True)
        (evidence_dir / "planning-review.md").write_text("# approved\n", encoding="utf-8")
        plan = initiative / "plan.md"
        plan.write_text(plan.read_text(encoding="utf-8") + "\nReview: [approved](evidence/planning-review.md#final-decision).\n", encoding="utf-8")
        refresh_represented_digests(initiative)
        anchored_evidence = run(root, "--write-baseline")
        require(anchored_evidence.returncode == 0, anchored_evidence.stdout + anchored_evidence.stderr)
        require(run(root).returncode == 0, "anchored v2 evidence reference must resolve to its file")
        write_v2_fixture(root)
        run(root, "--write-baseline")

        plan = initiative / "plan.md"
        plan.write_text(plan.read_text(encoding="utf-8") + "\nReview: evidence/missing-review.md#final.\n", encoding="utf-8")
        missing_evidence = run(root)
        require(
            missing_evidence.returncode == 1
            and "missing referenced v2 evidence artifact: evidence/missing-review.md (cited by plan.md)" in missing_evidence.stdout,
            missing_evidence.stdout,
        )
        missing_evidence_baseline = run(root, "--write-baseline")
        require(
            missing_evidence_baseline.returncode == 1
            and "missing referenced v2 evidence artifact: evidence/missing-review.md (cited by plan.md)" in missing_evidence_baseline.stdout,
            missing_evidence_baseline.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        plan = initiative / "plan.md"
        plan.write_text(plan.read_text(encoding="utf-8") + "\nReview: ./evidence/missing-dot-prefix.md#final.\n", encoding="utf-8")
        dot_prefix_evidence = run(root)
        require(
            dot_prefix_evidence.returncode == 1
            and "missing referenced v2 evidence artifact: evidence/missing-dot-prefix.md (cited by plan.md)" in dot_prefix_evidence.stdout,
            dot_prefix_evidence.stdout,
        )
        dot_prefix_baseline = run(root, "--write-baseline")
        require(
            dot_prefix_baseline.returncode == 1
            and "missing referenced v2 evidence artifact: evidence/missing-dot-prefix.md (cited by plan.md)" in dot_prefix_baseline.stdout,
            dot_prefix_baseline.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        plan = initiative / "plan.md"
        plan.write_text(plan.read_text(encoding="utf-8") + "\nReview: evidence/../outside.md.\n", encoding="utf-8")
        traversal_evidence = run(root)
        require(
            traversal_evidence.returncode == 1
            and "invalid v2 evidence reference in plan.md" in traversal_evidence.stdout,
            traversal_evidence.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        plan = initiative / "plan.md"
        plan.write_text(plan.read_text(encoding="utf-8") + "\nReview: /outside/evidence/review.md.\n", encoding="utf-8")
        absolute_evidence = run(root)
        require(
            absolute_evidence.returncode == 1
            and "invalid v2 evidence reference in plan.md" in absolute_evidence.stdout,
            absolute_evidence.stdout,
        )
        write_v2_fixture(root)
        run(root, "--write-baseline")

        # Preliminary task rows advertise future evidence destinations. They
        # must not make a planning-complete package impossible to baseline.
        state = initiative / "run-state.yaml"
        state.write_text(state.read_text(encoding="utf-8") + """\ntask_ledger:
  - id: "T-203"
    status: "pending"
    evidence: "evidence/T-203.md"
""", encoding="utf-8")
        plan = initiative / "plan.md"
        plan.write_text(plan.read_text(encoding="utf-8") + "\nFuture task proof: evidence/T-203.md.\n", encoding="utf-8")
        # Preliminary lifecycle states defer an explicitly declared future
        # destination. The complete matrix prevents a later refactor from
        # silently narrowing or broadening that allowance.
        for lifecycle_status in ("pending", "ready", "in_progress", "blocked"):
            state.write_text(
                re.sub(r'(?m)^    status: "[^"]+"', f'    status: "{lifecycle_status}"', state.read_text(encoding="utf-8")),
                encoding="utf-8",
            )
            refresh_represented_digests(initiative)
            deferred_baseline = run(root, "--write-baseline")
            require(
                deferred_baseline.returncode == 0,
                f"{lifecycle_status} must defer declared future evidence before baseline:\n{deferred_baseline.stdout}{deferred_baseline.stderr}",
            )
            deferred_normal = run(root)
            require(
                deferred_normal.returncode == 0,
                f"{lifecycle_status} must defer declared future evidence in normal validation:\n{deferred_normal.stdout}{deferred_normal.stderr}",
            )
        # At evaluation and terminal states, the absent pack is an integrity
        # failure. This is not an evidence waiver or a semantic approval.
        for lifecycle_status in ("needs_evaluation", "approved", "done"):
            state.write_text(
                re.sub(r'(?m)^    status: "[^"]+"', f'    status: "{lifecycle_status}"', state.read_text(encoding="utf-8")),
                encoding="utf-8",
            )
            required_normal = run(root)
            require(
                required_normal.returncode == 1
                and "missing referenced v2 evidence artifact: evidence/T-203.md (cited by plan.md)" in required_normal.stdout,
                f"{lifecycle_status} must require evidence in normal validation:\n{required_normal.stdout}{required_normal.stderr}",
            )
            required_baseline = run(root, "--write-baseline")
            require(
                required_baseline.returncode == 1
                and "missing referenced v2 evidence artifact: evidence/T-203.md (cited by plan.md)" in required_baseline.stdout,
                f"{lifecycle_status} must require evidence before baseline:\n{required_baseline.stdout}{required_baseline.stderr}",
            )
        write_v2_fixture(root)
        run(root, "--write-baseline")

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

        # The status is a closed lifecycle enum, not reviewer prose.  Do not
        # normalize passed-looking values by substring, case folding, trimming
        # or removing embedded quotes before deciding Human Visibility.
        state = initiative / "run-state.yaml"
        reviewed_state = state.read_text(encoding="utf-8")
        for outcome in ("not_passed", "compass", "unknown", "PASS", " pass ", "'pass'"):
            state.write_text(
                reviewed_state.replace('findings_status: "pass"', f'findings_status: "{outcome}"', 1),
                encoding="utf-8",
            )
            refused = run(root)
            require(
                refused.returncode == 1
                and "brief_review.findings_status" in refused.stdout,
                f"{outcome!r} must not grant Human Visibility readiness:\n{refused.stdout}{refused.stderr}",
            )
        state.write_text(reviewed_state, encoding="utf-8")
        exact_pass = run(root)
        require(exact_pass.returncode == 0, exact_pass.stdout + exact_pass.stderr)

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
        require(
            stale_v2.returncode == 1
            and "v2 represented provenance digest does not bind the current local source: tasks.md" in stale_v2.stdout,
            stale_v2.stdout,
        )
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

        # SPEC 013 T-002: rendered DOM integrity is global, but inert markup
        # and lexical text inside it cannot satisfy or violate the contract.
        for duplicated in ("coverage-register", "arbitrary-rendered-id"):
            report = Report()
            check_v2_provenance(
                f'<html data-harness-brief-design="v2"><body><div id="{duplicated}"></div><div id="{duplicated}"></div></body></html>',
                report,
            )
            require(any(f"duplicate rendered HTML id: {duplicated}" in error for error in report.structural), str(report.structural))

        inert = '<html data-harness-brief-design="v2"><body><template><div id="coverage-register"></div><div id="coverage-register"></div></template><script>const close="</html>";</script><style>#coverage-register{color:red}</style></body></html>'
        report = Report()
        check_v2_provenance(inert, report)
        require(not any("duplicate rendered HTML id" in error or "terminal </html>" in error for error in report.structural), str(report.structural))

        for tail in ("<div>tail</div>", "tail", "<!DOCTYPE html>", "<?tail?>"):
            report = Report()
            check_v2_provenance(f'<html data-harness-brief-design="v2"><body></body></html>{tail}', report)
            require("rendered content appears after terminal </html>; remove trailing document content" in report.structural, str(report.structural))

        sentinel_tail = "PRIVATE_SENTINEL_DO_NOT_EMIT"
        report = Report()
        check_v2_provenance(f'<html data-harness-brief-design="v2"><body></body></html>{sentinel_tail}', report)
        require(sentinel_tail not in "\n".join(report.structural), str(report.structural))

        report = Report()
        check_v2_provenance('<html data-harness-brief-design="v2"><body></body></html>\n<!-- permitted -->\n', report)
        require("rendered content appears after terminal </html>; remove trailing document content" not in report.structural, str(report.structural))

        # SPEC 013 T-003: a declared v2 tablist is checked per rendered
        # group. The fixture deliberately uses native anchors; this checker
        # proves a static enhancement contract, never runtime browser/AT use.
        require(not tab_contract_errors(tab_contract_fixture()), str(tab_contract_errors(tab_contract_fixture())))
        require(
            not tab_contract_errors(tab_contract_fixture(second_tablist=True)),
            str(tab_contract_errors(tab_contract_fixture(second_tablist=True))),
        )

        click_only = tab_contract_fixture().replace(
            "tab.addEventListener('keydown', event => {\n      if (event.key === 'ArrowLeft') {} if (event.key === 'ArrowRight') {}\n      if (event.key === 'Home') {} if (event.key === 'End') {}\n      if (event.key === 'Enter' || event.key === ' ') {}\n      document.getElementById(tab.getAttribute('aria-controls')).focus();\n    });\n",
            "",
        )
        click_only_errors = tab_contract_errors(click_only)
        require(
            "v2 tab handler initializer initializeTablist missing static keydown listener evidence" in click_only_errors,
            str(click_only_errors),
        )

        prose_only = tab_contract_fixture(
            script="",
        ).replace(
            "</body>",
            "<p>click keydown ArrowLeft ArrowRight Home End Enter Space aria-selected hidden focus history</p></body>",
        )
        prose_only_errors = tab_contract_errors(prose_only)
        require(
            "v2 tab handler missing a live per-tablist initializer; initialize each rendered tablist without a fixed tab count" in prose_only_errors,
            str(prose_only_errors),
        )

        multi_selected = tab_contract_fixture().replace('id="tab-plan" role="tab" href="#plan" aria-controls="plan" aria-selected="false"', 'id="tab-plan" role="tab" href="#plan" aria-controls="plan" aria-selected="true"')
        require(
            'v2 tablist 1 must have exactly one aria-selected="true" tab' in tab_contract_errors(multi_selected),
            str(tab_contract_errors(multi_selected)),
        )

        broken_reciprocity = tab_contract_fixture().replace('aria-labelledby="tab-plan"', 'aria-labelledby="not-the-tab"')
        require(
            "v2 tablist 1 tab/panel aria-controls and aria-labelledby must be reciprocal" in tab_contract_errors(broken_reciprocity),
            str(tab_contract_errors(broken_reciprocity)),
        )

        second_unselected = tab_contract_fixture(second_tablist=True).replace(
            'id="tab-secondary" role="tab" href="#secondary" aria-controls="secondary" aria-selected="true" tabindex="0"',
            'id="tab-secondary" role="tab" href="#secondary" aria-controls="secondary" aria-selected="false" tabindex="-1"',
        )
        require(
            'v2 tablist 2 must have exactly one aria-selected="true" tab' in tab_contract_errors(second_unselected),
            str(tab_contract_errors(second_unselected)),
        )

        # Evaluator regressions: proof must be executable, scoped to every
        # tablist, and independent from the old eight-tab canonical shape.
        commented_handler = tab_contract_fixture(script="/*\n" + tab_contract_fixture().split("<script>", 1)[1].split("</script>", 1)[0] + "\n*/")
        require(
            "v2 tab handler missing a live per-tablist initializer; initialize each rendered tablist without a fixed tab count" in tab_contract_errors(commented_handler),
            str(tab_contract_errors(commented_handler)),
        )

        dead_handler = tab_contract_fixture(script="if (false) {\n" + tab_contract_fixture().split("<script>", 1)[1].split("</script>", 1)[0] + "\n}")
        require(
            "v2 tab handler missing a live per-tablist initializer; initialize each rendered tablist without a fixed tab count" in tab_contract_errors(dead_handler),
            str(tab_contract_errors(dead_handler)),
        )

        global_tabs = tab_contract_fixture().replace("tablist.querySelectorAll('[role=\"tab\"]')", "document.querySelectorAll('[role=\"tab\"]')")
        require(
            "v2 tab handler initializer initializeTablist must query tabs within its tablist parameter" in tab_contract_errors(global_tabs),
            str(tab_contract_errors(global_tabs)),
        )

        # An unrelated control cannot lend its listeners to a scoped, but
        # no-op, tabs.forEach. This is deliberately a realistic token-level
        # bypass: all other tab mutations and key names remain present.
        scope_only_handlers = tab_contract_fixture(script="""
function initializeTablist(tablist) {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const panels = tabs.map(tab => document.getElementById(tab.getAttribute('aria-controls')));
  const activate = tab => {
    tabs.forEach((candidate, index) => {
      const selected = candidate === tab;
      candidate.setAttribute('aria-selected', String(selected));
      candidate.tabIndex = selected ? 0 : -1;
      panels[index].hidden = !selected;
    });
    history.replaceState(null, '', tab.hash);
  };
  tabs.forEach(tab => {});
  const scope = document.getElementById('tab-scope');
  scope.addEventListener('click', event => { event.preventDefault(); activate(scope); });
  scope.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft') {} if (event.key === 'ArrowRight') {}
    if (event.key === 'Home') {} if (event.key === 'End') {}
    if (event.key === 'Enter' || event.key === ' ') {}
    document.getElementById(scope.getAttribute('aria-controls')).focus();
  });
}
document.querySelectorAll('[role="tablist"]').forEach(initializeTablist);
""")
        scope_only_errors = tab_contract_errors(scope_only_handlers)
        require(
            "v2 tab handler initializer initializeTablist missing static click listener evidence" in scope_only_errors
            and "v2 tab handler initializer initializeTablist missing static keydown listener evidence" in scope_only_errors,
            str(scope_only_errors),
        )

        third_group = """
<nav role="tablist"><a id="tab-tertiary" role="tab" href="#tertiary" aria-controls="tertiary" aria-selected="true" tabindex="0">Tertiary</a></nav>
<section id="tertiary" role="tabpanel" aria-labelledby="tab-tertiary" tabindex="0"></section>
"""
        arbitrary_groups = tab_contract_fixture(second_tablist=True).replace("<script>", third_group + "<script>")
        require(not tab_contract_errors(arbitrary_groups), str(tab_contract_errors(arbitrary_groups)))

        no_tab_v2 = '<html data-harness-brief-design="v2"><body><section id="scope"></section></body></html>'
        require(not tab_contract_errors(no_tab_v2), str(tab_contract_errors(no_tab_v2)))

        template = (ROOT / ".harness" / "templates" / "stakeholder-brief.html").read_text(encoding="utf-8")
        template_tab_errors = tab_contract_errors(template)
        require(not template_tab_errors, str(template_tab_errors))
        require(
            'href="?view=scope"' in template
            and '@media print' in template
            and re.search(r"prefers-reduced-motion\s*:\s*reduce", template),
            "canonical tab scaffold must retain native anchors, print and reduced-motion fallbacks",
        )
        require(
            "tabs.length===8" not in template
            and re.search(r"document\s*\.\s*querySelectorAll\s*\(\s*['\"]\[role=\"tablist\"\]['\"]\s*\)\s*\.\s*forEach\s*\(\s*initializeTablist\s*\)", template)
            and re.search(r"tablist\s*\.\s*querySelectorAll\s*\(\s*['\"]\[role=\"tab\"\]['\"]\s*\)", template),
            "canonical tab scaffold must initialize each tablist without a fixed global tab count",
        )
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
