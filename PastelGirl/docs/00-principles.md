# Principles

The overall feel. When a specific rule is missing, decide by these.

## Direction

Softer, rounder and pastel. Feminine, with lots of pinks and creams (decisions/0002), and
**very cute** (decisions/0009). Dark by default, where pastels glow on a plum-black field, with
a light variant on blush cream (decisions/0008).

## Feel *(Proposed)*

| Quality | In practice |
|---|---|
| **Soft** | Generous radii, blurred frosted cards, soft lifts instead of hard lines. Nothing sharp-cornered. |
| **Very cute** | Pink leads, cream warms it. Hearts, moons, stars and sparkles everywhere they fit, little bounces and wiggles, playful words. |
| **Glowy** | In dark, the field is plum, not grey. In light, it's blush cream, not white. Pastels always sit on a tinted field. |
| **A touch of silver** | Optional: a silver chain divider or toggle knob, a crisp mono timestamp. A little sparkle of hardware, not a counterweight. |
| **Calm** | Roomier than a dashboard. One thing per card leads; the rest is quieter. |

## Do *(Proposed)*

- Lead with pink and cream. Most screens need nothing else.
- Add at most two guest pastels (lilac, mint, baby blue, butter, peach) per screen as
  decoration or accents. Small status glyphs don't count towards this.
- Put dark plum text on every pastel fill (`--color-on-accent`). Cream on pink fails contrast.
- Round everything: cards 20px, buttons and chips fully pill-shaped.
- Give every card a little personality: a sparkle by the title, a motif in the empty state,
  a heart that boops when tapped (`.soft-boop`), icons that wiggle on hover (`.soft-wiggle`).
- Celebrate: success gets a happy pop and a cheerful line ("Yay, saved!").

## Don't *(Proposed)*

- No pure white or pure black anywhere. Light uses blush cream, dark uses plum.
- No sharp corners (under 8px) on anything bigger than a checkbox.
- No neon or saturated pinks for the accent. The only saturated colour is cherry red, and it means danger.
- No rainbow screens. If you need more than two guest pastels, the screen is doing too much.
- No hard black drop shadows with offsets. Depth is a soft blur.
- Don't reuse status glyphs as decoration (see `06-iconography.md`).
- Cute never hides a problem: errors are cute in shape, plain in words.

## Lessons from the references

From the pastel e-girl article:

- **Tug of war between cute and cool.** The article's balance. This guide leans firmly cute
  (0009); silver details are an optional extra, not a requirement.
- **Two or three pastels at most.** The article's rule for outfits; here, pink plus one or two guests.
- **If it's only pastel, add a dark piece; if it's only dark, add a pale layer.** That's the
  balance between the plum field and the cream and pink.
- **Motifs:** hearts, stars, moons, bows, daisies, small dots.

## Inspiration

| Reference | Take this |
|---|---|
| [Kawaii Vibe: Pastel e-girl](https://kawaiivibe.com/blogs/kawaii/pastel-egirl-all-you-need-to-know) | Palette (pink, lilac, baby blue, mint, peach, butter, cream on black or plum), silver hardware, soft vs sharp textures, the motifs |
| [Dribbble: Educational App Concept](https://dribbble.com/shots/21672522-Educational-App-Concept) | Not yet reviewed: Dribbble blocks automated reading. Waiting for notes on what to take from it. |

## Open questions

- [ ] What to take from the Dribbble reference (layout, illustration, card style?).
