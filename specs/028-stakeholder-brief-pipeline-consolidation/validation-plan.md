# Plano de validação — SPEC 028

**Status:** validation_ready  
**Spec:** ./spec.md  
**Plan:** ./plan.md  
**Owner:** Guardian maintainers  
**Última atualização:** 2026-09-01

## 1. Estratégia

Validar primeiro a honestidade do lifecycle, depois a forma mínima do artefato
e por fim a experiência do HTML final. Testes determinísticos não aprovam
narrativa ou visual; eles impedem que uma aprovação seja falsificada, mas não
podem impedir que fontes legíveis cheguem ao HTML final mais completo possível.

| Perfil/task | Claim/risco | Técnica | Oracle/evidência | Executor | Avaliador | Falha/waiver |
|---|---|---|---|---|---|---|
| T-001 | Estado contraditório autoriza alegação indevida. | Fixture negativa de lifecycle e coerência de dados. | `REVISE` pre-skeleton recupera e reavalia; final não aprovado só existe após candidate rastreável. | builder | evaluator distinto | Falha aciona recovery no mesmo run, não uma espera por usuário. |
| T-002 | Conteúdo material cai em cards/tabelas vazias. | Contract tests + inspeção de artefato fonte-definido. | Declaração/disposição, dossiers recuperáveis. | builder | evaluator distinto | Retorna ao plano/compositor. |
| T-003 | Tela final não representa rota/aba real. | Preview HTTP local + interação manual/reproduzível. | URL, rota ativa, captura/record. | builder | reviewer final | Preview ausente mantém limitação/REVISE, não retém final. |
| T-004 | Parecer independente vira arquivo fantasma. | Binding de review, digest e estado. | Record oficial e Human Visibility coerente. | builder | evaluator distinto | Sem record não promove prontidão; recovery continua autônoma. |
| T-005 | Correção resolve só M003. | Suite heterogênea M001–M008. | Matriz de resultados por mock. | mock lab | reviewer distinto | Gaps são reportados, não escondidos. |

## 2. Rastreabilidade dos critérios

| ID | AC | Método/nível | Passos/comando | Resultado esperado | Evidência | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | determinístico, negativo | Usar fixture `REVISE` pre-skeleton e outra pós-render com candidate rastreável. | A primeira retorna a correção/review antes do skeleton; a segunda produz final não aprovado; ambas recusam `approved`/Human Visibility. | `evidence/T-001.md` | T-001 |
| V-002 | AC-002 | determinístico | Validar locator/digest/decisão/fase de plan, skeleton, candidate e final. | Não há combinação de arquivo e gate incompatível. | `evidence/T-001.md` | T-001 |
| V-003 | AC-003 | HTTP + manual | Servir o final em `127.0.0.1`, abrir cada rota e confirmar apenas painel ativo/URL recuperável. | Navegação real por subpágina interna desktop. | `evidence/T-003.md` | T-003 |
| V-004 | AC-004 | contract + review | Executar arquitetura visual quando material; inspecionar composição/zooms. | Declaração não é omitida; visual não é cadeia textual repetida. | `evidence/T-002.md` + review | T-002 |
| V-005 | AC-005 | determinístico + processo | Remover/revogar preview, digest ou review record em fixture. | Final continua disponível com limitação; estado não é aprovado/Human Visibility. | `evidence/T-004.md` | T-004 |
| V-006 | AC-006 | revisão de projeção | Em M003, M006 e M007, comparar task/proof no Markdown e no final HTML. | Dossiers recuperam campos existentes; lacunas são explícitas. | `evidence/T-002.md` | T-002 |
| V-007 | AC-007 | integração/mock lab | Rodar M001–M008 do início à matriz final. | Cada linha separa deterministic, review qualitativo e estado final. | `testes/mock-runs/<run>/matrix.md` | T-005 |
| V-008 | AC-008 | regressão | `python scripts/validate_bundle.py` e inspeção de diff/código. | Bundle verde; nenhum módulo cria conteúdo de brief a partir de Markdown. | `evidence/T-005.md` | T-005 |
| V-009 | AC-009 | integração resiliente | Introduzir finding de composição em fixture com fontes legíveis. | Há recomposição automática e final aprovado ou final completo com limitação explícita; nenhuma pergunta ao usuário. | `evidence/T-001.md` | T-001 |

## 3. Regressão e NFRs

| ID | Risco/restrição | Check | Resultado esperado | Evidência |
|---|---|---|---|---|
| V-REG-001 | Herança do skeleton regressa. | Executar `validate_brief_candidate_inheritance.py` em candidate válido e em mutação destrutiva. | Válido passa; mutação falha. | T-002 |
| V-REG-002 | Rule teste token, não fluxo. | Criar fixture em que tokens existem mas estado é inválido. | O lifecycle falha apesar dos tokens. | T-001 |
| V-REG-003 | Review estático finge review final. | Verificar que Human Visibility requer URL HTTP/digest/revisor/decisão. | Record sem uma dessas partes não passa, mas o final não desaparece. | T-004 |
| V-REG-004 | Fallback vira one-page contraditória. | Testar a política D-006 em HTML e contrato. | A documentação/teste descrevem a mesma semântica desktop. | T-001/T-003 |
| V-REG-005 | Escopo cresce para autoria determinística. | Revisão de arquivos alterados. | Nenhum script escolhe formas visuais, escreve narrativa ou constrói blocos finais. | T-005 |

## 4. Comandos obrigatórios

| Comando | Ambiente | Resultado esperado | Tasks |
|---|---|---|---|
| `python scripts/validate_bundle.py` | raiz do repositório | exit 0 após a implementação. | T-005 |
| `python scripts/validate_brief_candidate_inheritance.py <candidate> <skeleton>` | raiz + paths do mock | exit 0 só para herança física/autorizada. | T-002/T-005 |
| `python scripts/architecture_visual_contract.py <candidate>` | raiz + candidate material | exit 0 somente com disposição/forma válida. | T-002/T-005 |
| servidor HTTP local mínimo em `127.0.0.1` | diretório raiz ou run | HTML final navegável na URL gravada. | T-003/T-005 |

O comando exato do preview será resolvido em U-003. Nenhum comando acima
substitui a revisão qualitativa.

## 5. Checagens manuais e artefatos

| ID | Passos | Resultado esperado | Artefato |
|---|---|---|---|
| M-001 | Abrir final HTTP do M003 e alternar scope, architecture, impact, execution, validation, decision/coverage quando aplicável. | Uma subpágina interna por vez, contexto/título e URL coerentes; não um scroll longo. | record em `evidence/T-003.md` |
| M-002 | Comparar arquitetura planejada com tela do M003. | Topologia mostra responsabilidades/mudanças/fronteiras; zooms não repetem o mesmo texto. | review final M003 |
| M-003 | Ler execução de M003/M007 sem abrir Markdown. | Épicos e tasks têm nomes compreensíveis, propósito, dependência, prova e saída. | review final por mock |
| M-004 | Ler validação de M006/M007. | Elemento, método, oracle, AC, evidência, owner e limite aparecem quando a fonte os contém. | review final por mock |

## 6. Evals qualitativos independentes

| ID | Rubrica/oracle | Input | Julgamento de aprovação | Reviewer |
|---|---|---|---|---|
| E-001 | `rendered-brief-decision-review` + intenção do solicitante + plano composto. | `stakeholder-brief.html` servido por HTTP e fontes canônicas. | `APPROVE` só quando um leitor de negócio entende início, meio, fim, fronteiras, tasks e validações sem Markdown; `REVISE` traz fonte → perda → decisão prejudicada → correção e chama recomposição automaticamente. | distinto do autor |
| E-002 | Revisão de generalidade. | Matriz M001–M008 e amostra dos finais. | Nenhum padrão é considerado aprovado apenas por funcionar em um mock. | distinto de T-005 builder |

## 7. Validações indisponíveis ou explicitamente fora de escopo

| Check | Razão | Impacto | Aprovação/owner |
|---|---|---|---|
| Responsividade mobile | Pedido humano define foco desktop. | Não há alegação de suporte mobile. | Owner da SPEC. |
| Preview HTTP quando ambiente não puder abrir loopback | Não há substituto equivalente. | Brief final existe com limitação; não fica Human Visibility pronto. | Nenhum waiver automático. |

## 8. Decisão de validação

**Validation Ready:** yes.  
**ACs mapeados:** yes.  
**Bloqueios:** nenhum de construção; a execução espera somente a autorização
explícita do usuário para começar esta SPEC.
