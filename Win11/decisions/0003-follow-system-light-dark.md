# 0003. Follow the system's light or dark mode

Date: 2026-11-08
Status: accepted (following the system); proposed (the override attribute)

## Decision
Light and dark are both first-class, and by default the app follows Windows' "Choose your mode"
setting, live. An app may also offer a forced light or dark choice through
`data-theme="light" | "dark"` on `<html>`.

## Why
The user asked for the theme to follow the system light/dark theme. The override exists
because some apps have a settings page where users expect "Light / Dark / Use system setting",
as Windows apps do.

## Affects
`color-scheme` and every `light-dark()` in `tokens/tokens.css`; `docs/07-theming.md`.
