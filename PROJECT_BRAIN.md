# PROJECT_BRAIN.md — La Norma

> Tipo: **estado** — a seção 2 é **reescrita**, não empilha parágrafos datados.
> Histórico por rodada é o `EVOLUTION_LOG.md`.
> Atualizado: 30/09/2026 · Revisar até: 31/10/2026 · Dono: Diogo

Memória oficial e enxuta do projeto. Ler antes de qualquer sessão de implementação. Decisão que não está aqui não existe.

Este arquivo acumula quatro papéis de propósito (estado, decisão fechada, backlog
e próximo passo) — foi decidido na Rodada 8 e está na seção 15. A regra geral da
base está em `../../SISTEMA.md`; a exceção daqui é deliberada, para não criar uma
segunda verdade sobre o mesmo assunto.

---

## 1. Objetivo

Site institucional para a Lanorma Coffee Machine Manufacturer S.L. (Palma de Gandia, Valência), proposto ao administrador Daniel Climent Martínez. Front-end estático (HTML/CSS puro, sem backend), copy e specs reais extraídas do lanorma.es.

## 2. Estado atual

**29/09 — Rodada 9: revisão editorial e o site reaberto em pontos nomeados.** O sistema visual
está aprovado e não se mexeu. Mudaram duas coisas: **o tom** (o material estava escrito com voz
de agência externa a apontar falhas; passou a ser primeira leitura, referência e observação,
com o estado de cada informação declarado) e **as imagens do catálogo** (orientação e recorte).
Ver seção 13, item 11.

**28/09 — Rodada 8: o projeto deixou de ser só "o site".** Com o site congelado a pedido do
Diogo, a rodada fechou o material de apresentação (deck em três atos), o conteúdo de marketing
(pauta real, não maquete) e uma auditoria do próprio sistema de produção (`pesquisa/`). Ver
seção 13, item 10.

**Onde isso deixa o projeto:** sistema visual aprovado e congelado; site de 3
páginas no ar como preview no GitHub Pages
(`https://diogotorresweb.github.io/la-norma-preview-teste-/`); material de
apresentação ao Daniel pronto. **O próximo passo não é código — é a
apresentação.** Confirmar com o Diogo quando e como ela acontece.

Como chegamos aqui (identidade visual de 18/09, auditoria e memória de processo,
acabamento, hero full-bleed e intro): **rodadas 1 a 5 no `EVOLUTION_LOG.md`**, em
detalhe. Ficava repetido aqui em parágrafos datados que iam se empilhando — a
mesma doença que fez o status do site do Paulo chegar a 1065 linhas. Removida a
duplicata em 30/09; nada foi perdido.

**Buraco conhecido no histórico:** o `EVOLUTION_LOG.md` tem as rodadas 1, 2, 2.5,
3, 4, 5 e 8. **Faltam as rodadas 6, 7 e 9** — a 9 (revisão editorial de 29/09)
existe só no parágrafo acima. Quem tocar no projeto: registre-as antes de abrir
rodada nova.

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

~~**Título/parágrafo/fonte da hero**~~ — feito (`93259f4`). Título trocado pra sans (Archivo bold), parágrafo reescrito e ancorado em fato real, sem citar número de modelos (ver item 7 abaixo pra saber por quê).

7. **Correção factual pós-Rodada 6:** o Diogo apontou, depois do commit acima, que o parágrafo da hero dizia "Tres modelos" — que estava impreciso. Fato real completo (ver `EVOLUTION_LOG.md`, seção "Produtos — inventário real", bloco "AMPLIADO na Rodada 6"): as 3 máquinas de sempre (Compacta/2 grupos/3 grupos) formam a linha **"Ln1"**, cada uma com opção de compra em **versão vaso alto** (config na hora da compra, não upgrade depois — vale pras 3, não só Mini/2 grupos como se pensava antes). Além disso existe uma **4ª máquina real, LN200**, lançamento novo já vendido mas **ainda não integrado ao site** — vai ganhar campanha estratégica própria (specs completas ainda não fornecidas de propósito). **Feito nesta correção:** parágrafo da hero não cita mais número de modelos; rótulo do `stat-strip` (index e productos) mudou de "Modelos en la gama" pra "Modelos Ln1" (preciso, não conta o LN200); FAQ nova em `productos.html` sobre vaso alto. **Não feito de propósito:** nenhuma menção ao LN200 em `index.html`/`productos.html` — aguardar o Diogo trazer a campanha/specs antes de integrar. **Cuidado pra próxima sessão:** `ln200-site/` não é mais "fora de escopo" no sentido de "produto irrelevante" — é material de referência real do LN200, só que com identidade visual própria que não decidimos reaproveitar ainda. Os arquivos `ln1-blanco.jpg`/`ln1-negro.jpg` dentro de `ln200-site/assets/` **não são fotos do LN200** apesar do nome parecido (confirmado pelo Diogo) — não usar.

8. **Materiais de apresentação criados (21/09) — pasta `materiais/`.** O Diogo pediu pra pegar todo o conhecimento acumulado do projeto e aplicar em peças usáveis agora. Foram feitas 5: hub (`materiais/index.html`, **ponto de entrada da reunião**), deck de 5 slides refeito na identidade atual (`deck.html` + `La-Norma-Propuesta-2026.pptx` editável), protótipo de blog "Diario del taller" (`blog.html` + `blog-articulo.html`), kit de 6 posts de Instagram (`instagram.html`) e template de newsletter (`email.html`). Decisões técnicas e regra de honestidade aplicada estão em `materiais/README.md`. **Isso revoga o item 6 acima** — o deck deixou de estar adiado porque o Diogo pediu explicitamente. **Pendência real:** o `.pptx` **não foi aberto no PowerPoint** (não há PowerPoint nem LibreOffice nesta máquina); foi validado só por código — 5 slides 16:9, nenhum shape fora dos limites, todos os textos presentes. Conferir antes de mandar pro Daniel. Geradores versionados: `materiais/build-deck-pptx.py` e `materiais/recolor-logo.py`. **O blog usa o `css/style.css` real** (não uma cópia), então acompanha sozinho qualquer mudança de paleta do item 3.

9. **Rodada 7 (28/09) — intro + hero + header, com o que já funcionou nos outros projetos.** O Diogo disse que a hero "continua sem cara de hero" e que queria reestruturar o "pre entrance" (nome no código: `intro-gate`). O diagnóstico veio de ler os projetos terminados, não de opinião: a hero do **Oliveira** (`hero-d2`) centraliza o conteúdo em `100dvh`, faz a foto entrar de `blur(14px)` pra nítida, escalona a entrada do texto e funde a seção na cor da seguinte; a intro do **RC Arcade** é a evolução declarada desta aqui ("Regras duras herdadas da La Norma") e acrescenta um **segundo gesto** (a régua) e um **handoff** (`is-holding`) que a nossa não tinha. Ponto de retorno: tag `antes-hero-oliveira-28-09`.

   **Feito:** intro ganhou régua brass sob o wordmark, clique-em-qualquer-lugar e failsafe por timeout; a saída da intro agora **revela a hero em cascata** (`.hero.is-revealed`), então as duas telas viraram um movimento só. Hero passou a ocupar `100dvh` centralizada, com entrada da foto, degradê que funde na barra de números e botão-seta que rola até ela. Os dois botões viraram de mesmo peso — **Ver catálogo** (sólido) + **WhatsApp** (contorno com `backdrop-filter`), substituindo o link de texto. Header virou `grid-template-columns:1fr auto 1fr` com o logo no centro matemático, nav 3 à esquerda / 2 à direita, redes descendo pro topbar. No mobile, `.nav-panel` deixa de ser `display:contents` e vira ela mesma o painel deslizante — **os 5 links existem uma vez só no HTML, sem menu mobile duplicado**.

   **Duas decisões que a IA tomou sozinha, e que continuam abertas até o Diogo reagir ao vivo:** (a) **canto reto, não pílula** — o Oliveira usa `border-radius:9999px`, mas o `DESIGN_SYSTEM.md` diz em três lugares que `--radius:2px` é decisão de estilo e "não pill"; foi copiado o peso dos botões, não o formato; (b) **na intro foram aplicados só 2 dos 4 caminhos oferecidos** (segundo gesto + robustez), porque o Diogo respondeu "ainda não faço ideia" — ficaram de fora "composição com foto" e "cortina que abre", que competiriam com o handoff.

   **Bugs achados e corrigidos durante a verificação:** topbar de 34px com `overflow:hidden` cortava aviso e telefone depois que as redes entraram (redes escondidas abaixo de 900px, continuam no rodapé); o `justify-self:end` que centra o logo no desktop continuava valendo dentro do painel mobile e jogava Formación/Contacto pra direita; a seta da hero parava com a primeira linha da barra de números atrás do header fixo (`scroll-margin-top`).

   **Fora desta rodada, ainda pendente do `/professor`:** trazer o formulário do Oliveira, e a variante de cor negra das máquinas (o Diogo disse que tem as fotos no computador — **conferir se são mesmo as mesmas máquinas em negro antes de mexer**, e a ideia é segunda opção de cor arrastando pro lado, não trocar o que existe). **A seção das máquinas (Compacta / 2 grupos / 3 grupos) não foi tocada — ordem expressa do Diogo, ela só se mexe com ele junto.**

10. **Rodada 8 (28/09) — tudo o que não é o site.** Ordem expressa do Diogo: **não tocar no
    site**. A rodada tratou material de apresentação, conteúdo e o próprio jeito de trabalhar.

    **O fato novo que mudou o projeto:** o Diogo descreveu os buracos operacionais que vê de
    dentro da fábrica — etiqueta de cada máquina feita uma a uma na Zebra ZD421 (em alta
    temporada consome quase o dia do supervisor), albarán e etiqueta da DHL sempre presos a uma
    pessoa, e a pré-montagem que há tempos não sai do papel. Isso virou o **Ato 3** do deck.

    **Decisões fechadas com ele (não reabrir):** no Ato 3 ele se apresenta como **funcionário
    que enxerga e propõe**, demonstrando capacidade — **sem preço colado na automação**; o preço
    segue sendo só o da web, 800 €. O deck **não afirma qual sistema de gestão a empresa usa**
    (é misturado entre setores e ele não sabe com precisão): isso vira a primeira pergunta do
    diagnóstico. Nada no material menciona sair da empresa.

    **Entregue:** `materiais/deck-reuniao-daniel.html` (12 slides, três atos, com capturas reais
    do site em `materiais/assets/capturas/`); `pesquisa/` com três documentos
    (`sistema-de-producao.md`, `benchmark-fabricantes.md`, `automacao-pme-industrial.md`);
    `materiais/plan-de-contenido.md` com pauta de 8 artigos, calendário e textos de Instagram e
    newsletter prontos; segundo artigo escrito por inteiro (`materiais/blog-reparables.html`);
    `apresentacao-daniel/README.md` reescrito; e o **`.pptx` conferido pela primeira vez**, com
    dois defeitos reais corrigidos (contraste reprovado e colisão de título — ver
    `materiais/README.md`).

    **Piloto recomendado para o Ato 3: a etiqueta.** A ZD421 entende ZPL, então gerar em lote a
    partir da lista de pedidos é o caminho mais isolado, mais visível e reversível. **Antes de
    prometer qualquer coisa, confirmar com o Diogo como a etiqueta é feita hoje** (que programa,
    que modelo) e de onde sai a lista do dia.

    **Cuidado descoberto nesta rodada:** `materiais/` compartilha o `css/style.css` do site — o
    que é vantagem (acompanha a paleta) e risco (quebra em silêncio). A Rodada 7 renomeou a
    classe das redes sociais e os protótipos do blog ficaram com ícones gigantes por semanas sem
    ninguém ver. **Toda rodada que renomear classe no site precisa olhar `materiais/`.**

11. **Rodada 9 (29/09) — revisão editorial e imagens do catálogo.** O sistema visual está
    aprovado; nada de redesign. Mudou o **tom** e mudaram **três imagens**.

    **Regra de estado da informação (nova, vale para todo o material):** facto · observação do
    Diogo · referência · exemplo · hipótese · pergunta. Não se misturam, e cada slide declara
    o seu no `eyebrow`. Motivo: o material cobre uma fração pequena da empresa e estava escrito
    como se fosse um diagnóstico dela.

    **O que saiu do deck:** os cinco `no existe` a vermelho do slide do sector (viraram
    "todavía no", sem cor de falha, sob o título "miré qué tienen otros fabricantes… por si
    algo encaja aquí"); o veredito "La Norma tiene un problema de fricción"; "lo que hoy se
    hace en PowerPoint"; e **os 2.500–4.000 € da agência mais os "dos meses"**, que eram o
    único número sem fonte do material — substituídos por dizer que não pediu orçamento.

    **Imagens: o espelho foi tentado e revertido.** A ideia era pôr a Compacta e a de 3 grupos
    a olhar para dentro da página. **Não existe nenhum render virado para a direita em todo o
    repositório** — verificado nos 234 ficheiros, incluindo os 3 GIF turntable, que só têm 3
    poses únicas — por isso a única via era espelhar. **Não resulta, e está fechado:** o
    espelho troca o sentido do declive do painel da bandeja, e a pegatina "Lanorma Ln1"
    recolada fica encavalitada na aresta em vez de centrada, com fantasma do texto antigo por
    baixo. O Diogo apanhou isso à vista. Testado também: repor marca a marca o logótipo das
    chávenas (inconsistente) e limpá-las (apagou os ícones dos botões). **As duas imagens
    voltaram aos originais e o layout não mudou** — Compacta e 3 grupos continuam a olhar para
    fora da página, consequência aceite. A de 2 grupos nunca foi espelhada.

    Também: os vãos brancos fechados pelas barras do porta-chávenas na de 2 grupos eram recorte
    incompleto e foram abertos; **secção nova de vaso alto** em `productos.html`, com o único
    ativo limpo que existe (2 grupos, recortado de `VASO ALTO/`); e `.feature-item` tinha CSS
    escrito para `h4` com markup em `h3` — os títulos de "Pensada al detalle" nunca tiveram o
    uppercase pretendido, desde sempre.

    **Fallback em papel:** `@media print` novo **no fim** de `css/style.css` (antes perdia para
    o breakpoint de 900px, e a folha impressa tem ~720px) e dois PDFs derivados em `materiais/`.

    **Fica para depois:** variante negra. O recorte da Compacta negra está feito e guardado em
    `assets/_originais/compacta-negra-recorte-sem-espelho.webp`, mas espelhá-la deixa uma cunha
    onde a aresta brilhante da bandeja atravessa o wordmark. Falta material de 2 e 3 grupos
    negras na mesma pose, e de Compacta vaso alto (só existe em frame de GIF, com dithering).

    **Orientação das máquinas — em aberto, com as opções já pesadas.** Hoje a Compacta e a de
    3 grupos olham para fora da página. As três saídas possíveis, para não se voltar a discutir
    do zero: (a) passar as três fichas para texto-à-esquerda/máquina-à-direita — resolve sem
    espelho nenhum, mas acaba com o zigue-zague, e o Diogo preferiu não mudar a composição
    agora; (b) pedir renders do outro lado a quem fez os originais — é a única forma de ter
    isto sem remendo; (c) deixar como está. **Espelhar está descartado**, pelo motivo acima.

12. **Rodada 10 (29/09) — a hero em branco, e o protótipo enviado ao Daniel.**

    **O bug.** O Diogo abriu o link do Pages e a hero estava vazia; só o F5 a trazia. Não era
    especificidade nem ordem de regras: o conteúdo, a foto e a seta começam em `opacity:0` e
    dependiam de uma transição/animação correr até ao fim, e **a linha do tempo do browser está
    parada enquanto o separador está oculto** — que é o que acontece ao abrir um link do
    WhatsApp. Medido no ar: `.hero` tinha `is-revealed`, o seletor casava e tinha mais
    especificidade, e o `opacity` computado era `0`; em `getAnimations()` a transição estava
    `running` com `currentTime: 0` e `fill: backwards`, a segurar o valor inicial.

    **Regra que fica:** *nada que precise de estar visível pode depender de uma animação correr.*
    É a irmã da regra de fail-open que já existia (o `html.js` cobria o caso "sem JS", mas não
    o caso "JS corre e a animação não"). A classe `is-settled` dá o estado final por declaração
    estática e chega por três caminhos: agendada a seguir à cascata, à entrada quando a página
    carrega já oculta (aí salta-se a intro, que ninguém está a ver), e num `visibilitychange`.
    Verificado com o separador oculto e a timeline a zero — a condição que partia.

    **Ramos reconciliados.** Estavam divergidos (8 commits locais, `17ca234` no origin). Merge
    limpo; os ficheiros do site eram idênticos dos dois lados, a divergência era só material
    interno. `?v=15` → `?v=16`.

    **Descoberta com peso, para lá do site:** a biblioteca de media do WordPress antigo tem
    **123 ficheiros (52 MB)** e o site publica **33**. Lá dentro há produto que não está
    publicado (`VASO ALTO`, `MOEDOR`, `LEITERA`, `ESPECIFICACIONES`, GIFs turntable). Ou seja,
    material por lançar acessível a quem souber onde procurar. Vai dito ao Daniel como aviso,
    sem nomear mecanismo — o Diogo sabe que as descarregou, não afirma como é que a falha se
    chama.

    **A apresentação mudou de forma:** o Daniel não apareceu esta semana, por isso em vez da
    reunião com o deck de três atos vai uma mensagem de WhatsApp em duas etapas — primeiro o
    site com o aviso das fotos, o hub de materiais só depois. **O preço fica de fora**: os 800 €
    vivem colados ao diagnóstico, que é material de sala. A reunião continua em cima da mesa se
    ele a quiser. Mensagens redigidas em `~/.claude/plans/quirky-sniffing-barto.md`.

13. **Rodada 11 (01/10) — o aviso do `materiais/` cumpriu-se, e fui eu que o ignorei.**

    O Diogo abriu `blog-articulo.html` no telemóvel e o menu estava aberto por cima do
    artigo, com os seis itens derramados sobre o texto. Causa: a Rodada 7 trocou `.main-nav`
    por `.nav-panel` no site e **as regras do painel deslizante foram com a classe nova**. Os
    três protótipos do blog ficaram com o markup antigo e carregam o **mesmo** `css/style.css`,
    portanto o menu deixou de ter onde se esconder e renderizou inline.

    **Isto estava escrito na rodada 10, palavra por palavra** — *"toda rodada que renomear
    classe no site precisa olhar `materiais/`"* — e mesmo assim a Rodada 7 não olhou, e as
    rodadas seguintes também não. O aviso existir não chega; só é apanhado quem o lê **antes**
    de renomear, não depois. É a segunda vez que esta pasta quebra em silêncio (a primeira
    foram os ícones gigantes, por semanas).

    Corrigido: os três ficheiros do blog passam a ter o header split igual ao do site, com a
    nav partida 3/3 (Inicio·Nosotros·Catálogo | Diario·Formación·Contacto), as redes sociais
    descidas do header para o topbar, e `?v=14` → `?v=16`, que também estava para trás.
    Verificado a 375px (painel fora do ecrã, abre e fecha pelo botão, sem scroll horizontal) e
    a 1280px (`display:contents`, hambúrguer escondido, logo ao centro).

    **Os decks, o `email.html`, o `instagram.html` e o `materiais/index.html` não usam o header
    do site** — foram verificados e não foram tocados.

**Pendências já registradas em rodadas anteriores, ainda de pé:** personalização de frontal inox (detalhe técnico com o Daniel), medida da Compacta (530 mm parece estreita pra 2 porta-filtros — o Diogo confirmou que é 2 porta-filtros mesmo), padronizar ordem palavra/span dos `.principle` entre index/nosotros, conteúdo/notícias (P3, sem estratégia de manutenção confirmada).

## 14. Regra de colaboração registrada nesta sessão

O Diogo confirmou explicitamente que o formato de pergunta em rodadas, com opções clicáveis (via `AskUserQuestion`, no estilo do skill `grill-with-docs`), funcionou muito melhor do que pedir pra ele descrever em texto o que quer — "isso tem que tornar regra global". A única fricção foi quando uma pergunta não tinha a opção certa e ele precisou escrever manualmente — ou seja, **capprichar nas opções pra cobrir a resposta provável, mas sempre permitir resposta livre como saída**. Usar isso como padrão em qualquer rodada de decisão de design deste projeto (e, por extensão, outros projetos do Diogo). **4174 continua sendo a única base; 4176 continua definitivamente fora de cena** (seção 3).

## 15. Precedência entre arquivos (fixada na Rodada 8)

Existia contradição entre arquivos e nenhuma regra dizendo qual mandava. Agora manda esta:

1. **Estilo** → `DESIGN_SYSTEM.md`.
2. **Estado, decisão e próximo passo** → `PROJECT_BRAIN.md` (este arquivo).
3. **Por que foi decidido assim** → `EVOLUTION_LOG.md`.
4. **Ferramenta** → `TOOLS.md`.
5. **Fonte externa, com link e data** → `pesquisa/`.

Qualquer outro arquivo que contradiga os cinco acima **está desatualizado por definição** —
corrige-se, não se obedece. `contexto/` e `apresentacao-daniel/` são material de reunião, não
fonte de verdade sobre o estado do projeto.

Decisão registrada junto: **não criar `TASKS.md` nem `CURRENT_STATUS.md`.** O backlog vive na
seção 13 e funciona; um arquivo a mais seria uma segunda verdade sobre o mesmo assunto.
Diagnóstico da documentação inteira em `pesquisa/sistema-de-producao.md`, seção 5.

---

## Pontos a confirmar

- `README.md` e `contexto/CONTEXTO-SESSAO-2026-09-17.md` citam `hero-ln200-test.html`, que não existe mais na working tree (substituído por `ln200-site/`).
- `apresentacao-daniel/README.md` ainda descreve o 4174 como "preto+cobre"; o código já removeu o cobre antes, e agora (18/09) mudou pra paleta quente café/creme/brass — material de apresentação está ainda mais desatualizado frente ao código.
- `assets/real/diagrama-2-grupos.png`, `diagrama-3-grupos.png`, `diagrama-compacta.png` e `assets/real/logo.png` não são referenciados em nenhum HTML — sobra de iteração anterior, uso futuro não confirmado.
- Não existe no acervo nenhuma foto real de fábrica/linha de montagem (só macro de extração e uma foto de mostrador). Se o Diogo quiser uma seção de "processo de fabricación" mais literal no futuro, precisa de fotos novas — não dá pra forçar com o que já existe sem legendar errado.
