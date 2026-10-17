# Style Guides

Visual style guides for my personal apps. No application code: each folder is a
self-contained guide (design tokens, shared CSS, rules and the reasons behind them)
that apps copy from.

| Guide | Look | For |
|---|---|---|
| [`JarvisApps/`](JarvisApps/README.md) | Iron Man style HUD: dark only, warm metallics, glass, monospace readouts | Home-lab dashboards and tools (web and Electron) |

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
