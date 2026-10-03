---
name: executive-brief-experience-review
description: Abra todas as oito abas do stakeholder brief e repare explicação, SVG, hierarquia, cards, títulos e navegação no próprio HTML após o reparo factual pelo mesmo B qualificado; preserve o review de construção histórico somente para contrato 1/2 explícito.
version: "0.3.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Executive Brief Experience Review

## Selecionar a versão e confirmar o reparador

Leia `.harness/rules/brief-contract.md` e aplique BC-002. No contrato 3,
esta skill é o segundo mandato, B/visual, depois de
`rendered-brief-decision-review`. Confirme o HTML/digest de saída factual,
`A_id != B_content_id` e `B_visual_id == B_content_id`. Confirme novamente
o esforço efetivo `high`/`xhigh` ou superior suportado a partir da
configuração/traço nativo do executor por BC-025, com referência registrada.
Não trate promessa no prompt ou metadata do candidato como prova real.
`medium`, configuração desconhecida ou identidade incompatível são
`incomplete`, sem conclusão qualificada. Não imponha modelo/provider.

MD é somente leitura e correto por premissa. Confronte o snapshot factual
antes/depois: uma fonte alterada interrompe esse snapshot, com paths e
digests no relato; não edite MD, reabra planejamento ou declare sincronismo
falso. YAML operacional pode receber o registro, sem alterar autorização.

## Contrato 3 — abrir, explicar e reparar

Abra o próprio HTML em browser no contexto suportado, por arquivo/preview
ou loopback. Registre URL/contexto, viewport e JS ligado/desligado quando
suportado. Visite as oito abas, inclusive coverage; faça leitura visual e
operação, não somente snapshot de DOM ou uma landing page. Se não existe
browser capaz de abrir todas, o mandato visual fica `incomplete`. Contexto
específico não suportado é limite explícito BC-016, sem fingir teste.

Se o executor B não expõe browser, mas um operador/orquestrador dispõe de
ferramenta nativa, B pode solicitar abertura, interação e capturas reais.
B interpreta todas as oito abas, decide e edita por conta; o operador
somente executa os passos mecânicos, sem julgamento/aprovação ou terceira
skill. Registre operador, backend/contexto real e limite da sessão B.
Sem imagens/interações reais de browser capaz, permanece `incomplete`.

Leia as fontes/locators necessários para explicar o que B/conteúdo
recuperou. Repare diretamente no mesmo HTML os defeitos encontrados:

- Título e abertura respondem à pergunta da aba com transformação,
  benefício/critério e ação específicos; elimine preâmbulo genérico e
  placeholders visíveis, preservando o fato e o limite real.
- Hierarquia e densidade tornam unidades comparáveis: cards com campos,
  tabelas para matrizes/contratos e detalhes progressivos para material
  extenso. Encurte redundância, sem apagar contratos, riscos, tasks, provas
  ou fatos recuperados para caber no layout.
- Arquitetura material usa SVG inline conectado de BC-012/014. Repare nós,
  arestas dirigidas, nomes, labels de dados/contratos, fronteiras, estados
  textuais, `role="img"`/nome/descrição e equivalente legível. Faça o desenho
  explicar relações sustentadas pela fonte, sem inventar topologia,
  capacidade ou detalhe operacional. Cartões ou setas tipográficas sozinhos
  não substituem o SVG material; uma ausência real recebe BC-015.
- Preserve identidade selecionada e tokens do template, fonte de sistema,
  CSS/JS/SVG/asset autorizado inline e título `h1` único. Corrija hero
  desproporcional, título/chrome competindo com o conteúdo, alinhamento e
  contraste conforme a leitura disponível. Nenhuma quantidade fixa de
  cards, desenhos ou palavras prova qualidade.
- Preserve as oito abas e um painel principal por vez em tela, também sem
  JS. Radios nativos permanecem focáveis, labels mostram seleção/foco,
  teclado e alvos de coverage funcionam, hash abre o painel correto com
  JS e targets mostram aba/bloco em texto sem JS. Print pode exibir todas.
- Observe desktop 1280×800 e mobile 390×844, foco/teclado, redução de movimento
  e impressão no ambiente suportado. Cards se reorganizam; tabelas/SVG
  largos rolam localmente, sem overflow horizontal do documento. Faça o
  cabeçalho permitir acesso ao conteúdo na tela inicial.

Inspecione enquanto corrige e restaure os fatos se um ajuste visual os
enfraqueceu. Se encontrar nova omissão disponível na fonte durante este
mandato, recupere-a no mesmo HTML e atualize coverage; não transforme isso
em rerun obrigatório de B/conteúdo, retorno a A ou terceira validação.
Confirme a relação entre desenho, texto e dados recuperados; não declare
qualidade só porque o DOM é estruturalmente válido.

Ausência real mantém locator, efeito na decisão e owner/caminho fornecidos
por BC-015. Limite de ambiente informa a observação não feita. Não remova
uma aba para esconder dúvida nem invente autoridade, origem, baseline ou
evidence. A inspeção para terminar reparos pertence a esta skill e não é
uma aprovação dos próprios bytes.

## Relato final e fechamento

Registre em evidência/estado existente ou relato: A/B, referência e esforço
efetivo por mandato, snapshot intacto, contexto de browser/abas abertas,
reparos visuais e fatos preservados/recuperados, limites, HTML/path/digest
final. Complete `brief_repair.visual.{actor,effective_effort,execution_ref,
completed_at,status}` e `rendered_sha256` quando esse bloco existir.

Encerre com `completed`, `completed_with_source_limitations` ou `incomplete`
(BC-020/025). Depois de B/conteúdo → B/visual, o relato termina a operação:
sem reapproval, mandatório rerun factual ou terceiro avaliador/skill de
validação. Conclusão não é `approve`, task done, aprovação de evidência,
`Tasks Ready` ou autorização de produto. Mantenha o evaluator da mudança
de implementação distinto dos bytes que ele julga.

## Histórico 1/2 — somente quando selecionado

BC-002 preserva o lifecycle 1. Em 2 explícito, esta skill executa pass (a)
de BC-009, review de modelo/construção antes da projeção. Reviewer distinto
do compositor/builder lê solicitação, fontes, `brief-model.yaml` e plano
de validação; não edita modelo/HTML/CSS durante essa avaliação.

Examine tese/audiência, rotas selecionadas BC-007/022, relações materiais,
forma e razão, componentes, limitações e fechamento. Lentes proporcionais
incluem decisão, narrativa, arquitetura/operação, experiência e confiança.
Registre locators/digests, materialidade, finding/perda/invenção, impacto,
recovery canônico e reviewer de origem. `APPROVE` permite somente projeção;
`REVISE` retorna à composição/re-review. Pass (b) posterior é o rendered
review de BC-009, com rotas selecionadas em loopback BC-016 e sem editar
durante avaliação; untouched scaffold material exige `REVISE`.

Não confunda esse reviewer histórico com o reparador 3 ou com aprovação de
task/evidence. BC-015/017 preservam limites/exceções históricos e nenhum
verdict permite ao reviewer marcar a própria task done.
