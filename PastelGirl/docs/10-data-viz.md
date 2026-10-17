# Data viz *(Proposed)*

Round, soft and readable.

## Series order

1. Pink `--palette-pink-500`
2. Lilac `--palette-lilac-500`
3. Mint `--palette-mint-500`
4. Baby blue `--palette-sky-500`
5. Butter `--palette-butter-500`

More than five series means the chart should be split. Cherry is never a series. A chart
that sits next to a status list uses pink and lilac only, so series never look like statuses.

## Shapes

- **Ring progress**: thick stroke (8–10px), round line caps, a plum track. The value sits in the
  middle in Fredoka.
- **Bars**: fully rounded ends, 8px gap. Pink for the current item, plum-600 for the rest.
- **Area / line**: 2px line, round joins, a fill that fades from 30% to 0.
- **Progress bar**: pill track, pink fill, a sparkle at the end when it reaches 100%.

## Rules

- Gridlines: `--color-divider`, horizontal only.
- Axis labels: `--text-xs`, muted.
- Highlight one point at a time: a cream dot with a pink glow.
