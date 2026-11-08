# 0003. Follow the system's appearance

Date: 2026-11-08
Status: proposed

## Decision
Light and dark are both first-class, and by default the app follows System Settings >
Appearance, live. An app may offer a forced choice through `data-theme="light" | "dark"` on
`<html>`. Increase Contrast, Reduce Transparency and Reduce Motion are followed too.

## Why
A default Mac app follows the appearance setting, and the Win11 partner follows its system
the same way (Win11 decision 0003, which the user chose there). Proposed here because the user
hasn't said it for this guide.

## Affects
`color-scheme`, every `light-dark()` and the media queries in `tokens/tokens.css`; `docs/07-theming.md`.
