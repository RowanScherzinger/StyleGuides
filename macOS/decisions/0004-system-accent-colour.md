# 0004. The user's accent colour

Date: 2026-11-08
Status: proposed

## Decision
The accent is the user's macOS accent colour, held in four tokens (light, dark, increased
contrast light and dark), blue by default. A named accent maps to the system colour of the
same name (graphite to gray). As text, light mode uses the increased-contrast shade.

## Why
A default Mac app uses the system accent; a fixed blue looks wrong for anyone who picked
another. macOS names a fixed set of accents, and the HIG publishes four shades for each
system colour, so the tokens can carry them all. Apple's default light blue as text is
3.5:1 on white, so links use the darker IC shade, as AppKit's own `linkColor` is darker than
the accent. Matching the named accents to the system colours is an approximation: on a Mac,
read `controlAccentColor` instead.

## Affects
`--palette-accent*`, `--color-accent*` in `tokens/tokens.css`; `docs/01-color.md`, `docs/07-theming.md`.
