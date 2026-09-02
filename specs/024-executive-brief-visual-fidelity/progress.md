# Progress — SPEC 024

## Checkpoint 2026-08-31 — mismatch reproduced

O requester abriu `m005-ai/t004-candidate.html?view=architecture` e identificou
que ele não é o target visual gerado/aprovado. A comparação confirma: M-023-B
prevê topologia, registro gráfico de mudança e zoom; o candidato do corpus
renderiza relações principalmente em texto. Ele também é neutro por design,
logo não demonstra `pearson-design.md`.

## Checkpoint 2026-08-31 — correção em curso

SPEC 024 foi criada como bugfix sistêmico. T-001 constrói uma referência M-005
em raiz nova; corpus T-004 e HTMLs históricos permanecem preservados. Próximo
checkpoint seguro: revisão independente do render congelado. A saída não será
tratada como template/adaptação ampla sem esse parecer.

## Checkpoint 2026-08-31 — referência aprovada

O avaliador distinto aprovou o HTML M-005, as capturas desktop/mobile/full e o
PDF. Confirmou topologia conectada, escala declarada de seis superfícies, zoom
do serviço, assurance determinístico/probabilístico, limite de frontend/MySQL,
identidade Pearson e fallback de navegação. T-002 começou para prevenir que o
renderer volte a degradar esse tipo de visual em texto genérico.

## Checkpoint 2026-08-31 — contrato T-002 congelado

T-002 introduziu o contrato mínimo para uma rota que **declara** arquitetura
visual material: topologia SVG/HTML semântico com nós e relações nomeadas,
legenda dos quatro estados, mapa de superfícies com unidade honesta e zoom
fonte-apoiado ou N/A/descoberta explícito. O teste negativo prova que uma rota
material composta somente de texto falha objetivamente; uma rota imaterial não
recebe obrigação decorativa de SVG. Os checks focais e o bundle passaram.
O checkpoint é `needs_evaluation`, não aprovação visual/semântica.

## Checkpoint 2026-08-31 — REVISE T-002 reparado

A revisão independente encontrou um bypass: peças SVG/HTML soltas fora da
projeção podiam satisfazer o check. O reparo mantém a árvore da rota,
exige que primitivas pertençam à respectiva projeção e prova conectividade por
endpoints entre IDs de nós declarados. Também rejeita legenda, texto equivalente
e nome SVG vazios. Foram adicionadas regressões para SVG desconexo/vazio e HTML
semântico vazio. T-002 continua `needs_evaluation`; esta correção não é uma
autoaprovação.

## Checkpoint 2026-08-31 — segundo REVISE T-002 reparado

O revisor encontrou uma aresta adicional de endpoint desconhecido que passava
porque havia outra relação válida. O contrato agora exige os atributos exatos
`data-architecture-relation-from/to` em **cada** relação, com endpoints não
vazios, existentes e distintos. Regressões cobrem uma ligação válida mais uma
desconhecida e uma auto-relação. Os checks completos passaram; a task continua
`needs_evaluation` até nova decisão independente.

## Checkpoint 2026-08-31 — T-003 composto e aguardando avaliação

O builder criou uma raiz nova e inequivocamente descartável para M-001…M-008:
`testes/visual-reference-runs/20260831-spec024-heterogeneous/`. Cada caso tem
HTML Pearson offline, oito query subpáginas, captura desktop/mobile e PDF. As
sete arquiteturas materialmente declaradas passam o contrato SVG/mapa/zoom; o
quiosque declara `not-material` e apresenta jornada operacional com razão,
sem fingir backend. Render checks, contrato e `validate_bundle` passaram. O
builder corrigiu na segunda renderização a sobreposição de círculo aqua sobre
o texto da decisão. A saída continuava `needs_evaluation`, não adoção.

## Checkpoint 2026-08-31 — T-003 aprovado e SPEC concluída

O avaliador distinto examinou os oito renders, mobiles selecionados, PDF M-005,
fontes e preservação. Duas rodadas REVISE foram corrigidas: primeiro viewport
com leitura gráfica/material, topologias heterogêneas e fatos M-005/M-006/M-007/
M-008 recuperados; depois, impressão sem `Limite` órfão e chips mobile legíveis.
T-003 foi APPROVE. A raiz nova é referência descartável aprovada, não promoção
do corpus T-004 nem de qualquer brief histórico.

## Checkpoint 2026-08-31 — validação final registrada

O gate de Human Visibility passou com exceção `not_applicable` **revisada e
limitadamente documentada**: esta SPEC de manutenção do bundle não declara um
brief canônico de consumidor. A exceção não reduz as obrigações dos renders de
prova, já verificados e aprovados de modo independente. Também passaram o
contrato visual de arquitetura, sua suíte de regressão, a suíte de Human
Visibility e `validate_bundle` (272 checks). O hash atual do candidato T-004 é
`40DCA6FE4F101C379FB3DD1103CC35CAAEF9D52475AE6AADDD420A08FF63C1A5`, igual ao
marcador de preservação aprovado.
