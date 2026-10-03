# Kit de composição — brief com abas

O contrato normativo está em `.harness/rules/brief-contract.md`. Este kit
explica como preencher o template 3 (BC-008/024); não acrescenta gates nem
uma fonte narrativa. Histórico 1/2 conserva o dispatch de BC-002/009.

## Casca e interação

Copie `stakeholder-brief.html` e preencha a própria cópia. Preserve os tokens
navy/violet/lavender/aqua, a fonte de sistema e um título `h1` específico.
Use `h2` para o título de cada aba e `h3` para unidades comparáveis. O
cabeçalho contém transformação, benefício/critério disponível e autoridade
em frases curtas; a explicação extensa pertence à aba.

Os oito inputs `view-<id>` compartilham `name="brief-view"`; labels
`tab-<id>` apontam para eles. Os oito IDs de painel são os de BC-007.
Inputs recortados permanecem focáveis; não use `display:none` nos controles
em tela. CSS mantém um painel selecionado; setas e Espaço são nativos.
O JS inline somente acrescenta URL/hash, Home/End e acesso a alvos internos.
Um link de coverage mostra a aba e o bloco em texto, mesmo sem JS. Com JS,
um hash de bloco abre a aba correspondente. Print revela todos os painéis
e os detalhes; o estado de tela retorna após impressão.

## Preenchimento dos slots

`data-slot-source`, `data-question`, `data-material-fields` e
`data-representation` são instruções autorais. Não são provenance de um
fato. Para os blocos compostos, acrescente os locators reais de BC-005.
Troque todos os `{{campos}}` visíveis; duplique/remova unidades repetíveis
conforme os fatos, conservando cada aba. Não transforme vazio em conclusão
ou copie a estrutura de um grafo como se fosse topologia inspecionada.

| Slot | Fonte a ler / pergunta | Campos materiais recuperáveis | Forma útil |
|---|---|---|---|
| Header e scope | spec: quem ganha o quê? | identidade, problema, objetivo, beneficiário, transformação, benefício, critério, escopo/anti-escopo, requisitos/restrições | síntese curta, cards de valor e detalhes de requisitos |
| architecture | plan/impact e contratos da spec: como o atual chega ao alvo? | atual/alvo/delta, responsabilidades, relações, interfaces/dados, confiança, sucesso/falha, preservado e limites | SVG conectado, texto equivalente, unidades e matriz de contratos |
| impact | impact/rollback do plan: onde surge exposição? | superfície/delta, sinal, risco, controle, contingência, owner, reversão e prova | footprint, matriz e recuperação |
| execution | tasks/ordem do plan e estado disponível: por que este incremento vem agora? | outcome/incremento, FR/AC/discovery, escopo, dependências, risco/assurance, status/autoridade, exit e evidência | ledger de dependências e dossiês com detalhes |
| validation | ACs da spec e validation-plan: qual observação decide o aceite? | método, comando/passos, ambiente/fixture, oráculo, evidência/owner, estado e limite | matriz AC/prova e cards de prova |
| evolution | decisões/progress/ratchet material: o que mudou e com qual consequência? | contexto, alternativa, status, consequência, owner, propagação, checkpoint e aprendizado | registros/timeline |
| decision | decisão atual em MD e YAML como metadado: que ação é autorizada? | pronto/pendente, autoridade, owner, consequência, conflito e próximo passo exato | chamada de decisão e limites localizados |
| coverage | todas as fontes aplicáveis: o que deveria existir e onde ficou? | arquivo/heading → fato esperado → disposição → aba/bloco; razão/omissão/ausência | um registro humano iniciado pelas fontes, sob BC-006 |

## Componentes e densidade

Um card é uma unidade comparável com seus campos; uma tabela expõe uma
matriz ou contrato; `details` conserva material longo recuperável na mesma
aba. Use síntese objetiva com detalhes ricos. Não omita um campo material
para caber em um card e não imponha número de cards/palavras como qualidade.
Quantidades mantêm unidade, contexto e fonte; capacidade, baseline, SLA e
benefício sem medida fornecida permanecem limites de BC-015.

O SVG de scaffold ensina nós/arestas editáveis. Substitua-o por relações
efetivamente lidas, com labels de contratos/dados, estados por texto e
fronteiras visíveis. `title`/`desc` fornecem o nome/descrição acessíveis;
`.diagram-equivalent` permite recompor o fluxo sem ver o desenho. Registre
uma ausência fundamentada quando a fonte não estabelece relação material.
Diagramas/tabelas largos rolam localmente; o documento não se alarga.

A identidade padrão dispensa logo. Um perfil escolhido explicitamente pode
embutir o asset local autorizado no próprio HTML por BC-011/024. Preserve
a origem do asset selecionado; não busque fonte, biblioteca ou imagem remota.

## Fechamento autoral

A copia pronta declara `data-harness-template-kind="composed"` e a fase
real da operação; o scaffold não é entrega. O snapshot e handoff seguem
BC-025. A entrega autoral segue diretamente para B/conteúdo e B/visual por
BC-009. Os checks usados para desenvolver este template não acrescentam
uma terceira etapa à geração normal de um brief.
