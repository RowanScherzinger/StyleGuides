# 0004. Typefaces

Date: 2026-10-24
Status: proposed

## Decision
Fraunces for titles and big numbers, with its soft axis at 100 (`"SOFT" 100, "WONK" 0`).
Nunito Sans for UI text. Cascadia Mono for timestamps and code.

## Why
A soft, old-style serif gives the natural, field-guide feel; Fraunces' soft axis rounds its
serifs so it stays gentle rather than bookish. Nunito Sans is calm and very readable at small
sizes, and its slightly rounded shapes match. Both are free on Google Fonts. Rejected: a
fully rounded display face (reads as playful, not earthy), Lora or Merriweather for titles
(no soft axis, sharper at large sizes).

## Affects
`--font-*` in `tokens/tokens.css`, `docs/02-typography.md`.
