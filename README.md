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
- Não existe no acervo nenhuma foto real de fábrica ou linha de montagem — só macro de extração e uma foto de mostrador. Qualquer seção sobre processo de fabricação depende de foto nova.
- A **Ln 200** (máquina real, já vendida) **não aparece no site de propósito**: vai ganhar campanha própria e as especificações ainda não foram fornecidas. O protótipo dela vive em `ln200-site/`, com identidade visual própria que nunca foi decidida se aproveita.

> `hero-ln200-test.html` não existe mais — foi substituído por `ln200-site/`. Referência corrigida em 28/09/2026.

## Pendências
- Agent Reach: instalado, mas **degradado** — Twitter, Reddit e GitHub dependem da extensão OpenCLI, que não está conectada; só YouTube responde (verificado em 28/09/2026). As fotos do Instagram vieram do cache público do próprio WordPress, não do scraper.
- `gh` CLI não instalado e MCP do GitHub falhando: hoje não dá para ver se o deploy do Pages passou. Ver `pesquisa/sistema-de-producao.md`.
- Details.so MCP: registrado, mas precisa de autenticação OAuth (não pode ser concluída numa sessão não-interativa) — o usuário precisa autorizar via `claude mcp` ou `/mcp` numa sessão interativa.
