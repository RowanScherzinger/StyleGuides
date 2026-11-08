"""WCAG contrast check for the macOS tokens: light and dark, standard and Increase Contrast.

Translucent label colours are composited over each surface the way AppKit draws them.
Keep the values here in sync with tokens/tokens.css. Run: python tools/contrast.py
Pass an accent's four shades (light, dark, increased-contrast light, increased-contrast dark)
to check a different system accent, for example purple:
    python tools/contrast.py cb30e0 db34f2 b02fc2 ea8dff
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from wcag import hex_rgb, over, ratio, table  # noqa: E402  shared helpers in <repo>/tools/wcag.py

W = (255, 255, 255)

# HIG > Color > Specifications: light, dark, increased contrast light, increased contrast dark
SYSTEM = {
    "red":    ("ff383c", "ff4245", "e9152d", "ff6165"),
    "orange": ("ff8d28", "ff9230", "c55300", "ffa056"),
    "yellow": ("ffcc00", "ffd600", "a16a00", "fedf43"),
    "green":  ("34c759", "30d158", "008932", "4ad968"),
    "blue":   ("0088ff", "0091ff", "1e6ef4", "5cb8ff"),
    "gray":   ("8e8e93", "8e8e93", "6c6c70", "aeaeb2"),
}
SCRIM = 0.55  # --color-scrim alpha
ACCENT = sys.argv[1:5] if len(sys.argv) >= 5 else SYSTEM["blue"]
A_L, A_D, A_IC_L, A_IC_D = (hex_rgb(h) for h in ACCENT)
S = {k: [hex_rgb(h) for h in v] for k, v in SYSTEM.items()}

def report(name, surfaces, rows, pairs):
    print(f"\n{name}")
    table(surfaces, rows, label_w=26, col_w=9)
    for label, (fg, bg) in pairs.items():
        print(f"  {label:34}{ratio(fg, bg):6.2f}")

def light(ic):
    bg = hex_rgb("#ececec")
    surfaces = {"window": bg, "content": W, "box": over((0, 0, 0, 0.04), bg), "menu": hex_rgb("#f6f6f6")}
    acc = A_IC_L if ic else A_L
    rows = {
        "label": (0, 0, 0, 0.85),
        "secondary": (0, 0, 0, 0.70 if ic else 0.50),
        "tertiary": (0, 0, 0, 0.50 if ic else 0.26),
        "border-strong": (0, 0, 0, 0.55 if ic else 0.22),
        "accent text": A_IC_L,
        "status ok": S["green"][2],
        "status warning": S["orange"][2],
        "status danger": S["red"][2],
        "status idle": S["gray"][2],
    }
    if not ic:
        rows["(Apple default blue)"] = A_L
        rows["(Apple default green)"] = S["green"][0]
        rows["(Apple default yellow)"] = S["yellow"][0]
    pairs = {
        "white on accent fill": (W, acc),
        "white on danger button": (W, S["red"][2] if ic else S["red"][0]),
        "red text on push button": (S["red"][2], W),
        "white chip on scrim, white photo": (W, over((0, 0, 0, SCRIM), W)),
    }
    report("LIGHT" + (" + Increase Contrast" if ic else ""), surfaces, rows, pairs)

def dark(ic):
    bg = hex_rgb("#323232")
    surfaces = {"window": bg, "content": hex_rgb("#1e1e1e"), "box": over((255, 255, 255, 0.05), bg), "menu": hex_rgb("#2b2b2b")}
    i = 3 if ic else 1
    rows = {
        "label": (255, 255, 255, 0.85),
        "secondary": (255, 255, 255, 0.75 if ic else 0.55),
        "tertiary": (255, 255, 255, 0.50 if ic else 0.25),
        "border-strong": (255, 255, 255, 0.55 if ic else 0.22),
        "accent text": A_IC_D if ic else A_D,
        "status ok": S["green"][i],
        "status warning": S["orange"][i],
        "status danger": S["red"][i],
        "status idle": S["gray"][i],
    }
    ctrl_win = over((255, 255, 255, 0.20), bg)
    ctrl_dlg = over((255, 255, 255, 0.20), hex_rgb("#2b2b2b"))
    red = S["red"][1]
    pairs = {
        "white on accent fill": (W, A_D),
        "white on danger button": (W, S["red"][1]),
        "text on push button": (over((255, 255, 255, 0.85), ctrl_win), ctrl_win),
        "red text on push button (window)": (red, ctrl_win),
        "red text on push button (alert)": (red, ctrl_dlg),
    }
    if ic:
        pairs["(white on IC accent, not used)"] = (W, A_IC_D)
    report("DARK" + (" + Increase Contrast" if ic else ""), surfaces, rows, pairs)

light(False)
dark(False)
light(True)
dark(True)
