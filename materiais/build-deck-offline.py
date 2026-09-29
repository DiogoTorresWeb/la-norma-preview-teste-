"""Gera deck-reuniao-daniel-offline.html: o mesmo deck, num unico ficheiro
sem dependencias (fontes e imagens embutidas). Abre no telemovel sem PC,
sem servidor e sem internet."""
import base64, mimetypes, re, sys, urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SRC = AQUI / "deck-reuniao-daniel.html"
OUT = AQUI / "deck-reuniao-daniel-offline.html"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read()

def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

html = SRC.read_text(encoding="utf-8")

m = re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com[^"]+)">', html)
css = get(m.group(1)).decode()
# so o subconjunto latin (o deck e em espanhol/portugues); o resto pesa sem servir
blocos = re.split(r'(?=/\* )', css)
mantidos = [b for b in blocos if b.startswith("/* latin */")]
def embutir_fonte(mo):
    return f"url({data_uri_bytes(get(mo.group(1)), 'font/woff2')})"
def data_uri_bytes(b, mime):
    return f"data:{mime};base64," + base64.b64encode(b).decode()
fontes = re.sub(r"url\((https://[^)]+\.woff2)\)", embutir_fonte, "".join(mantidos))
html = html.replace(m.group(0), f"<style>{fontes}</style>")
html = re.sub(r'<link rel="preconnect"[^>]*>\n?', "", html)

def trocar(mo):
    ref = mo.group(2)
    if ref.startswith(("http", "data:")):
        return mo.group(0)
    p = (AQUI / ref).resolve()
    if not p.exists():
        sys.exit(f"falta o ficheiro: {ref}")
    return f"{mo.group(1)}{data_uri(p)}{mo.group(3)}"
html = re.sub(r"""(url\(['"]?)([^'")]+\.(?:png|jpe?g|webp|gif))(['"]?\))""", trocar, html)
html = re.sub(r"""(src=")([^"]+\.(?:png|jpe?g|webp|gif))(")""", trocar, html)

restos = re.findall(r"""(?:src|href)="(?!#|data:)[^"]+""", html)
if restos or "fonts.googleapis" in html:
    sys.exit(f"ainda ha referencias externas: {restos}")
OUT.write_text(html, encoding="utf-8")
print(f"{OUT.name}: {OUT.stat().st_size/1024:.0f} KB")
