# Data viz *(Proposed)*

macOS itself draws few charts (Activity Monitor, storage in System Settings). Follow their
restraint, and HIG > Charts.

- **One series**: the accent.
- **Several categories that must be told apart** (a storage bar): system colours in a fixed
  order (blue, purple, pink, orange, green, gray), each labelled directly. Light mode uses the
  default shades as fills, never as text.
- **Status colours are never series.** Red means an error, not "the third line".
- **Parts of a whole** (storage bar): one horizontal bar, 8px high, rounded ends, segments
  separated by a 2px gap in the background colour, each labelled with its size.
- **Lines**: 2px, round joins, no markers; gridlines in `--color-grid`.
- **Track** (empty part of a bar or ring): `--color-toggle-off`.
- **Numbers**: tabular figures, units in secondary text.
- **VoiceOver**: Swift Charts describe themselves; give web charts a text summary.
