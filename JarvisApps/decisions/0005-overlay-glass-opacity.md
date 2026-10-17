# 0005. Overlay glass is 84% opaque

Date: 2026-10-17
Status: proposed

## Decision
Glass that floats over the desktop wallpaper (Desktop-Widgets) uses
`--color-surface-overlay: rgba(6, 4, 4, 0.84)`, up from the current 0.38.

## Why
In a transparent Electron window, CSS `backdrop-filter` cannot blur the desktop behind it,
so the tint alone has to make text readable. Measured with `tools/contrast.py` over a
pure white wallpaper (the worst case):

| Tint | Body text | Muted text | Gold |
|---|---|---|---|
| 0.38 (current) | 1.76 | 1.04 | 1.10 |
| 0.72 | 5.93 | 3.49 | 3.71 |
| **0.84** | **9.35** | **5.50** | **5.84** |

0.84 is the lowest tint where text, muted text, gold and ember all pass 4.5:1. That's
less see-through than the current widgets. If that's too heavy, the alternative is a lower
tint plus a dark text halo on every label. That approach is weaker, and dim text would
still fail.

## Affects
`tokens/tokens.css`, `docs/07-theming.md`, `docs/01-color.md`.
