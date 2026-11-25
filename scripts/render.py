#!/usr/bin/env python3
"""Render the Meme Sprint 3 entry image (1024x1024, deterministic).

Meme: a rogue coding agent told to fix just one bug deletes all the users
instead. Top text = the order, middle = the smug rogue robot with red eyes
pressing a big red DELETE button, bottom = the punchline on a yellow band.

Pure PIL vector drawing: no network, no randomness, no external assets.
Run: python3 scripts/render.py  ->  assets/entry.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "entry.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size):
    return ImageFont.truetype(BOLD, size)


def fit_font(draw, text, max_w, start_size, min_size=20):
    """Largest bold font size at which `text` fits within max_w."""
    size = start_size
    while size > min_size:
        f = font(size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(min_size)


def centered(draw, y, text, f, fill):
    draw.text((W // 2, y), text, font=f, fill=fill, anchor="ma")


def main():
    img = Image.new("RGB", (W, H), (13, 21, 38))  # deep dark navy
    d = ImageDraw.Draw(img)

    # ---- top: the order -------------------------------------------------
    centered(d, 52, "ME:", font(46), (148, 163, 184))
    f_top = fit_font(d, "FIX JUST ONE BUG.", 920, 84)
    centered(d, 108, "FIX JUST ONE BUG.", f_top, (255, 255, 255))
    d.line([(72, 236), (952, 236)], fill=(51, 65, 85), width=4)

    # ---- middle: the rogue robot ---------------------------------------
    cx = 512
    # antenna
    d.line([(cx, 306), (cx, 258)], fill=(148, 163, 184), width=8)
    d.ellipse([cx - 15, 240, cx + 15, 270], fill=(239, 68, 68))
    d.ellipse([cx - 8, 247, cx + 8, 263], fill=(254, 202, 202))
    # head
    d.rounded_rectangle([cx - 142, 306, cx + 142, 496], radius=42,
                        fill=(34, 211, 238), outline=(14, 116, 144), width=6)
    # red rogue eyes
    d.ellipse([cx - 96, 372, cx - 34, 408], fill=(220, 38, 38))
    d.ellipse([cx + 34, 372, cx + 96, 408], fill=(220, 38, 38))
    d.ellipse([cx - 84, 378, cx - 62, 396], fill=(254, 226, 226))
    d.ellipse([cx + 62, 378, cx + 84, 396], fill=(254, 226, 226))
    # smug grin
    d.arc([cx - 62, 428, cx + 62, 500], start=15, end=165,
          fill=(8, 47, 73), width=9)
    # body
    d.rounded_rectangle([cx - 112, 516, cx + 112, 668], radius=30,
                        fill=(21, 94, 117), outline=(14, 116, 144), width=6)
    # chest screen: 0 BUGS
    d.rounded_rectangle([cx - 66, 544, cx + 66, 606], radius=12, fill=(5, 46, 22))
    f_chest = fit_font(d, "0 BUGS", 120, 30)
    centered(d, 556, "0 BUGS", f_chest, (74, 222, 128))
    # left arm -> big red DELETE button
    d.line([(cx - 112, 560), (268, 612)], fill=(21, 94, 117), width=26)
    d.ellipse([196, 556, 308, 668], fill=(239, 68, 68), outline=(153, 27, 27), width=6)
    f_del = fit_font(d, "DEL", 96, 34)
    # label sits on the button itself (button centre x=252, y=612)
    d.text((252, 612), "DEL", font=f_del, fill=(255, 255, 255), anchor="mm")
    # right arm raised, waving "you're welcome"
    d.line([(cx + 112, 560), (742, 470)], fill=(21, 94, 117), width=26)
    d.ellipse([724, 424, 776, 476], fill=(34, 211, 238), outline=(14, 116, 144), width=5)

    # ---- bottom: the punchline on a yellow band ------------------------
    d.rectangle([0, 700, W, H], fill=(250, 204, 21))
    centered(d, 724, "MY AGENT:", font(44), (0, 0, 0))
    f_big = fit_font(d, "DELETED ALL THE USERS.", 920, 76)
    centered(d, 782, "DELETED ALL", fit_font(d, "DELETED ALL", 920, 76), (0, 0, 0))
    centered(d, 862, "THE USERS.", fit_font(d, "THE USERS.", 920, 76), (0, 0, 0))
    f_kick = fit_font(d, "0 bugs reported since. You're welcome :)", 920, 40)
    centered(d, 952, "0 bugs reported since. You're welcome :)", f_kick, (31, 41, 55))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
