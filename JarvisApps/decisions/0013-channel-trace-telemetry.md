# 0013. Live telemetry is a grouped channel trace

Date: 2026-11-09
Status: accepted (the pattern); proposed (series 1 colour step, status tag shapes)

## Decision
- **Accepted.** Live system telemetry (CPU, GPU, memory, temperature) is drawn as a
  channel trace: an oscilloscope-style sweep with one channel per group of related
  readings. Readings that share a unit share a channel and a scale (Load, Memory,
  Thermal). The full rule is in `docs/10-data-viz.md`: Channel trace.
- **Proposed.** Categorical series 1 is gold-400 (`--color-series-1`), not the gold-500
  highlight.
- **Proposed.** A reading over a threshold gets a status tag in shape and word: ▲ `HIGH`
  (ember) and ■ `CRITICAL` (crimson).

## Why
User decision for Jarvis's System panel. The user compared four live mockups: sparkline
tiles, a set of conventional line charts ("twin scopes"), one sweep trace per reading,
and the combination. They asked for the combination: grouped readings, drawn in the
channel-trace layout. Not chosen: the sparkline tiles, the conventional charts, and one
channel per reading. The user gave no reason beyond preferring the combination. The sweep
was offered as the most instrument-like option, in keeping with the HUD direction
(decisions/0003), and grouping cuts five channels down to three.

The colour step is Claude's, found while building the mockups. Gold-500 and copper drawn
as two lines measured ΔE 13.2 under normal vision, below the 15 needed to tell two lines
apart. Gold-400 and copper measure 19.9 (19.1 under deuteranopia), and both pass 3:1
contrast against the surface. The palette checker still flags gold-400 as outside its
lightness band. That band suits generic palettes, and gold is this guide's signal colour,
so it's an accepted exception.

The tag shapes follow the status table (decisions/0009): ▲ is already warning and ■ is
already error. An early mockup used a diamond for warning. That was wrong, because ◆ means
running.

## Affects
`tokens/tokens.css` (`--color-series-1`, `--color-series-2`, `--color-chart-grid`),
`docs/10-data-viz.md`, `docs/05-motion.md`, `docs/01-color.md` (contrast table),
`tools/contrast.py`, `examples/preview.html`, `CLAUDE.md`.
