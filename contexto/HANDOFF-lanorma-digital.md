# Handoff — Projeto Lanorma Digital

**Data:** 14–15/09/2026
**Origem:** conversa no Claude chat (pesquisa de mercado + extração de assets + template de reuniões + navegação ao vivo)
**Destino:** Diogo quer migrar este projeto para o Claude Code em breve, junto com o projeto que já existe lá, para ter controle de tokens/contexto e handoff formal. Este documento é a base pra essa migração.
**Onde arquivar:** `C:\Users\Diogo Torres\diogo-base\Projetos\lanorma-digital\`

---

## 0. ATUALIZAÇÃO 15/09 — dados antigos ficaram obsoletos, confirmado ao vivo

Numa sessão de navegação real (Chrome do Diogo, conectado ao Claude), boa parte do diagnóstico original (seção 3 abaixo) ficou desatualizada. **Usar sempre estes números, não os da seção 3:**

- **LinkedIn:** a página duplicada (`lanorma-coffee-machine-manufacturer-s-l`) foi removida — "esta página não existe mais". Só resta `linkedin.com/company/lanorma-coffee-machine/`, agora com **324 seguidores**, 11-50 funcionários, logo e capa configuradas.
- **Instagram (@lanorma.coffee):** não é mais "conta nova" — **949 seguidores, 77 posts**, com destaques organizados (Eventos, Ingeniería, Coffee Shops, Press, Linkedin).
- **Google:** não é mais 1 reseña de 2022 — são **8 reseñas, nota 4,1**. A mais recente (3 meses atrás) é 1 estrela, de alguém que ligou pedindo informação e não foi bem atendido — prova viva de que falta canal de contato claro.
- **Ascaso (concorrência):** LinkedIn real é **"1 mil+" seguidores**, não 210 como o levantamento antigo via busca indicava.
- **Performance do site (testado ao vivo, PageSpeed Insights, 15/09):** lanorma.es → **35/100 mobile, 64/100 desktop**. Confirma o teste que o Diogo já tinha feito manualmente.
- **Site do Paulo Oliveira:** está no ar em **oliveirafotos.es** (não mais só local). Pasta do projeto: `C:\Users\Diogo Torres\.gemini\antigravity-ide\scratch\oliveira-ai-growth-testes`. Performance real testada: **99/100 mobile, 100/100 desktop**.
- **Identidade visual real:** site é só **preto e branco**, sem nenhuma cor de destaque — o laranja/cobre usado nas primeiras versões do deck foi inventado sem base e já foi removido. Fonte da wordmark real é um sans arredondado bold (tipo Calibri Bold), não serifada.
- **Logo real** baixada e já usada nos decks: `LANORMA_HORIZ_NEGRO.png` (fundo transparente, texto preto — precisa de fundo claro atrás quando usada em fundo escuro).
- **Biblioteca de mídia completa do site** já baixada pelo Diogo: `C:\Users\Diogo Torres\diogo-base\Projetos\La Norma\assets\biblioteca-wp-completa`.

**Consequência pro tom da proposta:** não dá mais pra vender como "está tudo abandonado". O enquadramento que substituiu isso: **"vocês já começaram a se mexer — deixa eu acelerar, não começar do zero."** O deck de proposta (seção 5) já foi reescrito nesse tom.

**Capacidade real do Diogo:** 15–18h/semana, mesmo continuando full-time na montagem. Isso é espaço suficiente pra sugerir alcance além de site/LinkedIn (automação de vendas, organização de e-mail) — mas de forma leve, sem virar compromisso fechado. Ver slide "Un camino que nadie más está pensando" no deck.

---

## 1. Objetivo do projeto

Diogo trabalha como montador na **Lanorma Coffee Machine Manufacturer S.L.** (Palma de Gandia, Valência) e quer propor ao administrador único, **Daniel Climent Martínez**, assumir todo o digital da empresa — site, LinkedIn, redes, captação, e também a estrutura interna de documentos e reuniões.

Este projeto é o segundo cliente do "modo agência" (ver `/areas/agencia-freelance.md`), ao lado da RC Arcade. O método vem do projeto do fotógrafo Paulo Oliveira: auditoria → sistema de design → blocos com critério objetivo.

**Estado atual:** pesquisa concluída, dois entregáveis prontos, proposta comercial ainda NÃO escrita e ainda NÃO apresentada ao Daniel.

---

## 2. Ficha da empresa (dados públicos verificados)

| Campo | Valor |
|---|---|
| Razão social | Lanorma Coffee Machine Manufacturer S.L. |
| CIF | B05497383 |
| Constituição | 13/05/2021, Registro Mercantil de Valencia |
| Administrador único | Daniel Climent Martínez (desde 08/07/2021) |
| CNAE | 2893 — maquinaria para indústria de alimentação e bebidas |
| Capital social | 753.000 € (começou em 3.000 €; duas ampliações, 2022 e 2023) |
| Funcionários | 8 (dado de 2024) |
| Faturamento | **fontes divergem**: Empresia diz 500 mil–1 M €, Informa D&B diz 1,5–3 M €. Ponto sólido: **+157,48% no último ano** |
| Endereço fiscal | C. Real de Gandia/Garulla 48, Gandia (46020 / 46702) |
| Endereço operacional | Pol. Ind., C. Garbí 1, Sector 3, 46724 Palma de Gandia |
| Contato público | +34 960 64 00 72 · info@lanorma.es |
| Site | lanorma.es (WordPress 7.1) |
| Instagram | @lanorma.coffee — 796 seguidores, 21 posts, bio marcada "NEW ACCOUNT" |
| LinkedIn | **DUAS páginas duplicadas**: `/company/lanorma-coffee-machine` e `/company/lanorma-coffee-machine-manufacturer-s-l` (47 seguidores) |
| Facebook | link existe no rodapé do site mas aponta para `#` — morto |
| Google | 1 única reseña, de novembro de 2022, nota 5,0 |

**Produtos:** três linhas — Compacta (caldeira 8 L, 45 kg), 2 grupos (13 L, 65 kg), 3 grupos (20,5 L, 70 kg). Diferenciais técnicos declarados: grupo erogador de desenho próprio com câmara de pré-infusão, controle PID por sonda, purga ajustável 2–6 s, modo Eco, temporizador diário, limpeza automática.

**Posicionamento declarado no site:** "não somos uma marca pensada desde o marketing, somos engenheiros e técnicos"; montagem e teste à mão no taller de Valência; suporte direto com o fabricante; máquinas reparáveis contra a obsolescência.

---

## 3. Diagnóstico digital — os furos encontrados

1. **LinkedIn duplicado e inativo** num negócio 100% B2B. Últimos posts visíveis são avisos de feira (Fórum Coffee Festival, Fitur 2024) sem follow-up.
2. **Site sem página de contato e sem formulário.** Só 3 páginas: Home, Nosotros, Catálogo. Seção "NOTICIAS" no rodapé está vazia.
3. **Zero reseñas no Google** desde 2022, apesar de nota 5,0.
4. **NAP inconsistente** — Gandia vs Palma de Gandia, telefone 960 64 00 72 vs 601..., e o nome da marca aparece em 4 variações ("Lanorma Coffee Machine S.L.", "...Manufacturer S.L.", "La Norma", "LaNorma").
5. **Zero internacionalização** — site só em espanhol, apesar de o objeto social prever importação e exportação.
6. **Três produtos numa página só** — impossível ranquear por modelo.
7. **Vídeos .mp4 auto-hospedados no WordPress** e cinco GIFs animados como visual de produto — suspeita principal de peso da página.

---

## 4. Análise competitiva — a tese central

| Marca | Instagram | LinkedIn | Escala |
|---|---|---|---|
| Ascaso (Barcelona, desde os anos 50) | 19K + 22K (conta US) | **210 seguidores** | 95 países, fábrica 4.000 m² |
| Iberital (Barcelona, 1975) | 13K | ativo, patrocina Fórum Café e Hostelco | 100+ países |
| Quality Espresso (Futurmat, Gaggia, Italcrem, Mairali, Visacrem) | — | corporativo | desde 1952; **comprada pelo grupo italiano Evoca** |
| Crem / Expobar | — | — | só caldeira de intercambiador, sem dupla caldeira |
| **La Norma** | 796 (21 posts) | 47, em duas páginas | 8 funcionários |

**A tese:** o setor espanhol inteiro investiu em Instagram e abandonou o LinkedIn — canal onde o comprador B2B (distribuidor, rede de cafeteria, hotel) realmente decide. A Ascaso vende em 95 países com 210 seguidores no LinkedIn. No Instagram a La Norma nunca alcança ninguém; no LinkedIn a distância é de 210 para 47 e o terreno está vazio.

**Fraquezas exploráveis:**
- Ascaso virou lifestyle/prosumer doméstico → La Norma se posiciona como máquina de trabalho pesado.
- Iberital comunica de forma institucional e distante, não mostra ninguém montando → La Norma mostra a bancada e a mão.
- Quality Espresso foi comprada por grupo italiano → "fabricante espanhol" virou meia verdade; La Norma é o que a Futurmat deixou de ser.

**Posicionamento defensável:** o único fabricante espanhol pequeno o bastante pra você falar com quem montou a sua máquina, e sério o bastante pra aguentar o ritmo de uma barra cheia. Ascaso, Iberital e Futurmat não conseguem copiar isso — já são grandes demais.

---

## 5. Entregáveis já produzidos

Salvar os três na pasta do projeto antes de começar a próxima sessão.

| Arquivo | O que faz | Estado |
|---|---|---|
| `lanorma_assets.py` | Raspa todos os assets de lanorma.es (tenta a API REST do WordPress primeiro, cai pro crawl), organiza em pastas por categoria, converte tudo pra PNG e JPEG, explode GIFs frame a frame, gera `inventario.csv` | Pronto, **ainda não executado** |
| `lanorma_perf.py` | Auditoria de performance: TTFB, peso por asset, compressão, cache, formato; gera `perf-lanorma.csv` | Pronto, **ainda não executado** |
| `La-Norma-Plantilla-Reuniones.pptx` | Template de reunião em espanhol, 12 slides, gráficos nativos editáveis, notas do apresentador em cada slide | Pronto e validado |

Ambos os scripts precisam rodar na máquina do Diogo — o container do Claude chat tem a rede restrita a uma whitelist e `lanorma.es` retorna `host_not_allowed`.

**Como rodar (literal):**
```
pip install requests pillow beautifulsoup4
python lanorma_assets.py
python lanorma_perf.py
```
Depois da auditoria, colar `https://lanorma.es` em `https://pagespeed.web.dev/` para o Core Web Vitals real, que o script não mede.

---

## 6. Estratégia acordada

**Estrutura de serviço em 3 fases:**

- **Fase 0 — auditoria e quick wins (2–3 semanas, preço baixo, é o cavalo de troia):** unificar as duas páginas de LinkedIn, corrigir NAP em todos os diretórios, criar página de contato com formulário, reclamar o Google Business Profile, campanha de reseñas com clientes desde 2021, biblioteca de assets organizada.
- **Fase 1 — captação (retainer mensal):** página por modelo com SEO, versão em inglês, LinkedIn B2B com conteúdo de bastidor, catálogo PDF como isca, funil e CRM, Google Ads em intenção de compra.
- **Fase 2 — escala:** área de distribuidores, conteúdo de suporte técnico e peças, automação pós-venda.

**Modelo de contrato:** retainer mensal + bônus por lead qualificado ou venda atribuída. Nunca por hora e nunca projeto fechado — projeto fechado acaba e o Diogo volta a ser só montador.

**Direção de arte:** preto, branco e aço (a sessão fotográfica existente, arquivos `LaNorma_Baja-XX`), com **um só tom de contraste: cobre** — cor da caldeira e do latão. Ascaso é marrom retrô, Iberital é colorido e tech; preto e cobre não pertence a nenhum dos dois. Essa paleta já está aplicada no template de reuniões.

**Social:** LinkedIn 2 posts/semana (um técnico, um de bastidor com rosto), postando também da conta pessoal do Daniel. Instagram deixa de ser captação e vira prova — máquina instalada em cafeteria real, marcando o cliente, com a reseña pedida no mesmo dia. YouTube urgente, resolve o peso do site e abre canal de tutorial.

---

## 7. O que falta — próximos passos

**Bloqueadores (só o Diogo consegue responder, estando dentro da empresa):**
1. Quem fez a reforma do site em janeiro de 2026 e quanto custou? (agência externa, alguém interno, ou o próprio Daniel)
2. De onde vieram os clientes que geraram os +157%? Feira, boca a boca, distribuidor?
3. Ticket médio e ciclo de venda de uma máquina.
4. Vendem direto ou por distribuidor — e qual a proporção?
5. Quem era dono da conta antiga do Instagram que sumiu?

**Decisão pessoal pendente:** o Diogo quer **sair da montagem** ou fazer os dois? A proposta muda por completo. Se for tarefa extra, o Daniel paga como extra; se for transição de função, precisa virar substituição de custo — e aí o item 1 acima é essencial.

**Tarefas na ordem:**
1. Rodar os dois scripts e revisar `inventario.csv` e `perf-lanorma.csv`
2. Preencher o slide 9 do template (Canal digital) com os números reais do diagnóstico — o template deixa de ser presente e vira prova de trabalho já feito
3. Escrever a proposta comercial (diagnóstico + escopo das 3 fases + preço)
4. Grelhar a proposta antes de apresentar ao Daniel

---

## 8. Skills sugeridas para a próxima sessão

| Skill | Quando invocar |
|---|---|
| `grill-me` | **Antes de apresentar a proposta ao Daniel.** Já foi oferecido nesta conversa e ficou pendente. O furo provável está no posicionamento do Diogo (funcionário vs fornecedor) e na precificação. |
| `validar-ideia-mercado` | Se surgir dúvida sobre a tese do LinkedIn B2B — valida com pesquisa real de dor e concorrentes em vez de assumir. |
| `to-questionnaire` | Para transformar os 5 bloqueadores da secção 7 num questionário que o Diogo leva pro Daniel ou pro pessoal do escritório, em vez de perguntar solto. |
| `pptx` | Para editar ou estender `La-Norma-Plantilla-Reuniones.pptx`, ou montar o deck da proposta comercial. |
| `docx` | Se a proposta comercial for entregue como documento formal ao Daniel. |
| `product-management:competitive-brief` | Se for preciso aprofundar a análise de Ascaso / Iberital / Quality Espresso além do que está na secção 4. |

**Preferência de comunicação registrada:** em passos técnicos de risco (terminal, configuração, instalação), explicar de forma literal — comando exato, onde colar, o que esperar ver. Fora disso, pode ser resumido.

---

## 9. Fontes usadas

Site oficial (lanorma.es — home, nosotros, productos) · Registro Mercantil via empresia.es, datoscif.es, infoempresa.com, lokinn.com · eInforma / Informa D&B · Iberinform · Empresite (elEconomista) · Kompass · LinkedIn (páginas públicas) · Instagram (perfis públicos) · Páginas Amarillas · Coffee Expo · Felac · forocafe.es · gastro-spain.com · ascaso.com · iberital.com

Nenhuma credencial, chave de API ou dado pessoal sensível foi coletado ou está armazenado neste documento. Todos os dados são de fontes públicas.
