# M-007 — Quiosque público de orientação acessível

## Pedido funcional

Criar a SPEC de um quiosque touchscreen em biblioteca pública que permite localizar livros por título/autor, ver o mapa da estante, consultar horários e imprimir um comprovante curto de rota. Não há login, coleta de perfil ou analytics individual. O equipamento pode ficar temporariamente sem rede e deve apresentar conteúdo essencial em cache local.

Stack sugerida: aplicação web estática em modo quiosque, TypeScript, cache local versionado, API pública de catálogo já existente, CSS sem dependência de framework pesado e impressão pelo navegador. O equipamento tem touchscreen, teclado físico opcional e leitor de tela do sistema.

## Limites e decisões obrigatórias

- A acessibilidade é requisito funcional central: navegação de teclado, foco visível, alto contraste, alvo de toque, fonte ampliável, leitor de tela, redução de movimento, idioma claro e equivalente textual para mapas/diagramas.
- Não usar `role="img"` na âncora de logo, autoplay, dependência de hover, captura de localização, câmera, conta de usuário, pagamento ou conteúdo publicitário.
- Definir estados sem rede, API indisponível, impressora sem papel, consulta sem resultado, reinício automático de sessão e limpeza de qualquer texto digitado.
- Cobrir desktop de manutenção, viewport de quiosque e impressão, incluindo uso sem JavaScript quando aplicável ao conteúdo informativo.

## O que a SPEC e o brief devem demonstrar

O resultado deve transformar os critérios de acessibilidade em ACs e tarefas verificáveis, não em uma frase genérica. O brief deve mostrar jornada de busca e contingências de operação pública sem exigir backend novo.
