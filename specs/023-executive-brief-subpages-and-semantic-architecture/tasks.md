# Task ledger — SPEC 023

## Contrato de autorização A2

As tarefas abaixo são contratos preliminares de assurance A2-elevated. Estão em
`pending`: D-023-001 permite preparar coverage/review, mas não iniciar task.
Cada uma só pode virar `ready` após **Brief Coverage Ready**, **Human Visibility
Ready** e a propagação da decisão de reunião que produz **Tasks Ready**. Builder
e evaluator são distintos; nenhum parecer semântico, visual ou de evidência
pode ser emitido pelo próprio builder.

Os papéis novos permanecem isolados dos existentes: `brief-experience-composer`
prepara mapas editoriais/candidatos; `executive-brief-reviewer` julga
profundidade, fontes e experiência de reunião. Não são fontes canônicas e não
alteram skills Guardian existentes.

## T-001 — Contrato editorial e fixtures de arquitetura explicável

- **Outcome:** permitir uma leitura executiva fonte-apoiada, inclusive quando a
  arquitetura é material, operacional ou insuficientemente descrita, sem que o
  renderer infira fatos.
- **Demonstrable increment:** formato revisável de mapa editorial e fixtures
  positivas, negativas e de descoberta demonstram tese, pilares, proveniência,
  change map, escala com unidade e zoom/N/A honesto.
- **FR / AC / V:** FR-023-04 a FR-023-07; AC-023-03 a AC-023-05; V-023-03 a
  V-023-05.
- **Scope / anti-scope:** definir entrada, fonte/locator por afirmação, síntese
  permitida, limite e discovery owner; cobrir arquitetura material, detalhe
  interno ausente, escala sem unidade, zero falso e não software. Não renderiza
  página, muda CSS/router/brief histórico, classifica materialidade ou infere
  frontend/qualidade por heurística.
- **Dependências:** D-023-001, gates v2 liberadas, provenance v2 existente;
  não inicia com coverage em `REVISE`.
- **Arquivos / superfícies esperados:** novas skills isoladas em
  `.harness/skills/executive-brief-composition/` e
  `.harness/skills/executive-brief-experience-review/`, papéis isolados em
  `.harness/agents/`, suporte existente de composição/validação,
  `scripts/fixtures/` e/ou `testes/mock-tests/`, testes correspondentes e
  `evidence/T-001.md`. Nomes de schema/helper seguem superfícies existentes.
- **Risco / assurance:** R-023-01/R-023-02, A2-elevated; testes recusam forma
  inválida, mas julgamento agêntico distinto decide se a explicação fabrica
  topologia ou vira formulário determinístico.
- **Papéis isolados:** builder `spec023-editorial-contract-builder` usa
  `brief-experience-composer`; evaluator
  `spec023-editorial-contract-evaluator` usa `executive-brief-reviewer` e não
  corrige durante o parecer.
- **Validation / evidence:** V-023-03/04/05; anexar mapa, fonte/locator,
  testes de integridade e parecer APPROVE/REVISE em `evidence/T-001.md`.
- **Why now:** funda T-002/T-003 sem transformar layout em explicação ou criar
  arquitetura por rótulo.
- **Exit criteria:** fixtures cobrem os casos; FR/AC/V têm evidência; N/A e
  discovery não fabricam fato; evaluator distinto aprova pack, permitindo o
  fluxo oficial `needs_evaluation → approved → done`.
- **Failure / revision behavior:** locator ausente, contagem falsa, zoom
  especulativo ou REVISE devolve a `in_progress`; builder repara o ponto,
  registra-o, pede novo parecer; recorrência alimenta `ratchet.md`.

## T-002 — Shell Pearson e router de subpáginas internas

- **Outcome:** um único HTML navega como domínios integrais, com Pearson local
  e acesso progressivo, sem perturbar MDs ou a camada de composição.
- **Demonstrable increment:** cada rota substitui a região principal completa;
  URL/histórico, foco, teclado, no-script, impressão e reduced motion provam
  que não se trata de âncora ou scroll disfarçado.
- **FR / AC / V:** FR-023-01, FR-023-03, FR-023-08, FR-023-09; AC-023-01,
  AC-023-02, AC-023-06; V-023-01, V-023-02, V-023-06.
- **Scope / anti-scope:** adaptar shell/projeção existentes para rota, região
  exclusiva, histórico/foco/semântica e sistema Pearson local, com composição
  mais vertical quando necessário; exibir responsável somente fonte-apoiado.
  Não cria HTML por rota, avatar/login decorativo, recurso remoto, nova fonte
  canônica, conteúdo de caso real, migração histórica ou mudança de skills.
- **Dependências:** T-001 aprovado, D-023-001, gates v2 liberadas, Pearson e
  fallback v2 existentes; bloqueada enquanto T-001/coverage estiverem em review.
- **Arquivos / superfícies esperados:**
  `.harness/templates/stakeholder-brief.html`,
  `.harness/templates/stakeholder-brief-design.md`,
  `scripts/render_stakeholder_brief.py`, testes renderer/browser já existentes,
  ativos Pearson autorizados, capturas e `evidence/T-002.md`; nenhum framework
  ou biblioteca de componentes nova é presumida.
- **Risco / assurance:** R-023-03/R-023-04, A2-elevated; testes verificam
  comportamento/a11y e evaluator distinto revisa visual Pearson, sem score
  estético.
- **Papéis isolados:** builder `spec023-subpage-shell-builder`; evaluator
  `spec023-subpage-shell-evaluator`, com lente `executive-brief-reviewer`, não
  edita template/script/CSS durante avaliação.
- **Validation / evidence:** V-023-01/02/06; capturas por rota em
  320/768/1024/1440, 200%, teclado, no-script, print, reduced motion,
  URL/histórico, ativo local e parecer em `evidence/T-002.md`.
- **Why now:** fornece o domínio inteiro onde T-003 põe explicação humana sem
  amontoar rotas numa rolagem.
- **Exit criteria:** sem `scrollIntoView` na navegação principal, nem corpo
  inativo exposto; fallback/print completos; Pearson local; evidência e parecer
  distintos aprovados antes do fluxo oficial até `done`.
- **Failure / revision behavior:** falha de rota/foco/no-script/print/
  responsividade/contraste/Pearson volta a `in_progress`; builder corrige e
  acrescenta regressão aplicável; evaluator reavalia sem corrigir.

## T-003 — Composição executiva, topologia, change map e zoom

- **Outcome:** cada domínio passa a explicar decisão humana; Arquitetura
  localiza mudança, preservação, escala e detalhe apenas na profundidade que o
  corpus sustenta.
- **Demonstrable increment:** candidatos heterogêneos têm abertura própria
  (tese, pilares, limite, próximo passo), macro/change map/escala/zoom nos
  materiais e N/A/discovery explícitos nos demais, todos revisáveis por fonte.
- **FR / AC / V:** FR-023-02, FR-023-04 a FR-023-07, FR-023-09, FR-023-10;
  AC-023-03 a AC-023-05; V-023-03 a V-023-05.
- **Scope / anti-scope:** integrar contrato aos oito domínios; compor títulos,
  teses, pilares, decisão, limite e próximo passo; projetar relações declaradas
  em macro, superfície, escala (unidade/denominador) e zoom condicional;
  registrar lacuna/owner. Não usa palavras-chave, diagramas obrigatórios,
  contagem de arquivos/LOC sem fonte, narrativa genérica ou reescrita canônica.
- **Dependências:** T-001/T-002 aprovados, gates v2 liberadas e corpus/locators
  confirmados; falta de suporte produz N/A/discovery, não especulação.
- **Arquivos / superfícies esperados:** projeção/orientações existentes de
  renderer/template, mapa editorial por candidato, suporte declarativo de
  topologia/superfície/escala/zoom/proveniência, fixtures/testes de T-001,
  reviews e `evidence/T-003.md`; não cria subsistema não declarado pelas fontes.
- **Risco / assurance:** R-023-01/R-023-02/R-023-05, A2-elevated; composição
  agêntica profunda e revisão independente por fontes/renderização, nunca gate
  de qualidade por contagem/léxico.
- **Papéis isolados:** builder `spec023-executive-composition-builder` usa
  `brief-experience-composer`; evaluator
  `spec023-executive-composition-evaluator` usa `executive-brief-reviewer`,
  confronta pedido/fontes/mapa/HTML e não modifica candidato.
- **Validation / evidence:** V-023-03/04/05 em dois casos materiais e um
  operacional/não software; anexar candidata, mapa, fonte→locator, macro/change
  map/escala/zoom ou N/A e parecer/reparos em `evidence/T-003.md`.
- **Why now:** é a camada adicional sobre os MDs que torna informação uma
  explicação de reunião, depois de contrato e subpágina prontos.
- **Exit criteria:** oito rotas têm início/fim próprios quando suportado; casos
  demonstram profundidade proporcional; toda quantidade declara
  unidade/denominador/fonte ou discovery; parecer distinto aprova antes de
  `done`.
- **Failure / revision behavior:** tese genérica, visual sem locator,
  arquitetura fabricada, escala ambígua, lacuna escondida ou REVISE retorna a
  `in_progress`; builder repara blocos apontados e pede revisão nova; recorrência
  entra no ratchet.

## T-004 — Recompose, revisão C-level e adoção controlada

- **Outcome:** demonstrar em corpus diverso experiência executiva vertical,
  profunda e preservadora de proveniência/lifecycle/fontes, decidindo
  explicitamente sua adoção.
- **Demonstrable increment:** M-001–M-008 recompostos em raiz nova recebem
  review independente de cinco lentes e decisão por artefato (adotar, refresh,
  manter histórico ou revisar), com regressões e limites.
- **FR / AC / V:** FR-023-01 a FR-023-10; AC-023-01 a AC-023-08; V-023-01 a
  V-023-08.
- **Scope / anti-scope:** recompose em raiz nova; verificar navegação, a11y,
  proveniência, arquitetura proporcional e Pearson; revisar contra pedido,
  fontes, rota e HTML; registrar decisão/migração/limites/regressão. Não promove
  automaticamente, sobrescreve histórico, reestiliza em massa, aceita screenshot
  como prova, certifica arquitetura externa nem permite correção pelo reviewer.
- **Dependências:** T-003 aprovado, gates v2 liberadas, raiz nova M-001–M-008 e
  decisão de refresh/migração quando necessária; ausência de erro técnico não
  promove baseline.
- **Arquivos / superfícies esperados:** nova raiz em `testes/mock-runs/`,
  regressões bundle/renderer, capturas/PDFs, decisões/evidências e
  `evidence/T-004.md`; apenas candidatos nessa raiz, sem mutação de brief
  histórico/pinned sem decisão posterior.
- **Risco / assurance:** R-023-01 a R-023-05, A2-elevated; regressão técnica,
  proveniência e five-lens humano/agêntico provam mais que uma suíte verde.
- **Papéis isolados:** builder `spec023-recompose-builder`; evaluator
  `spec023-c-level-evaluator`, distinto, usa `executive-brief-reviewer`, não
  edita candidato e escala decisão de migração não autorizada.
- **Validation / evidence:** V-023-01 a V-023-08 e regressões aplicáveis;
  conservar por M-001–M-008 hash/digests, fontes, lifecycle, capturas e parecer
  de propósito/perímetro/trade-off/próxima ação/confiança. Consolidar decisões,
  falhas/reparos/limites em `evidence/T-004.md`; `validate_bundle.py` é só prova
  estrutural.
- **Why now:** verifica generalidade e qualidade C-level antes de qualquer
  promoção ou migração histórica.
- **Exit criteria:** oito casos têm evidência proporcional, sem perda de fonte/
  lifecycle; parecer independente e decisão explícita por artefato; regressões
  passam; REVISE resolvido/reavaliado ou explicitamente não adotado; então segue
  o fluxo oficial até `done`.
- **Failure / revision behavior:** regressão, perda de fonte, rota parcial ou
  REVISE retorna a `in_progress`; builder repara, anexa pack e pede reavaliação.
  Migração ausente mantém histórico intacto; recorrência atualiza ratchet.

Nenhuma task está `ready`, `in_progress`, `approved` ou `done`. D-023-001 não
transforma mock/candidate/screenshot em evidence nem contorna coverage, review
distinto, renderização, decisão de reunião e Tasks Ready.
