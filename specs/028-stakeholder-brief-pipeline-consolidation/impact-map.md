# Impact map — SPEC 028

## Escopo e fronteiras

| Superfície | Alteração esperada | Fora do escopo |
|---|---|---|
| Lifecycle do brief | Unificar a decisão que autoriza candidate, promoção e Human Visibility. | Novo motor de workflow. |
| Plano de composição | Tornar construção/revisão pre-skeleton vinculante. | Gerar conteúdo por script. |
| Skeleton/candidate | Exigir cópia física e proveniência, preservando autoria por agente. | Redesign de uma marca específica. |
| Preview/revisão final | Revisar HTML final em HTTP local antes de Human Visibility. | Hosting/deploy público. |
| Contratos existentes | Conectar arquitetura, task/proof e rotas aos gates certos. | Inventar métricas de qualidade. |
| Mock lab | Executar M001–M008 fresco e reportar resultado honesto. | Reescrever runs históricos. |

## Mudança de fluxo

```text
Fontes canônicas + pedido humano
  → plano.md + construction record revisado
  → decisão oficial pre-skeleton (run-state + decision log)
  → cópia física do skeleton v3
  → candidate HTML autorado por agente
  → attestation / contratos determinísticos
  → promoção exata para stakeholder-brief.html
  → preview HTTP local e revisão independente
  → Human Visibility (ou REVISE com retorno ao autor)
```

## Impacto por domínio

| Domínio | Papel atual | Delta | Preservado | Risco/control |
|---|---|---|---|---|
| `run-state.yaml` | Declara fases/gates, mas pode divergir de arquivos. | Virar referência de lifecycle vinculada a log e artefatos. | Estrutura de gates existente. | Negar transições inválidas. |
| `decision-log.md` | Registra decisões, mas pode ficar paralelo. | Fornecer decisão oficial recuperável para cada transição material. | Registro Markdown. | Digest/locator e coerência de estado. |
| Skeleton v3 | Oferece estrutura/tabulação. | Permanecer a base que é copiada, não uma mera inspiração. | HTML/CSS/JS base. | Herança física + conteúdo humanamente revisado. |
| Candidate | Pode passar no hash e ainda ser pobre. | Receber provenance e gates corretos. | Autoria agêntica HTML/CSS/JS. | Não promover sem revisão. |
| Renderer | Promove lifecycle/bytes. | Ser nomeado e validado como promoção apenas. | Não reautorará conteúdo. | Sem “polimento” implícito. |
| Architecture/task/proof contracts | Existem com ativação parcial. | Acionar conforme disposição material declarada. | Checks de forma. | Revisão humana da clareza. |
| Review | Há skill/registro fora do fluxo. | Vincular decisão final a estado e digest. | Independência de revisor. | HTTP local + REVISE bloqueante. |

## Impacto nos atores

| Ator | Antes | Depois |
|---|---|---|
| Autor | Pode preencher candidate apesar de `REVISE` ou tratar skeleton como referência. | Só compõe depois de autorização e preenche a cópia do skeleton. |
| Revisor do plano | Pode produzir parecer sem efeito no lifecycle. | Sua decisão determina se o skeleton pode existir. |
| Revisor final | Pode ser opcional/desvinculado. | Revisa o brief final servido e deixa decisão oficial. |
| Stakeholder | Pode receber página crua/candidate. | Recebe apenas final com decisão de visibilidade coerente. |

## Descobertas obrigatórias

- Inventariar chamadas reais, não apenas arquivos existentes, para
  `validate_semantic_review_record.py`, `brief-experience-composer.md` e
  `rendered-brief-decision-review`.
- Resolver uma única política para fallback sem JavaScript compatível com a
  intenção desktop de uma subpágina interna por aba.
- Se qualquer mock não declarar arquitetura material, verificar se a decisão é
  N/A/discovery legítima, em vez de forçar a topologia do M003.
