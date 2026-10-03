# SPEC 030 — Projeção direta dos Markdown no stakeholder brief

**Status:** superseded pela SPEC 031 em 2026-10-02; rascunho preservado como histórico.
**Tipo:** refactor · **Risco:** medium · **Assurance:** A2-elevated
**Criada em:** 2026-09-23 · **Owner:** Guardian maintainers
**Antecessora:** SPEC 029 (`validation_done`)

> Rascunho deliberadamente enxuto, escrito sob limite de tokens. Contém o
> conteúdo de valor. `impact-map.md`, `plan.md`, `validation-plan.md`,
> `tasks.md` e revisões independentes ainda precisam ser completados.

> Direção substituída pelo pedido do owner em 2026-10-02: autoria agêntica sobre template HTML com abas e duas skills corretivas. Ver `specs/031-tabbed-brief-template-and-two-skill-repair/spec.md`. Não executar este rascunho. Nenhuma implementação da 030 foi iniciada.

## 1. Problema

O brief gerado pela SPEC 029 (`specs/029-.../stakeholder-brief.html`, T-010)
foi reprovado pelo owner em 2026-09-23. Achados verificados:

1. **Resumo em vez de fato.** As fontes Markdown da 029 somam ~129 mil chars
   (`spec.md` 36,6k, `tasks.md` 33,7k, `decision-log.md` 22,1k, `plan.md`
   16,3k, `validation-plan.md` 11,8k, `impact-map.md` 8,9k). O brief exibe
   ~21,5 mil chars de texto visível (~17%), e nenhum deles é o Markdown: são
   21 resumos escritos à mão pelo agente em `brief-model.yaml` (29k chars).
   O agente escreve mais do que o brief mostra, para dizer menos do que as
   fontes já dizem. É a camada onde fato se perde e token se gasta.
2. **Abas quebradas na prática.** Sem JS (como o owner abriu: arquivo
   estático / preview), todas as seções aparecem empilhadas e as abas viram
   links `?view=` que só deslocam a página. É o fallback no-script por
   desenho, mas é a experiência padrão nos visualizadores usados.
3. **Bug de duplicação.** `scripts/project_brief.py` emite a rota
   `coverage` duas vezes (linha ~760 força uma coverage mesmo quando o modelo
   já declara). Resultado: `id="coverage"` e `id="tab-coverage"` duplicados;
   com JS ativo, a cópia nunca é escondida — duas seções visíveis ao mesmo
   tempo. Verificado servindo em `127.0.0.1:4173`.
4. **Título genérico.** `<title>` saiu "software brief" (derivado de
   `domain`), não o nome da iniciativa.
5. **Testes não pegaram nada disso**, porque checam atributos de
   proveniência, não o que a pessoa vê.

## 2. Objetivo

O brief mostra o **conteúdo factual dos Markdown canônicos, transposto quase
literalmente**, organizado nas abas por um mapeamento fixo de fonte/seção →
aba. O agente só autora o que não existe nas fontes: resumo executivo curto e
o desenho de arquitetura. Qualidade factual primeiro; beleza visual é SPEC
posterior (decisão do owner: aceita-se visual "tosco" em troca de fato).

Critério de sucesso herdado de D-033 da 029: menos custo operacional
recorrente por brief (menos tokens de autoria, menos retrabalho).

## 3. Proposta

### 3.1 Transposição, não resumo
- Um renderizador Markdown→HTML determinístico converte seções inteiras
  (títulos, subtítulos, parágrafos, bullets, tabelas, blocos de código).
- Isso **não** viola NG-001 da 029 ("código não resume nem narra"):
  transpor não é resumir. Registrar essa leitura em decisão.
- Proveniência sai de graça: cada bloco *é* a seção de origem. Manter
  `data-source`, `data-source-section`, `data-coverage` e
  `data-source-digest` por seção.
- **Fragmento vira automático, não some.** `validate_human_visibility.py`
  (linhas ~716 e ~785) e `render_stakeholder_brief.py` ainda **exigem**
  `data-source-fragment` + SHA-256 em blocos v2; removê-lo quebra a
  validação. Solução barata: o fragmento de cada seção passa a ser o texto
  literal do próprio heading (garantido estar na fonte e no bloco visível).
  Custo de autoria zero; validadores seguem passando. O que se remove é a
  **autoria manual** de fragmento pelo agente, não o atributo.

### 3.2 Mapeamento fonte → aba (proposta inicial, ajustável)
| Aba | Fonte / seções |
|---|---|
| Valor e escopo | `spec.md` §Problema, §Objetivo, §Resultado de entrega, §Atores, §Não objetivos |
| Arquitetura | desenho autorado pelo agente + `plan.md` §decisões/arquitetura |
| Impacto | `impact-map.md` inteiro (superfícies, riscos, unknowns) |
| Execução | `tasks.md` (ledger + uma seção recolhível por task) |
| Validação | `validation-plan.md` (rastreabilidade AC→V, regressão, comandos) + `spec.md` §Critérios de aceite |
| Evolução | `decision-log.md` + `progress.md` |
| Decisão | estado dos gates (`run-state.yaml`) + próximo passo |
| Cobertura | tabela gerada: cada fonte/seção → aba onde aparece |

O mapeamento é dado (arquivo de configuração no bundle), não código de
negócio. Seção de fonte não mapeada deve aparecer em "Cobertura" como não
exibida, nunca sumir em silêncio.

### 3.3 Volume
`tasks.md` sozinho tem ~34k chars. Seções longas entram em `<details>`
recolhidos por padrão, com título visível. Sem isso a página afoga o leitor.

### 3.4 Papel do agente (única autoria)
- **Resumo executivo** no topo (poucas frases: decisão pedida, estado,
  riscos principais).
- **Arquitetura**: nós/arestas (reaproveitar o SVG de `topology` já
  existente em `project_brief.py`/T-003).
- Nada mais. Todo o resto é transposição.

### 3.5 Correções obrigatórias
- Remover a emissão duplicada de `coverage` em `project_brief.py`.
- `<title>` = nome/ID da iniciativa, não o `domain`.
- **Abas precisam funcionar sem depender de JS no visualizador do owner.**
  Recomendação: abas CSS-only no padrão radio + label, com JS apenas como
  melhoria opcional. `:target` está descartado porque rola a página
  (detalhe em 9.3).

## 4. Não objetivos
- Melhoria visual/identidade (SPEC futura).
- Reescrever briefs históricos (NG-004 da 029 continua).
- Gerar narrativa por código.

## 5. Critérios de aceite (essenciais)
- **AC-1** Todo parágrafo/bullet/linha de tabela das seções mapeadas aparece
  no HTML (check: texto normalizado da seção-fonte ⊂ texto do painel).
- **AC-2** Nenhuma seção de fonte some em silêncio: toda seção não mapeada
  aparece listada em Cobertura.
- **AC-3** Zero `id` duplicado no HTML (check automático).
- **AC-4** Abas trocam de painel com JS desabilitado, e só um painel visível
  por vez (verificar em visualizador estático, não só via HTTP).
- **AC-5** `<title>` contém o ID da iniciativa.
- **AC-6** Autoria do agente limitada a resumo executivo + arquitetura;
  medir tokens de autoria vs. os 29k do `brief-model.yaml` da 029.
- **AC-7** Regenerar o brief da própria 029 e o da 030 pela nova esteira; o
  owner aprova a leitura factual.
- **AC-8** Suíte atual verde (85 testes, 314 checks em 2026-09-23), sem
  regressão; remoções de código morto contam a favor.

## 6. Riscos
- **R-1** Transpor 129k chars gera página longa demais → mitigado por
  `<details>` e ordem de leitura por aba.
- **R-2** Markdown com HTML/`<>` literais: o renderizador deve escapar
  corretamente. Relacionado ao bug conhecido da 029 (`_verify_fragment_visible`
  compara fragmento cru com HTML escapado). Como o fragmento continua
  existindo (automático, pelo heading), esse bug **precisa ser corrigido**:
  heading com `<`/`>` literal faria a verificação recusar.
- **R-3** `decision-log.md` real é tabela plana, sem heading por decisão
  (achado da 029/T-010) → o mapeamento precisa tratar tabela como unidade.
- **R-4** CSS-only tabs perdem estado na URL/teclado → validar a11y básica.

## 7. Pendências herdadas da 029 (não bloqueiam)
- AC-009b da 029 (doutrina por papel ≤15k) segue não atingido (D-025).
- IR-003 da 029 (inventário de fontes SDD-shaped) segue aberto (D-028/D-029).

## 8. Lições a respeitar na execução (ratchet da 029)
- Verificar baseline com `git worktree add --detach <dir> HEAD` + copiar
  arquivos não commitados (`.harness/`, `schemas/`, `scripts/`, `specs/029*`,
  `specs/030*`, `testes/`). Nunca `git stash` (R-029-001).
- Subagente que diz "deleguei" pode deixar processo órfão rodando (R-029-002).
- `pytest scripts/` não coleta todos os `test_*.py`; rodar standalone.
- Nada da 029 está commitado ainda.

## 9. Detalhamento técnico (verificado em 2026-09-23)

### 9.1 Renderizador Markdown
- `markdown` 3.6 e `mistune` estão instalados no ambiente de
  desenvolvimento, mas o bundle roda instalado em projetos consumidores
  (`vendor/sdd-harness-guardian`). Decidir no plano: declarar a dependência
  ou escrever um renderizador mínimo em stdlib. Recomendação: renderizador
  mínimo próprio, porque o subconjunto usado é pequeno e previsível, e o
  bundle hoje é Python puro.
- Recursos que **precisam** funcionar, medidos nas fontes da 029: tabelas
  (356 linhas), checkboxes `- [x]`/`- [ ]` (63, só em `tasks.md`), pipe
  escapado `\|` em célula (1 caso), `code spans`, negrito, links, listas
  numeradas, blocos de código cercados. Nenhum `<br>` nem bullet aninhado
  nas fontes atuais, mas o renderizador não deve quebrar se aparecerem.
- Escapar HTML do conteúdo antes de renderizar (fontes podem ter `<` e
  `>` literais, ex.: `<initiative>`, `<dir>`). É o mesmo defeito que a 029
  achou em `_verify_fragment_visible`; aqui ele não pode se repetir.
- Cabeçalhos das tabelas e do Markdown ficam como estão (em PT); só os
  rótulos de aba do shell são fixos. Decidir idioma dos rótulos (hoje EN:
  "Value & scope") — recomendação: PT, porque as fontes são PT.

### 9.2 Unidade de mapeamento
- Unidade = seção H2 (`## ...`) de um arquivo fonte, com tudo que vem
  abaixo até o próximo H2. Arquivos sem H2 útil (ex.: `decision-log.md`,
  que é uma tabela plana sob um único H1) entram inteiros como uma unidade.
- Ordem dentro da aba = ordem de origem no arquivo.
- Uma seção pode aparecer em uma única aba (sem duplicar conteúdo). A aba
  Cobertura lista toda seção de toda fonte com o destino ou "não exibida".
- Cada seção ganha âncora estável (`#<arquivo>-<slug-do-heading>`) e um link
  "fonte" para o arquivo `.md`.
- Mapeamento vive em arquivo de dados no bundle (ex.:
  `.harness/templates/brief-section-map.yaml`), com padrões por nome de
  heading (numerado ou não, ex.: "1. Problema" e "Problem"), e pode ser
  sobrescrito por iniciativa só se necessário.

### 9.3 Abas sem JS
- `:target` resolve troca de painel sem JS, mas **rola a página até o
  alvo**, que é exatamente a reclamação do owner. Não usar.
- Recomendação: padrão radio + label (`<input type="radio" name="tab">` +
  `:checked ~` seletores). Troca sem scroll, sem JS, um painel por vez.
- JS opcional só para: `?view=` na URL, setas do teclado, voltar/avançar.
- Print: todos os painéis visíveis e `<details>` abertos.
- Testar em três contextos: arquivo estático (preview), HTTP com JS, HTTP
  sem JS. O teste da 029 só olhou atributos; aqui o check tem que abrir a
  página e contar painéis visíveis.

### 9.4 O que muda no que a 029 construiu
- **Fica:** shell/CSS do template, eixo `data-brief-contract`, digest de
  fonte, renderizador SVG de `topology`/`sequence` (T-003), check de
  suficiência de fontes (T-006) antes da projeção, lifecycle/attestation de
  `render_stakeholder_brief.py`, `resolve_locator` com guarda de colisão
  (T-002) para resolver headings.
- **Encolhe:** `brief-model.yaml` passa a ter só `thesis`/resumo
  executivo, `relations` (arquitetura) e, opcionalmente, overrides de
  mapeamento. O schema (`schemas/brief-model.schema.json`) e
  `validate_brief_model.py` encolhem junto.
- **Sai:** autoria de `text` por bloco, enumeração de `form` por bloco
  (as formas `dossier`, `matrix`, `footprint`, `risk-chain` deixam de ser
  escolhidas pelo agente; tabelas do Markdown já são a forma), fragmento
  manual, e os testes/fixtures que só existiam para isso.
- Remoção de arquivo exige aprovação do owner (invariante do bundle).

### 9.5 Doutrina
- `.harness/rules/brief-contract.md` tem regras sobre autoria por bloco,
  formas e fragmentos (BC-013, BC-022, BC-023 e vizinhas). Precisam ser
  reescritas para o modelo novo, e a SKILL
  `executive-brief-composition/SKILL.md` encolhe muito (o compositor quase
  não autora mais).
- Passagem (a) da cadeia de revisão (BC-009) passa a revisar: mapeamento,
  resumo executivo e arquitetura. Passagem (b) continua no HTML renderizado.
- Oportunidade: com menos regra de autoria, AC-009b da 029 (doutrina ≤15k
  chars por papel) pode finalmente ser atingível. Medir.

### 9.6 Corpus de teste disponível
- Fontes reais: `specs/029-*` e `specs/030-*` (esta).
- Oito iniciativas de mock com fontes completas:
  `testes/mock-runs/20260921-spec029-t009-m00{1..8}/initiative/`.
  Regenerar os oito pela esteira nova e comparar com os HTMLs da 029
  (`specs/029-*/evidence/t009-matrix/M-00N.html`): o novo deve mostrar
  mais conteúdo factual com menos autoria.
- Atenção: M-005 e M-006 compartilham tabela de impacto genérica
  (achado da 029, D-034). A transposição vai exibi-la como está; isso é
  correto (fonte fraca fica visível), não defeito do projetor.

## 10. Sugestão de tasks (a validar no plan/tasks)
1. Renderizador Markdown mínimo + testes com os recursos de 9.1.
2. Mapa seção→aba em dados + resolução por heading + aba Cobertura.
3. Projetor: transposição + fragmento automático pelo heading + corrigir
   `coverage` duplicado + `<title>` com ID da iniciativa.
4. Abas radio/label sem JS + check que conta painéis visíveis em estático.
5. Encolher `brief-model.yaml`/schema/validador ao resumo + arquitetura.
6. Reescrever doutrina (BC-009/013/022/023, SKILL do compositor) e medir
   AC-009b.
7. Remoção do código morto de autoria por bloco (destrutiva, aprovação).
8. Regenerar 029, 030 e M-001…M-008; revisão independente + owner.
