# Iconography *(Proposed, decisions/0007, 0008)*

The guide draws its own forest motifs and status glyphs, in `css/woodland.css`. They are SVG
masks on a 24px grid: one empty span, sized with `font-size`, coloured with `color`.

```html
<span class="motif motif--leaf" aria-hidden="true"></span>
<span class="glyph glyph--ok" aria-hidden="true"></span> Backup finished
```

## Motifs (decoration)

| Class | Shape | Good for |
|---|---|---|
| `.motif--leaf` | A single leaf on a stem | By a title, chips, the twig divider |
| `.motif--fern` | A fern frond | Large and faint in a hero card corner |
| `.motif--pine` | A three-tier pine | App or page title |
| `.motif--mushroom` | A spotted mushroom | Empty states |
| `.motif--acorn` | An acorn | Saved, stored, harvested things |
| `.motif--pinecone` | A pinecone | Collections, archives |
| `.motif--sun` | A sun | Morning, daylight, the light-mode toggle |

Motifs are moss by default, or walnut for warm things. Use one per card, small or faint
(about 0.2 opacity when large) so the content leads.

## Status glyphs (meaning only)

| Class | Shape | Means |
|---|---|---|
| `.glyph--ok` | Sprout | OK / done |
| `.glyph--pending` | Half-filled circle | Pending |
| `.glyph--idle` | Hollow pebble | Idle / off |
| `.glyph--warning` | Rounded triangle with ! | Warning |
| `.glyph--danger` | Circle with × | Error |
| `.glyph--info` | Small dot | Info |

Each glyph sets its own status colour. Never use a status glyph as decoration, and never use
a motif to show status. Every glyph sits next to words.

## UI icons for actions

Not chosen yet (decisions/0008). Until it is, use a rounded set with 2px strokes and round
joins at 20px (16px in chips), coloured like the text beside it. Check any set against the
motifs above so actions and decoration don't share a shape.

## Rules

- Decorative motifs and glyphs get `aria-hidden="true"`; the words carry the meaning.
- Hover on an icon button: `.wood-rustle`.
- New motifs: same 24px grid, filled shapes or 2px round strokes, no fine detail under 1px.
