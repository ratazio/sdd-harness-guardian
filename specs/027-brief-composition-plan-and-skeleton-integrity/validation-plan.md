# Plano de validação — SPEC 027

**Status:** validation_ready  
**Assurance:** A2-elevated por alterar contrato de promoção visual, sem runtime.

## Estratégia

Separar o que é verificável de forma determinística daquilo que exige revisão editorial: o hook prova preservação do skeleton; o revisor prova que a experiência representa o plano/fonte e navega como subpáginas. Nenhum lado substitui o outro.

| ID | AC | Método/oráculo | Resultado esperado | Evidência |
|---|---|---|---|---|
| V-027-01 | AC-027-01 | leitura de template + plano de casos distintos | scaffold contém tese, rotas, relações, forma, repetição, limite e fechamento; N/A honesto aceito | evidence/T-001.md |
| V-027-02 | AC-027-02 | reviewer distinto usa plano raso e plano material | \`REVISE\` identifica perda e correção; \`PASS\` não depende de volume | evidence/T-001.md |
| V-027-03 | AC-027-03 | fixture de skeleton e inspeção de marcadores | shell/slots/extensão delimitados e preservam perfil/fallback | evidence/T-002.md |
| V-027-04 | AC-027-04 | fixtures positiva e negativa do guard | página paralela com hash/IDs falha; cópia in-situ passa | evidence/T-002.md |
| V-027-05 | AC-027-05 | revisor distinto + inspeção desktop/navegação | pode reprovar HTML cru, rota longa ou perda de história com hook verde | evidence/T-004.md |
| V-027-06 | AC-027-06 | nova run de mocks heterogêneos | candidates não promovidos seguem o mesmo contrato sem regra específica | evidence/T-003.md |
| V-027-07 | AC-027-07 | \`validate_bundle.py\`, \`git diff --check\`, leitura de diff | não há gerador semântico/HTML nem regressão de contratos | evidence/T-004.md |

## Falhas e contenção

| Falha | Oráculo | Ação |
|---|---|---|
| Guard aceita shell paralelo | fixture negativa | bloquear T-002 e corrigir fingerprint/slots |
| Plano rico em cobertura, pobre em decisão | reviewer | \`REVISE\` no \`plan.md\`; não instanciar skeleton |
| Candidate visualmente fraco com guard verde | revisão desktop | não promover; recompor dentro do skeleton |
| Regra específica de mock aparece | diff/review | rejeitar T-003 e generalizar/remover a regra |

## Decisão de validação

**Validation Ready:** yes — [revisão independente](./evidence/spec-depth-review.md) confirmou cobertura proporcional dos ACs.  
**Comandos previstos:** \`python scripts/validate_bundle.py\`, guard de candidate e checks de fixtures; nenhum comando gera conteúdo.
