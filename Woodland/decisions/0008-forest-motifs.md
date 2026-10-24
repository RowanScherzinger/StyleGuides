# 0008. Forest motifs, shipped as CSS masks

Date: 2026-10-24
Status: proposed

## Decision
The guide ships its own seven decorative motifs (leaf, fern, pine, mushroom, acorn, pinecone,
sun) as SVG data URIs on a 24px grid, used through `.motif.motif--*`. They take `currentColor`,
so they follow the variant. A UI icon set for ordinary actions is a separate, open choice.

## Why
The brief asks for forest items and icons (0002). Drawing them in the guide means every app
gets the same shapes without depending on a library having a mushroom or a pinecone. Masks
rather than inline `<svg>` keep the markup to one empty span and let CSS colour them.

The UI icon set is not chosen: a library would need to be checked for its forest glyphs first.
Until then, apps use any rounded, 2px-stroke set for actions and this guide's motifs for decoration.

## Affects
`--motif-*`, `.motif*` in `css/woodland.css`, `docs/06-iconography.md`, `examples/preview.html`.
