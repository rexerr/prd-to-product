# Animation taste reference — extract from Emil Kowalski's `web-animation-design` skill

**Provenance:** Emil Kowalski's animations.dev course skill, distributed via `curl -fsSL "https://animations.dev/api/activate?email=<purchaser-email>" | bash` (purchaser-gated). Installed 2026-06-11, reviewed, extracted here, then **deliberately uninstalled** from all harnesses (`~/.claude/skills/`, `~/.codex/skills/`, `~/.cursor/skills/`) because its ~40-keyword proactive trigger description loaded into every session on every project and overlapped `vercel-react-view-transitions` / `frontend-design`. Re-run the curl above to reinstall the full skill (SKILL.md + PRACTICAL-TIPS.md) anytime.

Companion article: <https://emilkowal.ski/ui/agents-with-taste> — his core claim ("almost every 'taste' decision has a logical reason if you look close enough") is the positive-polarity twin of this repo's "every rule cites its failure mode."

This extract serves two purposes: **(1)** skill-authoring patterns worth stealing for our own skills, **(2)** candidate source material for a `design-system-bootstrap` motion-defaults layer, if that ever gets built.

---

## Part 1 — Skill-craft patterns (for authoring our skills)

1. **Anti-example output contracts.** His "Review Format (Required)" section shows the required output shape *and* an explicit "Wrong format (never do this)" block with the failure rendered literally. Our skills state desired output shape but never show the anti-pattern. Showing the failure is a stronger constraint than describing the success.
2. **Trigger saturation is an anti-pattern — observed, not theorized.** The skill's description packed ~40 trigger keywords plus "use this skill proactively." Result: it would fire in essentially any frontend session, on every project, in every harness — which is exactly why it was uninstalled within hours. Evidence for keeping our SKILL.md trigger phrases narrow and verb-specific.
3. **Progressive disclosure across two files.** Compact SKILL.md (decision rules, tables, flowchart) + `PRACTICAL-TIPS.md` (detailed implementations) linked from a one-line-per-scenario table. Same shape our skills already use; confirmation it's the convention serious skill authors converge on.
4. **Canned initial response.** "When invoked without a specific question, respond only with: <one line>. Do not provide any other information until the user asks." Prevents the invocation-triggers-info-dump failure. Cheap to add to knowledge-shaped skills.
5. **Cross-harness installer as a distribution reference.** One shell script, content base64-embedded, detects each agent harness by directory probe and writes the same markdown into each one's skills dir (with a marker-grep dedup for append-style targets like Windsurf). Relevant to the D-006 residual: the write-guard hook is operator-machine-only today; this script is a working example of the fan-out install pattern a shipped version would need.

## Part 2 — Animation content (candidate DSB motion-defaults material)

### Easing decision tree

1. Element entering/exiting the viewport? → `ease-out`
2. On-screen element moving/morphing? → `ease-in-out`
3. Hover/color transition? → `ease`
4. Constant motion (marquee, ticker, progress)? → `linear`
5. Default → `ease-out`. Avoid `ease-in` for UI (slow start delays feedback; same duration feels slower).

### Custom easing tokens (built-in CSS curves are usually too weak)

```css
/* ease-out, weak to strong */
--ease-out-quad: cubic-bezier(0.25, 0.46, 0.45, 0.94);
--ease-out-cubic: cubic-bezier(0.215, 0.61, 0.355, 1);
--ease-out-quart: cubic-bezier(0.165, 0.84, 0.44, 1);
--ease-out-quint: cubic-bezier(0.23, 1, 0.32, 1);
--ease-out-expo: cubic-bezier(0.19, 1, 0.22, 1);
--ease-out-circ: cubic-bezier(0.075, 0.82, 0.165, 1);

/* ease-in-out, weak to strong */
--ease-in-out-quad: cubic-bezier(0.455, 0.03, 0.515, 0.955);
--ease-in-out-cubic: cubic-bezier(0.645, 0.045, 0.355, 1);
--ease-in-out-quart: cubic-bezier(0.77, 0, 0.175, 1);
--ease-in-out-quint: cubic-bezier(0.86, 0, 0.07, 1);
--ease-in-out-expo: cubic-bezier(1, 0, 0, 1);
--ease-in-out-circ: cubic-bezier(0.785, 0.135, 0.15, 0.86);
```

### Duration

| Element type | Duration |
| --- | --- |
| Micro-interactions | 100–150ms |
| Standard UI (tooltips, dropdowns) | 150–250ms |
| Modals, drawers | 200–300ms |

- UI animations stay under 300ms.
- Larger elements animate slower than smaller ones; match duration to distance traveled.
- Exit ~20% faster than entrance.

### Frequency rule — when not to animate

- **100+ uses/day → no animation** (Raycast never animates; it opens hundreds of times daily).
- Never animate keyboard-initiated actions: arrow-key list navigation, shortcut responses, tab/focus moves.
- Marketing surfaces may go longer/fancier; product surfaces stay fast and purposeful.

### Paired-elements rule

Elements that move as a unit use the same easing and duration (modal + overlay, tooltip + arrow, drawer + backdrop).

### Springs

- Use for drag/momentum, interruptible gestures, "alive" elements (Dynamic Island). Springs keep velocity when interrupted; CSS restarts from zero.
- Prefer Apple-style config `{ type: "spring", duration: 0.5, bounce: 0.2 }` over mass/stiffness/damping.
- Avoid bounce in most UI; when used (drag-to-dismiss, playful contexts) keep it 0.1–0.3.

### Performance

- **Golden rule: only animate `transform` and `opacity`** (GPU path, skips layout + paint). Avoid animating padding/margin/height/width, blur filters >20px (Safari especially), CSS variables in deep trees.
- `will-change: transform` fixes 1px shake at transform start/end (GPU/CPU handoff).
- Framer Motion gotcha: `animate={{ transform: "translateX(100px)" }}` is hardware-accelerated; `animate={{ x: 100 }}` is not.
- React: animate outside the render cycle (refs over state); re-render per frame = dropped frames.
- CSS runs off main thread (better under load, for predetermined motion); JS (rAF) for dynamic/interruptible motion.

### Accessibility

- Every animated element ships a `prefers-reduced-motion: reduce` override setting `animation: none` / `transition: none` — no exceptions for opacity or color, no `!important`.
- Gate hover effects behind `@media (hover: hover) and (pointer: fine)` (touch fires hover on tap). Tailwind v4's `hover:` does this automatically.
- 44px minimum hit area (Apple/WCAG); use an absolutely-positioned pseudo-element to enlarge the target without changing layout.

### Scenario → fix table

| Scenario | Fix |
| --- | --- |
| Buttons feel unresponsive | `transform: scale(0.97)` on `:active` |
| Element appears from nowhere | Enter from `scale(0.95)` + `opacity: 0`, never `scale(0)` ("a deflated balloon still has shape") |
| Shaky/jittery animation | `will-change: transform` |
| Hover flicker (element moves out from under cursor) | Animate a child element; parent keeps the stable hover area |
| Popover scales from wrong point | `transform-origin: var(--transform-origin)` (Base UI) / `var(--radix-*-transform-origin)` (Radix) — scale from the trigger, not center |
| Sequential tooltips feel slow | First tooltip gets delay + animation; subsequent ones instant (`data-instant` → `transition-duration: 0ms`; Radix/Base UI support this) |
| Transition still feels off after easing/timing tweaks | Subtle blur (≤20px, e.g. `filter: blur(2px)` on `:active`) to mask the gap between states |
| Can't tell why it feels wrong | Record it and scrub frame by frame |
