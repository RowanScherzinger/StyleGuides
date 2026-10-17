# Iconography *(Proposed)*

## Set

[Phosphor Icons](https://phosphoricons.com), **Regular** weight for UI and **Fill** for
selected states. Its round joins suit the look, and it has hearts, stars, moons,
sparkles and flowers.

- Size 20px in UI, 16px in chips.
- Icon colour follows the text it sits next to. A pink icon only when the element is pink.

## Motifs

| Motif | Means |
|---|---|
| Heart (filled) | OK / done |
| Heart (hollow) | Idle / off |
| Broken heart | Error |
| Star (filled) | Favourite |
| Moon | Pending / later |
| Sparkle ✦ | New, highlight, decoration by a title (`.sparkle`) |
| Bow / flower | Decoration only: empty states and headers, never as a control |

## Rules

- Decorative motifs get `aria-hidden="true"`.
- Decorative motifs are welcome: one per card is a good rhythm. Keep them small and faint so
  the content still leads.
- Hover on an icon button: `.soft-wiggle`. Tapping a heart or favourite: `.soft-boop`.
- Status glyphs (hearts, broken heart, moon, triangle, dot) are listed in
  `01-color.md` and must not be reused for other meanings or as decoration.
