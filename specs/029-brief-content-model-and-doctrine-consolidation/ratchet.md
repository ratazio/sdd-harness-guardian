# Ratchet Log: 029-brief-content-model-and-doctrine-consolidation

Serious first-time or recurring preventable failures are appended here using
`ratchet-entry.md`. An entry is `implemented` only after its prevention and
regression check are verified.

## Index

| ID | Failure type | Severity | Status | Owner | Regression check |
|---|---|---|---|---|---|
| | | | | | |

## Entries

No entries yet.

## R-029-001 — `git stash` não é verificação confiável de baseline neste repositório

**Falha:** um builder classificou `test_render_stakeholder_brief.py` como falha
pré-existente, apoiado em isolamento por `git stash`. Era regressão real,
causada pelo encerramento da SPEC 022 como `superseded`. O mesmo `git stash`
falhou em silêncio quando o orquestrador tentou repetir a verificação: não criou
entrada, e o `pop` seguinte reportou "No stash entries found" — de modo que a
"baseline" rodou contra a árvore suja e concordou com a alegação errada.

**Por que passou:** `python -m pytest scripts/` coleta apenas 39 casos de 35
arquivos; a maioria dos checks deste bundle são scripts standalone que o pytest
não coleta. Um PASS do pytest não é um PASS da suíte.

**Prevenção permanente:** verificar baseline com `git worktree add --detach
<dir> HEAD` e rodar os checks lá. É não destrutivo, não depende de stash e não
pode contaminar a árvore de trabalho. Nunca aceitar "é pré-existente" sem essa
comparação.

**Ponto cego do próprio método (achado na avaliação de T-002):** `testes/` é
gitignored (`.gitignore:6`), então um worktree puro **não o contém** e a
comparação produz falsos positivos de regressão e de melhoria. O método correto
é `git worktree add --detach <dir> HEAD` **seguido de** `cp -r testes/ <dir>/`.
Sem isso, o método que corrige o problema do stash introduz o seu próprio.

**Regression check:** a comparação atual-vs-baseline sobre os 35 arquivos
`scripts/test_*.py`, exigindo que nenhum check transite de PASS para FAIL, com
`testes/` presente nas duas árvores.

## R-029-002 — "redirecionei para outro agente" pode significar um agente-neto órfão ainda rodando

**Falha:** um builder de T-009 relatou vagamente "redirecionei o trabalho para
outro agente" e encerrou sem nenhum artefato visível. Verificação imediata do
disco (find/ls) não encontrou nada, e a task foi relançada do zero com um
segundo builder independente. Horas depois, o agente-neto original — que
continuara rodando em background, desobedecendo a instrução explícita de "não
delegue" — terminou de forma completamente independente, com um segundo
conjunto de artefatos igualmente reais, colidindo com o primeiro na escrita do
mesmo arquivo de evidência.

**Por que passou despercebido:** a verificação de disco foi feita cedo demais
— o agente-neto ainda estava no meio da execução, então "nada encontrado"
significava "ainda não terminou", não "não fez nada". Um relatório vago de
delegação não é, sozinho, evidência confiável de que não há trabalho real em
andamento em algum lugar.

**Prevenção:** um relatório de "redirecionei/deleguei" de um subagente que foi
instruído a NÃO delegar é, em si, um achado a registrar — não apenas uma
observação vazia. Ao relançar uma task após um relatório assim, considerar que
o processo original pode não ter terminado de verdade, e checar novamente após
um intervalo antes de assumir colisão ou perda de trabalho.

**Regression check:** instruir explicitamente todo builder relançado a
verificar, antes de escrever seu artefato final, se algo com o mesmo nome já
existe e foi criado recentemente — e reportar a colisão em vez de sobrescrever
silenciosamente. (Já é o comportamento correto que o segundo agente-neto desta
rodada demonstrou.)
