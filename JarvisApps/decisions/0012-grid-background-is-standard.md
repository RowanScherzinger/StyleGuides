# 0012. The grid background is standard in every app

Date: 2026-10-28
Status: accepted

## Decision
- `.hud-grid-bg` (warm black, a faint 24px grid, a copper vignette at the top) is the page
  background of every app, on `<body>`. It was optional and kept off text-heavy pages.
- It uses `background-attachment: fixed`, so the grid holds still while content scrolls.
- Desktop-Widgets is the exception: it has no page background.

## Why
User decision, after seeing it on a home-lab dashboard: "I'd like that nice grid background
that the home-lab dashboard has. That should be a staple in the Jarvis style guide."
The grid is 2.5% opacity, so it doesn't hurt reading on text-heavy pages.

`fixed` is Claude's addition. On a long scrolling page (a transaction list), a scrolling
background stretches the top vignette down the whole page height. Fixed keeps the vignette
at the top of the view and reads as a HUD over a still field. Where `fixed` isn't supported
(iOS Safari), it falls back to scrolling, which still looks fine.

## Affects
`css/hud.css`, `docs/07-theming.md`, `CLAUDE.md`.
