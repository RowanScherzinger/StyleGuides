# 0006. Typefaces: Cascadia Mono, Inter, Orbitron

Date: 2026-10-17
Status: proposed

## Decision
- `--font-mono`: Cascadia Mono, falling back to DM Mono. This is the default UI voice.
- `--font-sans`: Inter, for prose only.
- `--font-display`: Orbitron, falling back to Bahnschrift, for uppercase labels and headings only.
- Fonts are self-hosted as woff2. Syne (used in Desktop-Widgets settings) is dropped.

## Why
- The user said "Campbell is what I use in the terminal". Campbell is a Windows Terminal
  colour scheme, not a font. Their Windows Terminal settings don't override the font, so
  they're seeing the default, Cascadia Mono.
- DM Mono and Orbitron are already in Desktop-Widgets.
- Inter is a widely used sans that stays readable at small sizes, which the user asked for
  ("sans-serif, easy to read").
- Three faces is the limit. A fourth (Syne) added noise without a role.

Campbell's ANSI colours (cool blue and green) are not used anywhere in the guide, not even
for log output.

## Affects
`tokens/tokens.css`, `docs/02-typography.md`.
