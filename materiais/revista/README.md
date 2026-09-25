# materiais/revista/ — duas "revistas" em HTML paginado

Primeira versão de duas peças impressas da La Norma, construídas com a identidade
aprovada no site (`DESIGN_SYSTEM.md`): paleta espresso/creme/areia com brass como
único acento, Fraunces para títulos, Archivo para corpo, IBM Plex Mono só para
dado numérico, radius 2px, nenhum card com borda.

| Arquivo | O que é |
|---|---|
| `index.html` | Hub com os dois links e uma frase sobre cada peça. |
| `visita.html` | **Revista de visita** — fica na mesa quando um cliente potencial visita o taller e vai embora com ele. 10 spreads (20 páginas A5). |
| `formacion.html` | **Dossier de formación técnica** para distribuidores e serviços técnicos. 9 spreads (18 páginas A5). Todo o programa é proposta, marcado como tal. |
| `revista.css` | Sistema compartilhado: spread, página, capa, sumário, folio, specs, legendas, marcas de honestidade, `@media print`. |
| `export-pdf.js` | Gera `visita.pdf` e `formacion.pdf` (1 spread por folha A4 paisagem) com Playwright. |
| `prep-images.py` | Redimensiona as fotos reais do acervo para `img/` e grava nelas o mesmo tratamento de cor do site. |
| `img/` | Saída do script acima + os recortes webp das máquinas (`assets/real/`). Nada gerado por IA. |
| `visita.pdf`, `formacion.pdf` | Exportação atual (1,7 MB e 1 MB). |

Idioma do conteúdo: espanhol (como o site). Comentários de código e este README: português.

---

## Como rodar

Da raiz do repo (as revistas carregam fotos de `../../assets` e o logo de
`../assets`, então precisam de servidor):

```bash
python3 -m http.server 4174
# http://localhost:4174/materiais/revista/
```

Em tela: scroll vertical, um spread por tela (o spread se dimensiona pela altura
da janela). O botão "Imprimir / PDF" no canto chama `window.print()` — o
`@page { size: A4 landscape; margin: 0 }` do CSS já deixa o diálogo do navegador
no formato certo.

## Como exportar PDF

```bash
node materiais/revista/export-pdf.js
```

O script sobe um `http.server` temporário na porta 4179, abre cada HTML no
Chromium do Playwright, espera as fontes do Google e chama
`page.pdf({ format:'A4', landscape:true, printBackground:true, preferCSSPageSize:true })`.
No fim imprime quantas páginas cada PDF tem e avisa se o número diferir do número
de spreads (sinal de overflow). Caminhos do Playwright e do Chromium estão em
constantes no topo do script (`PLAYWRIGHT_PATH` / `CHROME_PATH` por env var se a
máquina for outra).

**Resultado da última exportação:** `visita.pdf` = 10 páginas (10 spreads),
`formacion.pdf` = 9 páginas (9 spreads), página de 841,9 × 595 pt = A4 paisagem
exato. Conferido renderizando páginas com PyMuPDF.

Se a máquina não tiver internet, o PDF sai com Georgia/Arial/Courier no lugar de
Fraunces/Archivo/Plex Mono — funciona, mas não é a identidade.

---

## Decisões de formato

**Spread = A4 paisagem (297 × 210 mm), cada metade = A5 retrato.** A instrução
pedia "1 spread por página A4 paisagem"; a única maneira de isso fechar sem escala
é a dupla ser A4 e cada página A5. Impresso frente e verso e dobrado ao meio vira
um caderno A5 — o formato natural de uma peça que fica na mesa e vai no bolso.

**Toda medida em `cqw`** (1 % da largura do spread, via `container-type`). Corpo
1,2cqw ≈ 10 pt no papel, legenda 0,85cqw ≈ 7 pt, título de seção 3,6cqw ≈ 30 pt.
Assim tela e PDF têm exatamente a mesma diagramação, seja qual for a janela.

**A linha do grid não cresce** (`grid-template-rows:minmax(0,1fr)` + `overflow:hidden`
na página). Conteúdo que não cabe é cortado em vez de empurrar o folio pra fora —
e o script de screenshots tem uma checagem de overflow que acusa isso.

**Tratamento de cor gravado no JPEG, não em `filter` CSS.** O site aplica
`saturate(.88) sepia(.14) contrast(1.03)` via CSS; nas revistas isso fazia o
Chromium rasterizar cada foto no PDF (10 MB por revista). `prep-images.py` aplica
o mesmo tratamento no pixel e o PDF caiu para 1–1,7 MB.

**Capa e contracapa são spreads "single"** (uma composição na folha inteira), não
imposição de gráfica. Em tela lê-se capa primeiro e contracapa por último, que é o
que se espera de um PDF. Se a gráfica pedir imposição (capa + contracapa na mesma
folha), é reordenar dois `<section>`.

**Uma foto sangrada por spread, no máximo.** Onde há uma página com foto sangrada,
a página oposta é só texto e ar. Fotos com margem (`.figure`) só no sumário e no
spread de módulos.

**Ritmo claro/escuro** como o site: capa escura → creme → creme → areia → escuro →
creme → areia → escuro profundo → creme → escuro (visita).

**Estrutura da revista de visita** segue a sugerida, com dois ajustes: o sumário
ganhou uma página de "Gracias por venir" com a legenda das marcas (o leitor precisa
saber o que é `[A CONFIRMAR CON DANIEL]` antes de topar com uma), e a última página
útil tem uma pauta "Notas de la visita" para escrever à mão — é uma peça que fica
na mesa durante a visita, faz sentido que sirva de bloco.

**Estrutura do dossier**: capa · sumário + como ler · por qué · a quién va dirigido
/ qué sale sabiendo · módulos 1/2 · módulos 2/2 · formato y lugar · cómo apuntarse
· contracapa.

---

## O que é fato e o que está marcado

Tudo que aparece sem marca sai de `index.html`, `nosotros.html`, `productos.html`
ou `formacion.html` do próprio site (specs das 3 Ln1, as 8 funções, PID/sonda/
manómetro, copy de "diseñada por técnicos", vaso alto nos 3 modelos, telefone,
email, endereço, Instagram, LinkedIn, as duas reseñas do Google literais).

**Marcado `[A CONFIRMAR CON DANIEL]`** (estilo `.tag-confirmar`, contorno brass):

- Visita: personalização do frontal de aço (processo, modelos, prazo); LN200 —
  primeiras unidades entregues e data de apresentação; ficha técnica do LN200
  inteira (a tabela está vazia de propósito, com travessões); prazo de entrega e
  instalação.
- Formación: requisitos prévios; duração de cada módulo; calendário de revisão por
  volume; condições de garantia e prazos de repostos; máquinas disponíveis no
  taller para a prática; duração, vagas, preço, certificado e outros idiomas;
  próximas convocatórias.

**Marcado `[PROPUESTA]`** (`.tag-propuesta`, tracejado): os três perfis de público,
a lista "qué sale sabiendo" e os seis módulos do dossier. O único fato do dossier é
"presencial, no taller de Palma de Gandia".

**Não inventado, de propósito:** preço, datas, número de alunos, certificação,
distribuidores nomeados, ano de fundação, prêmios, specs ou foto do LN200, foto de
fábrica/linha de montagem (não existe no acervo — as fotos são de máquina em uso,
detalhe e o time no mostrador, e as legendas dizem exatamente isso). A distância
Palma de Gandia–Valencia também não entrou, por não estar confirmada em lugar nenhum.

**Nomes:** a reseña de Borja cita "Oscar y Dani"; a legenda da foto do time diz só
"El equipo de La Norma" porque não está confirmado quem é quem na foto.

---

## Pesquisa de referências (antes de desenhar)

`WebSearch` funcionou; `WebFetch` foi bloqueado pelo proxy em todos os domínios
tentados (lamarzoccousa.com, copenhagencoffeelab.com, simonelliusa.com,
ibca-usa.com, pdf.archiexpo.com). Os achados abaixo vêm dos snippets de busca +
conhecimento prévio de como essas peças são estruturadas — não foi possível abrir
os PDFs. Princípios extraídos, nada copiado:

1. **La Marzocco — Linea PB product brochure** (`lamarzocco.com/it/wp-content/uploads/2023/04/product_brochure_linea_pb_eng.pdf`) e product sheet 2021 (`lamarzoccousa.com/wp-content/uploads/2023/10/2021_ProductSheet_LineaPB.pdf`): specs sempre em tabela por nº de grupos (2 | 3 | 4) com altura/largura/profundidade em cm e polegadas, numa única página no fim; a narrativa vem antes, a tabela fecha. → Aplicado: ficha da Ln1 em tabela de 3 colunas por modelo, mono, uma página inteira só pra isso.
2. **Victoria Arduino — Eagle One brochure** (34 páginas, `services.unitedbaristas.com/equipment-catalogue/espresso-machine-catalogue/victoria-arduino-eagle-one/`): peça longa, uma ideia por spread, foto de produto grande e muito ar. → Aplicado: densidade baixa (1 título + 1 parágrafo + 1 lista por página), máquina recortada ocupando meia página.
3. **La Marzocco Technical Center / tech training** (`techcenter.lamarzocco.com`, `lamarzoccousa.com/news/blog/2012-tech-training-schedule/`): formação técnica de fabricante é apresentada por níveis, com objetivo explícito ("criar técnicos de campo") e pré-requisito de proficiência elétrica básica. → Aplicado: seção "Qué sale sabiendo" em resultados verificáveis e pré-requisitos como item a confirmar.
4. **Nuova Simonelli / Simonelli USA technician training** (`simonelliusa.com/technician-training`): conteúdo organizado como funcionamento → instalação → manutenção diária → sistemas de água. → Aplicado: ordem dos módulos 01→04 (arquitetura, instalação, eletrônica/controle, preventivo) antes de diagnóstico.
5. **IBCA — 5-Day Technical Machine Maintenance** (`ibca-usa.com/technical-machine-maintenance`): curso de vários dias, prática em máquina real, duração e formato declarados na capa do programa. → Aplicado: bloco "Formato y lugar" com todos os campos visíveis mesmo quando o valor é "a confirmar" — o leitor vê o que falta decidir.
6. **Publitas — How to design a magazine layout** (`publitas.com/blog/how-to-design-a-magazine-layout/`): hierarquia, propósito, legibilidade e equilíbrio; o grid de colunas é a ferramenta central. → Aplicado: grid fixo de 2 páginas, margens iguais em todas, folio sempre no mesmo lugar.
7. **PRINT Magazine — Leica Fotografie / LFI** (`printmag.com/design-inspiration/photography-magazines-printed-and-backlit/`): uma única família tipográfica usada com cuidado extremo dá mais precisão que muitas. → Aplicado: três famílias com papel fixo e nenhuma outra; mono só em número.

---

## Como foi verificado

- Screenshots Playwright em `review/revista/`: `visita-viewport-1440x900.jpg`,
  `formacion-viewport-1440x900.jpg`, `hub-1440x900.jpg` e um por spread
  (`visita-spread-01..10.jpg`, `formacion-spread-01..09.jpg`), com a barra de
  ferramentas de tela escondida.
- Checagem automática de overflow (nenhum elemento além da caixa do seu spread):
  zero ocorrências nas duas revistas depois das correções.
- PDF: contagem de páginas = contagem de spreads; páginas 1, 2, 4, 9 da visita e
  1, 5, 7 do dossier renderizadas com PyMuPDF e comparadas com a tela.

## O que ainda não foi verificado

- Impressão física (sangria, dobra). Os spreads não têm marca de corte nem
  sangria extra de 3 mm — se for pra gráfica, adicionar antes.
- Fontes do Google no PDF dependem de internet na hora de exportar.
- Leitura em celular: o spread vira só largura (`max-width:700px`), legível mas
  pequeno — a peça é pra papel e desktop.
