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
- H1 hero: Fraunces 500, `clamp(2.3rem, min(4.6vw, 7.4vh), 3.6rem)`, `line-height:1.14` (Rodadas 8–9; o `vh` segura laptops baixos)
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

**Topbar (resolvido na Rodada 4):** o label e o número têm papéis tipográficos separados — `Llamar` em `--ff-body`, `.64rem`, peso 600, `letter-spacing:.18em`, cor `--muted`; o número em `--ff-mono`, `.78rem`, `tabular-nums`, cor `--brass-light`, com sublinhado só no hover. Em ≤600px o label some e fica só o número. **Regra geral que sai daqui: mono é para o dado, nunca para a palavra que rotula o dado.**

---

## 6. Footer

Estrutura de 3 colunas (`logo+bio` / `contato` / `social`), mesma paleta escura do header (`--espresso-deep`). Telefone do footer isolado em `<p>` próprio com mono só no número (`.footer-grid a[href^="tel:"]`). Ícones sociais usam o mesmo sprite do header (seção 7), com o mesmo hover de preenchimento em brass.

---

## 7. Ícones

Duas famílias, com origens diferentes de propósito:

- **Ícones de marca** (Facebook/Instagram/LinkedIn, no header e no footer): glifos oficiais do **Simple Icons** (CC0), sólidos, embutidos num sprite SVG no topo de cada página (`<symbol id="ic-*">` + `<use href="#ic-*">`). Sprite em vez de SVG repetido: funciona offline, não duplica o path em 6 lugares. Tamanho 14px dentro dos círculos de 34/36px, `fill:currentColor`, hover preenche o círculo em brass.
- **Ícones funcionais** (telefone, email, mapa no `.cta-band`): SVG inline linha fina (`stroke-width:1.7`, viewBox 24×24). Padrão que já funcionava, mantido.

Regra: **não desenhar ícone à mão quando existe biblioteca real** — e escolher a biblioteca pelo tipo: set de UI (Lucide/Phosphor) não tem logo de marca, set de marca (Simple Icons) não tem ícone de ação.

---

## 8. Tratamento de imagem

- Filtro compartilhado para dar unidade de cor às fotos reais: `filter: saturate(0.88) sepia(0.14) hue-rotate(-8deg) contrast(1.03)` — aplicado em hero panel, about-strip, video-panel, workshop photo, process-panel. Não duplicar essa regra em lugares novos — adicionar o seletor à lista existente.
- `aspect-ratio` fixo + `object-fit:cover` em todo container de foto real (evita layout shift, preserva enquadramento original).
- **Foto de produto: recorte, não painel** (Rodada 4). A máquina aparece sem fundo próprio, direto sobre o fundo da seção, com `drop-shadow` discreto e uma sombra elíptica no chão (`::after` com radial-gradient) pra dar contato. Nada de moldura, gradiente de painel ou borda em volta.
- **Como os recortes são feitos:** a partir dos renders originais de 1920×1080 em `assets/biblioteca-wp-completa/MAQUINA FUNDO BRANCO/`, com remoção de fundo por *flood fill* a partir das bordas — nunca por limiar global, porque o corpo da máquina é branco e um limiar comeria a própria máquina. Saída em **WebP** (62–94 KB contra ~620 KB em PNG). Script em `EVOLUTION_LOG.md`, Rodada 4.
- Regra: só remover fundo chapado. Não inventar fundo, não gerar imagem, não alterar a máquina.

---

## 9. Bordas e cantos

- `--radius:2px` — quase reto, não é o "cantos bem arredondados" genérico de UI kit. Manter esse valor baixo é uma decisão de estilo (editorial/técnico, não "app").
- Bordas finas (`--line`, 1px) usadas com função real (separar spec de card, separar coluna de footer) — não decorativas soltas.

---

## 10. Cards

**O card foi eliminado do site.** Nenhum conteúdo principal mora dentro de caixa com borda hoje:

- `.pillars` → `.principles` (Rodada 2): lista editorial com régua superior em brass.
- `.product-card` → `.machine` (Rodada 4): no catálogo, a máquina ocupa ~1,18fr contra ~0,82fr das specs, alternando de lado a cada modelo, sem moldura. Specs em lista com régua (`.spec-list`), valores em mono alinhados à direita. Hover: `translateY(-8px)` na máquina em 550ms — único movimento, sem escala nem sombra crescendo.

A exceção que restou é o `.channel` do `.cta-band` (bloco pequeno de contato, onde a caixa tem função de área clicável).

---

## 10.5 Hero (atualizado na Rodada 9)

- **Full-bleed, não mais grid de 2 colunas.** `.hero` é `<img class="hero-bg">` em `position:absolute` cobrindo a seção + conteúdo por cima com dois gradientes sobrepostos (vertical de baixo + diagonal da esquerda — um só gradiente não dá contraste suficiente pra título grande sobre foto real).
- **Regra fixada: nunca cobrir rosto de pessoa real com texto**, mesmo que o scrim resolva o contraste técnico — decidido incorreto pra uma marca que quer mostrar "pessoas de verdade" (ver `EVOLUTION_LOG.md` Rodada 5). Fotos com gente só entram em full-bleed se sobrar espaço negativo real fora do rosto.
- Foto atual (Rodada 7): painel da Ln1 aceso no vapor (`assets/hero/`, tratada por `treat_hero.py`). `<picture>`: 16:9 (`hero-1280/1920/2560`) em tela larga, recorte 2:3 (`hero-mobile.jpg`) em **qualquer tela mais alta que larga (`max-aspect-ratio: 1/1`)** — entre 3:4 e 1:1 o 16:9 cortava dígitos dos displays laterais ao meio.
- Texto (Rodada 8): H1 em Fraunces 500 ("Hechas a mano. Pensadas para durar y repararse."), lede pequeno em Archivo.
- **Regra fixada (Rodada 9): o texto nunca sobe até a fileira de ícones/display.** O respiro de baixo é só do `.hero-content` e escala com a altura (`clamp(48px,10vh,112px)`; 136px no celular, 56px + CTA empilhado em celular ≤760px de altura). A hero não herda o padding de `section`. Testar sempre em altura baixa (1440×760, 1280×720, 375×667, 390×664 = iPhone com barras do Safari), não só nas alturas "de catálogo".
- Contraste medido (pior 5% dos pixels atrás de cada linha de texto): ≥4.7:1 em 12 viewports. O eyebrow tem um halo escuro só atrás das letras (`text-shadow`) em vez de escurecer mais o scrim.
- Entrada: cascata `hero-in` (ver seção 11).

## 11. Animações

O que existe hoje (tudo microinteração pontual, sem scroll-driven):
- Hover de botão (preenchimento `scaleX`), sublinhado de nav, hover de ícone/canal (`translateY` leve), hover de máquina (`translateY(-8px)`, 550ms).
- Accordion de FAQ (`faq-open` keyframe, translateY+opacity).
- **Intro-gate, ~1,5s de espera + 620ms de saída:** eyebrow entra (Rodada 5) → wordmark revelado por `clip-path` em brass (720ms) → cortina sobe (`translateY(-101%)`, 620ms) enquanto o wordmark **desliza até a posição exata do logo no header**, calculada em runtime. **Sem linha de assinatura embaixo** — testado com 4 tratamentos de fonte na Rodada 5 e nenhum convenceu; a estrutura final é só eyebrow + wordmark. Regras que isso fixou: a intro nunca exige clique, some sozinha, tem Saltar e Esc, roda uma vez por sessão, vira estática com `prefers-reduced-motion`, e **só existe se o JS rodar** (`html.js` no CSS) — sem JS o site abre direto. Fundo com textura real (crop desfocado/escurecido de uma foto real, nunca gerado) atrás do texto, bem sutil.
- **Entrada da hero (Rodadas 8–9):** eyebrow → H1 → lede → CTA, fade + `translateY(18px)`, 700ms, mesma curva da intro (`cubic-bezier(.22,.8,.2,1)`, sem overshoot), delays .12/.24/.40/.52s — termina em ~1,2s, antes da intro começar a sair (1,5s), então a cortina sempre revela o texto pronto. O estado invisível mora só no keyframe (`fill-mode:both`): se a animação não rodar, o texto aparece.
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
- Lista editorial sem card (`.principles`, `.machine`, zig-zag de produto) em vez de grid de cards iguais.
- `--radius:2px` (quase reto) em vez de cantos arredondados genéricos.
- Ícone de marca vem de biblioteca real (Simple Icons, via sprite); ícone funcional é SVG linha-fina inline.
- Produto recortado sobre o fundo da seção, com sombra de contato — nunca dentro de painel.
- Mono para o dado, sans para o rótulo do dado.
- Qualquer coisa que cubra a tela inteira (intro) tem que falhar aberto: sem JS ou com API bloqueada, o site abre.

## 14. Padrões rejeitados (resumo)

- Grid de cards idênticos com borda fina → tell de IA (corrigido em `.pillars` na Rodada 2 e em `.product-card` na Rodada 4).
- Cor de acento terracota (~`#D97757`) → tell de IA reconhecível, evitado de propósito.
- Ícone social como texto/abreviação (`f`, `ig`, `in`) → corrigido na Rodada 4 com glifos reais.
- Fonte mono aplicada a frase inteira (label + número) → corrigido na Rodada 4 na topbar.
- Intro que exige clique pra entrar no site → removida na Rodada 4; a entrada não pode depender de interação.
- Vídeo como base da hero → trocado por foto estática pra garantir a composição pretendida (Rodada 2); vídeo continua não sendo requisito.
- Frame de GIF comprimido como foto de produto → substituído por recorte de render em alta (Rodada 4).
