# SPEC 024 — Fidelidade visual do brief executivo

**Status:** complete  
**Sequence:** 024  
**Slug:** executive-brief-visual-fidelity  
**Owner:** Guardian maintainers + brief experience owner  
**Created:** 2026-08-31  
**Last updated:** 2026-08-31  
**Risk:** high  
**Assurance profile:** A2-elevated

## 1. Problem

O requester identificou corretamente uma divergência material entre a direção
visual aprovada em SPEC 023 (`M-023-A/B/C`) e o HTML que lhe foi apresentado:
`testes/mock-runs/20260831-spec023-t004-r1/m005-ai/t004-candidate.html`.
Esse arquivo é um candidato técnico de corpus descartável; sua rota de
arquitetura contém texto e relações lineares, mas não materializa os gráficos,
a topologia, o mapa de alteração, a escala e o zoom que a direção visual exigia.
Além disso, ele é deliberadamente vendor-neutral, portanto não prova aplicação
do perfil Pearson.

Apresentar esse candidato como exemplo final confundiu uma verificação de
corpus com uma referência executiva de produto. A falha é sistêmica: o contrato
atual permite que uma rota seja semanticamente correta e navegável sem provar
que sua tradução visual é comparável à direção aprovada em artefato renderizado.

## 2. Objective

Garantir que um brief executivo materialmente visual seja demonstrado e
avaliado como experiência renderizada: narrativa humana, hierarquia Pearson e
visuais de arquitetura reais, fonte-apoiados e legíveis — nunca substituídos
por listas ou caixas técnicas genéricas.

## 3. Delivery outcome

- **Product/user outcome:** sponsor e liderança técnica veem a conversa
  decisória completa, incluindo os gráficos que localizam a mudança.
- **Demonstrable increment:** referência M-005 em HTML único, offline, com
  oito subpáginas e captura/PDF; depois, um contrato reutilizável que evita o
  downgrade visual onde arquitetura/impacto forem materiais.
- **MVP/slice boundary:** corrigir tradução visual e gates; não promover HTML
  histórico nem implementar o serviço de correção de provas.
- **Priority source:** pedido humano explícito de 2026-08-31.

## 4. Users or actors

| Ator | Necessidade |
|---|---|
| Sponsor executivo | Decidir benefício, limite e próximo passo sem decodificar relatório técnico. |
| Liderança técnica | Localizar mudança, preservação, fronteiras e descoberta em diagrama/zoom. |
| Assurance/privacy | Distinguir controle determinístico, sugestão probabilística e autoridade humana. |
| Compositor/revisor | Produzir e avaliar experiência fonte-apoiada sem transformar corpus em entrega. |

## 5. Observable outcomes

- **O-024-01:** referência M-005 mostra topologia SVG com relações nomeadas,
  mapa de superfícies, escala com unidade e zoom do fluxo de decisão.
- **O-024-02:** oito rotas trocam toda a região principal por `?view=`, mantêm
  leitura linear sem JavaScript e não usam scroll como navegação principal.
- **O-024-03:** artefato aplica o perfil Pearson: logo oficial local em navy,
  canvas lavender, tokens, tipografia, raio, contraste e espaço negativo.
- **O-024-04:** revisor independente compara captura real ao pedido,
  `design.md` e M-023-B; pode reprovar mesmo com checks determinísticos verdes.
- **O-024-05:** contrato futuro não declara arquitetura visual satisfeita quando
  o renderer emitiu apenas fallback textual.

## 6. Non-goals

- Promover/sobrescrever M-001–M-008, ou rebatizar o candidato T-004 como entrega.
- Inventar frontend, número de arquivos, métrica de modelo ou detalhe ausente.
- Usar imagem gerada no lugar de diagrama factual acessível; gráficos são SVG/HTML.
- Obrigatoriedade de fotografia, ilustração ou visual decorativo.
- Converter avaliação visual em score determinístico.

## 7. Functional requirements

| ID | Requirement | Rationale |
|---|---|---|
| FR-024-01 | Preservar raiz de referência separada de T-004 e dos históricos. | Não confundir candidato de laboratório com produto. |
| FR-024-02 | Para arquitetura material, emitir topologia gráfica legível com atores, fronteiras, fluxo rotulado e legenda de alteração/preservação/fora de escopo/descoberta. | Cadeia textual não localiza mudança. |
| FR-024-03 | Emitir mapa de superfícies e escala somente com unidade e denominador fonte-apoiados; lacuna é desconhecida, não zero. | Evita precisão visual falsa. |
| FR-024-04 | Aprofundar por zoom somente caixa suportada; frontend não fonte-apoiado recebe N/A explícito. | Evita UI fictícia. |
| FR-024-05 | Aplicar perfil Pearson verificável: asset local, tokens/contraste, tipo, composição e responsividade. | Cor aproximada não é o `design.md`. |
| FR-024-06 | Cada rota é uma subpágina completa com abertura, tese, pilares, limite, próximo passo e fechamento. | Uma aba não pode ser ponto de scroll. |
| FR-024-07 | Capturas desktop/mobile, PDF e inspeção independente são obrigatórios antes de alegar fidelidade visual. | Qualidade relevante é do render. |
| FR-024-08 | Contrato reutilizável distingue visual estruturado de fallback e falha quando a rota visual-material contém apenas texto. | Previne regressão em outros domínios. |

## 8. Acceptance criteria

| ID | Criterion | Initial validation |
|---|---|---|
| AC-024-01 | Referência M-005 é HTML único offline, abre `?view=architecture` como subpágina e continua legível/imprimível sem JS. | V-024-01 |
| AC-024-02 | Captura de Arquitetura mostra macro-topologia SVG, conectores rotulados, legenda, mapa com unidade e zoom factual M-005. | V-024-02 |
| AC-024-03 | HTML não apresenta frontend nem MySQL direto como alteração; expõe explicitamente o limite. | V-024-03 |
| AC-024-04 | PNG desktop/mobile, PDF e revisão independente confirmam aplicação material do `design.md`, não só cores. | V-024-04 |
| AC-024-05 | Check reutilizável rejeita rota visual-material que contenha apenas fallback textual/sem SVG equivalente. | V-024-05 |
| AC-024-06 | Corpus e históricos T-004 continuam intocados e claramente não adotados. | V-024-06 |

## 9. Edge cases and failure behavior

| ID | Condition | Expected behavior |
|---|---|---|
| EC-024-01 | Fonte não dá detalhe interno | Zoom mostra fronteira e descoberta, nunca módulo hipotético. |
| EC-024-02 | Caso sem arquitetura material | Rota oferece N/A/equivalente operacional explícito, sem SVG decorativo. |
| EC-024-03 | JS desabilitado/rota inválida | Links e conteúdo linear recuperáveis; rota inválida retorna à visão geral. |
| EC-024-04 | Tela estreita/200% | Diagrama reorganiza/rola internamente sem cortar rótulos ou reduzir corpo abaixo de 16px. |
| EC-024-05 | Revisão visual reprova | Candidato não é promovido; finding volta ao compositor com captura e causa. |

## 10. Constraints and non-functional requirements

- **Arquitetura:** SVG/HTML é projeção de fontes, não autoridade paralela.
- **Privacidade:** nenhuma PII real; preservar minimização, pseudônimo e modelo local.
- **Dados:** não alegar precisão, viés, volume ou contagem de arquivos sem fonte.
- **Acessibilidade:** offline, AA, texto+forma além de cor, teclado, no-script, print e reduced motion.
- **Operação:** logo Pearson local; sem hotlink, data URI, avatar ou login inventado.

## 11. Assumptions

| Assumption | Validation/owner |
|---|---|
| SVG nativo é mais adequado que imagem gerada para fatos arquiteturais. | Revisor compara legibilidade, rastreabilidade e design; owner: brief experience. |
| M-005 prova a falha, não generalidade. | T-003 aplica contrato a casos heterogêneos; owner: mock lab. |

## 12. Risks

| ID | Risk | Probability | Impact | Mitigation/owner |
|---|---|---|---|---|
| R-024-01 | Visual bonito porém factual/acessível fraco. | medium | high | Proveniência, legenda/texto e review distinto. |
| R-024-02 | Tokens passam mas aparência segue genérica. | high | high | Captura comparada a design.md/M-023-B; REVISE bloqueia. |
| R-024-03 | Zoom fictício para fonte macro. | medium | high | N/A/descoberta e teste negativo. |
| R-024-04 | Referência isolada confundida com T-004. | medium | medium | Caminho, título e README inequívocos. |

## 13. Dependencies

| Dependency | Status | Owner | Blocking? |
|---|---|---|---|
| `.harness/references/pearson-design.md` e logo local | available | design authority | yes |
| M-005 pedido e fontes | available | mock lab | yes |
| M-023-A/B/C como hipótese de layout | available | SPEC 023 evidence | yes |
| Revisor Terra distinto do compositor | requested | delivery orchestrator | yes |

## 14. Validation notes

`validation-plan.md` separa checks estruturais e revisão visual. Captura não
prova sozinha correção factual; validação estrutural também não prova que a
experiência é apresentável.

## 15. Spec Guardian decision

**Outcome Ready:** yes  
**Spec Ready:** yes — pedido, reprodução, limites e validação estão registrados.  
**Reviewer:** requester autorizou avaliação agêntica; avaliador distinto por task continua obrigatório.  
**Reviewed at:** 2026-08-31  
**Blocking issues:** nenhum para referência isolada; promoção reutilizável depende do render reviewed.  
**Required revisions:** registrar findings independentes antes de concluir cada task.  
**Decision evidence/link:** `reproduction.md`; pedido nesta conversa.
