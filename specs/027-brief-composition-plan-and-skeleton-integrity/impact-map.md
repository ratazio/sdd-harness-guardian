# Impact map — SPEC 027

**Status:** reviewed  
**Overall risk:** medium / A2-elevated

## Limite da mudança

Esta iniciativa fecha a lacuna entre o plano de composição, o skeleton e o
candidate. Preserva fontes Markdown, conteúdo agêntico, identidade
vendor-neutral padrão, renderer como promotor e gates de Human Visibility/
Tasks Ready.

| Superfície | Alteração | Risco | Limite preservado |
|---|---|---|---|
| `plan.md` e template de orientação | scaffold de composição e revisão | medium | não cria fonte paralela |
| Skeleton/template v3 | marcadores de casca e slots | medium | sem redesenho de marca |
| Hook de herança | rejeita substituição de casca | medium | não interpreta Markdown ou estética |
| Skills/reviewer/workflow | plano e inspeção visual distintos | medium | julgamento segue humano/agêntico |
| Renderer/promoção | consome candidate exato revisado | low | não compõe HTML |
| Runtime/API/dados/deploy | `not_applicable` | low | nenhum componente operacional novo |

## Fluxo e fronteiras

```text
fontes canônicas → autor do plano em plan.md → reviewer distinto
→ skeleton local imutável + slots → compositor agêntico → hook estreito
→ revisão desktop distinta → renderer promotor → brief final
```

## Riscos e controles

| ID | Evento | Controle | Contingência/owner | Validação |
|---|---|---|---|---|
| IR-027-01 | Candidate refeito do zero declara hash copiado. | regiões imutáveis/slots + hook de preservação. | `REVISE`; compositor recompõe da cópia. | V-027-04 |
| IR-027-02 | Plano raso omite uma relação ou subpágina. | scaffold + revisor distinto antes do skeleton. | corrigir `plan.md`, fontes quando necessário. | V-027-02 |
| IR-027-03 | Regra mecânica impede domínio incomum. | N/A/discovery proporcional e revisão qualitativa. | decisão humana se materialidade for incerta. | V-027-01 |
| IR-027-04 | HTML atende hook mas falha visualmente/navegação. | inspeção desktop distinta. | candidate permanece não promovido. | V-027-05 |

## Unknowns

| ID | Unknown | Impacto | Dono/resolução | Bloqueia implementação? |
|---|---|---|---|---|
| U-027-01 | Melhor granularidade do fingerprint sem quebrar extensões legítimas. | Define o limite do hook. | T-002, fixtures positivas/negativas. | sim |
| U-027-02 | Como registrar extensão visual excepcional sem permitir shell paralelo. | Mantém flexibilidade fonte-apoiada. | T-001/T-002, revisão distinta. | sim |

## Decisão de impacto

**Impact mapped:** yes — confirmado por [revisão independente](./evidence/spec-depth-review.md).  
**Human review required:** não para o desenho da SPEC; sim para autorizar tasks depois dos gates.  
**Condição:** não misturar o hook de integridade com avaliação estética.
