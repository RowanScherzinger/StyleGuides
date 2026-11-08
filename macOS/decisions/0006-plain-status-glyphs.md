# 0006. Plain status glyphs, with an octagon for error

Date: 2026-11-08
Status: proposed

## Decision
In dense places, status is a small plain shape next to words: filled dot (OK), half-filled
ring (pending), ring (idle), triangle (warning), octagon (error), small dot (info). In light
mode the glyphs use the increased-contrast system colours; warning is orange, not yellow.

## Why
Each state needs its own shape so colour isn't the only signal. The shapes match SF Symbols
(`circle.fill`, `circle.lefthalf.filled`, `exclamationmark.triangle.fill`, `xmark.octagon.fill`),
so they read the Mac way; the octagon replaces Win11's crossed ring because it is Apple's error
shape. Apple's default light green is 1.9:1 and yellow 1.3:1 on the window, too pale for
small marks, so light mode takes the IC shades (3.8 to 3.9:1).

## Affects
`--color-status-*` in `tokens/tokens.css`; `.status--*` in `css/macos.css`; `docs/01-color.md`, `docs/06-iconography.md`.
