# 0006. Plain status glyphs

Date: 2026-11-08
Status: proposed

## Decision
In dense places, status is a small plain shape next to words: filled dot (OK), half-filled
ring (pending), ring (idle), triangle (warning), ring with a cross (error), small dot (info).
In messages, the InfoBar uses the full Fluent status icons.

## Why
Each state needs its own shape so colour isn't the only signal, and the shapes must be plain to
fit the look. Fluent's circled icons are too detailed at 9–11px, so these simpler shapes keep
the same family (circles, plus the warning triangle). Phone Explorer draws this set.

## Affects
`.status--*` in `css/fluent.css`; `docs/01-color.md`, `docs/06-iconography.md`.
