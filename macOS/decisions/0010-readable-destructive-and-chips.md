# 0010. Readable destructive buttons and photo chips

Date: 2026-11-08
Status: proposed

## Decision
The destructive push button is bold system red text on the bezel in light, and a system red
fill with bold white text in dark. Chips over photos sit on black at 55% (`--color-scrim`) with
white text.

## Why
Measured with `tools/contrast.py`: red text on the dark grey bezel is 2.0:1 (2.2 on an alert),
below even the 3:1 bold allowance. A red fill with white text is 3.4:1, which passes as bold.
For chips, the HIG's 35% dimming layer (meant for under clear glass) gives white text 2.4:1
over a white photo; 55% gives 4.7:1.

## Affects
`--color-danger-button*`, `--color-scrim` in `tokens/tokens.css`; `.btn--destructive` in
`css/macos.css`; `docs/01-color.md`, `docs/04-components.md`, `docs/07-theming.md`.
