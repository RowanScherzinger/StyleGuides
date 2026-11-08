"""Shared WCAG colour maths and table printing for every guide's tools/contrast.py.

Each guide keeps its own token values in its contrast.py and imports these helpers:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
    from wcag import hex_rgb, over, ratio, table

Colours are (r, g, b) tuples of 0-255 ints, or (r, g, b, a) with a in 0-1 for
translucent colours that have to be composited over a backdrop first.
"""
import colorsys


def hex_rgb(h):
    """'#rrggbb' or 'rrggbb' to an (r, g, b) tuple."""
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def over(fg, bg):
    """Composite fg over the opaque bg. An opaque (r, g, b) fg is returned unchanged."""
    if len(fg) == 3:
        return fg
    r, g, b, a = fg
    return tuple(round(c * a + d * (1 - a)) for c, d in zip((r, g, b), bg))


def lum(rgb):
    """WCAG 2 relative luminance."""
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    """WCAG contrast ratio between two opaque colours, 1 to 21."""
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def hls(rgb):
    """(hue in degrees, lightness 0-1, saturation 0-1)."""
    h, l, s = colorsys.rgb_to_hls(*(c / 255 for c in rgb))
    return h * 360, l, s


def hue_gap(a, b):
    """Shortest distance between two colours' hues, in degrees."""
    d = abs(hls(a)[0] - hls(b)[0]) % 360
    return min(d, 360 - d)


def table(surfaces, rows, label_w=18, col_w=18):
    """Print a contrast grid: one row per text colour, one column per surface.

    surfaces and rows are {name: colour} dicts. Translucent row colours are composited
    over each surface before measuring. Column headings are cut to col_w - 2 characters.
    """
    print(f"{'':{label_w}}" + "".join(f"{s[:col_w - 2]:>{col_w}}" for s in surfaces))
    for label, colour in rows.items():
        cells = "".join(f"{ratio(over(colour, s), s):>{col_w}.2f}" for s in surfaces.values())
        print(f"{label:{label_w}}{cells}")


def separation(pairs):
    """Print hue gap and luminance ratio for ((name, colour), (name, colour)) pairs."""
    for (an, a), (bn, b) in pairs:
        print(f"  {an:>14} vs {bn:<14} hue gap {hue_gap(a, b):5.0f}  luminance ratio {ratio(a, b):.2f}")
