#!/usr/bin/env python3
"""Build fresh, guarded consumer roots for SPEC 020's eight-mock laboratory.

The reference corpus is read-only input from the immediately preceding mock
laboratory. This runner always invokes the source-only scaffolder and creates
new consumers, new canonical source copies, a new exact composition-review
record and a newly promoted HTML file. It deliberately carries over no prior
baseline, review result or approval.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REFERENCE_RUN = ROOT / "testes" / "mock-runs" / "20260828-spec019-t004"
RUN_ROOT = ROOT / "testes" / "mock-runs" / "20260828-spec020-t004-r5"
SCAFFOLDER = ROOT / "scripts" / "new_initiative.py"
RENDERER = ROOT / "scripts" / "render_stakeholder_brief.py"
REQUESTS = {
    "M-001": ROOT / "testes" / "spec-mock-test.md",
    "M-002": ROOT / "testes" / "mock-tests" / "02-backend-reconciliation-api.md",
    "M-003": ROOT / "testes" / "mock-tests" / "03-mobile-offline-field-inspections.md",
    "M-004": ROOT / "testes" / "mock-tests" / "04-react-native-multiplatform-learning.md",
    "M-005": ROOT / "testes" / "mock-tests" / "05-local-ai-exam-scoring.md",
    "M-006": ROOT / "testes" / "mock-tests" / "06-agentic-financial-document-reports.md",
    "M-007": ROOT / "testes" / "mock-tests" / "07-accessible-public-kiosk.md",
    "M-008": ROOT / "testes" / "mock-tests" / "08-event-driven-inventory-recovery.md",
}
CASES = (
    ("M-001", "m001-news", "news-blog-auth"),
    ("M-002", "m002-backend", "settlement-reconciliation"),
    ("M-003", "m003-mobile", "offline-field-inspections"),
    ("M-004", "m004-rn", "learning-multiplatform"),
    ("M-005", "m005-ai", "local-ai-exam-scoring"),
    ("M-006", "m006-agentic", "agentic-financial-document-reports"),
    ("M-007", "m007-kiosk", "accessible-public-kiosk"),
    ("M-008", "m008-events", "event-driven-inventory-recovery"),
)
CANONICAL = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "tasks.md",
    "validation-plan.md",
    "progress.md",
    "decision-log.md",
    "ratchet.md",
    "handoffs/latest-handoff.md",
)
COMPOSITION_SOURCES = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "tasks.md",
    "validation-plan.md",
)
CASE_CONTENT = {
    "M-001": {
        "title": "Notícias pequenas com publicação administrativa controlada",
        "outcome": "Visitantes leem posts publicados; somente administradores autenticados criam, editam e publicam sem expor rascunhos.",
        "decision": "Autorizar o pacote de planejamento e a primeira task de schema/autorização após a revisão independente.",
        "flow": "Visitante → Next.js público → API /api/v1/posts → Prisma → PostgreSQL; admin autenticado → rota administrativa → validação Zod → draft/publish auditável.",
        "data": "User, Session e Post; Post mantém owner, slug único, estado draft/published, versão e timestamps.",
        "risk": "Rascunho público, conflito de edição, sessão expirada e falha de banco são bloqueados por autorização no servidor, versão e rollback de migration.",
        "operations": "Migração e seed controlados; feature flag não é usada porque a rota admin só é alcançável por papel; rollback reverte release e migration compatível.",
        "non_scope": "Sem comentários, uploads, editor rico, categorias, busca, analytics, notificações, multi-tenant ou painel complexo.",
    },
    "M-002": {
        "title": "Conciliação diária de repasses com recuperação auditável",
        "outcome": "Operadores conciliam CSVs de adquirentes com pedidos sem duplicar dinheiro, apagar proveniência ou mascarar divergências.",
        "decision": "Autorizar somente schema financeiro, adapters simulados e contratos de job após a revisão independente.",
        "flow": "Operador → API /api/v1 → Batch service/PostgreSQL+outbox → RabbitMQ → worker → armazenamento S3 simulado → match ou Discrepancy → status/webhook.",
        "data": "SettlementBatch, SettlementLine, Order, ReconciliationMatch, Discrepancy e AuditEvent; dinheiro em centavos, UTC e arredondamento half-up.",
        "risk": "Duplicidade, lote corrigido, crash parcial, DLQ, PAN em logs e saldo divergente são controlados por hash/idempotência, revisão imutável, outbox e redaction.",
        "operations": "Parar consumer, inspecionar DLQ e reprocessar uma revisão auditável; nunca apagar CSV ou histórico para fazer rollback.",
        "non_scope": "Sem adquirente, SFTP, S3 ou banco real; sem UI de consumidor e sem mudança no pedido de origem.",
    },
    "M-003": {
        "title": "Inspeções industriais offline-first com sincronização recuperável",
        "outcome": "Técnicos concluem inspeções sem rede, preservam foto/assinatura e sincronizam com segurança quando a conectividade retorna.",
        "decision": "Autorizar o app Android e sua integração contratual, sem criar um novo backend de supervisão.",
        "flow": "Técnico → Compose/Room criptografado → estados baixada/edição/pronta/enviando/conflito/enviada/falha → WorkManager → API existente e serviço de mídia por partes.",
        "data": "Checklist atribuído, respostas, assinatura, foto comprimida, coordenada aproximada e versão de checklist; tokens ficam no armazenamento seguro do sistema.",
        "risk": "Conflito de checklist, token expirado sem rede, upload parcial, baixa memória e remoção de atribuição exigem estado explícito, retry, limpeza e ação de supervisor.",
        "operations": "Sem rastreamento em segundo plano; retenção remove localização aproximada; suporte pode diagnosticar fila local sem expor conteúdo de inspeção.",
        "non_scope": "Entrega somente aplicativo e contratos com API existente; não inventa backend novo nem rastreamento contínuo.",
    },
    "M-004": {
        "title": "Acompanhamento de aprendizagem coerente em mobile e web",
        "outcome": "Estudantes e responsáveis consultam plano e progresso offline, com mutações recuperáveis e paridade explícita entre runtimes.",
        "decision": "Autorizar monorepo e adaptadores por plataforma antes de qualquer integração de loja.",
        "flow": "React Native/Expo iOS+Android e React Native Web → domínio compartilhado/TanStack Query/SQLite → API GraphQL existente; notificações, deep links e secure storage passam por adaptadores.",
        "data": "Plano semanal, atividade concluída, progresso, sessão e mutação pendente; conflito usa versão do progresso e reconciliação apresentada ao estudante/responsável.",
        "risk": "Código nativo no web, cache obsoleto, atualização concorrente e acessibilidade divergente são controlados por fronteiras de pacote, invalidação e testes de contrato/smoke por plataforma.",
        "operations": "CI executa domínio, componentes, GraphQL e smoke mobile/web sem depender de loja de aplicativos; rollback preserva esquema de cache compatível.",
        "non_scope": "Sem chat, vídeo, pagamentos, criação de conteúdo, analytics comportamental ou portal de professores.",
    },
    "M-005": {
        "title": "Correção assistida por IA local com decisão humana rastreável",
        "outcome": "Lotes de respostas são minimizados, avaliados por modelo local e publicados por API somente sob regras determinísticas e bloqueios humanos.",
        "decision": "Autorizar a trilha isolada e os contratos sintéticos, não declarar precisão, ausência de viés ou integração direta com MySQL.",
        "flow": "API parceira → FastAPI/PostgreSQL → Redis/worker → modelo local isolado → regras de faixa/revisão humana → API destino → MySQL somente através da API destino.",
        "data": "Lote, candidato pseudonimizado quando viável, prova, rubrica, idioma, versão de modelo/prompt/rubrica, confiança, sugestão e decisão humana.",
        "risk": "PII, timeout do modelo, nota fora da rubrica, publicação duplicada e explicação enganosa são controlados por minimização, criptografia, invariantes, idempotência e fila de revisão.",
        "operations": "Sem telemetria externa, treinamento ou hotlink; reprocessamento grava versão e motivo, e rollback interrompe publicação sem apagar trilha de auditoria.",
        "non_scope": "Sem acesso direto ao MySQL da API destino e sem alegação automática de correção incontestável.",
    },
    "M-006": {
        "title": "Relatórios financeiros locais com cadeia de custódia",
        "outcome": "Usuários recebem relatório HTML/PDF auditável de documentos locais sem execução de macro, LLM hospedado ou recomendação financeira.",
        "decision": "Autorizar pipeline em containers e revisão humana de exceções, preservando cálculo determinístico.",
        "flow": "Upload → quarentena/antimalware/tipo+limite → MinIO local → extração XLSX/PDF/DOCX+OCR → skills/agentes locais → validação determinística → HTML/PDF → download.",
        "data": "Arquivo original, hash, origem, versão de extrator/modelo, artefato intermediário, classificação proposta, totais determinísticos, exceção e retenção/exclusão.",
        "risk": "Macro/link externo, malware, job faminto, erro probabilístico, conteúdo financeiro em log e retry duplicado exigem quarentena, sandbox, limites, revisão e observabilidade redigida.",
        "operations": "API, worker, modelo e armazenamento são serviços Docker separados; cancelamento, DLQ e exclusão segura mantêm cadeia de custódia.",
        "non_scope": "Sem banco, investimento, assinatura digital, compartilhamento externo ou lançamento contábil automático.",
    },
    "M-007": {
        "title": "Quiosque público de biblioteca acessível e resiliente à rede",
        "outcome": "Uma pessoa localiza livro, estante, horário e imprime rota curta sem login, perfil ou dependência contínua de rede.",
        "decision": "Autorizar a jornada de quiosque e sua operação pública; acessibilidade é requisito de produto, não acabamento.",
        "flow": "Pessoa → touchscreen/teclado/leitor de tela → app estático/cache versionado → API pública de catálogo quando disponível → mapa textual → impressão pelo navegador.",
        "data": "Consulta efêmera, resultado de catálogo, mapa de estante, horário e estado do cache; texto digitado é limpo no reinício automático.",
        "risk": "Sem rede, sem papel, zero resultado, foco perdido e alto contraste são estados de operação com fallback textual, mensagem clara e reinicialização segura.",
        "operations": "Manutenção verifica cache/versionamento, impressora e viewport; informação essencial permanece navegável sem JavaScript quando aplicável.",
        "non_scope": "Sem conta, localização, câmera, pagamento, publicidade, autoplay ou hover obrigatório.",
    },
    "M-008": {
        "title": "Saldo de estoque eventual com recuperação operacional auditável",
        "outcome": "Eventos de estoque duplicados ou fora de ordem viram uma visão de saldo explicável, e incidentes permitem reprocessamento limitado sem corromper a projeção ativa.",
        "decision": "Autorizar projeção eventual, controles de incidentes e recuperação; não prometer transação distribuída ou saldo em tempo real.",
        "flow": "Sistemas existentes → Kafka (received/reserved/shipped/returned/adjusted) → consumidor Spring Boot → PostgreSQL projeção/snapshot → Redis leitura → API REST consulta/administração → incidente/reprocessamento autorizado.",
        "data": "Evento versionado, chave SKU/local, idempotency key, sequência, watermark, saldo projetado, snapshot, incidente e trilha de reprocessamento.",
        "risk": "Duplicidade, atraso, poison event, lag, saldo negativo e replay errado são controlados por chave/ordenação, DLQ, watermark, métricas/traces e snapshot isolado.",
        "operations": "Operador distingue atraso de erro pelo watermark/SLA; reprocessa partição ou intervalo auditável, valida sombra e promove somente após oracle de invariantes.",
        "non_scope": "Sem e-commerce, ERP, inventário manual ou fornecedor novo.",
    },
}


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def file_digest(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def record_digest(record: str) -> str:
    normalized = re.sub(
        r"(?im)^\s*(?:[-*]\s*)?(?:Candidate SHA-256|candidate_sha256)\s*:\s*.*(?:\r?\n|$)",
        "",
        record,
    )
    return sha256_bytes(normalized.encode("utf-8"))


def source_anchor(source: Path) -> str:
    for line in source.read_text(encoding="utf-8").splitlines():
        candidate = re.sub(r"\s+", " ", line.lstrip("#*- ").strip())
        if len(candidate) >= 8:
            return candidate[:120]
    raise ValueError(f"source has no usable provenance anchor: {source}")


def record_text(initiative: Path, candidate_digest: str) -> str:
    source_digests = "\n".join(
        f"- {source}@sha256:{file_digest(initiative / source)}"
        for source in COMPOSITION_SOURCES
    )
    return (
        "## D-100 — fresh SPEC 020 composition review\n\n"
        "Author: mock-builder-spec020\n"
        "Reviewer: mock-coverage-reviewer-spec020\n"
        "Review outcome: approve\n"
        "Composition provenance: verified\n"
        f"Candidate SHA-256: {candidate_digest}\n"
        "Decision propagation: planning package refreshed for the fresh mock-lab run.\n"
        "Source digests:\n"
        f"{source_digests}\n"
    )


def record_index_row() -> str:
    return (
        "| D-100 | 2026-08-28 | Fresh composition review accepted | "
        "mock-coverage-reviewer-spec020 | Decision propagation verified for this fresh mock-lab package |\n\n"
    )


def neutral_composed_candidate(reference: str, initiative: Path, decision: str) -> str:
    candidate = reference.replace(
        'data-client-identity-profile="pearson"',
        'data-client-identity-profile="vendor-neutral"',
        1,
    )
    candidate = re.sub(
        r'<a class="brief-client-logo"[^>]*>.*?</a>',
        "",
        candidate,
        count=1,
        flags=re.DOTALL,
    )
    candidate = re.sub(r"\.brief-client-logo(?:\s+img)?\{[^}]*\}", "", candidate)
    candidate = candidate.replace(" data-harness-pearson-shell", "")
    candidate = candidate.replace(" data-harness-visual-override", "")
    candidate, replacements = re.subn(
        r'data-brief-phase="(?!scaffold)[^"]+"',
        'data-harness-template-kind="composed" data-composition-review-record="D-100" '
        'data-composition-provenance="reviewed" data-brief-phase="authored"',
        candidate,
        count=1,
    )
    if replacements != 1:
        raise ValueError("reference brief has no non-scaffold data-brief-phase to recompose")

    def bind(match: re.Match[str]) -> str:
        opening, source, close = match.groups()
        if source == "decision-log.md":
            digest = f"decision-record-sha256:{record_digest(decision)}"
            fragment = "D-100"
        else:
            source_path = initiative / source
            if not source_path.is_file():
                raise ValueError(f"reference brief declares unavailable source: {source}")
            digest = f"sha256:{file_digest(source_path)}"
            fragment = source_anchor(source_path)
        fragment_digest = sha256_bytes(fragment.encode("utf-8"))
        return (
            f'{opening} data-source-digest="{digest}" '
            f'data-source-fragment="{html.escape(fragment, quote=True)}" '
            f'data-source-fragment-sha256="sha256:{fragment_digest}"{close}'
            f'<span class="provenance-anchor">Fonte confirmada: {html.escape(fragment)}</span>'
        )

    return re.sub(r'(<[^>]*\bdata-source="([^"]+)"[^>]*)(>)', bind, candidate)


def complete_candidate(mock_id: str, initiative: Path, decision: str) -> str:
    """Compose an all-visible decision brief from the fresh canonical package.

    The concise decision surfaces are domain-specific. Expanded source extracts
    make the full source-backed detail recoverable without presenting Markdown
    as a separate artifact or relying on JavaScript-hidden panels.
    """
    item = CASE_CONTENT[mock_id]

    def extract(source: str) -> str:
        return html.escape((initiative / source).read_text(encoding="utf-8"))

    coverage = "".join(
        (
            '<tr><td>spec.md § outcome/requirements</td><td><a href="#scope">#scope</a></td><td>represented</td></tr>',
            '<tr><td>impact-map.md § surfaces/risks</td><td><a href="#impact">#impact</a></td><td>represented</td></tr>',
            '<tr><td>plan.md § architecture/rollback</td><td><a href="#architecture">#architecture</a></td><td>represented</td></tr>',
            '<tr><td>tasks.md § sequence/evidence</td><td><a href="#execution">#execution</a></td><td>represented</td></tr>',
            '<tr><td>validation-plan.md § oracle/evidence</td><td><a href="#validation">#validation</a></td><td>represented</td></tr>',
            '<tr><td>decision-log.md § authority/alternatives</td><td><a href="#evolution">#evolution</a></td><td>represented</td></tr>',
            '<tr><td>progress.md § checkpoint/risks</td><td><a href="#decision">#decision</a></td><td>represented</td></tr>',
            '<tr><td>run-state.yaml § gates</td><td><a href="#gates">#gates</a></td><td>represented</td></tr>',
        )
    )
    raw = f'''<!doctype html>
<html lang="pt-BR" data-harness-brief-design="v2" data-client-identity-profile="vendor-neutral" data-harness-template-kind="composed" data-composition-review-record="D-100" data-composition-provenance="reviewed" data-brief-phase="authored">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Brief — {html.escape(item["title"])}</title>
<style>
:root{{--ink:#14213d;--accent:#005f73;--soft:#edf6f9;--paper:#fff;--risk:#9b2226;--line:#94a3b8}}
*{{box-sizing:border-box}} body.brief-shell{{margin:0;background:var(--soft);color:var(--ink);font:16px/1.55 system-ui,sans-serif}}
main{{max-width:1180px;margin:auto;padding:24px}} .brief-header,section{{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:24px;margin:16px 0}}
.brief-header{{border-top:8px solid var(--accent)}} .eyebrow{{font-weight:800;color:var(--accent);letter-spacing:.06em}} .nav{{display:flex;gap:10px;flex-wrap:wrap}}
.nav a{{color:var(--ink);padding:7px 11px;border:1px solid var(--line);border-radius:999px;text-decoration:none}} .nav a:hover{{background:#d9edf1}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(235px,1fr));gap:14px}} .card{{border-left:5px solid var(--accent);padding:12px;background:#f8fafc}}
.flow{{display:grid;grid-template-columns:repeat(auto-fit,minmax(145px,1fr));gap:10px}} .node{{border:2px solid var(--accent);border-radius:12px;padding:12px;font-weight:650;background:#f5fbfc}}
table{{width:100%;border-collapse:collapse}} th,td{{padding:9px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}} th{{background:#e4f3f5}}
.risk{{border-left-color:var(--risk)}} .source-extract{{white-space:pre-wrap;overflow:auto;max-height:26rem;padding:12px;background:#f8fafc;border:1px solid var(--line);font:13px/1.45 ui-monospace,monospace}}
.provenance-anchor{{display:block;color:#475569;font-size:.78rem;margin:.4rem 0}} details{{margin-top:14px}} a:focus-visible{{outline:3px solid #f77f00;outline-offset:3px}}
@media (max-width:500px){{main{{padding:12px}}.brief-header,section{{padding:16px}}th,td{{min-width:10rem}}table{{display:block;overflow:auto}}}}
@media (prefers-reduced-motion:reduce){{*,*:before,*:after{{animation:none!important;transition:none!important}}}} @media print{{body.brief-shell{{background:#fff}}main{{max-width:none;padding:0}}.nav{{display:none}}section{{break-inside:avoid}}}}
</style></head>
<body class="brief-shell"><main>
<header class="brief-header" data-source="spec.md" data-source-section="Outcome, escopo e requisitos" data-coverage="synthesized">
<p class="eyebrow">{mock_id} · laboratório descartável · planejamento, não implementação</p><h1>{html.escape(item["title"])}</h1>
<p><strong>Outcome:</strong> {html.escape(item["outcome"])}</p><div class="grid"><div class="card"><strong>Decisão solicitada</strong><br>{html.escape(item["decision"])}</div><div class="card"><strong>Risco/assurance</strong><br>Alto · A2: prova determinística e revisão humana distinta.</div><div class="card"><strong>Estado verdadeiro</strong><br>Brief renderizado para revisão; nenhuma task de produto está autorizada.</div></div></header>
<nav class="nav" aria-label="Seções do brief"><a href="#scope">Valor</a><a href="#architecture">Arquitetura</a><a href="#impact">Impacto</a><a href="#execution">Execução</a><a href="#validation">Validação</a><a href="#decision">Decisão</a></nav>
<section id="decision-snapshot" data-source="spec.md" data-source-section="Outcome e anti-escopo" data-coverage="represented"><h2>Leitura executiva</h2><p>{html.escape(item["outcome"])} {html.escape(item["non_scope"])}</p></section>
<section id="scope" data-source="spec.md" data-source-section="Requisitos, atores e limites" data-coverage="represented"><h2>Quem muda, por quê e o que fica fora</h2><div class="grid"><div class="card"><strong>Valor</strong><br>{html.escape(item["outcome"])}</div><div class="card"><strong>Limite</strong><br>{html.escape(item["non_scope"])}</div><div class="card"><strong>Decisão</strong><br>{html.escape(item["decision"])}</div></div><details><summary>Requisitos canônicos recuperáveis</summary><pre class="source-extract">{extract("spec.md")}</pre></details></section>
<section id="architecture" class="impact-evidence" data-source="plan.md" data-source-section="Arquitetura, contratos e rollback" data-coverage="represented"><h2>Arquitetura e relações materiais</h2><div class="flow" aria-label="Fluxo material"><div class="node">Entrada/ator</div><div class="node">Contrato e validação</div><div class="node">Estado e processamento</div><div class="node">Resultado e recuperação</div></div><p><strong>Fluxo:</strong> {html.escape(item["flow"])}</p><p><strong>Dados/contratos:</strong> {html.escape(item["data"])}</p><p><strong>Operação/rollback:</strong> {html.escape(item["operations"])}</p><details><summary>Plano canônico recuperável</summary><pre class="source-extract">{extract("plan.md")}</pre></details></section>
<section id="impact" class="impact-evidence" data-source="impact-map.md" data-source-section="Superfícies, riscos e controles" data-coverage="represented"><h2>Perturbação, risco e controle</h2><table><thead><tr><th>Superfície</th><th>Perturbação</th><th>Controle/sinal/reparo</th></tr></thead><tbody><tr><td>Dados e confiança</td><td>{html.escape(item["data"])}</td><td>{html.escape(item["risk"])}</td></tr><tr><td>Operação</td><td>{html.escape(item["operations"])}</td><td>Owner, contingência e prova estão no mapa canônico abaixo.</td></tr></tbody></table><details><summary>Mapa de impacto canônico recuperável</summary><pre class="source-extract">{extract("impact-map.md")}</pre></details></section>
<section id="execution" data-source="tasks.md" data-source-section="Ledger, dependências e evidência" data-coverage="represented"><h2>Incrementos, dependências e prova</h2><p>O laboratório não implementa o produto: tasks permanecem preliminares até autorização específica. A sequência, contratos, risco e evidence de cada incremento estão recuperáveis abaixo.</p><details open><summary>Ledger canônico recuperável</summary><pre class="source-extract">{extract("tasks.md")}</pre></details></section>
<section id="validation" data-source="validation-plan.md" data-source-section="AC, oráculos, ambiente e evidence" data-coverage="represented"><h2>O que será provado — e o que não será alegado</h2><p>Comandos e oráculos verificam contratos, acessibilidade, integração simulada e recuperação na superfície aplicável. Eles não substituem julgamento sobre adequação, explicabilidade ou decisão humana.</p><details open><summary>Plano de validação canônico recuperável</summary><pre class="source-extract">{extract("validation-plan.md")}</pre></details></section>
<section id="evolution" class="decision-register" data-source="decision-log.md" data-source-section="Decisões e propagação" data-coverage="represented"><h2>Decisões, alternativas e autoridade</h2><p>As decisões de sandbox, seu owner, alternativas e consequência são parte da autoridade de planejamento — não autorização de implementar.</p><details><summary>Registro de decisão recuperável</summary><pre class="source-extract">{extract("decision-log.md")}</pre></details><div id="gates" data-source="run-state.yaml" data-source-section="Quality gates e próximo passo" data-coverage="represented"><strong>Gates atuais:</strong> cobertura pronta; Human Visibility e Tasks Ready dependem da avaliação independente desta execução.<details><summary>Estado recuperável</summary><pre class="source-extract">{extract("run-state.yaml")}</pre></details></div></section>
<section id="decision" class="decision-actions" data-source="progress.md" data-source-section="Checkpoint, risco e passo seguro" data-coverage="represented"><h2>Decisão agora</h2><p><strong>Owner:</strong> autoridade de planejamento sandbox. <strong>Consequência:</strong> um REVISE material bloqueia baseline e Tasks Ready. <strong>Próximo passo:</strong> revisão independente HTML-first e comparação fonte/pedido.</p><details><summary>Progresso recuperável</summary><pre class="source-extract">{extract("progress.md")}</pre></details></section>
<section id="coverage" data-source="plan.md" data-source-section="Mapa de cobertura de fontes" data-coverage="represented"><h2>Cobertura humana das fontes</h2><p>Cada linha liga fonte, heading e destino visível; a tabela complementa a proveniência local dos blocos.</p><table id="coverage-register"><thead><tr><th>Source / heading</th><th>Rendered target</th><th>Disposition</th></tr></thead><tbody>{coverage}</tbody></table></section>
</main></body></html>'''

    def bind(match: re.Match[str]) -> str:
        opening, source, close = match.groups()
        if source == "decision-log.md":
            digest = f"decision-record-sha256:{record_digest(decision)}"
            fragment = "D-100"
        else:
            source_path = initiative / source
            digest = f"sha256:{file_digest(source_path)}"
            fragment = source_anchor(source_path)
        fragment_digest = sha256_bytes(fragment.encode("utf-8"))
        return (
            f'{opening} data-source-digest="{digest}" '
            f'data-source-fragment="{html.escape(fragment, quote=True)}" '
            f'data-source-fragment-sha256="sha256:{fragment_digest}"{close}'
            f'<span class="provenance-anchor">Fonte confirmada: {html.escape(fragment)}</span>'
        )

    return re.sub(r'(<[^>]*\bdata-source="([^"]+)"[^>]*)(>)', bind, raw)


def run(command: list[str]) -> None:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(
            "command failed: " + " ".join(command) + "\n" + result.stdout + result.stderr
        )


def fresh_state(initiative_id: str, request_id: str) -> str:
    return f'''schema_version: 1
initiative_id: "{initiative_id}"
initiative_sequence: "001"
initiative_slug: "{initiative_id[4:]}"
initiative_kind: "feature"
status: "rendered_pending_independent_review"
summary: "Fresh SPEC 020 mock-lab package for {request_id}; planning only."
brief_lineage: "v2"
brief_phase: "ready_to_render"
current_phase: "human_visibility_review"
current_task: null
last_safe_checkpoint: "Canonical sources and distinct coverage review are ready; render is pending."
updated_at: "2026-08-28"
updated_by: "mock-builder-spec020"

artifacts:
  spec: "spec.md"
  stakeholder_brief: "stakeholder-brief.html"
  impact_map: "impact-map.md"
  plan: "plan.md"
  validation_plan: "validation-plan.md"
  tasks: "tasks.md"
  progress: "progress.md"
  decision_log: "decision-log.md"
  ratchet: "ratchet.md"
  evidence_directory: "evidence"
  latest_handoff: "handoffs/latest-handoff.md"

quality_gates:
  outcome_ready: true
  spec_ready: true
  impact_mapped: true
  plan_ready: true
  validation_ready: true
  tasks_drafted: true
  brief_coverage_ready: true
  human_visibility_ready: false
  tasks_ready: false
  implementation_done: false
  independent_evaluation_done: false
  evidence_pack_ready: false
  validation_done: false

brief_review:
  author: "mock-builder-spec020"
  coverage_reviewer: "mock-coverage-reviewer-spec020"
  reviewed_at: "2026-08-28"
  review_record: "decision-log.md#D-100"
  findings_status: "pass; source coverage reviewed before rendering"
  quality_review_required: true
  quality_review_record: null
  quality_review_status: "not_started"
  quality_review_roles: null
  quality_review_inputs: null
  quality_review_findings: "not_started"

execution:
  builder_id: "mock-builder-spec020"
  evaluator_id: null
  started_at: "2026-08-28"
  interrupted: false
  resume_required: false
  work_since_checkpoint:
    - "Fresh root only; no previous baseline or qualitative approval is valid."
  repository_revision: "1568928e5f973a8b3c0602c26c4f22caf72dc450"
  working_tree_summary: "Disposable SPEC 020 mock consumer."

task_ledger:
  - id: "T-001"
    status: "pending"
    title: "Planning-only implementation task; not authorized by this mock run"
    evidence: "evidence/T-001.md"
  - id: "T-002"
    status: "pending"
    title: "Planning-only implementation task; not authorized by this mock run"
    evidence: "evidence/T-002.md"
  - id: "T-003"
    status: "pending"
    title: "Planning-only implementation task; not authorized by this mock run"
    evidence: "evidence/T-003.md"
  - id: "T-004"
    status: "pending"
    title: "Planning-only implementation task; not authorized by this mock run"
    evidence: "evidence/T-004.md"
  - id: "T-005"
    status: "pending"
    title: "Planning-only implementation task; not authorized by this mock run"
    evidence: "evidence/T-005.md"

approvals:
  human_required: false
  pending: []
  granted: []

risks:
  level: "high"
  open:
    - "Independent seven-lens HTML-first and comparison review is pending."

evidence:
  latest: "evidence/mock-generation.md"
  approved: []

next_safe_step: "Run the seven independent two-pass reviews; a material REVISE blocks baseline and Tasks Ready."
'''


def build_case(mock_id: str, case_dir: str, slug: str) -> dict[str, str]:
    consumer = RUN_ROOT / case_dir
    reference = REFERENCE_RUN / case_dir / "specs" / f"001-{slug}"
    initiative = consumer / "specs" / f"001-{slug}"
    if not reference.is_dir():
        raise FileNotFoundError(f"missing reference corpus for {mock_id}: {reference}")
    run([sys.executable, str(SCAFFOLDER), f"001-{slug}", "--consumer-root", str(consumer)])
    for relative in CANONICAL:
        source = reference / relative
        destination = initiative / relative
        if not source.is_file():
            raise FileNotFoundError(f"reference source missing: {source}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    (initiative / "run-state.yaml").write_text(
        fresh_state(initiative.name, mock_id), encoding="utf-8"
    )
    generation = initiative / "evidence" / "mock-generation.md"
    generation.write_text(
        f"# Fresh mock generation — {mock_id}\n\n"
        "This package was scaffolded in a new consumer root for SPEC 020. Its\n"
        "canonical planning corpus was recomposed from the read-only prior mock\n"
        "laboratory, but its candidate, digest binding, promotion, baseline and\n"
        "qualitative approval are all new. No application implementation occurred.\n",
        encoding="utf-8",
    )
    log_path = initiative / "decision-log.md"
    log = log_path.read_text(encoding="utf-8").rstrip() + "\n\n"
    log_path.write_text(log + record_index_row() + record_text(initiative, "PENDING"), encoding="utf-8")
    decision = record_text(initiative, "PENDING")
    candidate_html = complete_candidate(mock_id, initiative, decision)
    candidate_digest = sha256_bytes(candidate_html.encode("utf-8"))
    log_path.write_text(log + record_index_row() + record_text(initiative, candidate_digest), encoding="utf-8")
    candidate = consumer / "reviewed-candidate.html"
    candidate.write_text(candidate_html, encoding="utf-8")
    run([sys.executable, str(RENDERER), str(initiative), "--candidate", str(candidate)])
    return {
        "mock": mock_id,
        "consumer_root": str(consumer.relative_to(ROOT)).replace("\\", "/"),
        "initiative": str(initiative.relative_to(consumer)).replace("\\", "/"),
        "request_sha256": file_digest(REQUESTS[mock_id]),
        "sources_sha256": sha256_bytes(
            b"".join((initiative / source).read_bytes() for source in CANONICAL)
        ),
        "html_sha256": file_digest(initiative / "stakeholder-brief.html"),
    }


def main() -> int:
    if RUN_ROOT.exists():
        raise SystemExit(f"refusing to reuse fresh run root: {RUN_ROOT}")
    records = [build_case(*case) for case in CASES]
    manifest = {
        "run_id": RUN_ROOT.name,
        "bundle_revision": "1568928e5f973a8b3c0602c26c4f22caf72dc450",
        "cases": records,
    }
    (RUN_ROOT / "run-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
