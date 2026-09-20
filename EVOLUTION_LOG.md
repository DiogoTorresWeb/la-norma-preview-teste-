# EVOLUTION_LOG.md — La Norma

Registro de evolução visual e estratégica do projeto. Objetivo: uma sessão futura entender como chegamos até aqui sem depender do histórico do chat. Cada rodada importante entra aqui — problema, hipótese, referência, decisão, implementação, resultado, aprendizado, o que não repetir, próxima hipótese.

Ver também `DESIGN_SYSTEM.md` (o que ficou aprovado, em forma prática) e `PROJECT_BRAIN.md` (estado e decisões fechadas).

---

## Rodada 1 — 16/09, limpeza de última hora antes da reunião com Daniel

**Problema:** o site de 3 páginas tinha "cara de IA" evidente — cards genéricos, números de sequência falsos, eyebrows redundantes, seta solta na topbar, meta-string estranha no hero — e precisava destravar a reunião do mesmo dia sem quebrar nada.

**Decisão:** correção pontual e segura, sem tocar em composição de fundo (não havia tempo pra isso).

**Implementação:** logo real substituindo texto "Ln La Norma"; fotos de produto reais (`spec-*.jpg`, extraídas via ffmpeg de GIFs reais do site oficial); header com topbar recolhível (inspirado em oliveirafotos.es); seção de contato com grade de canais; transição de página via Swup; remoção da cor cobre/laranja inventada (não tinha base real — o site oficial é preto e branco); correção de emoji quebrado no carrossel.

**Resultado:** reunião destravada, mas o próprio Diogo apontou no mesmo dia que "ainda parece IA" (feedback textual: "cara de ai sloop ainda do carai") — os cards, a hierarquia tipográfica fraca e a falta de um elemento de assinatura visual continuavam.

**Aprendizado:** ajuste cosmético pontual sob pressão de prazo resolve sintoma, não causa. Cor sem base real (o cobre) foi identificada e removida rápido porque havia uma fonte real (site oficial) pra contrastar contra — mostra o valor de checar contra a fonte antes de aceitar uma decisão visual anterior.

**O que não repetir:** decidir paleta ou elemento visual "porque parece bonito" sem checar se tem base real no material da empresa.

**Próxima hipótese:** rodar uma skill de design de verdade (`example-skills:frontend-design`), com tempo, pra repensar composição — não só tokens de cor.

---

## Rodada 2 — 18/09, primeira identidade visual completa

**Problema:** o projeto não travava por falta de código ou assets — travava porque a direção visual nunca tinha sido *decidida*. Três hipóteses completas (Instrumento de Precisão / Oficina não catálogo / Editorial de Padrão) foram descartadas pelo Diogo numa rodada de comparação; uma rodada seguinte com 9 referências "cinematográficas" também não gerou escolha.

**Hipótese:** em vez de mais uma hipótese de estilo completa, usar 4 referências que o próprio Diogo achou e reagiu positivamente (Mulliri Mayfair, Elevated Coffee, BeanCrafters, Kosmos — ver `PROJECT_BRAIN.md` seção 7) como base de uma **estrutura de página**, não de um estilo pronto.

**Referência:** as 4 acima. Extraídos princípios (ritmo claro/escuro entre seções, hero editorial de 2 colunas, barra de números, produto em zig-zag) — nunca copiado layout, texto ou imagem.

**Decisão:** cor quente ligada a café (saiu de preto/branco puro), 3 famílias tipográficas com papel definido (Fraunces/Archivo/IBM Plex Mono), hero reconstruída como grid editorial 2 colunas com a foto real (`hero-bg.jpg`) em vez de vídeo autoplay, `.pillars` (cards) virou `.principles` (lista editorial).

**Implementação:** as 3 páginas reordenadas seguindo o esqueleto hero → stat-strip → "más que una máquina" → produtos zig-zag → diferenciais → macro de processo → depoimento → contato → rodapé. `simplify` rodou depois (4 subagentes em paralelo) e achou 2 blocos de CSS mortos, 3 duplicações reais, 1 `@import` de peso não usado — tudo corrigido.

**Resultado:** protótipo visual apresentável publicado (ver seção "Rodada 2.5" abaixo, deploy no GitHub Pages). Ainda é primeira versão, não acabamento final.

**Aprendizado:** decisão visual real não veio de gerar mais opções nem de descrever em texto o que se queria — veio de reagir a referências concretas e existentes. "Mostra, não descreve" funcionou onde 3 rodadas de hipótese-e-descrição não tinham funcionado. Também: nem toda foto do acervo serve pra toda legenda — descobrimos ao implementar que não existe nenhuma foto real de "linha de montagem/fábrica" no acervo (só macro de extração e uma foto de mostrador), e ajustamos a legenda pro que a foto realmente mostra em vez de forçar uma narrativa que a imagem não sustenta.

**O que não repetir:** pedir pra decidir direção visual só a partir de descrição textual, sem imagem de referência real na mesa. Também: os dois padrões de conteúdo dos `.principle` (`index.html` é palavra-depois-do-span, `nosotros.html` é span-depois-da-palavra) ficaram inconsistentes entre si — foi decisão consciente não padronizar ainda porque exigiria reescrever copy real aprovada; mas é uma inconsistência pendente, não esquecer dela.

**Próxima hipótese:** publicar como preview remoto (GitHub Pages) pra o Diogo reagir ao resultado real fora do ambiente de desenvolvimento, e só depois abrir a próxima rodada de refinamento.

---

## Rodada 2.5 — 19–20/09, preview remoto no GitHub Pages

Tarefa de infraestrutura pura (sem tocar em design): workflow do GitHub Actions publicando só os arquivos públicos (`index.html`, `nosotros.html`, `productos.html`, `css/style.css`, `assets/real/`) num repositório público, excluindo `PROJECT_BRAIN.md`, `TOOLS.md`, `contexto/` e o resto do material interno. Um bug de `cp -r` (perdeu um nível de pasta, `assets/real/*` foi publicado direto em `assets/*`) quebrou as imagens no ar por uma rodada — corrigido e verificado. **Aprendizado:** testar localmente a montagem exata da pasta de publicação antes de depender do resultado do CI economizaria o ciclo de "publicar → usuário reporta quebra → corrigir". URL final: `https://diogotorresweb.github.io/la-norma-preview-teste-/`.

---

## Aprendizados acumulados (antes da Rodada 3)

### O que funcionou
- Reorganizar a narrativa da Home em vez de só trocar estilo de seções existentes.
- Usar conteúdo real (specs, depoimentos do Google, fotos do acervo) em vez de placeholder.
- Números reais como prova (stat-strip) em vez de adjetivo solto.
- Apresentação editorial de produto (zig-zag) em vez de grid de card genérico.
- Prova social real (depoimentos verificáveis, atribuídos).
- Fotografia real, mesmo quando limitada (aceitar o que existe em vez de fingir que existe mais).
- Preocupação ativa em não inventar dado, claim ou testemunho.
- Usar referência externa real pra extrair princípio, não pra copiar.
- Separar claramente estrutura (o que vai em cada seção) de direção visual (cor/tipografia) de execução (código) — decidir uma coisa de cada vez.
- Git como memória do projeto (histórico de commit, branches) e GitHub Pages como preview remoto acessível do celular.

### O que não funcionou tão bem
- Alterações pequenas demais (rodadas de CSS pontual sem direção maior) — resolvem sintoma, viram alteração aleatória sem acumular aprendizado.
- Tentar decidir direção visual só por descrição textual, sem referência visual real na mesa (3 hipóteses + 9 referências não geraram escolha; 4 referências concretas geraram).
- Manter a hero praticamente intocada por várias rodadas, tratando-a como já resolvida sem reavaliar.
- Dependência excessiva de preto+branco puro (herdado do site oficial, sem examinar se servia à nova direção).
- Elemento visual criado do zero sem uma referência real por trás (ex.: cor cobre inventada na v1).
- Ícones sociais genéricos (texto abreviado, "f"/"ig"/"in") em vez de biblioteca de ícone real.
- Imagens de produto com fundo branco/cinza percebido como fraco, sem comparação de critério contra alternativas do próprio acervo.
- Excesso de "aparência de site institucional gerado" quando a composição não tem um elemento de assinatura visual próprio.
- Tomar decisão visual (não estrutural) apenas por descrição em texto, sem visualizar.

### Regra futura, antes de criar qualquer elemento visual novo
1. Verificar se existe um padrão real de mercado/referência pro problema.
2. Verificar se já existe skill/MCP/biblioteca que resolve melhor que desenhar na mão.
3. Analisar referências reais e concretas (não descrever de memória).
4. Decidir.
5. Implementar.
6. Visualizar (preview real, não assumir pelo código).
7. Registrar o aprendizado aqui antes de seguir pra próxima etapa.

Não reinventar componente que já tem solução melhor no design web moderno (ícone de marca, ícone de UI, tratamento de foto de produto, preloader).

---

## Rodada 3 — 20/09, auditoria e memória de processo (esta rodada — sem redesign)

**Problema:** depois de duas rodadas de execução, faltava uma auditoria honesta do estado atual (o que está ~80% aprovado vs o que precisa mudar) e um inventário real de produto/foto antes de qualquer nova rodada visual — inclusive corrigir uma possível inconsistência de contagem de modelos (3 vs 4) sem checar o material primeiro.

**Decisão:** só auditoria, inventário, pesquisa visual pequena e registro nesta rodada. Nenhuma linha de design foi alterada.

### Header

**Aprovado (~80%, confirmado pelo Diogo — não redesenhar):** estrutura fixa com topbar recolhível ao rolar, transição suave, nav com sublinhado animado, drawer mobile funcional.

**Precisa melhorar:**
- **Ícones sociais** (`f`, `ig`, `in` como texto dentro de círculo, em `index.html`/`nosotros.html`/`productos.html` header e footer) — são placeholder de texto, não ícone de marca real. Achado real de código, não suposição.
- **Tipografia do telefone na topbar** — hoje `<a href="tel:...">Llamar: +34 960 64 00 72</a>` inteiro em `--ff-mono` (`.topbar a{font-family:var(--ff-mono)}`). O label "Llamar:" não deveria estar em mono — só o número. É provavelmente essa mistura que o Diogo percebe como "ruim", não a fonte em si (mono já é a escolha certa pra número, ver `DESIGN_SYSTEM.md` seção 2).
- Facebook aponta pra `#` (link morto) nas 3 páginas — sobra do site oficial, não é decisão nova.

### Intro-gate

Conceito atual (diálogo "¿Té? ¿Jugo? ... Café. La Norma") pode continuar — é um gancho real e específico da marca, não genérico. Execução visual hoje: texto centralizado, fade+translateY simples, fundo liso com um radial-gradient sutil, sem elemento fotográfico.

**Pesquisa visual (pequena, referências reais e verificáveis, não copiar):**
- [Site intro — galeria Awwwards](https://www.awwwards.com/inspiration/site-intro-submission-64807e940c5aa094817353)
- [Intro transition — galeria Awwwards](https://www.awwwards.com/inspiration/intro-transition)
- [Preloader animation — Awwwards](https://www.awwwards.com/inspiration/preloader-animation-youssri-rahman-1)
- [Branded counter preloader — Awwwards](https://www.awwwards.com/inspiration/branded-counter-preloader-navbar-digital)

**Princípios extraíveis (não copiar layout nem texto):** reveal tipográfico letra-a-letra ao invés de fade em bloco inteiro; contador numérico 0→100 com overlay expansivo no lugar de um timer automático fixo (900ms/step hoje); preloader "type-first" (tipografia carrega o peso visual, não imagem) — o que já é parecido com o conceito atual, mas a execução pode ganhar mais peso tipográfico e uma transição de saída mais desenhada do que o fade atual. **Não fazer:** recriar como imagem/vídeo de fábrica que não existe no acervo (ver seção Fotografia abaixo).

### Topbar / telefone

Mesmo achado do Header — separar label do número na hierarquia tipográfica é o ajuste concreto (não precisa de nova pesquisa, é aplicação da própria regra já registrada em `DESIGN_SYSTEM.md`).

### Ícones

Achado de código: os únicos ícones "desenhados à mão" que já existem (telefone, email, Instagram, mapa no `.cta-band`) são SVG inline estilo linha fina, coerentes entre si — **esse padrão está bom, não precisa trocar**. O problema é só os 3 glifos de marca do header/footer sendo texto. Biblioteca real recomendada pra ícone de marca: **Simple Icons** (MIT, glifos de logo de marca — Facebook/Instagram/LinkedIn inclusos). Para ícone de UI genérico (se algum dia precisar de mais além do que já existe), **Lucide** é a opção mais madura e coerente com o traço fino já em uso (fork ativo do Feather Icons, MIT). Nenhuma das duas foi instalada nesta rodada — só registrada como recomendação.

### Produtos — inventário real

**Modelos oficialmente vendidos, confirmados no catálogo real (specs em `productos.html` e no handoff comercial `contexto/HANDOFF-lanorma-digital.md`): 3 — Compacta (8 L / 45 kg), 2 grupos (13 L / 65 kg), 3 grupos (20,5 L / 70 kg).** Não foi encontrada nenhuma quarta linha de produto documentada em specs, handoff ou proposta comercial.

**Achado real em `assets/biblioteca-wp-completa/`:** existe uma pasta `VASO ALTO/` com `2 GRUPO VASO ALTO.png`, e a pasta `GIF/` tem `MINI - VASO ALTO.gif` e `NEGRA MINI VASO ALTO.gif`. Isso confirma que **"vaso alto" é uma variante/configuração real** (folga de xícara maior sob o grupo), disponível pelo menos para Mini e 2 grupos — **não é um 4º modelo**, é uma opção dentro dos modelos existentes. Não há confirmação, em nenhum material do projeto, de "vaso alto" pra 3 grupos — não assumir que existe até confirmar.

> **AMPLIADO na Rodada 6 (20/09):** o Diogo confirmou que **vaso alto vale para os 3 modelos** (Compacta, 2 grupos e 3 grupos), não só Mini/2 grupos — é uma configuração escolhida na compra (como uma versão de carro), o desenho muda pouco, a proposta é copo pequeno de bar vs. copo grande tipo Starbucks. Adicionado como FAQ em `productos.html`. **Também confirmado nesta rodada:** essas 3 máquinas formam oficialmente a linha **"Ln1"** (nome usado nos arquivos de imagem `lanorma-ln1-coffee-machine-0X.jpg` e no material `contexto/propuesta-daniel-5slides.html`, mas nunca antes conectado ao termo "Ln1" com essa clareza). Os rótulos "Modelos en la gama" no `stat-strip` (index.html e productos.html) foram trocados pra **"Modelos Ln1"** — mais preciso, porque existe uma 4ª máquina real (ver abaixo) que essas 3 não cobrem.
>
> **Novo achado, ainda fora do site:** existe um lançamento real chamado **LN200**, já vendido pelo Diogo mas **ainda não integrado ao site principal** — vai ganhar campanha estratégica própria depois (não implementar agora, não citar specs/fotos dele em lugar nenhum do 4174 até essa campanha ser decidida). Existe um protótipo de landing separado em `ln200-site/` (visual verde/cinza, fontes Saira/IBM Plex Sans) que **é sim sobre esse mesmo produto** — antes registrado erroneamente como "fora de escopo" sem essa conexão. Cuidado: os arquivos `ln200-site/assets/ln1-blanco.jpg` e `ln1-negro.jpg` **não são fotos do LN200** apesar do nome parecido — são de outra coisa, confirmado pelo Diogo, não usar como referência do LN200. `ln200-site/assets/ln200.jpg` seria a foto certa a checar quando essa campanha for retomada.

**Achado de possível inconsistência visual, a confirmar antes da próxima rodada:** `assets/real/spec-compacta.jpg` e `assets/real/spec-2-grupos.jpg` foram comparadas lado a lado e mostram um render com a mesma configuração de 2 grupos de extração — visualmente muito parecidas ou idênticas. `assets/real/spec-3-grupos.jpg` está correta (mostra claramente 3 grupos). **Não dá pra confirmar com certeza, só olhando a imagem, que o modelo Compacta tem uma foto errada** (pode ser um render genérico de divulgação reaproveitado) — mas é uma bandeira real que vale checar contra `assets/biblioteca-wp-completa/MAQUINA FUNDO BRANCO/MINI BRANCA.png` (que também mostra a mesma configuração de 2 grupos, apesar do nome "MINI") antes de publicar qualquer coisa nova com essas imagens.

> **RESOLVIDO na Rodada 4 (20/09):** o Diogo, que monta as máquinas, confirmou que **a Mini/Compacta tem 2 porta-filtros**, igual à 2 grupos — a diferença entre os dois modelos é o corpo e a caldeira (8 L vs 13 L), não o número de grupos. **Não havia erro de foto.** Fica aberto só um detalhe secundário: a medida publicada da Compacta (485 × 564 × **530** mm) parece estreita demais pra uma máquina de 2 grupos. Esse dado é real, veio do site oficial, e **foi mantido como está** — corrigir por dedução seria inventar. Confirmar com o Daniel/no taller.

**Fundo branco/cinza das fotos de produto** apontado como fraco: o acervo tem pelo menos 3 tratamentos diferentes ainda não comparados com critério — fundo transparente/branco liso (`MAQUINA FUNDO BRANCO/`), fundo cinza de estúdio com sombra suave (`FUNDO CINZA/`, 6 fotos "lanorma-ln1-coffee-machine-0X.jpg") e os renders atuais em uso (`assets/real/spec-*.jpg`, fundo com gradiente CSS por cima). Nenhuma comparação de escala/recorte/sombra foi feita ainda — fica pra próxima rodada de execução, não decidir aqui.

### Personalização

**O Diogo confirmou nesta conversa** (não está documentado em nenhum arquivo do projeto) que as máquinas podem ter personalização de marca/nome do estabelecimento no frontal de inox, quando disponível. Não foi encontrada nenhuma foto, spec ou menção escrita disso em `contexto/` ou nos assets — **registrado como diferencial real, mas sem detalhe técnico confirmado ainda** (processo — gravação a laser? chapa impressa? adesivo? —, quais modelos suportam, custo, prazo). Não implementar no site antes de confirmar esses detalhes com o Daniel — risco de prometer algo tecnicamente errado.

### B2B-first, não B2B-only

Hipótese de posicionamento, apoiada em dado real do handoff comercial (`contexto/HANDOFF-lanorma-digital.md` seção 4): o comprador que decide de verdade é B2B (distribuidor, cafeteria, hotel, tostador), e a concorrência espanhola (Ascaso, Iberital, Quality Espresso) ocupa mal esse canal. Públicos reais já levantados no material: cafeterías, baristas, tostadores, microcafés, distribuidores, hotéis, "amantes de café que exigem nível profissional em casa" (este último já é copy real do `nosotros.html`, seção `.audience`). O site já fala parcialmente nesse tom (specs técnicas completas, suporte direto sem intermediário, FAQ de orçamento) — o que falta mapear numa próxima rodada é se **manutenção/suporte pós-venda** e **fabricação/processo** estão fáceis de achar (hoje "fabricación" só aparece na FAQ de `productos.html`, não como seção própria). Não implementar mudança de posicionamento agora, só registrar a hipótese.

### Fotografia — inventário por categoria

| Categoria | Arquivos reais | Observação |
|---|---|---|
| Hero | `hero-bg.jpg` (em uso), `hero-home.mp4` (fora de uso, ver Rodada 2) | Composição atual aprovada na Rodada 2; não reavaliar sem motivo novo. |
| Produto (render estúdio) | `spec-compacta.jpg`, `spec-2-grupos.jpg`, `spec-3-grupos.jpg` (em uso); `MAQUINA FUNDO BRANCO/*`, `FUNDO CINZA/*`, `VASO ALTO/*`, `ICON MAQUINA PLAN/*` (não usados) | Ver achado de possível inconsistência acima; comparação de fundo pendente. |
| Detalhe/macro | `nosotros-02.jpg` (extração, em uso) | Único macro em uso; `especificaciones.jpg` é diagrama técnico, já em uso em `productos.html`. |
| Café/processo | `nosotros-30/50/82/87.jpg` (em uso no `about-strip` e workshop-block) | Todas são macro de extração/latte art/oficina, não linha de montagem — ponto já registrado no `PROJECT_BRAIN.md` ("Pontos a confirmar"). |
| Pessoas | `nosotros-cabecera.jpg` (em uso — equipe real no mostrador); `ig-1.jpg`…`ig-6.jpg` (não usados no site atual, vêm do carrossel de Instagram que saiu do fluxo principal na Rodada 2) | `ig-1.jpg` é uma foto de barista com boa luz/composição (vapor, ambiente real) — candidata a reforço de "pessoas" numa próxima rodada, mas confirmar com o Diogo se é foto própria da La Norma antes de promover pra um lugar de destaque (veio do carrossel de Instagram, origem exata não confirmada nesta auditoria). |
| Equipe | `nosotros-cabecera.jpg` | Mesma foto da categoria "pessoas" — é a única foto de equipe reconhecível no acervo hoje. |
| Diagramas | `especificaciones.jpg` (em uso); `diagrama-compacta.png`, `diagrama-2-grupos.png`, `diagrama-3-grupos.png` (não usados, ver `PROJECT_BRAIN.md`) | Diagramas por modelo existem e não são usados — oportunidade real pra reforçar a ficha de cada produto individualmente. |
| Outras | `logo.png` (não usado, `logo-lanorma.png` é o que está em uso) | Confirmar se `logo.png` é redundante ou uma variante diferente antes de descartar. |

Nenhuma imagem externa foi copiada pro projeto — todas as opções acima já existem no acervo local.

### Novas possibilidades — registradas, não implementadas

- **Formación:** empresa oferece cursos segundo informação que temos, mas não está no site oficial nem documentada em detalhe no material do projeto. Não implementar até confirmar com o Daniel: quais cursos, público, formato, local, frequência, responsável, material/fotos.
- **Conteúdo/notícias:** possibilidade futura de área editorial sobre o mundo do café. Não implementar sem antes confirmar se existe estratégia sustentável de atualização e quem seria responsável — seção vazia por trás de um menu "Notícias" já existe no site oficial hoje e é apontada como problema no handoff comercial (`contexto/HANDOFF-lanorma-digital.md` seção 3, item 2), não repetir esse erro no 4174.

### Fila de priorização — próxima rodada

> Status depois da Rodada 4: **P0 fechado por inteiro** (itens 1–4), mais os itens 5, 6 e 7 do P1. Resta o item 8 do P1 e todo o P2/P3.

**P0 — obrigatório pra próxima apresentação**
1. Separar label "Llamar:" do número na topbar (mono só no número).
2. Trocar os 3 ícones sociais de texto (`f`/`ig`/`in`) por glifos reais de marca (Simple Icons) no header e no footer.
3. Confirmar se `spec-compacta.jpg` é de fato a foto certa do modelo Compacta antes de reaproveitá-la em qualquer lugar novo.
4. Corrigir o link morto do Facebook (`href="#"`) ou remover o ícone até existir uma página real.

**P1 — melhoria visual de alto impacto**
5. Comparar com critério os 3 tratamentos de fundo disponíveis pra foto de produto (branco liso / cinza estúdio / gradiente CSS atual) e escolher um só.
6. Repensar a execução visual do intro-gate mantendo o conceito, usando os princípios extraídos da pesquisa (reveal tipográfico mais forte, transição de saída mais desenhada).
7. Reavaliar `.product-card` em `productos.html` contra o mesmo critério que já tirou o padrão de card genérico dos `.pillars` (ver `DESIGN_SYSTEM.md` seção 10).
8. Padronizar a ordem palavra/span dos `.principle` entre `index.html` e `nosotros.html` (pendência da Rodada 2).

**P2 — melhoria comercial/estratégica**
9. Levar pro Daniel as perguntas técnicas da personalização de frontal inox (processo, modelos suportados, custo/prazo) e só então registrar como seção do site.
10. Mapear se "fabricación/processo" e "suporte pós-venda" merecem virar seção própria (hoje só aparecem na FAQ), como parte da hipótese B2B-first.
11. Decidir se "vaso alto" vira uma linha extra dentro da ficha técnica de Mini/2 grupos (não como 4º modelo).
12. Confirmar a origem de `ig-1.jpg` (e das demais `ig-*.jpg`) antes de promovê-las a um lugar de destaque no site.

**P3 — funcionalidades futuras, não implementar agora**
13. Seção "Formación" — pendente de confirmação de conteúdo com o Daniel.
14. Área editorial/notícias — pendente de estratégia de manutenção sustentável.
15. Cine-scroll ou animação de página inteira.

**Resultado desta rodada:** nenhuma linha de design foi alterada. Auditoria, inventário e pesquisa registrados aqui e em `DESIGN_SYSTEM.md`.

**Aprendizado:** boa parte do que parecia "decisão a tomar" (quantos modelos existem, se personalização é real, o que já está aprovado no header) já tinha resposta no próprio material do projeto ou na memória do Diogo — só não tinha sido puxado e registrado num lugar só antes de começar a mexer em código.

**O que não repetir:** already covered — não abrir uma rodada de implementação visual nova sem primeiro checar se a pergunta já tem resposta no material existente (regra futura, seção acima).

**Próxima hipótese:** com a fila de priorização acima, a próxima rodada de execução deveria atacar o P0 inteiro primeiro (é pequeno e mecânico) antes de abrir qualquer decisão visual maior de P1.

---

## Rodada 4 — 20/09, acabamento perceptível (intro, produto, topbar, ícones)

**Problema:** o site já tinha estrutura e identidade, mas quatro pontos pequenos derrubavam a percepção de acabamento: a intro parecia feita do zero, as fotos de produto eram as piores imagens do acervo dentro de cards genéricos, o telefone da topbar tinha tipografia errada e os ícones sociais eram letras (`f`, `ig`, `in`) em vez de ícones.

**Hipótese:** dá pra mudar a percepção sem redesign — trocando a matéria-prima (imagem melhor), tirando a moldura (card) e corrigindo os detalhes que o olho registra como "amador".

**Referências e princípios aplicados:** as galerias de intro/preloader registradas na Rodada 3. Princípios extraídos, não copiados: reveal tipográfico em vez de fade de bloco; saída desenhada (cortina) em vez de sumir; marca carregando o peso visual em vez de imagem.

### O que mudou

**1. Intro-gate — conceito trocado, a pedido do Diogo.** A sequência "¿Té? ¿Jugo? … Café." saiu. Motivo concreto: **obrigava a clicar em "Café." pra entrar** e levava ~4,5s. Entrou uma abertura de marca: wordmark real revelado por máscara → a linha real da marca (*«Una forma distinta de preparar un café»*, copy que já existia no rodapé) → cortina sobe e **o wordmark desliza até a posição exata do logo no header**, calculada em runtime com `getBoundingClientRect`. Total ~2,1s, sem clique. Mantidos: Saltar, Esc, sessionStorage (chave nova `ln_intro_v2`), offline. Adicionado `prefers-reduced-motion` (estático, 0,6s).

**2. Bug real corrigido de quebra:** a intro antiga chamava `sessionStorage.getItem` sem proteção. Em contexto de origem opaca (arquivo local/aba privada) isso **lança SecurityError**, o script morria antes de fechar o portão e **o site ficava coberto pra sempre**. Agora está em try/catch, e a intro só existe se o JS rodar (`html.js` no CSS) — sem JS, o site abre direto. Testado num contexto onde o `sessionStorage` realmente lança: a intro abre, fecha e libera a página.

**3. Fotos de produto refeitas a partir do acervo.** As `spec-*.jpg` em uso eram frames de GIF de 1080×1080 com 46–71 KB. Foram substituídas por recortes gerados dos renders originais de 1920×1080 (`MAQUINA FUNDO BRANCO/`), com fundo removido por *flood fill* a partir das bordas — algoritmo escolhido de propósito porque o corpo da máquina é branco e uma remoção por limiar global comeria a própria máquina. Feather de 1px nas bordas, corte na bounding box e saída em WebP: **de ~620 KB para 62–94 KB por imagem**, com o dobro da resolução. Nenhuma imagem externa, nenhuma imagem gerada, nenhum fundo inventado — só o branco chapado removido.

**4. Apresentação de produto: card → composição.** No catálogo, os 3 `.product-card` viraram `.machine`: máquina grande sobre o fundo claro, sem moldura, posição alternando lado a lado, sombra elíptica suave no chão pra dar contato, specs em lista com régua e valores em mono alinhados à direita, e um hover discreto de 8px. Mesmo tratamento no zig-zag da home (saiu o painel com gradiente e borda).

**5. Topbar.** `Llamar: +34 960…` estava inteiro em mono. Agora "Llamar" é label em Archivo, micro e mutado, e só o número é mono, em brass, com sublinhado no hover. Em telas ≤600px o label some e fica só o número.

**6. Ícones sociais.** As letras viraram os glifos oficiais de marca do **Simple Icons** (CC0), buscados da fonte e embutidos num sprite SVG por página (`<symbol>` + `<use>`), o que funciona offline e não repete o path 6 vezes. Os círculos do header foram mantidos — o header estava ~80% aprovado e não era pra redesenhar. O Facebook, que apontava pra `#`, agora aponta pra página real que o Diogo passou.

**Resultado:** testado no navegador em desktop (1280) e mobile (375), nas 3 páginas: 0 imagem quebrada, 0 erro de console, sem overflow horizontal real (os 4px acusados no mobile são a barra de rolagem emulada afetando o header fixo, não conteúdo), layout alternado funcionando, lazy-load carregando ao rolar, e o site abrindo normalmente como arquivo local.

**O que funcionou:** trocar a matéria-prima antes de mexer no layout — metade do ganho de percepção veio só da imagem melhor. E usar biblioteca real de ícone de marca em vez de desenhar: resolveu em minutos um item que vinha arrastando há rodadas.

**O que não funcionou tão bem:** a captura de tela do navegador embutido compõe errado quando o viewport emulado é maior que o painel — várias fotos saíram com só um pedaço da tela renderizado. A medição por JS (`getBoundingClientRect`, `getComputedStyle`) foi o que deu confiança de verdade. Vale lembrar disso na próxima rodada: **conferir layout por medida, usar screenshot só como ilustração.**

**O que não repetir:** deixar `sessionStorage` (ou qualquer API que pode lançar) sem try/catch dentro de algo que cobre a tela inteira. Um erro silencioso ali derruba o site inteiro pro visitante, e isso ficou no ar sem ninguém notar desde a Rodada 1.

**Próxima hipótese:** os dois pontos que mais devem pesar agora são o item 8 do P1 (padronizar a ordem palavra/span dos `.principle`) e o P2 comercial — confirmar com o Daniel os detalhes da personalização de frontal inox e a medida da Compacta. Do lado visual, a hero é o maior bloco ainda intocado desde a Rodada 2.

---

## Rodada 5 — 20/09, hero full-bleed e intro final (via `/grill-with-docs`)

**Problema:** dois itens específicos apontados pelo Diogo depois de ver a Rodada 4 no ar — a hero, mesmo aprovada estruturalmente na Rodada 2, "continua sem cara de hero"; e a intro (já refeita na Rodada 4) tinha uma frase e uma fonte que ele não gostou ao ver de verdade.

**Processo:** sessão de grilling (`mattpocock-skills:grilling` + `domain-modeling`) em vez de implementar direto — perguntas em rodadas, com opções, até fechar decisão. Cross-referenciado contra o código antes de perguntar (ex.: o Diogo achava que faltava "o logo oficial" na intro; o código já usava o arquivo oficial, só filtrado de branco — a percepção era sobre o tratamento, não sobre faltar o arquivo).

### Hero — decisão final: full-bleed com foto nova, fornecida pelo Diogo nesta sessão

**Hipótese testada e descartada, com motivo registrado:** full-bleed com `hero-bg.jpg` (o barista com vapor, já aprovado na Rodada 2 para o painel contido) não funciona em tela cheia — o título cobria o rosto da pessoa. Testado também full-bleed com `nosotros-cabecera.jpg` (foto real do mostrador, dois homens) com um scrim reforçado em duas direções (vertical + diagonal); mesmo assim o texto cruzava o rosto do segundo homem. **Decisão de princípio que fica registrada:** não cobrir rosto de pessoa real com texto, mesmo que o scrim resolva o contraste — decidido incorreto pra uma marca que quer mostrar "pessoas de verdade".

**Resolvido com fotos novas do Diogo:** duas fotos macro do próprio display digital da máquina (temperatura + hora + **a palavra "Lanorma" acesa no visor**), sem nenhuma pessoa no quadro, com grande área negra real (não é vinheta CSS — é o fundo real da foto). Usada a mais forte das duas (`assets/real/hero-display.jpg`, salva a partir do arquivo que o Diogo mandou, redimensionada pra 2400px). Resolve os 3 problemas relatados de uma vez: domina a tela (full-bleed de verdade), não repete nenhum padrão de outra seção do site, e tem assinatura visual própria (a marca já está literalmente escrita na cena, não precisa ser adicionada).

**Implementação:** `.hero` deixou de ser grid de 2 colunas — virou `<img class="hero-bg">` em `position:absolute` cobrindo a seção, com dois gradientes sobrepostos (vertical de baixo + diagonal da esquerda) em vez de um só, porque um gradiente só não dava contraste suficiente pro texto em cima da foto. `object-position` diferente por breakpoint: `48% 48%` no desktop (mostra "115°C" e o início de "Lanorma" no visor), `62% 40%` em ≤600px (testado de verdade em viewport 375×812 — sem corte, CTA visível sem rolar). `.hero-panel`/`.hero-grid`/`.hero-copy` removidos do CSS (confirmado por grep que nenhuma página ainda referenciava).

**Fotos descartadas nesta rodada, registradas pra não serem retestadas à toa:** `LaNorma_Alta-69` (ambiente real de torrefação, boa foto mas maria confusa pra hero — guardada como candidata pra seção de processo/fabricação); `ig-1.jpg` (na real é a mesma foto/estilo de `LaNorma_Alta-01`, macro de extração — redundante com o que já existe, não é achado novo).

### Intro — decisão final: sem linha de assinatura embaixo, só eyebrow + wordmark

**O que mudou desde a Rodada 4:** a Rodada 4 tinha adicionado uma linha (`Una forma distinta de preparar un café`, cópia real do rodapé) embaixo da wordmark, em itálico Fraunces. O Diogo não gostou nem da frase nem da fonte ao ver publicado.

**Testado ao vivo, 4 tratamentos de fonte pra essa linha** (mantendo a frase trocada por outra também real, da meta description: `Máquinas de café profesionales, ensambladas a mano en Valencia`): itálico Fraunces (original, rejeitado), Fraunces reto, Archivo em caixa alta (rejeitado por repetir exatamente o tratamento do eyebrow acima — redundante), IBM Plex Mono em brass (o preferido, mas não fechado). **Decisão final do Diogo: tirar a linha inteira.** A estrutura final é eyebrow (`Fabricante de máquinas de café · Valencia`) + wordmark grande — mais seca, sem "poema".

**Também fechado nesta rodada:** a wordmark passa a ser preenchida em `--brass-light` via `mask-image` (technique igual ao logo do header, mas recolorida) em vez de branca — usa a cor de marca em vez de um branco genérico, seguindo a mesma regra de "um único acento controlado" que já rege o resto do sistema. E foi adicionada uma textura de fundo (`assets/real/intro-texture.jpg`, um crop desfocado e escurecido do próprio `hero-bg.jpg`, focado na área do vapor) atrás do texto — sutil, real, sem competir com a leitura.

**Pesquisa pequena feita:** 4 galerias reais do Awwwards (site-intro, intro-transition, preloader-animation, branded-counter-preloader) já registradas na Rodada 3 — usadas de novo aqui pra confirmar o princípio "tracking largo + caixa alta + restrição" (fonte: comparação de wordmarks de marca, ver referência no texto da pergunta ao Diogo) em vez de repetir a mesma pesquisa.

### Bug real achado e corrigido nesta rodada

Depois de editar o CSS, o navegador continuou servindo a versão antiga por cache (`style.css?v=10` não tinha mudado) — as mudanças não apareciam mesmo com o arquivo correto no disco. **Corrigido subindo pra `?v=11`** nas 3 páginas. Registrar como hábito: **sempre subir o `?v=` do CSS depois de editar, antes de testar** — já tinha acontecido antes (`TOOLS.md`/handoffs mencionam isso), mas vale repetir aqui porque quase gerou um relatório errado ("a mudança não funcionou" quando na verdade era cache).

**Resultado:** testado em desktop (1280) e mobile (375×812) — 0 erro de console, 0 overflow, hero e intro corretos nos dois, CTA sempre visível sem rolar no mobile.

**O que funcionou:** grillar com perguntas de múltipla escolha antes de implementar economizou pelo menos 2 rodadas de "implementei, você não gostou, refaço" — o Diogo conseguiu reagir rápido a opções concretas em vez de descrever o que queria em texto (mesmo padrão já registrado como aprendizado na Rodada 2). Também funcionou pedir foto nova quando as duas opções existentes falharam no mesmo teste (cobrir rosto) — em vez de forçar uma das duas ruins, voltar e perguntar "tem outra?" trouxe a melhor foto da rodada inteira.

**O que não funcionou tão bem:** gastei 3 tentativas de crop tentando fazer `hero-bg.jpg` e depois `nosotros-cabecera.jpg` funcionarem em full-bleed antes de admitir que nenhuma das duas tinha espaço negativo real — deveria ter testado a hipótese "essa foto tem espaço vazio suficiente?" antes de escrever o CSS de scrim, não depois.

**O que não repetir:** editar CSS/HTML e testar sem subir o cache-bust — quase levou a diagnosticar errado uma mudança que na verdade tinha funcionado.

**Próxima hipótese:** os itens novos que o Diogo trouxe no fim desta rodada (paleta de cor questionada — o brass não existe nas máquinas reais; possível redesenho do material de apresentação/slides pra vender junto; e uma menção não confirmada sobre "curso no cabeçalho") ficam registrados como abertos, não decididos — precisam de uma rodada de grilling própria antes de qualquer implementação, porque cada um sozinho já é uma mudança grande.
