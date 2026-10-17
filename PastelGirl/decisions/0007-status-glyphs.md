# 0007. Status glyphs

Date: 2026-10-17
Status: superseded by 0010

## Decision
OK is a mint filled heart, pending a butter crescent moon, idle a mauve hollow circle,
warning a peach triangle, error a cherry circled cross, info a baby-blue dot.

## Why
Every state needs a shape as well as a colour. The heart and moon use the look's motifs
for the gentle states (the moon reads as "later"); the star is kept for "favourite". Warning and error keep plain, serious shapes so a real problem
never looks cute.

## Affects
`--color-status-*`, `docs/01-color.md`, `docs/06-iconography.md`.
