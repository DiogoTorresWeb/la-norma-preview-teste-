"""
Misturador: uma página só com 3 composições × 3 tipografias da hero, alternáveis
por dois seletores fixos no rodapé. Serve pra cruzar sem gerar variante por variante.
Gera review/hero-mobile/mix.html a partir do header real do index.html.
"""
import re

src = open("index.html", encoding="utf-8").read()
top = src[: src.index('<main id="swup"')].replace("css/style.css?v=15", "css/style.css?v=16")
top = re.sub(r"<title>.*?</title>", "<title>La Norma — misturador de hero</title>", top)
stat = src[src.index('<section class="stat-strip">'): src.index('<section class="section-dark">')]

text = """
  <span class="eyebrow hero-kicker">Fabricante de máquinas de café · Valencia</span>
  <h1>Para negocios que quieren ir un paso más allá</h1>
  <p class="lede">Fabricadas a mano en Valencia. Pensadas para durar y repararse — no para reemplazarse.</p>
  <div class="hero-cta">
    <a href="#" class="btn btn-primary">Ver catálogo</a>
    <a href="#" class="hero-link">Conocer La Norma →</a>
  </div>"""

css = """
/* ---- composições (data-comp no <html>) ---- */
.mx{display:none}
html[data-comp="foto"] .mx-foto, html[data-comp="empilhada"] .mx-emp, html[data-comp="tipo"] .mx-tipo{display:flex}

.mx-foto{position:relative;min-height:100svh;align-items:flex-end;color:var(--cream);overflow:hidden;background:var(--espresso-deep)}
.mx-foto .media{position:absolute;inset:0}
.mx-foto .media img{width:100%;height:100%;object-fit:cover;object-position:center 34%}
.mx-foto::after{content:"";position:absolute;inset:0;background:
  linear-gradient(0deg, rgba(23,15,10,.94) 0%, rgba(23,15,10,.72) 28%, rgba(23,15,10,.28) 56%, transparent 80%),
  linear-gradient(100deg, rgba(23,15,10,.62) 0%, rgba(23,15,10,.3) 36%, transparent 64%)}
.mx-foto .hero-content{position:relative;z-index:1;padding:0 32px 96px;max-width:640px}
@media (max-width:700px){
  .mx-foto{min-height:max(100svh,780px)}
  .mx-foto .media img{object-position:center top}
  .mx-foto::after{background:linear-gradient(0deg, rgba(23,15,10,.97) 0%, rgba(23,15,10,.86) 34%, rgba(23,15,10,.4) 58%, transparent 76%)}
  .mx-foto .hero-content{padding:0 24px 56px}
}

.mx-emp{flex-direction:column;background:var(--espresso);color:var(--cream)}
.mx-emp .hero-content{padding:150px 32px 48px;max-width:640px}
.mx-emp .band{position:relative;aspect-ratio:16/9;overflow:hidden}
.mx-emp .band img{width:100%;height:100%;object-fit:cover;object-position:center 40%}
.mx-emp .band::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,var(--espresso) 0%,transparent 22%,transparent 80%,var(--espresso) 100%)}
@media (min-width:701px){
  .mx-emp{display:grid!important;grid-template-columns:1fr 1fr;align-items:center;min-height:100svh}
  html:not([data-comp="empilhada"]) .mx-emp{display:none!important}
  .mx-emp .hero-content{padding:150px 32px 96px}
  .mx-emp .band{aspect-ratio:auto;height:100%;min-height:100svh}
  .mx-emp .band::after{background:linear-gradient(90deg,var(--espresso) 0%,transparent 30%)}
}
@media (max-width:700px){.mx-emp .hero-content{padding:132px 24px 40px}.mx-emp .band{aspect-ratio:4/3}}

.mx-tipo{position:relative;background:var(--espresso-deep);color:var(--cream);min-height:100svh;align-items:flex-end;overflow:hidden}
.mx-tipo .tex{position:absolute;left:0;right:0;bottom:0;width:100%;height:180%;object-fit:cover;object-position:center bottom;opacity:.22}
.mx-tipo::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(23,15,10,.9),rgba(23,15,10,.2) 60%,rgba(23,15,10,.6))}
.mx-tipo .hero-content{position:relative;z-index:1;padding:150px 32px 88px;max-width:720px}
.mx-tipo .readout{display:block;width:min(360px,72%);border-radius:2px;margin:0 0 30px;border:1px solid rgba(243,236,221,.14)}
@media (max-width:700px){.mx-tipo .hero-content{padding:130px 24px 56px}.mx-tipo .readout{width:min(300px,80%);margin-bottom:26px}}

/* ---- tipografias (data-type no <html>) ---- */
.mx h1{text-wrap:balance;color:var(--cream)}
.mx p.lede{margin-top:22px;max-width:460px;color:var(--muted)}
.mx .hero-kicker{display:block;margin-bottom:20px}
html[data-type="archivo-bold"] .mx h1{font-family:var(--ff-body);font-weight:700;font-size:clamp(2.05rem,4.2vw,3.4rem);line-height:1.08;letter-spacing:-0.02em}
html[data-type="archivo-bold"] .mx p.lede{font-size:1rem}
html[data-type="fraunces"] .mx h1{font-family:var(--ff-display);font-weight:500;font-size:clamp(2.3rem,4.4vw,3.4rem);line-height:1.12;letter-spacing:-0.02em}
html[data-type="fraunces"] .mx p.lede{font-size:1.02rem}
html[data-type="archivo-italic"] .mx h1{font-family:var(--ff-body);font-weight:500;font-size:clamp(2.5rem,5vw,4rem);line-height:1.04;letter-spacing:-0.03em}
html[data-type="archivo-italic"] .mx p.lede{font-family:var(--ff-display);font-style:italic;font-size:1.15rem;line-height:1.5}

/* ---- seletores ---- */
.mixer{position:fixed;left:12px;right:12px;bottom:12px;z-index:700;display:grid;gap:6px;
  background:rgba(23,15,10,.94);border:1px solid rgba(243,236,221,.22);border-radius:2px;padding:10px 12px;
  -webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.mixer .row{display:grid;grid-template-columns:64px 1fr 1fr 1fr;gap:6px;align-items:center}
.mixer .lab{font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:#b7a489;font-weight:600}
.mixer button{font:600 .66rem/1 Archivo,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#f3ecdd;
  background:none;border:1px solid rgba(243,236,221,.22);border-radius:2px;padding:9px 4px;cursor:pointer}
.mixer button.on{background:#b8843c;border-color:#b8843c;color:#170f0a}
.mixer .code{grid-column:1/-1;font:500 .62rem/1 'IBM Plex Mono',monospace;color:#e4c48c;letter-spacing:.04em;text-align:right}
.whatsapp-fab{display:none}
"""

body = f"""
<main id="swup">
<section class="mx mx-foto">
  <picture class="media">
    <source media="(max-width:700px)" srcset="assets/hero/hero-mobile-tight.jpg">
    <img src="assets/hero/hero-1920.jpg" alt="">
  </picture>
  <div class="hero-content">{text}</div>
</section>
<section class="mx mx-emp">
  <div class="hero-content">{text}</div>
  <div class="band"><img src="assets/hero/hero-band.jpg" alt=""></div>
</section>
<section class="mx mx-tipo">
  <img class="tex" src="assets/hero/hero-1280.jpg" alt="">
  <div class="hero-content">
    <img class="readout" src="assets/hero/hero-readout.jpg" alt="">
    {text}
  </div>
</section>
{stat}
</main>
<div class="mixer" id="mixer">
  <div class="row"><span class="lab">Compos.</span>
    <button data-k="comp" data-v="foto">Foto</button><button data-k="comp" data-v="empilhada">Empilhada</button><button data-k="comp" data-v="tipo">Tipográfica</button></div>
  <div class="row"><span class="lab">Tipo</span>
    <button data-k="type" data-v="archivo-bold">Archivo bold</button><button data-k="type" data-v="fraunces">Fraunces</button><button data-k="type" data-v="archivo-italic">Archivo 500 + itálico</button></div>
  <div class="code" id="code"></div>
</div>
<script>
  const html=document.documentElement;
  const state={{comp:'foto',type:'archivo-bold'}};
  const q=new URLSearchParams(location.search);
  if(q.get('comp')) state.comp=q.get('comp'); if(q.get('type')) state.type=q.get('type');
  function apply(){{
    html.dataset.comp=state.comp; html.dataset.type=state.type;
    document.querySelectorAll('#mixer button').forEach(b=>b.classList.toggle('on', state[b.dataset.k]===b.dataset.v));
    document.getElementById('code').textContent='comp='+state.comp+' · type='+state.type;
    history.replaceState(null,'','?comp='+state.comp+'&type='+state.type);
  }}
  document.querySelectorAll('#mixer button').forEach(b=>b.addEventListener('click',()=>{{state[b.dataset.k]=b.dataset.v;apply();window.scrollTo(0,0);}}));
  apply();
  document.getElementById('navToggle').addEventListener('click',()=>document.getElementById('mainNav').classList.toggle('open'));
  const hs=document.getElementById('headerStack');const os=()=>hs.classList.toggle('is-scrolled',window.scrollY>40);os();window.addEventListener('scroll',os,{{passive:true}});
</script>
</body></html>"""

page = top.replace('<a href="index.html" class="logo">', '<a href="#" class="logo">') + f"<style>{css}</style>\n" + body
open("review/hero-mobile/mix.html", "w", encoding="utf-8").write(page)
print("mix.html", len(page))
