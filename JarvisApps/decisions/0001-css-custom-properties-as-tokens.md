# 0001. CSS custom properties are the token format

Date: 2026-10-17
Status: accepted

## Decision
All design tokens live in one file, `tokens/tokens.css`, as CSS custom properties.
There is no JSON source and no build step.

## Why
Every app that uses this guide (Jarvis, Larder, Desktop-Widgets, Plox) renders in a
browser or Electron, so CSS variables work in all of them directly. A JSON source with
a generator would only pay off if a non-web consumer appeared (for example the Unity
game); revisit then.

## Affects
`tokens/tokens.css`, `README.md`.
