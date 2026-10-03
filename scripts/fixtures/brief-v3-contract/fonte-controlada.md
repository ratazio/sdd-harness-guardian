# Fonte controlada — ensaio T2

Dado sintético somente para apresentação. Nenhuma aplicação/atendimento implementado. Não há baseline, SLA de tempo, capacidade ou infraestrutura real.

## scope
- **initiative:** Ficha de atendimento editorial
- **initiative_id:** ENSAIO-T2
- **data_snapshot:** 02/10/2026
- **estado_fonte:** Ensaio de apresentação
- **categoria_iniciativa:** Atendimento editorial · dados controlados
- **titulo_iniciativa:** Recuperar a orientação editorial
- **transformacao_e_beneficio:** A equipe consulta orientação, contratos e prova em uma ficha portátil, preservando os registros de origem.
- **criterio_observavel:** 8 visões disponíveis; 1 painel selecionado em tela
- **autorizacao_atual:** Somente ensaio de apresentação
- **scope_titulo:** Uma ficha recuperável para a equipe
- **scope_sintese:** A orientação está distribuída em três registros. A ficha reúne fatos para que a equipe encontre a ação e sua justificativa em uma consulta.
- **atores_e_valor:** Equipe editorial encontra orientação; responsável pelo ensaio verifica fonte e limite.
- **beneficio_concreto:** Orientação na própria ficha
- **como_observar_beneficio:** O leitor recupera escopo, fluxo e próximo passo sem reabrir três registros.
- **criterio_sucesso:** 8 visões; 1 painel em tela
- **metrica_unidade_contexto_fonte_ou_limite:** Contagem do DOM/navegador no ensaio; não mede ganho de tempo de atendimento.
- **incremento_demonstravel:** Ficha HTML portátil
- **limite_incremento:** Dados controlados e SVG inline; nenhuma aplicação editorial implementada.
- **escopo_material:** Orientação, fluxo, risco, sequência, prova, decisão e rastreabilidade do ensaio.
- **anti_escopo_e_restricoes:** Sem operar atendimento, editar registros ou publicar serviço. Não há baseline ou SLA de tempo.
- **requisitos_contratos_nfr_e_atores:** <ul><li>F-01: oito visões e um painel por vez com ou sem JS.</li><li>F-02: origem, revisão e orientação rastreáveis.</li><li>F-03: teclado, 390 px e impressão conservam leitura.</li></ul>

## architecture
- **architecture_titulo:** Origem preservada, orientação derivada
- **architecture_sintese:** O registro fornece um item à triagem; a revisão registra a orientação na ficha. O ensaio representa somente essas relações.
- **arquitetura_atual:** Três registros dispersos; processo real não inspecionado.
- **arquitetura_alvo:** Ficha derivada com item, revisão e orientação.
- **arquitetura_delta_preservado:** Consulta portátil acrescentada; registros e autoridade do atendimento preservados.
- **fluxo_arquitetura_titulo:** Do registro à orientação
- **fronteiras_arquiteturais:** Origem preservada; triagem e ficha são artefatos derivados do ensaio.
- **svg_nome_acessivel:** Registro de origem, triagem e ficha de orientação
- **svg_descricao_relacoes:** Registro fornece item à triagem; triagem fornece revisão à ficha; não representa software implementado.
- **no_entrada:** Registro de origem
- **papel_entrada:** Preservado · item
- **no_transformacao:** Triagem
- **papel_transformacao:** Proposta · revisão
- **no_resultado:** Ficha de orientação
- **papel_resultado:** Proposta · consulta
- **relacao_entrada:** item
- **relacao_resultado:** revisão
- **legenda_estados_aplicaveis_com_significado:** <span class="preserved">Preservado: registro fonte</span><span>Proposto: triagem/ficha</span>
- **texto_equivalente_fluxo:** Registro fornece item à triagem. A triagem vincula revisão e orientação na ficha. O registro permanece preservado; a ficha não decide autoridade de atendimento.
- **unidade_arquitetural:** Triagem de orientação
- **unidade_papel_owner:** Relaciona item e revisão; responsável pelo ensaio.
- **unidade_contratos_dados:** Entrada: item com origem. Saída: revisão com orientação; nenhum endpoint definido.
- **unidade_delta_fronteira:** Exposição derivada; bytes fonte permanecem iguais.
- **unidade_falha_recovery:** Fonte alterada invalida snapshot; interromper e registrar divergência.
- **unidade_tasks_validacao:** E-01/E-02; P-01/P-02.
- **limites_confianca_falhas_contrato:** Processo real, capacidade, baseline e SLA não fornecidos. O gráfico explica somente o ensaio.
- **contratos_campos_estados_falhas_material:** <dl class="fields"><dt>Item</dt><dd>Origem e identificador.</dd><dt>Revisão</dt><dd>Item, orientação e snapshot.</dd><dt>Fonte alterada</dt><dd>Interromper sem editar origem.</dd></dl>

## impact
- **impact_titulo:** Conservar origem e explicação
- **impact_sintese:** A mudança está na apresentação; risco principal é perder orientação ou origem ao resumir.
- **superficie_nome:** Ficha derivada
- **superficie_delta:** Agrupa orientação e prova.
- **superficie_fronteira:** Registros e autoridade preservados.
- **superficie_controle_owner:** Omissão → comparar fato/ficha; responsável pelo ensaio.
- **superficie_prova_reversao:** P-02 compara snapshot; descartar ficha incompleta.
- **risco_id_evento_sinal:** R-01: orientação omitida; falta de vínculo na cobertura.
- **risco_probabilidade_impacto:** Leitor perde ação recuperável; probabilidade não estimada.
- **risco_controle:** Comparar item, revisão e orientação com a fonte.
- **risco_contingencia_owner_ou_limite:** Recuperar HTML; responsável pelo ensaio; MD intacto.
- **risco_validacao:** P-02 — hash e leitura.
- **rollback_gatilho_acao_preservacao_owner:** Se orientação faltar ou fonte mudar, interromper/descartar cópia; preservar fonte e snapshot; responsável registra motivo.

## execution
- **execution_titulo:** Do inventário à ficha
- **execution_sintese:** E-01 identifica fatos; E-02 compõe depois para conservar origem e orientação.
- **tasks_autoridade_atual:** Somente ensaio autorizado; atendimento excluído.
- **task_ledger_id_incremento:** E-01 inventário → E-02 ficha
- **task_ledger_dependencias:** E-02 depende E-01 para conhecer fonte.
- **task_ledger_status_autoridade:** Planejado no dado controlado; sem task de aplicação.
- **task_ledger_risco_prova:** Omissão → P-02; navegação → P-01.
- **task_id:** E-02
- **task_status:** planejada no ensaio
- **task_assurance:** comportamento e fonte
- **task_titulo:** Compor a ficha portátil
- **task_outcome_incremento:** Leitor recupera orientação e prova na ficha.
- **task_fr_ac_discovery:** F-01..03; P-01/P-02.
- **task_escopo_anti:** HTML/SVG; sem aplicação, publicação ou source edit.
- **task_dep_razao:** E-01 congela inventário e snapshot.
- **task_risco_controle:** Omissão → leitura factual e cobertura.
- **task_validacao_evidence_owner:** P-01/P-02; logs do ensaio; responsável e avaliador distinto.
- **task_exit_porqueagora:** Visões operáveis e fonte preservada; depois do inventário.
- **task_autoridade:** Somente apresentação; nenhuma operação de atendimento.

## validation
- **validation_titulo:** Provar navegação e preservação
- **validation_sintese:** P-01 observa navegador; P-02 compara hashes/fatos. Não medem desempenho editorial.
- **validation_id_ac_claim:** P-01/F-01/F-03 · oito visões e seleção
- **validation_metodo_contexto_fixture:** Desktop 1280×800; mobile 390×844; ficha controlada.
- **validation_comando_passos:** Alternar opções, teclado, JS desativado e imprimir.
- **validation_oracle:** Um painel em tela; oito em print; sem overflow.
- **validation_evidence_owner_limite_status:** Capturas/logs; responsável pelo ensaio; prova planejada no dado, sem aplicação.
- **proof_titulo:** P-02 · fonte e orientação
- **proof_claim_importancia:** Hash e leitura protegem origem e recuperabilidade.
- **proof_invariante_oracle:** SHA-256 antes/depois idêntico; item/revisão/orientação recuperáveis.
- **proof_humano_probabilistico_limite:** Leitura factual; não estima tempo ou SLA.
- **proof_falha_owner_evidence:** Divergência interrompe; logs por responsável e avaliador distinto.

## evolution
- **evolution_titulo:** Mudança restrita à consulta
- **evolution_sintese:** D-01 escolhe ficha derivada e conserva registros.
- **decisao_id_data_status:** D-01 · 02/10/2026 · definida no ensaio
- **decisao_titulo:** Agrupar orientação preservando origem
- **decisao_contexto_alternativa:** Três registros dispersos; reescrever origem excluído.
- **decisao_consequencia:** Conservar fatos e vínculos sem autoridade de atendimento.
- **decisao_owner_propagacao:** Responsável pelo ensaio; sem propagação para produto.
- **checkpoint_ratchet_material_ou_na_fundamentado:** Fonte congelada antes do navegador. Ratchet N/A: nenhuma falha recorrente fornecida.

## decision
- **decision_titulo:** Concluir somente apresentação
- **decision_sintese:** Ficha e verificações permitidas; atendimento e publicação excluídos.
- **decisao_solicitada_ou_acao:** Observar navegação e fatos
- **autoridade_fonte:** D-01 e fronteira do ensaio: apresentação.
- **decisao_owner_ou_limite:** Responsável pelo ensaio; avaliador distinto julga template.
- **decisao_consequencia_limite:** Conclusão de ficha não aprova task/produto/evidence de atendimento.
- **proximo_passo_acao_owner_condicao:** Abrir oito visões e registrar comportamento/fonte após freeze; responsável pelo ensaio.
- **limites_conflitos_fontes_locators_impacto:** Fonte não contém SLA, baseline, capacidade ou infraestrutura real. Nenhum conflito de autoridade definido.

## coverage
- **coverage_titulo:** Recuperar fatos das fontes
- **coverage_sintese:** O registro parte dos oito headings do dado controlado e aponta fatos para os blocos.
- **coverage_fonte_heading:** fonte-controlada.md#scope
- **coverage_fato_material:** Beneficiário, transformação, benefício e critério.
- **coverage_disposicao:** represented
- **coverage_aba_bloco_legivel_link_interno:** <a href="#scope-benefit">Visão e valor · benefício</a>
- **coverage_razao_ausencia_omissao:** Fato exposto; tempo/SLA ausentes.
- **coverage_limites_fato_locator_impacto_owner_caminho_disponivel:** #architecture: processo real não inspecionado. #scope: baseline/SLA/capacidade ausentes; ganho de tempo não quantificado. Owner/caminho de política real não fornecidos.
- **snapshot_identidade_autoria:** ENSAIO-T2 · autoria /root/presentation031
- **limite_autoridade_relato:** Somente apresentação; nenhum atendimento realizado.

