# Gera cópias redimensionadas (1800 px no lado maior, JPEG q82) das fotos reais do acervo
# para as revistas. Rodar da raiz do repo: python3 materiais/revista/prep-images.py
# Nenhuma imagem é gerada ou alterada além do redimensionamento — só pixel real.
from PIL import Image, ImageEnhance
import os

# Mesmo tratamento de cor que o site aplica via CSS (saturate .88 · sepia .14 · contrast 1.03),
# só que gravado no pixel: assim as revistas não precisam de `filter`, e o PDF fica leve.
def treat(im):
    im = ImageEnhance.Color(im).enhance(0.88)
    im = ImageEnhance.Contrast(im).enhance(1.03)
    sepia = im.convert('RGB', (0.393, 0.769, 0.189, 0,
                               0.349, 0.686, 0.168, 0,
                               0.272, 0.534, 0.131, 0))
    return Image.blend(im, sepia, 0.14)
SRC = 'assets/biblioteca-wp-completa'
OUT = 'materiais/revista/img'
MAP = {
    'capa-panel.jpg':     'assets/hero/hero-2560.jpg',          # Alta-75 já tratada (painel aceso no vapor)
    'equipo.jpg':         f'{SRC}/CABECERA_PAG.NOSOTROS-1.jpg', # time real no mostrador
    'extraccion.jpg':     f'{SRC}/LaNorma_Alta-77-scaled.jpg',  # extração com vapor, paisagem
    'display.jpg':        f'{SRC}/LaNorma_Alta-65-scaled.jpg',  # display "115 °C · Lanorma"
    'vapor.jpg':          f'{SRC}/LaNorma_Alta-86-scaled.jpg',  # mão na lança de vapor, retrato
    'maquina-frente.jpg': f'{SRC}/LaNorma_Alta-71-scaled.jpg',  # Ln1 de frente, xícaras coloridas
    'tueste.jpg':         f'{SRC}/LaNorma_Alta-69-scaled.jpg',  # ambiente de torrefação, retrato
    'portafiltro.jpg':    f'{SRC}/LaNorma_Alta-81-scaled.jpg',  # mão com porta-filtro sob o painel
    'manos.jpg':          f'{SRC}/LaNorma_Alta-08-scaled.jpg',  # mãos com porta-filtro, máquina branca
    'botonera.jpg':       f'{SRC}/LaNorma_Alta-04-scaled.jpg',  # botoeira e display, máquina branca
    'maquina-oscura.jpg': f'{SRC}/LaNorma_Alta-73-scaled.jpg',  # Ln1 preta, grupo em destaque
    'taza.jpg':           f'{SRC}/LaNorma_Alta-12-scaled.jpg',  # extração em xícara, retrato
}
os.makedirs(OUT, exist_ok=True)
for name, src in MAP.items():
    im = Image.open(src).convert('RGB')
    im.thumbnail((1800, 1800), Image.LANCZOS)
    im = treat(im)
    im.save(f'{OUT}/{name}', quality=82, optimize=True, progressive=True)
    print(name, im.size, os.path.getsize(f'{OUT}/{name}')//1024, 'KB')
