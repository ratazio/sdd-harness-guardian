# Decision log — SPEC 028

| ID | Data | Decisão | Autoridade | Consequência | Estado |
|---|---|---|---|---|---|
| D-001 | 2026-09-01 | Reorientar a iniciativa para consolidar a cadeia de composição, promoção e revisão final, em vez de adicionar um novo template/gerador. | Decisão humana nesta conversa. | Esta é a direção aceita; implementação ainda requer readiness. | accepted |
| D-002 | 2026-09-01 | Manter autoria do plano e do HTML com agentes; limitar determinismo a lifecycle, integridade, contratos, rota e evidência. | Decisão humana + limites desta SPEC. | Não criar gerador Markdown→HTML, seletor de diagramas ou score visual. | accepted |
| D-003 | 2026-09-01 | `REVISE` bloqueia somente a transição que ele avalia e chama correção + nova revisão autônomas. Candidate/final não pulam skeleton, proveniência ou revisão; um candidate já rastreável pode gerar final explicitamente não aprovado durante recuperação pós-render. | Decisão humana desta conversa. | Run-state e log controlam a veracidade do estado sem criar espera operacional pelo usuário. | accepted |
| D-004 | 2026-09-01 | Human Visibility depende de revisão independente do HTML final servido em HTTP local, ligada a URL/digest/veredito; a revisão não pede aprovação do usuário e devolve correções ao compositor. | Decisão humana desta conversa. | Renderer não será descrito como etapa de melhoria de conteúdo; preview ausente não apaga o final. | accepted |
| D-005 | 2026-09-01 | Disposição de arquitetura material/N/A/discovery precisa ser explícita para acionar contracts existentes. | Proposta técnica, a revisar antes de Plan Ready. | Não haverá diagrama obrigatório universal. | proposed |
| D-006 | 2026-09-01 | No desktop, JavaScript é requisito da navegação por subpáginas internas; sem JS, mostrar aviso/alternativa de leitura honesta, não uma one-page que finja equivalência. | Decisão humana desta conversa. | Ajustar contrato e teste sem bloquear autoria do brief. | accepted |
| D-007 | 2026-09-01 | Inventariar e decidir o papel de validators/skills existentes antes de introduzir novos hooks. | Pendente U-001. | Estruturas órfãs são conectadas, aposentadas ou mantidas como opcionais com razão. | proposed |
| D-008 | 2026-09-01 | O pipeline normal não pede aprovação do usuário final: usa plano suficiente, reviews internos e loop de recomposição; limitações fonte-apoiadas são visíveis no final. | Decisão humana desta conversa. | Uma pergunta externa só é legítima para nova autoridade ou expansão de escopo. | accepted |
| D-009 | 2026-09-01 | Iniciar a execução da SPEC 028. | Objetivo ativo do usuário nesta tarefa. | T-001 é a primeira task; as demais seguem pela ordem e evidências definidas. | accepted |
| D-010 | 2026-09-02 | Proveniência material pertence aos blocos preenchidos dentro de slots; painéis de rota v3 são casca imutável e não afirmam fonte parcial. | Diagnóstico de execução T-002 + contrato de renderer. | Remove a contradição que obrigava o compositor a fabricar hashes ou alterar a estrutura herdada; mantém a proveniência completa e verificável onde há conteúdo factual. | accepted |
| D-011 | 2026-09-02 | A revisão agêntica percorre as oito rotas e devolve `REVISE` para conteúdo editorial reutilizável, mesmo quando a herança, os cards e as abas passam. Chrome funcional estável (navegação, acessibilidade, proveniência fixa e estado honesto de gate) não recebe variação artificial; sua explicação editorial deve ser específica. | Evidência da matriz M001–M008 + decisão de execução desta SPEC. | Impede que o compositor trate o skeleton como prosa parcial e evita um novo blacklist/score determinístico de escrita. Recuperações substituem conteúdo nos slots, sem reescrever a casca. | accepted |

## Regra de recuperação

Uma decisão `REVISE` é registrada como **fonte → perda/ambiguidade → decisão
prejudicada → correção canônica**. Ela não pode ser substituída por arquivo de
review paralelo, texto em progress.md ou artefato HTML posterior. Ela inicia
recuperação autônoma e retém a transição avaliada; não cria espera de aprovação
operacional. Um final não aprovado exige candidate já rastreável e nunca salta
skeleton, proveniência ou revisão.
