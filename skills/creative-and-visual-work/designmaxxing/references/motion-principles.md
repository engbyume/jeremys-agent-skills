# Motion and Animation Principles

## Contents

- [Use references, then recreate](#use-references-then-recreate)
- [Eighteen motion cues](#eighteen-motion-cues)
- [Accessibility and evaluation](#accessibility-and-evaluation)
- [Research sources](#research-sources)

## Use references, then recreate

Use motion references to identify the trigger, start and end states, path, timing, easing, overlap, interruption behavior, and platform conventions. Recreate the useful interaction in the product's own components, design system, and visual language. Do not copy third-party animation code, assets, or distinctive branding.

For AI-assisted design or code, specify the trigger, state change, duration or spring, easing, path, stagger, interruption behavior, reduced-motion alternative, and input method. Treat the values below as starting examples, not a universal animation system. Current platform guidance can use springs or native transitions instead of fixed durations.

The cues are optional. Add motion only when it clarifies cause and effect, feedback, hierarchy, spatial continuity, or state change. Combine or omit cues when they compete or add delay.

## Eighteen motion cues

1. **Ease-out entrances:** decelerate into the resting state so an entering control settles quickly.
2. **Dropdowns, 150-250 ms:** use this as a starting range for lightweight menus. Keep the control responsive and follow a native platform pattern where one exists.
3. **List-row stagger, about 30 ms:** use short staggering for a small set of newly appearing rows. Avoid delaying access to long lists.
4. **Press scale, about 0.97:** use a slight scale-down for press feedback when it remains readable and does not change layout or hit testing.
5. **Stretch moving knobs, about 12%:** a small stretch can communicate a knob or handle in motion. Let related details settle with a short stagger after release.
6. **Arcs for object movement:** use a curved path when it clarifies spatial relationships. Prefer direct movement when that is easier to track.
7. **Success pulse:** use one subtle pulse to confirm a completed action, paired with a clear status message or state.
8. **Ease in and out for moves:** use acceleration and deceleration to make state changes feel controlled. Tune the curve to the action and platform.
9. **Popovers at 0.95 scale:** a small scale-in can support the connection to a trigger. Avoid large zooms or repeated bounce.
10. **Enter from the trigger, exit to the trigger:** preserve spatial continuity when a popover, menu, or contextual surface opens and closes.
11. **No bounce on everyday UI:** avoid spring overshoot on frequent, routine controls. Reserve bounce for interactions whose meaning benefits from it.
12. **Do not tween while held:** track a pointer or finger directly during a drag. Animate the settle after release, not the held position.
13. **Exits about 20% shorter:** try a shorter exit than entrance when it improves responsiveness. Treat the ratio as a starting point.
14. **Overlap old and new states:** crossfade or transition related states together to avoid a blank pause. Keep only the correct state interactive and focused.
15. **Masks for reveals and color:** use masks or color transitions when they clarify a reveal or state change. Preserve contrast and do not hide essential content during motion.
16. **Crossfade icons with subtle blur:** use a brief crossfade and restrained blur for a meaningful icon change. Remove the blur if it harms clarity or performance.
17. **Rubber-band past bounds:** reserve elastic overshoot for direct-manipulation bounds or platform conventions. Do not add it to everyday UI without a reason.
18. **Reuse the same layout ID:** in systems with shared-layout transitions, keep a stable ID for the same element across source and destination states. Do not reuse an ID for unrelated elements.

## Accessibility and evaluation

- Respect the platform's reduced-motion setting and the web's prefers-reduced-motion preference. Replace non-essential movement with an instant state change or a simple fade when that preserves meaning.
- Do not rely on motion, blur, or color alone to communicate success, error, selection, or progress. Keep status text and accessible state available.
- Make important motion interruptible and do not block input or navigation while decorative transitions run.
- Check contrast and focus during masks, fades, and blur. Avoid large-area or repeated movement that can distract or cause discomfort.
- Review the interaction at normal speed, with reduced motion enabled, and on each relevant input method. Do not claim user testing unless it occurred.
- WCAG 2.2 SC 2.3.3 Animation from Interactions is Level AAA and applies to non-essential interaction-triggered animation when that conformance level is targeted. SC 2.2.2 covers certain automatically moving content. Verify the chosen conformance target and current guidance.

## Research sources

- [Apple Human Interface Guidelines: Motion](https://developer.apple.com/design/human-interface-guidelines/motion/) and [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility/).
- [Material 3 Motion](https://m3.material.io/styles/motion), which currently describes physics-based motion and spring tokens instead of a universal duration-and-easing system.
- W3C [WCAG 2.2: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions), [Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide), and [Media Queries Level 5: prefers-reduced-motion](https://www.w3.org/TR/mediaqueries-5/).
