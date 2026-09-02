# Decision log — SPEC 024

## D-024-001 — Classificar o artefato apresentado como candidato técnico inadequado

**Date:** 2026-08-31  
**Status:** accepted for correction  
**Owner:** delivery orchestrator  
**Decision:** `testes/mock-runs/20260831-spec023-t004-r1/m005-ai/t004-candidate.html`
é candidato técnico, neutro e descartável do corpus T-004; não é referência
Pearson nem implementação fiel dos mocks M-023.

**Evidence:** screenshot do requester, `reproduction.md`, README T-004 e
comparação com `M-023-B-architecture.png`.

**Consequence:** não promover, não reapresentar como exemplo final e criar
referência isolada antes de extrair mudança reutilizável.

## D-024-002 — Gráficos factuais serão HTML/SVG, não imagem gerada

**Date:** 2026-08-31  
**Status:** accepted for T-001  
**Owner:** brief experience owner  
**Decision:** SVG/HTML nativo será usado para topologia, mapa de mudança, zoom e
assurance. Imagem gerada é hipótese estética, não diagrama factual: não fornece
texto, contraste, impressão, proveniência ou responsividade confiáveis.

**Consequence:** visual satisfaz T-001 somente quando legível e factual no
render; não por um mock de imagem sofisticado.

## D-024-003 — Autorização de execução e revisão independente

**Date:** 2026-08-31  
**Status:** granted  
**Authority:** requester  
**Decision:** requester autorizou execução das specs necessárias e avaliação
semântica/visual agêntica. Isso autoriza T-001, mas não substitui veredito
independente nem promove históricos/corpus.

## D-024-004 — Referência M-005 aprovada como prova visual isolada

**Date:** 2026-08-31  
**Status:** approve for T-001 only  
**Builder:** `/root/spec024_visual_reference_builder`  
**Reviewer:** `/root/spec024_visual_reference_reviewer`  
**Input:** `m005-executive-reference.html` SHA-256
`BA71D86EF45599835B04A7E28604C175B88A7C9382A7FCF73519A7E60D7D5716`.

**Decision:** a referência passou a revisão visual/factual independente. Ela
tem topologia, registro de superfícies, zoom e assurance legíveis no render,
aplica Pearson materialmente e não inventa frontend, MySQL direto ou qualidade
do modelo. A aprovação é estritamente da referência descartável, não de T-004,
históricos ou de um contrato de template ainda não revisado.

## D-024-005 — Contrato reutilizável aprovado após revisão adversarial

**Date:** 2026-08-31  
**Status:** approve  
**Builder:** `/root/spec024_visual_contract_builder`  
**Reviewer:** `/root/spec024_visual_contract_reviewer`  
**Decision:** o guard só é aplicado quando a rota declara materialidade; protege
topologia conectada, relações por endpoints, legenda visível, escala, zoom/N-A
e equivalentes acessíveis. Dois bypasses encontrados pelo revisor foram
corrigidos e cobertos por regressão. Não substitui revisão visual/factual.

## D-024-006 — Corpus visual heterogêneo aprovado sem promoção

**Date:** 2026-08-31  
**Status:** approve for T-003 only  
**Builder:** `/root/spec024_visual_heterogeneous_builder`  
**Reviewer:** `/root/spec024_visual_heterogeneous_reviewer`  
**Decision:** os oito renders isolados são prova heterogênea aprovada. A revisão
exigiu e confirmou first viewport gráfico, topologias por domínio, factualidade,
PDF/mobile legíveis e hash preservado do candidato T-004. Esta decisão não
adota, atualiza ou substitui briefings históricos.

## D-024-007 — Exceção limitada de visibilidade humana para a SPEC de bundle

**Date:** 2026-08-31  
**Status:** reviewed  
**Owner:** Guardian maintainers and brief experience owner  
**Decision surface:** human visibility gate  
**Rationale:** a SPEC 024 altera o bundle reutilizável e a sua prova é composta
por referências descartáveis renderizadas e revisadas de forma independente.
Criar um nono `stakeholder-brief.html` canônico dentro desta SPEC faria parecer
que houve adoção em um consumidor. A exceção `not_applicable` é portanto
limitada ao brief canônico da própria SPEC, não aos oito artefatos de prova.

**Consequence:** o gate registra a limitação de forma visível; T-001 e T-003
permanecem submetidos às capturas desktop/mobile/PDF, à revisão independente e
à preservação de T-004. Uma adoção futura em consumidor exige seu próprio
brief, baseline e revisão normal — esta decisão não os dispensa.
