# Reunião com Daniel

## ⏱ Os 30 segundos antes de entrar

**Abre isto:** `..\materiais\deck-reuniao-daniel.html` — setas para avançar, F11 para ecrã
cheio. Se o portátil não tiver servidor a correr, abre o PDF ao lado, que é igual:
`..\materiais\deck-reuniao-daniel.pdf`.

**A ordem é a do deck. São três atos e um fecho:**

| | Bloco | Para que serve | O que é |
|---|---|---|---|
| 1–2 | Abertura | Dizer que é uma **primeira leitura**, não um diagnóstico da empresa | — |
| 3–4 | **Ato 1 · A web** | Mostrar que o problema está medido e que sabes resolvê-lo | **Facto** — PageSpeed e Google Maps |
| 5 | O site novo | Deixar ver. Não expliques, mostra | **Já construído** |
| 6–7 | **Ato 2 · A marca** | Provar que a identidade escala sem redesenhar nada | **Exemplo** — protótipos reais, conteúdo marcado como exemplo |
| 8 | O que se faz lá fora | Trazer ideias, não cobrar | **Referência** — Iberital, Ascaso, La Marzocco |
| 9–11 | **Ato 3 · O taller** | Mostrar que vês processo e sabes automatizar | **Observação tua** + duas **perguntas** |
| 12 | Fecho | Preço só da web: **800 €** | — |

**Onde parares para conversar:** no slide 5 (deixa-o olhar) e no slide 11, que acaba em
pergunta de propósito — *¿dónde se registra hoy el pedido?* e *¿con qué programa se hacen
ahora las etiquetas?*. **Não respondas tu.** É ele que sabe.

**O que não precisas de explicar:** as métricas do slide 3 (leem-se sozinhas), o design, e
como fizeste o site. Se ele perguntar, aí sim.

**As três frases que valem mais do que todo o resto:**
> «Es una primera lectura, no un diagnóstico de toda la empresa.»
> «No te traigo un número de horas ahorradas, porque no lo he medido.»
> «Eso todavía no lo pongo en precio.»

---

## O que levar

| O quê | Onde está | Para quê |
|---|---|---|
| **Deck de três atos** | `..\materiais\deck-reuniao-daniel.html` | O fio condutor. 12 slides. |
| **O mesmo em PDF** | `..\materiais\deck-reuniao-daniel.pdf` | Se não houver servidor. 12 páginas landscape. |
| **O site em PDF** | `..\materiais\la-norma-web-impressa.pdf` | As 4 páginas em papel digital, 18 páginas. Recurso, não substituto. |
| Site novo, 4 páginas | `..\index.html` (+ `nosotros`, `productos`, `formacion`) | A prova de que existe. Abre também no telemóvel. |
| Deck curto de 5 slides | `..\materiais\deck.html` e o `.pptx` | Versão enxuta, ou ficheiro para ele reencaminhar. |
| Hub dos materiais | `..\materiais\index.html` | Reúne tudo, para navegar em vez de apresentar. |

**Não abrir na reunião:** `ln200-site/`. A Ln 200 ainda não tem campanha nem especificações,
e aquele protótipo tem identidade própria que nunca foi decidida. Citar de boca, sim; mostrar
o ficheiro, não.

## Regra de estado da informação

O deck separa seis coisas, e não as mistura. Se ele perguntar «isto é certo?», a resposta
está na etiqueta do próprio slide:

- **Facto** — medido ou verificável (slides 3 e 4).
- **Já construído** — existe e abre-se agora (slides 5 e 7).
- **Referência** — visto noutras empresas (slide 8).
- **Exemplo** — demonstração, com o conteúdo marcado como tal (slide 7).
- **Observação tua** — visto por ti no taller, dito como teu (slides 9 e 10).
- **Pergunta** — o que ainda não sabemos (slide 11).

Nada de número que não tenha sido medido. «Em época alta isso come quase o dia» é
**observação tua**, e vai dita como tua. «Poupa X horas por mês» não existe — ninguém mediu.

## Identidade atual (para não a descreveres mal)

Não é «preto + cobre». É paleta quente de café: `--espresso-deep #170f0a`, creme `#f3ecdd`,
areia `#e7d9be` e **um único acento**, o brass `#b8843c`. Três tipografias com papel fixo:
Fraunces (títulos), Archivo (texto e navegação), IBM Plex Mono (números).

## Antes de sair de casa

Com o telemóvel ou tablet na mesma Wi-Fi deste PC:

- Materiais: `http://192.168.1.7:4174/materiais/`
- Site: `http://192.168.1.7:4174`

O IP muda quando o router reatribui endereço — confirma antes:
`Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -eq 'Wi-Fi' }`

**Sem depender do PC:** o site e as peças de portefólio estão em
`https://diogotorresweb.github.io/la-norma-preview-teste-/materiais/`.
**Os dois decks não estão lá, de propósito** — e o de três atos menos ainda, porque o Ato 3
fala de processos internos da fábrica. Isso não pode existir em URL pública indexável.

## Se ele perguntar...

| Pergunta dele | Resposta |
|---|---|
| «¿Cuánto me costaría esto?» | «800 €, por la web y el visual nuevo. Ya está prácticamente lista.» |
| «¿Y lo del taller, cuánto?» | «Eso todavía no lo pongo en precio. Primero quiero ver cómo se hace hoy — si te digo un plazo ahora, me lo estaría inventando.» |
| «¿Y tu trabajo en el taller?» | «Sigue al 100%. Esto lo hago fuera de mis horas de montaje.» |
| «¿Cuánto cobraría una agencia?» | «No lo sé, no he pedido presupuesto. No te voy a dar un número inventado.» |
| «Vamos a tener una reunión de marketing...» | «Perfecto — con esto ya resuelto, esa reunión parte de una base sólida.» |
| «¿Sigue la misma persona con la web?» (perguntas tu) | Em aberto: se sim, complementas; se não, assumes. |

## Piso de preço

800 € é fixo, e é só da web. Não é ponto de partida para negociar para baixo.

---

Atualizado em 28/09/2026. **Se este ficheiro discordar do `PROJECT_BRAIN.md` ou do código,
o errado é este ficheiro** — já aconteceu ficar a descrever uma identidade de duas rondas atrás.
