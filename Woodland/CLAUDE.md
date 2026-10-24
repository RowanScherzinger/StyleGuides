# CLAUDE.md

This folder is a style guide, not an app. There is nothing to build, run or test.
It is independent of the other guides in this repo: don't copy rules across from them.

## When editing this guide

- A decision has three homes, and all three change together:
  1. the value in `tokens/tokens.css`,
  2. the rule (when and how to use it) in the matching `docs/NN-*.md`,
  3. the reason in a new `decisions/NNNN-short-title.md`.
- Do not invent preferences. If you must fill a gap, label it *(Proposed)* in the doc and
  log it with `Status: proposed` in `decisions/`. Never write it up as if the user decided it.
- There are two variants: light (`:root`, the default) and dark (`:root[data-theme="dark"]`).
  Every semantic colour change is made in both.
- After changing any colour, haze or glass token, update `tools/contrast.py` to match, run it,
  and update the contrast tables in `docs/01-color.md`.
- Icons live as SVG data URIs in `css/woodland.css` (`--motif-*`, `--glyph-*`). Draw new ones on
  the same 24px grid, filled, with round ends, and add them to `docs/06-iconography.md` and the preview.
- `examples/preview.html` must keep working in both variants: update it when tokens or classes change.
- Remove an open question from a doc once it is answered.
- Keep docs short and prescriptive.

## When applying this guide inside another project

1. Read `docs/00-principles.md` first, then the docs for what you are building.
2. Use tokens (`var(--...)`) for every colour, font size, space, radius, shadow and
   duration. A literal value in app CSS is a bug unless the guide allows it.
3. Prefer semantic tokens (`--color-accent`) over palette tokens (`--palette-moss-600`).
   Only semantic tokens switch with the variant, so palette tokens in app code break dark mode.
   Moss words and icons use `--color-accent-text`; the plain `--color-accent` is for fills.
4. If the guide is silent, ask the user, then record the answer here.
5. Moss and oat lead, bark is the ink. At most two guest colours per screen as decoration.
6. Green means two things here: the moss accent and the fern OK status. OK always uses the
   sprout glyph and words. Never show a green status without its glyph.
7. Rowan red is only for danger. Never use it as decoration or a chart series.
8. Motifs (leaf, fern, pine, mushroom, acorn, pinecone, sun) are decoration. Status glyphs
   (sprout, half-filled circle, pebble, triangle, crossed circle, dot) are never decoration.

Decision 0002 is the user's own. Everything else is proposed until the user confirms it, so
follow it, but raise anything that seems wrong.
