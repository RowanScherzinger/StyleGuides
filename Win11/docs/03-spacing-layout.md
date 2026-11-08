# Spacing and layout

## Scale

A 4px grid: `--space-1` (4px) to `--space-14` (56px). Every margin, gap and padding is a step.

| Gap | Value | Where |
|---|---|---|
| Between related cards | 4px (`--space-1`) | A stack of settings cards |
| Between controls | 8px (`--space-2`) | Buttons in a row |
| Control to its label | 8–12px | Label above a text box |
| Inside a card | 16px (`--space-4`) | Card padding |
| Between groups | 24–32px | A body-strong group header above cards |
| Dialog padding | 24px (`--space-6`) | |
| Page margin | 36px narrow, 56px wide | `--space-9`, `--space-14` |

## Sizes

| Thing | Size | Token |
|---|---|---|
| Button, text box, combo box | 32px high | `--control-height` |
| Compact control | 24px | `--control-height-small` |
| List row | 40px | `--list-item-height` |
| Navigation item | 36px | `--nav-item-height` |
| Title bar | 48px with navigation, 32px minimum | `--titlebar-height` |
| Navigation pane | 320px open, 48px compact | `--nav-pane-width`, `--nav-pane-compact` |
| Buttons | at least 120px wide when they have text | |
| Touch targets | at least 40×40px | |

## Composition

The standard Windows 11 app frame:

1. **Window** (`--color-bg`): the title bar and navigation pane sit directly on it.
2. **Content layer** (`.layer`): one panel to the right of the navigation, rounded 8px at its
   top-left corner only, with a hairline.
3. **Cards** on the layer, in a single column up to about 1000px wide, left-aligned.

Apps without navigation put the content layer under the toolbar, or skip it and put cards
on the window. A toolbar or command bar uses `--color-bg-elevated`.

## Breakpoints *(Proposed)*

| Width | Navigation | Page margin |
|---|---|---|
| Under 640px | Hidden behind a menu button | 16px |
| 640–1007px | Compact (48px icons) | 36px |
| 1008px and up | Open (320px) | 56px |

These follow NavigationView's default thresholds.
