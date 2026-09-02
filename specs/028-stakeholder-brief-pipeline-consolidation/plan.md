# Plano técnico — SPEC 028

**Status:** plan_ready  
**Spec:** ./spec.md  
**Impact map:** ./impact-map.md  
**Validation plan:** ./validation-plan.md  
**Owner:** Guardian maintainers  
**Última atualização:** 2026-09-01

## 1. Abordagem técnica

Esta SPEC reduz fragmentação; não acrescenta uma camada concorrente. O trabalho
conecta o que já existe em uma sequência única, com duas responsabilidades bem
separadas:

- agentes leem pedido e fontes, elaboram o plano suficiente, escolhem formas
  visuais e escrevem/preenchem o HTML na cópia do skeleton até chegar à versão
  mais completa possível;
- checks determinísticos só protegem lifecycle, proveniência, declaração de
  materialidade, integridade de rotas e evidência. Eles não sintetizam narrativa
  nem desenham diagramas.

O ponto de parada é explícito: a promoção não altera conteúdo. Se o final não
for apropriado na revisão HTTP, o retorno é **automático** ao agente compositor,
não a um “polimento” invisível do renderer nem a uma solicitação de aprovação
do usuário. Se a fonte não permite resolver um achado, o fluxo ainda produz o
final com limitação/discovery visível; só a alegação de aprovação fica retida.

## 2. Decisões de arquitetura

| ID | Decisão | Racional | Alternativa rejeitada | Consequência/risco |
|---|---|---|---|---|
| D-001 | Usar `run-state.yaml` + `decision-log.md` como única decisão oficial de transição. | Evita estado, logs e artefatos contraditórios. | Criar outro arquivo de aprovação. | Migração cuidadosa dos chamadores. |
| D-002 | `REVISE` pre-skeleton retorna imediatamente a correção e nova revisão; só após `APPROVE` a cópia física do skeleton é instanciada. Um candidate já rastreável pode chegar a final explicitamente não aprovado durante a recuperação pós-render. | A cadeia não fica parada aguardando usuário, mas não perde a autoridade do gate. | Ignorar o gate ou bloquear passivamente até alguém aprovar. | Só o rótulo `approved`/Human Visibility fica condicionado; provenance e sequência continuam obrigatórias. |
| D-003 | `render_stakeholder_brief.py` permanece promoção de bytes/metadados, não autor. | Não há transformação secreta após candidate. | Adicionar pós-processador visual. | Um candidate que cumprir as precondições pode ser promovido; autor/revisor resolvem qualidade em loop. |
| D-004 | Revisão do final usa HTTP loopback e é vinculada a URL, digest, revisor e decisão; ela dispara recomposição sem interação humana. | O usuário avalia interação/renderização real, mas não deve operar o pipeline. | Review estático de arquivos ou screenshot isolado. | Preview indisponível retém aprovação, não a criação do final. |
| D-005 | Contratos existentes são ativados por disposição explícita (`material`, `N/A`, `discovery`). | Forma mínima não deve deixar de rodar por omissão. | Forçar diagrama universal ou inferir arquitetura com código. | A decisão de materialidade fica revisável no plano. |
| D-006 | O produto desktop exige JavaScript para a navegação por subpáginas internas; sem JS, a página mostra aviso honesto/alternativa de leitura, não simula equivalência com uma one-page. | “Todas as seções em sequência” conflita com subpáginas internas. | Aceitar ambos sem contrato. | Ajustar o teste de tabbed surface sem criar bloqueio de autoria. |

## 3. Tamanho e proporcionalidade

**Tamanho:** M.  
**Por quê:** altera alguns contratos e pontos de chamada, mas preserva os
artefatos e ferramentas principais.  
**Opção menor considerada:** adicionar só um prompt de revisão. É insuficiente,
pois o R2 demonstra que pareceres podem existir sem bloquear lifecycle.  
**Complexidade excluída:** engine novo, banco de dados, plugin de navegador,
gerador Markdown→HTML, score visual, mobile/responsividade e redesign de marca.

### Perfil visual

O padrão é **vendor-neutral**. Nenhum logo, fonte ou ativo de cliente é parte
do escopo. Um brief futuro só seleciona perfil de cliente quando fontes
canônicas o autorizarem.

## 4. Prontidão arquitetural

**Assurance:** A2-elevated. A alteração afeta uma superfície material de
qualidade/visibilidade e pode fazer artefatos incorretos parecerem aprovados.

| Dimensão | Estado atual | Decisão alvo | Prova/owner |
|---|---|---|---|
| Contexto | Plano, skeleton, candidate, renderer e review têm relações parcialmente independentes. | Uma cadeia linear e auditável. | T-001 / maintainer. |
| Responsabilidades | Autor, renderer e revisor se confundem em mensagens de estado. | Autor cria conteúdo; renderer promove; revisor decide. | T-001/T-004. |
| Contratos | Herança física não valida lifecycle; arquitetura pode não ativar guard. | Attestation, estado e materialidade interligados. | T-002. |
| Dados/evidência | Estado e pareceres podem divergir. | Locator + digest + decisão oficial recuperáveis. | T-001/T-004. |
| Fluxo crítico | Candidate pode aparecer sem precondição comprovada. | `REVISE` pre-skeleton retorna para correção/revisão; `REVISE` pós-render retorna ao compositor, podendo manter final explicitamente não aprovado. | V-001. |
| Falha/recuperação | Preview ausente ou review opcional. | Falha = `REVISE`, retorno ao autor. | V-005. |
| Observabilidade | Há checks verdes sem significado de UX. | Matriz separa deterministic/qualitative/final state. | T-005. |
| Rollback | Mudança em rules/hooks pode ser regressiva. | Testes negativos e checkpoints por task. | T-001–T-004. |
| Unknowns | Chamadores efetivos de skills/reviews e fallback no-JS. | Inventariar e decidir antes de mudar. | U-001/U-002. |

### Atual → alvo → delta

| Vista | Atual | Alvo | Compromisso |
|---|---|---|---|
| Lifecycle | Arquivos podem existir apesar de gates negativos. | Gates são precondição verificável de cada promoção; recuperação é automática e final não aprovado exige candidate rastreável. | Alterar invocações/validador, não criar workflow engine. |
| Autoria | Candidate pode tratar skeleton como inspiração. | Candidate parte da cópia física e preserva estrutura de rotas. | Manter inheritance checker e adicionar attestation estatal. |
| Arquitetura | Guard pode nunca rodar por ausência de declaração. | Disposição é declarada/revisada; guard roda quando material. | Não inferir conteúdo automaticamente. |
| Review | Skill e record podem ser opcionais/órfãos. | Um único review final oficial condiciona Human Visibility. | Inventário antes de obrigar/remover. |

## 5. Sequência de mudança

| Passo | Superfícies | Pré-condição | Resultado | Reversível? |
|---|---|---|---|---|
| 1 | workflow, run-state, decision log e testes | execução autorizada | Lifecycle único, resiliente e testes negativos. | sim |
| 2 | instruções de composição, attestation, contracts | passo 1 | Skeleton/candidate ligados ao plano e à materialidade, sem bloquear autoria. | sim |
| 3 | preview e revisão renderizada | passo 1 | HTTP local, record oficial e recomposição autônoma do final. | sim |
| 4 | suite M001–M008 | passos 1–3 | Evidência fresca, final para cada mock e gaps honestos. | sim |

## 6. Contratos, dados e compatibilidade

- **Identidade do artefato:** plan locator/digest, decisão pre-skeleton,
  skeleton digest, candidate digest e final digest devem descrever a mesma
  linhagem autorizada.
- **Fases:** `not_rendered`, candidate em avaliação, `needs_remediation`, final
  com limitações, final revisado e Human Visibility não são sinônimos. A
  transição de achado para recuperação não remove o direito de gerar o final.
- **Rotas:** `?view=<route>` ou equivalente deve selecionar um painel por vez
  no desktop, manter URL recuperável e não expor todas as abas como o conteúdo
  normal de uma única página.
- **Provas:** o HTML final projeta campos existentes; não cria task schema nem
  preenche lacunas com fatos inventados.

## 7. Segurança, privacidade e permissões

- Preview é estritamente `127.0.0.1`, sem deploy, credenciais ou telemetria.
- A revisão registra metadados do artefato e não dados de usuário.
- Não há alteração destrutiva ou migração de dados.

## 8. Rollout, observabilidade e rollback

- **Rollout:** aplicar primeiro em mocks novos; não reclassificar retroativamente
  o R2 como sucesso.
- **Sinal de sucesso:** cada mock expõe estado final, checks determinísticos e
  decisão qualitativa sem contradição.
- **Sinal de falha:** candidate/final afirma `approved` após gate `REVISE`,
  decisão sem digest, ou visual material sem contrato correspondente. Preview
  ausente é limitação/recovery, não ausência de final.
- **Rollback:** reverter a task isolada e manter o final com estado honesto;
  nunca degradar para uma exceção silenciosa ou para não produzir HTML.

## 9. Cobertura de composição do brief

Esta iniciativa altera o processo, por isso suas próprias projeções devem
explicar a cadeia e os controles, não decorar uma UI.

| Fonte/locator | Cobertura | Destino do brief | Motivo |
|---|---|---|---|
| `spec.md` §§1–10 | represented | valor, impacto, decisão | problema, limites e resultado. |
| `impact-map.md` | represented | arquitetura, impacto | cadeia, limites e mudanças por domínio. |
| `tasks.md` | represented | execução, validação | dossiers e entregas por task. |
| `validation-plan.md` | represented | validação | provas e gates. |
| `reproduction.md` | synthesized | valor/evolução | evidência do gap que motivou a SPEC. |

**Autor do plano:** Guardian maintainer.  
**Revisor de cobertura:** pendente, distinto do autor.  
**Decisão:** pendente em `decision-log.md`; nenhuma instância de skeleton desta
SPEC é autorizada antes de uma revisão `APPROVE`. Um `REVISE` inicia correção e
nova revisão sem aguardar o usuário.

### 9.1 Registro de construção do brief

| Rota/componente | Pergunta executiva | Arco | Fatos/relacionamentos | Forma visual | Campos repetidos | Ausência/discovery | Ação final |
|---|---|---|---|---|---|---|---|
| `scope` | Por que corrigir a esteira agora? | problema → risco → outcome → limite | R2, fonte→final, não-goals | hero + mapa de resultado | atores e resultados | nenhum | aprovar correção de processo |
| `architecture.global` | Onde a esteira muda e onde não muda? | contexto → fluxo → controles → consequência | fontes, plano, skeleton, candidate, renderer, review, estado | topologia de pipeline com regiões alteradas | nós, fronteiras, gates | U-001/U-002 explícitos | confirmar sequência única |
| `architecture.lifecycle` | Quem pode avançar cada fase? | gate → artefato → prova → recuperação | estado, log, digests, revisor | diagrama de estado/fluxo | fase, precondição, bloqueio, retorno | nenhum | validar autoridade do lifecycle |
| `impact.<domínio>` | O que muda neste domínio? | delta → exposição → controle → ação | impact map | dossiers/footprint | delta, dono, preservado, controle | N/A fonte-apoiado | aprovar fronteiras |
| `execution.task.<id>` | Qual incremento cada task entrega? | objetivo → escopo → dependência → prova → gate | T-001–T-005 | epic arc quando fonte existir + dossier por task | objetivo, anti-escopo, dependência, risco, AC/prova, saída | lacuna vira discovery nomeada | decidir sequência |
| `validation.proof.<id>` | Como provar que a cadeia é honesta? | claim → método → oracle → limite → decisão | V-001–V-008 | matriz + proof dossiers | método, ambiente, evidência, responsável, limite | review humano não vira check automático | decidir Human Visibility |
| `evolution` | O que muda do R2 para a nova execução? | antes → correção → execução → pendências | reproduction + task state | linha do tempo/registro | eventos fonte-apoiados | sem reescrever passado | pedir nova run |
| `decision` | O que o maintainer aprova? | contexto → autoridade → trade-off → ação | D-001–D-006 | decision record | dono, consequência, próximo gate | U-002 bloqueante | aprovar/revisar |
| `coverage` | O que foi transportado para a tela? | fonte → disposição → confiança → ação | tabela de cobertura | registro | toda fonte aplicável | N/A com razão | habilitar revisão |

**Política de arquitetura:** a topologia global será uma arquitetura da solução
de processo, destacando os nós alterados. Zomm por domínio só é exibido quando
o domínio tem mudança própria; não há três quadrados genéricos ou cadeia textual
repetida. Para brief de produto futuro, a forma é escolhida pelas fontes: pode
ser topologia de software, mapa de aplicação, sequência de dados/navegação ou
outro visual justificado.

**Revisão independente de construção:** o revisor compara esta tabela com
`spec.md`, `impact-map.md`, `tasks.md` e `validation-plan.md`; o veredito é
`APPROVE` ou `REVISE`, registrado em decision log. `REVISE` inicia correção e
nova revisão autônomas e preserva o finding. Enquanto ele estiver aberto, não
há cópia/instanciação do skeleton; depois de um candidate rastreável existir,
uma revisão posterior pode manter um final explicitamente não aprovado para
recuperação. Uma pergunta só chega ao usuário se exigir nova autoridade ou
mudar o escopo além das fontes.

## 10. Perguntas abertas

| ID | Pergunta | Owner | Resolução | Bloqueia? |
|---|---|---|---|---|
| U-001 | Onde `validate_semantic_review_record.py`, `brief-experience-composer.md` e `rendered-brief-decision-review` são chamados hoje, se em algum lugar? | T-004 | Inventário de chamadas e decisão explícita. | não — investigação ocorre na task. |
| U-002 | Política de fallback sem JS. | T-001 | Resolvida por D-006; atualizar testes/documentação. | não |
| U-003 | Qual mecanismo local mínimo abre a URL HTTP nas validações reproduzíveis? | T-003 | Escolher helper já disponível ou servidor Node mínimo. | não |

## 11. Decisão do plano

**Plan Ready:** yes.  
**Condições operacionais:** cada revisão interna deve acionar recuperação, não
um bloqueio de autoria. A execução aguarda exclusivamente a autorização de
execução que o usuário disse que dará ou negará nesta conversa.
