# PROJECT_BRAIN.md — La Norma

Memória oficial e enxuta do projeto. Ler antes de qualquer sessão de implementação. Decisão que não está aqui não existe.

---

## 1. Objetivo

Site institucional para a Lanorma Coffee Machine Manufacturer S.L. (Palma de Gandia, Valência), proposto ao administrador Daniel Climent Martínez. Front-end estático (HTML/CSS puro, sem backend), copy e specs reais extraídas do lanorma.es.

## 2. Estado atual

**Primeira versão de identidade visual completa implementada em 18/09** (mesma madrugada, segunda rodada): não é só estrutura mais — cor, tipografia e a hero foram redesenhadas nas 3 páginas. Publicada como preview remoto no GitHub Pages em 19–20/09 (`https://diogotorresweb.github.io/la-norma-preview-teste-/`).

**20/09 — Rodada 5, hero e intro fechadas via grilling.** Hero virou full-bleed com uma foto nova fornecida pelo Diogo (macro do display da máquina, sem pessoa, com "Lanorma" aceso na tela) — descartadas duas tentativas com fotos de pessoas por cobrirem rosto com texto. Intro perdeu a linha de assinatura (nenhuma das 4 fontes testadas convenceu) e a wordmark passou a ser brass em vez de branca. Ver `EVOLUTION_LOG.md` Rodada 5 para o processo completo e os itens em aberto (paleta de cor, material de apresentação, menção não confirmada de "curso no cabeçalho").

**20/09 — Rodada 4, acabamento executado.** Intro-gate refeita como abertura de marca (sem clique, ~2,1s, wordmark migra pro header), fotos de produto trocadas por recortes em alta dos renders reais, card eliminado do catálogo, topbar e ícones sociais corrigidos. Detalhe importante: a intro antiga travava o site inteiro em contexto onde `sessionStorage` lança — corrigido. Ver `EVOLUTION_LOG.md`, Rodada 4.

**20/09 — auditoria completa sem redesign.** Antes de abrir a próxima rodada visual, o projeto ganhou memória de processo dedicada: `EVOLUTION_LOG.md` (histórico de decisão + aprendizado por rodada) e `DESIGN_SYSTEM.md` (o que já está aprovado, em forma prática). Essa rodada auditou header, intro-gate, ícones, produtos (inventário real de modelos/fotos) e fotografia, e fechou uma fila de priorização P0–P3. Nenhuma linha de design foi alterada nela.

## 3. Decisão já fechada

- **4174** (`index.html` + `nosotros.html` + `productos.html` + `css/style.css`) é a **única base principal** da La Norma.
- **4176** (`ln200-site/`) está **fora de cena e não será desenvolvido**. Fica só como referência exploratória pontual (ver seção 5).
- **Não voltar a discutir 4176 como alternativa de projeto.** Essa discussão está encerrada.

## 4. Diagnóstico central

O projeto não trava por falta de código, assets ou pesquisa. Trava porque **a direção visual nunca foi decidida** — foi substituída, sessão após sessão, por ajustes cosméticos pontuais sob pressão de prazo.

## 5. O que manter do 4174

- Estrutura de 3 páginas (Home / Nosotros / Catálogo), navegação e transição entre páginas.
- Copy e specs técnicas reais (não inventadas).
- Limpeza de "tells de IA" já feita.
- **4176 não é fonte de referência para a nova direção visual.** Está fora de cena (seção 3) e não deve ser revisitado. Qualquer aprendizado útil que ele já rendeu (elemento de assinatura visual, registro tipográfico mono, arco narrativo) já está absorvido como conhecimento neste Brain — não exige voltar ao código do 4176 para consultá-lo de novo.
- A nova direção visual se constrói a partir de: **4174 + assets reais do projeto + referências externas reais** (quando necessário, ver seção 7).

## 6. Direção visual — primeira versão de identidade implementada

Hipóteses A (Instrumento de Precisão), B (Oficina, não catálogo), C (Editorial de Padrão) foram descartadas como estilos completos — o Diogo rejeitou os três na rodada de comparação visual. Uma rodada seguinte (9 referências "cinematográficas com fotografia estática") também não gerou escolha.

**O que gerou reação real:** 4 referências que o próprio Diogo encontrou (ver seção 7). A partir delas foi montada uma hipótese de estrutura, confirmada pelo Diogo em 18/09 e depois estendida para uma reconstrução completa do sistema visual ("transformar o 4174 em protótipo visual convincente para apresentar ao responsável da empresa").

**Sistema de cor** — saiu de preto/branco puro para uma paleta quente ligada ao universo do café, sem virar "bege":
- `--espresso` `#241c15` (base escura, substitui o preto puro `#141414`) e `--espresso-deep` `#170f0a` (rodapé).
- `--cream` `#f3ecdd` (base clara) e `--sand` `#e7d9be` (superfície clara secundária, usada em `.audience`/`.cta-band` para variar o ritmo sem virar full-brass).
- `--brass` `#b8843c` / `--brass-light` `#e4c48c` — acento único e controlado (evitado propositalmente o terracota `#D97757`-like por ser um "tell" reconhecível de design gerado por IA). Usado só em: botão primário, hover de link/ícone, sublinhado de nav ativo, linha divisória dos "principles", estrelas do depoimento — nunca como fundo de seção inteira.

**Sistema de tipografia** — trocado Bricolage Grotesque + Inter por três famílias com papel claro:
- **Fraunces** (serif) para headlines/H1-H3 — sentence case, sem uppercase (títulos grandes em uppercase foram removidos: eram genéricos demais). Dá o lado "café/humano".
- **Archivo** (sans) para nav, botões, corpo de texto, labels pequenas.
- **IBM Plex Mono** para números: specs técnicas (`spec-list`, `zig-specs`), barra de números (`stat-strip`), telefone. Dá o lado "engenharia/precisão".

**Hero (index.html) redesenhada** — era foto de fundo cobrindo a seção inteira (crop pesado, vídeo autoplay por cima, anéis decorativos sem função). Virou grid editorial de 2 colunas (texto à esquerda em fundo escuro sólido / foto real à direita em painel vertical, proporção fiel ao enquadramento original da `hero-bg.jpg`). O vídeo (`hero-home.mp4`) foi tirado da hero porque mostrava um enquadramento diferente (uma placa da máquina) do que a foto estática (barista + vapor) — manter a foto estática garante a composição pretendida; vídeo continua não sendo requisito.

**Reduzido conscientemente:** anéis decorativos da hero (`.hero-rings`), eyebrows redundantes (~7 removidos: "Más que una máquina", "Precisión", "Lo dicen nuestros clientes" ×2, "¿Hablamos?", "¿Quieres conocernos en persona?", "¿Para quién trabajamos?" — mantidos só os que carregam informação real: "Modelo", "Catálogo", "Nosotros"). `.pillars`/`.pillar` (grid de 3 cards com borda) virou `.principles`/`.principle` (lista editorial sem card, com régua superior em brass) — o padrão de "3 cards iguais" é o layout mais genérico de IA segundo a skill `redesign-existing-projects`. Removida função JS `initCarousel` morta dos 3 HTMLs (o carrossel de Instagram já tinha saído do HTML numa rodada anterior, a função ficou órfã).

**O que ainda está aberto:** isto é uma primeira versão para aprovação, não acabamento final. Cor de marca definitiva, uso de foto humana e nível de fidelidade ao site oficial continuam pendentes (seção 13). Copy não foi reescrito em profundidade — só os labels/eyebrows removidos; parágrafos maiores não foram tocados por já terem sido validados como reais em rodadas anteriores.

## 7. Referências visuais

- **Referências que geraram reação positiva real** (achadas pelo Diogo, não substituir sem pedido explícito):
  1. [Coffee Shop Website — Mulliri Mayfair](https://dribbble.com/shots/27640542-Coffee-Shop-Website-E-commerce-Experience) — hero em 3 colunas (texto / foto vertical central / texto+CTA); menu como lista elegante sobre foto.
  2. [Premium Café Shop — Elevated Coffee](https://dribbble.com/shots/27490733-Premium-Caf-Shop-Landing-Page) — tipografia gigante sobre foto macro. Importante para a composição da hero, junto com a Mulliri.
  3. [Business Website Concept — BeanCrafters](https://dribbble.com/shots/21480764-Business-Website-Concept) — **a referência estrutural que mais chamou atenção do Diogo.** Ritmo de seções alternando fundo claro/escuro é a ideia estrutural mais forte encontrada até agora.
  4. [Luxury Café Restaurant — Kosmos](https://dribbble.com/shots/27489018-Luxury-Caf-Restaurant-Landing-Page) — hero claro, xícara isolada com halo de luz, barra de números logo abaixo do hero, menu em zig-zag.
- **Restrição fixada:** a direção precisa funcionar principalmente com **fotografia estática real que a La Norma já possui** (produto, detalhe, oficina, pessoas, diagramas). Não depender de vídeo — vídeo é possibilidade futura, não requisito.
- **Hipótese de estrutura de página** (montada em cima das 4 referências acima — **ainda é hipótese de implementação, não decisão visual fechada**):
  ```
  HERO → barra de números (specs reais) → "mais que uma máquina" (foto real da oficina/fábrica + texto)
  → PRODUTOS (lista zig-zag, specs reais) → diferenciais (ícone + texto) → fabricação/processo (foto real)
  → depoimento (cliente real) → contato / onde encontrar (Palma de Gandia) → rodapé
  ```
- Extrair princípios (composição, tratamento de foto, hierarquia tipográfica), nunca copiar um site inteiro.
- **Implementado em 18/09** (commit a seguir): `index.html` reordenado seguindo o esqueleto acima (hero → barra de números → "más que una máquina" com `nosotros-cabecera.jpg` (foto real do time no mostrador) → produtos em zig-zag → diferenciais (pillars já existentes) → macro de extração (`nosotros-02.jpg`) com legenda sobre controle de temperatura/presión → depoimento → contato → rodapé). Carrossel de Instagram saiu do fluxo principal do index por não estar no esqueleto. `productos.html` ganhou a mesma barra de números após a hero e IDs de âncora por modelo (`#modelo-compacta`, `#modelo-2-grupos`, `#modelo-3-grupos`) para os links do zig-zag. `nosotros.html` ganhou depoimento + faixa de contato antes do rodapé (não tinha nenhuma chamada de contato antes).
- **Descoberta ao implementar:** as fotos de `assets/real/` (`nosotros-02/30/50/82/87.jpg`) são todas macro de extração/latte art, não fotos de fábrica/montagem — não existe nenhuma foto real de "linha de produção" no acervo hoje. Nenhuma seção nova afirma "ensamblaje" ou "taller" apoiada nessas fotos; onde o esqueleto pedia isso, foi ajustado para o que as fotos realmente mostram (ver seção "Pontos a confirmar").
- **Depoimentos reais usados** (avaliações públicas do Google, print enviado pelo Diogo — não inventados): Manuel Juan Rodríguez ("café fáciles de mantener y bonitas, servicio de 10") no index, focado em produto; Borja Reina Romero ("cracks, profesionales y serios") no nosotros, focado em pessoas. Um terceiro (berto fuster) ficou disponível e não usado ainda.

## 8. Skills

- Skills instaladas são **ferramentas disponíveis, não instruções permanentes**. Usar uma skill numa tarefa não significa que ela continua ativa nas próximas.
- Escolher a skill pela tarefa atual, não por hábito. Não empilhar skills sem necessidade.
- Não remover/desinstalar uma skill só por não ter sido usada recentemente.
- **Usadas em 18/09** para a implementação da seção 6: `redesign-existing-projects` (checklist de diagnóstico — apontou o padrão de "3 cards genéricos" e o cliché de cor terracota `#D97757`-like, evitado de propósito) e `example-skills:frontend-design` (processo de plano de design: paleta nomeada, papel de cada fonte, princípio de "gastar o efeito especial em um lugar só"). `simplify` rodou depois da implementação (4 subagentes em paralelo: reuse/simplificação/eficiência/altitude) — ver resultado no diff commitado.
- **Não usadas nesta rodada:** `humanizer` (copy grande não foi reescrito, só labels removidos) e `professor` (registro de decisão foi direto neste Brain, sem precisar da skill).
- **Usar depois** (fase de execução mais fina, não nesta rodada): `industrial-brutalist-ui` (só se um caminho mais industrial vencer), `animate`/`animation-vocabulary`, `improve-animations` (cine-scroll é fase futura, seção 13).
- **Ignorar por enquanto:** `10k-websites`, `high-end-visual-design`, `gpt-taste`, `stitch-design-taste`, `minimalist-ui`, `design-taste-frontend` (v1/v2) — sobreposição entre si e/ou já embutem resposta à pergunta da seção 6, que agora já tem uma primeira resposta implementada.

## 9. Caveman

- Disponível no projeto, mas **não é ativo continuamente** — uso sob demanda, tarefa por tarefa.
- Adequado para **execução mecânica, delimitada e cirúrgica** (1-2 arquivos, tarefa nomeada). Não decide direção visual, estratégia ou arquitetura.
- Quando uma tarefa for claramente adequada a ele, Claude pode sugerir o uso antes de executar.
- Sempre revisar o resultado/diff depois da execução — a checagem é sempre posterior ao fato.

## 10. Controle de contexto

- O chat **não é** a memória permanente do projeto. Arquivos do projeto são a memória persistente.
- `PROJECT_BRAIN.md` guarda estado, decisões e próximo passo. `TOOLS.md` guarda aprendizado sobre ferramentas.
- Chat atual deve conter só o contexto necessário para a tarefa atual. Tarefa grande se divide em etapas menores.
- `/compact` = mesma tarefa, contexto cresceu. Nova sessão = tarefa mudou de natureza.
- Antes de abrir nova sessão, registrar no Brain qualquer decisão importante que precise sobreviver.
- Não carregar conversa gigante por medo de perder contexto, e não repetir no chat o que já está registrado nos arquivos.
- Na dúvida sobre o estado do projeto, ler os arquivos oficiais antes de assumir. Estado atual registrado nos arquivos tem prioridade sobre conversas antigas ou documentos desatualizados.

## 11. Regra de continuidade

Se uma ferramenta, skill ou processo produzir um resultado claramente útil, **registrar o aprendizado no `TOOLS.md` antes de seguir para outra etapa**. Resultado bom não pode depender da memória do usuário.

## 12. Como trabalhar com este projeto

- Não assumir decisão que não está registrada neste arquivo.
- Não redesenhar antes da seção 6 ter escolha fechada.
- Não transformar discussão estratégica em implementação prematura.
- Manter decisões curtas e acionáveis — este arquivo é para decisão, não para diagnóstico longo.

## 13. Próximo passo exato

Rodadas 4 e 5 fecharam P0 inteiro, a maior parte do P1, e a hero/intro (`EVOLUTION_LOG.md`). Sessão pausada a pedido do Diogo pra commit + `/compact` antes de continuar — a lista abaixo é o backlog exato combinado no fim da Rodada 5, pra uma sessão nova (ou a mesma pós-compact) continuar sem perguntar de novo o que já foi decidido.

**Backlog confirmado pelo Diogo — Rodada 6 (20/09, pós-compact):**

1. ~~**Botão de WhatsApp fixo**~~ — feito (`6716ca5`). Círculo verde fixo, fora do `#swup`, mesmo telefone real (+34 960 64 00 72), confirmado pelo Diogo como WhatsApp Business ativo.
2. ~~**CTA da hero repensado**~~ — feito (`7ca0724`). Testamos ao vivo 4 variantes (2 CTAs x 2 tipos de prova social — citação real do Google, depois specs). Nenhuma prova social coube no tom B2B da hero (o Diogo rejeitou as 4); decisão final: hero fica limpa (título + parágrafo + 2 botões), só resolvendo a hierarquia entre eles — "Conocer La Norma" virou link de texto em vez de 2º botão do mesmo peso visual. **Aprendizado registrado:** prova social (depoimento ou specs) colada nos CTAs da hero não combinou — se isso for revisitado no futuro, considerar outro lugar da página, não embaixo dos botões.
3. **Explorar paleta de cor nova, com urgência** — o Diogo apontou que o brass/dourado (o único acento do sistema desde a Rodada 2) **não existe em nenhuma máquina real nem na fábrica** — é uma cor sem base fotográfica real, mesmo problema que já matou o cobre na v1 (seção 6). Ele confirmou que quer testar isso, mas **não** foi escolhido como prioridade na Rodada 6 (o Diogo pulou esse item ao escolher o que fazer agora) — ou seja, ainda pendente, sem trabalho iniciado. Qualquer teste deve rodar em preview isolado, sem sobrescrever o brass já aplicado até uma nova cor ser aprovada de verdade.
4. ~~**"Formación" no menu do header**~~ — feito (`e901796`). Página `formacion.html` nova, honesta ("estamos preparando", sem inventar curso), com canais reais (WhatsApp/telefone/email) pra quem quiser ser avisado. Item adicionado ao menu nas 4 páginas.
5. **Motionographer como referência** — ainda pendente, não iniciado nesta rodada.
6. **Deck/material de apresentação para o Daniel** — ainda adiado, não iniciado nesta rodada.

**Aberto pela própria Rodada 6, ainda não resolvido:** o Diogo questionou o parágrafo abaixo do título da hero ("não sei se é dos melhores") e a fonte da hero, e pediu pra puxar isso na mesma rodada — ainda não foi feito, é o próximo passo real de uma sessão futura antes de ir pro item 3 (paleta).

**Pendências já registradas em rodadas anteriores, ainda de pé:** personalização de frontal inox (detalhe técnico com o Daniel), medida da Compacta (530 mm parece estreita pra 2 porta-filtros — o Diogo confirmou que é 2 porta-filtros mesmo), padronizar ordem palavra/span dos `.principle` entre index/nosotros, conteúdo/notícias (P3, sem estratégia de manutenção confirmada).

## 14. Regra de colaboração registrada nesta sessão

O Diogo confirmou explicitamente que o formato de pergunta em rodadas, com opções clicáveis (via `AskUserQuestion`, no estilo do skill `grill-with-docs`), funcionou muito melhor do que pedir pra ele descrever em texto o que quer — "isso tem que tornar regra global". A única fricção foi quando uma pergunta não tinha a opção certa e ele precisou escrever manualmente — ou seja, **capprichar nas opções pra cobrir a resposta provável, mas sempre permitir resposta livre como saída**. Usar isso como padrão em qualquer rodada de decisão de design deste projeto (e, por extensão, outros projetos do Diogo). **4174 continua sendo a única base; 4176 continua definitivamente fora de cena** (seção 3).

---

## Pontos a confirmar

- `README.md` e `contexto/CONTEXTO-SESSAO-2026-09-17.md` citam `hero-ln200-test.html`, que não existe mais na working tree (substituído por `ln200-site/`).
- `apresentacao-daniel/README.md` ainda descreve o 4174 como "preto+cobre"; o código já removeu o cobre antes, e agora (18/09) mudou pra paleta quente café/creme/brass — material de apresentação está ainda mais desatualizado frente ao código.
- `assets/real/diagrama-2-grupos.png`, `diagrama-3-grupos.png`, `diagrama-compacta.png` e `assets/real/logo.png` não são referenciados em nenhum HTML — sobra de iteração anterior, uso futuro não confirmado.
- Não existe no acervo nenhuma foto real de fábrica/linha de montagem (só macro de extração e uma foto de mostrador). Se o Diogo quiser uma seção de "processo de fabricación" mais literal no futuro, precisa de fotos novas — não dá pra forçar com o que já existe sem legendar errado.
