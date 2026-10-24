"""WCAG contrast check for the Woodland tokens, with glass composited over the field.

Keep the values here in sync with tokens/tokens.css. Run: python tools/contrast.py
"""
import colorsys

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

def hls(rgb):
    h, l, s = colorsys.rgb_to_hls(*(c / 255 for c in rgb))
    return h * 360, l, s

def hue_gap(a, b):
    d = abs(hls(a)[0] - hls(b)[0]) % 360
    return min(d, 360 - d)

def table(surfaces, texts):
    print(f"{'':18}" + "".join(f"{s:>18}" for s in surfaces))
    for tn, t in texts.items():
        row = "".join(f"{ratio(t, s):>18.2f}" for s in surfaces.values())
        print(f"{tn:18}{row}")

def separation(pairs):
    for (an, a), (bn, b) in pairs:
        print(f"  {an:>14} vs {bn:<14} hue gap {hue_gap(a, b):5.0f}  luminance ratio {ratio(a, b):.2f}")

# ---------- Light (default, :root) ----------
print("LIGHT (default)")
L_BG = hex_rgb("#f1ebdd")
# Worst case: a card where the two haze glows are strongest (top corners)
L_HAZE = over((217, 187, 106, 0.16), over((111, 140, 88, 0.16), L_BG))
L_SURFACE = over((250, 247, 239, 0.80), L_BG)
L_SURFACE_HAZE = over((250, 247, 239, 0.80), L_HAZE)

l_surfaces = {
    "bg": L_BG,
    "haze": L_HAZE,
    "surface/haze": L_SURFACE_HAZE,
    "sunken/surf-haze": over((84, 71, 58, 0.06), L_SURFACE_HAZE),
    "accent-soft/haze": over((111, 140, 88, 0.16), L_SURFACE_HAZE),
    "danger/surf-haze": over((168, 21, 42, 0.08), L_SURFACE_HAZE),
}

l_texts = {
    "text bark-900": hex_rgb("#2a2319"),
    "muted bark-700": hex_rgb("#54473a"),
    "dim bark-600": hex_rgb("#665847"),
    "accent-text m700": hex_rgb("#3f5a33"),
    "moss-600 fill": hex_rgb("#4e6b3c"),
    "highlight m800": hex_rgb("#33472a"),
    "walnut-ink": hex_rgb("#7b5232"),
    "ok fern-ink": hex_rgb("#276b3a"),
    "pending lake-ink": hex_rgb("#33688a"),
    "idle bark-500": hex_rgb("#8a7a66"),
    "warning lichen": hex_rgb("#7a5d0c"),
    "danger rowan-700": hex_rgb("#a8152a"),
    "info heather-ink": hex_rgb("#6c5288"),
    "knob bark-500": hex_rgb("#8a7a66"),
    "walnut-500 fill": hex_rgb("#8a6444"),
}
table(l_surfaces, l_texts)

print()
print("Text on the light accent fill (--color-on-accent):")
moss600 = hex_rgb("#4e6b3c")
print(f"  oat-50 on moss-600      {ratio(hex_rgb('#f8f4eb'), moss600):6.2f}")
print(f"  oat-50 on moss-700      {ratio(hex_rgb('#f8f4eb'), hex_rgb('#3f5a33')):6.2f}  (hover)")
print(f"  bark-900 on moss-600    {ratio(hex_rgb('#2a2319'), moss600):6.2f}  (why on-accent is light here)")
print(f"  oat-50 on walnut-500    {ratio(hex_rgb('#f8f4eb'), hex_rgb('#8a6444')):6.2f}")

print()
print("Separation (light): accent vs OK, warning vs danger, secondary vs warning and danger")
separation([
    (("moss-600", moss600), ("fern-ink", l_texts["ok fern-ink"])),
    (("lichen-ink", l_texts["warning lichen"]), ("rowan-700", l_texts["danger rowan-700"])),
    (("walnut-ink", l_texts["walnut-ink"]), ("lichen-ink", l_texts["warning lichen"])),
    (("walnut-ink", l_texts["walnut-ink"]), ("rowan-700", l_texts["danger rowan-700"])),
])

# ---------- Dark ([data-theme="dark"]) ----------
print()
print("DARK VARIANT")
D_BG = hex_rgb("#0f1712")
D_HAZE = over((147, 173, 124, 0.10), D_BG)
D_SURFACE = over((34, 49, 40, 0.62), D_BG)
D_SURFACE_HAZE = over((34, 49, 40, 0.62), D_HAZE)

d_surfaces = {
    "bg": D_BG,
    "surface/bg": D_SURFACE,
    "surface/haze": D_SURFACE_HAZE,
    "raised/bg": over((27, 39, 32, 0.95), D_BG),
    "accent-soft/haze": over((147, 173, 124, 0.14), D_SURFACE_HAZE),
    "danger/surf-haze": over((168, 21, 42, 0.22), D_SURFACE_HAZE),
}

d_texts = {
    "text oat-100": hex_rgb("#f1ebdd"),
    "muted pine-300": hex_rgb("#b3c0b2"),
    "dim pine-400": hex_rgb("#8a9a8b"),
    "accent-text m300": hex_rgb("#b9cca6"),
    "moss-400 fill": hex_rgb("#93ad7c"),
    "highlight oat-200": hex_rgb("#e6dcc8"),
    "walnut-300": hex_rgb("#c9a27c"),
    "ok fern-300": hex_rgb("#8fcf97"),
    "pending lake-300": hex_rgb("#8db8cf"),
    "idle pine-400": hex_rgb("#8a9a8b"),
    "warning lichen": hex_rgb("#d9bb6a"),
    "danger rowan-400": hex_rgb("#f05a63"),
    "danger-txt r300": hex_rgb("#ff8088"),
    "info heather-300": hex_rgb("#bba6cc"),
    "knob pine-300": hex_rgb("#b3c0b2"),
}
table(d_surfaces, d_texts)

print()
print("Text on the dark accent fill (--color-on-accent):")
moss400 = hex_rgb("#93ad7c")
print(f"  pine-950 on moss-400    {ratio(D_BG, moss400):6.2f}")
print(f"  pine-950 on moss-300    {ratio(D_BG, hex_rgb('#b9cca6')):6.2f}  (hover)")
print(f"  oat-100 on moss-400     {ratio(hex_rgb('#f1ebdd'), moss400):6.2f}  (why on-accent is dark here)")
print(f"  pine-950 on walnut-300  {ratio(D_BG, hex_rgb('#c9a27c')):6.2f}")

print()
print("Separation (dark): accent vs OK, warning vs danger, secondary vs warning and danger")
separation([
    (("moss-400", moss400), ("fern-300", d_texts["ok fern-300"])),
    (("lichen-300", d_texts["warning lichen"]), ("rowan-400", d_texts["danger rowan-400"])),
    (("walnut-300", d_texts["walnut-300"]), ("lichen-300", d_texts["warning lichen"])),
    (("walnut-300", d_texts["walnut-300"]), ("rowan-400", d_texts["danger rowan-400"])),
])
