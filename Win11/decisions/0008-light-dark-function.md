# 0008. One `light-dark()` pair per colour

Date: 2026-11-08
Status: proposed

## Decision
Each semantic colour is written once as `light-dark(<light>, <dark>)`, and the variant is
chosen by `color-scheme` (`light dark` by default; forced by `data-theme`).

## Why
Following the system and allowing an override would otherwise need the dark values twice (in a
`prefers-color-scheme` block and in a `data-theme="dark"` block), which drift apart. One pair
per token can't. The cost is browser support from 2024 (Chrome 123, Firefox 120, Safari 17.5,
Electron 30), which is fine for personal apps. Shadows can't use `light-dark()`, so they read
two colour tokens that do.

## Affects
`tokens/tokens.css`; `docs/07-theming.md`.
