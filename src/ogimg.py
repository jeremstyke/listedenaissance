# -*- coding: utf-8 -*-
# Images de partage (Open Graph) 1200x630 générées pour chaque page
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(__file__)
F_TITLE = os.path.join(HERE, 'fonts', 'bricolage-grotesque-latin-800-normal.woff')
F_TEXT = os.path.join(HERE, 'fonts', 'figtree-latin-600-normal.woff')
F_EMOJI = os.path.join(HERE, 'fonts', 'NotoColorEmoji.ttf')
TINTS = {'ciel': (215, 237, 248), 'menthe': (213, 239, 226), 'peche': (255, 227, 214), 'lilas': (232, 225, 248), 'miel': (255, 241, 199)}
ENCRE = (30, 45, 59); DOUX = (90, 107, 120); MIEL = (255, 207, 92); FRAMB = (217, 70, 111)

def _emoji(e, size):
    try:
        f = ImageFont.truetype(F_EMOJI, 109)
        im = Image.new('RGBA', (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 10), e, font=f, embedded_color=True)
        bb = im.getbbox()
        if not bb: return None
        im = im.crop(bb)
        r = size / max(im.size)
        return im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)
    except Exception:
        return None

def _wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def make(path, title, kicker='Ma liste bébé', emoji='🍼', tint='peche'):
    W, H = 1200, 630
    bg = TINTS.get(tint, TINTS['peche'])
    im = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(im)
    # points décoratifs
    for x in range(640, W, 34):
        for y in range(0, H, 34):
            d.ellipse([x, y, x + 5, y + 5], fill=tuple(min(255, c + 22) for c in bg))
    # carte avec ombre miel
    d.rounded_rectangle([86, 96, 1124, 548], radius=40, fill=MIEL)
    d.rounded_rectangle([70, 80, 1108, 532], radius=40, fill=(255, 255, 255))
    d.ellipse([104, 114, 128, 138], outline=(220, 230, 227), width=4)
    # emoji dans une pastille
    d.ellipse([890, 120, 1060, 290], fill=bg)
    em = _emoji(emoji, 100)
    if em: im.paste(em, (975 - em.width // 2, 205 - em.height // 2), em)
    # titre
    size = 70
    while size > 40:
        ft = ImageFont.truetype(F_TITLE, size)
        lines = _wrap(d, title, ft, 720)
        if len(lines) <= 3: break
        size -= 4
    y = 170
    for ln in lines[:3]:
        d.text((130, y), ln, font=ft, fill=ENCRE); y += int(size * 1.12)
    fk = ImageFont.truetype(F_TEXT, 30)
    d.rounded_rectangle([130, 452, 130 + d.textlength('malistebebe.fr', font=fk) + 40, 500], radius=24, fill=ENCRE)
    d.text((150, 457), 'malistebebe.fr', font=fk, fill=(255, 255, 255))
    d.text((130 + d.textlength('malistebebe.fr', font=fk) + 64, 459), kicker, font=fk, fill=DOUX)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, optimize=True)
