---
name: ig-viral
description: Research currently successful short-form content in the user's niche, compare performance relative to each creator's normal baseline, identify recurring hook/format patterns, and build an attributed swipe file. Trigger on /ig-viral, viral research, what's working now, reverse-engineer a niche, or swipe-file requests.
---
# ig-viral

Use current web/browsing tools when available. Research a modest sample across direct, adjacent, and larger reference accounts. Never ask for the user's Instagram password and do not scrape Instagram at scale. If login-gated data is unavailable, use public sources or user-provided screenshots/links.

Raw views alone are weak evidence. Prefer an outlier multiple: post views divided by the account's recent median. Treat >3x as a strong signal and <1.5x as near-baseline only as a heuristic, not a law.

Capture account, approximate audience size, recent median, post views, opening hook, first on-screen text, length, CTA, and source link. Attribute every example. If code execution is available, `swipe.py` can rank a TSV export; otherwise compute ratios directly.

Report: sample size, top recurring formulas, structural differences between winners and baseline posts, unclassified patterns, and 3 original content directions for the user. Never copy another creator's script verbatim beyond short quoted hooks needed for analysis.
