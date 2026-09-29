# Sistema de produção — auditoria e arquitetura de trabalho

**Data:** 28/09/2026 · **Escopo:** como este projeto é produzido, não o que ele contém.
**Status:** diagnóstico e recomendação. **Nada aqui foi implementado.**

Regra que governa o documento inteiro: **mais MCP, skill ou plugin não é melhor.** Toda
recomendação carrega o custo ao lado do benefício, e "manter como está" é uma conclusão
legítima. Ferramenta que não resolve uma dor observada neste projeto não entra, por mais
sofisticada que pareça.

---

## 1. Inventário verificado

Levantado por execução, não por leitura de documentação. "Instalado" não é "funciona".

### 1.1 Modelos

| Papel | Modelo | Onde já se usa |
|---|---|---|
| Decisão, pesquisa, direção visual, spec | Opus 5 | esta sessão e todas as rodadas de design |
| Execução delimitada | Sonnet 5 / Haiku 4.5 | via subagentes; `caveman` já registrado no Brain §9 como ferramenta de execução mecânica |
| Subagentes disponíveis | Explore, Plan, general-purpose + os dos plugins | Explore/Plan usados nas rodadas de planejamento |

### 1.2 MCPs — estado real

| Servidor | Estado verificado | Consequência prática |
|---|---|---|
| **GitHub** | **falha** — "Authorization header is badly formatted" | sem leitura de Actions, PR ou issue por MCP |
| Google Drive, Gmail, Calendar, Slack, Dropbox, Figma, Supabase, Docs, Higgsfield | conectados (conectores da conta claude.ai) | Drive é o que resolve a renderização do `.pptx` |
| `details` | exige OAuth, sessão não-interativa | indisponível |
| browser-use, definite (plugins) | falham ao conectar | irrelevantes aqui — o browser embutido cobre |
| ccd_* (session, pr, view, sidebar…) | ok | infraestrutura do app, não do projeto |
| Claude_Browser (embutido) | ok | eixo do Visual QA: screenshot, console, rede, viewport, leitura de página |
| claude-in-chrome / computer-use | ok | Chrome real do Diogo e desktop, sob permissão |

Configurados localmente em `~/.claude.json`: só `github` (quebrado) e `details` (sem auth).
Todo o resto vem da conta claude.ai ou do próprio app.

### 1.3 Ferramentas de linha de comando

| Ferramenta | Estado | Observação |
|---|---|---|
| git | ok | remoto `DiogoTorresWeb/la-norma-preview-teste-`, branch `redesign-visual-16-09` |
| **gh CLI** | **ausente** | somado ao MCP quebrado: **não há como ver se o deploy do Pages passou** |
| node 24 / npm / npx | ok | permite rodar auditoria sem instalar nada permanentemente |
| python 3.12 + `python-pptx` + `pillow` | ok | gerador do deck funciona |
| ffmpeg, yt-dlp | ok | vídeo e legenda |
| **ImageMagick** | **ausente** | o `convert` que aparece no PATH é o `convert.exe` do Windows (converte sistema de arquivos) — **armadilha**, não usar |
| PowerPoint / LibreOffice | ausentes | por isso o `.pptx` nunca foi conferido |
| lighthouse, axe, pa11y, playwright | ausentes | **Performance QA e Accessibility QA hoje são zero** |
| `opencli` 1.8.7 | instalado, extensão não conectada | por isso `agent-reach` só responde YouTube |

### 1.4 Skills, plugins, hooks

- **28 skills de usuário**, das quais ~15 são variações de "não deixe a UI genérica"
  (`gpt-taste`, `high-end-visual-design`, `stitch-design-taste`, `minimalist-ui`,
  `industrial-brutalist-ui`, `design-taste-frontend` v1 e v2, `impeccable`,
  `image-to-code`, `brandkit`, `emil-design-eng`, `apple-design`, `redesign-existing-projects`…).
- **7 marketplaces de plugin ativos**: example-skills, mattpocock, claude-seo, superpowers,
  ponytail, caveman, watch. Juntos somam centenas de skills e dezenas de subagentes.
- **2 comandos próprios**: `/professor` e `/insta`.
- **Nenhum hook configurado** — nem de usuário, nem de projeto.
- `.claude/launch.json` do projeto está correto e específico (portas 4174 e 4176).

**Custo escondido:** a lista de skills e agentes disponíveis é injetada no contexto de
**toda** sessão. Plugin ligado que nunca é acionado não é neutro — é imposto fixo de contexto.

### 1.5 As lacunas reais

1. **Não se sabe se o deploy passou.** O `.github/workflows/deploy-pages.yml` tem uma trava
   que falha o build se material interno vazar pro Pages — e é exatamente essa trava cujo
   resultado ninguém consegue ler hoje. É a lacuna mais grave: silenciosa e com risco.
2. **Zero verificação objetiva.** Nenhuma medição de performance, contraste ou acessibilidade
   jamais rodou neste projeto. Todo "está bom" é visual e subjetivo.
3. **Content QA é manual e é a trilha que já custou caro** (depoimentos inventados removidos
   do site do Paulo). Nenhuma ferramenta cobre isso.
4. **Documentação vazando** — arquivos afirmando coisas que o código já desmentiu (§5).

---

## 2. Ferramentas candidatas

Critério: resolve uma das lacunas acima, neste projeto, agora.

| Candidata | Função | Benefício real aqui | Custo | Complexidade | Contexto | Frequência | Etapa | Veredito |
|---|---|---|---|---|---|---|---|---|
| **`gh` CLI** | GitHub por linha de comando | fecha a lacuna nº 1: ver se o deploy e a trava anti-vazamento passaram | grátis | baixa (winget + login) | nenhum (é Bash) | toda sessão com push | Fase 5 | **adotar já**, permanente |
| **`npx lighthouse`** | performance, boas práticas, SEO | primeira medição objetiva do site; o deck afirma "35 → 99" e hoje isso não é reverificável | grátis | nula (npx, sem instalar) | só o resumo que se pedir | por rodada | Performance QA | **adotar já**, sob demanda |
| **`npx @axe-core/cli`** | acessibilidade automatizada | contraste real do brass sobre foto, alvo de toque, ordem de foco | grátis | nula (npx) | baixo | por rodada | Accessibility QA | **adotar já**, sob demanda |
| **Git hook `pre-push`** | roda a trava anti-vazamento local | impede publicar material interno **antes** do push, em vez de descobrir depois | grátis | baixa (~15 linhas) | zero | automático | Fase 3 | **adotar já**, permanente |
| chrome-devtools-mcp | trace de performance no Chrome real | o README oficial cobre trace, rede e debug; **não promete auditoria de acessibilidade** (resultados de busca que afirmam isso contradizem a fonte) | grátis | média (MCP permanente, exige Chrome) | **alto — 29 ferramentas no contexto** | rara | — | **não adotar agora**: site estático de 4 páginas, performance não é a dor, e sobrepõe o browser embutido |
| BackstopJS / Playwright screenshot | regressão visual | pegaria quebra não intencional entre rodadas | grátis | média-alta (baseline + rotina) | médio | — | — | **não adotar agora**: o design **muda de propósito** toda rodada; baseline que muda toda semana vira ruído. Reavaliar quando o visual congelar |
| Mobbin | biblioteca de padrões de UI | referência de app, não de site institucional | pago | — | — | — | — | **não adotar**: fora do tipo de produto, e bloqueia leitura automatizada (403 verificado) |
| Figma MCP | design ↔ código | o projeto não tem arquivo de design; a fonte da verdade é o CSS | conectado | média | alto | nunca até hoje | — | **não adotar**: resolveria um fluxo que não existe aqui |
| Suíte `claude-seo` | auditoria e conteúdo SEO | hoje o site é institucional de 4 páginas sem estratégia de conteúdo | grátis | alta (dezenas de agentes) | **alto** | — | — | **adiar**: reavaliar **depois da Fase 4**, quando existir blog real — e mesmo então usar só `seo-page` e `seo-content`, nunca a suíte inteira |

**O padrão que emerge:** o que vale a pena é quase tudo CLI sob demanda, não MCP permanente.
MCP custa contexto em toda sessão; `npx` custa contexto só na sessão em que roda.

---

## 3. Fontes de referência visual

O acesso foi testado, porque "a fonte é boa" não importa se o agente não consegue lê-la.

| Fonte | Leitura automatizada | Serve para |
|---|---|---|
| Typewolf | **livre e completa** | tipografia em sites reais, pares de fonte, alternativas — a mais diretamente útil |
| SiteInspire | **livre**, com filtros por estilo/tipo/assunto | achar o vizinho estrutural certo ("Typographic", "Minimal", "Agencies") |
| Awwwards | **livre**, mostra autor, prêmio e link vivo | ver o site real, não o mockup |
| recent.design | **livre** | **`godly.website` redireciona pra cá** (301) — a fonte da lista original mudou de nome |
| Dribbble | **falha em leitura direta** (retorna vazio) | precisa do browser embutido, ou do Diogo mandando o link |
| Mobbin | **403** | inacessível ao agente, e é biblioteca de app |
| Behance, Lapa Ninja, Motionographer | não testados nesta rodada | testar antes de entrarem no fluxo |

### O pipeline, e por que ele existe

```
REFERÊNCIA → OBSERVAÇÃO → PRINCÍPIO → DECISÃO → SPEC → IMPLEMENTAÇÃO
```

O projeto já provou os dois extremos, e essa é a evidência mais valiosa que temos:

- **Funcionou:** as 4 referências que **o próprio Diogo** achou (Brain §7) geraram reação
  real e viraram estrutura de página.
- **Falhou:** três hipóteses de estilo completas e depois nove referências "cinematográficas"
  **servidas pela IA** foram rejeitadas em bloco, sem escolha.

A conclusão não é "a IA escolhe mal". É que **referência escolhida pela IA chega como
proposta de estética**, e estética não se aprova por catálogo. Referência escolhida pelo
Diogo chega com a reação já embutida — o trabalho da IA começa depois, em extrair o princípio.

**Regras que isso fixa:**

1. Quem escolhe a referência é o Diogo — ou a IA busca **contra um princípio já nomeado**
   ("preciso de ritmo claro/escuro alternado"), nunca "achei 9 sites bonitos".
2. Máximo 3 por rodada, cada uma com **uma observação escrita** antes de qualquer código.
3. O que atravessa pro projeto é o **princípio**, nunca o traço visual. "Tipografia gigante
   sobre foto macro" é princípio; a fonte e a foto daquele site não atravessam.
4. Nenhuma referência entra sem passar pela trava do `DESIGN_SYSTEM.md` §14 (padrões
   rejeitados) — foi assim que o grid de 3 cards e o terracota `#D97757` foram barrados.

---

## 4. Arquitetura Opus → executor → QA → revisão

### Quando compensa

Quando **a decisão já foi tomada e o trabalho é volumoso**: aplicar um padrão em várias
páginas, gerar variações dentro de limites fechados, refatorar, produzir conteúdo repetitivo
a partir de um molde aprovado. O ganho vem de a decisão estar congelada numa spec — não de o
modelo executor ser bom.

### Quando não compensa

- **Tarefa pequena.** Se escrever a spec custa mais que fazer, faça. Trocar uma cor, corrigir
  um texto, ajustar um `scroll-margin-top`.
- **Tarefa exploratória.** Não dá pra especificar o que ainda não foi decidido. A Rodada 6
  testou 4 variantes de CTA **ao vivo** com o Diogo e as 4 foram rejeitadas — nenhuma spec
  teria previsto isso, porque a resposta era a reação dele.
- **Quando o critério de aceitação é "o Diogo tem que gostar".** Aí não existe verificação,
  existe apresentação.

### Critério de corte por modelo

| Exige o modelo de maior capacidade | Pode descer de modelo |
|---|---|
| direção criativa e escolha de referência | aplicar spec fechada, com limites explícitos |
| decisão visual sem resposta certa (paleta, hero, ritmo) | refactor mecânico, renomear, mover |
| motion e interação — "certo" é julgamento, não medida | gerar N variações dentro de restrições dadas |
| arquitetura de informação e estrutura de página | conteúdo repetitivo a partir de molde aprovado |
| qualquer coisa que o Diogo vá aprovar ou rejeitar por reação | verificação objetiva (mede e reporta) |
| redação que carrega a regra de honestidade | conversão de formato (HTML → pptx, etc.) |
| **revisão crítica da implementação** | — |

A revisão final volta pro Opus por um motivo específico: o executor entrega o que a spec
pediu; só quem tomou a decisão sabe se o que a spec pediu era o que a decisão queria dizer.

**Instância que já existe:** `caveman` está registrado no Brain §9 exatamente nesses termos —
execução mecânica delimitada sim, direção não, e **sempre revisar o diff depois**. A
arquitetura generaliza; o que faltava era a spec (§6).

---

## 5. Sistema de contexto e documentação

### O que existe, e o que cada um deve ser

| Arquivo | Papel | Estado | Ação |
|---|---|---|---|
| `CLAUDE.md` (raiz da base) | regras da diogo-base | saudável, curto | manter |
| `PROJECT_BRAIN.md` | **decisão, estado, próximo passo** | 25 KB, com diagnóstico longo dentro — contra a regra que ele mesmo declara no §12 | **enxugar**: narrativa de rodada vai pro EVOLUTION_LOG, ficam decisão e backlog |
| `DESIGN_SYSTEM.md` | o que já está aprovado, em forma prática | **o melhor arquivo do conjunto** — tem inclusive a lista de padrões rejeitados | manter e continuar alimentando |
| `EVOLUTION_LOG.md` | histórico por rodada e o porquê | 37 KB — grande demais para leitura integral | manter, **com índice de rodadas no topo**; lê-se por rodada, nunca inteiro |
| `TOOLS.md` | aprendizado sobre ferramenta | manter | registrar os achados do §1 |
| `README.md` | entrada do repositório | cita arquivo que não existe mais | corrigir |
| `contexto/` | material da reunião de setembro | **é arquivo histórico, não fonte** | marcar como histórico no topo de cada arquivo |
| `apresentacao-daniel/README.md` | folha de cola da reunião | descreve identidade de **duas rodadas atrás** ("preto+cobre") | reescrever (Fase 5) |
| `materiais/README.md` | decisões das peças | diz "não verificado" sobre o `.pptx` | atualizar depois da Fase 2 |

### Regra de precedência (não existia; passa a existir)

1. **Estilo** → `DESIGN_SYSTEM.md` manda.
2. **Estado, decisão e o que fazer agora** → `PROJECT_BRAIN.md` manda.
3. **Por que foi decidido assim** → `EVOLUTION_LOG.md`.
4. **Ferramenta** → `TOOLS.md`.
5. Qualquer outro arquivo que contradiga os quatro acima **está desatualizado por definição**
   e deve ser corrigido, não obedecido.

### Sobre criar `TASKS`, `CURRENT_STATUS`, `specs/`

**Não criar `TASKS` nem `CURRENT_STATUS`.** O backlog vive na seção 13 do Brain, numerado,
com o que está feito riscado e o motivo de cada pendência. Funciona. Um arquivo a mais seria
uma segunda verdade sobre o mesmo assunto — que é exatamente a doença diagnosticada acima.
Fica registrado aqui para a pergunta não voltar.

**`specs/` cria-se quando houver a primeira spec de verdade**, não antes. Pasta vazia é
convite a preenchimento cerimonial.

**`pesquisa/`** (esta pasta) é legítima porque tem dono claro: material com fonte externa e
data, que não é decisão nem estilo. **Nunca vai pro Pages** — ver §8.

---

## 6. Formato de Design Spec

Serve para transformar uma decisão do Opus em instrução executável por outro modelo, sem que
ele precise entender por que a decisão foi tomada.

### Template

```markdown
# SPEC — <nome curto do componente ou seção>
Rodada: <n> · Decidido por: <quem> · Arquivos: <caminhos exatos>

## Intenção
Uma frase: o que essa peça deve fazer com quem olha. Não descreve aparência.

## Hierarquia
Ordem de leitura pretendida, do primeiro ao último elemento. O que domina, o que serve.

## Comportamento
O que acontece em uso: clique, rolagem, carga, erro, ausência de JS, offline.

## Motion
Gatilho → propriedade → duração → curva. E o que acontece com `prefers-reduced-motion`.

## Tipografia
Família, peso, tamanho (com clamp se fluido), altura de linha, caixa — por papel, não por
elemento solto.

## Espaçamento
Ritmo vertical, respiro interno, alinhamento ao grid existente.

## Responsividade
O que muda em cada breakpoint já existente. Breakpoint novo precisa de justificativa.

## Limites — NÃO ALTERAR
Lista fechada: tudo que está fora da spec e não pode ser tocado de passagem.

## Critérios de aceitação
Lista verificável. Cada item respondível com sim ou não por quem não participou da decisão.
```

### Exemplo preenchido — a hero da Rodada 7 (spec retroativa, caso real)

```markdown
# SPEC — Hero da home + saída da intro
Rodada: 7 · Decidido por: Diogo (reação) + Opus (tradução) · Arquivos: index.html, css/style.css

## Intenção
A primeira tela tem que parecer uma hero de verdade, e a intro tem que entregá-la — as duas
telas são um movimento só, não duas coisas coladas.

## Hierarquia
1. foto (display da máquina, "Lanorma" aceso) · 2. título · 3. parágrafo ·
4. dois botões de mesmo peso · 5. seta que leva à barra de números.

## Comportamento
A intro roda uma vez por sessão, sai sozinha, aceita clique em qualquer lugar, tem Saltar e
Esc, e failsafe por timeout. Sem JS, a intro não existe e o site abre direto. A seta rola até
a barra de números com `scroll-margin-top` suficiente pro header fixo não cobrir a primeira
linha.

## Motion
Saída da intro: cortina `translateY(-101%)` em 620ms, wordmark deslizando até a posição real
do logo no header (calculada em runtime) → dispara `.hero.is-revealed`, que revela o conteúdo
da hero em cascata. Com `prefers-reduced-motion`, tudo estático.

## Tipografia
Título em Archivo bold (sans — decidido na Rodada 6, **não** Fraunces). Parágrafo em Archivo
regular. Números da barra seguinte em IBM Plex Mono.

## Espaçamento
Hero ocupa `100dvh`, conteúdo centrado verticalmente. Degradê inferior funde a seção na cor da
barra de números — sem costura visível entre as duas.

## Responsividade
Breakpoints existentes: 900px e 600px. `object-position` da foto muda por breakpoint e **tem
que ser conferido em mobile real**. Nenhum breakpoint novo.

## Limites — NÃO ALTERAR
- `--radius:2px`. Botão **não** vira pílula, mesmo que a referência do Oliveira use.
- Não cobrir rosto de pessoa real com texto (regra da Rodada 5).
- Nenhuma prova social colada nos CTAs — 4 variantes foram testadas e rejeitadas na Rodada 6.
- Seção das máquinas (Compacta / 2 grupos / 3 grupos): **não se toca sem o Diogo junto.**
- Os 5 links do menu existem **uma vez só** no HTML. Não criar menu mobile duplicado.

## Critérios de aceitação
- [ ] Sem JS, o site abre e a hero aparece.
- [ ] A intro some sozinha mesmo se o gesto falhar.
- [ ] A seta para com a primeira linha da barra de números visível abaixo do header.
- [ ] Nenhum link de navegação aparece duas vezes no HTML.
- [ ] A topbar não corta o telefone em nenhuma largura entre 320px e 1920px.
- [ ] `prefers-reduced-motion: reduce` elimina toda a animação sem quebrar o layout.
```

Os três últimos critérios existem porque **foram bugs reais** encontrados na verificação da
Rodada 7. Critério de aceitação bom nasce de erro cometido, não de imaginação.

---

## 7. QA separado por trilha

| Trilha | Verifica | Com o quê | Quando | Quem aprova |
|---|---|---|---|---|
| **Design QA** | bate com a decisão e com `DESIGN_SYSTEM.md` §13/§14 | leitura humana + a spec | antes de mostrar ao Diogo | Opus, depois Diogo |
| **Visual QA** | renderiza certo, responsivo, sem estouro | browser embutido: screenshot, `read_page`, `resize_window` | toda mudança visível | Opus |
| **Code QA** | correção, duplicação, código morto | `/code-review`, `/simplify` (já usados no projeto) | antes do commit | Opus |
| **Security QA** | segredo em código, `.gitignore`, **vazamento interno pro Pages** | `/security-review` + a trava do workflow + hook `pre-push` | todo push | automático |
| **Performance QA** | peso, LCP, imagem não otimizada | `npx lighthouse` | por rodada | objetivo |
| **Accessibility QA** | contraste (brass sobre foto), foco, alvo de toque, `prefers-reduced-motion` | `npx @axe-core/cli` + teclado no browser | por rodada | objetivo |
| **Content QA** | **todo fato rastreável** a arquivo, catálogo real ou fala do Diogo | leitura dirigida, sem ferramenta | todo texto novo | Opus, com o Diogo confirmando fato de dentro da empresa |

**Content QA é a trilha mais importante e a única sem ferramenta.** É a que já custou caro
(depoimento e nome de evento inventados no site do Paulo) e a que está em risco agora: o Ato 3
do deck vai falar de processos internos da fábrica que **só o Diogo pode confirmar**. Regra
operacional: número, data, nome e depoimento **não existem** até terem origem apontada.

---

## 8. Arquitetura mínima recomendada

O menor conjunto que dá o maior ganho — quatro itens, custo somado praticamente zero:

1. **`gh` CLI instalado.** Fecha a lacuna mais grave: hoje ninguém sabe se o deploy passou nem
   se a trava anti-vazamento disparou.
2. **`npx lighthouse` e `npx @axe-core/cli` sob demanda.** Primeira verificação objetiva que
   este projeto vai ter. Sem instalação permanente, sem custo de contexto entre usos.
3. **Git hook `pre-push` rodando a trava do workflow localmente.** O material do Ato 3 e a
   pasta `pesquisa/` não podem chegar ao Pages. Hoje isso só é checado **depois** do push, num
   CI que ninguém consegue ler.
4. **A regra de precedência de documentos (§5) escrita no `PROJECT_BRAIN.md`.** Custa uma seção
   e resolve a classe inteira de erro em que a IA obedece um arquivo desatualizado.

**Nenhum MCP novo.** O browser embutido já cobre inspeção visual; o que falta é medição, e
medição é CLI.

### O que descartar, e por quê

| Descartar | Motivo |
|---|---|
| ~13 das 15 skills de design | fazem a mesma coisa. **Ficam duas**: `redesign-existing-projects` (checklist de diagnóstico — foi ela que apontou o grid de 3 cards e o terracota) e `example-skills:frontend-design` (processo de plano de design). O resto embute resposta pronta a uma pergunta que este projeto já respondeu |
| plugins `product-management`, `human-resources`, `marketing`, `data`, `brand-voice` | nunca acionados, nenhum aponta pro negócio real, e cada um paga imposto de contexto em toda sessão |
| `superpowers`, `ponytail` | nunca acionados aqui |
| `claude-seo` | adiar até depois da Fase 4; e então só `seo-page` e `seo-content` |
| chrome-devtools-mcp, BackstopJS, Figma MCP, Mobbin | §2 — resolvem problema que este projeto não tem hoje |

`caveman` fica: tem uso registrado e papel definido no Brain §9. `watch`, `agent-reach` e
`mattpocock-skills` ficam como estão — uso baixo, mas sem substituto quando precisam.

### Roadmap em ondas

**Onda 1 — agora, junto com as fases já aprovadas**
`gh` instalado · hook `pre-push` · regra de precedência no Brain · achados do §1 no `TOOLS.md`.

**Onda 2 — na próxima rodada visual (a da paleta)**
Primeira `lighthouse` e primeira `axe` do projeto, gerando linha de base. A rodada da paleta é
o momento certo: contraste é exatamente o que muda quando a cor muda. Também a primeira spec
escrita antes da implementação, com execução delegada e revisão do Opus depois.

**Onda 3 — quando o design congelar**
Reavaliar regressão visual. Enquanto o design muda de propósito toda rodada, baseline é ruído.

**Onda 4 — depois da Fase 4 (blog real)**
Reavaliar SEO, restrito a `seo-page` e `seo-content`.

**Nunca, salvo mudança de contexto:** MCP permanente para o que um comando `npx` resolve.

---

## Fontes consultadas (28/09/2026)

- [chrome-devtools-mcp — repositório oficial](https://github.com/ChromeDevTools/chrome-devtools-mcp/)
- [Chrome DevTools MCP — página de plugin da Anthropic](https://claude.com/plugins/chrome-devtools-mcp)
- [Playwright visual regression — guia 2026](https://testquality.com/playwright-visual-regression-guide/)
- [BackstopJS — guia de regressão visual](https://qaskills.sh/blog/backstopjs-visual-regression-testing-guide)
- [Typewolf](https://www.typewolf.com/) · [SiteInspire](https://www.siteinspire.com/) · [Awwwards](https://www.awwwards.com/websites/) · [recent.design](http://recent.design/) (destino do redirecionamento de `godly.website`)

Estado de `agent-reach`, MCPs, CLIs e skills: verificado por execução nesta máquina em
28/09/2026, não por documentação.
