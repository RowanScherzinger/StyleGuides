# 0008. One `light-dark()` pair per colour

Date: 2026-11-08
Status: proposed

## Decision
Each semantic colour is written once as `light-dark(<light>, <dark>)`, and the appearance is
chosen by `color-scheme` (`light dark` by default; forced by `data-theme`). Increase Contrast
overrides some pairs in one `prefers-contrast: more` block.

## Why
Following the system and allowing an override would otherwise need the dark values twice,
which drift apart. It needs Safari 17.5, Chrome 123, Firefox 120 or Electron 30 (2024), which
is fine for personal apps. Same approach as the Win11 guide, so the two stay easy to compare.

## Affects
`tokens/tokens.css`; `docs/07-theming.md`.
