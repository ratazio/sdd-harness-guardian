# Progress — SPEC 028

**Atualizado em:** 2026-09-02  
**Estado:** concluída; T-001…T-005 têm evidência e avaliação independente.

## Marco atual

O lifecycle resiliente, a casca v3, a composição agêntica e a revisão local HTTP
foram consolidados. A matriz heterogênea expôs conteúdo genérico, cards
repetidos e contaminação entre mocks apesar de herança estrutural válida; cada
caso foi devolvido para recomposição a partir de seu próprio skeleton e fontes.
A regra agora pede leitura agêntica das oito rotas: afirmações editoriais devem
pertencer ao caso, enquanto chrome de navegação/lifecycle pode permanecer
estável. O diagnóstico R2 permanece preservado em `reproduction.md`; não foi
apagado para maquiar a recuperação.

## Próximo passo seguro

Nenhum passo de execução resta nesta iniciativa. O próximo uso do bundle deve
seguir a cadeia consolidada e manter finais de mock em revisão até a aprovação
per-initiative correspondente.

## Trabalho realizado nesta iniciativa

- [x] Instanciar a SPEC 028.
- [x] Registrar objetivo e limites: autoria agêntica, plumbing determinístico.
- [x] Registrar arquitetura de fluxo e reprodução do problema.
- [x] Definir tasks, critérios e revisão HTTP final como proposta.
- [x] Incorporar decisão de resiliência/autonomia: recuperação não espera por
  burocracia, mas preserva a sequência e a autoridade dos gates.
- [x] T-001 — lifecycle resiliente e autoridade de afirmação; avaliação
  independente `APPROVE` registrada em `evidence/T-001.md`.
- [x] T-002 — plano, skeleton e contratos de conteúdo material provados pelo
  piloto M003 R4 e avaliados independentemente.
- [x] T-003 — preview loopback e 64/64 rotas desktop verificados.
- [x] T-004 — revisão renderizada e inventário de validações conectados.
- [x] T-005 — matriz M001–M008 recomposta/revisada sem promoção indevida.

## Riscos abertos

- Futuros projetos ainda precisam de um record próprio de review renderizado
  antes de alegar Human Visibility; a aprovação desta SPEC não concede esse
  gate a nenhum mock.
- M007 mantém labels de proveniência mais visíveis do que o ideal, ressalva
  editorial não bloqueante registrada pela avaliação cruzada.
