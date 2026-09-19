# DESIGN_SYSTEM.md — La Norma

Memória prática de decisões visuais já aprovadas ou comprovadamente úteis no 4174. Não é teoria — é o que existe hoje no código, com o motivo de cada escolha. Atualizar só quando uma decisão nova for de fato validada, não a cada ideia.

---

## 1. Cores

Definidas em `css/style.css :root`. Paleta quente ligada a café, saiu de preto/branco puro de propósito (ver `EVOLUTION_LOG.md`, Rodada 2).

| Token | Valor | Papel |
|---|---|---|
| `--espresso` | `#241c15` | Fundo escuro principal (`.section-dark`, header, hero) |
| `--espresso-deep` | `#170f0a` | Rodapé, fundo mais profundo (hero, page-hero) |
| `--cream` | `#f3ecdd` | Fundo claro principal, texto sobre fundo escuro |
| `--sand` | `#e7d9be` | Superfície clara secundária (`.audience`, `.cta-band`) — varia o ritmo sem virar full-brass |
| `--brass` | `#b8843c` | **Único acento** — botão primário, hover de link/ícone, sublinhado de nav ativo, régua dos `.principle`, estrelas do depoimento. Nunca fundo de seção inteira. |
| `--brass-light` | `#e4c48c` | Variante clara do acento (texto em brass sobre fundo escuro, telefone da topbar) |
| `--muted` / `--muted-dark` | `#b7a489` / `#6b5b45` | Texto secundário sobre fundo escuro/claro |
| `--line` / `--line-dark` | rgba translúcido | Bordas finas sobre fundo escuro/claro |

**Regra fixada:** só um acento controlado (brass/latão). O terracota `#D97757`-like foi evitado de propósito por ser um "tell" reconhecível de design gerado por IA (achado pela skill `redesign-existing-projects`). Não introduzir uma segunda cor de destaque sem motivo forte.

---

## 2. Tipografia

Três famílias, cada uma com um papel fixo — não usar fora do papel sem motivo:

| Família | Uso | Por quê |
|---|---|---|
| **Fraunces** (serif, `--ff-display`) | H1–H3, testemunho (itálico) | Lado "café/humano". Sentence case sempre — títulos grandes em uppercase foram removidos por parecerem genéricos. |
| **Archivo** (sans, `--ff-body`) | Nav, botões, corpo de texto, labels/eyebrow | Leitura corrida, neutro. |
| **IBM Plex Mono** (`--ff-mono`) | Números: `spec-list`, `zig-specs`, `stat-strip`, telefone | Lado "engenharia/precisão". Reservada para dado técnico/numérico — não usar em frase corrida (ver achado sobre a topbar no `EVOLUTION_LOG.md`). |

**Escala aproximada (extraída do CSS, não redefinida aqui):**
- H1 hero: `clamp(2.4rem, 4.6vw, 3.8rem)`, peso 600, `line-height:1.08`
- H1 page-hero: `clamp(2.2rem, 4.4vw, 3.4rem)`
- H2 de seção: `clamp(1.7rem, 3vw, 2.3rem)`
- Corpo (`p`): `1rem` base, `line-height:1.6`, lede do hero `1.05rem`
- Eyebrow/label: `.72rem`, peso 600, `letter-spacing:.2em`, uppercase
- Valor de stat: `clamp(1.15rem, 2.2vw, 1.55rem)` mono

---

## 3. Espaçamento e grid

- `.container`: `max-width:1180px`, padding lateral `32px`.
- `section`: padding vertical `112px` (`80px` em mobile ≤600px).
- Grid de 2 colunas para hero (`1.05fr .95fr`, gap `72px`) e `.workshop-block` (`1fr 1fr`, gap `64px`) — colapsa pra 1 coluna em ≤900px.
- `.principles` e `.product-zigzag`: gap generoso (`48px` / `88px`) — o espaço em branco é parte da composição editorial, não sobra.

---

## 4. Botões

- `.btn-primary`: fundo `--brass`, texto `--espresso-deep`, preenchimento invertido em hover (`::before` com `scaleX`).
- `.btn-ghost`: borda translúcida, preenchimento brass em hover.
- Sempre uppercase, `letter-spacing:.08em`, `border-radius:var(--radius)` (2px — quase reto, não pill).
- **Não criar um terceiro estilo de botão** sem motivo — os dois cobrem CTA primário e secundário em todas as páginas hoje.

---

## 5. Header

**Aprovado (~80%, segundo o Diogo — não redesenhar por redesenhar):**
- Estrutura fixa (`.header-stack`): topbar (nota + telefone) que recolhe ao rolar + header com logo/nav/social.
- Transição de recolhimento suave (`height`/`opacity` no scroll) — inspirada no site do Paulo Oliveira, já testada.
- Nav com sublinhado brass animado no ativo/hover.
- Comportamento mobile (drawer lateral, `.nav-toggle`) — funcional, sem bug relatado.

**Não está bom, registrado para próxima rodada (ver `EVOLUTION_LOG.md` Rodada 3):**
- Ícones sociais são caracteres de texto (`f`, `ig`, `in`) dentro de círculo — não são ícones reais, parecem placeholder.
- Tipografia do telefone na topbar: o link inteiro (`Llamar: +34 960 64 00 72`) está em `--ff-mono`, incluindo a palavra "Llamar" — deveria ser só o número em mono, o label em `--ff-body`.

---

## 6. Footer

Estrutura de 3 colunas (`logo+bio` / `contato` / `social`), mesma paleta escura do header (`--espresso-deep`). Telefone do footer **já** está isolado corretamente em `<p>` próprio com mono só no número (`.footer-grid a[href^="tel:"]`) — não repete o problema da topbar. Mesmo problema de ícones sociais genéricos do header se repete aqui (mesmo mercado, mesma solução).

---

## 7. Ícones

- **Ícones funcionais** (telefone, email, Instagram, mapa no `.cta-band`) já são SVG inline desenhados à mão, estilo linha fina (`stroke-width:1.7`, viewBox 24×24) — visualmente já parecido com bibliotecas tipo Lucide/Feather. Padrão bom, manter.
- **Ícones sociais do header/footer** (`f`, `ig`, `in` em texto) são o problema — não usam essa mesma linguagem.
- **Padrão recomendado para a próxima rodada:** ícones de marca (Facebook/Instagram/LinkedIn) vêm de uma biblioteca real de logos de marca — ex. **Simple Icons** (MIT, glifos de marca), não de um set de ícones de UI genérico (Lucide/Phosphor/Heroicons não têm logos de marca, são pra ações de interface). Ícones funcionais continuam no padrão SVG inline linha-fina já em uso — não precisa trocar o que já funciona.
- Não desenhar ícone novo à mão se uma biblioteca real já resolver.

---

## 8. Tratamento de imagem

- Filtro compartilhado para dar unidade de cor às fotos reais: `filter: saturate(0.88) sepia(0.14) hue-rotate(-8deg) contrast(1.03)` — aplicado em hero panel, about-strip, video-panel, workshop photo, process-panel. Não duplicar essa regra em lugares novos — adicionar o seletor à lista existente.
- `aspect-ratio` fixo + `object-fit:cover` em todo container de foto real (evita layout shift, preserva enquadramento original).
- Fotos de produto (render de estúdio) usam fundo com gradiente radial suave (`radial-gradient` branco + `linear-gradient` bege) em vez de fundo liso — mas o resultado ainda foi apontado como "fundo branco/cinza ruim" (ver Rodada 3). Existem alternativas no acervo (`assets/biblioteca-wp-completa/FUNDO CINZA/`, `MAQUINA FUNDO BRANCO/`) ainda não comparadas a fundo com critério.

---

## 9. Bordas e cantos

- `--radius:2px` — quase reto, não é o "cantos bem arredondados" genérico de UI kit. Manter esse valor baixo é uma decisão de estilo (editorial/técnico, não "app").
- Bordas finas (`--line`, 1px) usadas com função real (separar spec de card, separar coluna de footer) — não decorativas soltas.

---

## 10. Cards

- **Rejeitado e já corrigido:** grid de 3 cards iguais com borda fina (`.pillars`) — era o padrão mais genérico de IA identificado pela skill `redesign-existing-projects`. Virou `.principles`: lista editorial sem card, com régua superior em brass.
- **Ainda em uso, não revisado:** `.product-card` em `productos.html` (grid de 3, com borda, fundo `--espresso`, arte com fundo gradiente) — mesma família visual de "card com borda fina" que os `.pillars` tinham. O `index.html` já resolveu isso pro teaser de produto (zig-zag sem card, seção 4 do `EVOLUTION_LOG.md`); `productos.html` mantém o card por ser a página de ficha técnica completa (decisão consciente da Rodada 2 — não duplicar o zig-zag), mas vale reavaliar se o card ainda parece genérico numa próxima rodada de produtos.

---

## 11. Animações

O que existe hoje (tudo microinteração pontual, sem scroll-driven):
- Hover de botão (preenchimento `scaleX`), sublinhado de nav, hover de ícone/canal (`translateY` leve).
- Accordion de FAQ (`faq-open` keyframe, translateY+opacity).
- Intro-gate: fade+translateY por step (`intro-fade`, 500ms).
- Transição de página via Swup (fade+translateY, `html.is-changing`/`is-animating`) — via CDN, falha em silêncio se offline (o site precisa funcionar 100% sem internet).

**Regra fixada:** sem cine-scroll ou animação de página inteira nesta fase — isso é fase futura (seção 13 do `PROJECT_BRAIN.md`). Microinteração pontual pode continuar sendo refinada.

---

## 12. Responsivo

Breakpoints únicos: `900px` (grids colapsam pra 1–2 colunas, nav vira drawer) e `600px` (ajuste fino de padding). Testado e funcional nas 3 páginas — não é ponto de dor reportado até agora.

---

## 13. Padrões aprovados (resumo)

- Paleta quente com 1 acento único controlado.
- 3 famílias tipográficas com papel fixo (display / corpo / mono-número).
- Filtro de foto compartilhado pra unidade visual entre fotos reais de origens diferentes.
- Lista editorial sem card (`.principles`, zig-zag de produto no index) em vez de grid de cards iguais.
- `--radius:2px` (quase reto) em vez de cantos arredondados genéricos.
- Ícone funcional = SVG inline linha-fina desenhado à mão, consistente entre si.

## 14. Padrões rejeitados (resumo)

- Grid de 3 cards idênticos com borda fina → tell de IA (corrigido nos `.pillars`, pendente revisão em `.product-card`).
- Cor de acento terracota (~`#D97757`) → tell de IA reconhecível, evitado de propósito.
- Ícone social como texto/abreviação (`f`, `ig`, `in`) em vez de glifo de marca real → pendente de correção (seção 7).
- Fonte mono aplicada a frase inteira (label + número) em vez de só o número → pendente de correção na topbar (seção 5).
- Vídeo como base da hero → trocado por foto estática pra garantir a composição pretendida (Rodada 2); vídeo continua não sendo requisito.
