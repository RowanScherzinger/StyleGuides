# Theming

## Variants

| Variant | How | Status |
|---|---|---|
| Dark (default) | nothing to set | accepted direction (0002) |
| Light | `<html data-theme="light">` | the user wants a light variant (0008); values *(Proposed)* |

`tokens.css` sets `color-scheme` to match, so form controls and scrollbars follow.

*(Proposed)* Dark is the default. An app chooses how to pick the variant: a toggle, the OS
setting, or both. To follow the OS:

```js
const light = matchMedia("(prefers-color-scheme: light)");
const apply = () => document.documentElement.dataset.theme = light.matches ? "light" : "dark";
apply(); light.addEventListener("change", apply);
```

Only semantic tokens (`--color-*`, `--shadow-*`, `--glow-*`) change between variants. Palette
tokens don't, which is why components must not use them.

## The field

`.soft-root` paints `--color-bg-haze` (a faint pink glow top-left and lilac glow
bottom-right) over `--color-bg`. Keep it faint: the cards are the content, not the background.
The light haze is stronger (0.18) because pink on cream needs more to show.

## Glass

Cards are frosted glass with an 18px blur: plum in dark, white at 0.70 in light. The haze
lightens what's behind the glass, so the worst case is a card at the haze's brightest point;
`tools/contrast.py` measures it (`surface/haze`) for both variants. Don't make the haze
stronger without rerunning it.

## Per-app tint

Not yet decided. If an app needs its own character, change `--color-secondary` (for example
mint instead of lilac), never the pink.
