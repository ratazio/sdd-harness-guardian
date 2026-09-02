# M-005 — Correção local assistida por modelo de IA

## Pedido funcional

Criar a SPEC de um serviço de correção de provas discursivas. Uma API parceira envia lote de respostas realizadas, identificador do candidato, identificador da prova, rubrica e idioma. O serviço valida o lote, encaminha somente os dados necessários a um modelo de IA executado localmente em infraestrutura isolada, recebe uma nota e justificativa estruturada, aplica regras determinísticas de faixa e persistência e publica o resultado por outra API. A API de destino grava a nota associada ao candidato em MySQL; este projeto não acessa o banco diretamente.

Stack fixa: Python 3.12, FastAPI, worker assíncrono, PostgreSQL para estado operacional, Redis para fila, cliente HTTP para a API de destino, execução local do modelo por servidor interno compatível com OpenAI e Docker Compose para desenvolvimento. Não pode haver hotlink, chamada a modelo externo, telemetria que exporte respostas, nem treinamento com os dados recebidos.

## Limites e decisões obrigatórias

- Dados de candidato e respostas são pessoais/sensíveis no contexto educacional: definir minimização, pseudonimização para o modelo quando viável, criptografia, retenção, acesso, auditoria e mascaramento de logs.
- A nota do modelo é uma sugestão rastreável, não uma decisão incontestável: exigir versão do modelo/rubrica/prompt, confiança, regra de bloqueio para revisão humana e mecanismo de reprocessamento.
- Contratos precisam cobrir lote inválido, resposta ambígua, indisponibilidade/timeout do modelo local, resposta fora da rubrica, publicação idempotente, falha da API de destino e reenvio.
- Separar controles determinísticos das avaliações probabilísticas do modelo; não alegar precisão, ausência de viés ou conformidade sem método de medição.
- Incluir testes de contratos e dados sintéticos, testes de invariantes de nota, simulação do modelo e avaliação independente de privacidade, segurança e explicabilidade.

## O que a SPEC e o brief devem demonstrar

O stakeholder brief deve exibir fluxos e fronteiras API origem → serviço → modelo local → API destino/MySQL, além de responsabilidade humana e sinais de qualidade do modelo. Tasks devem preservar que a integração final é via API, não uma conexão direta ao MySQL.
