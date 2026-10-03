# Ratchet — 031

**Last updated:** 2026-10-02
**Scope:** prevenção implementada e exercitada; aceite independente D-016.

## R-031-001 — Código verde não prova fidelidade do brief

**Observed failure:** oito modelos minimal foram projetados sem erro, mas
faltaram fatos materiais já disponíveis nos MD.
**Prevention:** a skill de conteúdo parte das fontes/fatos esperados e
corrige o HTML; lacunas reais ficam qualificadas. Schema/contagem de texto
não certifica significado. Aceitação única T-005 usou matriz por domínio.
**Regression:** V-006/V-009/V-013; omissão controlada C001 em T-003 e leitura
dos oito casos em evidence/T-005-source-acceptance.md.
**Status:** enforced — regra/skill implementadas, demonstrações aceitas.

## R-031-002 — Cobertura duplicada, incompleta ou com target parcial

**Observed failure:** coverage duplicado gerava IDs/painel permanente;
inventário de blocos emitidos escondia omissões. Targets coarse também
podiam apontar somente parte do fato composto.
**Prevention:** oito controles/painéis únicos, um painel por vez inclusive
sem JS; coverage dentro da sua aba. Inventariar fatos esperados de todas
as fontes; usar vários alvos quando tópico composto ocupa vários blocos.
**Regression:** V-003/V-004/V-013; 256 seleções nativas e correções pontuais
de M001/M002/M006 com targets completos confirmados.
**Status:** enforced — template/skills exercitados e aceitos, sem score de cards.

## R-031-003 — Provenance pertence ao nó que a declara

**Observed failure:** data-source com vários arquivos unidos por ponto e
vírgula violava BC-005; filhos novos sem data-coverage não completavam a
tríade, mesmo com snapshot/conclusion consistentes.
**Prevention:** locator único por arquivo; várias fontes usam filhos/blocos
próprios. Cada nó com data-source declara também source-section e coverage;
não presumir que herda atributos do pai. Reparo no HTML, sem editar fonte.
**Regression:** V-013/V-015; falhas anteriores preservadas no lab, seis
patches de provenance com texto/CSS/JS/SVG/IDs iguais aos preimages, hashes
finais vinculados aos relatos e oito checks mecânicos PASS. Consistência
mecânica não certifica o significado do locator ou o esforço nativo.
**Status:** enforced — BC-005 e checks existentes exercitados; nenhuma
terceira skill/validação obrigatória criada para futuras gerações.

## Inherited safe baseline practice

Preservado R-029-001: working tree atual não é HEAD. Snapshot dos bytes
locais antes de implementar, sem stash/reset/remoção. Conferência final
preservou23 históricos/72 originais/64 MD copiados/8 estados de produto.
