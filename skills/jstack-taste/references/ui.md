# UI reference

Adapted from taste-skill (Leonxlnx, MIT): tasteskill v2, its critique rubric, and the redesign audit.

## Critique rubric

Judge the screenshots, never the code: you wrote the code, so you read your intentions into it. Make each pass on its own.

1. **One second.** Glance and look away. You should be able to name exactly one thing you saw. "A website" means there is no focal point.
2. **Squint.** Text turns into gray bars. The screen should reduce to two or three masses of clearly different size. Many similar masses means nothing leads.
3. **Cover the name.** Could this screen belong to a competitor or another product? If swapping the name gives an equally valid screen, it has no idea of its own.
4. **Edges.** Count the distinct left edges of text blocks. Two or three, reused on purpose, is composed. Six means things were placed one at a time.
5. **Space.** Related things sit close, unrelated things far. Every empty region is a decision, not a hole beside a short column.
6. **Type.** The step from body to heading is decisive (three times or more). No more than five sizes. No orphan word on a heading's last line. No paragraph wider than about 75 characters.
7. **Color.** Name the proportions: the ground, the support, the accent. An accent in ten places means nothing.
8. **Sameness.** Give each section's layout one word (split, list, table, grid, statement). The same word three times is the template showing.
9. **Phone.** The 390px screen is a composition of its own, with its own crops and line breaks, not the desktop squeezed.
10. **Substance.** Every section delivers its full information at a readable size. A screen that looks like an unfinished wireframe is underbuilt, however clean it is.
11. **Collisions.** Nothing overlaps a heading, text, or a button at any scroll position. Nothing runs off the phone edge or scrolls sideways by accident.
12. **States.** Each control shows hover, focus, and pressed feedback. Loading, empty, and error states exist and read as finished.

Score design, usability, creativity, and content from 1 to 10, weighted 40, 30, 20, 10. An honest 8 is good work. If you score your own first pass at 9, score it again as a juror who did not build it. Fix the three problems that cost the most, then look again.

## Laws of the craft

**Type**
- Display type: tracking -0.02 to -0.05em, leading 0.85 to 1.05.
- Text: 16 to 20px, leading 1.45 to 1.6, 45 to 75 characters per line.
- Use `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.
- Center at most one moment per page.

**Space**
- Margins of 16 to 32px, one pair, used everywhere. Large things run to the edges.
- Section gaps of 120 to 220px on desktop for pages; tighter, but still larger than inner gaps, for app screens.
- Use CSS Grid for multi-column structure, `min-height: 100dvh` instead of `100vh`, and relative units over fixed pixel widths.

**Color**
- Off-black (`#0a0a0a`, `#121212`) instead of pure black. Accent saturation under 80%.
- Tint all grays with one hue. Keep one light or dark mode across the page.

**Imagery**
- One dominant image beats six small ones. Keep crop ratios and treatment consistent.
- A real picture of the subject beats a drawn one, and a drawn one beats a placeholder, an icon, or an abstract shape.
- Nothing lies on top of a heading.

**Components**
- Buttons: one fill, square corners or fully round, decided once. A soft 9 to 16px radius is the weak default.
- Navigation: the name, three to five plain links, one action. Mark the current page.
- Inline editing, slide-over panels, or expandable sections before a modal.
- Cards only when elevation shows hierarchy; otherwise use spacing or a background tone.
- One icon set (Phosphor or Heroicons over the Lucide default), one stroke width, no cliché metaphors (rocket for launch).

**Code**
- Semantic elements: `nav`, `main`, `article`, `aside`, `section`.
- A z-index scale in the theme, not `9999`.
- Every import exists in the dependency file. Styling stays in the project's styling system.
- `title`, `description`, and social meta tags on public pages.

## Audit order for an existing UI

Work with the existing stack; improve, never rewrite. Fix in this order, testing after each step:

1. Typography: font choice, scale, weights (add 500 and 600 for hierarchy), measure.
2. Color cleanup: one accent, one gray family, no clashing saturation.
3. Hover, focus, and pressed states.
4. Layout and spacing: grid, max-width, alignment across siblings.
5. Generic components replaced (three-card rows, accordion FAQs, three-tower pricing, sun-moon toggles).
6. Loading, empty, and error states.
7. Final pass on type scale and spacing.

What generated UIs usually forget: a way back from every page, a 404 page, form validation, a skip-to-content link, legal links on public sites.

## Pages

For a landing page, marketing site, portfolio, or other public page:

1. **Inventory the subject.** List eight to twelve things that belong to this client and no competitor: its name and what it means, its place, its numbers, its constraints, its materials, its rituals, the printed things of its world.
2. **Write the argument.** List the page as claims with their proof, one line per section. The claims decide which sections exist and their order. Delete any section without a claim; this replaces the stock hero, logos, three features, testimonial, pricing, call-to-action sequence.
3. **Find the idea.** Fill this sentence from the inventory: "On this page, [something that belongs to the subject] becomes [a layout device]." Put the nearest competitor in the sentence; if it still works, the idea belongs to the category, not the client.
4. **Build with substance.** Type set large, whole fields of color, real pictures of the subject's world (found in open archives and credited on the page, or drawn for it), and every section carrying its full content. A thin page with no tells loses to a rich page with some.
5. **Move.** One signature move done well; staggered entrances (60 to 90ms apart, rising 16 to 32px with opacity) for the parts of each section; feedback on every control. Content never stays hidden if the script fails.
6. **Report** the idea sentence, the scores from your last critique round, and every found picture with its title, creator, license, and source.
