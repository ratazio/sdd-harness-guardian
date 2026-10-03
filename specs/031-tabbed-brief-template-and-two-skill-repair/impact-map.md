# Impact Map — 031

**Status:** mapped — planejamento, sem alteração de implementação
**Owner:** Guardian maintainers
**Last updated:** 2026-10-02

## 1. Boundary

Muda projeção/apresentação e correção de briefs do bundle fonte. MD do
consumidor são entrada imutável. Não muda autoria de fontes, implementação
do produto, autorização do owner ou evidence/evaluation das tasks.

## 2. Affected surfaces

| Superfície | Current → target | Limite |
|---|---|---|
| .harness/templates/stakeholder-brief.html | Casca atual → template instruído, completo e abas sem JS. | Preservar identidade; corrigir IDs/header/título. |
| .harness/templates/stakeholder-brief-design.md | Guia atual → instruções de slots e componentes. | Não duplicar contrato normativo. |
| .harness/skills/executive-brief-composition/SKILL.md | Modelo/review/projection → preencher HTML e entregar a B. | Sem modelo obrigatório para contrato 3. |
| .harness/skills/rendered-brief-decision-review/SKILL.md | Review devolutivo → conferir e corrigir conteúdo. | B high/xhigh é reparador, não evaluator de suas edições. |
| .harness/skills/executive-brief-experience-review/SKILL.md | Review de modelo → conferir e corrigir experiência final. | Segunda e última passagem do mesmo B. |
| .harness/skills/spec-review/SKILL.md | Entry point ainda descreve reviews a/b do contrato 2 → dispatch explícito para 3. | Preservar o ramo histórico sem exigir a cadeia 2 no caminho 3. |
| .harness/rules/brief-contract.md e human-visibility.md | Contrato 2 → ramo explícito 3. | Histórico 1/2 conserva contrato e leitura. |
| .harness/AGENTS.md, agents/workflows | Cadeia antiga → autoria e duas correções. | Preservar gates da implementação, mudar só mandatos do brief. |
| templates/README.md, plan.md, run-state.yaml.md | Modelo/review obrigatório → fonte/estado e handoff simples. | Não mudar conteúdo mínimo dos MD nem os mocks. |
| scripts/render_stakeholder_brief.py, validate_human_visibility.py | Pressupostos 2 → ramo 3 explícito. | Utilitários mecânicos, sem etapa extra semântica por brief. |
| scripts/project_brief.py, schema/model tests | Caminho obrigatório 029 → legado opcional para 1/2. | Remoção física fora do MVP. |
| manifest.yaml, validate_bundle.py, testes de contrato | Registry antigo → novo fluxo/compatibilidade. | Ajustar referências efetivamente afetadas. |
| testes/mock-runs/ | Históricos → execução nova com cópias idênticas. | Não sobrescrever originais nem implementar produto. |

## 3. Unchanged surfaces

MD dos consumidores; autoria de specs/plans/tasks; autorização humana;
builder/evaluator de implementação; evidence packs; briefs históricos;
integrações e marcas externas.

## 4. Impact risks

| ID | Risco/sinal | Controle | Contingency/owner |
|---|---|---|---|
| IR-001 | Entry point 3 ainda exige review/modelo antigo. | V-012/017, traço normal. | Reverter entrypoints ao checkpoint — Guardian maintainers |
| IR-002 | Reparador altera MD para fazer HTML passar. | Hashes antes/depois. | Descartar saída de laboratório e corrigir mandato — Guardian maintainers |
| IR-003 | Gates 3 contaminam leitura 1/2. | Históricos congelados e version dispatch. | Reverter ramo 3, sem editar histórico — Guardian maintainers |
| IR-004 | Falta de esforço/browser reportada como sucesso. | Configuração efetiva/ambiente registrados. | Não concluir passagem qualificada — Executor |
| IR-005 | Layout apaga conteúdo recuperado. | Skill visual lê todas as abas/explicação. | Restaurar na segunda passagem — Reparador B |

## 5. Evidence basis

Pedido do owner: MD fora do escopo; HTML único/abas; duas skills corretivas
com high/xhigh, sem terceira validação. Laboratório: 8 projeções aceitas e
8 revisões pedindo ajuste; omissões dos modelos, cobertura duplicada e
limitações dos fixtures separados. Skills atuais proíbem reparar e impõem
re-review: esses mandatos precisam ser substituídos, não sobrepostos.
