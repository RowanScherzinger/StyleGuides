# Data viz *(Proposed)*

Soft, earthy and readable.

## Series order

Use `--color-accent` and `--color-secondary` for the first two so they follow the variant.

1. Moss `--color-accent`
2. Walnut `--color-secondary`
3. Lake
4. Heather
5. Lichen

More than five series means the chart should be split. Rowan is never a series. A chart next
to a status list uses moss and walnut only, so series never look like statuses. Fern is not a
series: it is too close to moss.

## Shapes

- **Ring progress**: 8–10px stroke, round caps, `--color-track` behind. The value sits in the
  middle in Fraunces.
- **Bars**: softly rounded tops (`--radius-sm`), 8px gap. Moss for the current item,
  `--color-series-muted` for the rest.
- **Area / line**: 2px line, round joins, a fill that fades from 25% to 0.
- **Progress bar**: pill track, walnut fill.

## Rules

- Gridlines: `--color-divider`, horizontal only.
- Axis labels: `--text-xs`, muted.
- Highlight one point at a time with the moss ring (`--glow-accent`).
