"""
Tratamento da hero da home a partir de uma foto real da La Norma
(`LaNorma_Alta-75`: painel da Ln1 aceso no meio do vapor, "Lanorma" no display
central). Só cor/textura em cima de pixel real — nada gerado.

Uso:  python3 assets/hero/treat_hero.py            # gera todas as saídas
      python3 assets/hero/treat_hero.py --preview  # só uma prévia 1400px
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC = "assets/biblioteca-wp-completa/LaNorma_Alta-75-scaled.jpg"
OUT = "assets/hero"

ESPRESSO_DEEP = np.array((23, 15, 10), np.float32)
ESPRESSO_MID = np.array((108, 84, 62), np.float32)
CREAM = np.array((228, 216, 196), np.float32)
PANEL_BOTTOM = 0.31                    # fração da altura do original onde o painel termina

# Recortes sobre o original de 2560x1707. O painel fica em y≈0.21–0.27 e as
# saídas dos grupos descem até y≈0.85; o display central está em x≈0.495.
BOX_WIDE = (0, 100, 2560, 1540)        # 16:9
BOX_TALL = (698, 0, 1836, 1707)        # 2:3 — as bordas caem nos vãos entre
                                       # os displays laterais e o central
FOCUS = (0.495, 0.30)                  # centro da vinheta/zona nítida


def tone_map(arr):
    """Mapeia a luminância pra uma rampa espresso→creme (3 pontos), com as altas
    luzes contidas: o vapor fica âmbar e escuro o bastante pra receber texto."""
    lum = arr @ np.array((0.2126, 0.7152, 0.0722), np.float32) / 255.0
    lum = np.clip(lum, 0, 1) ** 1.12 * 0.9
    t = lum[..., None]
    lo = ESPRESSO_DEEP + (ESPRESSO_MID - ESPRESSO_DEEP) * np.clip(t / 0.5, 0, 1)
    hi = ESPRESSO_MID + (CREAM - ESPRESSO_MID) * np.clip((t - 0.5) / 0.5, 0, 1)
    return np.where(t < 0.5, lo, hi)


def display_mask(img, box):
    """Os displays e ícones acesos são a única luz de marca real da foto: ficam
    com a cor original em vez de virar espresso. Máscara por matiz ciano/azul
    com saturação e brilho altos, limitada à faixa do painel (o vapor azulado
    das bordas não pode entrar), suavizada pra não recortar seco."""
    hsv = np.array(img.convert("HSV")).astype(np.float32)
    h, s, v = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2] / 255
    m = ((h > 165) & (h < 235) & (s > 0.32) & (v > 0.42)).astype(np.float32)
    panel_rows = int(PANEL_BOTTOM * 1707 - box[1])
    m[max(panel_rows, 0):, :] = 0
    m = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))
    m = m.filter(ImageFilter.GaussianBlur(3))
    return np.array(m).astype(np.float32)[..., None] / 255.0


def vignette(arr, size, center, strength=0.48, radius=0.84):
    w, h = size
    cx, cy = center[0] * w, center[1] * h
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx - cx) / (w * radius)) ** 2 + ((yy - cy) / (h * radius)) ** 2)
    k = 1.0 - strength * np.clip((d - 0.5) / 0.9, 0, 1) ** 1.5
    return ESPRESSO_DEEP + (arr - ESPRESSO_DEEP) * k[..., None]


def soft_periphery(img, center, sharp_ratio=(0.44, 0.46), feather=160, blur=4):
    """Zona nítida elíptica no painel; fora dela um desfoque leve — o vapor já é
    difuso, isso só tira detalhe da borda pra o olho ir pro display."""
    w, h = img.size
    blurred = img.filter(ImageFilter.GaussianBlur(blur))
    mask = Image.new("L", (w, h), 0)
    cx, cy = int(w * center[0]), int(h * center[1])
    rx, ry = int(w * sharp_ratio[0]), int(h * sharp_ratio[1])
    ImageDraw.Draw(mask).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
    return Image.composite(img, blurred, mask.filter(ImageFilter.GaussianBlur(feather)))


def add_grain(arr, amount=5.5):
    rng = np.random.default_rng(7)
    return arr + rng.normal(0, amount, arr.shape[:2])[..., None]


def build(box, focus, out, target_w, quality=84):
    im = Image.open(SRC).convert("RGB").crop(box)
    src = np.array(im).astype(np.float32)
    toned = tone_map(src)
    keep = display_mask(im, box)
    arr = toned * (1 - keep) + src * keep
    arr = vignette(arr, im.size, focus)
    arr = add_grain(arr)
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    im = soft_periphery(im, focus)
    im = im.resize((target_w, round(target_w * im.height / im.width)), Image.LANCZOS)
    im.save(out, quality=quality, subsampling=0, progressive=True)
    print(f"{out}  {im.size}  {os.path.getsize(out)//1024} KB")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if "--preview" in sys.argv:
        build(BOX_WIDE, FOCUS, f"{OUT}/preview-wide.jpg", 1400, 80)
        build(BOX_TALL, (0.5, 0.27), f"{OUT}/preview-tall.jpg", 800, 80)
    else:
        for w in (1280, 1920, 2560):
            build(BOX_WIDE, FOCUS, f"{OUT}/hero-{w}.jpg", w, 82 if w < 2560 else 80)
        build(BOX_TALL, (0.5, 0.27), f"{OUT}/hero-mobile.jpg", 1000, 82)
        build(BOX_WIDE, FOCUS, f"{OUT}/hero-lqip.jpg", 32, 40)
