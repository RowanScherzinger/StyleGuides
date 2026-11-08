# 0007. Native apps mirror the tokens

Date: 2026-11-08
Status: proposed

## Decision
Native Windows apps copy the tokens by hand into one theme class, read light/dark and the accent
palette from the registry and follow changes live, leave the title bar colours to Windows, and
pre-blend translucent fills where native controls can't draw them.

## Why
The first app to use this look is a WinForms app (Phone Explorer), which can't read CSS. Leaving
the title bar to Windows keeps the user's "accent colour on title bars" setting working, which
a default Windows app would respect.

## Affects
`docs/07-theming.md`.
