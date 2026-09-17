# PROJECT_BRAIN.md — La Norma

Memória oficial e enxuta do projeto. Ler antes de qualquer sessão de implementação. Decisão que não está aqui não existe.

---

## 1. Objetivo

Site institucional para a Lanorma Coffee Machine Manufacturer S.L. (Palma de Gandia, Valência), proposto ao administrador Daniel Climent Martínez. Front-end estático (HTML/CSS puro, sem backend), copy e specs reais extraídas do lanorma.es.

## 2. Estado atual

~40% do projeto. Implementação **pausada** por decisão do Diogo — bloqueio de direção visual e de processo, não técnico.

## 3. Decisão já fechada

- **4174** (`index.html` + `nosotros.html` + `productos.html` + `css/style.css`) é a **única base principal** da La Norma.
- **4176** (`ln200-site/`) está **fora de cena e não será desenvolvido**. Fica só como referência exploratória pontual (ver seção 5).
- **Não voltar a discutir 4176 como alternativa de projeto.** Essa discussão está encerrada.

## 4. Diagnóstico central

O projeto não trava por falta de código, assets ou pesquisa. Trava porque **a direção visual nunca foi decidida** — foi substituída, sessão após sessão, por ajustes cosméticos pontuais sob pressão de prazo.

## 5. O que manter do 4174

- Estrutura de 3 páginas (Home / Nosotros / Catálogo), navegação e transição entre páginas.
- Copy e specs técnicas reais (não inventadas).
- Limpeza de "tells de IA" já feita.
- **4176 não é fonte de referência para a nova direção visual.** Está fora de cena (seção 3) e não deve ser revisitado. Qualquer aprendizado útil que ele já rendeu (elemento de assinatura visual, registro tipográfico mono, arco narrativo) já está absorvido como conhecimento neste Brain — não exige voltar ao código do 4176 para consultá-lo de novo.
- A nova direção visual se constrói a partir de: **4174 + assets reais do projeto + referências externas reais** (quando necessário, ver seção 7).

## 6. Direção visual — ainda NÃO decidida

Hipóteses A (Instrumento de Precisão), B (Oficina, não catálogo), C (Editorial de Padrão) existem só como texto — nenhuma foi escolhida.

**Regra:** não decidir só lendo descrição A/B/C. Primeiro precisamos **enxergar possibilidades visualmente**, com referências reais e exemplos concretos — depois comparar e decidir. Não implementar redesign antes dessa decisão.

## 7. Referências visuais

- Pesquisar referências externas reais só quando servir para destravar uma decisão concreta da seção 6 — não pesquisar por pesquisar.
- Extrair princípios (composição, tratamento de foto, hierarquia tipográfica), nunca copiar um site inteiro.

## 8. Skills

- Skills instaladas são **ferramentas disponíveis, não instruções permanentes**. Usar uma skill numa tarefa não significa que ela continua ativa nas próximas.
- Escolher a skill pela tarefa atual, não por hábito. Não empilhar skills sem necessidade.
- Não remover/desinstalar uma skill só por não ter sido usada recentemente.
- **Usar agora** (só depois que a seção 6 tiver decisão fechada): `redesign-existing-projects`, `impeccable` ou `example-skills:frontend-design`, `professor`, `humanizer`.
- **Usar depois** (na execução, não na decisão): `industrial-brutalist-ui` (só se caminho A vencer), `animate`/`animation-vocabulary`, `improve-animations`, `code-review`/`simplify`.
- **Ignorar por enquanto:** `10k-websites`, `high-end-visual-design`, `gpt-taste`, `stitch-design-taste`, `minimalist-ui`, `design-taste-frontend` (v1/v2) — sobreposição entre si e/ou já embutem resposta à pergunta ainda aberta da seção 6.

## 9. Caveman

- Disponível no projeto, mas **não é ativo continuamente** — uso sob demanda, tarefa por tarefa.
- Adequado para **execução mecânica, delimitada e cirúrgica** (1-2 arquivos, tarefa nomeada). Não decide direção visual, estratégia ou arquitetura.
- Quando uma tarefa for claramente adequada a ele, Claude pode sugerir o uso antes de executar.
- Sempre revisar o resultado/diff depois da execução — a checagem é sempre posterior ao fato.

## 10. Controle de contexto

- O chat **não é** a memória permanente do projeto. Arquivos do projeto são a memória persistente.
- `PROJECT_BRAIN.md` guarda estado, decisões e próximo passo. `TOOLS.md` guarda aprendizado sobre ferramentas.
- Chat atual deve conter só o contexto necessário para a tarefa atual. Tarefa grande se divide em etapas menores.
- `/compact` = mesma tarefa, contexto cresceu. Nova sessão = tarefa mudou de natureza.
- Antes de abrir nova sessão, registrar no Brain qualquer decisão importante que precise sobreviver.
- Não carregar conversa gigante por medo de perder contexto, e não repetir no chat o que já está registrado nos arquivos.
- Na dúvida sobre o estado do projeto, ler os arquivos oficiais antes de assumir. Estado atual registrado nos arquivos tem prioridade sobre conversas antigas ou documentos desatualizados.

## 11. Regra de continuidade

Se uma ferramenta, skill ou processo produzir um resultado claramente útil, **registrar o aprendizado no `TOOLS.md` antes de seguir para outra etapa**. Resultado bom não pode depender da memória do usuário.

## 12. Como trabalhar com este projeto

- Não assumir decisão que não está registrada neste arquivo.
- Não redesenhar antes da seção 6 ter escolha fechada.
- Não transformar discussão estratégica em implementação prematura.
- Manter decisões curtas e acionáveis — este arquivo é para decisão, não para diagnóstico longo.

## 13. Próximo passo exato

A próxima grande decisão é a **direção visual do 4174**. Buscar referências visuais reais e exemplos concretos (seção 7) que materializem as hipóteses A, B e C — decidir **vendo**, não só lendo descrição. Só depois disso resolver as pendências restantes (cor de marca definitiva, uso de foto humana, nível de fidelidade ao site oficial) e abrir sessão de implementação.

---

## Pontos a confirmar

- `README.md` e `contexto/CONTEXTO-SESSAO-2026-09-17.md` citam `hero-ln200-test.html`, que não existe mais na working tree (substituído por `ln200-site/`).
- `apresentacao-daniel/README.md` ainda descreve o 4174 como "preto+cobre"; o código já removeu o cobre. Material de apresentação desatualizado frente ao código.
- `assets/real/diagrama-2-grupos.png`, `diagrama-3-grupos.png`, `diagrama-compacta.png` e `assets/real/logo.png` não são referenciados em nenhum HTML — sobra de iteração anterior, uso futuro não confirmado.
