# Tasks — SPEC 026

**Status:** complete — T-005 aprovada por revisão independente em 2026-09-01.  
**Spec:** [spec.md](./spec.md) | **Plan:** [plan.md](./plan.md) | **Validation:** [validation-plan.md](./validation-plan.md)

| ID | Status | Entrega | Dependência | Risco | Evidência |
|---|---|---|---|---|---|
| T-001 | done | Criar skill/guia de autoria aprofundada | nenhuma | low | evidence/T-001.md |
| T-002 | done | Conectar o guia ao fluxo de autoria existente | T-001 | low | evidence/T-002.md |
| T-003 | done | Criar papel/prompt independente de revisão de profundidade | T-001 | low | evidence/T-003.md |
| T-004 | done | Calibrar com exemplos Markdown mínimos, com e sem localizador de código | T-002, T-003 | low | evidence/T-004.md |
| T-005 | done | Preservar fatos materiais fornecidos e repetir regressão heterogênea | T-001, T-003, T-004 | medium | evidence/T-005.md |

## T-001 — Guia de autoria aprofundada

**Objetivo:** entregar uma única orientação curta, baseada em perguntas, que leva respostas aos Markdown canônicos.  
**Escopo:** perguntas condicionais de FR-026-02 a FR-026-05 e regra de não invenção.  
**Fora de escopo:** schema, parser, score ou texto/HTML gerado por código.  
**Validação:** V-026-01, V-026-02 e V-026-05.  
**Exit:** guia permite a um agente registrar fatos, inspeção, inferência e descoberta sem quota de conteúdo.

## T-002 — Referência no fluxo existente

**Objetivo:** tornar o guia encontrável no momento de criação da SPEC.  
**Escopo:** referência mínima na instrução/workflow já responsável pela autoria.  
**Fora de escopo:** novo comando, hook obrigatório ou mudança do renderer.  
**Validação:** V-026-01 e V-026-05.  
**Exit:** a leitura do fluxo existente leva ao guia, sem acrescentar etapa automatizada.

## T-003 — Revisor independente de profundidade

**Objetivo:** tornar reproduzível uma segunda leitura crítica, distinta do autor.  
**Escopo:** papel/prompt, entrada obrigatória (pedido, SPEC, plano), saída `PASS`/`REVISE` e formato de achado FR-026-07.  
**Fora de escopo:** reescrever a SPEC, aprovar implementação ou aplicar score.  
**Validação:** V-026-03.  
**Exit:** um revisor pode explicar concretamente qual perda prejudica qual decisão e onde corrigir.

## T-004 — Calibração proporcional

**Objetivo:** provar de forma leve que o guia enriquece fonte rica e preserva incerteza quando não há localizador de código.  
**Escopo:** dois exemplos curtos de Markdown: M005 e um pedido sem caminho/localizador; revisão independente das saídas.  
**Fora de escopo:** criar/recriar SPECs completas, novos mocks, pipeline, HTML ou brief final; provar generalidade por um fixture.  
**Validação:** V-026-04 e V-026-05.  
**Exit:** evidência leve mostra relações recuperáveis ou descobertas nomeadas, sem detalhe inventado e sem produzir uma nova frente de artefatos.

## T-005 — Preservação de fatos materiais da fonte

**Objetivo:** corrigir a regressão encontrada na run heterogênea: a não invenção não pode apagar entrega, limite, risco/controle, AC/prova ou incremento já explícito no pedido.  
**Escopo:** atualizar guia e papel revisor; regenerar a suíte em Markdown e comparar M-001..M-008 contra a baseline.  
**Fora de escopo:** schema/ledger/score, automação semântica, HTML, renderer ou retoque manual para favorecer um mock.  
**Validação:** V-026-06 e V-026-05.  
**Exit:** M-001, M-004 e M-006 recuperam as relações perdidas sem transformar fatos externos ausentes em invenção; revisão independente julga a suíte melhor ou aponta limitação restante.

**Tasks Ready:** yes — T-005 recebeu `approve` por revisores independentes e foi transicionada para `done`.
