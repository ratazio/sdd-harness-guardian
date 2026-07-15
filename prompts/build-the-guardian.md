# Prompt para construir o SDD Harness Guardian

Copie e rode este prompt na raiz do repositório `sdd-harness-guardian`.

```txt
Você está dentro do repositório `sdd-harness-guardian`.

Objetivo:
Construir e completar um bundle agêntico versionado em Git para governança de Spec Driven Development dentro de um Harness Engineering system.

Antes de editar qualquer coisa:
1. Leia `README.md`.
2. Leia `manifest.yaml`.
3. Leia `.harness/AGENTS.md`.
4. Leia todos os arquivos em `.harness/rules/`.
5. Leia todos os arquivos em `.harness/workflows/`.
6. Leia todos os arquivos em `.harness/agents/`.
7. Leia todos os arquivos em `.harness/skills/`.
8. Leia `docs/architecture.md`, `docs/operating-model.md` e `docs/acceptance-criteria.md`.

Gate de bootstrap deste repositório fonte:
9. Crie ou retome `specs/build-the-guardian/` com todos os artefatos obrigatórios.
10. Trate este prompt como input da spec, complete impact map, plan, validation
    plan, stakeholder brief e tasks, e registre `Outcome Ready`/`Spec Ready`/
    `Human Visibility Ready`/`Tasks Ready` antes da implementação.
11. Se o bootstrap ocorrer tarde, registre a divergência em decision log e
    ratchet; não esconda a quebra de sequência.

Tarefa:
Completar, revisar e endurecer este bundle para que ele seja instalável como submódulo Git em `vendor/sdd-harness-guardian` e utilizável por agentes de IA em projetos consumidores.

Escopo obrigatório:
- manter o foco apenas em Spec Driven Development;
- usar Harness Engineering apenas como camada de execução, validação, memória e qualidade;
- manter separação entre builder e evaluator;
- criar ou revisar templates de spec, stakeholder brief, plan, tasks, impact
  map, validation plan, evidence pack, run-state, progress, handoff e ratchet;
- garantir que toda regra crítica tenha versão soft e recomendação de hard mirror;
- garantir que outcome readiness bloqueie execução sem transformar o Guardian em
  Product Owner;
- garantir que o stakeholder brief dê visibilidade humana sem virar fonte de
  verdade paralela;
- garantir que nenhum workflow permita marcar task como done sem evidence pack;
- garantir que interrupção e retomada sejam tratadas explicitamente;
- garantir que erros recorrentes alimentem `ratchet.md`;
- garantir que o bundle seja vendor-neutral;
- preservar compatibilidade com instalação por submódulo em `vendor/`.

Não faça:
- não transformar este bundle em aplicação SaaS;
- não implementar frontend;
- não implementar workflow engine real;
- não assumir LangGraph como dependência obrigatória deste repo;
- não misturar knowledge base viva dentro das skills;
- não criar regras específicas de um projeto consumidor;
- não remover a possibilidade de override por regras locais do projeto consumidor;
- não declarar tarefa completa sem checklist de validação.

Entrega esperada:
1. Estrutura final de diretórios.
2. Todos os arquivos `.md` revisados.
3. `manifest.yaml` coerente.
4. `INSTALL.md` operacional.
5. Templates prontos para copiar para projetos consumidores.
6. Checklist final em `docs/acceptance-criteria.md`.
7. Resumo final com:
   - arquivos criados;
   - decisões tomadas;
   - pendências;
   - como instalar;
   - como versionar;
   - como consumir em outro projeto.
8. Evidence packs da própria construção e decisão de evaluator independente.

Critério de aceite:
O bundle está pronto quando um segundo agente conseguir instalar este repositório em `vendor/sdd-harness-guardian`, ler `.harness/AGENTS.md`, abrir uma spec de feature em `specs/`, executar o workflow SDD e produzir evidence pack sem precisar de instruções externas.
```
