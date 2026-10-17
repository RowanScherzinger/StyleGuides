# 0008. Light variant

Date: 2026-10-17
Status: accepted (the variant); proposed (the values and mechanism)

## Decision
There is a light variant as well as the dark default. It is switched with
`data-theme="light"` on `<html>`, and redefines only semantic tokens: blush-cream field, white
frosted cards, plum ink text, the same pastel pink fills, and deep "ink" versions of every
pastel used as text or a glyph.

## Why
The user asked for a light variant; it supersedes "dark only" (0003). Pastels as text fail on
cream (pink is 1.8:1), so the light variant needs ink partners; all of them measure at least
4.5:1 on cards (`tools/contrast.py`). An attribute rather than only `prefers-color-scheme`
lets an app offer a toggle, and it can still follow the OS (snippet in `docs/07-theming.md`).

## Affects
`:root[data-theme="light"]` and the `-ink` palette in `tokens/tokens.css`, the new
`--color-accent-text`, `--color-secondary-text`, `--color-track` and `--color-series-muted`
tokens, `docs/01-color.md`, `docs/07-theming.md`, `tools/contrast.py`, `examples/preview.html`.
