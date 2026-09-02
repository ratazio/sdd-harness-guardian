# Tasks — SPEC 021

| ID | Status | Title | Dependency | Builder | Evaluator | Evidence |
|---|---|---|---|---|---|---|
| T-001 | done | Definir fontes condicionais e hook semântico orientado por corpus | none | spec021_t001_builder | /root/reevaluate_spec021_t001 | evidence/T-001.md |
| T-002 | done | Integrar disposição semântica na composição de relações materiais | T-001 | spec021_t002_builder | /root/evaluate_spec021_t002 | evidence/T-002.md |
| T-003 | done | Provar limites do contrato determinístico e revisão cross-domain | T-001/T-002 | spec021_t003_builder | /root/evaluate_spec021_t003 | evidence/T-003.md |
| T-004 | done | Regerar M-001–M-008 e repetir sete lentes | T-001–T-003 | /root/execute_spec021_t004 | /root/review_t004_arch_system | evidence/T-004.md |

- **T-001 / AC-021-01/02:** define materialidade condicional, estado vazio e o
  prompt/contrato do hook. O revisor recebe entradas completas, produz decisão
  impossível, locator, impacto, reparo e N/A justificado; V-021-01/02; exit
  exige negativos/positivos e avaliador distinto.
- **T-002 / AC-021-03:** usa a disposição semântica para compor relações de dois
  domínios reais; V-021-03; exit exige revisão distinta sem quota visual,
  taxonomia fixa ou formato obrigatório.
- **T-003 / AC-021-04:** protege integridade de identidade/digest/escopo do
  hook e prova que código não o substitui por score, classificação de domínio
  ou aprovação automática; V-021-04; exit exige bundle e evidence aprovada.
- **T-004 / AC-021-05:** só inicia após `evidence/T-001.md`,
  `evidence/T-002.md` e `evidence/T-003.md` aprovadas independentemente. Cria
  uma raiz nova com M-001–M-008 como oito consumidores novos, registra digests
  de request/fonte/HTML e executa a matriz sete lentes × duas passagens. Todo
  `REVISE` material bloqueia baseline, exige corrigir fontes, rerenderizar e
  repetir ambos os passes antes de qualquer baseline.
