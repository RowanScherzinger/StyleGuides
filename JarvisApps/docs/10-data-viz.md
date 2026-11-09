# Data visualisation

Dashboards (Jarvis, Desktop-Widgets) are mostly live metrics. In the HUD style, charts are
instruments: thin lines, ticks, arcs and minimal chrome.

## Chart colours *(Proposed)*

| Use | Order / tokens |
|---|---|
| Categorical series | 1 `--color-series-1` (gold-400), 2 `--color-series-2` (copper), 3 silver, 4 off-white, 5 pale copper (`--palette-copper-300`). More than five series means the chart should be split. |
| Sequential (low to high) | `--palette-neutral-700` → copper → gold → `--palette-gold-300` |
| Thresholds | Normal: series colour. Warning: ember. Critical: crimson. Draw threshold lines as dashed hairlines. A single-series line may turn ember or crimson where it crosses a threshold. On a multi-series chart the lines keep their series colours, and the dashed lines and status tags show the threshold. |
| Gridlines | `--color-chart-grid` (off-white at 4%) |

Red is never a data series. It means critical only.

Series 1 is gold-400, not the gold-500 highlight. Next to copper, gold-500 measured
ΔE 13.2 under normal vision, below the 15 needed to tell two lines apart. Gold-400 measures
19.9 (19.1 for deuteranopia), and both pass 3:1 against the surface. The palette checker
still flags gold as outside its lightness band. That is a known exception: gold is the
signal colour (decisions/0013).

## Patterns

| Pattern | Use for | Rule |
|---|---|---|
| **Readout** | A single current value | `.hud-value` + unit + label. Optional delta (`▲ 4.2`) in muted text. |
| **Ring gauge** | A percentage of a limit | A 270° arc, 2px track at `--color-divider`, value arc in the series colour, tick marks every 10%. The value sits in the centre. |
| **Segmented bar** | Capacity, queue depth | 10–20 discrete segments with 2px gaps, not a smooth fill |
| **Sparkline** | A recent trend | 1.5px line, no axes, the latest point marked with a dot, optional 10% area fill |
| **Line chart** | Time series | 1.5px lines, horizontal gridlines only at 4% opacity, tick labels in `--text-2xs` mono |
| **Bar chart** | Comparison | Thin bars (≤ 8px), with values labelled at the end of the bar rather than an axis |
| **Channel trace** | Live telemetry: a few readings watched together (CPU, GPU, memory, temperature) | A sweep trace, one channel per group of related readings. See below. |

## Channel trace

An oscilloscope-style sweep for live readings (decisions/0013). Jarvis's System panel is
the reference.

- **Channels.** One row per group of readings that share a unit and scale: Load (CPU %,
  GPU %), Memory (RAM and VRAM as % of their totals), Thermal (°C), Network (download and
  upload, Mb/s). Never put two
  different units on one channel. At most two series per channel, in series order.
- **Row layout.** A readings column on the left holds the channel title (display face,
  copper), then one readout per series: a 14×2px swatch in the series colour, the label,
  the value and unit. The trace fills the rest of the row.
- **Window.** 30 samples. At 60 samples a minute that is the last 30 seconds; at 12 a minute
  (one every 5 s) the last 2.5 minutes.
- **Frequency.** The sample rate can be offered as a choice, written as samples per minute
  over 60 Hz: `6/60Hz`, `12/60Hz`, `20/60Hz`, `30/60Hz`, `60/60Hz` (one every 10 s down to one
  a second). Keep 30 slots at every rate, so the window changes with it (5 minutes down to
  30 seconds), and say the window beside the channel set (`last 30 s`). Clear the trace when the
  rate changes, because slots taken at the old spacing would squash or stretch it. Put the
  control, labelled `Frequency`, beside the monitoring switch *(Proposed)*.
- **Sweep.** Each sample has a fixed slot (`sample index % 30`). A write head moves one
  slot left to right per sample and wraps. The trace never scrolls.
- **Write head.** A 1px vertical hairline in `--color-highlight` at about 28% opacity, plus
  a 6px diamond on each line in its series colour with a small glow. The diamond sits on the
  newest real reading. The segment leading to it grows from the previous reading over one
  sample interval, so the line tracks smoothly and meets the dot as the next reading lands
  *(Proposed)*.
- **Gap.** Leave 3 slots blank ahead of the head, so the newest and oldest readings never
  join up.
- **Fade with age.** Line opacity runs from 100% at the head to 25% for the oldest slot.
- **Scale.** Y ticks only: minimum, middle and maximum (`0% 50% 100%`, `20° 60° 100°`) in
  `--text-2xs` mono, `--color-text-dim`. No time labels, because slots don't stay at a fixed
  time. A ruler of short ticks along the top marks time instead: a minor tick every 3 slots
  (3 s at 60 a minute) and a taller one every 15 slots (15 s at 60 a minute).
- **Labels.** Each line is labelled at the head on a small plate in the surface colour, so
  the label stays readable over old trace. The plate sits in the gap ahead of the head and
  flips to the left near the right edge. Labels push apart when two lines meet.
- **Thresholds.** Dashed hairlines at the warning (ember) and critical (crimson) levels,
  at about 45% opacity. Lines keep their series colours.
- **Open-ended channels.** A reading with no natural maximum, such as network throughput,
  scales to the first 1-2-5 step (1, 2, 5, 10, 20, 50 …) with 10% headroom over the
  window's peak, with ticks at zero, half and the step (`0 25M 50M`). It has no thresholds
  or status tags, because a fast transfer isn't a fault. Read values out in the largest unit
  that keeps them at 1 or more (`438 kb/s`, `12.4 Mb/s`) *(Proposed)*.
- **Status tags.** A reading over a threshold gets a tag beside its label, in shape and
  word: ▲ `HIGH` in `--color-status-warning`, ■ `CRITICAL` in `--color-danger-text` with a
  crimson square. Never a diamond, because ◆ means running.
- **Hover.** A vertical crosshair in `--color-contrast-accent` at the nearest slot, a ring on
  each line, and a glass tooltip giving the age (`−2:15`, `Now`) and each value.
- **Monitoring off.** Clear the traces, keep the scale and threshold lines, dim the channels
  to 40%, and show `--` for every value.

## Rules

- Draw charts on with `draw-line` the first time they render. Later updates go straight to the new value.
- Tooltips are small glass panels with a crosshair at the point, in `--color-contrast-accent`. Values are tabular mono.
- No 3D, no pie charts. Use a ring or a segmented bar instead. A share-of-total
  breakdown is a thin multi-segment ring: about 6px thick, 2° gaps, no stroke (decisions/0011).
- Income and spending are ordinary series (gold, copper), never green and red (decisions/0011).
- Axis and tick text uses `--color-text-dim` on app surfaces only.
