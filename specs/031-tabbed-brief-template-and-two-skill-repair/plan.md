# Technical Plan — 031

**Status:** complete — T-001..005 done; evidências aprovadas por /root em D-016
**Owner:** Guardian maintainers
**Last updated:** 2026-10-02
**Spec:** spec.md
**Impact map:** impact-map.md
**Validation plan:** validation-plan.md

## 1. Technical approach

    Fontes existentes (leitura, sem correção)
      → A: preencher template HTML padrão
      → B/high ou xhigh: skill conteúdo, comparar/corrigir HTML
      → B/high ou xhigh: skill visual, abrir abas/corrigir experiência
      → único stakeholder-brief.html + relato final

B é distinto de A e mantém identidade nas duas skills. Não há modelo
editorial obrigatório, aprovação pré-render, devolução rotineira a A,
reaprovação ou terceira validação. Inspecionar o bloco editado para concluir
sua correção integra a própria skill.

## 2. Architecture decisions

| ID | Decisão | Razão | Alternativa descartada | Consequência |
|---|---|---|---|---|
| PD-001 | Template preenchido diretamente pelo agente. | Owner remove duplicação narrativa. | Transposição literal da 030. | Slots instrutivos/casca estável. |
| PD-002 | Reutilizar três skills existentes, mandatos disjuntos. | Menos caminhos/contexto. | Somar novas skills à cadeia antiga. | Descrições/agents/workflow sincronizados. |
| PD-003 | Duas correções pós-HTML pelo mesmo B high/xhigh. | Correção na mesma passagem. | REVISE seguido de novo approve. | Conclusão de reparo, sem autoapprove de task. |
| PD-004 | Base CSS/controle nativo de abas sem JS. | Preview estático é uso real. | Painéis empilhados ou :target que desloca leitor. | Radio/label é ponto de partida; JS opcional. |
| PD-005 | Contrato 3, um eixo de versão. | Review/modelo 2 têm outra semântica. | Trocar regras 2 sem migração. | Leitura 1/2 preservada. |
| PD-006 | Conteúdo/figuras inline, fontes sistema. | Arquivo único portátil. | Rede, páginas/assets externos necessários. | Tokens visuais preservados, sem marca nova obrigatória. |
| PD-007 | Fonte/heading/bloco dentro do HTML, resumo na evidência existente. | Origem sem narrativa paralela. | Fragmento manuscrito/modelo obrigatório. | Locator válido não prova completude. |

## 3. Size and proportionality

**Initiative size:** M — uma fronteira pública de apresentação e múltiplos
mandatos/leitores acoplados; não é estimativa de duração.
**Smaller option considered:** corrigir IDs e pedir modelos mais completos;
não elimina a cadeia que o owner mandou simplificar.
**Complexity deliberately excluded:** engine, renderer Markdown, autoria de
fontes, instalação global, migração em massa e remoção física do legado.

### Architecture scope/size profile

**Profile:** M

| Dimensão | Current | Target/decision | Proof / owner |
|---|---|---|---|
| Contexto | Bundle fonte instalável. | Mesmo contexto, estado no consumidor. | Manifest — maintainers |
| Componentes | Compositor/YAML/projetor/review/promotor. | Template+compositor e duas skills corretivas. | T-001..004 |
| Contratos | Brief 1/2 e reviews a/b. | Contrato 3 autoria/conteúdo/visual. | V-012/015/017 |
| Dados | MD e metadados. | Conteúdo somente leitura; HTML derivado. | V-001 |
| Confiança | Narrativa além da fonte/approval ambíguo. | Fonte explícita; B reparador sem authority fictícia. | V-006/014 |
| Fluxo crítico | Modelo/review/projection/re-review. | A → B conteúdo → B visual → relato. | V-012 |
| Falha | REVISE devolvido ao compositor. | Reparar no passo; limite não amplia MD. | EC-001..008 |
| NFR | JS/fallback empilhado/header longo. | CSS tabs, SVG/texto e leitura proporcional. | V-002..004/007/016 |
| Migração | Checks/reviews antigos acoplados. | Version dispatch 1/2/3. | V-015 |
| Observabilidade | Estado nem sempre sincronizado. | Ator, esforço, snapshot e duas passagens. | V-011/012/014 |
| Rollback | Working tree com 029 não commitada. | Snapshot atual dos paths antes da implementação. | §8 |
| Alternativas | Literal 030 / modelo 029 mais rico. | Autoria agêntica escolhida pelo owner. | D-003 / PD-001 |
| Unknowns | Executor sem esforço/browser. | Declarar limite, sem medium/falsa conclusão. | EC-004 / R-006 |

### Current → target → delta

| View | Current | Target | Delta/commitment |
|---|---|---|---|
| Autoria | Modelo intermediário seguido de HTML. | Preencher template diretamente. | Modelo não obrigatório no contrato 3. |
| Correção | Reviewer não edita; exige re-review. | B corrige conteúdo e visual. | Sem terceiro gate. |
| Apresentação | Aba + coverage permanente/fallback empilhado. | Um painel por vez com e sem JS. | Casca corrigida, fatos recuperáveis. |
| Fontes | Reparos durante recuperação. | Read-only nesta iniciativa. | Nenhuma task altera mock MD. |

## 4. Contracts for the skills

### Conteúdo — rendered-brief-decision-review

**Entrada:** HTML, fontes aplicáveis e slots. Ler spec, impacto, plano, tasks,
validação, decisões/progresso e estado; ratchet/handoff/evidence somente
quando carregam fato material.
**Trabalho:** identificar o que deveria existir por heading/fato, comparar com
todas as abas, recuperar omissões/contradições/invenções no HTML. Paráfrase
pode mudar palavras, não apagar contrato material.
**Saída:** mesmo HTML corrigido + resumo factual/limites. Não editar MD,
emitir approve próprio, pedir re-review ou criar modelo editorial.

### Visual — executive-brief-experience-review

**Entrada:** HTML pós-conteúdo, template e fontes para preservar significado.
**Trabalho:** abrir todas as abas; corrigir hierarquia, títulos, cards/tabelas,
SVG conectado/texto equivalente, fluxo de leitura, concisão versus riqueza,
responsividade, tabs/foco/impressão. Explicar bem a spec é o critério, não
beleza isolada. Não cortar fatos para caber.
**Saída:** mesmo HTML final + resumo visual; encerrar sem repetir primeira
skill/terceira validação.

### Esforço e execução

Despachar B com high/xhigh; confirmar capacidade e registrar o nível efetivo
fornecido pelo executor. Promessa no prompt não prova esforço. Modelo
específico configurável; medium não cumpre. Não inventar API universal.

## 5. Change sequence

| Step | Superfície | Precondition | Result |
|---|---|---|---|
| 1 | Contrato/agents/workflows e dispatch | OK do owner e planejamento pronto. | Contrato 3 coerente; tasks do produto governadas. |
| 2 | Template/design/compositor | T-001 done. | HTML rico a partir de MD existentes. |
| 3 | Duas skills e handoff | T-002 done. | Conteúdo/visual corrigidos high/xhigh. |
| 4 | Leitores/promotor/checks/manifest | T-001/002 done; interfaces definidas. Pode implementar paralelo a 3; aceite exige T-003 done (D-013). | Utilitários não exigem cadeia antiga para 3. |
| 5 | Oito casos e defeitos injetados | T-001..004 done. | Aceitação da mudança do bundle. |

## 6. Compatibility and state

Não apagar schema/projetor 029 nem reescrever histórico. Entry points 3
param de exigi-los; validators 1/2 continuam. Para 3, não exigir review de
modelo, fragmento manuscrito por bloco ou approve do reparador.

Estado/evidence existentes registram snapshot e conclusão das passagens;
sem arquivo permanente de agente novo. Campos operacionais de conclusão de
reparo não equivalem a task done, owner approval ou avaliação independente.
A skill visual não autoriza executar a spec.

## 7. Security, privacy and permissions

Fontes sintéticas no aceite; nenhum upload/deploy. HTML não executa conteúdo
ativo do MD nem depende de rede. Não mudar autorização/decisão/dados.
Execução integral autorizada em D-010. Remoção
física do legado fora do MVP.

## 8. Rollout, observability and rollback

- **Checkpoint:** snapshot verificável dos paths que serão tocados antes de
  implementar; HEAD não contém a 029. Cópia segura, sem stash/reset.
- **Rollout:** contrato 3 em nova geração ou refresh explicitamente autorizado;
  não regenerar histórico em lote.
- **Signals:** três etapas, esforço efetivo, limites, fonte preservada e
  fatos materiais recuperáveis nos oito casos.
- **Rollback trigger:** perda factual, fonte alterada, ramo 3 em histórico ou
  exigência da cadeia anterior.
- **Exact rollback:** restaurar somente paths de implementação do snapshot
  pré-031, preservando 029/trabalho alheio. Não reset --hard, clean ou
  restauração ampla de HEAD.

## 9. Planning/brief disposition

Owner dispensou HTML031 (D-002). Não fabricar coverage/render/Human
Visibility. Execução autorizada em D-010; registrar a
dispensa específica sem transformar not_rendered em rendered nem marcar
gates de brief falsamente concluídos.

## 10. Plan decision

**Plan Ready:** yes
**Reviewer:** /root/review_spec031 — independente da autoria, esforço high; 2026-10-02
**Decision evidence:** evidence/planning-review.md
**Conditions:** política/fontes suficientes; OK de desenvolvimento concedido em D-010.
HTML desta iniciativa não é pré-condição (D-002).
