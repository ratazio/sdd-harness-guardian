---
name: executive-brief-composition
description: Preencha diretamente o template HTML de stakeholder brief com fatos das fontes canônicas e encaminhe o arquivo a um reparador distinto para conteúdo e experiência; preserve o fluxo histórico quando o contrato 1/2 estiver explicitamente selecionado.
version: "0.3.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Executive Brief Composition

## Selecionar a versão

Leia `.harness/rules/brief-contract.md` e determine o ramo de BC-002 antes
de agir. Nova composição usa 3. Um histórico 1/2 permanece no ramo registrado;
não migre nem regenere seus bytes silenciosamente. Os procedimentos abaixo
de autoria direta aplicam-se somente a 3.

## Contrato 3 — autoria A

Leia o pedido e as fontes aplicáveis de BC-003, incluindo todos os headings,
FRs, ACs, tasks, riscos e decisões materiais. Compare revisões/supersessões
para distinguir grafo ativo de histórico arquivado. Registre locators e um
snapshot SHA-256 dos MD; consulte YAML somente como metadado operacional.
No ramo 3, gaps e conflitos recebem a disposição de BC-015/020; não execute
o pre-check de suficiência 2 como gate nem repare fontes.

Copie `.harness/templates/stakeholder-brief.html` para o candidato único e
preencha seu HTML diretamente. Consulte
`.harness/templates/stakeholder-brief-design.md` para os slots/componentes.
Retenha identidade, oito abas e interação nativa de BC-007/021/024. Perfil/
domínio orienta profundidade dentro das abas por BC-022, não sua remoção.

Para cada slot, responda sua pergunta com os campos materiais das fontes.
Abra a visão com uma tese específica e faça contratos, dados, falhas,
limites, tasks e provas recuperáveis em cards/tabelas/detalhes. Recupere
benefício e critério observável disponíveis, com unidade/contexto; uma
baseline, capacidade ou SLA ausente não vira número. Evite preâmbulo
genérico e cards só de título. Preserve todos os campos materiais mesmo
quando resumir a linguagem.

Quando arquitetura é material, substitua o grafo de scaffold por um SVG
conectado que explique relações reais, atual/alvo/delta, responsabilidades e
fronteiras por BC-012/014. Forneça labels, legenda textual e equivalente
legível; não inferir topologia a partir de nomes de arquivos/tasks. Registre
o limite/N/A exato quando a relação realmente não está na fonte.

Preencha coverage começando pelo inventário das fontes lidas: arquivo/
heading → fato esperado → aba/bloco, por BC-005/006. Compare inclusive o que
ainda não entrou no HTML. Distinga omissão da composição, ausência de fonte,
conflito e N/A; listar somente blocos emitidos não prova recuperação. Use
IDs únicos para targets e links internos, com nome da aba/bloco em texto.
Nenhum fato core material fica somente atrás de link para Markdown.

Use fontes de sistema. CSS, SVG e eventual JS/asset escolhido são inline
por BC-011/024. Dados/textos dos MD não se tornam scripts executáveis.
Um logo selecionado pode ser embutido a partir de bytes locais autorizados,
sem rede; default vendor-neutral dispensa logo. Não instale skills globais.

Remova placeholders visíveis; declare `data-harness-template-kind="composed"`
e fase real. Confirme os hashes de fonte antes do handoff. Se a fonte mudou,
interrompa o snapshot e relate os paths afetados; não conclua sincronização
nem edite o MD para estabilizá-lo.

## Handoff direto A → B

Entregue HTML exato/path/digest, fontes/locators/snapshot, autoria A, limites
e contexto da solicitação. Peça ao executor B distinto de A as duas skills
em sequência BC-009/010, com configuração efetiva de BC-025. Configuração
nativa/traço do executor, não uma promessa no prompt, confirma o esforço.
Não prescreva modelo/provider ou API universal; use a capacidade real.

Use o bloco operacional existente `brief_repair` quando disponível:
`author`, `source_snapshot` (paths de MD → SHA-256), `content` e `visual`
(`actor`, `effective_effort`, `execution_ref`, `completed_at`, `status`),
e `rendered_sha256` final. São metadados de composição/reparo, não
aprovações/gates. Snapshot inclui os MD lidos; atualização operacional de
YAML não equivale a editar o conteúdo das fontes.

Não crie `brief-model.yaml`, projeção determinística, mapa narrativo paralelo
ou review pré-render como pré-requisito 3. A segue para B/conteúdo, depois
o mesmo B/visual; relato final encerra por BC-009/025. Não execute produto
nem conceda autoridade de implementação por entregar HTML.

## Histórico 1/2 — procedimento somente quando selecionado

BC-002 preserva o lifecycle 1. Para composição explicitamente 2, BC-008/009
mantêm `brief-model.yaml`, review distinto de construção (pass a), projeção
com `scripts/project_brief.py` e review rendered (pass b). Antes do review,
execute `scripts/validate_brief_model.py` e
`scripts/validate_source_sufficiency.py` no contexto 2 (BC-019). Findings
retornam ao compositor e à correção/re-review requeridas nesse ramo; não
faça patch HTML como fechamento de finding 2. `render_stakeholder_brief.py`
promove os bytes por seu lifecycle, não compõe narrativa. Não trate esse
procedimento como cadeia oculta sob 3.

### Profile x domain route defaults

Somente para o modelo 2: software parte de scope/impact/decision e pode
acrescentar architecture/execution/validation/evolution; ops acrescenta
execution/validation/evolution; docs execution/evolution; policy evolution;
research validation/evolution. Coverage permanece. Ajuste presença ao
material de fonte e registre razão no model/thesis/plan por BC-022. Uma
relação material não-software é representável; domínio não proíbe topologia.

No ramo 2, o perfil Pearson explícito usa o logo local oficial verificado
pelo renderer em `.harness/assets/brand/pearson-logo-white.png`, como imagem
dentro de link nativo nomeado; não hotlink/data URI/path no bundle instalado.
Baseline histórico: `"Plus Jakarta Sans", "Segoe UI", Arial, sans-serif`
sem fetch; contextos 320/768/1024/1440, teclado e print por BC-021.
Revisão rendered 2 usa URL loopback registrada por BC-016.
