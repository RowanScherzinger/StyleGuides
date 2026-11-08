# Colour

Tokens: `--palette-*` (raw) and `--color-*` (semantic) in `tokens/tokens.css`.
Components use semantic tokens only: they are what switches between light and dark.

## Palette *(Proposed, decisions/0006)*

| Family | Key value | Use |
|---|---|---|
| Moss | `#4e6b3c` light / `#93ad7c` dark | `--palette-moss-800` to `-200`: the identity |
| Oat | `#f1ebdd` | `--palette-oat-50` to `-300`: light field, dark-variant text |
| Bark | `#2a2319` | `--palette-bark-900` to `-300`: light-variant text and muted tones |
| Pine | `#0f1712` | `--palette-pine-950` to `-300`: dark field, cards and muted text |
| Walnut | `#8a6444` / `#c9a27c` | Secondary: secondary chips, second chart series, progress |
| Fern | `#276b3a` / `#8fcf97` | Guest: OK status |
| Lake | `#33688a` / `#8db8cf` | Guest: pending status |
| Lichen | `#7a5d0c` / `#d9bb6a` | Guest: warning status |
| Heather | `#6c5288` / `#bba6cc` | Guest: info status |
| Rowan | `#a8152a` / `#f05a63` | Danger only |

Pairs are light-variant ink / dark-variant tone. Guests are never page backgrounds or large
cards. As decoration (chips, chart series, highlights) use two per screen at most. A status
list may show every status colour, because each is a small glyph with words.

## Roles *(Proposed)*

| Colour | Role | Tokens |
|---|---|---|
| **Moss** | Primary buttons, selection, focus, links, eyebrows, the one thing per card that leads. `--color-accent` for fills, `--color-accent-text` for words and icons. | `--color-accent*`, `--color-focus-ring`, `--color-selection` |
| **Bark / oat** | Text. Bark in light, oat in dark. | `--color-text*` |
| **Moss-800 / oat-200** | Big numbers | `--color-highlight` |
| **Walnut** | Secondary: secondary chips, the second chart series, progress fills | `--color-secondary*` |
| **Oat / pine** | Field and cards | `--color-bg`, `--color-surface*` |
| **Rowan** | Errors and destructive actions. Nothing else. | `--color-status-danger`, `--color-danger-*` |

**Text on the moss fill is `--color-on-accent`**: oat in light (5.5:1), pine-black in dark
(7.4:1). It flips because the moss changes shade; bark on light moss is only 2.6:1.

**Moss vs OK.** Both are green. Fern (OK) sits 40° of hue from moss in light and 36° in dark,
is fresher and bluer, and always comes with the sprout glyph and a label.

## Status *(Proposed, decisions/0007)*

One colour **and** one shape per state.

| State | Colour | Glyph | Motion |
|---|---|---|---|
| OK / done | `--color-status-ok` (fern) | Sprout | None |
| Pending | `--color-status-pending` (lake) | Half-filled circle | Slow breathe |
| Idle / off | `--color-status-idle` (bark-500 / pine-400) | Hollow pebble | None |
| Warning | `--color-status-warning` (lichen) | Rounded triangle with ! | None |
| Error | `--color-status-danger` (rowan) | Circle with × | None |
| Info | `--color-info` (heather) | Small dot | None |

## Measured contrast

From `python tools/contrast.py`. "Field" is the worst point of the field (where the haze is
strongest); "card" is `--color-surface` over that same point.

### Light (default)

| Text | On field | On card | On `accent-soft` |
|---|---|---|---|
| Text bark-900 | 10.7 | 13.7 | 11.7 |
| Muted bark-700 | 6.2 | 7.9 | 6.8 |
| Dim bark-600 | 4.7 | 6.1 | 5.2 |
| Moss words (moss-700) | 5.3 | 6.8 | 5.8 |
| Big numbers (moss-800) | 7.0 | 8.9 | 7.6 |
| Walnut ink | 4.7 | 6.0 | 5.1 |
| Fern ink (OK) | **4.4** | 5.7 | 4.9 |
| Lake ink (pending) | **4.2** | 5.3 | 4.5 |
| Lichen ink (warning) | **4.3** | 5.5 | 4.7 |
| Heather ink (info) | 4.5 | 5.8 | 4.9 |
| Rowan-700 (danger) | 5.2 | 6.6 | 5.6 |
| Idle glyph bark-500 | 2.9 | 3.7 | 3.1 |

- Danger text on the danger fill: 5.8. Oat on moss-600: 5.5 (7.0 on hover).
- Fern, lake and lichen ink pass as glyphs everywhere, but as text only on cards. Don't set
  status text on the bare field.
- The idle pebble (bark-500) is a glyph only, and only on cards (3.7, above the 3:1 for marks).
  Its label uses normal text. The off toggle knob is the same colour on the track.

### Dark variant

| Text | On field | On card | On `accent-soft` |
|---|---|---|---|
| Text oat-100 | 13.1 | 12.1 | 9.4 |
| Muted pine-300 | 8.3 | 7.6 | 5.9 |
| Dim pine-400 | 5.3 | 4.8 | **3.8** |
| Moss words (moss-300) | 9.1 | 8.4 | 6.5 |
| Moss fill (moss-400) | 6.3 | 5.8 | 4.5 |
| Big numbers (oat-200) | 11.5 | 10.6 | 8.2 |
| Walnut-300 | 6.7 | 6.1 | 4.8 |
| Fern / lake / lichen / heather | 7.0+ | 6.5+ | 5.0+ |
| Rowan-400 (glyphs, borders) | 4.7 | 4.3 | 3.4 |
| Rowan-300 (danger text) | 6.5 | 6.0 | 4.6 |

- Never put dim text on `accent-soft` in dark (3.8).
- Danger text uses `--color-danger-text` (rowan-300): 5.7 on the danger fill. Rowan-400 is for glyphs and borders.
- Pine-black on moss-400: 7.4 (10.6 on hover). Oat on it would be 2.1.

### Hue separation

| Pair | Light | Dark |
|---|---|---|
| Moss vs fern (accent vs OK) | 40° | 36° |
| Lichen vs rowan (warning vs danger) | 53° | 47° |
| Walnut vs rowan (secondary vs danger) | 35° | 33° |
| Walnut vs lichen (secondary vs warning) | **18°** | **14°** |

Walnut and lichen are the closest pair; the warning triangle and its words carry the difference.
Never use walnut for a status.
