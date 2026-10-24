# 0006. Colour roles

Date: 2026-10-24
Status: proposed

## Decision
- Moss is the accent, oat is the field (and text in dark), bark is the ink, pine is the night
  field. Walnut is secondary.
- Guests, one per status: fern (OK), lake (pending), lichen (warning), heather (info).
  Two per screen at most as decoration; status glyphs are exempt.
- Danger is rowan red, a crimson, and nothing else is red.
- Every colour used as text or a glyph in light has a deep `-ink` partner.

## Why
- The brief asks for green and forest colours (0002), so moss leads; oat and bark are the
  paper and soil around it.
- **Green twice.** A green accent and a green OK status are hard to avoid in a forest palette.
  They are kept apart three ways: hue (fern sits 36 to 40° from moss, measured), a unique
  sprout glyph, and words. A fresher green was chosen for OK rather than a non-green, because
  green-means-done is too strong a convention to break.
- **Warning was first fox orange.** `tools/contrast.py` measured it 6° of hue from walnut,
  so a walnut chip could read as a warning. Warning moved to lichen yellow (18° from walnut in
  light, 14° in dark, plus the triangle glyph), and pending moved to lake blue.
- Rowan is crimson so it sits at least 33° from walnut and 47° from lichen.
- Walnut and lichen are still the closest pair. That's why the warning glyph is a triangle
  and walnut is never used as a status.

## Affects
`--color-*` and the guest palette in `tokens/tokens.css`, `docs/01-color.md`,
`docs/10-data-viz.md`, `tools/contrast.py`.
