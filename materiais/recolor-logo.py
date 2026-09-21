"""Recolore o wordmark preto-sobre-transparente mantendo o canal alpha.

Necessário porque clientes de e-mail e o PowerPoint não suportam a técnica de
CSS mask-image usada no site para tingir o logo.
"""
import os
from PIL import Image

SRC = r"assets/real/logo-lanorma.png"
OUT_DIR = r"materiais/assets"
VARIANTS = {
    "logo-lanorma-cream.png": (243, 236, 221),   # --cream
    "logo-lanorma-brass.png": (228, 196, 140),   # --brass-light
}

os.makedirs(OUT_DIR, exist_ok=True)
src = Image.open(SRC).convert("RGBA")
alpha = src.getchannel("A")

for name, rgb in VARIANTS.items():
    flat = Image.new("RGBA", src.size, rgb + (255,))
    flat.putalpha(alpha)
    path = os.path.join(OUT_DIR, name)
    flat.save(path, "PNG", optimize=True)
    print(f"{path}  {os.path.getsize(path)} bytes  {flat.size}")
