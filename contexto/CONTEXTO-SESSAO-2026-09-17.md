# Contexto da sessão — La Norma (2026-09-17)

> **ARQUIVO HISTÓRICO (17/09/2026).** Retrato daquele momento, mantido como registro. Não é fonte sobre o estado atual — para isso valem `PROJECT_BRAIN.md`, `DESIGN_SYSTEM.md` e `pesquisa/`. Cita `hero-ln200-test.html`, que não existe mais, e uma identidade "preto + cobre" que já foi substituída.

Gerado pra referência externa. Snapshot do momento — MCPs/skills mudam com o tempo, revalidar antes de confiar cegamente.

---

## 1. Projeto: La Norma — just the front

Front-end estático (HTML/CSS puro, sem backend), inspirado na estrutura real de lanorma.es. Identidade: preto `#141414` + cobre `#B26A2E`.

**Arquivos principais**
- `index.html` — home (hero, pilares de marca, grid de novidades)
- `nosotros.html` — sobre a marca
- `productos.html` — catálogo (3 máquinas + specs técnicas)
- `css/style.css` — estilo, tokens de cor/tipografia no `:root`
- `hero-ln200-test.html` — teste de Hero pra produto novo LN200 (sem specs/fotos confirmadas ainda)

**Conteúdo real vs placeholder**
- Textos: copiados literalmente do lanorma.es (extraídos manualmente, 2026-09-14).
- Fotos em `assets/real/`: reais, baixadas direto do servidor deles (2026-09-15) — hero, oficina, produto, diagrama técnico, 6 thumbs do Instagram (cache público do WordPress).
- `especificaciones.jpg`: diagrama técnico real de fábrica, modelo "Lanorma Ln1".
- Ainda placeholder: os 3 cards de produto (Compacta/2 grupos/3 grupos) usam silhueta CSS — falta foto individual de cada modelo.

**Pendências conhecidas**
- Agent Reach instalado, mas adaptador Instagram (`opencli instagram user`) quebrado — recebe HTML em vez de JSON. Fotos do Insta vieram do cache do WordPress, não do scraper.
- Details.so MCP registrado mas precisa OAuth — não dá pra completar em sessão não-interativa.

**Branch atual:** `redesign-visual-16-09` (main = `main`), status limpo.

**Commits recentes**
```
8f601a4 Corrige tipografia, cards, contraste e qualidade de midia; garante site offline
3fb8fdf Corrige identidade visual e adiciona materiais reais para reunião com Daniel
62662be Instala skill 10k-websites no projeto
4df5896 Integra midia real do site e corrige achados da critica de design
c6257ba Adiciona teste de Hero para a LN200
632c5ae Cria front-end estatico da La Norma (preto/cobre)
```

**Pasta `contexto/`** guarda material da reunião com Daniel (proposta, roteiro de conversa, deck, handoffs de trabalho anterior).

---

## 2. Regras da diogo-base (herdadas do CLAUDE.md raiz)

- 5 gavetas: Recursos (estudo), Projetos (fim definido), Areas (operação contínua), Pessoal, Arquivo (só o que morreu).
- Nome de pasta/arquivo: minúsculo, hífen, sem acento, tem que dizer a verdade sobre o conteúdo.
- Chave/token/senha nunca no código — sempre `.env`, sempre no `.gitignore`.
- Nada de pasta `.git` dentro de pasta sincronizada pelo Google Drive.
- Dado pessoal de família (financeiro, saúde) não entra em projeto nem prompt de estudo.
- Regra de honestidade: não inventar fato. Depoimento/nome de evento inventado já foi removido do site do Paulo por esse motivo — não repetir.

---

## 3. MCPs ativos nesta sessão

### Conectados e usáveis
| MCP | Serve pra |
|---|---|
| Gmail | ler/enviar/rascunhar email, labels, threads |
| Google Drive | arquivos: ler, criar, buscar, compartilhar |
| Google Calendar | eventos, disponibilidade, convites |
| Dropbox | arquivos Dropbox: copiar, mover, links |
| Supabase | projetos, branches, migrations, SQL, edge functions |
| Figma | design context, screenshots, code connect, shaders, diagramas |
| Slack | mensagens, canais, listas, canvas, busca |
| Enriquecimento de leads | autocomplete empresa, enrich business/prospects, export CSV |
| Busca de vagas | search_jobs, dados de empresa, resume |
| Geração de mídia (grande, tipo Higgsfield) | imagem/vídeo/áudio/voz, publica TikTok, cria site, 3D, upscale, remove fundo |
| Docs (batch/create/query/update) | criar/editar doc estruturado com tabs, charts, comments |
| ccd_* (session, pr, sidebar, view, window, host, directory, connectors) | controle interno do app Claude Code Desktop — não é do projeto |
| Claude_Browser | navegador embutido isolado, dentro do app |
| claude-in-chrome | controla Chrome real do usuário |
| computer-use | controla desktop inteiro (mouse/teclado, apps nativos) |
| terminal | ler o que está no terminal do usuário |
| scheduled-tasks | criar/rodar cron jobs |
| mcp-registry | buscar/sugerir outros conectores |
| visualize | renderiza SVG/HTML widget inline no chat |

### Falharam conexão (indisponíveis, não é falta de configuração)
- **github** — erro de header de autorização mal formado
- **browser-use** (plugin) — connection closed
- **definite** (plugin, dados) — endpoint não encontrado

### Exigem autorização do usuário antes de usar
Atlassian, Box, Figma (via brand-voice), Gong, Granola, Notion, BigQuery, Hex, Ahrefs, Canva, HubSpot, Klaviyo, Similarweb, Supermetrics, Amplitude (+EU), Asana, ClickUp, Fireflies, Intercom, Linear, Monday, Pendo, Slack (instância separada via product-management). Autorizar via configuração de conectores do claude.ai ou `claude mcp`/`/mcp` numa sessão interativa.

---

## 4. Skills instaladas nesta sessão

### Usadas de fato / relevantes pro projeto
- **10k-websites** — build de site cinematic scroll-driven. Instalado especificamente pra esse projeto.
- **professor** — aplica lentes "professor + conselho" no projeto atual, mapeia lacunas.
- **insta** — sincroniza reels salvos do Instagram pro inbox do professor.
- **code-review / simplify** — revisão de diff e limpeza de código.

### Cluster de design/frontend (muita sobreposição entre si)
animate, animate-expo, animation-vocabulary, apple-design, design-taste-frontend (v1 e v2), emil-design-eng, find-animation-opportunities, gpt-taste, high-end-visual-design, humanizer, image-to-code, imagegen-frontend-mobile, imagegen-frontend-web, impeccable, improve-animations, industrial-brutalist-ui, minimalist-ui, redesign-existing-projects, stitch-design-taste, ask-sonner, write-swift, dataviz, artifact-design, artifact-diagramming, artifact-capabilities, frontend-design (example-skills)

→ candidato principal a poda: várias fazem "não deixe a UI genérica", sobrepõem forte (design-taste v1+v2, impeccable, high-end-visual-design, gpt-taste, redesign-existing-projects).

### Infra do Claude Code (não é do projeto)
update-config, keybindings-help, fewer-permission-prompts, loop, schedule, claude-api, run, init, security-review

### Pesquisa web
agent-reach — pesquisa multi-plataforma (xiaohongshu, twitter, reddit, linkedin, github, youtube, etc). Não usada neste projeto até agora.

### Plugins de time/negócio instalados globalmente, nunca acionados aqui
brand-voice (5), product-management (8), human-resources (8), marketing (8), data (10), figma-plugin (13), design-plugin (7), claude-seo (dezenas), caveman (dezenas), superpowers (13), ponytail (6), anthropic-skills (dezenas), example-skills (12), mattpocock-skills (11), watch, pdf-viewer (6)

→ maiores candidatos a desativar se quiser enxugar: nenhum aponta pro negócio real hoje (La Norma, agência, professor).

---

## 5. Resumo pra decisão futura

- **Usa de fato:** Gmail, Drive, Calendar, Slack, Figma, Supabase, browser embutido, 10k-websites, professor, code-review/simplify.
- **Duplicado/sobreposto:** cluster de design-frontend (~15 skills fazendo variação da mesma coisa).
- **Nunca acionado nesta sessão:** SEO, RH, marketing, product-management, data, caveman-extra, superpowers, mattpocock, ponytail, geração de mídia pesada, busca de vaga, enriquecimento de leads.
- **Quebrado:** MCP do GitHub, browser-use, definite.
