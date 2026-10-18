---
name: jstack-explain
description: "Explain how or why code or a system works: walkthroughs, architecture, design rationale, history. Use for 'how does X work', 'why is Y like this', or before changing unfamiliar code."
---

# Explain

Build a true mental model in the person's head, at their pace. The goal is that they understand it, not that you change anything.

## 1. Frame

Name the **target** (a function, a subsystem, a decision) and the **question** (how it works, why it is this way, or both). Read from the conversation why they ask: about to change it, reviewing it, debugging it, or new to it. That decides where the depth goes. If the target is vague, state your reading in one line and continue; the person can redirect.

Size the work. **Simple** is one module or a narrow question: read it yourself. **Complex** spans files, services, or history: fan out in step 2.

## 2. Gather

**How it works.** Read the entry points and trace the flow end to end. For a complex target, split the question into two to four angles (a distinct slice each) and send each to a read-only subagent on the fast model, all at once. Each returns facts with `file:line`, not prose. Reconcile overlaps and check contradictions in the code yourself.

**Why it is this way.** Build the code anchor first, then follow the evidence:

- `git blame -L <start>,<end> <file>` for the last-touch commits.
- `git log --follow --oneline -- <file>` for history through renames, and `git log -1 --format=%B <sha>` for PR numbers and ticket IDs.
- `gh pr view <n> --json title,body,comments,reviews` for the PR discussion.
- Tickets, error reports, and chat threads that the anchor names, through the tools you have for them (an MCP server or a CLI).

Search every source the anchor points to. A source you searched and found empty is a finding; record it.

Done when you can state, with a citation for each: what it is, how data flows through it, where it lives, and, for a why question, what forces shaped it.

## 3. Explain

- **Plain definition first.** Name the thing and say what it is in general terms, with its common name if it has one. Then tie it to this case: "here, we use it to...".
- **Smallest complete answer first.** One or two sentences that answer the question, then stop. Add layers when the person asks. When no person is live, give the full account, with the short answer first.
- **Mechanism over metaphor.** "When an item scrolls past the buffer, its DOM node and its data are evicted." Concrete names: "`UserService` calls `AuthClient.refresh()`".
- **Build diagrams up.** For three or more moving parts, draw a short series where each diagram redraws the last and adds one part. Use mermaid for flows and structure, a small ASCII sketch for simple relations. A single simple point needs no figure.
- **One name per concept**, kept throughout.

For a full walkthrough, use these sections and drop any that do not apply: **Overview** (what it is and why it exists, in a paragraph), **Key concepts**, **How it works** (the flow, the longest part), **Where things live** (the files someone needs first), **Gotchas**.

## 4. Label confidence

Every why-claim sits in one tier, phrased to match:

- **Direct**: an author wrote the reason (PR body, ticket, commit message, design doc). "This exists because X [source]."
- **Supported**: several indirect sources agree. "The evidence points to X: [sources]."
- **Inferred**: your reading of the context. "Given A and B, X seems likely."
- **Unknown**: you searched and found nothing. Say what you searched: "No PR, ticket, or commit in the six changes since 2023 gives a reason."

Words like "because", "was designed to", and "fixes" need a citation in the same sentence.

## When it does not land

If the person says it did not make sense, re-pitch it: less jargon, one concrete example, the project's own terms, and the smallest complete answer again.
