# Principles

The overall feel every app shares. When a specific rule is missing, decide by these.

## Direction

An Iron Man style HUD: futuristic and kinetic, built from lines, shapes and icons so
information can be read at a glance. Dark only. Warm metallic colours: red, gold,
copper, silver, black, off-white.

## Feel

| Quality | In practice |
|---|---|
| **Futuristic** | Hairline frames, corner brackets, tick marks, arcs and rings. Uppercase tracked labels. Glass panels over a dark field. |
| **Kinetic** | The interface feels alive: it boots in, values settle, brackets lock on hover, a slow ring turns. Motion has a job (see `05-motion.md`). |
| **Packed but clean** | High density without clutter. Order comes from alignment, a strict spacing scale and hairlines, not from padding. |
| **Glanceable** | The most important number is the biggest and brightest thing in its panel. State is read from shape and colour before text. |
| **Engineered** | Every element looks like it measures something. Nothing is purely decorative. |

## Do

- Lead each panel with one readout: big mono numerals in gold, then a small unit and label.
- Draw structure with 1px copper hairlines and corner brackets instead of filled boxes.
- Use shape to carry meaning: rings for percentages, segmented bars for capacity, ticks for scale.
- Keep "nominal" quiet. Colour and motion get louder only as something needs attention.
- Align everything to the 4px grid. In a dense layout, misalignment is what looks messy.

## Don't

- No light theme, no white surfaces, no pastel colours.
- No large rounded corners (more than 6px), no soft drop shadows. Depth comes from glow and glass.
- No cool sci-fi look. Chartreuse and blue appear only as status lights and small
  high-contrast marks, never as surfaces, borders or the main accent. The heat is the identity.
- No decoration that pretends to be data unless it's clearly ambient (a faint grid, a slow ring).
- Don't let several things blink at once. Only one thing at a time should be shouting.

## Design lessons from the references

From Jayse Hansen and Territory Studio's work on the Avengers films:

- **Reason every element out.** "Just looks cool but isn't well thought out won't feel
  right." Every line, ring and tick should map to something real.
- **Tune density and motion together.** Their late revisions were density and colour
  shifts (towards red) and limits on how many elements animate or blink at once.
- **Show the machine's work, but carefully.** Film UI shows the computer working. Real
  apps can borrow that (boot sequences, scanning sweeps) only where it doesn't slow the task.
- **Give each app its own character inside the family.** Each film character got their own
  palette and personality on a shared language.

## Reference implementation

The Desktop-Widgets app already uses this look (glass, copper hairlines, brackets,
scan sweep, flicker boot). The tokens and `css/hud.css` here are taken from it.

## Inspiration

| Reference | Take this |
|---|---|
| [Territory Studio: Age of Ultron](https://territorystudio.com/project/marvels-avengers-age-of-ultron/) | Darker, grittier Stark screens; engineering and work-in-progress content; per-character palettes |
| [Pinterest: FUI Iron Man](https://www.pinterest.com/michael_scala/fui-iron-man/) | Rings, arcs, brackets, readout layouts |
| [Jayse Hansen interview](https://thenextweb.com/news/jayse-hansen-on-creating-tools-the-avengers-use-to-fight-evil-touch-interfaces-and-project-glass) | Research first then push past reality; limit simultaneous animation; a "bible" for each component |

## Open questions

- [ ] Same accent palette in every app, or a per-app accent within the warm range (for
      example Plox leaning copper, Jarvis leaning red)?
