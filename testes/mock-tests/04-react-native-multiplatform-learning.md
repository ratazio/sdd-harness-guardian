# M-004 — Acompanhamento de aprendizagem multiplataforma

## Pedido funcional

Criar a SPEC para um produto de acompanhamento de aprendizagem que deve funcionar como aplicativo iOS/Android e como aplicação web responsiva para estudantes e responsáveis. O mesmo domínio permite ver plano semanal, marcar atividades concluídas, consultar progresso e receber lembretes locais. Professores continuam usando um portal separado e já existente. Dados vêm de uma API GraphQL existente, que suporta consultas e mutações de progresso.

Stack fixa: React Native, Expo com prebuild, TypeScript, React Navigation, React Native Web, TanStack Query, armazenamento seguro para sessão, SQLite local para cache e um monorepo com pacote compartilhado de domínio. Há módulos nativos para notificações e armazenamento seguro; a versão web não pode carregar código nativo incompatível.

## Limites e decisões obrigatórias

- Delimitar o que é realmente compartilhado entre plataformas e o que exige adaptadores por plataforma, incluindo notificações, deep links, autenticação e armazenamento.
- Definir comportamento do cache, modo offline de leitura, mutações pendentes, invalidação e conflito quando aluno/responsável atualizam progresso em aparelhos diferentes.
- Descrever acessibilidade nas três superfícies, suporte a teclado/web, leitores de tela e diferenças de navegação.
- Não incluir chat, vídeo, pagamentos, criação de conteúdo, analytics comportamental ou portal de professores.
- Projetar CI que execute testes do domínio compartilhado, componentes, contrato GraphQL e smoke tests web/mobile sem depender de loja de aplicativos.

## O que a SPEC e o brief devem demonstrar

O resultado deve tornar visíveis as fronteiras mobile/web, a arquitetura do monorepo, contratos GraphQL e riscos de paridade entre plataformas. Evitar pressupor que React Native automaticamente resolve todas as diferenças de runtime.
