# Examples

Three example runs of the prd-creator skill. Read these to understand what a real interview produces, what the output PRD looks like, and how scope shapes the conversation.

## Three project shapes

- **Small.** `small/` shows a focused single-purpose tool. Full transcript plus full output PRD. The brand-and-voice cluster is skipped. Decisions list is short. Use this as the canonical example of what minimum viable PRD looks like.
- **Medium.** `medium/` shows a SaaS tool with substantive voice work. Abbreviated transcript. Brand content lands inline (three items). Decisions list is medium length.
- **Large.** `large/` shows a multi-surface personal product with substantive brand voice. Abbreviated transcript plus a separate `BRAND.md` output. Decisions list is longer. Demonstrates the sibling-file path.

## What "abbreviated transcript" means

Medium and large transcripts skip the verbatim back-and-forth on routine clusters and show only:

- The cluster prompt.
- The user's answer (sometimes paraphrased for length).
- The summary the skill produced before moving to the next cluster.

The small transcript shows the full conversation including push-back moments, because those are the load-bearing examples of how the interview should actually run.

## What these examples are not

- Not real projects. Synthetic examples written to illustrate the shape.
- Not exhaustive of the cluster space. Edge cases (cluster 0 with substantial source material, cluster 5 with zero decisions) are documented in `NOTES.md` regression tests, not in examples.
- Not style references. They follow the output style for PRDs (sentence-case, no em dashes), but a real run may produce richer prose if the user's source material is rich.
