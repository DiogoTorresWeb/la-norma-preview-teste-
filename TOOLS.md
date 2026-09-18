# TOOLS.md — La Norma

Registro simples de skills, agentes e ferramentas testadas neste projeto. Objetivo: não depender da memória do usuário pra lembrar o que já foi tentado e o que deu.

Estados: ⭐ APROVADO (já funcionou, considerar de novo) · 🟡 TESTAR (parece útil, evidência ainda insuficiente) · ⚪ ARQUIVADO (não em uso agora, não precisa remover).

Só entra aqui o que já tem evidência no projeto. Não classificar skill por especulação.

---

### example-skills:frontend-design
- **Função:** revisão/correção de composição visual e "tells de IA" em UI existente. Também serve como guia de PROCESSO de design (plano em duas passadas: tokens nomeados → revisão contra o brief → código).
- **Resultado observado:** rodada em 16/09 sobre `index.html`/`productos.html` — removeu números de sequência falsos, eyebrows redundantes, seta solta, meta-string estranha. Corrigiu sintomas pontuais, mas não resolveu composição de fundo. Rodada em 18/09 usada de verdade como guia de processo para o redesign completo (sistema de cor, tipografia, hero) — explicitamente listou o acento terracota `#D97757`-like como "tell" reconhecível de IA, o que ajudou a escolher um acento diferente (brass/latão).
- **Estado:** ⭐ APROVADO — bom tanto para limpeza pontual quanto como processo de decisão de direção visual, desde que combinado com brief específico do Diogo (não decide sozinho).
- **Quando usar:** em qualquer rodada de decisão ou polimento visual — ler o guia de processo antes de montar paleta/tipografia do zero.

### redesign-existing-projects
- **Função:** checklist de auditoria de padrões genéricos de IA em projeto existente (tipografia, cor, layout, componentes, iconografia, conteúdo) + ordem de prioridade de correção.
- **Resultado observado:** rodada em 18/09 — apontou "3 cards iguais" (`.pillars`) como o layout mais genérico de IA (virou `.principles`, lista editorial sem card) e confirmou a prioridade fonte→cor→estados→layout→componentes usada na execução.
- **Estado:** ⭐ APROVADO — bom como checklist de diagnóstico rápido antes de uma rodada de redesign.
- **Quando usar:** no início de qualquer rodada de redesign visual, antes de decidir o que mudar.

### simplify
- **Função:** revisão pós-implementação focada em reuso/simplificação/eficiência/altitude (não correção de bugs) — roda 4 subagentes em paralelo, um por ângulo, e aplica os achados.
- **Resultado observado:** rodada em 18/09 sobre o diff do redesign (index/nosotros/productos/style.css) — os 4 agentes juntos acharam 2 blocos de CSS inteiramente mortos (override de `.btn-primary` em seções que não têm esse botão), 3 duplicações reais de valor (filtro de foto, tipografia de eyebrow/hero-kicker, span de spec-list/zig-specs) e um `@import` de fonte com peso nunca usado — todos corrigidos. Também apontou duplicação estrutural (catálogo repetido entre index/productos, JS de página repetido 3x) que foi conscientemente mantida por ser decisão de produto ou exigir mudança de arquitetura fora do escopo da noite.
- **Estado:** ⭐ APROVADO — achou problema real sem inventar refactor desnecessário; vale rodar depois de qualquer implementação grande.
- **Quando usar:** depois de qualquer implementação grande, antes do commit.

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
