# Theming *(Proposed, decisions/0003)*

## Variants

| Variant | How |
|---|---|
| Light (default): a sunlit clearing | nothing to set |
| Dark: the forest at night | `<html data-theme="dark">` |

`tokens.css` sets `color-scheme` to match, so form controls and scrollbars follow. An app
chooses how to pick the variant: a toggle, the OS setting, or both. To follow the OS:

```js
const dark = matchMedia("(prefers-color-scheme: dark)");
const apply = () => document.documentElement.dataset.theme = dark.matches ? "dark" : "light";
apply(); dark.addEventListener("change", apply);
```

Only semantic tokens (`--color-*`, `--shadow-*`, `--glow-*`, `--texture-grain`) change between
variants. Palette tokens don't, which is why components must not use them.

## The field

`.wood-root` paints three layers: the paper grain, the haze, then `--color-bg`.

- **Haze**: dappled light. In light, a moss glow top-left and warm sun top-right (0.16 each).
  In dark, a faint moss glow top-left and a lantern glow bottom-right.
- **Grain**: SVG fractal noise at 5% (light) or 3.5% (dark). Keep it barely visible.

`tools/contrast.py` measures text at the haze's strongest point. Don't make the haze stronger
without rerunning it.

## Glass

Cards are lightly frosted: linen at 0.80 with a 12px blur in light, moss-tinted pine at 0.62
with a 16px blur in dark.

## Per-app tint

Not yet decided. If an app needs its own character, change `--color-secondary` (for example
lake instead of walnut), never the moss.

## Browser extensions

Dark-mode extensions (such as Dark Reader) recolour the light variant. If the preview looks
dark and muddy in light mode, turn the extension off for the page.
