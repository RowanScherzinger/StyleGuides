# 0011. Money in and out: plain amounts, coloured signs

Date: 2026-10-28
Status: accepted

## Decision
- Amounts of money are plain text. Only the sign is coloured: a chartreuse `+`
  (`--color-status-ok`) for money in, and a red `-` (`--color-danger-text`) for money out.
- In charts, income and spending are ordinary categorical series (gold, then copper).
  Neither is green or red.
- A category breakdown is drawn as a thin multi-segment ring (gaps between segments, no
  stroke), not a filled pie or donut.

## Why
User decision for ProjectMoney, when asked how income should look now that green is
reserved for status lights. Colouring only the sign keeps a quick in/out cue, which is
a small mark (allowed for chartreuse by 0007), without turning a list of amounts into a
wall of green and red. Rejected: gold amounts for income, and chartreuse amount text.

The thin ring was Claude's recommendation, accepted by the user, as the closest fit to
"no pie charts, use a ring" in `docs/10-data-viz.md`.

## Affects
`docs/01-color.md`, `docs/10-data-viz.md`, `CLAUDE.md`.
