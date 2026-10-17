# Spacing and layout

Tokens: `--space-*`.

## Spacing scale

4px base. Use only the tokens: `--space-1` (4px), `2` (8), `3` (12), `4` (16), `5` (20),
`6` (24), `8` (32), `10` (40), `12` (48).

## Density

Packed but clean. Defaults:

| Thing | Spacing |
|---|---|
| Inside a panel | `--space-3` |
| Between panels | `--space-2` to `--space-3` |
| Label to value | `--space-1` |
| Table row height | 28px (`--text-sm` text) |
| Input / button height | 28px, 32px for primary |
| Page gutter | `--space-4` |

Density comes from small gaps, not small text. Leave text at `--text-sm` or bigger and tighten the gaps.

## Composition

- **Panels on a grid.** Screens are made of glass panels on a 12-column grid with
  `--space-2` gaps. Each panel has a label, one main readout, then detail.
- **Hierarchy from scale.** One hero readout per screen (`--text-4xl`), a few section
  readouts (`--text-2xl`/`3xl`), everything else small. Avoid a screen of equal-sized boxes.
- **Hairlines over boxes.** Inside a panel, separate groups with `--color-divider` lines or
  whitespace, never nested bordered boxes.
- **Anchor to edges and corners.** HUDs read from the edges inward: status along the top,
  controls along one side, the main view in the centre.
- **Align numerals.** Right-align numbers in columns. Line up units.

| Pattern | Used in |
|---|---|
| Top status strip + panel grid | Jarvis (PC Server) |
| Sidebar + content | Larder |
| Free-floating panels | Desktop-Widgets |
| Full-bleed media + edge HUD chrome | Plox |

## Breakpoints

| Name | Min width | Behaviour |
|---|---|---|
| base | 0 | One column, 16px gutter |
| `md` | 768px | Two-column panel grid |
| `lg` | 1200px | Full 12-column grid |

## Open questions

- [ ] Which apps actually need to work on a phone (Larder, for shopping)?
