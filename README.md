# La Norma — just the front

Front-end estático (HTML/CSS puro, sem backend) inspirado na estrutura real de [lanorma.es](https://lanorma.es), com identidade visual preto (`#141414`) e cobre (`#B26A2E`).

## O que é isto
- `index.html` — home (hero, pilares de marca, grid de novidades)
- `nosotros.html` — sobre a marca (pilares técnicos + público-alvo)
- `productos.html` — catálogo (3 máquinas + specs técnicas + features)
- `css/style.css` — todo o estilo, tokens de cor/tipografia no `:root`

## O que foi copiado do site real
- Os textos (copy) vêm literalmente do lanorma.es — extraídos manualmente navegando o site em 2026-09-14.
- As fotos em `assets/real/` são as fotos reais do próprio lanorma.es (baixadas em 2026-09-15 direto do servidor deles — hero, oficina/equipe, produto, diagrama técnico e 6 thumbnails do feed de Instagram que o próprio site já cacheia publicamente). São imagens da La Norma sendo usadas no front dela mesma, não conteúdo de terceiros.
- `assets/real/especificaciones.jpg` é o diagrama técnico real de fábrica (modelo "Lanorma Ln1") — usado na página de Catálogo como ficha técnica visual.

## O que ainda é placeholder
- Os 3 cards de produto (Compacta / 2 grupos / 3 grupos) continuam com silhueta ilustrada em CSS — não temos foto individual de cada modelo, só uma foto geral da linha.
- `hero-ln200-test.html` é uma peça à parte, teste de Hero para um produto novo (LN200) ainda sem specs/fotos confirmadas — ver seção própria abaixo.

## Pendências
- Agent Reach: instalado pelo usuário, mas o adaptador de Instagram (`opencli instagram user`) está quebrado atualmente (recebe HTML em vez de JSON — bug do adaptador, não é falta de login). Por isso as fotos do Instagram vieram do cache público do próprio WordPress, não do scraper.
- Details.so MCP: registrado, mas precisa de autenticação OAuth (não pode ser concluída numa sessão não-interativa) — o usuário precisa autorizar via `claude mcp` ou `/mcp` numa sessão interativa.
