# 0010. Cute status glyphs

Date: 2026-10-17
Status: proposed

## Decision
OK is a mint filled heart, pending a butter crescent moon, idle a mauve hollow heart, warning a
peach rounded triangle with "!", error a cherry broken heart, info a baby-blue dot.
Supersedes 0007.

## Why
"Very cute" (0009) applies to warnings and errors too, so the plain circled cross became a
broken heart. Each state still has a distinct shape (whole, hollow and cracked hearts, a moon,
a triangle, a dot), a distinct colour, and is always shown with words, so cute never makes a
problem easy to miss.

## Affects
`--color-status-*`, `docs/01-color.md`, `docs/06-iconography.md`, `examples/preview.html`.
