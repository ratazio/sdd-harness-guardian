# Plano técnico — SPEC 027

**Status:** plan_ready  
**Tamanho:** M — altera contrato reutilizável de composição, sem runtime novo.  
**Perfil visual:** vendor-neutral; identidade Pearson fica fora desta iniciativa.

## 1. Estratégia mínima

1. Acrescentar ao `plan.md` já canônico um scaffold conciso de construção do
   brief; ele orienta decisão e forma, mas não vira sidecar.
2. Fazer o revisor distinto julgar esse plano contra as fontes antes da criação
   do skeleton.
3. Marcar no template v3 a casca preservada e os slots onde o compositor pode
   escrever conteúdo/visuais.
4. Fortalecer o guard para comprovar cópia preservada, não só hash, classes e
   oito IDs.
5. Manter a composição final inteiramente agêntica, seguida por revisão
   desktop distinta e promoção dos bytes exatos.

Parser de Markdown, score, regras de quantidade e gerador de HTML foram
rejeitados: não decidem a forma de uma SPEC arbitrária e repetiriam a perda de
contexto que esta iniciativa corrige.

## 2. Arquitetura da mudança

```text
                 fontes Markdown canônicas
                            │
                            ▼
     plan.md: cobertura + plano de composição revisado
                            │ PASS / REVISE distinto
                            ▼
template v3 ──cópia──► skeleton local (casca + slots)
                            │ cópia física
                            ▼
       candidate agêntico (conteúdo dentro dos slots)
                            │ hook: integridade, não semântica
                            ▼
 revisão desktop: fontes + plano + navegação + narrativa
                            │ candidate SHA-256 exato
                            ▼
                  renderer/promotor existente
```

| Superfície | Muda | Preservada |
|---|---|---|
| Plano | scaffold e revisão de construção | Markdown continua autoridade |
| Template/skeleton | limites explícitos de mutabilidade | oito rotas, fallback, perfil atual |
| Guard | fingerprint de shell/slots | não gera nem avalia conteúdo |
| Compositor | preenchimento *in situ* | autonomia de texto/diagrama fonte-apoiado |
| Renderer | assinatura de candidate exato | não redesenha nem resolve lacunas |

## 3. Scaffold canônico no `plan.md`

O template acrescentará esta seção à cobertura existente, sem criar
`brief-plan.md`, manifesto JSON ou ledger paralelo.

### 3.1 Tese e visão global

| Campo | Registro esperado |
|---|---|
| Decisão/audiência | Qual decisão ou entendimento o brief habilita e para quem. |
| Tese | Resultado, limite e próxima decisão em linguagem humana. |
| Perfil/limite visual | vendor-neutral por padrão; perfil/exceção somente se fonte o selecionar. |
| Relações globais | Relações que exigem visão transversal, e por quê. |

### 3.2 Registro por rota e componente material

| Rota / componente | Questão executiva e arco | Fonte + relação recuperável | Forma escolhida e motivo | Campos de repetição/slot | Limite/discovery | Fechamento/ação |
|---|---|---|---|---|---|---|
| `scope` | orientação → valor → limite → decisão | outcome/atores/anti-escopo | narrativa, comparação ou outra forma | fatos aplicáveis | | próxima decisão |
| `architecture.global` | contexto → mudança/preservação → trade-off → ação | responsabilidades/fronteiras/fluxo quando materiais | topologia, sequência, matriz ou N/A motivado | zooms só quando fonte os apoia | | decisão arquitetural |
| `impact.<id>` | delta → exposição → controle → ação | superfície, owner, risco/controle | footprint, cadeia, dossiê etc. | delta/owner/exposição/controle | | checkpoint |
| `execution.task.<id>` | incremento → dependência → prova → saída | contrato completo de task | dossiê de task | outcome, escopo, anti-escopo, dependência, risco, prova, exit, autoridade | | por que agora |
| `validation.proof.<id>` | claim → método → oráculo → limite → gate | AC/prova | dossiê/matriz/fluxo | elemento, contexto, método, oráculo, evidência, owner, aceite | | gate |
| `evolution`, `decision`, `coverage` | estado → consequência → próximo passo | decisão/gate/proveniência | timeline, painel, registro | campos fonte-apoiados | | ação segura |

O revisor não exige todas as formas nem mede volume. Exige que cada relação
material tenha destino inteligível ou ausência/discovery fonte-apoiada.

## 4. Contrato de integridade do skeleton

O template delimitará, por atributos semânticos, três regiões:

| Região | Regra |
|---|---|
| Shell imutável | `<head>`, stylesheet-base marcado, outer shell, nav/rotas, fallback, hooks de identidade/lifecycle e comportamento-base permanecem estruturalmente idênticos. |
| Slot composável | Região marcada onde o agente acrescenta/edita narrativa, cards, diagramas SVG/HTML, tabelas e estilos locais necessários. |
| Extensão autorizada | Elemento explicitamente marcado e documentado para uma forma fonte-apoiada não prevista; não pode substituir shell nem ocultar fallback. |

O hook compara o candidate ao skeleton local e falha por ausência, alteração ou
troca da região imutável. Ele aceita variação dentro de slots e extensão
permitida. Um digest de base declarado jamais é prova suficiente sozinho.

## 5. Sequência de implementação

| Passo | Dono | Resultado | Validação |
|---|---|---|---|
| 1 | Builder | scaffold + instrução/revisor de plano | V-027-01/02 |
| 2 | Builder | template/skeleton marcado e hook fortalecido | V-027-03/04 |
| 3 | Compositor distinto | candidates heterogêneos derivados por cópia | V-027-06 |
| 4 | Revisor distinto | parecer visual/desktop e achados acionáveis | V-027-05 |
| 5 | Evaluator | evidência, regressão e manutenção do bundle | V-027-07 |

## 6. Rollback e compatibilidade

- Templates/skills/hooks são versionados e reversíveis por commit; não há
  migração de dados.
- Briefs históricos e candidates existentes não são reescritos.
- Skeleton já existente sem marcadores segue o contrato histórico até refresh
  material; novos skeletons usam a nova versão.
- Falha de hook bloqueia candidate/promoção e retorna ao compositor; não há
  fallback para geração paralela.

## 7. Questões abertas

| ID | Questão | Dono | Bloqueia |
|---|---|---|---|
| Q-027-01 | O fingerprint usará serialização DOM canônica, regiões identificadas ou ambos? | T-002 | implementação, não Spec Ready |
| Q-027-02 | Quais extensões visuais são necessárias no skeleton sem abrir fuga de shell? | T-001/T-002 + reviewer | implementação, não Spec Ready |

## 8. Decisão de plano

**Plan Ready:** yes — [revisão independente](./evidence/spec-depth-review.md) confirmou a separação entre integridade verificável e composição agêntica.  
**Limite explícito:** conteúdo final continua uma decisão agêntica, nunca do hook.
