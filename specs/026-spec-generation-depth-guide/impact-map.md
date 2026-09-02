# Impact map — SPEC 026

**Status:** draft  
**Overall risk:** low

## Limite da mudança

Muda a orientação de autoria da SPEC e adiciona uma leitura independente antes de `Spec Ready`. Preserva templates, renderer, shell HTML, promoção de brief, automações existentes e liberdade de o compositor escolher a linguagem visual correta para cada domínio.

| Superfície | Alteração esperada | Direta/indireta | Risco | Fonte/evidência |
|---|---|---|---|---|
| Skills/instruções | nova skill curta e referência | direta | low | FR-026-01..05 |
| Papéis de revisão | novo `spec-depth-reviewer` | direta | low | FR-026-06..08 |
| Artefatos de iniciativa | maior completude em Markdown existente | indireta | low | O-026-01..02 |
| Template/renderer/HTML | `not_applicable — preservado` | indireta | low | NG-026-03 |
| Runtime, API, dados, segurança, deploy | `not_applicable — nenhum componente novo` | indireta | low | NG-026-01 |

## Fluxo

```text
pedido / fontes acessíveis → autor → Markdown canônico → revisor distinto → gate existente → compositor agêntico
```

## Riscos e controles

| ID | Evento | Controle | Contingência | Validação |
|---|---|---|---|---|
| IR-026-01 | guia adiciona burocracia sem decisão | perguntas condicionais, sem quotas | simplificar guia com achado de calibração | V-026-01 |
| IR-026-02 | caminho ou arquitetura inventados | tipo de fonte + regra contra busca semântica sem localizador | `REVISE` e descoberta nomeada | V-026-02 |
| IR-026-03 | revisor apenas confirma | formato obrigatório de achado acionável | revisão humana/escalonamento | V-026-03 |

**Impact mapped:** yes — confirmado pelo [parecer independente](./evidence/spec-depth-review.md).  
**Human review required:** no para criar a orientação; sim antes de autorizar tarefas de implementação.
