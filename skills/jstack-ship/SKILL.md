---
name: jstack-ship
description: "Ship work after refine passes: branch, commits, PR body, CI, deploy, and the ticket update. Use for commit, push, open a PR, watch CI, deploy, or 'ship it'."
---

# Ship

Take a change from "refine passed" to "merged, deployed, and the ticket updated". Each step that changes something outside this machine (a push, a PR, a deploy, a ticket edit) is outward-facing: do it only when the person asked for that step or for the whole ship.

Load `jstack-craft` first. A repo's own convention (its `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, recent `git log`) overrides every format here.

## 1. Branch

- Name: `<user>/<ticket-id>-<slug>`, lowercase. `<user>` is the prefix the person's existing branches use (`git branch -a`), else `git config user.name` with spaces removed. Leave out `<ticket-id>` when there is no ticket; never invent one.
- Never commit to the default branch. Branch first.
- Up to date: `git fetch`, then rebase on the default branch when it moved. Ask before a rebase that rewrites commits already pushed.
- One change: `git log <base>..HEAD` and `git diff <base>...HEAD --stat` hold only this work. Move unrelated work to its own branch.

## 2. Commits

- Message: `<TICKET-ID>: what changed and why`, or `what changed and why` with no ticket. Short and direct.
- Make a new commit. Amend, squash, or reorder only when the person asks. Ask before any history rewrite.
- Force-push only with `--force-with-lease`, and only after a rewrite the person approved.
- Schema changes go in migrations; one-off data fixes go in one-time scripts.
- Never set work aside with a bare `git stash`; use a WIP commit.
- Hooks and linters that fail block the commit. Fix the code; never skip a hook.

## 3. Pull request

- Write the body from the diff and the ticket. Fetch the ticket and its comments with your tracker tool (an MCP server or a CLI).
- Body: what changed and why, how you verified it (commands and results), and what is not verified. Link the ticket.
- Scan the title and body with the `jstack-taste` prose rules before you open it.
- Push the branch, then open it with the forge CLI: `gh pr create` on GitHub, `glab mr create` on GitLab.

## 4. CI

- When the harness watches CI for you, let it. Otherwise watch it once: `gh pr checks <n> --watch`, or `glab ci status --wait`.
- On a failure, read the failed job's log (`gh run view <id> --log-failed`, or `glab ci trace <job>`) and hand off to `jstack-diagnose`. Never re-run a failed job to make it pass.
- When a check flags a smell, fix the code. Keep every rule as it is.

## 5. Deploy

- Deploy only when the repo has a deploy path: a deploy config (for example Kamal's `config/deploy*.yml`) or a documented command.
- A request to ship (`/jstack-ship`, "ship it") is the yes to deploy to production. Deploy without asking again.
- Use that path. For Kamal: `bin/kamal deploy` (add `-d <destination>` for a destination file).
- Prove it is live: check the app's health URL for a 200 (for Kamal, the proxy host plus its `healthcheck.path`, `/up` by default), then load a page or call an endpoint that shows the change itself, and confirm the new behavior on production. Report the status code and what you saw.
- When the deploy, the health check, or the live check fails, stop and report the output. Do not roll back unless the person asks.

## 6. Close the loop

- Move the ticket and link the PR with your tracker tool. Use the state the work is in: the team's review state when the PR is open, its done or released state when it is merged.
- Never send a message for the person. When the loop needs one (a chat note, an email), write it and give it to the person to send.

## Report

Give the branch, each commit SHA and message, the PR link, the CI result, the deploy result, health status, and live check, the ticket state, and any message the person must send.
