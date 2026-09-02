# SPEC 028 — Consolidação do pipeline de stakeholder brief

**Status:** spec_ready  
**Sequência:** 028  
**Tipo:** bugfix de processo reutilizável  
**Owner:** Guardian maintainers + responsável pela experiência do brief  
**Criada em:** 2026-09-01  
**Risco:** high  
**Assurance profile:** A2-elevated

## 1. Problema

O run de composição R2 mostrou que o bundle contém regras e verificadores úteis,
mas eles não formam uma única esteira autoritativa. Em `m003-offline`, o
`run-state.yaml` declara `brief_phase: not_rendered`, `plan_ready: false`,
`tasks_drafted: false`, `findings_status: revise` e revisão de qualidade não
iniciada. Mesmo assim, existem skeleton e candidate HTML. O decision log também
proíbe continuar para skeleton/candidate enquanto o `REVISE` estiver aberto.

O candidate passa no verificador de herança física do skeleton, mas permanece
visualmente e semanticamente inadequado: conserva texto de scaffold, repete a
mesma topologia em zooms distintos e transforma tasks em cartões-título. O
verificador de arquitetura visual não acusa nada porque o candidate não declara
que sua arquitetura é material. Não há `stakeholder-brief.html` final, e a
revisão de human visibility não foi executada.

O problema não é falta de mais um gerador ou de uma meta estética isolada. É a
falta de uma cadeia única que torne impossível confundir: plano aprovado,
candidate em avaliação, brief final revisado e Human Visibility pronto.

## 2. Objetivo

Fazer com que cada stakeholder brief percorra autonomamente uma única cadeia
auditável — fontes canônicas → plano composto suficiente → cópia física do
skeleton → candidate autorado por agente → promoção sem reautoria → revisão
independente do HTML final por HTTP local → estado de visibilidade — sem que um
artefato ou revisão fora dessa cadeia possa aparentar prontidão e sem que uma
revisão incompleta interrompa a construção do HTML mais completo possível.

## 3. Resultado de entrega

- **Resultado para usuário:** quando a SPEC tem fontes suficientes, o sistema
  entrega autonomamente o HTML final mais completo e verdadeiro que elas
  permitem. Quem o abre vê seu estado real; uma pendência não some nem exige
  que o usuário intervenha para o trabalho continuar.
- **Incremento demonstrável:** uma matriz de execução nova para M001–M008, com
  candidate/final/revisão/estado coerentes e evidência recuperável por brief.
- **Limite da entrega:** consolida orquestração, contratos e revisão. Não cria
  um gerador Markdown→HTML nem reescreve retrospectivamente evidências antigas.
- **Fonte de prioridade:** decisão humana registrada nesta conversa.

## 4. Atores

| Ator | Necessidade |
|---|---|
| Autor do plano | Traduzir fontes em um plano visual profundo antes do skeleton. |
| Agente compositor | Preencher a cópia do skeleton com narrativa, diagramas e dossiers adequados ao caso. |
| Revisor independente | Julgar, no HTML final navegável, clareza, cobertura e adequação para decisão. |
| Maintainer do harness | Ter gates e evidências coerentes, sem estruturas fantasmas. |
| Stakeholder | Entender propósito, arquitetura, impactos, execução e validação sem abrir Markdown. |

## 5. Resultados observáveis

- **O-001:** um `REVISE` oficial interrompe apenas o *gate* que ele reprova,
  nunca a execução para aguardar uma aprovação operacional do usuário. Ele
  dispara correção e nova revisão autônomas no mesmo run. Um candidate já
  composto pode ser promovido como final explicitamente não aprovado para essa
  recuperação; ele jamais salta o gate pre-skeleton nem a alegação de
  `approved`/Human Visibility.
- **O-002:** cada candidate possui proveniência verificável do plano, da cópia
  do skeleton e da decisão pre-skeleton que o permitiu.
- **O-003:** o renderer continua somente promovendo bytes e metadados aprovados;
  ele não finge ser uma etapa de melhoria visual.
- **O-004:** a aprovação final depende de uma revisão independente do HTML
  servido em loopback HTTP, com URL, ambiente, digest e decisão registrados.
- **O-005:** quando arquitetura, tasks ou provas são materiais, as regras já
  existentes passam a ser acionadas e sua ausência precisa ser declarada como
  N/A ou discovery com impacto decisório.
- **O-006:** uma lacuna de fonte vira uma ausência/discovery visível com impacto
  e próximo passo, nunca uma interrupção silenciosa ou uma pergunta ao usuário
  final durante a construção normal.

## 6. Não objetivos

- **NG-001:** criar código determinístico que escreva narrativa, escolha
  diagramas, resuma specs ou monte o HTML final.
- **NG-002:** introduzir score de “beleza”, cota fixa de cards/gráficos ou um
  template visual específico de fornecedor.
- **NG-003:** tornar responsividade mobile ou breakpoints parte deste escopo;
  a avaliação solicitada é desktop.
- **NG-004:** declarar o R2 histórico válido, alterar seus logs ou mascarar suas
  falhas por arquivos de exceção.
- **NG-005:** substituir o julgamento qualitativo independente por testes
  estáticos.
- **NG-006:** transformar o usuário final em aprovador operacional de plano,
  skeleton, candidate ou remediação; sua autorização só é necessária quando
  houver uma decisão de escopo/autoridade fora das fontes.

## 7. Requisitos funcionais

| ID | Requisito | Racional |
|---|---|---|
| FR-001 | Quando uma decisão pre-skeleton estiver `REVISE`, o sistema deve registrar o achado, corrigir o plano e pedir nova revisão no mesmo run; não aguarda aprovação operacional do usuário. Quando um candidate já existir e a revisão posterior for `REVISE`, pode promover uma versão final explicitamente não aprovada para recuperação, recusando `approved`/Human Visibility. | Preserva a autoridade do gate sem deixar um candidate fonte-apoiado sem superfície de revisão. |
| FR-002 | O candidate deve ligar plano composto, decisão pre-skeleton e cópia física do skeleton à sua proveniência. | Herança visual sem autorização de ciclo não é suficiente. |
| FR-003 | A promoção para `stakeholder-brief.html` deve ser explicitamente uma operação de lifecycle/bytes, sem autoria ou “polimento” de conteúdo. | Impede expectativa falsa de uma segunda transformação qualitativa. |
| FR-004 | Todo brief final que solicitar aprovação de Human Visibility deve ser revisado em URL HTTP local por revisor distinto do autor. | Testa a experiência que o stakeholder realmente abre. |
| FR-005 | Arquitetura material deve declarar sua disposição visual e cumprir o contrato de arquitetura; N/A ou discovery deve ser explícito e ter razão. | Impede omissão silenciosa de topologias/zooms necessários. |
| FR-006 | As projeções de execução e validação devem recuperar dossiers fonte-definidos de tasks e provas, não apenas IDs ou títulos. | Preserva entendimento, critérios e evidência no brief. |
| FR-007 | Cada mock deve reportar separadamente checks determinísticos e decisão qualitativa humana/agêntica. | Um PASS técnico não pode parecer aprovação de experiência. |
| FR-008 | O requisito desktop de rotas internas por abas e a política de fallback sem JavaScript devem ter contrato explícito e não contraditório. | Evita uma página longa como degradação que invalida a intenção. |
| FR-009 | Havendo fontes canônicas legíveis, o sistema deve completar plano suficiente, candidate, revisão e HTML final sem aguardar aprovação do usuário final; revisões retornam ao compositor automaticamente. | A esteira precisa chegar ao fim sozinha. |

## 8. Critérios de aceite

| ID | Critério | Validação inicial |
|---|---|---|
| AC-001 | Um fixture pre-skeleton com `REVISE` registra correção e nova revisão automáticas antes de instanciar o skeleton; um fixture de revisão posterior com candidate fonte-apoiado produz final marcado como não aprovado. Nenhum dos dois declara `approved`/Human Visibility. | V-001 |
| AC-002 | Estado, decision log, attestation, digests e fase do brief não aceitam combinação contraditória. | V-002 |
| AC-003 | O brief final abre em HTTP local e alterna uma rota interna por vez; a rota ativa é recuperável pela URL. | V-003 |
| AC-004 | Para arquitetura material, uma cadeia textual repetida não satisfaz o contrato de visualização e os zooms recuperam mudança, fronteira preservada e vínculo com trabalho. | V-004 |
| AC-005 | Ausência de preview, revisor, digest ou decisão independente mantém o brief não aprovado. Se já houver candidate com fontes, skeleton e decisão recuperáveis, gera a versão final mais completa com limitação explícita; se não houver essa base, recupera-a autonomamente antes de renderizar. | V-005 |
| AC-006 | Tasks e provas materiais mantêm objetivo, anti-escopo, dependência/controle, critério, evidência e próximo gate recuperáveis no HTML final. | V-006 |
| AC-007 | Uma execução fresca M001–M008 produz HTML final e matriz de evidências para cada mock; o estado `approved` só aparece após revisão, mas um `REVISE` aciona recomposição sem pedir decisão ao usuário. | V-007 |
| AC-009 | Em uma SPEC com fontes legíveis e achados de revisão, ao menos uma recomposição automática ocorre e termina em final aprovado ou final completo com limitações explicitadas. | V-009 |
| AC-008 | A validação do bundle continua verde e não há novo gerador de conteúdo HTML baseado em Markdown. | V-008 |

## 9. Casos de borda e falha

| ID | Condição | Comportamento esperado |
|---|---|---|
| EC-001 | Preview HTTP local indisponível | Gerar o final; registrar motivo, limitação e retorno de recuperação, sem inventar aprovação/Human Visibility. |
| EC-002 | A spec não revela arquitetura suficiente | Declarar discovery com owner, consequência e próximo passo no final; não desenhar arquitetura fictícia nem interromper o restante. |
| EC-003 | A arquitetura é comprovadamente não material | Registrar N/A fonte-apoiado e não forçar diagrama decorativo. |
| EC-004 | JavaScript desabilitado | Aplicar a política desktop explicitamente decidida; não usar fallback long-page para afirmar equivalência se ele contradiz as abas. |
| EC-005 | Candidate existe sem attestation válida | Reconstituir proveniência e repetir a revisão antes de promover. Uma versão não aprovada só é permitida quando o candidate já vincula fontes, skeleton e decisão recuperáveis. |
| EC-006 | Um revisor pede correção | O resultado volta automaticamente ao authoring/composição; o renderer não altera conteúdo e o usuário não precisa aprovar a correção. |

## 10. Restrições e NFRs

- **Arquitetura:** manter uma cadeia simples e aproveitando `run-state`, decision
  log, skeleton, inheritance checker, renderer, contracts e review já existentes.
- **Autoria:** plano e HTML final são produzidos por agentes; automação só
  coordena, verifica identidade/estado/forma e captura evidências.
- **Design:** vendor-neutral por padrão, salvo seleção canônica explícita; não
  há redesign de marca neste trabalho.
- **Compatibilidade:** foco desktop; preservar navegação por URL, teclado e
  impressão/texto conforme o contrato resolvido para fallback.
- **Operação:** preview local não é deploy nem publicação externa.
- **Resiliência:** checks determinísticos podem bloquear uma afirmação de
  aprovação ou a passagem de um gate; nunca criam uma espera passiva. Toda
  falha retorna a correção/revisão no mesmo run. Um HTML final com limitação só
  é permitido a partir de um candidate já rastreável; não é uma rota para pular
  skeleton, proveniência ou autoridade.

## 11. Premissas

| Premissa | Validação/owner |
|---|---|
| O v3 skeleton permanece a base física de todo candidate. | T-001 / maintainer. |
| `render_stakeholder_brief.py` pode continuar como promoção, não autoria. | T-001 / maintainer. |
| A revisão independente consegue ser registrada em artefato com digest e URL local. | T-003 e T-004. |
| Alguns componentes/skills atuais podem ser órfãos ou opcionais. | T-004 inventaria antes de remover ou tornar obrigatório. |

## 12. Riscos

| ID | Risco | Prob. | Impacto | Mitigação/owner |
|---|---|---:|---:|---|
| R-001 | Criar outro gate paralelo ou uma barreira burocrática. | média | alto | Um único estado, gates apenas para alegação de aprovação e recuperação autônoma; T-001. |
| R-002 | Supercorrigir com gerador rígido ou score visual. | média | alto | Limites explícitos de autoria agêntica; T-002. |
| R-003 | Resolver somente o M003. | média | alto | Matriz fresca M001–M008; T-005. |
| R-004 | Confundir presença de HTML com Human Visibility, ou bloquear o HTML por falta de Human Visibility. | alta | alto | Final sempre é gerado; revisão HTTP só governa o rótulo de aprovação; T-003/T-004. |
| R-005 | Regra de fallback contradizer abas reais. | média | médio | Decisão arquitetural explícita antes de mudança; T-001. |

## 13. Dependências

| Dependência | Estado | Owner | Bloqueante? |
|---|---|---|---|
| `.harness/templates/stakeholder-brief-design.md` e skeleton v3 | existente | Guardian | sim |
| `validate_brief_candidate_inheritance.py` | existente, insuficiente sozinho | Guardian | sim |
| `architecture_visual_contract.py` | existente, precisa conexão | Guardian | sim |
| `render_stakeholder_brief.py` e Human Visibility | existentes, lifecycle | Guardian | sim |
| `rendered-brief-decision-review` | existente, precisa rota oficial | Guardian | sim |
| suíte M001–M008 | existente | mock lab | sim |

## 14. Notas de validação

O plano de validação distingue deliberadamente duas classes: checks
determinísticos provam estado, proveniência, rota e forma mínima; revisão
independente prova inteligibilidade, storytelling, diagramação proporcional e
adequação para decisão. Uma não substitui a outra, e nenhuma deve impedir que
fontes legíveis sejam transformadas em HTML final; elas apenas determinam o
estado exibido e a recuperação autônoma seguinte.

## 15. Decisão do Spec Guardian

**Outcome Ready:** yes — direção humana confirmada.  
**Spec Ready:** yes — pronta para autorização explícita de execução.  
**Bloqueios:** nenhum bloqueio burocrático de autoria; a execução aguarda apenas a autorização solicitada pelo usuário nesta conversa.  
**Evidência:** decisão humana desta conversa + reprodução documentada em `./reproduction.md`.
