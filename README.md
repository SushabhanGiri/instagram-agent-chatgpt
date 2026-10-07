# Instagram Agent for ChatGPT

A **ChatGPT-native port** of Jake Schincariol's excellent open-source
[`instagram-agent-skill`](https://github.com/Jakeschincariol/instagram-agent-skill).

> **Credit:** Original concept, upstream skills, Reel hook library, and upstream helper logic by
> **Jake Schincariol** ([opusjake.ai](https://opusjake.ai)), licensed under MIT.
> This repository is a ChatGPT adaptation/package maintained by **Sushabhan Giri**.
> It is not an official release by Jake and does not imply his endorsement.

## What this package changes for ChatGPT

The upstream project targets Claude/Claude Code. This port keeps the same 13 workflow names,
but packages them as an **Agent Plugins 1.0 skills-only plugin** for ChatGPT/Codex and removes
hard dependencies on Claude-specific filesystem paths or commands.

- ChatGPT-native `plugin.json` + `.codex-plugin/plugin.json`
- 13 skills under `skills/`
- prompt aliases such as `/ig-reel`, `/ig-caption`, `/ig-plan`
- helper scripts are dependency-free Python and optional: when code execution is unavailable,
  the skill instructions define a reasoning fallback
- web research instructions use the browsing tools available in the current ChatGPT session
- no Instagram password collection, no scraping at scale, and no automatic posting

## Important note about `/ig-*`

In ChatGPT, these are **prompt aliases**, not guaranteed native slash-menu commands. Starting a
message with `/ig-reel` (or another alias) strongly signals the matching skill. ChatGPT may also
invoke the skill automatically from normal language, e.g. “turn this idea into a Reel.”

## Workflows

| Alias | Purpose |
|---|---|
| `/ig-reel` | Idea → three hook options → scored winner → script → on-screen text → beat timing |
| `/ig-viral` | Research what is working in a niche and build an attributed swipe file |
| `/ig-caption` | Write/lint captions with feed-preview checks |
| `/ig-carousel` | Build swipe-post structure and slide copy |
| `/ig-story` | Plan a daily Story sequence and sticker/DM flow |
| `/ig-profile` | Score and rewrite an Instagram profile |
| `/ig-plan` | Build a one-week content plan |
| `/ig-human` | Remove robotic phrasing and invisible formatting artifacts |
| `/ig-comment` | Write useful comments for other posts |
| `/ig-reply` | Triage and draft replies under your own post |
| `/ig-dm` | Draft keyword delivery, first DM, collab pitch, and follow-ups |
| `/ig-repurpose` | Turn one long-form asset into a week of standalone posts |
| `/ig-audit` | Post-mortem published content using reach/outlier metrics |

## Install

Package the repository root as a ZIP and install it as a private ChatGPT plugin, or use the
prebuilt release ZIP if provided. The root folder contains exactly one Agent Plugins package.

## Voice profile

Start from `templates/voice.md`. The skills will work without it, but a filled voice profile makes
scripts much more likely to sound natural when spoken.

## Safety / platform boundaries

This package **writes and analyzes content; it does not automatically post**. Do not provide
Instagram passwords. Do not use the workflows to scrape Instagram at scale or evade platform
limits. For publishing or account actions, use Meta-supported APIs or approved integrations.

## License and attribution

MIT. See `LICENSE` and `NOTICE.md`. Please retain attribution to Jake Schincariol when redistributing
substantial portions of the upstream work.
