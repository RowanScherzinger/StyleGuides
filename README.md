# Style Guides

Visual style guides for my personal apps. No application code: each folder is a
self-contained guide (design tokens, shared CSS, rules and the reasons behind them)
that apps copy from.

| Guide | Look | For |
|---|---|---|
| [`JarvisApps/`](JarvisApps/README.md) | Iron Man style HUD: dark only, warm metallics, glass, monospace readouts | Home-lab dashboards and tools (web and Electron) |
| [`PastelGirl/`](PastelGirl/README.md) | Very cute, soft and round: pinks and creams, dark by default with a light variant, frosted round cards, pills, hearts and sparkles | Planned: an optional theme in iPhone Explorer |
| [`Woodland/`](Woodland/README.md) | Soft, earthy and natural: moss greens on oat paper with bark ink, light by default with a night-forest dark variant, leaf, fern, pine, mushroom and acorn motifs | TBD |

Guides are independent. Each app names the guide it follows in its own `CLAUDE.md` (or the
guides it offers, if it lets the user pick a theme).

## Layout of a guide

Each guide follows the same shape:

```
<Guide>/
  README.md     what it is, who uses it, how to adopt it
  CLAUDE.md     rules for an agent editing or applying the guide
  tokens/       design tokens (single source of truth for values)
  css/          shared primitives built on the tokens
  docs/         one file per topic (colour, type, layout, components...)
  decisions/    one file per decision, with the reason
  examples/     a preview page that renders the guide
  tools/        checks, e.g. contrast
```

## Adding a guide

Make a new top-level folder with the same layout, and add a row to the table above.
