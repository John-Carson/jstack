---
name: jstack-taste
description: "Taste for anything a person sees: UI screens, pages, components, terminal output, and prose such as docs, READMEs, PR text, and reports. Load before you build UI or write for people."
---

# Taste

A generated screen or paragraph drifts to the average of everything the model has seen. Nothing in it is wrong and nothing in it was decided. Replace each default with a decision that comes from the subject: its users, its data, its words.

## UI

1. **Read what is real.** Find the users, the one job of the screen, the stack, and the existing design system (tokens, components, fonts, icons). An existing system wins; extend it. If the request is vague, decide, and state your reading in one line.
2. **Build with substance.** Apply the house rules below. Removing an ornament leaves space; fill it with scale, the full content, real data, or a field of flat color, never with another ornament.
3. **Build every state.** Hover, focus, and pressed feedback; loading as a skeleton in the layout's shape; an empty state that says what to do next; inline errors in plain words; disabled; long text; zero, one, and many items.
4. **Build it accessible.** Semantic HTML or the platform's native controls, a visible focus ring, a label on every input and icon button, alt text that describes, text contrast of 4.5:1 or more, 44px touch targets, a working keyboard path, and a reduced-motion fallback (`prefers-reduced-motion` on the web).
5. **Look at it.** Take screenshots at 1440, 768, and 390 pixels wide with the browser tool you have, or on the target devices for a native app. Critique them with the rubric in [references/ui.md](references/ui.md), fix the top three problems, and look again, for up to three rounds. What a screenshot shows is real, whatever the code says.

Done when the screenshots at every size show no house-rule break, no overflow or clipped text, and every state from step 3.

### House rules

- **Type.** One family, two at most. Five sizes at most, with one very large and one small doing most of the work. Sentence case. Left-aligned by default. Body text 16 to 20px at 45 to 75 characters per line. Tabular figures where numbers align.
- **Color.** One ground, one ink, one accent, and the accent marks the main action. Running text in full ink. One gray family. Surfaces separated by a step in tone. Flat color only; the one gradient allowed is a scrim under text on a photo. Choose a palette from the subject, away from the violet-indigo and cream-terracotta defaults.
- **Layout.** One grid and one pair of margins, used everywhere. The gap between sections is larger than any gap inside one. Shared elements line up across siblings (titles, prices, buttons). A max-width container on wide screens. Each section gets its own composition; a row of identical icon cards is the tell to replace.
- **Components.** Flat buttons with one radius, decided once. Shadows only on what floats: menus and dialogs. Solid bars instead of glass blur. Plain labels in the heading or first sentence instead of pill badges and small caps eyebrows. One icon set with one stroke width; emoji stay out of the interface.
- **Content.** Real copy and plausible data: specific names, uneven numbers, real dates. Direct messages: "Connection failed. Try again." Calm success messages, without exclamation marks.
- **App screens.** Dense layouts are right for data. Tables and form fields keep their lines. Monospace is for code and IDs.
- **Motion.** Transform and opacity only, 150 to 300ms, for feedback and entry. Every move has a reduced-motion fallback that keeps the content.

For a landing page, marketing site, or other public page, also follow the Pages section of [references/ui.md](references/ui.md).

## Terminal output

Align columns. Use color only for meaning: green for success, red for failure, dim for secondary detail. Use honest status words (`ok`, `fail`, `skip`). Keep output readable at 80 columns and in light and dark themes, with no emoji or decorative boxes.

## Prose

Write clean as you draft; a cleanup pass misses what drafting put in.

- Lead with the point. Use short declarative sentences, one idea each, in active voice.
- Use concrete nouns, real numbers, and the mechanism instead of a feeling ("a column rename fails the build", not "types you can trust").
- Each claim carries its source, or a label that says it is an inference or a guess.

Before you publish docs, a README, PR text, a commit message, or a report, scan it against [references/prose.md](references/prose.md) and fix every hit.
