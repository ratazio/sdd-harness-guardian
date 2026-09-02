# Handoff — SPEC 027

## Checkpoint

T-001 implementou o scaffold de construção em `plan.md` e a revisão distinta
pré-skeleton, e foi aprovada por evaluator independente. As evidências são
`evidence/T-001.md` e `evidence/evaluation-T-001.md`; a task está `done`.
Nenhum skeleton, HTML, renderer, guard ou mock foi alterado por T-001.

T-002 implementou o contrato de casca/slots no template e o guard de herança
material. A avaliação independente aprovou a cópia in-situ e a rejeição da
casca paralela; evidências em `evidence/T-002.md` e
`evidence/evaluation-T-002.md`. T-003/T-004 também foram concluídas pela
auditoria R2 completa; evidência em `evidence/evaluation-T-003-T-004.md`.

## Why this SPEC exists

R3 candidates proved semantic source coverage but exposed two distinct gaps: the plan could be only a coverage paragraph, and a candidate could declare a skeleton hash while replacing the visual shell. This SPEC addresses both without making composition deterministic or mock-specific.

## Required next action

Não há ação pendente nesta SPEC. Manter R2 como regressão não promovida; o
browser não suportou `file://`, portanto uma futura revisão live deve ocorrer
somente se um runtime apropriado estiver disponível. As observações MA-001..003
não autorizam alteração adicional sem nova SPEC.
