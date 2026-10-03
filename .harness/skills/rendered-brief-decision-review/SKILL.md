---
name: rendered-brief-decision-review
description: Compare o stakeholder brief HTML às fontes canônicas e recupere diretamente fatos materiais omitidos, contraditos ou inventados no contrato 3; use como primeiro mandato do reparador distinto da autoria e preserve o review histórico quando 1/2 estiver explicitamente selecionado.
version: "0.3.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Rendered Brief Decision Review

## Selecionar a versão e o mandato

Leia `.harness/rules/brief-contract.md` e aplique o dispatch de BC-002.
No contrato 3, esta skill é B/conteúdo: comparar e reparar o próprio HTML
composto por A. Não é aprovação dos bytes editados por B. O procedimento
histórico ao final aplica-se somente a 1/2 explícito.

Antes de concluir um mandato 3, confirme `A_id != B_id`, o path/digest do
candidato e a configuração efetiva `high`/`xhigh` (ou superior suportado)
fornecida pelo executor. Registre a referência da configuração/traço real
por BC-025. Texto de prompt, frontmatter ou esforço declarado pelo próprio
HTML não provam configuração efetiva. `medium`, esforço desconhecido ou
reparador qualificado indisponível resultam em `incomplete`; não os relate
como execução qualificada. Use o modelo/capacidade disponível, sem inventar
API universal ou exigir provider específico.

## Contrato 3 — comparação e reparo factual

Receba o handoff de A com solicitação, HTML exato, autoria, fontes/locators,
snapshot SHA-256 e limites. Leia integralmente as fontes aplicáveis de
BC-003 e suas revisões/supersessões. MD fornecido é correto por premissa e
somente leitura. YAML é metadado operacional; atualizar `brief_repair` não
autoriza alterar gates, tasks ou aprovação.

Confronte o snapshot antes de editar. Se um MD mudou desde o handoff,
interrompa o reparo desse snapshot e relate paths/digests afetados como
`incomplete`; não estabilize editando fontes nem conclua freshness falsa.
Quando o handoff não registra snapshot, capture os hashes dos MD lidos
antes do reparo e confirme os mesmos bytes ao fechá-lo.

Parta do inventário esperado nas fontes, não somente dos blocos que A
emitiu. Para cada heading/FR/AC/task/decisão/risco material, identifique
o fato, onde deveria ser recuperável e a diferença no HTML. Aplique os
contratos de aba BC-013 e os slots do kit de composição. Recupere objetivo,
beneficiário, benefício/critério, contratos/dados, responsabilidades,
relações/falhas, controles, ordem/exit/provas e autoridade efetivamente
fornecidos. Leia detalhes expansíveis também; link para MD não substitui
fato core no HTML. Nenhuma quota de palavras/cards decide completude.

Localize cada omissão, contradição ou invenção com fonte/heading/fato e
aba/bloco, explique seu efeito na decisão e corrija o mesmo arquivo HTML.
Restaure o fato existente, substitua afirmação contraditória e remova
invenção com o limite correspondente. Preserve oito abas, identidade,
componentes, SVG e proveniência BC-005/006; expanda unidades/detalhes quando
necessário. Não retorne a A para regeneração rotineira e não encerre com
lista de findings corrigíveis esperando autorização do usuário.

Distinga omissão de composição de ausência real da fonte. Ausência recebe
no HTML fato exato, locator, impacto e owner/caminho somente se fornecidos
(BC-015); owner/caminho ausentes ficam explícitos. N/A exige fundamento.
Não invente baseline, capacidade, SLA, métrica, topologia ou aprovação.
Contradição histórica continua visível como limite de fonte, sem reabrir
gates de planejamento ou exigir que o MD seja reescrito.

Repare também coverage: fonte/heading → fato esperado → aba/bloco e
disposição honesta. Uma linha `represented` não encobre fato que ainda
falta. Corrija locators/targets e mantenha limitações reais qualificadas.
Não acrescente modelo, projeção determinística, suficiência prévia ou mapa
narrativo paralelo como pré-requisito 3.

Faça a inspeção necessária para terminar os próprios reparos e confirmar
os bytes de fonte. Essa inspeção integra o mandato; não abre aprovação ou
re-review. Registre fatos recuperados e digest do HTML que segue para
`executive-brief-experience-review`, executada pelo mesmo B com esforço
efetivo qualificado. Não imponha rerun desta primeira skill após o visual.

## Registro e handoff para B/visual

Em evidência/estado existente ou no relato, registre autoria A, identidade
B, configuração efetiva/referência, snapshot, path/digest antes/depois,
reparos com locators e limites. No `brief_repair` existente, use
`author`, `source_snapshot` e `content.{actor,effective_effort,execution_ref,
completed_at,status}`; entregue o digest atual ao mesmo B/visual.
Não duplique uma narrativa fora do HTML nem copie segredos/PII desnecessários.

Use `completed`, `completed_with_source_limitations` ou `incomplete` conforme
BC-020/025. A conclusão factual não é `approve`, task done, evidence
approval, `Tasks Ready` ou autoridade para implementar. O relato final
vem depois do segundo mandato; nenhum terceiro agente/validador semântico
ou ciclo de reapproval é requisito do uso normal 3.

## Histórico 1/2 — somente quando selecionado

BC-002 preserva o lifecycle 1. Para 2 explícito, esta skill executa pass
(b) de BC-009: reviewer distinto do autor/builder lê fontes, construção
revista e HTML renderizado em loopback BC-016, sem editar durante o review.
Registre locators/digests, identidade, timestamp, URL exata e ambiente.
Escolha lentes materiais e registre julgamento qualitativo por aba:
`recoverable`, `superficial`, `absent` ou N/A fundamentado, e
`APPROVE`/`REVISE` com perda factual, impacto, recovery na composição e
re-review de origem. Falha material não recebe aprovação.

No ramo 2, findings retornam ao compositor/modelo/projeção e ao re-review
previsto; patch apenas no HTML não fecha finding. Exceções editoriais
seguem BC-017 sem dispensar integridade/lifecycle. Registre checks
determinísticos separadamente do julgamento qualitativo e do próximo
passo. Esse mandato de reviewer e suas restrições não se acumulam com o
reparo direto 3.
