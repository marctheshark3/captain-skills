# Captain skills

OpenCode skills for captaining a coding agent. The agent is the crew. You are the captain. The crew does not get to report that it arrived.

Five skills. No bundle. A bundle hides the gate.

| Skill | Voyage |
| --- | --- |
| `navigator` | Trusted advisor. Load this first. It does not write the product. |
| `captain-order` | Four lines, outside the chat, before any code. |
| `miss-check` | One wrong behavior becomes one failing check. No fix in that session. |
| `cut-bloat` | `git diff --stat` first. Over budget goes back unread. Delete only. |
| `miss-hunt` | Fresh session. Three failing tests. A review plan from the build is not an input. |

A subagent spawned from the build session is still that ship. It inherited the frame. It is not a substitute for a new session.

## Install

Clone this repo somewhere that is not the project the agent is changing. Do not commit these skills into a repository you do not own.

```sh
git clone https://github.com/marctheshark3/captain-skills.git
cd captain-skills
./install.sh
```

That symlinks each skill into `~/.config/opencode/skills/`. OpenCode reads that path for every project. Start a new OpenCode session after install. A session that was already running will not see them.

Copy instead of symlink, if the machine cannot symlink:

```sh
./install.sh --copy
```

Personal instruction, in your own OpenCode config, not in a project repo:

```
Before writing or editing code, load navigator. If it says open a new session, stop.
```

## How to start

New session. Plan agent if the harness has one. Paste:

```
Load navigator. Do not write code.
```

It will name one voyage and give you a paste for the next session. Do not `--continue` into that next session.

## Order

`templates/ORDERS.md` is the shape. It lives in the ticket, or in a file you attach with `-f`. If it only exists in the chat, it does not exist.

## License

MIT. Copyright Marc.
