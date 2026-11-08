# Colour

Tokens: `--palette-*` (raw) and `--color-*` (semantic) in `tokens/tokens.css`.
Components use semantic tokens only. Each semantic colour is a `light-dark()` pair, so it
switches with the appearance (`07-theming.md`).

## Palette

Apple's twelve system colours plus gray, each in four variants: light, dark, increased
contrast light and increased contrast dark (`--palette-red`, `--palette-red-dark`,
`--palette-red-ic`, `--palette-red-ic-dark`). The values are from HIG > Color >
Specifications (decisions/0001). Apple says the values may change between releases: re-copy
them, don't adjust by eye.

| Colour | Light | Dark | IC light | IC dark |
|---|---|---|---|---|
| Red | `#ff383c` | `#ff4245` | `#e9152d` | `#ff6165` |
| Orange | `#ff8d28` | `#ff9230` | `#c55300` | `#ffa056` |
| Yellow | `#ffcc00` | `#ffd600` | `#a16a00` | `#fedf43` |
| Green | `#34c759` | `#30d158` | `#008932` | `#4ad968` |
| Blue | `#0088ff` | `#0091ff` | `#1e6ef4` | `#5cb8ff` |
| Purple | `#cb30e0` | `#db34f2` | `#b02fc2` | `#ea8dff` |
| Pink | `#ff2d55` | `#ff375f` | `#e7124d` | `#ff8ac4` |
| Gray | `#8e8e93` | `#8e8e93` | `#6c6c70` | `#aeaeb2` |

Mint, teal, cyan, indigo and brown are in `tokens.css` too (default variants only). Gray is
published for iOS only; SwiftUI's `Color.gray` is the same colour.

The **accent** is four `--palette-accent*` tokens, blue by default (decisions/0004).

## Roles

Apple names these colours but doesn't publish their values. The values are *(Proposed)*:
close to what AppKit draws (decisions/0001).

| Role | Light | Dark | Token | AppKit |
|---|---|---|---|---|
| Window | `#ececec` | `#323232` | `--color-bg` | `windowBackgroundColor` |
| Toolbar (solid) | `#f6f6f6` | `#2b2b2b` | `--color-bg-elevated` | |
| Sidebar (solid) | `#e3e3e3` | `#282828` | `--color-sidebar` | |
| List, table, text view | white | `#1e1e1e` | `--color-content` | `controlBackgroundColor` |
| Grouped box | black 4% | white 5% | `--color-surface` | |
| Push button | white | white 20% | `--color-control` | `controlColor` |
| Menu, popover, alert | `#f6f6f6` | `#2b2b2b` | `--color-surface-raised`, `--color-dialog` | |
| Text | black 85% | white 85% | `--color-text` | `labelColor` |
| Secondary text | black 50% | white 55% | `--color-text-muted` | `secondaryLabelColor` |
| Tertiary, placeholder | black 26% | white 25% | `--color-text-dim` | `tertiaryLabelColor` |
| Separator | black 10% | white 10% | `--color-border` | `separatorColor` |
| Accent fill | blue | blue dark | `--color-accent` | `controlAccentColor` |
| Accent text, links | blue IC | blue dark | `--color-accent-text` | `linkColor` |
| Text on accent | white | white | `--color-on-accent` | `alternateSelectedControlTextColor` |
| Selection, focused list | accent | accent | `--color-selection` | `selectedContentBackgroundColor` |
| Selection, unfocused | `#dcdcdc` | `#464646` | `--color-selection-inactive` | `unemphasizedSelectedContentBackgroundColor` |

**The accent** marks: the default button, selected rows in a focused list, highlighted menu
items, switches, check boxes and radios that are on, progress, links, sidebar icons and the
focus ring. HIG > Color: apply it to the background of one primary control, not to many.

## Status

One colour **and** one shape per state. Status words are written in `--color-text`, next to a
glyph in the status colour (`06-iconography.md`).

| State | Light | Dark | Token | Glyph |
|---|---|---|---|---|
| OK / done | green IC | green dark | `--color-status-ok` | Filled dot |
| Pending | accent | accent | `--color-status-pending` | Half-filled ring |
| Idle / off | gray IC | gray | `--color-status-idle` | Ring |
| Warning | orange IC | orange dark | `--color-status-warning` | Triangle |
| Error | red IC | red dark | `--color-status-danger` | Octagon |
| Info | accent | accent | `--color-info` | Small dot |

*(Proposed)* Light mode uses the increased-contrast shades for status, because Apple's
defaults are made for fills, not marks: default green is 1.9:1 on the window. Warning is
orange, not yellow: yellow measures 1.3:1 on the window. Each has a faint fill for callouts
(`--color-ok-fill` and so on). The destructive button uses system red (`--color-danger`).

## Measured contrast

From `python tools/contrast.py`, default blue. Box = `--color-surface` over the window.

| Text | Light: window | Light: content | Dark: window | Dark: content |
|---|---|---|---|---|
| Text | 13.3 | 15.1 | 9.7 | 12.3 |
| Secondary | **3.8** | **4.0** | 5.1 | 5.9 |
| Tertiary | 1.9 | 1.9 | 2.2 | 2.3 |
| Accent text | **3.9** | 4.6 | **4.0** | 5.2 |
| OK | **3.8** | 4.5 | 6.3 | 8.3 |
| Warning | **3.9** | 4.6 | 5.7 | 7.5 |
| Error | **3.9** | 4.6 | **3.7** | 4.9 |
| Idle | 4.4 | 5.2 | **3.9** | 5.1 |

- White on the accent fill: 3.5 (light), 3.2 (dark). White on the destructive red: 3.6 / 3.4.
- Text on a push button: 5.4 (dark). Red text on a push button: 4.6 (light) but 2.0 (dark),
  which is why the dark destructive button is a red fill instead (`--color-danger-button`).
- White chip text on `--color-scrim` over a white photo: 4.7.
- Apple's default blue as text would be 3.0 on the window, default green 1.9, default yellow 1.3.
- With Increase Contrast: secondary 7.9 (light) / 8.0 (dark), white on accent 4.6 (light).
  Dark keeps the default accent fill: white on the IC blue would be 2.2.

Rules that follow from the numbers:

- **Secondary text fails AA in light (3.8:1), and so does Apple's.** Use it for supporting
  text only. Anything the user must read is `--color-text`.
- **Coloured text in light reaches 4.5 only on content backgrounds** (lists, tables, text
  views). On the window, coloured text must be bold, which HIG > Accessibility allows at 3:1,
  or be replaced by a glyph plus normal text.
- **Text on the accent fill is 3.2 to 3.5:1, the system's own choice.** Keep labels on
  accent fills short and bold where you can (default button, selected row). Increase Contrast
  lifts light mode to 4.6.
- Tertiary text is for placeholders and watermarks only. Disabled text is exempt, as WCAG allows.
- The check box and radio outline (`--color-border-strong`) is 1.7:1 in light, below the 3:1
  WCAG asks for control edges. That is AppKit's look; Increase Contrast fixes it (4.6).

## Other accents

Check another accent by passing its four shades, light, dark, IC light and IC dark:
`python tools/contrast.py 8e8e93 8e8e93 6c6c70 aeaeb2` (graphite: accent text 4.4 / 3.9,
white on accent 3.3).
