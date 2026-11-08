# 0007. Status glyphs

Date: 2026-10-24
Status: proposed

## Decision
One shape per state, drawn in `css/woodland.css`:

| State | Glyph |
|---|---|
| OK | Sprout (two leaves on a stem) |
| Pending | Half-filled circle |
| Idle | Hollow pebble |
| Warning | Rounded triangle with ! |
| Error | Filled circle with × |
| Info | Small filled dot |

## Why
Green accent next to green OK, and red danger next to green, is the classic red-green
colour-blindness trap. Every state must be clear in greyscale, so each has its own outline.
The sprout ties OK to the forest theme without borrowing a decorative motif. Error uses a plain
crossed circle rather than a themed shape (a dead leaf, a broken twig) because it must read as
"wrong" at a glance.

## Affects
`--glyph-*` and `.glyph--*` in `css/woodland.css`, `docs/01-color.md`, `docs/06-iconography.md`.
