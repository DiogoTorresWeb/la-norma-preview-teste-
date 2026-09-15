# Pacote de design — Ln 200

Entrada do build. Toda copy aqui vai para a página **literalmente**. Números de faixa são pontos de partida, validados depois pelo teste de rolagem.

## 1. Premissa da marca

*La norma* quer dizer o padrão. O medo de quem compra máquina profissional é a **deriva**: o décimo café não sai como o primeiro porque a temperatura varia. O nome da marca é a ausência dessa variação. A página inteira ensina e vende uma só ideia: **el estándar que no se mueve.**

Se uma seção não serve essa ideia, ela não entra.

## 2. Paleta, amostrada da foto real da Ln 200

```css
:root{
  --canvas:#DFE3ED;      /* parede do estudio, levantada; nunca branco puro */
  --canvas-deep:#CDD3E0; /* alternancia de secao */
  --panel:#EFF1F6;       /* cartoes */
  --ink:#0E1518;         /* texto principal, do preto dos grupos levantado */
  --ink-2:#46555C;       /* texto secundario */
  --green:#335154;       /* marca, corpo da maquina na sombra */
  --green-light:#6F8989; /* corpo da maquina na luz */
  --green-deep:#22383A;  /* secoes escuras */
  --accent:#6B2A30;      /* vinho de espresso, o botao de acao */
  --accent-hover:#55201F;
  --brass:#CFB24A;       /* a linha de calibracao. So traco, nunca texto no claro */
  --steel:#C4C7CD;       /* bancada */
}
```

## 3. Tipografia

- Display: **Saira** 600/700. Cara de placa de máquina.
- Texto: **IBM Plex Sans** 400/500.
- Mono: **IBM Plex Mono** 400/500, para números, rótulos e a escala de calibração.

Nenhuma é Inter nem Roboto.

## 4. Mapa de faixas do herói

| # | Faixa | Momento da filmagem | Copy (literal) | Entrada |
|---|---|---|---|---|
| 1 | 0.00–0.22 | máquina inteira, parada, luz de estúdio | kicker `Lanorma Ln 200` / título `El décimo café sabe como el primero.` | desfoque-para-nítido (mais rampa única de carga) |
| 2 | 0.26–0.48 | câmera avança, controles e displays entram | `La temperatura no negocia.` / sub `Por eso el sabor tampoco.` | aproximação-da-profundidade |
| 3 | 0.52–0.74 | fecha no grupo, primeiras gotas caem | `Montada y probada a mano, una por una.` / sub `En nuestro taller de Valencia.` | deriva-para-baixo |
| 4 | 0.78–1.00 | extração corre, crema fecha, descanso | `Esto es la norma.` / sub `Bienvenido al nuevo estándar.` / botão `Ver la Ln 200` | subida palavra-a-palavra em três chegadas |

A ação fica na pista central. As legendas moram nas laterais limpas. Composição centrada, então **scrim de dois lados**, com a pista do meio intocada.

## 5. Herói estático (celular e movimento reduzido)

Sobre `hero-ending.jpg`:

- kicker: `Lanorma Ln 200`
- título: `El décimo café sabe como el primero.`
- sub: `Montada y probada a mano en Valencia. Bienvenido al nuevo estándar.`
- botão: `Ver la Ln 200`

## 6. Abaixo da dobra

Tudo afunila para **uma** ação: falar com o taller.

**A. La deriva** — imagem `dos-tazas.jpg`
- eyebrow `El problema`
- título `No es el café. Es la deriva.`
- corpo `Pides el mismo café a la misma máquina y sale distinto. Cambia la temperatura, cambia la extracción, cambia el sabor. En hora punta, cuando más gente hay delante, es cuando más se nota.`

**B. La norma** — imagem `norma-temp.jpg`. Aqui vive o momento interativo.
- eyebrow `La norma`
- título `Una franja estrecha. Siempre la misma.`
- corpo `Un espresso bueno vive dentro de una ventana muy corta. La presión, el tiempo y la temperatura tienen que caer juntos en el mismo sitio, taza tras taza. Eso es todo lo que hace una máquina. Y es lo único que hace la Ln 200.`
- interativo: `Mantén pulsado para extraer`. Solta cedo → `Corto. Ácido.` Solta tarde → `Largo. Amargo.` Dentro → `Dentro de la norma.`

**C. Tres cosas que no cambian** — três cartões, cada um com imagem (tratamento igual)
1. `Calidad garantizada` / img `grupo.jpg` / `Cada máquina se ensambla y se prueba a mano en nuestro taller. Sale de allí funcionando como va a funcionar durante años.`
2. `Soporte directo con el fabricante` / img `taller.jpg` / `Hablas con quien la diseña y la construye. Sin intermediarios. Antes, durante y después.`
3. `Compromiso ambiental` / img `ln1-blanco.jpg` / `Fabricar menos, pero mejor. Máquinas duraderas, reparables y eficientes, que alargan su vida en lugar de acabar en la basura.`

**D. La Ln 200** — imagem `ln200.jpg`
- eyebrow `El producto`
- título `Ln 200. Dos grupos.`
- corpo `Cuerpo en verde salvia, frente en acero pulido. Dos grupos con pantalla independiente cada uno y una central. Calientatazas arriba, dos lanzas de vapor, manómetro a la vista e iluminación LED sobre los grupos.`
- chips (só o observável na foto real): `2 grupos` · `2 pantallas` · `Calientatazas` · `2 lanzas de vapor` · `Manómetro` · `LED en los grupos`
- linha honesta: `Ficha técnica completa a petición.`

**Regra de honestidade desta seção:** a Ln 200 não tem ficha técnica confirmada no projeto. Nada de número inventado: sem litros de caldeira, sem watts, sem pressão, sem peso.

**E. Preguntas que nos hacen** (objeções reais da pesquisa)
- `¿Y cuando se avería?` → `Hablas directamente con el taller que la construyó. Sin intermediarios y sin pasar por un distribuidor.`
- `¿Cuánto cuesta mantenerla?` → `Está pensada para repararse, no para sustituirse. Piezas accesibles y servicio directo con quien la fabricó.`
- `¿Aguanta la hora punta?` → `Es justo el momento para el que está hecha. Rendimiento constante incluso en los momentos de mayor demanda.`
- `¿Dónde se fabrica?` → `En Palma de Gandia, Valencia. Allí se ensambla y allí se prueba, a mano, una por una.`

**F. Cierre** — imagem `taza-verde.jpg`
- título `Hablemos de tu barra.`
- corpo `Cuéntanos cuántos cafés sirves al día y te decimos qué necesitas. Sin compromiso.`
- formulário: `Nombre` · `Cafetería o empresa` · `Email` · `¿Cuántos cafés al día?` · botão `Hablar con el taller`
- estado de sucesso: `Recibido. Te escribimos desde Valencia.`
- **Tratamento do formulário:** estado de sucesso em JS apenas. Não há servidor, então nada é enviado. O telefone e o email reais ficam visíveis ao lado como o canal que funciona de verdade.

**G. Pé** — dados reais: `+34 960 64 00 72` · `Pol. Ind., C. Garbí, 1, SECTOR 3, 46724 Palma de Gandia, Valencia` · `info@lanorma.es` · Instagram e LinkedIn reais. Sem aviso de IA, por decisão do cliente.

## 7. Camada vetorial

**Elemento assinatura: a régua de calibração.** Uma escala vertical em latão na borda esquerda, com traços, rótulos em mono por seção e **uma janela destacada**, que é a norma. Desenha-se sozinha conforme a rolagem. No celular vira uma linha fina de progresso no topo.

Teste de ousadia: se eu remover a régua, a página muda de verdade. Ela é o que transforma "site de máquina de café" em "site sobre o padrão".

Mais: partículas de vapor em nível sussurro na seção escura, divisores que se desenham, e um fundo fixo único com deriva lenta de 90s para a página inteira ser um só ambiente.

Tudo honra movimento reduzido: estados finais visíveis, motores parados.

## 8. Engenharia obrigatória

Blob fetch (2,1 MB, então forma simples), lerp normalizado por dt, seeks com portão à prova de travamento, escritas no DOM só na mudança, faixas paginadas em distância de rolagem com teste de flick, sistema de legibilidade de quatro camadas com scrim de dois lados, os cinco portões do herói estático **vivos** com listeners de mudança, página completa sem o vídeo, e o piso de qualidade inteiro.

## 9. Portão de copy

Toda linha acima vai literal. A página construída passa pelo grep da Fase 9 (zero travessões, zero palavras de catálogo) mais a varredura de vícios de IA, antes de qualquer pessoa ver.

Dispositivos deliberados que **ficam**: `La temperatura no negocia.` e `Corto. Ácido.` / `Largo. Amargo.` São staccato escolhido de propósito para esta marca, não vício que entrou sozinho.
