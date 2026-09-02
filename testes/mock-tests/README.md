# Biblioteca de mocks para geração de SPECs

Estes arquivos são pedidos funcionais de teste, não SPECs e não instruções para alterar o produto Guardian. Eles exercitam a criação de pacotes de planejamento v2 e stakeholder briefs em domínios, arquiteturas e perfis de risco distintos.

## Casos disponíveis

| ID | Arquivo | Foco primário |
| --- | --- | --- |
| M-001 | `../spec-mock-test.md` | Aplicação web full-stack com autenticação e publicação |
| M-002 | `02-backend-reconciliation-api.md` | Backend transacional e integrações assíncronas |
| M-003 | `03-mobile-offline-field-inspections.md` | Aplicativo mobile offline-first |
| M-004 | `04-react-native-multiplatform-learning.md` | React Native para mobile e web, com módulos nativos |
| M-005 | `05-local-ai-exam-scoring.md` | Modelo local de IA, APIs e dados pessoais de avaliações |
| M-006 | `06-agentic-financial-document-reports.md` | Agentes/skills locais, documentos e infraestrutura Docker |
| M-007 | `07-accessible-public-kiosk.md` | Quiosque público, acessibilidade e operação sem rede |
| M-008 | `08-event-driven-inventory-recovery.md` | Eventos, consistência eventual e recuperação operacional |

## Uso

Execute cada mock em uma raiz consumidora descartável, mantendo o bundle Guardian fonte intacto. A skill global `guardian-stakeholder-brief-mock-lab` descobre este índice e aplica esse isolamento automaticamente. Um resultado só é comparável quando registra validações determinísticas, revisão humana/independente e a classificação de qualquer falha.

Os fatos de cada mock podem ser inventados apenas quando o próprio arquivo o autorizar. Não transforme uma limitação de um caso em regra universal do Guardian.
