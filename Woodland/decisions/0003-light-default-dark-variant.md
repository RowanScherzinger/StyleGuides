# 0003. Light by default, with a dark variant

Date: 2026-10-24
Status: proposed

## Decision
Light is the default (`:root`): an oat-paper field with linen cards and bark-brown ink.
A dark variant is switched with `data-theme="dark"` on `<html>`: a pine-black field with moss
glass cards and oat text. Only semantic tokens change between them.

## Why
"Soft, earthy, natural" reads most naturally as daylight on paper; a dark forest is the
mood for night. Rejected: dark only (heavier and less soft), light only (no night mode for apps
used in the evening). An attribute rather than only `prefers-color-scheme` lets an app offer a
toggle and still follow the OS (snippet in `docs/07-theming.md`).

Moss as a fill has to change shade between the two: moss-600 with oat text in light (5.5:1),
the lighter moss-400 with pine-black text in dark (7.4:1). So `--color-on-accent` flips
between the variants.

## Affects
`:root` and `:root[data-theme="dark"]` in `tokens/tokens.css`, `docs/01-color.md`,
`docs/07-theming.md`, `tools/contrast.py`, `examples/preview.html`.
