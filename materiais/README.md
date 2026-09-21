# materiais/ — peças construídas com a identidade do site

Cinco exemplos de coisas que dá pra fazer com o sistema visual já aprovado no 4174.
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
| `index.html` | Hub que lista as 5 peças | Abre essa primeiro. É o fio condutor. |
| `deck.html` | Proposta em 5 slides, tela cheia | Substitui o `contexto/propuesta-daniel-5slides.html` antigo. Mesmo conteúdo, identidade nova. |
| `La-Norma-Propuesta-2026.pptx` | O mesmo deck, editável | Se ele pedir o arquivo pra editar ou repassar. |
| `blog.html` + `blog-articulo.html` | Protótipo da seção "Diario del taller" | O serviço agregado mais fácil de vender: conteúdo que também ajuda a vender máquina. |
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

## O que ainda não foi verificado

**O `.pptx` não foi aberto no PowerPoint.** Não há PowerPoint nem LibreOffice nesta
máquina, então não deu pra renderizar e conferir visualmente. O que foi validado por
código: são 5 slides em 16:9, nenhum elemento fora dos limites do slide, e todos os
textos estão presentes. **Abrir e conferir antes de mandar pro Daniel.** Se algo estiver
torto, é só ajustar o gerador e rodar de novo, da raiz do projeto:

```bash
pip install python-pptx pillow
python materiais/build-deck-pptx.py    # regera o .pptx
python materiais/recolor-logo.py       # regera os logos tingidos
```

A versão HTML (`deck.html`) essa sim foi testada nos 5 slides, em 1280×720 e em mobile.
