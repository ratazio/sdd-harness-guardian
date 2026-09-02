# Reprodução — contradição de composição no R2

## Contexto

Run observado:
`testes/mock-runs/20260901-spec027-composition-r2/m003-offline/specs/001-mobile-offline-inspections/`.

O candidate aberto pelo usuário foi:
`brief-candidates/stakeholder-brief.candidate.html?view=execution`.

## Estado fonte observado

`run-state.yaml` declara, entre outros:

```yaml
brief_lineage: null
brief_phase: "not_rendered"
current_phase: "ready_to_compose"
plan_ready: false
tasks_drafted: false
brief_coverage_ready: true
human_visibility_ready: false
findings_status: "revise"
quality_review_required: true
quality_review_status: "not_started"
```

O `decision-log.md` do mesmo run inclui decisões que proíbem HTML/skeleton/
candidate enquanto a revisão pre-skeleton for `REVISE`. Mesmo assim, há
`brief-candidates/stakeholder-brief.skeleton.html` e
`brief-candidates/stakeholder-brief.candidate.html`. Não há
`stakeholder-brief.html` final.

## Resultado dos checks existentes

- `validate_brief_candidate_inheritance.py` aceita a herança física do
  skeleton; isso não mede qualidade de texto/visual/lifecycle.
- `architecture_visual_contract.py` não acusa a arquitetura porque o candidate
  não declara uma disposição `material` que acione o guard.
- A validação Human Visibility falha: falta final e o gate não está pronto.
- `python scripts/validate_bundle.py` passa para o bundle; isso não prova que
  um run específico tenha brief final de qualidade.

## Perda observável no candidate

- Texto visível de scaffold: “Scaffolded — not ready for review, baseline or
  delivery”.
- A mesma cadeia de topologia aparece em vários zooms e campos distintos,
  substituindo responsabilidades, mudanças, fronteiras e recovery específicos.
- Três épicos repetem uma lista codificada de T-001…T-007 em vez de dossiers de
  execução compreensíveis.
- A própria planificação M003 descreve zooms, impactos, tasks e provas
  individuais mais ricos que os blocos recuperados no HTML.

## Conclusão reprodutível

O defeito é sistêmico: há uma chain de candidate, uma de promoção/Human
Visibility e uma revisão qualitativa opcional, sem uma autoridade única. A
SPEC 028 deve corrigir essa ligação sem automatizar a autoria do brief.
