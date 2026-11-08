# Data viz *(Proposed)*

Windows itself draws few charts (Task Manager, storage in Settings). Follow their restraint.

- **One series**: the accent.
- **Two or more**: the accent first, then neutral greys from `--color-text-muted` down to
  `--color-border-strong`. If the series must be told apart by colour, label them directly.
- **Status colours are never series.** Red means an error, not "the third line".
- **Parts of a whole** (storage bar): one horizontal bar, 8px high, 4px corners, segments
  separated by a 2px gap in the background colour, each labelled with its size.
- **Lines**: 2px, no markers, no smoothing; gridlines in `--color-divider`.
- **Track** (empty part of a bar or ring): `--color-border-strong` at 1px for progress,
  `--color-control` for meters.
- **Numbers**: tabular figures, units in secondary text.
