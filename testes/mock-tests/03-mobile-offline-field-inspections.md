# M-003 — Inspeções de campo offline-first

## Pedido funcional

Criar a SPEC de um aplicativo mobile para técnicos realizarem inspeções de segurança em equipamentos industriais mesmo sem conexão. O técnico baixa uma lista atribuída de locais e checklists, preenche respostas, fotos e assinatura, registra coordenada aproximada e envia tudo quando a conectividade voltar. Supervisores usam uma API web existente para atribuir inspeções e acompanhar pendências; este projeto entrega apenas o aplicativo e sua integração contratual.

Stack fixa: Kotlin, Jetpack Compose, Room/SQLite criptografado, WorkManager, câmera do dispositivo, Android 10+ e API REST JSON existente. A autenticação é OAuth 2.1 com PKCE e tokens no armazenamento seguro do sistema. Fotos são comprimidas no aparelho e enviadas em partes para um serviço de mídia já existente.

## Limites e decisões obrigatórias

- Explicitar máquina de estados da inspeção e da sincronização: baixada, em edição, pronta, enviando, conflito, enviada e falha recuperável.
- Definir como o app resolve atualização concorrente do checklist, expiração de token sem rede, falha de upload parcial, remoção de atribuição e troca de aparelho.
- A localização é aproximada, coletada somente durante a inspeção e removida conforme período de retenção definido; não há rastreamento em segundo plano.
- Cobrir acessibilidade Android, leitor de tela, alvo de toque, contraste, orientação, fonte ampliada, permissões e comportamento em aparelho de baixo armazenamento.
- Incluir uma estratégia de testes para lógica de sincronização, banco local, UI acessível, integração de API simulada e fluxo em dispositivo/emulador.

## O que a SPEC e o brief devem demonstrar

O brief deve projetar claramente sincronização offline, fronteiras de dados do dispositivo, decisões de conflito e cenários de recuperação, sem inventar um backend novo. As tasks precisam ser incrementais e verificáveis, sem implementar o aplicativo.
