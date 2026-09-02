# Plano técnico — SPEC 026

**Status:** draft  
**Spec:** [spec.md](./spec.md)  
**Impact map:** [impact-map.md](./impact-map.md)  
**Validation plan:** [validation-plan.md](./validation-plan.md)  
**Tamanho:** S — orientação e revisão sobre artefatos existentes; nenhuma mudança de runtime.

## 1. Estratégia mínima

1. Criar uma única skill/guia curta para o agente autor, organizada por perguntas condicionais e destino Markdown canônico.
2. Referenciá-la no ponto de autoria já existente, sem acrescentar lógica semântica ao scaffolder ou ao renderer.
3. Criar o papel/prompt de `spec-depth-reviewer`, separado do autor, para comparar pedido → SPEC → plano e registrar `PASS` ou `REVISE`.
4. Calibrar contra o M005 e contra um pedido sem raiz de projeto, verificando profundidade útil e ausência honesta.
5. Acrescentar uma passada qualitativa de preservação: fatos e relações materiais já fornecidos devem chegar aos artefatos correspondentes; discoveries representam apenas o que a fonte não estabelece.

O menor caminho é documentação operacional + revisão independente. Um parser, schema de conteúdo, score, gerador de Markdown/HTML ou nova etapa automatizada foi rejeitado: ele não consegue decidir o significado de uma SPEC arbitrária e repetiria o defeito observado.

## 2. Limite arquitetural

```text
pedido + fontes explicitamente acessíveis
                 │
                 ▼
        agente autor da SPEC
                 │  fatos, relações, limites e descobertas
                 ▼
     SPEC + impact-map + plan + validation-plan
                 │
                 ▼
   spec-depth-reviewer (identidade distinta)
           │ PASS / REVISE acionável
           ▼
 gates existentes → composição agêntica do brief → HTML
```

| Superfície | Mudança | Preservado |
|---|---|---|
| Instrução de autoria | nova skill/guia curta e sua referência | liberdade de julgamento do agente |
| Revisão de SPEC | novo papel qualitativo antes de `Spec Ready` | Spec Guardian, gates e evidências existentes |
| Markdown canônico | preenchimento mais profundo dos artefatos existentes | uma única fonte de verdade |
| Renderer/template/HTML | nenhuma alteração nesta SPEC | composição final por agente, não por script |

## 3. Registro de construção do brief

O guia não determina diagramas ou cards. Ele exige que o autor forneça no `plan.md` material de decisão para cada rota aplicável, para que o compositor humano/agêntico escolha a forma correta:

| Rota | Pergunta executiva a preservar | Material mínimo quando aplicável | Forma decidida depois pelo compositor |
|---|---|---|---|
| Valor e escopo | Que resultado importa e qual limite protege a decisão? | outcome, atores, porquê, anti-escopo, incerteza | narrativa, cards, comparação |
| Arquitetura | Onde a mudança ocorre, o que preserva e por quê? | contexto, componentes/limites, fluxos, contratos, alteração e não alteração | topologia, zoom, sequência ou ausência justificada |
| Impacto | Quem/superfície é afetado e qual controle reduz exposição? | delta, dono, risco, controle, rollback | mapa, matriz, dossiê |
| Execução | Que incrementos compõem a entrega e por que são a sequência segura? | tasks, escopo/anti-escopo, dependência, risco, evidência, exit | épicos quando existentes e dossiês de task |
| Validação | O que será provado, por qual método e qual limite permanece? | AC, método, contexto, oráculo, evidência, owner, limitação | pilares e dossiês de prova |
| Evolução/decisão/cobertura | Qual decisão está pendente, quem decide e de onde vem cada fato? | gate, autoridade, consequência, fonte e descoberta | timeline, decision log, matriz |

Uma resposta ausente só é aceitável como `not_applicable` com razão ou descoberta nomeada/dono. Ela não autoriza o autor a fabricar componente, caminho, teste ou diagrama.

Antes dessa decisão de ausência, o autor faz uma leitura de preservação da fonte: se o pedido já declara uma entrega, limite, risco/controle, AC, prova ou incremento, ele deve continuar recuperável no artefato canônico pertinente. Isso não cria ledger, quota ou segunda fonte de verdade; é uma verificação semântica curta do autor e do revisor. Uma discovery pode explicar o contrato, caminho ou valor que falta, mas não substituir o resultado já declarado.

Se o pedido disser “definir retenção”, “usar criptografia”, “consultar horários” ou equivalente, preserve a obrigação observável e sua prova; a discovery pode guardar o prazo, algoritmo, origem ou outra escolha que não foi fornecida. Uma paráfrase genérica — por exemplo, “estado protegido” para um pedido de criptografia — não recupera o controle material.

## 4. Regra de inspeção de código

| Situação | Conduta do autor |
|---|---|
| Caminho relevante está explicitamente fornecido ou inequivocamente indicado por um localizador/instrução acessível | Inspecionar o mínimo necessário; registrar caminho, observação e limite. |
| Só existe raiz, sem caminho/localizador inequívoco | Não fazer busca semântica para eleger pasta, teste ou arquitetura; registrar limite e descoberta/dono se a ausência bloquear decisão. |
| Pedido não fornece raiz/código acessível | Confiar no pedido, declarar a limitação e nunca inventar localização. |
| Fonte contradiz pedido | Registrar ambas, impacto da contradição e decisão/owner necessários. |

## 5. Sequência de mudança

| Passo | Resultado | Pré-condição | Reversível |
|---|---|---|---|
| 1 | Guia de autoria | SPEC aprovada | Sim; documento isolado |
| 2 | Referência no fluxo existente | guia revisado | Sim |
| 3 | Papel/prompt revisor | guia e decisão de gate claros | Sim |
| 4 | Calibração Markdown mínima e evidência | autor e revisor distintos | Sim |
| 5 | Regressão de preservação de fonte em M-001, M-004 e M-006 | guia e revisor corrigidos | Sim |

## 6. Não há alteração de contratos operacionais

- API, banco, autenticação, deploy e telemetria: `not_applicable — orientação local do bundle`.
- Rollback: reverter os documentos/referências desta iniciativa; não há migração de dados nem artefato de execução.

## 7. Questões abertas

| ID | Questão | Dono | Bloqueia |
|---|---|---|---|
| Q-026-01 | Onde a skill curta será referenciada de forma mais natural no fluxo de autoria existente? | Builder T-002 | Plan Ready, não Spec Ready |
| Q-026-02 | Qual pedido sem raiz de projeto representa melhor a calibração mínima? | Builder T-004 | Validation Ready, não Spec Ready |

## 8. Decisão de plano

**Plan Ready:** yes  
**Reviewer:** `spec-depth-reviewer`  
**Reviewed at:** 2026-09-01  
**Condição atendida:** [revisão independente](./evidence/spec-depth-review.md) confirmou guia + revisor, sem automação semântica, busca especulativa ou calibração expansiva.
