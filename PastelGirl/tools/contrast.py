"""WCAG contrast check for the Pastel Girl tokens, with glass composited over the field.

Keep the values here in sync with tokens/tokens.css. Run: python tools/contrast.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from wcag import hex_rgb, over, ratio, hls, table  # noqa: E402  shared helpers in <repo>/tools/wcag.py

BG = hex_rgb("#120b12")
SURFACE = over((44, 31, 47, 0.62), BG)
# Worst case: a card at the brightest point of the pink haze (--color-bg-haze)
HAZE = over((245, 163, 195, 0.10), BG)
SURFACE_HAZE = over((44, 31, 47, 0.62), HAZE)

surfaces = {
    "bg": BG,
    "surface/bg": SURFACE,
    "surface/haze": SURFACE_HAZE,
    "danger/surf-haze": over((196, 26, 18, 0.20), SURFACE_HAZE),
    "raised/bg": over((34, 23, 36, 0.92), BG),
    "sunken/surface": over((18, 11, 18, 0.55), SURFACE),
    "accent-soft/surf": over((245, 163, 195, 0.14), SURFACE),
    "danger-fill/surf": over((196, 26, 18, 0.20), SURFACE),
}

texts = {
    "text cream-100": hex_rgb("#fbefe3"),
    "muted plum-300": hex_rgb("#c3adc0"),
    "dim plum-400": hex_rgb("#a08aa3"),
    "pink-500": hex_rgb("#f5a3c3"),
    "pink-600": hex_rgb("#c0668f"),
    "cream-200": hex_rgb("#f3e1cf"),
    "lilac": hex_rgb("#c8a8ef"),
    "mint": hex_rgb("#a6e7c8"),
    "sky": hex_rgb("#a8d4f5"),
    "butter": hex_rgb("#f6e19c"),
    "peach": hex_rgb("#f9bf9e"),
    "cherry-500": hex_rgb("#ff5247"),
    "cherry-400 text": hex_rgb("#ff6a5e"),
    "silver-500": hex_rgb("#b9b4c2"),
}

table(surfaces, texts, label_w=16)

print()
print("Dark text on pastel fills (--color-on-accent):")
for name in ("pink-500", "pink-400", "lilac", "mint", "butter", "cream-200"):
    fill = texts.get(name) or hex_rgb("#f8bcd3")
    print(f"  plum-950 on {name:10}{ratio(BG, fill):6.2f}")
print(f"  cream-100 on pink-500   {ratio(texts['text cream-100'], texts['pink-500']):6.2f}  (why on-accent is dark)")

print()
print("Accent vs danger separation (they must never look alike):")
for name in ("pink-500", "pink-600", "cherry-500"):
    h, l, s = hls(texts[name])
    print(f"  {name:11} hue {h:5.0f}  light {l:.2f}  sat {s:.2f}")
print(f"  luminance ratio pink-500 : cherry-500 = {ratio(texts['pink-500'], texts['cherry-500']):.2f}")

# ---------- Light variant ([data-theme="light"]) ----------
print()
print("LIGHT VARIANT")
L_BG = hex_rgb("#fff4ef")
L_HAZE = over((245, 163, 195, 0.18), L_BG)
L_SURFACE = over((255, 252, 250, 0.70), L_BG)
L_SURFACE_HAZE = over((255, 252, 250, 0.70), L_HAZE)

l_surfaces = {
    "bg": L_BG,
    "surface/bg": L_SURFACE,
    "surface/haze": L_SURFACE_HAZE,
    "sunken/surf-haze": over((140, 68, 102, 0.06), L_SURFACE_HAZE),
    "accent-soft/haze": over((245, 163, 195, 0.22), L_SURFACE_HAZE),
    "danger/surf-haze": over((196, 26, 18, 0.10), L_SURFACE_HAZE),
}

l_texts = {
    "text #2a1a2c": hex_rgb("#2a1a2c"),
    "muted #5e4762": hex_rgb("#5e4762"),
    "dim #7a6280": hex_rgb("#7a6280"),
    "accent-text": hex_rgb("#a83d6f"),
    "secondary-txt": hex_rgb("#7a52b3"),
    "ok #1f7550": hex_rgb("#1f7550"),
    "pending #866400": hex_rgb("#866400"),
    "warning #a84c18": hex_rgb("#a84c18"),
    "danger #c41a12": hex_rgb("#c41a12"),
    "info #2a6fb0": hex_rgb("#2a6fb0"),
    "focus #c0668f": hex_rgb("#c0668f"),
    "hardware": hex_rgb("#8f899a"),
    "pink-500 fill": hex_rgb("#f5a3c3"),
}

table(l_surfaces, l_texts, label_w=16)
print(f"  text on pink-500 fill: {ratio(l_texts['text #2a1a2c'], l_texts['pink-500 fill']):.2f}")
