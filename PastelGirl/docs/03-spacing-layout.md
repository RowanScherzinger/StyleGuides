# Spacing and layout *(Proposed)*

## Scale

4px base: `--space-1` (4px) to `--space-16` (64px). Never use a value off the scale.

## Density

Comfortable, not packed.

- Card padding `--space-5` (20px), or `--space-6` for hero cards.
- Gap between cards `--space-4` (16px).
- Rows at least 44px tall so pills and toggles have room.

## Composition

- Cards on the haze background. Don't nest cards. Inside a card, group with `.well` or spacing.
- One leading element per card: a big number, a title or an illustration. Everything else is quieter.
- Prefer a two-column grid of cards on desktop, and one column on a phone.
- Round shapes want air. If a pill touches the card edge, add space instead of shrinking the radius.

## Breakpoints

| Name | Min width | Layout |
|---|---|---|
| phone | 0 | One column, 16px gutters |
| tablet | 640px | Two columns |
| desktop | 1024px | Two to three columns, max content width 1200px |
