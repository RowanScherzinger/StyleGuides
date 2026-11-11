# 0014. The channel trace's write head glides to a prediction, then corrects

Date: 2026-11-11
Status: accepted (predict, then correct); proposed (the prediction formula and timing)

## Decision
- **Accepted.** The write head never jumps. Between readings the diamond glides toward a
  predicted next reading in the next slot, over one sample interval. When the real reading
  lands, the diamond moves quickly from where it is to the real reading, and the next
  glide starts. The full rule is in `docs/10-data-viz.md`: Channel trace, Write head.
- **Proposed.** The prediction is the newest value plus 0.6 × the least-squares slope of the
  last 3 consecutive readings. The correction takes `--duration-normal` (220 ms) on
  `--ease-out-expo`, and it runs at the same time as the next glide, so the head never
  stops. After a wrap, or when more than 3 readings arrive at once, the head starts from
  the real reading instead of carrying over.

## Why
User decision. The user disliked the head's jumpy movement: the diamond jumped to each new
reading, and only the line grew in behind it (0013). They asked for the head to "smoothly
lerp to the next predicted step, using the last two or 3 steps as a guide, and then move
quickly to the actual reading when it arrives over a short duration."

The numbers are Claude's. A full-strength trend overshoots on noisy readings such as CPU
load, which jitters by several percent between samples, so the prediction takes 0.6 of the
slope. Fitting 3 points instead of 2 halves the effect of one noisy reading. Running the
correction during the next glide, rather than before it, keeps the head moving at an even
pace. Positions are in slot and value units, so a resize or an auto-scale change during a
glide doesn't throw the head off.

The animation stops once the head reaches its prediction, so it still only moves when data
arrives and stays out of the ambient-loop budget (`docs/05-motion.md`).

## Affects
`docs/10-data-viz.md`, `docs/05-motion.md`, `examples/preview.html`, `CLAUDE.md`. No
token changes: it uses `--duration-normal` and `--ease-out-expo`.
