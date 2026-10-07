---
name: ig-profile
description: Audit an Instagram profile and rewrite its name field, bio, CTA, highlights, and pinned-post strategy. Trigger on /ig-profile, profile audit, bio rewrite, Instagram bio, or “score my profile”.
---
# ig-profile

Score the profile out of 100 using `rubric.json`: identity clarity, audience specificity, value proposition, proof, searchability, CTA, link clarity, visual coherence, pinned posts, highlights, trust, and friction. If the user provides a screenshot, inspect it directly. If information is missing, score only what is visible and mark unknowns rather than guessing.

Return: score, highest-impact fixes first, rewritten name field, 2-3 bio options, CTA, highlight set, and recommended pinned-post roles.
