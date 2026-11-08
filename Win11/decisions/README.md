# Decisions

One short file per style decision, so the reason survives after the value changes.

Name: `NNNN-short-title.md`, numbered in order. Never renumber; if a decision is
reversed, write a new one that supersedes it.

Status:
- `accepted`: the user decided it.
- `proposed`: written in by Claude to fill a gap. It's in use, but not yet confirmed by the
  user. Confirm it, or supersede it.
- `superseded by NNNN`.

## Template

```markdown
# NNNN. Title

Date: YYYY-MM-DD
Status: accepted | proposed | superseded by NNNN

## Decision
What was decided, in one or two sentences.

## Why
The reason, including what was rejected.

## Affects
Tokens and docs that changed.
```
