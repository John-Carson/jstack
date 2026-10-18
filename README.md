# jstack

Seven skills that make a coding agent work like a careful senior engineer. Each one is short, opinionated, and works with any language or framework. They follow the [Agent Skills](https://agentskills.io) format, so Claude Code, Codex, OpenCode, Pi, claude.ai, and other agents that read `SKILL.md` files can load them.

| Skill | Load it when | What it makes the agent do |
| --- | --- | --- |
| `jstack-craft` | Any coding task | Reuse before writing, take the smallest change that solves the real problem, fix root causes, write the failing test first, and prove the result on the real artifact. Includes Vanilla Rails defaults for Rails projects. |
| `jstack-taste` | UI or prose that a person sees | Replace generated defaults with decisions, build every state, check accessibility, critique real screenshots, and remove the tells of machine-written prose. |
| `jstack-explain` | "How does X work?" or "Why is Y like this?" | Trace the code end to end, dig through blame, PRs, and tickets for the reason, and label each claim Direct, Supported, Inferred, or Unknown. |
| `jstack-design` | A new feature or a change across modules | Ask about each open decision with a recommendation, settle the domain terms, and sketch two different interfaces before any code exists. |
| `jstack-diagnose` | A bug, a flaky test, or slow code | Build a command that fails on the exact bug before any theory, minimize it, rank hypotheses, and fix at the root with a regression test. |
| `jstack-refine` | Before you call work done | Review the diff for correctness, spec gaps, standards, bloat, and blast radius. Prove the one fact the change is safe because of, then fix. |
| `jstack-ship` | Commit, PR, deploy | Branch, commit, open the PR, watch CI, deploy to production, prove the change is live, and update the ticket. |

## Install

### Claude Code

```
/plugin marketplace add John-Carson/jstack
/plugin install jstack@jstack
```

### Any agent, with the skills CLI

```bash
npx skills add John-Carson/jstack
```

### Manual

Clone the repo and link the skills into the folder your agent reads:

```bash
git clone https://github.com/John-Carson/jstack ~/jstack
mkdir -p ~/.claude/skills ~/.agents/skills
for skill in ~/jstack/skills/*/; do ln -s "$skill" ~/.claude/skills/; ln -s "$skill" ~/.agents/skills/; done
```

Claude Code reads `~/.claude/skills`. Codex, OpenCode, and Pi read `~/.agents/skills`. Run `git -C ~/jstack pull` to update.

### claude.ai

Download the zips from the [latest release](https://github.com/John-Carson/jstack/releases/latest). Upload each one in Settings > Capabilities > Skills.

## Make them load every time

Agents choose skills from each skill's description. `jstack-craft` works best when it loads on every coding task, so add these lines to your global instructions (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or your agent's equivalent):

```markdown
Load the `jstack-craft` skill for every coding task. Load the `jstack-taste` skill before you build UI or write prose for people.
Load a mode skill when the task is one: `jstack-explain` how or why something works, `jstack-design` before you build, `jstack-diagnose` broken or slow behavior, `jstack-refine` before you call work done, `jstack-ship` to commit, open the PR, deploy, and update the ticket.
```

## How they fit together

`jstack-craft` is the base. The four modes (`explain`, `design`, `diagnose`, `refine`) each load it before they edit code. A typical change runs `design`, then `craft`, then `refine`, then `ship`. `taste` joins whenever the work has a screen or text that a person reads.

Your repo's own rules win. Each skill reads `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, the linter config, and recent `git log`, and follows them where they differ from the skill.

## Things to know before you use `jstack-ship`

- **It deploys to production.** A request to ship (`/jstack-ship` or "ship it") counts as approval to deploy. The skill does not ask again. It deploys only when the repo has a deploy config (for example Kamal's `config/deploy.yml`) or a documented deploy command. After the deploy, it checks the health URL and then checks the change itself on production. If any step fails, it stops and reports. It does not roll back unless you ask.
- **It uses your tools.** It opens PRs with `gh` or `glab`. It reads and moves tickets with whatever tracker tool your agent has, such as an MCP server or a CLI. It never sends a message for you. It writes the message and gives it to you to send.
- **Branch and commit format.** Branches are `<user>/<ticket-id>-<slug>` and commits are `<TICKET-ID>: what changed and why`. The ticket part is left out when there is no ticket. A repo's own convention overrides both.

## Credits

jstack rewrites and merges ideas from Matt Pocock's skills, Lauren Tan's pstack, DietrichGebert's ponytail, and Leonxlnx's taste-skill, all MIT. See [CREDITS.md](CREDITS.md) for each source and pin.

## License

[MIT](LICENSE)
