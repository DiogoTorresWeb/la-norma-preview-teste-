# TOOLS.md — La Norma

Registro simples de skills, agentes e ferramentas testadas neste projeto. Objetivo: não depender da memória do usuário pra lembrar o que já foi tentado e o que deu.

Estados: ⭐ APROVADO (já funcionou, considerar de novo) · 🟡 TESTAR (parece útil, evidência ainda insuficiente) · ⚪ ARQUIVADO (não em uso agora, não precisa remover).

Só entra aqui o que já tem evidência no projeto. Não classificar skill por especulação.

---

### example-skills:frontend-design
- **Função:** revisão/correção de composição visual e "tells de IA" em UI existente.
- **Resultado observado:** rodada em 16/09 sobre `index.html`/`productos.html` — removeu números de sequência falsos, eyebrows redundantes, seta solta, meta-string estranha (ver `contexto/HANDOFF-frontend-cleanup.md`). Corrigiu sintomas pontuais; feedback do Diogo no mesmo dia foi que o site "ainda parece cara de IA" — não resolveu a composição de fundo (cards genéricos, hierarquia tipográfica fraca).
- **Estado:** 🟡 TESTAR — útil para limpeza pontual, não validado ainda para decisão de composição/direção visual.
- **Quando usar:** depois que a direção visual (seção 6 do `PROJECT_BRAIN.md`) estiver decidida, para polimento de detalhe — não para decidir direção.

### 10k-websites
- **Função:** build de site cinematográfico com scroll (vídeo scrub, elemento de assinatura animado).
- **Resultado observado:** produziu o `ln200-site/` (4176) — tecnicamente sólido (scrub de vídeo com blob fetch, régua de calibração, fallback para mobile/reduced-motion), mas como peça de vendas de produto único, não como site institucional. 4176 foi formalmente tirado de cena (ver `PROJECT_BRAIN.md` seção 3).
- **Estado:** ⚪ ARQUIVADO — não está em uso no projeto principal (4174). Mantido só como referência técnica pontual (régua, tratamento mono, arco narrativo).
- **Quando usar:** não usar para o site institucional. Só reconsiderar se um dia existir uma landing de produto único separada.

### professor
- **Função:** aplica lentes "professor + conselho" sobre o projeto atual, mapeia lacunas e MCPs/skills relevantes.
- **Resultado observado:** provável origem de `contexto/CONTEXTO-SESSAO-2026-09-17.md` (mapeamento de MCPs, skills e resumo pra decisão futura) — não confirmado com certeza que foi essa skill especificamente, e não outra forma de pedido.
- **Estado:** 🟡 TESTAR — resultado parece útil, evidência de autoria não é 100% certa.
- **Quando usar:** início ou fim de sessão, para registrar contexto de decisões e ferramentas — sempre conferindo se o resultado deve virar entrada no `PROJECT_BRAIN.md` ou aqui.

---

Regra de continuidade: se uma ferramenta/skill/processo produzir resultado claramente útil, registrar aqui antes de seguir para outra etapa (ver `PROJECT_BRAIN.md` seção 11).
