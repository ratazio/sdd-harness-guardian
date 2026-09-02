---
name: spec-depth-authoring
description: Use ao redigir ou aprofundar uma SPEC antes de Spec Ready, para preservar decisões, limites de fonte, descobertas e destinos Markdown canônicos.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Autoria aprofundada de SPEC

## Quando usar

- Ao criar ou aprofundar uma SPEC antes de `Spec Ready`.
- Quando o pedido contém relações de produto, técnicas ou operacionais que não
  podem se perder entre o pedido, a SPEC e o plano.

## Procedimento

1. Separe cada informação em: **fato pedido**, **fato inspecionado** (com
   fonte/localizador), **inferência limitada** (e seu motivo) ou **descoberta**
   (lacuna, dono e caminho de resolução). Não apresente inferência ou ausência
   como fato.
2. Antes de abrir discoveries, faça uma passada qualitativa curta do pedido:
   todo fato ou relação material explicitamente fornecido deve continuar
   recuperável no Markdown canônico adequado. Preserve, quando já constarem da
   fonte, por exemplo: resultado e limite; risco com controle, owner ou
   contingência; AC com método, oráculo ou evidência; e task com escopo,
   anti-escopo, dependência ou exit. Não reduza uma entrega explícita a
   `futuro` nem a remova — por exemplo, HTML/PDF pedido continua uma entrega,
   ainda que seu formato técnico dependa de decisão posterior.
   Quando o pedido exigir definir, aplicar ou validar um controle ou uma
   entrega sem informar valor ou mecanismo, preserve a obrigação e sua prova
   canônica; abra discovery somente para o valor, método ou fonte ausente.
   Uma paráfrase ampla não substitui o controle específico: requisitos de
   criptografia, horários ou retenção, por exemplo, permanecem identificáveis.
3. Pergunte somente quando aplicável: qual resultado e porquê; quais atores;
   qual contexto e impacto arquitetural; quais superfícies mudam, permanecem ou
   ficam fora de escopo; quais dados/contratos; quais falhas e recuperação;
   quais impactos/riscos; quais incrementos de task; qual validação, evidência
   e critério de aceite; e quais incertezas têm dono. Ausência proporcional é
   `not_applicable` com razão ou uma descoberta nomeada, nunca preenchimento.
   Abra uma descoberta somente para o detalhe realmente ausente; ela não
   substitui nem retira fato, relação ou entrega já explícita no pedido.
4. Se um caminho de código ou teste foi fornecido explicitamente, ou está
   inequivocamente indicado por uma instrução/localizador acessível, inspecione
   somente o necessário e registre caminho, observação, mudança/teste relevante
   e limite. Se há apenas uma raiz ambígua, não faça busca semântica para eleger
   pasta, teste ou arquitetura: registre o limite e, se bloquear decisão,
   abra descoberta com dono. Se a fonte contradiz o pedido, preserve ambos e a
   decisão pendente.
5. Mapeie proporcionalmente cada relação material do pedido: intenção, outcome,
   escopo e obrigação em `spec.md`; superfícies, riscos e controles em
   `impact-map.md`; incrementos, dependências, aplicação e exit em `tasks.md`;
   e critérios, método, oráculo e evidência em `validation-plan.md`. Registre
   estratégia, limites, rollback e o material de construção do brief em
   `plan.md`; contradições, decisões e donos em `decision-log.md`.
6. Mantenha `run-state.yaml`, `progress.md` e `handoffs/latest-handoff.md`
   coerentes com o checkpoint. Peça revisão independente antes de declarar a
   SPEC pronta.

## Limites

- Não use quota, score, contagem, JSON ou Python como critério de profundidade.
- Não gere conteúdo, HTML, diagramas ou estrutura técnica sem fonte.
- Não transforme perguntas condicionais em checklist mecânico: preserve a
  decisão material e a incerteza honesta.
