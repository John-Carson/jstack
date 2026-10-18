---
name: jstack-design
description: "Design before you build: grill open decisions, name the domain, sketch two interfaces. Use for new features, changes across module boundaries, architecture choices, or 'grill me'."
---

# Design

Settle the decisions and the shape before code exists, while changing them is still cheap. The code that follows implements the agreed sketch.

## 1. Ground

Trace every system the change touches, the way the `jstack-explain` skill does: entry points, data flow, owners, and the reasons behind the current shape. A reason you find becomes a constraint, not a guess. Read `CONTEXT.md` or `CONTEXT-MAP.md` and `docs/adr/` when they exist, and use their terms.

Done when you can draw how the affected flow works today, with `file:line` anchors.

## 2. Grill

Map the work as a **design tree**: each decision branches into the decisions that hang off it. The **frontier** is every decision whose prerequisites are already settled.

- Ask the whole frontier in one round with your harness's question tool, one question per decision, at least two concrete options, your recommended option first and marked `(Recommended)`.
- **Facts are yours, decisions are theirs.** Look up anything the code, the tools, or the docs can answer, with a subagent when it takes digging. Ask the person only for preferences, priorities, and product calls.
- A question that depends on another open question waits for a later round. After each round, recompute the frontier.
- When an earlier answer conflicts with new evidence, say so and reopen that one decision.

Done when the frontier is empty, nothing is silently assumed, and the person confirms the shared understanding.

## 3. Name

Hold the domain language to one word per concept.

- When the person uses a term that conflicts with `CONTEXT.md`, or a vague word ("account" for both Customer and User), call it out and propose the precise term.
- Test relationships with concrete edge-case scenarios ("an order is half shipped and then cancelled: what happens?").
- When the code disagrees with what the person says, show the contradiction.
- Record each resolved term in `CONTEXT.md` the moment it settles, using [references/context-format.md](references/context-format.md). The file is a glossary only, free of implementation detail.
- Offer an ADR only when a decision is hard to reverse, surprising without context, and the result of a real trade-off, using [references/adr-format.md](references/adr-format.md).

## 4. Sketch twice

Write the caller's code first, then derive the types and signatures from it, with stub bodies and pseudocode. Produce at least two **structurally different** candidates: whole-shape alternatives, not variations inside one shape. For a novel interaction or architecture with no precedent in the codebase, make three.

Screen each candidate against the red flags in [references/interfaces.md](references/interfaces.md): shallow module, information leakage, temporal decomposition, pass-through method. Then compare on **depth** (behavior hidden behind a small interface), **locality** (change concentrates in one place), and **seam** placement (where tests and adapters attach). Pick the deeper interface, or graft the strongest part of the loser into it, and state why in two or three sentences.

Done when one sketch is chosen, its usage example compiles in your head, and its reasons are written down.

## 5. Build against the sketch

Load `jstack-craft`, then fill in the stubs. The sketch is the contract. A deviation (a parameter the sketch did not foresee, a caller that must know internal rules) is a signal: decide whether the sketch, the requirement, or the implementation is wrong, and say which.

**Scrap** the sketch when the same workaround keeps appearing, unrelated edge cases each need a special branch, or types need escape hatches to compile. Re-ground on what you built, redesign as if the new constraints had been there from day one, make the new sketch smaller than the old one, and return to step 4.
