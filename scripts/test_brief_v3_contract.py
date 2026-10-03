#!/usr/bin/env python3
"""Contract 3 mechanical integration tests; actor records are synthetic fixtures.

This runs no medium agent and proves no executor configuration or narrative
quality. Real repair skill execution/browser evidence is recorded separately.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from brief_v3_contract import (
    CORE_MD, ROUTES, completion_errors, materialized_state, repair_metadata,
    sha256, snapshot_errors, structural_errors, write_repair_metadata,
)
from validate_human_visibility import validate
from validate_bundle import brief_contract_lineage, stakeholder_brief_errors

ROOT = Path(__file__).resolve().parent.parent


def candidate_html() -> str:
    controls = ''.join(f'<input class="view-control" type="radio" name="brief-view" id="view-{route}" aria-controls="{route}"' + (' checked' if route == 'scope' else '') + '>' for route in ROUTES)
    labels = ''.join(f'<label id="tab-{route}" for="view-{route}">{route}</label>' for route in ROUTES)
    panels = ''.join(f'<section id="{route}" class="tab-panel brief-route" aria-labelledby="tab-{route}"' + (' data-architecture-visual="not_applicable" data-architecture-visual-reason="No architecture relation is provided in this synthetic source fixture."' if route == 'architecture' else '') + f'><h2>{route}</h2>' + ('<table class="coverage"><tr><th>Source / fact / target / limit</th></tr><tr><td>spec.md / Fixture / scope / source TODO remains a source limit.</td></tr></table>' if route == 'coverage' else '<p>Fixture fact; no task or implementation approval.</p>') + '</section>' for route in ROUTES)
    css = '.route-panels>.tab-panel{display:none}' + ''.join(f'#view-{route}:checked~.route-panels>#{route}{{display:block}}' for route in ROUTES) + '@media print{.route-panels>.tab-panel{display:block}}'
    return f'<!doctype html><html data-brief-contract="3" data-harness-template-kind="composed"><head><title>Mechanical fixture</title><style>{css}</style></head><body class="brief-shell"><header class="brief-header"><h1>Mechanical fixture</h1></header><div class="decision-register impact-evidence decision-actions"><p data-source="spec.md" data-source-section="Fixture" data-coverage="represented">Source TODO/TBD and future evidence are limits.</p><pre><code>{{{{literal_code_syntax}}}}</code></pre><!-- {{{{instruction_only}}}} --></div><div class="brief-tabs">{controls}<nav class="route-nav">{labels}</nav><div class="route-panels">{panels}</div></div></body></html>'


def initial_state() -> str:
    return '''schema_version: 1
status: "draft"
brief_phase: "not_rendered"
brief_lineage: null
current_phase: "source_authority_unresolved"
quality_gates:
  human_visibility_ready: false
  tasks_drafted: false
  brief_coverage_ready: false
  tasks_ready: false
  implementation_done: false
task_ledger:
  - id: T-001
    status: pending
approvals:
  granted: []
brief_review:
  findings_status: "not_started"
brief_repair:
  contract: 3
  author: "fixture-author-A"
  status: incomplete
  source_snapshot: {}
  content:
    actor: null
    effective_effort: null
    execution_ref: null
    completed_at: null
    status: incomplete
  visual:
    actor: null
    effective_effort: null
    execution_ref: null
    completed_at: null
    status: incomplete
  rendered_sha256: null
  report: null
'''


def seed(root: Path) -> tuple[Path, str]:
    initiative = root / "specs" / "001-mechanical-v3-fixture"
    initiative.mkdir(parents=True)
    for name in CORE_MD:
        (initiative / name).write_text('# Fixture\n\nSource TODO/TBD and evidence/future.md are source limits, not generation gates.\n', encoding='utf-8')
    (initiative / 'run-state.yaml').write_text(initial_state(), encoding='utf-8')
    html = candidate_html()
    (initiative / 'candidate.html').write_text(html, encoding='utf-8')
    return initiative, html


def complete(state: str, html: str) -> str:
    metadata = repair_metadata(state)
    metadata['status'] = 'completed_with_source_limitations'
    for name in ('content', 'visual'):
        metadata[name] = {
            'actor': 'fixture-repair-B', 'effective_effort': 'high',
            'execution_ref': 'synthetic-test-fixture://executor-config/high/' + name,
            'completed_at': '2026-10-02T12:00:00Z', 'status': 'completed_with_source_limitations',
        }
    metadata['rendered_sha256'] = sha256(html.encode('utf-8'))
    return write_repair_metadata(state, metadata)


def exercise(root: Path) -> dict:
    initiative, html = seed(root)
    before = {name: (initiative / name).read_bytes() for name in CORE_MD}
    assert not structural_errors(html, rendered=True)
    command = [sys.executable, str(ROOT / 'scripts/render_stakeholder_brief.py'), str(initiative), '--candidate', str(initiative / 'candidate.html')]
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    state_path = initiative / 'run-state.yaml'
    rendered = state_path.read_text(encoding='utf-8')
    (initiative / 'state-after-materialization.yaml').write_text(rendered, encoding='utf-8')
    assert (initiative / 'stakeholder-brief.html').read_bytes() == html.encode('utf-8')
    assert {name: (initiative / name).read_bytes() for name in CORE_MD} == before
    assert repair_metadata(rendered)['status'] == 'incomplete'
    assert 'human_visibility_ready: false' in rendered and 'tasks_ready: false' in rendered
    assert 'status: pending' in rendered and 'granted: []' in rendered
    initial = validate(initiative, root, None)
    assert any('incomplete' in error for error in initial.failures)
    assert not any('independent' in message for message in initial.human_review)
    completed = complete(rendered, html)
    state_path.write_text(completed, encoding='utf-8')
    (initiative / 'state-after-repairs.yaml').write_text(completed, encoding='utf-8')
    final = validate(initiative, root, None)
    assert not final.failures, final.failures
    assert 'human_visibility_ready: false' in completed and 'tasks_ready: false' in completed
    metadata = repair_metadata(completed)
    for effort in ('xhigh', 'max', 'ultra'):
        supported = json.loads(json.dumps(metadata))
        for name in ('content', 'visual'):
            supported[name]['effective_effort'] = effort
            supported[name]['execution_ref'] = 'synthetic-test-fixture://explicitly-supported/' + effort
        assert not completion_errors(supported, html)
    checks = {}
    for name, mutate, expected in (
        ('medium-record', lambda record: record['content'].update(effective_effort='medium'), 'effective_effort'),
        ('missing-execution-ref', lambda record: record['visual'].update(execution_ref=None), 'execution_ref'),
        ('author-repairs-own-html', lambda record: record['content'].update(actor=record['author']), 'distinct'),
        ('different-visual-actor', lambda record: record['visual'].update(actor='fixture-other-C'), 'same repair actor'),
        ('wrong-html-digest', lambda record: record.update(rendered_sha256='0' * 64), 'rendered_sha256'),
    ):
        changed = json.loads(json.dumps(metadata))
        mutate(changed)
        errors = completion_errors(changed, html)
        assert any(expected in error for error in errors), errors
        checks[name] = errors
    (initiative / 'tasks.md').write_bytes(before['tasks.md'] + b'\nchanged during composition\n')
    checks['changed-source'] = snapshot_errors(initiative, metadata, html)
    assert any('tasks.md' in error for error in checks['changed-source'])
    state_before_failure = state_path.read_bytes()
    refused = subprocess.run(command + ['--refresh'], capture_output=True, text=True)
    assert refused.returncode == 1 and 'snapshot changed' in refused.stderr, refused.stderr
    assert state_path.read_bytes() == state_before_failure
    (initiative / 'tasks.md').write_bytes(before['tasks.md'])
    legacy_only = subprocess.run([sys.executable, str(ROOT / 'scripts/render_stakeholder_brief.py'), str(initiative), '--finalize-post-review'], capture_output=True, text=True)
    assert legacy_only.returncode == 1 and 'historical contract 1/2 only' in legacy_only.stderr
    assert {name: (initiative / name).read_bytes() for name in CORE_MD} == before
    for path in (ROOT / 'scripts/fixtures/tabbed-brief-surface/template-v2.html', ROOT / 'specs/004-consumer-enforcement-contract/stakeholder-brief.html', ROOT / 'specs/010-stakeholder-brief-composition-kit/stakeholder-brief.html'):
        if path.is_file():
            old = path.read_bytes()
            assert brief_contract_lineage(old.decode('utf-8')) in {'v1', 'v2'}
            assert not stakeholder_brief_errors(old.decode('utf-8'), rendered=False if path.name == 'template-v2.html' else True)
            assert path.read_bytes() == old
    return {'command': command, 'exit_code': result.returncode, 'stdout': result.stdout, 'initial_failures': initial.failures, 'final_failures': final.failures, 'negative_checks': checks, 'source_hashes': {name: sha256(data) for name, data in before.items()}, 'boundary': 'Synthetic metadata consistency only; no native effort/skill/browser proof.'}


def test_contract3_materialization_and_completion(tmp_path):
    exercise(tmp_path)


def test_contract3_structure_negative_cases():
    html = candidate_html()
    for changed, expected in (
        (html.replace(' checked', ''), 'initially checked'),
        (html.replace('id="view-impact"', 'id="view-scope"'), 'unique'),
        (html.replace('<head>', '<head><script src="https://example.invalid/script.js"></script>'), 'inline'),
        (html.replace('Fixture fact;', '{{unfilled_slot}}'), 'placeholder'),
        (html.replace('data-harness-template-kind="composed"', 'data-harness-template-kind="scaffold"'), 'scaffold'),
    ):
        assert any(expected in error for error in structural_errors(changed, rendered=True))
    template = (ROOT / '.harness/templates/stakeholder-brief.html').read_text(encoding='utf-8')
    assert brief_contract_lineage(template) == 'v3'
    assert not stakeholder_brief_errors(template, rendered=False)
    real = (ROOT / 'scripts/fixtures/brief-v3-contract/composed.html').read_bytes().decode('utf8')
    assert not structural_errors(real, rendered=True)
    broken_graph = real.replace('data-from="entrada"', 'data-from="missing-node"')
    assert any('connections' in error for error in structural_errors(broken_graph, rendered=True))


def test_repair_mapping_preserves_unrelated_yaml_and_rejects_duplicate_fields():
    state = initial_state()
    metadata = repair_metadata(state)
    updated = write_repair_metadata(state, metadata)
    assert updated.split('brief_repair:', 1)[0] == state.split('brief_repair:', 1)[0]
    duplicate = state.replace('  contract: 3', '  contract: 3\n  contract: 3')
    try:
        repair_metadata(duplicate)
    except ValueError as error:
        assert 'duplicate' in str(error)
    else:
        raise AssertionError('duplicate metadata accepted')


def test_real_composed_template_and_raw_crlf_bytes(tmp_path):
    """A's actual T002 HTML, not a hand-crafted validator-specific shell."""
    initiative, _ = seed(tmp_path)
    fixture = ROOT / 'scripts/fixtures/brief-v3-contract'
    html_bytes = (fixture / 'composed.html').read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
    (initiative / 'candidate.html').write_bytes(html_bytes)
    shutil.copyfile(fixture / 'fonte-controlada.md', initiative / 'fonte-controlada.md')
    initial = initial_state().replace('\n', '\r\n')
    (initiative / 'run-state.yaml').write_bytes(initial.encode('utf8'))
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/render_stakeholder_brief.py'), str(initiative), '--candidate', str(initiative / 'candidate.html')], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (initiative / 'stakeholder-brief.html').read_bytes() == html_bytes
    after = (initiative / 'run-state.yaml').read_bytes().decode('utf8')
    assert after.split('brief_repair:', 1)[0].replace('brief_phase: "rendered"', 'brief_phase: "not_rendered"').replace('brief_lineage: "v3"', 'brief_lineage: null') == initial.split('brief_repair:', 1)[0]
    completed = complete(after, html_bytes.decode('utf8'))
    (initiative / 'run-state.yaml').write_bytes(completed.encode('utf8'))
    report = validate(initiative, tmp_path, None)
    assert not report.failures, report.failures


def main() -> int:
    with tempfile.TemporaryDirectory(prefix='brief-v3-mechanical-') as temporary:
        root = Path(temporary)
        results = exercise(root)
        test_contract3_structure_negative_cases()
        test_repair_mapping_preserves_unrelated_yaml_and_rejects_duplicate_fields()
        test_real_composed_template_and_raw_crlf_bytes(root / 'real-composed')
        if len(sys.argv) == 3 and sys.argv[1] == '--artifacts':
            output = Path(sys.argv[2])
            output.mkdir(parents=True, exist_ok=True)
            shutil.copytree(root / 'specs', output / 'specs', dirs_exist_ok=True)
            (output / 'checks.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print('Contract 3 mechanical integration passed; synthetic effort records do not prove native skill execution.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
