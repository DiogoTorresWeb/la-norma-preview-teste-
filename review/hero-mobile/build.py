"""
Gera 3 variantes da hero pra comparar no celular (review/hero-mobile/v1..v3.html).
Cada uma reaproveita o header real do index.html e o css/style.css; só a hero muda.
Os caminhos são relativos à raiz do repo (a página é publicada como preview com
css/ e assets/ ao lado), então abrir local exige servir a raiz: python3 -m http.server
e acessar /review/hero-mobile/ não funciona — usar o preview publicado.
"""
import re

src = open("index.html", encoding="utf-8").read()
head_end = src.index("<main id=\"swup\"")
top = src[:head_end].replace('css/style.css?v=15', 'css/style.css?v=16')
top = re.sub(r"<title>.*?</title>", "<title>La Norma — hero {label}</title>", top)

stat = src[src.index('<section class="stat-strip">'): src.index('<section class="section-dark">')]

tail = """
<div class="rev-pill"><a href="index.html">← variantes</a><span>{label}</span></div>
</main>
<script>
  document.getElementById('navToggle').addEventListener('click', () => document.getElementById('mainNav').classList.toggle('open'));
  const hs = document.getElementById('headerStack');
  const onScroll = () => hs.classList.toggle('is-scrolled', window.scrollY > 40);
  onScroll(); window.addEventListener('scroll', onScroll, {passive:true});
</script>
</body></html>"""

pill_css = """
.rev-pill{position:fixed;left:16px;bottom:16px;z-index:600;display:flex;gap:10px;align-items:center;
  background:rgba(23,15,10,.92);border:1px solid rgba(243,236,221,.25);border-radius:999px;padding:8px 14px;
  font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:#f3ecdd}
.rev-pill span{color:#b7a489}
"""

content = """
    <span class="eyebrow hero-kicker">Fabricante de máquinas de café · Valencia</span>
    <h1>Para negocios que quieren ir un paso más allá</h1>
    <p class="lede">Fabricadas a mano en Valencia. Pensadas para durar y repararse — no para reemplazarse.</p>
    <div class="hero-cta">
      <a href="#" class="btn btn-primary">Ver catálogo</a>
      <a href="#" class="hero-link">Conocer La Norma →</a>
    </div>"""

variants = {
 "v1": dict(label="V1 · foto limpa", css="""
/* V1 — mesma hero full-bleed, mas o recorte mobile fecha só no display central
   (sem ícones laterais) e a altura mínima garante vão entre display e texto. */
@media (max-width:700px){
  .hero{min-height:max(100svh, 780px);}
  .hero-bg{object-position:center top;}
  .hero::after{background:
    linear-gradient(0deg, rgba(23,15,10,.97) 0%, rgba(23,15,10,.86) 34%, rgba(23,15,10,.4) 58%, transparent 76%);}
  .hero h1{font-size:2.05rem;line-height:1.08;letter-spacing:-0.02em;}
  .hero p.lede{font-size:.98rem;margin-top:18px;}
  .hero-cta{margin-top:28px;}
}
""", html="""
<section class="hero">
  <picture class="hero-media">
    <source media="(max-width:700px)" srcset="assets/hero/hero-mobile-tight.jpg">
    <img class="hero-bg" src="assets/hero/hero-1920.jpg" alt="">
  </picture>
  <div class="hero-content">%s</div>
</section>""" % content),

 "v2": dict(label="V2 · editorial empilhada", css="""
/* V2 — no celular a hero vira duas peças: texto sobre fundo sólido em cima,
   foto do painel como faixa 4:3 embaixo. Nunca há texto sobre foto. Tipografia
   troca pra Fraunces (a serif do sistema), peso médio, mais ar. */
.hero-v2{background:var(--espresso);color:var(--cream);}
.hero-v2 .hero-text{padding:150px 32px 48px;max-width:640px;}
.hero-v2 h1{font-family:var(--ff-display);font-weight:500;font-size:clamp(2.1rem,4vw,3.2rem);line-height:1.12;letter-spacing:-0.02em;text-wrap:balance;}
.hero-v2 .hero-kicker{display:block;margin-bottom:22px;}
.hero-v2 p.lede{margin-top:22px;max-width:460px;color:var(--muted);font-size:1.02rem;}
.hero-v2 .hero-band{position:relative;aspect-ratio:16/9;overflow:hidden;}
.hero-v2 .hero-band img{width:100%;height:100%;object-fit:cover;object-position:center 40%;}
.hero-v2 .hero-band::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,var(--espresso) 0%,transparent 22%,transparent 80%,var(--espresso) 100%);}
@media (min-width:701px){
  .hero-v2{display:grid;grid-template-columns:1fr 1fr;align-items:center;min-height:100svh;}
  .hero-v2 .hero-text{padding:150px 32px 96px;}
  .hero-v2 .hero-band{aspect-ratio:auto;height:100%;min-height:100svh;}
  .hero-v2 .hero-band::after{background:linear-gradient(90deg,var(--espresso) 0%,transparent 30%);}
}
@media (max-width:700px){
  .hero-v2 .hero-text{padding:132px 24px 40px;}
  .hero-v2 h1{font-size:2.3rem;}
  .hero-v2 .hero-band{aspect-ratio:4/3;}
}
""", html="""
<section class="hero-v2">
  <div class="hero-text">%s</div>
  <div class="hero-band"><img src="assets/hero/hero-band.jpg" alt=""></div>
</section>""" % content),

 "v3": dict(label="V3 · tipográfica", css="""
/* V3 — a tipografia é a hero. Fundo sólido com a foto só como textura quase
   invisível; o display da máquina entra como um detalhe pequeno (faixa fina),
   não como cena. Título em Archivo peso 500, maior, e lede em Fraunces itálico. */
.hero-v3{position:relative;background:var(--espresso-deep);color:var(--cream);min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;}
/* a textura mostra só a metade de baixo da foto (vapor), nunca o display —
   senão ele aparece como fantasma atrás da faixa */
.hero-v3 .tex{position:absolute;left:0;right:0;bottom:0;width:100%;height:180%;object-fit:cover;object-position:center bottom;opacity:.22;}
.hero-v3::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(23,15,10,.9),rgba(23,15,10,.2) 60%,rgba(23,15,10,.6));}
.hero-v3 .hero-content{position:relative;z-index:1;padding:150px 32px 88px;max-width:720px;}
.hero-v3 .readout{display:block;width:min(360px,72%);border-radius:2px;margin:0 0 30px;border:1px solid rgba(243,236,221,.14);}
.hero-v3 h1{font-family:var(--ff-body);font-weight:500;font-size:clamp(2.4rem,5vw,4rem);line-height:1.04;letter-spacing:-0.03em;text-wrap:balance;}
.hero-v3 p.lede{font-family:var(--ff-display);font-style:italic;font-weight:400;font-size:1.15rem;line-height:1.5;margin-top:22px;max-width:440px;color:var(--muted);}
@media (max-width:700px){
  .hero-v3 .hero-content{padding:130px 24px 56px;}
  .hero-v3 h1{font-size:2.5rem;}
  .hero-v3 .readout{width:min(300px,80%);margin-bottom:26px;}
}
""", html="""
<section class="hero-v3">
  <img class="tex" src="assets/hero/hero-1280.jpg" alt="">
  <div class="hero-content">
    <img class="readout" src="assets/hero/hero-readout.jpg" alt="Display de la Ln1: 118 °C, Lanorma">
    <span class="eyebrow hero-kicker">Fabricante de máquinas de café · Valencia</span>
    <h1>Para negocios que quieren ir un paso más allá</h1>
    <p class="lede">Fabricadas a mano en Valencia. Pensadas para durar y repararse — no para reemplazarse.</p>
    <div class="hero-cta">
      <a href="#" class="btn btn-primary">Ver catálogo</a>
      <a href="#" class="hero-link">Conocer La Norma →</a>
    </div>
  </div>
</section>"""),
}

for key, v in variants.items():
    page = top.replace("{label}", v["label"]) + \
        "<style>%s%s</style>\n<main id=\"swup\">\n%s\n%s" % (pill_css, v["css"], v["html"], stat) + \
        tail.replace("{label}", v["label"])
    page = page.replace('<a href="index.html" class="logo">', '<a href="#" class="logo">')
    open(f"review/hero-mobile/{key}.html", "w", encoding="utf-8").write(page)
    print(key, len(page))
