# Colour

Tokens: `--palette-*` (raw) and `--color-*` (semantic) in `tokens/tokens.css`.
Components use semantic tokens only. Each semantic colour is a `light-dark()` pair, so it
switches with the variant (`07-theming.md`).

Values are WinUI's (decisions/0001); the WinUI resource name is beside each token.

## Palette

The only palette is the **accent**: seven shades Windows derives from the user's accent colour
(decisions/0004). The defaults are Windows blue.

| Token | Default | Used as |
|---|---|---|
| `--palette-accent-light-3` | `#99ebff` | Accent text in dark |
| `--palette-accent-light-2` | `#60cdff` | Accent fill in dark |
| `--palette-accent-light-1` | `#0093f9` | |
| `--palette-accent-base` | `#0078d4` | The user's chosen colour |
| `--palette-accent-dark-1` | `#005fb8` | Accent fill in light |
| `--palette-accent-dark-2` | `#003e92` | Accent text in light |
| `--palette-accent-dark-3` | `#001968` | |

Everything else is neutral grey, or a status colour.

## Roles

| Role | Light | Dark | Tokens |
|---|---|---|---|
| Window | `#f3f3f3` | `#202020` | `--color-bg` |
| Toolbar, title area | `#f9f9f9` | `#282828` | `--color-bg-elevated` |
| Content layer | white 50% | grey 30% | `--color-layer` |
| Card | white 70% | white 5% | `--color-surface*` |
| Control (button, input) | white 70% | white 6% | `--color-control*` |
| Flyout, menu | `#f9f9f9` | `#2c2c2c` | `--color-surface-raised` |
| Dialog | `#ffffff` | `#2b2b2b` | `--color-dialog*` |
| Text | black 89% | white | `--color-text` |
| Secondary text | black 62% | white 77% | `--color-text-muted` |
| Tertiary text | black 45% | white 53% | `--color-text-dim` |
| Accent fill | dark-1 | light-2 | `--color-accent*` |
| Accent text, links | dark-2 | light-3 | `--color-accent-text` |
| Text on accent | white | black | `--color-on-accent` |

**The accent** marks: the primary button, selected items (a short pill on the row's left
edge), toggles and check boxes that are on, progress, links and focusable "on" states. Use it
for one primary action per view.

**Strokes** do the separating. Controls have a hairline (`--color-border`) with a slightly
darker bottom edge (`--color-border-secondary`), cards have `--color-card-border`, and
check boxes, radios and toggles use `--color-border-strong`.

*(Proposed, not WinUI)* `--color-accent-soft` (accent at 12%) and `--color-selection` (22%)
for selected tiles in a grid, where a row's edge pill doesn't fit. `--color-scrim` for
chips over photos: the window colour, nearly opaque, so chip text keeps its contrast on
any image.

## Status

One colour **and** one shape per state. In messages use an InfoBar (`04-components.md`); in
lists use the small status glyphs (`06-iconography.md`).

| State | Light | Dark | Token | Glyph |
|---|---|---|---|---|
| OK / done | `#0f7b0f` | `#6ccb5f` | `--color-status-ok` | Filled dot |
| Pending | accent | accent | `--color-status-pending` | Half-filled ring |
| Idle / off | `#8a8a8a` | `#9d9d9d` | `--color-status-idle` | Ring |
| Warning | `#9d5d00` | `#fce100` | `--color-status-warning` | Triangle |
| Error | `#c42b1c` | `#ff99a4` | `--color-status-danger` | Ring with a cross |
| Info | accent | accent | `--color-info` | Small dot |

Each has a background for InfoBars: `--color-ok-fill`, `--color-warning-fill`,
`--color-danger-fill`, `--color-info-fill`. Text on those fills is the normal text colour.

Pending and info use the accent, as WinUI's "attention" does. *(Proposed)* the glyph shapes
(decisions/0006).

## Measured contrast

From `python tools/contrast.py`, default blue accent. Layer = `--color-layer` over the
window; card = `--color-surface` over the layer.

| Text | Light: window | Light: card | Dark: window | Dark: card |
|---|---|---|---|---|
| Text | 15.7 | 16.9 | 16.3 | 12.6 |
| Secondary (muted) | 6.0 | 6.2 | 10.2 | 8.3 |
| Tertiary (dim) | **3.3** | **3.3** | 5.5 | 4.8 |
| Disabled | 2.5 | 2.5 | 3.3 | 3.1 |
| Accent text | 9.0 | 9.8 | 12.2 | 9.4 |
| OK | 4.9 | 5.4 | 8.0 | 6.2 |
| Warning | 4.7 | 5.2 | 12.3 | 9.6 |
| Error | 5.1 | 5.6 | 8.0 | 6.2 |
| Idle | 3.1 | 3.4 | 6.0 | 4.7 |

- Text on the accent fill: 6.3 (light), 11.7 (dark).
- Error text on its own fill: 4.8 (light), 6.6 (dark). Normal text on any status fill: 11.3+.
- Chip text on `--color-scrim`, over the worst photo: 8.5 (light), 13.0 (dark).

Rules that follow from the numbers:

- **Tertiary text fails AA in light (3.3:1).** Use it only for placeholders, hints and
  information repeated elsewhere. Anything the user must read is secondary or better.
- Disabled text is exempt from contrast rules, as WCAG allows. Never use it for anything else.
- The idle grey (3.1 in light) is for glyphs, which need 3:1, not for text.

## Other accents

Windows lets the user pick any accent. Check a different one by passing its seven shades:
`python tools/contrast.py e6e5e1 a6a5a1 7c7a77 4c4a48 413f3d 272524 100d0d` (the graphite
accent: accent text 13.8 light / 12.9 dark, on-accent 10.5 / 8.5). Windows picks shades that
keep these readable, so an app doesn't need to adjust them.
