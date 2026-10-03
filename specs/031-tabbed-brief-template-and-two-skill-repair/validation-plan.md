# Validation Plan — 031

**Status:** validation_done — AC-001..017 aceitos por /root; D-016
**Owner:** Guardian maintainers
**Last updated:** 2026-10-02

## 1. Boundary and strategy

Aceitar a implementação do novo caminho do bundle, uma vez, com oráculos
proporcionais. Não acrescentar uma terceira validação ao uso normal do
brief. Não avaliar a qualidade dos MD nem repará-los para o teste passar.

Reutilizar cópias imutáveis dos oito pacotes de
testes/mock-runs/20260921-spec029-t009-m00N/initiative/ em uma NOVA raiz de
laboratório. O modelo minimal antigo e o HTML antigo são comparação
histórica; a implementação nova deve executar autoria A + duas skills B.
Não criar aplicação, executar suas tasks ou fabricar autoridade/gates.

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | Hashes | SHA-256 das fontes antes/depois de cada caso. | Bytes idênticos. | evidence/T-005.md | Builder do lab / evaluator distinto |
| V-002 | AC-002 | Artefato + browser | Abrir arquivo único; inspecionar requisições/refs de assets. | Conteúdo/estilo/SVG/navegação não dependem de rede nem arquivo auxiliar. | evidence/T-002.md, evidence/T-005.md | Builder / evaluator |
| V-003 | AC-003 | DOM/browser | Abrir todas as abas, contar IDs/painéis visíveis; reproduzir coverage duplicado. | Oito abas, IDs únicos, um painel por vez. | evidence/T-002.md, evidence/T-005.md | Builder / evaluator |
| V-004 | AC-004 | Browser | Abrir via HTTP e arquivo/preview quando suportado; desabilitar JS e trocar abas. | Troca funcional sem empilhar painéis. Ambiente não suportado é limite explícito. | evidence/T-002.md, evidence/T-005.md | Builder / evaluator |
| V-005 | AC-005 | Leitura de fonte/HTML | Recuperar objetivo, beneficiário, benefício e critério realmente existentes. | Fatos fiéis; ausência fonte não vira métrica inventada. | evidence/T-005.md | Evaluator |
| V-006 | AC-006 | Leitura qualitativa independente de aceite | Usar matriz de §3 sobre fontes congeladas e HTML final. | Fatos existentes recuperáveis; nenhum omitido/contradito ou só linkado. | evidence/T-005.md | Evaluator |
| V-007 | AC-007 | SVG/explicação | Inspecionar nós/arestas, labels/legend/texto equivalente e fronteiras nas oito arquiteturas. | SVG conectado explica relações das fontes, sem inventar topologia. | evidence/T-002.md, evidence/T-005.md | Builder / evaluator |
| V-008 | AC-008 | Slot/artefato | Examinar todos os slots editoriais e ausências condicionais. | Sem scaffold vazio; limites reais qualificados. | evidence/T-002.md, evidence/T-005.md | Builder / evaluator |
| V-009 | AC-009 | Ensaio comportamental | Remover fato material existente de um HTML isolado; executar primeira skill high/xhigh. | Reparador detecta/localiza e recupera no HTML; MD intactos. | evidence/T-003.md | Builder / evaluator |
| V-010 | AC-010 | Ensaio visual | Degradar SVG/card/título/fluxo em cópia; executar segunda skill high/xhigh. | Reparos no mesmo HTML preservam fatos. | evidence/T-003.md | Builder / evaluator |
| V-011 | AC-011 | Configuração/traço | Inspecionar esforço efetivo fornecido pelo executor, não só prompt; caso medium. | Ambas high/xhigh ou superior; medium indisponível não vira conclusão. | evidence/T-003.md | Builder / evaluator |
| V-012 | AC-012 | Traço operacional | Executar caminho normal e ler chamadas/hand-offs e identidades efetivas. | A → B conteúdo → B visual → relato; A_id != B_conteúdo_id e B_conteúdo_id == B_visual_id; sem modelo/pré-review/terceira validação. | evidence/T-003.md, evidence/T-004.md | Builder / evaluator |
| V-013 | AC-013 | Inventário versus HTML | Fonte/heading/fato → bloco/aba; caso com item intencionalmente ausente. | Cobertura honesta, não só lista de blocos emitidos. | evidence/T-003.md, evidence/T-005.md | Builder / evaluator |
| V-014 | AC-014 | Estado/relato | Examinar autoridade e status após concluir brief. | Nenhuma implementação autorizada, task done/approve/evidence inventados. | evidence/T-004.md | Builder / evaluator |
| V-015 | AC-015 | Compatibilidade | Congelar hashes de briefs 1/2 e executar leitores/dispatch 3. | Históricos iguais/legíveis, sem gates 3 forçados. | evidence/T-001.md, evidence/T-004.md | Builder / evaluator |
| V-016 | AC-016 | Experiência | Desktop 1280x800 e mobile 390x844, teclado/print, todas as abas. | Navegação/leitura operáveis, sem overflow do documento/header sozinho na tela. | evidence/T-002.md, evidence/T-005.md | Builder / evaluator |
| V-017 | AC-017 | Entry point/contrato | Invocar o novo fluxo pelo entrypoint documentado. | Três mandatos efetivos; cadeia antiga não é executada por baixo. | evidence/T-001.md, evidence/T-004.md | Builder / evaluator |

## 3. Matriz de fatos materiais dos mocks

Usar os fatos efetivamente presentes nos MD congelados. Não exigir que a
nova composição invente valores/contratos que constam somente no pedido
bruto. Se um item não consta nas fontes, marcar limite com locator; isso
não autoriza modificar fonte, declarar o fato recuperado ou excluir da
análise um fato presente em outro heading.

| Caso | Fontes | Fatos/relações a recuperar no HTML |
|---|---|---|
| M-001 blog | spec, plan, impact, tasks, validation | Publicação draft→published; sessão/RBAC no servidor; User/Session/Post; cinco APIs declaradas; conflito/slug; riscos e oráculos; rollback/ordem das tasks. |
| M-002 conciliação | spec, plan, impact, tasks, validation | Arquivo→fila→reconciliação→divergências; centavos/timezone; lote corrigido com auditoria; idempotência; retry/DLQ/recuperação no nível existente; controles/provas. |
| M-003 mobile offline | spec, plan, impact, tasks, validation | Máquina de estados/sync; token expirado; upload parcial e conflito checklist; dados/retenção declarados; acessibilidade; recuperação/oracles. |
| M-004 multiplataforma | spec, plan, impact, tasks, validation | Mobile/web e adaptadores; código nativo isolado; GraphQL; cache/mutações/confirmação; acessibilidade/paridade/CI; limites de fonte. |
| M-005 IA local | spec e R2, impact, plan, tasks, validation | Origem→modelo local→API destino/MySQL; proibição de acesso direto; modelo/rubrica/prompt/confiança; gate humano; limites da nota; privacidade; prova determinística versus probabilística. |
| M-006 documentos | spec e R2, impact R2, plan, tasks, validation | Ingestão→quarentena/scan→extração→agente/validação→HTML/PDF; custódia; totais determinísticos; review humano; containers/isolamento; operação. Não alegar faltar breakdown já descrito no R2. |
| M-007 quiosque | spec, plan, impact, tasks, validation | Acessibilidade com AC/oracle; busca/mapa/texto; cache/offline/API; sem resultado; impressora sem papel; reset/limpeza; contextos desktop/quiosque/print/no-JS aplicáveis. |
| M-008 estoque | spec, plan, impact, tasks, validation | Eventos/ordem/idempotência; consistência eventual, watermark/atraso→erro no nível existente; replay limitado/autorizado/isolado; snapshot/rollback; cache sem inventar que nunca recebe escritas. |

Para todos: valor/outcome, anti-escopo, execução/validação, decisões materiais
e autoridade/estado que as fontes forneçam. Históricos conflitantes ficam
visíveis como limite, não são corrigidos pelo lab.

## 4. Environment and exact commands

No repositório fonte:

    python scripts/validate_bundle.py
    python -m pytest scripts/ -q -p no:cacheprovider

Depois da mudança, executar também os standalone de contrato realmente
afetados pelo dispatch/template/fluxo. Pytest não coleta todos os scripts
test_*.py. Documentar a lista no evidence pack e não usar contagem da suíte
como prova semântica. Os comandos atuais são regressão do bundle, não etapa
obrigatória pós-skill do contrato 3.

Preview de laboratório, limitado a loopback e à nova raiz:

    python -m http.server 4179 --bind 127.0.0.1 --directory <nova-raiz-do-lab>

Usar a ferramenta de browser disponível; registrar URL, viewport, JS ligado/
desligado, contexto file/preview se disponível e screenshots com estado.
Não usar snapshot-only como prova visual nem simular execução do produto.

## 5. Assurance and failure disposition

**Profile:** A2-elevated. Oráculos de DOM/hashes para integridade;
experimentos de skills para reparo; leitura independente para significado;
browser para experiência. Sem score de texto/cards.
**Executor:** builder de cada task, atribuído após OK.
**Evaluator:** identidade distinta; não edita a implementação julgada.
**Failure:** task da 031 volta a needs_revision; fonte de mock não é reparada.
**Waiver:** ausência realmente na fonte/ambiente fica delimitada; não dispensa
fato existente nem transforma medium em high.
**Runtime boundary:** essa avaliação de implementação não acrescenta um
avaliador/skill/approval depois de B em cada geração normal.

## 6. Validation decision

**Validation Ready:** yes
**Reviewer:** /root/review_spec031 — independente da autoria, esforço high; 2026-10-02
**Decision evidence:** evidence/planning-review.md
**Implementation checks executed:** T-001..004 aprovadas por /root; 319 checks,
89 pytest e 27 standalones passaram. Ensaio real de duas skills em T-003.
Aceitação semântica/visual dos oito mocks concluída em T-005: leitura material,
256 seleções nativas, fontes/estado preservados e oito checks mecânicos PASS.
Evidências: evidence/T-005.md e evidence/T-005-source-acceptance.md; D-016.
**Historical evidence:** laboratório de 02/10 e 314 checks do bundle antes
da implementação; não são resultados de aceite da 031.
