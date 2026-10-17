# 0004. Typefaces

Date: 2026-10-17
Status: accepted

## Decision
Nunito for UI text, Fredoka for titles and numbers, Cascadia Mono for timestamps and code.

## Why
"Rounder" applies to type too: both Nunito and Fredoka have round terminals and stay readable
at small sizes. Cascadia Mono is the user's terminal font and gives the one crisp "cool" face.
Rejected: Quicksand (too thin on dark at body sizes), Comfortaa (hard to read in long text).
Proposed by Claude, confirmed by the user on 2026-10-17.

## Affects
`--font-*` in `tokens/tokens.css`, `docs/02-typography.md`.
