"""WCAG contrast check for the Jarvis tokens, including glass composited over a backdrop.

Keep the values here in sync with tokens/tokens.css. Run: python tools/contrast.py
"""

def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def over(fg_rgba, bg_rgb):
    r, g, b, a = fg_rgba
    return tuple(round(c * a + d * (1 - a)) for c, d in zip((r, g, b), bg_rgb))

def lum(rgb):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

BG = hex_rgb("#060404")
WHITE = (255, 255, 255)
MID = (128, 128, 128)

surfaces = {
    "bg": BG,
    "surface/bg": over((14, 10, 9, 0.62), BG),
    "raised/bg": over((21, 16, 14, 0.88), BG),
    "overlay/white": over((6, 4, 4, 0.84), WHITE),
    "overlay/mid-grey": over((6, 4, 4, 0.84), MID),
    "OLD widget glass .38/white": over((6, 4, 4, 0.38), WHITE),
}

texts = {
    "text #ded2c6": hex_rgb("#ded2c6"),
    "muted #ada197": hex_rgb("#ada197"),
    "dim #85796f": hex_rgb("#85796f"),
    "copper #b87333": hex_rgb("#b87333"),
    "gold #d4a017": hex_rgb("#d4a017"),
    "gold-300 #f2d27a": hex_rgb("#f2d27a"),
    "silver-600 #8c8c8c": hex_rgb("#8c8c8c"),
    "ember #f07a2a": hex_rgb("#f07a2a"),
    "crimson #dc143c": hex_rgb("#dc143c"),
    "red-400 #f0485f": hex_rgb("#f0485f"),
    "chartreuse #a3d21f": hex_rgb("#a3d21f"),
    "arc-400 #6ec6ff": hex_rgb("#6ec6ff"),
}

print(f"{'':22}" + "".join(f"{s[:16]:>18}" for s in surfaces))
for tn, t in texts.items():
    row = "".join(f"{ratio(t, s):>18.2f}" for s in surfaces.values())
    print(f"{tn:22}{row}")

print()
for fill in ("#b87333", "#d4a017"):
    print(f"neutral-950 on {fill}: {ratio(BG, hex_rgb(fill)):.2f}")
