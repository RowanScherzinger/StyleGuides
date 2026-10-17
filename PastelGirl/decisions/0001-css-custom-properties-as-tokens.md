# 0001. CSS custom properties as tokens

Date: 2026-10-17
Status: proposed

## Decision
All values live as CSS custom properties in `tokens/tokens.css`, in three layers: palette,
semantic, scales. Apps copy the file. No build step.

## Why
Same approach as the other guides in this repo: works in any web stack without tooling, and
a single file is easy to copy and diff.

## Affects
`tokens/tokens.css`, every doc.
