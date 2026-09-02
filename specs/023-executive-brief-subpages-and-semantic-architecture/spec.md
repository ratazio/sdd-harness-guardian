# SPEC 023 — Brief executivo por subpáginas e arquitetura explicável

**Status:** spec ready; direção visual documentada; execução bloqueada apenas
pela revisão explícita dos mocks desta SPEC.  
**Owner:** Guardian maintainers + brief experience owner.  
**Created / updated:** 2026-08-31.  
**Risk / assurance:** high / A2-elevated.  
**Origin:** pedido direto do requester após a avaliação dos mocks M-001–M-008.

## 1. Problema

O mock recente M-001 apresenta uma sequência vertical de seções acessadas por
âncoras. O shell v2 mais novo consegue ocultar painéis, mas ainda oferece uma
troca estreita de painel, não uma página integral para cada domínio da conversa.
Em ambos os casos, a pessoa que precisa conduzir uma reunião precisa reconstruir
o contexto ao navegar: falta uma abertura executiva, uma tese, os pilares, a
consequência e o próximo diálogo de cada visão.

A visão de arquitetura é o caso mais crítico. Hoje ela pode reduzir relações
materiais a nós genéricos e setas; não torna visíveis o perímetro da mudança,
o que permanece protegido, a escala por aspecto, nem o zoom do subsistema onde
a mudança de fato ocorre. Isso é insuficiente para uma decisão de liderança e
induz uma aparência de relatório gerado por uma estrutura fixa.

O requester determinou também que os briefs novos ou materialmente renovados
usem integralmente `C:\Users\rataz\Downloads\design_pearson\design.md`, cuja
cópia de autoridade no bundle é `.harness/references/pearson-design.md`. A
SPEC 014 já autoriza o perfil Pearson e seus ativos locais; esta SPEC evolui a
experiência e a explicação, sem reescrever silenciosamente artefatos históricos.

## 2. Objetivo

Fazer com que um stakeholder brief seja uma experiência executiva, navegável
como subpáginas completas dentro de **um único HTML**, na qual cada domínio
explica uma decisão humana com profundidade proporcional às fontes e a visão de
arquitetura torna recuperáveis topologia, perímetro, escala e zoom da mudança.

## 3. Resultado de entrega

- **Resultado para o usuário:** uma pessoa C-level pode abrir qualquer visão do
  brief e imediatamente entender por que ela importa, o que muda, o que não
  muda, quem precisa decidir e qual conversa vem a seguir.
- **Incremento demonstrável:** shell de rotas internas, protocolo de composição
  editorial semântica, superfícies arquiteturais proporcionais e regressões em
  domínios heterogêneos.
- **Fronteira do slice:** geração e revisão do brief; não implementação dos
  produtos descritos pelos briefs nem reescrita de fatos canônicos.
- **Fonte de prioridade:** solicitação humana explícita em 2026-08-31.

## 4. Pessoas e decisões atendidas

| Pessoa | Precisa decidir / entender | Resposta esperada do brief |
|---|---|---|
| Patrocinador executivo | valor, risco, perímetro e próxima decisão | uma tese curta, consequências e uma ação inequívoca |
| Liderança de produto/operação | quem é afetado e como o benefício chega | impacto, trade-offs, donos e ondas de execução |
| Liderança técnica | o que muda no sistema e o que é preservado | topologia, change-surface map e zoom material |
| Responsável por assurance | o que torna a afirmação confiável | evidência, limitações, proveniência e autoridade atual |

## 5. Resultados observáveis

- **O-023-01:** ativar uma visão altera a experiência principal inteira para a
  subpágina daquele domínio; não executa `scrollIntoView` nem deixa o conteúdo
  de outra visão como continuação visual.
- **O-023-02:** cada subpágina começa com uma abertura editorial fonte-apoiada
  que explica tese, pilares, pergunta de decisão e próximo passo em linguagem
  natural.
- **O-023-03:** quando arquitetura é material, o leitor consegue distinguir
  topologia, áreas alteradas, áreas preservadas/fora do escopo, escala declarada
  e pelo menos um zoom material; quando não é material, vê um N/A justificado.
- **O-023-04:** o resultado parece uma narrativa preparada para reunião, sem
  ocultar proveniência, incerteza ou autoridade canônica.

## 6. Não objetivos

- Converter todo brief em site de marketing, exigir fotografia, ou impor uma
  quota de heros, cartões, páginas, palavras, diagramas ou componentes.
- Extrair arquitetura por heurística de nomes de arquivo, fabricar frontend,
  APIs, contagens, dependências ou relações que as fontes não afirmam.
- Fazer uma regra determinística pontuar qualidade narrativa, materialidade ou
  decidir que um executivo compreendeu o brief.
- Alterar briefs históricos/renderizados sem decisão de migração e refresh
  explícitos, ou tornar o HTML uma segunda fonte de verdade.

## 7. Requisitos funcionais

| ID | Requisito | Razão |
|---|---|---|
| FR-023-01 | Um brief deve conter uma rota interna integral por domínio — Visão geral, Valor e escopo, Arquitetura, Impacto, Execução, Validação, Evolução/decisões e Confiança/proveniência. Ao navegar, só a rota ativa participa da região principal visual e de leitura; cabeçalho institucional, navegação e rodapé podem persistir. | Uma aba precisa abrir um domínio completo, não deslocar o leitor numa página longa. |
| FR-023-02 | Cada rota deve ter título editorial forte, contexto para o decisor, tese curta, 3–5 pilares quando as fontes os tornam materiais, conteúdo próprio, limite/incerteza relevante e fechamento com decisão, atenção ou próximo passo. | A explicação precisa ter intenção humana, não repetir rótulos de seção. |
| FR-023-03 | A navegação deve preservar rota no histórico/URL, foco e `aria-current`/semântica; voltar/avançar restaura a rota. Sem JavaScript, as rotas permanecem links e o conteúdo é linearmente recuperável; impressão revela todas; movimento reduzido é respeitado. | A subpágina interna não pode sacrificar acesso, links compartilháveis ou leitura sem script. |
| FR-023-04 | A composição deve receber pedido efetivo e fontes canônicas, e produzir um **mapa editorial de rotas** revisável: para cada afirmação, tese, pilar, pergunta e visual, registrar fonte/locator, síntese permitida, limite ou descoberta dona. O mapa orienta o candidato, mas não substitui as fontes canônicas. | A camada agêntica precisa aprofundar sentido sem inventar fatos nem se tornar nova autoridade. |
| FR-023-05 | Quando fontes tornam arquitetura material, a rota Arquitetura deve oferecer: (a) topologia macro de componentes, atores, limites e fluxos materiais; (b) mapa de superfícies com `alterado`, `preservado/contexto`, `fora de escopo` e `desconhecido`; (c) escala por aspecto, com a unidade explicitada; e (d) um zoom para cada subsistema material selecionado. | Liderança precisa localizar a mudança antes de discutir detalhe técnico. |
| FR-023-06 | Um zoom de arquitetura deve mostrar, por exemplo no frontend quando ele é fonte-apoiado, as áreas internas, contratos/fluxos, pontos que mudam e limites que não mudam. O compositor não pode inferir esse zoom de um rótulo: se a fonte não define o interior, deve apresentar descoberta/limitação, não um diagrama fictício. | Evita a falsa precisão visual que o requester rejeitou. |
| FR-023-07 | A escala arquitetural deve contar apenas unidades definidas pela composição (por exemplo, superfícies fonte-apoiadas ou contratos declarados), indicar o denominador e separar `0`, `fora de escopo` e `desconhecido`. Nunca alegará contagem de arquivos, linhas ou componentes sem fonte. | “Quantidade de alterações” deve ser interpretável e honesta. |
| FR-023-08 | O perfil Pearson será a base dos briefs novos ou materialmente renovados: identidade local, logo local protegido em navy, Plus Jakarta Sans com fallback local/sistema, tokens navy/lavender/surface, grade, tipografia, cartões, foco e responsividade do guia. Uma exceção visual continua exigindo o registro previsto pela SPEC 014. | O resultado deve respeitar a referência fornecida, e não apenas aplicar cores. |
| FR-023-09 | A rota Confiança/proveniência mantém composição por bloco, lifecycle, review, limites e origem das afirmações; ela pode ser mais técnica, mas não pode dominar a primeira leitura executiva. | Explicação humana e auditabilidade devem coexistir. |
| FR-023-10 | Avaliação semântica e visual será feita por revisor distinto do compositor contra pedido, fontes, rota ativa e artefato renderizado. O código verifica contratos, integridade e comportamento; não aprova suficiência, materialidade ou estética por score. | Preserva julgamento humano/agêntico em vez de transformar a experiência num tratado determinístico. |

## 8. Critérios de aceite

| ID | Critério | Validação inicial |
|---|---|---|
| AC-023-01 | Em um único HTML, cada domínio abre como subpágina com início, narrativa e fechamento próprios; uma troca de rota não rola para uma âncora nem mostra o corpo de outra rota. | V-023-01 |
| AC-023-02 | Rota, histórico, teclado, foco, 320/768/1024/1440px, 200% zoom, no-script, impressão e movimento reduzido são recuperáveis e utilizáveis. | V-023-02 |
| AC-023-03 | Um revisor humano/agêntico confirma, em casos heterogêneos, que cada rota responde à pergunta de decisão com tese, pilares, limites e próximo passo materialmente fonte-apoiados. | V-023-03 |
| AC-023-04 | Dois casos de arquitetura material mostram topologia, superfície, escala definida e zoom; um caso operacional/não software mostra equivalente proporcional ou N/A justificado sem software inventado. | V-023-04 |
| AC-023-05 | O mapa de mudança distingue alteração, contexto preservado, fora de escopo e desconhecido; toda contagem afirma a unidade e o suporte de fonte, ou torna a lacuna acionável. | V-023-05 |
| AC-023-06 | O shell cumpre literalmente as partes aplicáveis do guia Pearson e SPEC 014: ativo local, sem hotlink, marca/contraste corretos, Plus Jakarta Sans/fallback, composição de produto e WCAG 2.2 AA. | V-023-06 |
| AC-023-07 | Os mocks M-023-A/B/C tornam a direção visual compreensível e recebem decisão explícita do requester antes do refactor do renderer/template. | V-023-07 |
| AC-023-08 | A suíte M-001–M-008 recomposta em raiz nova não perde lifecycle, proveniência, fontes materiais ou revisão independente enquanto ganha a nova experiência. | V-023-08 |

## 9. Comportamentos de borda e falha

| ID | Condição | Comportamento esperado |
|---|---|---|
| EC-023-01 | JavaScript indisponível ou rota desconhecida | Conteúdo linear e links de âncora continuam legíveis; a rota desconhecida volta de modo explícito à Visão geral sem ocultar conteúdo. |
| EC-023-02 | Arquitetura não é material | Rota explica por que não há topologia, mostra o equivalente operacional ou N/A com fonte e não adiciona caixas técnicas decorativas. |
| EC-023-03 | Há topologia, mas detalhe interno ausente | Mapa marca a lacuna, impacto decisório, owner e caminho de descoberta; não cria zoom especulativo. |
| EC-023-04 | Contagem de mudança não é recuperável | O visual mostra `desconhecido — descoberta necessária`, com unidade necessária; não exibe zero ou estimativa como fato. |
| EC-023-05 | Rota extensa ou tabela densa em tela estreita | A subpágina reorganiza conteúdo, cartões e tabela sem rolagem horizontal de página nem redução abaixo de 16px. |

## 10. Direção visual documentada — base para os mocks

### Experiência de reunião

O brief não será um dashboard nem uma landing page genérica. Ele terá uma barra
Pearson navy persistente de produto, logo oficial local à esquerda e navegação
de domínios à direita. Abaixo dela, cada rota se abre como um território próprio:
um eyebrow de orientação, H1 em sentence case, uma placa lavanda de tese e
decisão, e uma composição específica. O leitor nunca precisa procurar, no
restante da página, o que aquela visão está tentando lhe dizer.

O ritmo é o do guia Pearson: canvas lavanda `#EDECF5`, superfícies brancas,
navy `#0B004A` dominante, violeta `#4C30A5` apenas como ação/estado ativo,
bordas lavanda e sombra rara. Tipografia é Plus Jakarta Sans 400/500/600/700,
H1 de aplicação entre 40–56px, corpo mínimo 16px e espaço negativo abundante.
A rota pode ter uma imagem editorial humana apenas quando a fonte e a conversa
se beneficiam dela; não é requisito e nunca será decoração para mascarar falta
de explicação.

### Gramática das subpáginas

| Rota | Pergunta que responde | Composição esperada |
|---|---|---|
| Visão geral | “Qual decisão importa agora e por quê?” | tese, resultado, três sinais de decisão, atenção e próximo encontro |
| Valor e escopo | “Que resultado estamos comprando e qual limite aceitamos?” | narrativa de valor, pilares, incluído/excluído, trade-offs e medidas observáveis |
| Arquitetura | “Onde a mudança vive e o que ela preserva?” | topologia, mapa de superfícies, escala por aspecto e zoom material |
| Impacto | “Quem muda de comportamento e como controlamos a transição?” | pessoas/áreas, cadeia de efeitos, riscos, controles e consequências |
| Execução | “Como entregamos valor sem esconder dependências?” | ondas/incrementos, porquê agora, dependências, decisões por task e saída segura |
| Validação | “Que evidência permite avançar e o que ainda não prova?” | cadeia risco–método–evidência, limites e readiness |
| Evolução e decisões | “O que mudou, quem decidiu e o que permanece aberto?” | linha de evolução, escolhas, dono, consequência e checkpoint |
| Confiança e proveniência | “Por que devo confiar nesta leitura?” | origem, síntese, lacunas, lifecycle e links para a autoridade canônica |

### Topologia e zoom de arquitetura

O diagrama macro é um mapa de relação, não uma coleção de ícones. Ele deve
separar contexto preservado (bordas neutras), alteração proposta (borda/violeta
e rótulo textual), fora de escopo (tratamento discreto) e descoberta necessária
(sinal textual de incerteza). Setas carregam uma relação legível: dado, evento,
contrato, dependência, controle ou handoff. Uma legenda torna cor e forma
suplementares, nunca únicas.

Ao lado, o **registro de mudança** declara a unidade da escala — por exemplo,
“3 superfícies fonte-apoiadas: interface, contrato de publicação e controle de
rollback” — e mostra o número por aspecto só se a composição consegue apontar
as fontes. O zoom ocupa uma sub-região clara da rota, não um modal escondido:
começa pela caixa escolhida na topologia, abre seus pontos internos relevantes
e chama atenção para o que continua intocado. Caso a fonte só sustente a caixa
macro, o zoom explica a descoberta necessária em vez de desenhar módulos falsos.

### Antipadrões explicitamente proibidos

- Tabs que apenas chamam `scrollIntoView`, links para âncora como experiência
  principal, ou trocar um único painel mantendo o resto da página como contexto.
- Uma introdução de template idêntica em todas as rotas, jargão sem tradução,
  métricas decorativas e diagramas genéricos de quatro caixas.
- Gradientes decorativos, glassmorphism, neon, sombra pesada, logo redesenhado,
  fonte remota ou aparência de painel SaaS indiferenciado.
- Tratar todo caso como frontend/software; esconder “não muda” ou transformar
  ausência em zero.

### Mocks a gerar e como interpretá-los

Os três mocks são **hipóteses visuais não canônicas**, não screenshots de um
brief real nem especificação de fatos. Eles omitem texto miúdo/legível porque
o gerador de imagem não é fonte de tipografia final. A implementação continuará
a usar o logo oficial local, não uma versão gerada.

| ID | Vista | O que permite avaliar |
|---|---|---|
| M-023-A | Visão geral executiva | hierarquia, tese, pilares, chamada de decisão e navegação de subpáginas |
| M-023-B | Arquitetura | topologia, mudança vs. preservação, escala e zoom de frontend fonte-apoiado como exemplo de layout |
| M-023-C | Impacto e execução | narrativa de pessoas/impacto, ondas de entrega, riscos/controles e linguagem de reunião |

As imagens geradas a partir desta direção estão preservadas em
`evidence/visual-mocks/`. Elas são contexto de decisão D-023-001, não uma
implementação, fonte canônica, ativo Pearson ou prova de acessibilidade.

## 11. Restrições não funcionais

- **Arquitetura:** preservar fonte canônica, proveniência por bloco, lifecycle,
  refresh explícito e a distinção autor/compositor/revisor.
- **Acessibilidade:** HTML semântico, landmarks, rota/foco recuperáveis, texto
  + forma além de cor, contraste AA, teclado, no-script, impressão, 200% e
  `prefers-reduced-motion`.
- **Privacidade/dados:** conteúdo e diagramas não revelam informação sensível
  além do que fontes e política permitem; o revisor exige abstração/redação.
- **Compatibilidade:** um arquivo HTML sem dependência de runtime, logo/fontes
  remotos ou rede; progressivo em navegadores modernos.
- **Qualidade humana:** a revisão pergunta se um decisor entende propósito,
  perímetro, trade-off e próxima ação sem abrir as fontes; uma resposta negativa
  devolve reparo específico, não nota numérica.

## 12. Premissas e dependências

| Premissa / dependência | Dono e validação |
|---|---|
| A cópia local do guia Pearson e o logo oficial continuam a autoridade visual. | Guardian maintainer; hash/ativo local e revisão visual. |
| Cada iniciativa possui fontes canônicas suficientemente explícitas para que a composição cite locators. | Autor da iniciativa; mapa editorial e review distinto. |
| O requester revisará M-023-A/B/C como intenção visual antes do refactor amplo. | Requester; decisão D-023-001. |
| M-001–M-008 continuam a cobrir domínios heterogêneos. | Maintainer/evaluator; recompose em raiz nova. |

## 13. Riscos

| ID | Risco | Prob. / impacto | Mitigação / dono |
|---|---|---|---|
| R-023-01 | A experiência vira um conjunto de telas bonitas, porém genéricas. | média / alta | mapa editorial com fontes e review executivo distinto; compositor + revisor. |
| R-023-02 | O diagrama confere falsa precisão à arquitetura. | média / alta | fonte/locator por afirmação, N/A/descoberta explícita e exemplos heterogêneos; reviewer. |
| R-023-03 | Um router interno quebra no-script, print ou foco. | média / alta | fallback linear, testes de browser e revisão assistiva; builder/evaluator. |
| R-023-04 | O Pearson vira somente paleta e não sistema de composição. | média / média | checklist do guia, revisão comparativa e ativo local; visual reviewer. |
| R-023-05 | Atualizar registros revisados altera autoridade histórica. | baixa / alta | refresh/migração explícitos; lifecycle owner. |

## 14. Decisão da SPEC

**Outcome Ready:** sim — o requester definiu a experiência desejada e aprovou a
criação da SPEC.  
**Spec Ready:** sim — escopo, limites, visual, validação e tarefas estão
especificados.  
**Autoridade de execução:** não iniciada. A revisão dos mocks M-023-A/B/C é a
decisão visual D-023-001 que precede qualquer refactor amplo; ela não é um
gate determinístico nem uma autorização implícita de reescrever briefs.
