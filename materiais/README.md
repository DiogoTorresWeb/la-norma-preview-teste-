# materiais/ — peças construídas com a identidade do site

Peças construídas com o sistema visual já aprovado no 4174.
Servem pra duas coisas: apresentar pro Daniel e mostrar que existe serviço agregado
pra vender depois do site.

**Ponto de entrada: `index.html`.** É a página que reúne tudo — abre essa na reunião
e navega a partir dela.

```bash
python -m http.server 4174
```

Depois abre `http://localhost:4174/materiais/`.

## Como abrir no celular

`localhost` no celular aponta pro próprio celular — por isso dá "conexão recusada".
Tem dois caminhos:

**1. Pela rede local (tudo, inclusive o deck).** Celular na mesma Wi-Fi, PC ligado com
o servidor rodando:

```
http://192.168.1.7:4174/materiais/
```

O IP muda quando o roteador reatribui endereço. Pra conferir o atual:
`Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -eq 'Wi-Fi' }`

**2. Pelo GitHub Pages (sem depender do PC).** Publicado automaticamente a cada push:

```
https://diogotorresweb.github.io/la-norma-preview-teste-/materiais/
```

**O deck não vai pro Pages, de propósito.** Ele traz o diagnóstico crítico do site atual
da La Norma, a reseña de 1 estrela e quanto uma agência cobraria — isso numa URL pública
e indexável seria ruim. O workflow apaga o bloco do deck do hub publicado (marcadores
`LOCAL-ONLY:START/END` em `index.html`) e falha o build se algo interno vazar. Pra
mostrar o deck: rede local, ou o `.pptx` no próprio celular.

---

## O que é cada peça

| Arquivo | O que é | Pra que serve na reunião |
|---|---|---|
| `index.html` | Hub que lista as peças | Abre essa primeiro. |
| `deck-reuniao-daniel.html` | **Deck de 12 slides em três atos** — a web, a marca, o taller | **É o fio condutor da reunião.** O Ato 3 fala de processos internos da fábrica: **nunca vai pro Pages.** |
| `deck-reuniao-daniel.pdf` | O mesmo deck, 12 páginas A4 landscape | Recurso, se não houver servidor. Gerado do HTML, não mantido à mão. |
| `la-norma-web-impressa.pdf` | As 4 páginas do site em papel digital, 19 páginas | Mostra o catálogo sem depender do PC. **Não substitui o site** — não tem as transições nem o FAQ aberto. |
| `plan-de-contenido.md` | Pauta de 8 artigos, calendário de Instagram com os seis textos e uma edição de newsletter escrita | Tira o conteúdo do estado de maquete. |
| `deck.html` | Proposta em 5 slides, tela cheia | Versão curta, se a conversa for rápida. Substitui o `contexto/propuesta-daniel-5slides.html` antigo. |
| `La-Norma-Propuesta-2026.pptx` | O mesmo deck, editável | Se ele pedir o arquivo pra editar ou repassar. |
| `blog.html` + `blog-articulo.html` + `blog-reparables.html` | Seção "Diario del taller" com **dois artigos escritos por inteiro** | O serviço agregado mais fácil de vender: conteúdo que também ajuda a vender máquina. |
| `assets/capturas/` | Capturas reais do site e das peças, em alta | Alimentam os slides do deck. Não são publicadas. |
| `instagram.html` | 6 formatos de post quadrado | Mostra que a identidade escala pra redes sem redesenhar nada. |
| `email.html` | Template de newsletter | Prova que dá pra manter contato com cliente sem depender de rede social. |

---

## Como navegar no deck

- **Setas / espaço / PageDown** avançam slide.
- **F11** deixa em tela cheia no notebook.
- Os pontinhos no canto inferior direito indicam e navegam entre os slides.
- Imprimir (Ctrl+P) gera um PDF com um slide por página.

Os 5 slides cabem exatos em 720px de altura — testado. Em tela mais baixa que isso
a tipografia aperta sozinha via media query.

## Como regerar os dois PDFs

Os PDFs são derivados — **não se editam à mão**. Com o servidor local de pé:

```bash
python -m http.server 4174
chrome --headless=new --no-pdf-header-footer --print-to-pdf=deck.pdf http://localhost:4174/materiais/deck-reuniao-daniel.html
```

O do site sai igual, uma página de cada vez (`index`, `nosotros`, `productos`, `formacion`),
e depois junta-se. O bloco `@media print` que faz isto funcionar está no **fim** de
`css/style.css`: declarado antes, perdia por ordem de origem para o `@media (max-width:900px)`
— a folha impressa tem ~720px de largura em CSS, e sem isso o site sairia todo em coluna
única, como sai no telemóvel.

---

## Decisões técnicas que valem saber

**O deck não usa caixas com borda.** O deck antigo era todo em `.card` com borda fina,
que é justamente o padrão rejeitado no `DESIGN_SYSTEM.md` (seção 14 — "tell de IA").
Aqui a informação vive em lista editorial com régua brass no topo, igual aos
`.principle` e `.machine` do site.

**O blog reaproveita o `css/style.css` de verdade**, não uma cópia. Header, rodapé,
botões e cores vêm do mesmo arquivo do site — por isso ele parece parte do site, e não
uma maquete separada. Se a paleta mudar (item 3 do backlog), o blog acompanha sozinho.

**E-mail e PowerPoint não suportam as fontes nem a técnica de cor do site.**
Por isso:
- As fontes viram equivalentes seguras: Georgia no lugar de Fraunces, Arial no lugar
  de Archivo, Courier New no lugar de IBM Plex Mono. Gmail ignora Google Fonts e o
  PowerPoint só usa fonte instalada na máquina.
- O logo do site é PNG preto tingido por `mask-image` no CSS, o que não funciona em
  nenhum dos dois. Foram geradas versões já coloridas em `materiais/assets/`
  (`logo-lanorma-cream.png` e `logo-lanorma-brass.png`).
- O e-mail é HTML de tabelas com estilo inline de propósito: é o único formato que
  Gmail, Outlook e Apple Mail renderizam igual.

---

## Regra de honestidade aplicada

Nenhuma peça inventa dado. Especificações, telefone, endereço e nomes de modelo saem
do catálogo real (`productos.html`).

O que é conteúdo de exemplo está **marcado na própria página**:
- `blog.html` e `blog-articulo.html` têm uma etiqueta fixa no canto inferior esquerdo
  dizendo que datas e autoria são de exemplo.
- `instagram.html` e `email.html` trazem o aviso no topo do conteúdo.

Os temas dos artigos saem todos de informação que já existe no site (como escolher
entre os modelos, o que é a versão vaso alto, PID e sonda, limpeza automática, grupo
erogador próprio, purga/eco/temporizador).

**O LN200 não aparece em lugar nenhum**, de propósito — ele ainda não foi integrado ao
site e vai ganhar campanha própria (ver `PROJECT_BRAIN.md`, seção 13, item 7). As
únicas menções são no deck, onde o protótipo dele já era citado antes como prova
técnica, e isso é verdade.

---

## Verificação do `.pptx` (28/09/2026)

Não há PowerPoint nem LibreOffice nesta máquina, então o arquivo foi conferido por três
caminhos objetivos, e **dois defeitos reais apareceram e foram corrigidos**:

1. **Contraste.** Todos os 84 trechos de texto foram medidos contra a cor de fundo do slide
   pela fórmula de contraste do WCAG. Os números `01/02/03` do slide 4 estavam em brass
   (`#B8843C`) sobre areia (`#E7D9BE`) — **2,35:1**, muito abaixo do mínimo de 4,5:1 para
   texto pequeno. Num slide projetado numa sala, isso simplesmente não se lê. Corrigido: sobre
   fundo claro o passo agora usa `BRASS_DARK` `#7C5623` (4,69:1 sobre areia, 5,56:1 sobre
   creme), e sobre fundo escuro o brass continua igual (5,77:1). Nova medição: **0 trechos
   abaixo do mínimo.**
2. **Colisão no slide 1.** O título ocupa 4 linhas a 30pt, cerca de 2,1 pol, numa caixa de
   1,9 pol — a última linha encostava no parágrafo abaixo. Corrigido: caixa do título passou a
   2,2 pol e o parágrafo desceu de 5,35 para 5,6 pol.

Também verificado e **correto**: 5 slides em 16:9 (13,33 × 7,5 pol), nenhum elemento fora dos
limites, fundo de cada slide na cor certa (escuro / creme / escuro / areia / escuro, igual ao
`deck.html`), e **só três fontes em uso — Arial, Georgia e Courier New**, que existem em
qualquer Windows. Nenhuma referência a Fraunces/Archivo/IBM Plex sobrou no arquivo.

**O que isso ainda não garante.** A conferência foi feita com um renderizador aproximado
escrito aqui (posições e textos reais do XML, métrica de fonte do Windows) — não é o que o
PowerPoint desenha. Ele pega colisão, estouro e contraste; não pega diferença fina de
espaçamento nem de quebra de linha. **Para o veredito final:** sobe o `.pptx` no Google Drive
(arrastar e soltar), que o Google Slides converte — com o arquivo lá, dá para exportar o PDF
e conferir slide a slide num renderizador de verdade.

Se algo estiver torto, **ajusta-se o gerador e roda de novo** — nunca o `.pptx` na mão, senão
o gerador e o arquivo divergem:

```bash
pip install python-pptx pillow
python materiais/build-deck-pptx.py    # regera o .pptx
python materiais/recolor-logo.py       # regera os logos tingidos
```

A conferência é repetível — `materiais/check-deck-pptx.py` desenha os 5 slides em PNG a partir
das posições reais e aponta colisão e elemento fora dos limites:

```bash
python materiais/check-deck-pptx.py materiais/La-Norma-Propuesta-2026.pptx /tmp/deck-render
```

A versão HTML (`deck.html`) essa sim foi testada nos 5 slides, em 1280×720 e em mobile.
