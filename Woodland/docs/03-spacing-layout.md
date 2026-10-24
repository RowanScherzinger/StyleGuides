# Spacing and layout *(Proposed)*

## Scale

4px base: `--space-1` (4px) to `--space-16` (64px). Never use a value off the scale.

## Density

Roomy, like a page in a field guide.

- Card padding `--space-5` (20px), or `--space-6` for the pebble hero card.
- Gap between cards `--space-4` (16px).
- Rows at least 44px tall.

## Composition

- Cards on the field. Don't nest cards. Inside a card, group with `.well` or spacing.
- One leading element per card: a big number, a title or a motif. Everything else is quieter.
- At most one pebble card (`.card--pebble`) per screen, for the thing that matters most.
- Motifs sit at the edges (by a title, in a corner), never in the middle of content.

## Breakpoints

| Name | Min width | Layout |
|---|---|---|
| phone | 0 | One column, 16px gutters |
| tablet | 640px | Two columns |
| desktop | 1024px | Two to three columns, max content width 1200px |
