# Colour

Tokens: `--palette-*` (raw) and `--color-*` (semantic) in `tokens/tokens.css`.
Components use semantic tokens only: they are what switches between dark and light.

## Palette

Lots of pinks and creams (decisions/0002). The values below are the dark default; the light
variant is at the end. The rest is *(Proposed)*.

| Family | Key value | Use |
|---|---|---|
| Plum-black | `#120b12` | `--palette-plum-950` to `-300`: field, card tint, muted text |
| Cream | `#fbefe3` | `--palette-cream-50` to `-300`: text, big numbers, soft fills |
| Pink | `#f5a3c3` | `--palette-pink-700` to `-200`: the identity |
| Lilac | `#c8a8ef` | Guest: secondary accent, links, second series |
| Mint | `#a6e7c8` | Guest: OK status |
| Baby blue | `#a8d4f5` | Guest: info |
| Butter | `#f6e19c` | Guest: pending |
| Peach | `#f9bf9e` | Guest: warning |
| Silver | `#b9b4c2` | Hardware: chain dividers, toggle knobs, rings |
| Cherry | `#ff5247` | Danger only |

Pink and cream are the look. The other pastels are **guests**, never page backgrounds or
large cards. As decoration or accents (chips, chart series, highlights) use two per screen
at most. Status glyphs are exempt: a status list may show every status colour, because each
is a small glyph with words.

## Roles *(Proposed)*

| Colour | Role | Tokens |
|---|---|---|
| **Pink** | Primary buttons, selection, focus, eyebrow labels, the one thing per card that leads. `--color-accent` for fills, `--color-accent-text` for words and icons. | `--color-accent*`, `--color-focus-ring`, `--color-selection` |
| **Cream** | Body text and big numbers | `--color-text*`, `--color-highlight` |
| **Lilac** | Secondary: links, secondary chips, the second chart series | `--color-secondary*` |
| **Plum** | Field, card tint, muted and dim text | `--color-bg`, `--color-surface*`, `--color-text-muted`/`-dim` |
| **Silver** | The hard edge | `--color-hardware` |
| **Cherry** | Errors and destructive actions. Nothing else. | `--color-status-danger`, `--color-danger-*` |

**Text on pastel fills is always dark plum** (`--color-on-accent`). Cream on pink is 1.7:1.

**Pink vs danger.** With a pink accent, a pink-ish red would read as "just another button".
Cherry is a true red (hue 4° against pink's 337°), fully saturated, and the only saturated
colour in the palette. It always comes with its own glyph and words.

## Status *(Proposed)*

One colour **and** one shape per state.

| State | Colour | Glyph | Motion |
|---|---|---|---|
| OK / done | `--color-status-ok` (mint) | Filled heart ♥ | Boop once when it arrives |
| Pending / later | `--color-status-pending` (butter) | Crescent moon ☾ | Slow pulse |
| Idle / off | `--color-status-idle` (mauve) | Hollow heart ♡ | None |
| Warning | `--color-status-warning` (peach) | Rounded triangle with ! | None |
| Error | `--color-status-danger` (cherry) | Broken heart | One wiggle when it's new |
| Info | `--color-info` (baby blue) | Filled dot ● | None |

OK and error are both hearts, so they also differ in shape (whole vs cracked) and the words
always say which it is (decisions/0010).

## Measured contrast

From `python tools/contrast.py`. Card = `--color-surface` composited over the field.
At the brightest point of the haze every value drops by about 8%; the tightest real pairs are
dim text on a hazed card (5.1) and danger text on the danger fill over the haze (5.0).

| Text | On field | On card | On `accent-soft` |
|---|---|---|---|
| Text cream-100 | 17.2 | 15.3 | 11.4 |
| Muted plum-300 | 9.3 | 8.3 | 6.2 |
| Dim plum-400 | 6.2 | 5.5 | **4.1** |
| Pink-500 | 10.1 | 9.0 | 6.7 |
| Pink-600 | 5.1 | 4.6 | **3.4** |
| Lilac | 9.5 | 8.5 | 6.3 |
| Mint / sky / butter / peach | 12.0+ | 10.7+ | 8.0+ |
| Cherry-500 (glyphs, borders) | 6.1 | 5.4 | 4.0 |
| Cherry-400 (danger text) | 6.9 | 6.2 | 4.6 |

Dark plum on pastel fills: 9.5 (lilac) to 15.2 (cream).

- Never put dim text or pink-600 on `accent-soft`. Pink-600 is for fills and borders, never text.
- Danger text uses `--color-danger-text` (cherry-400). Cherry-500 on the danger fill over the haze is 4.4.
- Everything else passes AA (4.5:1) everywhere it's used.

## Light variant *(Proposed values, decisions/0008)*

Set `data-theme="light"` on `<html>`. Same roles, inside out:

| Role | Dark | Light |
|---|---|---|
| Field | plum `#120b12` | blush cream `#fff4ef` |
| Cards | plum glass | white glass at 0.70 |
| Text | cream `#fbefe3` | plum ink `#2a1a2c` |
| Pink fill | `#f5a3c3` | `#f5a3c3` (same), dark ink on it |
| Pink words | `#f5a3c3` | deep pink `#a83d6f` |
| Lilac words | `#c8a8ef` | deep lilac `#7a52b3` |
| Status | pastels | deep "inks" of the same hues |
| Danger | `#ff5247` / text `#ff6a5e` | `#c41a12` |

Pastels can't be words on cream (pink-500 on cream is 1.8:1), so every pastel that is text or a
glyph has a deep `-ink` partner in the light variant. Pastels stay as fills.

Measured, worst case = white card over the brightest haze:

| Text (light) | On card | On `accent-soft` |
|---|---|---|
| Text ink-900 | 15.3 | 13.5 |
| Muted ink-700 | 7.7 | 6.8 |
| Dim ink-500 | 5.0 | **4.5** |
| Pink ink | 5.5 | 4.9 |
| Lilac ink | 5.3 | 4.7 |
| Mint / butter / peach ink | 5.1+ | 4.5+ |
| Sky ink | 4.9 | 4.3 |
| Danger `#c41a12` | 5.6 | 4.9 |

Danger text on its own fill over the haze: 4.7. Sky ink on `accent-soft` (4.3) is fine for the
info glyph (non-text needs 3:1), but don't set info text on pink tint.

Ink on the pink fill: 8.5. Focus ring (pink-600) 3.5 and silver hardware 3.2, both above the
3:1 needed for non-text marks.
