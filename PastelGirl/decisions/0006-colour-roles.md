# 0006. Colour roles

Date: 2026-10-17
Status: proposed

## Decision
- Pink is the accent, cream is text and big numbers, lilac is secondary, plum is the field.
- Other pastels (mint, baby blue, butter, peach) are guests for status and charts, two per
  screen at most as decoration. Status glyphs are exempt.
- Text on pastel fills is dark plum. Pink and lilac words use `-text` tokens, which become
  deep inks in the light variant (0008).
- Danger is cherry red `#ff5247`, the only saturated colour, with `#ff6a5e` for danger text.

## Why
- Pinks and creams lead (0002). The "two or three pastels" limit comes from the reference article.
- Cream on pink measures 1.7:1, so fills need dark text.
- A pink-red danger would blend with pink buttons. Cherry sits 27° of hue away from the
  accent at full saturation (measured in `tools/contrast.py`).

## Affects
`--color-*` in `tokens/tokens.css`, `docs/01-color.md`.
