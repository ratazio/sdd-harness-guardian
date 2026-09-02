# Pearson — guia de identidade visual digital

> **Status:** especificação operacional para implementação de sites, portais e aplicações web.
> **Base visual:** capturas do site corporativo Pearson fornecidas em 11/08/2026 e inspeção do CSS público correspondente.
> **Objetivo:** permitir que outro agente replique o *look and feel* observado sem depender das capturas originais.

---

## 1. Direção de marca

A experiência Pearson deve parecer **humana, segura, inclusiva, clara e contemporânea**. A marca combina a credibilidade de uma instituição global de educação com uma linguagem digital acessível e calorosa.

Quatro princípios orientam todas as decisões:

1. **Aprendizado protagonizado por pessoas.** Use fotografia documental de pessoas aprendendo, colaborando, ensinando ou aplicando conhecimento.
2. **Clareza antes de decoração.** Hierarquia forte, texto legível, bastante espaço em branco e poucos elementos simultâneos.
3. **Geometria acolhedora.** Blocos simples, cantos arredondados e superfícies claras, sem aparência infantil.
4. **Contraste institucional.** Azul-marinho profundo ancora a marca; lavanda claro cria respiro; violeta indica ação.

O resultado não deve parecer um SaaS genérico, uma plataforma escolar infantil nem uma página excessivamente corporativa. Deve transmitir educação ao longo da vida, diversidade, progresso e confiança.

---

## 2. Ativos de marca

### 2.1 Logotipo principal disponível

- **Arquivo oficial fornecido:** [logo Pearson branco](https://plc.pearson.com/sites/pearson-corp/files/logo_w.png)
- **Formato:** PNG com transparência
- **Dimensão intrínseca:** `175 × 53 px`
- **Proporção:** `3,302:1`
- **Uso:** cabeçalhos, rodapés e áreas com fundo azul-marinho ou fotografia suficientemente escurecida.

Durante a implementação, baixe o arquivo e sirva-o localmente, por exemplo em `assets/brand/pearson-logo-white.png`. Evite *hotlink* em produção. Preserve a proporção e nunca redesenhe, digite, recorte, distorça, aplique sombra ou altere a cor do logotipo.

```html
<a class="brand" href="/" aria-label="Pearson — página inicial">
  <img
    src="/assets/brand/pearson-logo-white.png"
    width="175"
    height="53"
    alt="Pearson"
  />
</a>
```

```css
.brand img {
  display: block;
  width: clamp(9rem, 12vw, 11rem);
  height: auto;
}
```

### 2.2 Regras de aplicação

- Use o logotipo branco somente quando o contraste com o fundo for inequívoco.
- Sobre fotografia, aplique uma faixa ou gradiente escuro atrás do cabeçalho. Não dependa apenas da área escura ocasional da imagem.
- Como não foi fornecida uma versão escura do logotipo, em superfícies claras coloque-o dentro de uma área azul-marinho; não use filtros CSS para improvisar outra versão.
- Mantenha uma área livre mínima ao redor equivalente à altura do símbolo à esquerda do nome.
- Tamanho recomendado: `144–176 px` de largura no desktop e `128–148 px` no mobile.
- O logotipo deve ser um link para a página inicial e ter nome acessível, mesmo que a imagem possua `alt`.

---

## 3. Sistema de cores

### 3.1 Paleta central

| Token | Valor | Uso principal |
|---|---:|---|
| `brand-navy` | `#0B004A` | cabeçalho, rodapé, títulos, texto forte, ícones |
| `brand-violet` | `#4C30A5` | CTA primário, foco, seleção e estados ativos |
| `brand-lavender` | `#C1BFFA` | bordas, divisores e anéis de foco auxiliares |
| `canvas` | `#EDECF5` | fundo dominante de páginas e seções |
| `surface` | `#FFFFFF` | cartões, formulários, modais e superfícies elevadas |
| `ink-muted` | `#475061` | texto secundário, metadados e ajuda |
| `ink-subtle` | `#7F7E7E` | texto desabilitado; nunca para corpo pequeno em branco |
| `brand-magenta` | `#CE4EC9` | detalhe gráfico ou destaque pontual |
| `brand-aqua` | `#7FDFE0` | detalhe gráfico e ilustração sobre navy |

O azul-marinho deve ser visualmente dominante entre as cores saturadas. A distribuição sugerida é: `60%` lavanda/áreas claras, `25%` branco, `10%` navy e até `5%` de violetas ou acentos.

### 3.2 Cores semânticas

| Estado | Cor forte | Fundo sugerido | Regra |
|---|---:|---:|---|
| Informação | `#4C30A5` | `#F3F2FE` | ícone e borda violeta; texto navy |
| Sucesso | `#007A53` | `#E8F7F1` | use texto escuro; não comunique só pela cor |
| Atenção | `#B39D00` | `#FBF9E0` | ícone `#F7D046` com texto navy |
| Erro | `#B42318` | `#FDECEA` | mensagem explícita junto ao campo |

As cores vermelha, vinho e magenta dos cartões de Objetivos de Desenvolvimento Sustentável observados nas referências pertencem à identidade oficial dos **ODS**, não à paleta Pearson. Use-as apenas quando o próprio conteúdo exigir a marca dos ODS.

### 3.3 Tokens CSS

```css
:root {
  color-scheme: light;

  --color-brand-navy: #0b004a;
  --color-brand-violet: #4c30a5;
  --color-brand-lavender: #c1bffa;
  --color-brand-magenta: #ce4ec9;
  --color-brand-aqua: #7fdfe0;

  --color-canvas: #edecf5;
  --color-surface: #ffffff;
  --color-text: #0b004a;
  --color-text-muted: #475061;
  --color-text-disabled: #7f7e7e;
  --color-border: #c1bffa;
  --color-border-soft: #e0def8;
  --color-focus: #4c30a5;

  --color-info-bg: #f3f2fe;
  --color-success: #007a53;
  --color-success-bg: #e8f7f1;
  --color-warning: #b39d00;
  --color-warning-icon: #f7d046;
  --color-warning-bg: #fbf9e0;
  --color-danger: #b42318;
  --color-danger-bg: #fdecea;
}
```

### 3.4 Contraste

- Navy sobre branco: aproximadamente `18,9:1`.
- Navy sobre lavanda claro: aproximadamente `16,1:1`.
- Violeta sobre branco: aproximadamente `9,2:1`.
- Texto secundário sobre branco: aproximadamente `8,1:1`.
- Não use magenta (`#CE4EC9`) como texto pequeno sobre branco; o contraste é insuficiente para corpo de texto.
- Não use cinza sutil (`#7F7E7E`) para corpo de texto pequeno; reserve-o para estados desabilitados e elementos não essenciais.

---

## 4. Tipografia

### 4.1 Família

A família observada no site corporativo é **Plus Jakarta Sans**. Use-a em todo o produto, inclusive interface, títulos e números. Hospede os arquivos localmente quando possível. Fallback:

```css
html {
  font-family: "Plus Jakarta Sans", "Segoe UI", Arial, sans-serif;
  color: var(--color-text);
  font-synthesis: none;
  text-rendering: optimizeLegibility;
}
```

Pesos necessários: `400`, `500`, `600` e `700`. Evite `800/900`, pois deixam a marca mais pesada e agressiva do que as referências.

### 4.2 Escala responsiva

| Papel | Desktop | Mobile | Peso | Altura de linha |
|---|---:|---:|---:|---:|
| Display / H1 | `clamp(2.5rem, 4vw, 4rem)` | mínimo `40px` | `500–600` | `1.08–1.12` |
| H2 de seção | `clamp(2rem, 3vw, 3rem)` | mínimo `32px` | `500` | `1.15–1.2` |
| H3 / título de cartão | `28–36px` | `24–28px` | `500–600` | `1.2` |
| H4 / grupo de interface | `20–24px` | `20px` | `600` | `1.25` |
| Corpo amplo/editorial | `18–20px` | `17–18px` | `400` | `1.55–1.65` |
| Corpo de interface | `16px` | `16px` | `400` | `1.5` |
| Navegação/CTA | `15–17px` | `16px` | `600–700` | `1.3` |
| Eyebrow/breadcrumb | `12–14px` | `12px` | `700` | `1.3` |

Regras:

- Títulos usam *sentence case*, não todas as palavras capitalizadas.
- Eyebrows e breadcrumbs podem usar caixa alta com `letter-spacing: 0.12em`.
- Limite texto editorial a `60–72ch`; textos de cartão a `32–42ch`.
- Evite títulos extrapesados e corpo com menos de `16px`.
- Use sublinhado real em links inseridos em texto e nos CTAs textuais.

---

## 5. Espaçamento, grade e composição

### 5.1 Escala espacial

Use uma base de `8px`, com meios passos apenas em detalhes:

```css
:root {
  --space-1: 0.25rem; /* 4 */
  --space-2: 0.5rem;  /* 8 */
  --space-3: 0.75rem; /* 12 */
  --space-4: 1rem;    /* 16 */
  --space-6: 1.5rem;  /* 24 */
  --space-8: 2rem;    /* 32 */
  --space-10: 2.5rem; /* 40 */
  --space-12: 3rem;   /* 48 */
  --space-16: 4rem;   /* 64 */
  --space-20: 5rem;   /* 80 */
  --space-24: 6rem;   /* 96 */
  --space-30: 7.5rem; /* 120 */
}
```

### 5.2 Contêineres

- Site editorial/marketing: largura máxima de `1440px`.
- Produto web/dashboards: largura máxima de `1280px`.
- Gutter: `24px` em mobile, `32–48px` em tablet e `48–64px` em desktop amplo.
- Grade: `12` colunas no desktop, `6` no tablet e `1–4` no mobile; gap de `24–32px`.
- Seções editoriais devem respirar: `80–120px` na vertical em desktop e `56–80px` no mobile.

```css
.container {
  width: min(100% - 3rem, 90rem);
  margin-inline: auto;
}

@media (max-width: 47.99rem) {
  .container { width: min(100% - 2rem, 90rem); }
}
```

### 5.3 Ritmo visual

- Prefira grandes áreas planas de lavanda claro alternadas com blocos brancos.
- Alinhe títulos, parágrafos e cartões a uma grade comum.
- Não preencha todos os vazios. Espaço negativo é uma característica central.
- Use sobreposição apenas como gesto editorial importante, especialmente placa de conteúdo sobre hero.

---

## 6. Forma, borda, elevação e movimento

### 6.1 Raios

| Elemento | Raio |
|---|---:|
| Campo e controle compacto | `8–12px` |
| Botão padrão | `12px` ou cápsula completa |
| Cartão de produto | `20–24px` |
| Imagem de cartão | acompanha `20–24px` nos cantos externos |
| Placa sobre hero | `28–32px` nos cantos superiores |
| Avatar, ícone social | `999px` |

Não misture muitos raios numa mesma tela. Em páginas editoriais, cartões maiores podem ser mais arredondados; em interfaces densas, use `12–20px`.

### 6.2 Bordas e sombras

- Borda padrão: `1px solid #C1BFFA` ou `#E0DEF8` em contextos muito leves.
- As referências são majoritariamente planas. Use borda antes de sombra.
- Sombra permitida para menus, popovers e modais: `0 16px 40px rgb(11 0 74 / 0.12)`.
- Cartões comuns: sem sombra ou `0 8px 24px rgb(11 0 74 / 0.06)` no máximo.
- Evite sombras cinza pesadas, brilho difuso e efeito “cartão flutuando” em todos os blocos.

### 6.3 Movimento

- Duração: `160–240ms` para microinterações; até `400ms` para entrada de painel.
- Curva: `cubic-bezier(.2, .8, .2, 1)`.
- Hover deve alterar no máximo cor, sublinhado, borda ou deslocamento de `2px`.
- Respeite `prefers-reduced-motion: reduce` e remova transições não essenciais.

---

## 7. Fotografia e imagem

### 7.1 Direção fotográfica

Escolha cenas autênticas, otimistas e observacionais:

- pessoas de diferentes idades, gêneros, etnias e contextos;
- aprendizado em ação: colaboração, tecnologia, escrita, conversa, laboratório e trabalho prático;
- luz natural, cores reais e ambientes reconhecíveis;
- enquadramentos próximos o suficiente para criar conexão humana;
- momentos espontâneos, não poses corporativas olhando para a câmera.

Evite bancos de imagem excessivamente encenados, salas vazias, colagens, filtros de cor fortes e ilustrações “edtech” infantis.

### 7.2 Tratamento

- Hero: proporção aproximada `16:7` a `16:9`, `object-fit: cover` e ponto focal controlado.
- Cartão editorial: `4:3` ou `3:2`, com alturas uniformes por linha.
- Preserve tons de pele; não aplique tintas violetas sobre toda a fotografia.
- No hero com navegação branca, aplique gradiente superior:

```css
.hero::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgb(0 0 0 / 0.72) 0,
    rgb(0 0 0 / 0.25) 22%,
    rgb(0 0 0 / 0) 55%
  );
  pointer-events: none;
}
```

- Todo `<img>` informativo deve ter `alt` que descreva o conteúdo e a finalidade. Imagem puramente decorativa usa `alt=""`.

---

## 8. Componentes editoriais

### 8.1 Cabeçalho institucional

Desktop:

- altura visual de `88–104px`;
- fundo navy sólido ou sobreposição transparente em hero com gradiente;
- logotipo à esquerda, navegação horizontal central/direita e busca no extremo direito;
- texto branco, `15–16px`, peso `600`;
- estado ativo por sublinhado, borda inferior ou mudança sutil para lavanda.

Mobile:

- altura de `72–80px`;
- logotipo de `128–148px`;
- busca e menu em botões de toque de pelo menos `44 × 44px`;
- menu aberto em painel navy, não em minúsculo dropdown flutuante.

### 8.2 Hero com placa sobreposta

Padrão de maior assinatura visual:

1. fotografia em largura total com altura mínima de `500–620px` no desktop;
2. navegação sobre a parte superior escurecida;
3. placa lavanda centralizada, sobrepondo-se ao rodapé da imagem em `72–112px`;
4. placa com largura de `min(90%, 1160px)`, padding `48–72px` e cantos superiores `28–32px`;
5. breadcrumb em caixa alta; H1 grande; conteúdo subsequente alinhado à placa.

No mobile, reduza a sobreposição, use placa quase em largura total e padding `24px`.

### 8.3 Cartão editorial com imagem

- Superfície branca, raio `20–24px`, borda lavanda fina.
- Imagem ocupa a largura total e cerca de `42–50%` da altura do cartão.
- Conteúdo com padding `28–36px`.
- Título `28–36px`; corpo `17–19px`; CTA ancorado na base.
- Em uma linha de cartões, alturas devem ser iguais e CTAs alinhados.
- CTA textual: peso `700`, sublinhado e seta simples `→` à direita.

```css
.editorial-card {
  display: grid;
  grid-template-rows: auto 1fr;
  overflow: hidden;
  min-height: 100%;
  border: 1px solid var(--color-brand-lavender);
  border-radius: 1.5rem;
  background: var(--color-surface);
}

.editorial-card__body {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 2rem;
}

.editorial-card__cta { margin-top: auto; }
```

### 8.4 Cartão de destaque único

Use para relatórios, campanhas ou conteúdo prioritário. Largura aproximada de `640–760px`, centralizado na seção; imagem panorâmica em cima, corpo branco abaixo e borda lavanda. Não use sombra forte.

### 8.5 Links e CTAs

- Link editorial: navy, peso `700`, sublinhado visível, seta `→` com `16–24px` de afastamento.
- Botão primário de produto: fundo violeta, texto branco, altura mínima `48px`.
- Botão institucional claro sobre navy: fundo lavanda muito claro, texto navy, formato cápsula.
- Botão secundário: branco ou transparente, texto navy, borda navy/lavanda.
- Não use mais de um CTA primário por bloco visual.

```css
.button-primary {
  min-height: 3rem;
  padding: 0.75rem 1.5rem;
  border: 1px solid var(--color-brand-violet);
  border-radius: 0.75rem;
  background: var(--color-brand-violet);
  color: #fff;
  font: 700 1rem/1.25 "Plus Jakarta Sans", sans-serif;
}

.button-primary:hover { background: var(--color-brand-navy); }

.button-primary:focus-visible,
.text-link:focus-visible {
  outline: 3px solid var(--color-brand-aqua);
  outline-offset: 3px;
}
```

### 8.6 Rodapé

O rodapé é uma grande superfície navy e pode ter `560–760px` no desktop, conforme a quantidade de conteúdo.

- Logotipo branco no topo/esquerda.
- Uma área de descoberta com pequeno cartão fotográfico opcional.
- Colunas para inscrição, links rápidos e redes sociais.
- Títulos `28–32px`; links brancos com divisores `rgba(255,255,255,.3)`.
- Botão de inscrição claro em cápsula.
- Links legais menores, mas nunca abaixo de `14px`.
- Ícones sociais em círculos brancos de `32–40px`, com ícone navy.
- No mobile, empilhe tudo em uma coluna e preserve gaps de `32–48px`.

---

## 9. Componentes de produto e aplicações web

Esta seção traduz a identidade editorial para telas operacionais, como a referência “Ciclo editorial local”, sem prejudicar densidade, velocidade ou legibilidade.

### 9.1 Estrutura de página

- Adicione uma barra superior navy de `72–88px` com logotipo branco e, se necessário, nome curto do produto/usuário.
- Use fundo geral `#EDECF5`, substituindo fundos cinza-azulados genéricos.
- Limite o conteúdo a `1280px` e mantenha títulos alinhados com os cartões.
- H1 de aplicação: `40–56px`, navy, peso `600`; eyebrow violeta em caixa alta.
- Mantenha explicações operacionais em `#475061` e largura legível.

### 9.2 Painéis e cartões

- Fundo branco, borda `#C1BFFA`, raio `16–20px`.
- Padding `24–32px`.
- Sem sombra por padrão; sombra mínima apenas para hierarquia real.
- Título de painel `20–24px`, peso `600`, navy.
- Estado vazio usa borda tracejada lavanda, ícone simples e instrução útil; não exibe apenas “nenhum item”.

### 9.3 Formulários

- Rótulo sempre visível acima do controle; placeholder não substitui label.
- Altura de input/select: `48–52px`.
- Textarea: mínimo `144px`, redimensionável verticalmente.
- Fundo branco; borda `1px solid #C1BFFA`; raio `10–12px`.
- Espaço entre label e campo: `8px`; entre grupos: `20–24px`.
- Foco: borda violeta de `2px` e halo `0 0 0 4px rgb(76 48 165 / .14)`.
- Erro: borda vermelha, mensagem textual e ícone; sucesso não deve apagar instruções importantes.
- Campos desabilitados precisam continuar legíveis e não podem depender apenas de opacidade baixa.

```css
.field-control {
  width: 100%;
  min-height: 3rem;
  padding: 0.75rem 0.875rem;
  border: 1px solid var(--color-border);
  border-radius: 0.625rem;
  background: var(--color-surface);
  color: var(--color-text);
  font: inherit;
}

.field-control:focus-visible {
  border-color: var(--color-focus);
  outline: 2px solid var(--color-focus);
  outline-offset: 1px;
  box-shadow: 0 0 0 4px rgb(76 48 165 / 0.14);
}
```

### 9.4 Alertas, contexto e estado

- Aviso informativo: fundo `#F3F2FE`, borda lavanda, texto navy e ícone violeta.
- “Somente demonstração” deve ser um alerta explícito e persistente, não apenas uma faixa decorativa.
- Contexto de usuário/tenant pode ser um cartão compacto branco; use label secundária e valor forte, sem sombra grande.
- Tags de status usam texto + ícone ou texto + forma; nunca apenas cor.

### 9.5 Tabelas, listas e decisões

- Cabeçalho da tabela em lavanda claro ou branco, texto navy `600`.
- Divisores finos `#E0DEF8`; hover de linha `#F3F2FE`.
- Ações por linha devem ter rótulo acessível; evite menus de três pontos para a única ação disponível.
- Em telas estreitas, transforme linhas complexas em cartões, preservando a ordem semântica.
- Decisões críticas devem exigir confirmação clara, mas não confirmação dupla desnecessária.

### 9.6 Aplicação direta à tela “Ciclo editorial local”

Ao adaptar a tela de referência:

1. inserir cabeçalho navy com o logo Pearson branco;
2. trocar o fundo atual por `#EDECF5`;
3. manter H1 navy e trocar o eyebrow para `#4C30A5`;
4. refazer cartões com borda lavanda, raio `20px` e sombra quase imperceptível;
5. usar o CTA “Criar roteiro draft” em violeta `#4C30A5`, com hover navy;
6. padronizar todos os campos com `48–52px`, borda lavanda e foco violeta;
7. transformar a faixa de demonstração em alerta semântico com ícone de informação;
8. enriquecer o estado vazio de “Versões e decisão” com próximo passo;
9. empilhar as duas colunas abaixo de `1024px`, colocando “Roteiro” antes de “Versões e decisão”;
10. preservar a densidade de ferramenta: não adicionar hero fotográfico ou seções editoriais dentro do fluxo operacional.

---

## 10. Ícones e elementos gráficos

- Ícones de interface: traço simples, cantos levemente arredondados, `20–24px`, `stroke-width` próximo de `1.75–2`.
- Use navy por padrão; branco sobre navy; violeta para estados ativos.
- Setas textuais `→` são uma assinatura recorrente e devem permanecer simples.
- Ícone de busca no header: branco, `22–24px`, área clicável mínima de `44px`.
- Não misture ícones preenchidos, emojis, pictogramas 3D e traços finos no mesmo produto.
- Gráficos podem usar violeta, aqua, magenta e lavandas, sempre acompanhados de labels/padrões para acessibilidade.

---

## 11. Conteúdo e voz

- Tom claro, otimista, direto e inclusivo.
- Prefira verbos concretos: “Aprenda”, “Explore”, “Leia”, “Crie”, “Continue”.
- Explique valor ou próximo passo; não use slogans vagos em interfaces transacionais.
- Títulos curtos e naturais; corpo em frases completas.
- CTAs descrevem a ação, não “Clique aqui”.
- Em português, use *sentence case*: “Versões e decisão”, não “Versões e Decisão”.
- Evite jargão educacional ou técnico sem explicação próxima.

---

## 12. Responsividade

Breakpoints recomendados, ajustáveis ao conteúdo:

| Faixa | Largura | Comportamento |
|---|---:|---|
| Mobile | `< 640px` | uma coluna, gutters `16–24px`, header compacto |
| Tablet | `640–1023px` | 1–2 colunas, cartões mais largos, menu recolhido |
| Desktop | `1024–1439px` | grade de 12 colunas, navegação completa |
| Wide | `≥ 1440px` | conteúdo limitado; espaço externo cresce |

Regras:

- Grade de três cartões vira duas colunas em tablet e uma no mobile.
- Não apenas reduza tudo proporcionalmente; reorganize blocos e preserve tipografia legível.
- Nenhum conteúdo ou ação deve depender de hover.
- Áreas de toque devem ter no mínimo `44 × 44px`.
- Tabelas não devem forçar a página inteira a rolar horizontalmente.

---

## 13. Acessibilidade obrigatória

Meta mínima: **WCAG 2.2 AA**.

- Contraste de `4.5:1` para texto comum e `3:1` para texto grande e elementos gráficos essenciais.
- Foco visível em todo elemento interativo; não remover `outline` sem reposição equivalente.
- Ordem de tabulação acompanha a ordem visual e de leitura.
- HTML semântico: landmarks, headings sequenciais, listas, buttons e links corretos.
- Labels, instruções, erros e status associados programaticamente aos campos.
- Alertas dinâmicos usam `aria-live` apenas quando necessário.
- Ícones isolados têm nome acessível; ícones decorativos usam `aria-hidden="true"`.
- Conteúdo continua utilizável a `200%` de zoom e com largura CSS de `320px`.
- Vídeo precisa de legenda; áudio, de transcrição; animação respeita redução de movimento.
- Não codificar categoria, prioridade ou estado somente por cor.

---

## 14. O que fazer e o que evitar

### Fazer

- Usar navy, lavanda claro e branco como base dominante.
- Criar hierarquia por escala, espaço e contraste.
- Usar Plus Jakarta Sans em toda a experiência.
- Repetir cartões brancos arredondados com borda lavanda sutil.
- Manter fotografia humana, diversa e ligada a aprendizado real.
- Usar links sublinhados com seta para navegação editorial.
- Fazer interfaces operacionais mais densas que páginas institucionais.

### Evitar

- Usar roxo médio genérico como cor dominante no lugar do navy Pearson.
- Colocar o logo branco sobre fundo claro ou fotografia sem proteção de contraste.
- Inventar uma versão escura do logo com filtros CSS.
- Aplicar cores dos ODS como se fossem paleta da marca.
- Usar gradientes decorativos, glassmorphism, neon ou sombras pesadas.
- Misturar várias famílias tipográficas ou usar títulos ultra-bold.
- Arredondar absolutamente tudo em cápsulas.
- Encher dashboards com grandes fotos, heros e espaços editoriais que atrapalhem tarefas.
- Esconder links sob cards inteiros sem indicação visual e foco adequado.

---

## 15. Receita de implementação para agentes

Ao aplicar este guia em um site novo ou existente, siga esta ordem:

1. **Inventariar:** localizar layout global, fontes, cores, logo, botões, campos, cartões, navegação e estados.
2. **Instalar tokens:** criar as variáveis de cor, espaço, raio, sombra e tipografia antes de estilizar páginas isoladas.
3. **Aplicar fonte:** carregar Plus Jakarta Sans com os pesos `400/500/600/700` e eliminar famílias conflitantes.
4. **Adicionar ativo:** baixar o logo fornecido para os assets locais e usá-lo sobre navy.
5. **Corrigir a estrutura:** definir canvas, contêineres, gutters, grade e breakpoints.
6. **Atualizar componentes-base:** header, footer, botões, links, inputs, cartões, alertas, tabelas e modais.
7. **Adaptar templates:** diferenciar página editorial, landing page e tela operacional.
8. **Revisar conteúdo e fotografia:** garantir tom Pearson, crop responsivo e textos alternativos.
9. **Validar:** testar contraste, teclado, foco, zoom, mobile, tablet, desktop e redução de movimento.
10. **Comparar:** conferir consistência sistêmica, não apenas semelhança de uma única tela.

### Critérios de aceite visual

- [ ] A primeira leitura da página é navy + lavanda claro + branco.
- [ ] O logotipo está íntegro, proporcional e com contraste seguro.
- [ ] Plus Jakarta Sans está carregada e sem *layout shift* relevante.
- [ ] Títulos não estão pesados ou comprimidos demais.
- [ ] Cartões têm raio, borda e padding consistentes.
- [ ] Sombras são raras e discretas.
- [ ] CTAs primários são inequívocos; links editoriais estão sublinhados.
- [ ] Fotografia parece autêntica, humana e inclusiva.
- [ ] O layout reorganiza-se corretamente em `320px`, `768px`, `1024px` e `1440px`.
- [ ] Foco, contraste, labels, erros e estados atendem WCAG 2.2 AA.

---

## 16. Referência mínima copiável

```css
@layer reset, tokens, base, components, utilities;

@layer tokens {
  :root {
    --brand-navy: #0b004a;
    --brand-violet: #4c30a5;
    --brand-lavender: #c1bffa;
    --canvas: #edecf5;
    --surface: #fff;
    --text: #0b004a;
    --text-muted: #475061;
    --border: #c1bffa;
    --focus: #4c30a5;

    --radius-control: 0.625rem;
    --radius-panel: 1.25rem;
    --radius-editorial: 1.5rem;
    --shadow-overlay: 0 16px 40px rgb(11 0 74 / 0.12);
  }
}

@layer base {
  *, *::before, *::after { box-sizing: border-box; }

  html {
    font-family: "Plus Jakarta Sans", "Segoe UI", Arial, sans-serif;
    color: var(--text);
    background: var(--canvas);
  }

  body { margin: 0; line-height: 1.5; }
  img { display: block; max-width: 100%; height: auto; }
  h1, h2, h3, p { margin-block-start: 0; }
  a { color: inherit; text-underline-offset: 0.2em; }
  button, input, select, textarea { font: inherit; }

  :focus-visible {
    outline: 3px solid var(--focus);
    outline-offset: 3px;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

---

## 17. Fontes de referência

- Capturas fornecidas: hero e página de sustentabilidade; cards “Product, People, Planet”; ODS; card de relatório; rodapé; aplicação “Ciclo editorial local”.
- Site corporativo observado: [Pearson plc](https://plc.pearson.com/).
- Logo solicitado: [https://plc.pearson.com/sites/pearson-corp/files/logo_w.png](https://plc.pearson.com/sites/pearson-corp/files/logo_w.png).

Este guia descreve com alta fidelidade o sistema visual observado, mas não substitui eventuais manuais jurídicos oficiais da Pearson sobre marca registrada, licenciamento ou *co-branding*.
