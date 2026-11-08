"""WCAG contrast check for the Win11 tokens, light and dark, with translucent fills
composited the way Windows stacks them: window background, content layer, card.

Keep the values here in sync with tokens/tokens.css. Run: python tools/contrast.py
Pass an accent palette to check a different system accent, for example:
    python tools/contrast.py 99ebff 60cdff 0093f9 0078d4 005fb8 003e92 001968
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from wcag import hex_rgb, over, ratio, table  # noqa: E402  shared helpers in <repo>/tools/wcag.py

# Light3, Light2, Light1, Base, Dark1, Dark2, Dark3 (the default Windows blue)
ACCENT = [hex_rgb(h) for h in (sys.argv[1:8] if len(sys.argv) >= 8 else
          ("99ebff", "60cdff", "0093f9", "0078d4", "005fb8", "003e92", "001968"))]
LIGHT3, LIGHT2, _, _, DARK1, DARK2, _ = ACCENT

W = (255, 255, 255)
K = (0, 0, 0)

def mode(name, bg, layer, card, raised, dialog, texts, statuses, fills, accent, accent_text, on_accent, smoke_on):
    layer_bg = over(layer, bg)
    card_bg = over(card, layer_bg)
    surfaces = {
        "window": bg,
        "layer": layer_bg,
        "card": card_bg,
        "flyout": raised,
        "dialog": dialog,
    }
    print(f"\n{name}")
    rows = dict(texts)
    rows["accent text"] = accent_text
    rows["accent fill"] = accent
    for label, colour in statuses.items():
        rows[label] = colour
    table(surfaces, rows, label_w=20, col_w=10)
    print(f"  on-accent on accent fill        {ratio(on_accent, accent):6.2f}")
    for label, (fill, text) in fills.items():
        print(f"  {label:32}{ratio(text, fill):6.2f}")
    t = over(texts["text"], smoke_on)
    print(f"  text on scrim, worst photo      {ratio(t, smoke_on):6.2f}")

# ---------- Light ----------
L_BG = hex_rgb("#f3f3f3")
L_TEXT = (0, 0, 0, 0.894)
mode(
    "LIGHT",
    bg=L_BG,
    layer=(255, 255, 255, 0.50),
    card=(255, 255, 255, 0.70),
    raised=hex_rgb("#f9f9f9"),
    dialog=W,
    texts={
        "text": L_TEXT,
        "muted": (0, 0, 0, 0.62),
        "dim": (0, 0, 0, 0.447),
        "disabled": (0, 0, 0, 0.36),
        "strong stroke": (0, 0, 0, 0.45),
    },
    statuses={
        "ok #0f7b0f": hex_rgb("#0f7b0f"),
        "warning #9d5d00": hex_rgb("#9d5d00"),
        "danger #c42b1c": hex_rgb("#c42b1c"),
        "idle #8a8a8a": hex_rgb("#8a8a8a"),
    },
    fills={
        "danger text on danger fill": (hex_rgb("#fde7e9"), hex_rgb("#c42b1c")),
        "text on ok fill": (hex_rgb("#dff6dd"), over(L_TEXT, hex_rgb("#dff6dd"))),
        "text on warning fill": (hex_rgb("#fff4ce"), over(L_TEXT, hex_rgb("#fff4ce"))),
        "text on danger fill": (hex_rgb("#fde7e9"), over(L_TEXT, hex_rgb("#fde7e9"))),
    },
    accent=DARK1,
    accent_text=DARK2,
    on_accent=W,
    smoke_on=over((249, 249, 249, 0.88), K),
)

# ---------- Dark ----------
D_BG = hex_rgb("#202020")
mode(
    "DARK",
    bg=D_BG,
    layer=(58, 58, 58, 0.30),
    card=(255, 255, 255, 0.05),
    raised=hex_rgb("#2c2c2c"),
    dialog=hex_rgb("#2b2b2b"),
    texts={
        "text": W,
        "muted": (255, 255, 255, 0.773),
        "dim": (255, 255, 255, 0.53),
        "disabled": (255, 255, 255, 0.365),
        "strong stroke": (255, 255, 255, 0.55),
    },
    statuses={
        "ok #6ccb5f": hex_rgb("#6ccb5f"),
        "warning #fce100": hex_rgb("#fce100"),
        "danger #ff99a4": hex_rgb("#ff99a4"),
        "idle #9d9d9d": hex_rgb("#9d9d9d"),
    },
    fills={
        "danger text on danger fill": (hex_rgb("#442726"), hex_rgb("#ff99a4")),
        "text on ok fill": (hex_rgb("#393d1b"), W),
        "text on warning fill": (hex_rgb("#433519"), W),
        "text on danger fill": (hex_rgb("#442726"), W),
    },
    accent=LIGHT2,
    accent_text=LIGHT3,
    on_accent=K,
    smoke_on=over((32, 32, 32, 0.80), W),
)
