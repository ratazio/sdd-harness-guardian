# M-006 — Relatórios financeiros a partir de documentos locais

## Pedido funcional

Criar a SPEC para uma plataforma interna que recebe planilhas Excel, PDFs e documentos Word de uma empresa, extrai dados financeiros, executa uma cadeia local de skills/agentes para classificar receitas, despesas e anomalias, e gera um relatório financeiro em HTML e PDF. Usuários enviam arquivos, acompanham o processamento e baixam o resultado; não existe integração externa nem uso de LLM hospedado.

Stack fixa: Python 3.12, FastAPI, workers Celery, Redis, PostgreSQL, armazenamento de arquivos compatível com S3 local (MinIO), OCR local, bibliotecas de leitura de XLSX/PDF/DOCX, motor de modelo local e Docker Compose. A produção deverá ser implantável em containers, com serviços separados para API, worker, modelo e armazenamento.

## Limites e decisões obrigatórias

- Arquivos entram em quarentena, são verificados contra malware e têm tipo/limite de tamanho validados antes de qualquer parser; macros e links externos não são executados.
- Definir cadeia de custódia: hash, origem, versão do extrator/modelo, artefatos intermediários, retenção e exclusão segura.
- O agente pode propor classificação, mas totais, regras contábeis e cálculos devem ser determinísticos e auditáveis; exceções seguem para revisão humana.
- Descrever isolamento entre jobs, limites de recursos, cancelamento, retry, DLQ, observabilidade sem conteúdo financeiro e escalabilidade em containers.
- Não incluir conexão bancária, recomendação de investimento, assinatura digital, compartilhamento externo ou automação de lançamento contábil.

## O que a SPEC e o brief devem demonstrar

O pacote deve detalhar pipeline de ingestão → quarentena → extração → agentes/validação → relatório, contratos de status/download e um desenho Docker legível. Deve distinguir claramente oráculos determinísticos de avaliação probabilística do agente.
