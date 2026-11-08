# 0005. Organic shape, paper grain and warm depth

Date: 2026-10-24
Status: proposed

## Decision
- Rounded but not bubbly: cards 18px, buttons and inputs 12px, chips and toggles pills.
- One "pebble" card per screen at most: an uneven river-stone radius (`--radius-pebble`).
- A faint paper grain (`--texture-grain`, SVG noise at 5% in light, 3.5% in dark) over the field.
- Depth is a low, warm-brown blurred shadow in light and a soft black one in dark. No hard offsets.
- Buttons press down 1px instead of squishing.

## Why
Natural things are soft-edged but not perfectly round; full pills everywhere read as cute
rather than earthy, and sharp corners read as technical. The grain and warm shadows stop the
page feeling like flat screen colour. The grain sits under the cards, so it doesn't affect
text contrast.

## Affects
`--radius-*`, `--shadow-*`, `--texture-grain` in `tokens/tokens.css`, `.card--pebble` and
`.wood-root` in `css/woodland.css`, `docs/04-components.md`, `docs/07-theming.md`.
