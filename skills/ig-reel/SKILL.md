---
name: ig-reel
description: Write an Instagram Reel from a raw idea using three distinct hook formulas, score the hooks, write a spoken script and on-screen text, and check timing. Trigger on /ig-reel, Reel requests, short-form video scripts, hooks, voiceovers, or “what should I say in this video?”.
---
# ig-reel — ChatGPT port

Turn one true, specific idea into one Reel. Do not invent metrics, clients, outcomes, prices, or quotes.

## Inputs
Use the user's voice profile if supplied. If none exists, infer voice from examples already in the conversation; otherwise write in simple conversational language and label the voice as provisional. Do **not** block the task just because a voice profile is missing.

Read `hooks.json`. Pick **three genuinely different formulas**, not three rewrites of one formula. Write a spoken hook and a separate on-screen hook (six words or fewer).

## Score hooks
If a Python/code tool is available, run the logic in `hookscore.py`. Otherwise score each hook 0-100 on: length, specificity, stakes, front-loading, and audience address. Penalize greetings, “stop scrolling,” video preambles, hashtags, or emoji in the spoken hook. Show the ranking and use the best hook. A score below 50 means rewrite before scripting.

## Script shape
- 0:00-0:02 hook
- 0:02-0:07 stake
- body: one idea per beat, frame/visual changes each beat
- last 3s: payoff + one CTA
- last line: echo a word/concept from the hook when natural

Aim for 15-45 seconds unless the user specifies otherwise. Write for speech: contractions, short lines, no corporate prose.

If code execution is available, use `beats.py` to estimate timing and fix: hook >3s, any beat >4s, abstract runs, or no loop. Otherwise estimate at ~165 WPM.

## Output
Return: (1) ranked hooks, (2) winning spoken script, (3) timed on-screen text cards, (4) shooting notes, and (5) a compact readiness summary. Never claim to have posted it.

Attribution: adapted for ChatGPT from Jake Schincariol's MIT-licensed `ig-reel` skill.
