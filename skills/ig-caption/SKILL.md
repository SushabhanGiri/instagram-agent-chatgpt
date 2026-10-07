---
name: ig-caption
description: Draft or lint an Instagram caption for readability, first-125-character feed preview, concrete opening, search terms, hashtag restraint, and one clear CTA. Trigger on /ig-caption or caption-writing/editing requests.
---
# ig-caption

Write captions that earn the tap before optimizing the rest. Keep the first ~125 characters useful on their own. Lead with a concrete line, not “new post,” “happy to share,” or generic hype.

Use the user's voice when known. Preserve factual claims exactly; never invent numbers or results. Prefer natural search terms in sentences over keyword stuffing. Use at most one primary CTA. Keep hashtags restrained and verify any current platform limit with web research if the exact cap matters.

If code execution is available, `caption.py` can preview truncation and basic linting. Otherwise manually report: visible preview, total length, first-line cut risk, concrete markers, CTA count, keyword coverage, and hashtag count.

Return the final caption plus a short lint report. Do not auto-post.
