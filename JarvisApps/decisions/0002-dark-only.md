# 0002. Dark only, no light theme

Date: 2026-10-17
Status: accepted

## Decision
Every app is dark. There is no light theme, no theme switch, and `prefers-color-scheme`
is ignored.

## Why
User decision: "Dark - don't waste time on a light theme." The HUD look depends on light
lines and glow on a dark field, and doesn't translate to a light theme.

## Affects
`tokens/tokens.css` (`color-scheme: dark`, light-theme blocks removed), `docs/07-theming.md`.
