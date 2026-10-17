# Data visualisation

Dashboards (Jarvis, Desktop-Widgets) are mostly live metrics. In the HUD style, charts are
instruments: thin lines, ticks, arcs and minimal chrome.

## Chart colours *(Proposed)*

| Use | Order / tokens |
|---|---|
| Categorical series | 1 gold, 2 copper, 3 silver, 4 off-white, 5 pale copper (`--palette-copper-300`). More than five series means the chart should be split. |
| Sequential (low to high) | `--palette-neutral-700` → copper → gold → `--palette-gold-300` |
| Thresholds | Normal: series colour. Warning: ember. Critical: crimson. Draw threshold lines as dashed hairlines. |

Red is never a data series. It means critical only.

## Patterns

| Pattern | Use for | Rule |
|---|---|---|
| **Readout** | A single current value | `.hud-value` + unit + label. Optional delta (`▲ 4.2`) in muted text. |
| **Ring gauge** | A percentage of a limit | A 270° arc, 2px track at `--color-divider`, value arc in the series colour, tick marks every 10%. The value sits in the centre. |
| **Segmented bar** | Capacity, queue depth | 10–20 discrete segments with 2px gaps, not a smooth fill |
| **Sparkline** | A recent trend | 1.5px line, no axes, the latest point marked with a dot, optional 10% area fill |
| **Line chart** | Time series | 1.5px lines, horizontal gridlines only at 4% opacity, tick labels in `--text-2xs` mono |
| **Bar chart** | Comparison | Thin bars (≤ 8px), with values labelled at the end of the bar rather than an axis |

## Rules

- Draw charts on with `draw-line` the first time they render. Later updates go straight to the new value.
- Tooltips are small glass panels with a crosshair at the point. Values are tabular mono.
- No 3D, no pie charts. Use a ring or a segmented bar instead.
- Axis and tick text uses `--color-text-dim` on app surfaces only.
