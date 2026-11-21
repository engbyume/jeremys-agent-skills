# Animation and Scroll Tooling

Use this guide to choose implementation tools after the visual direction and motion behavior are clear. These are scoped tools, not dependencies to add by default.

## Cross-platform scope

Apply Designmaxxing's visual guidance to user-facing websites, apps, game UI, widgets, dashboards, prototypes, and other visual products when it fits. Adapt it to the platform, renderer, input, audience, and accessibility needs. Do not apply web layout, CSS, DOM scrolling, or browser assumptions to 3D game worlds, 3D art, VR/AR scenes, or engine-rendered environments. Use the matching 3D or game-engine skills there; Designmaxxing still applies to menus, HUDs, overlays, and other interface surfaces.

## Lenis for intentional browser smooth scrolling

- If a DOM-based website or web app deliberately needs custom smooth scrolling, use [Lenis](https://github.com/darkroomengineering/lenis) as the implementation source. Do not hand-roll wheel, touch, or scroll interpolation.
- Keep native browser scrolling when it serves the reading task, keyboard use, touch behavior, reduced motion, or performance better. Lenis wraps native scroll, but its behavior still needs project-level checks.
- Keep Lenis's `respectReducedMotion` enabled. The current README says reduced-motion users receive input-tracking scroll and instant programmatic scrolling by default.
- Check anchor links, focus and keyboard movement, sticky and fixed elements, scroll restoration, modals, and nested scroll areas. Enable `anchors` when Lenis should handle anchor links. Prefer targeted `data-lenis-prevent` or `prevent` handling for inner scroll areas; broad nested-scroll detection can cost work on every scroll event.
- Test touch and Safari on the actual target devices. The README warns that `syncTouch` can behave unexpectedly on older iOS. Destroy the Lenis instance when its owning view unmounts.
- Do not use Lenis for native-app scrolling or game-engine input. Use the platform or engine scroll system.

## GSAP for complex JavaScript animation

- For custom, choreographed, timeline-driven, or scroll-triggered animation on a compatible JavaScript surface, use [GSAP](https://github.com/greensock/GSAP). Do not hand-build a timeline or scroll-sync engine for these cases.
- GSAP is the required first choice for ambitious custom motion on a JavaScript-rendered web or app surface when the project does not already have a suitable animation system. Reuse an established compatible system rather than adding GSAP as a duplicate.
- Use GSAP for multi-step sequences and motion on DOM, CSS, SVG, canvas, WebGL, or JavaScript objects. Use ScrollTrigger for scroll-linked scenes when it fits the interaction.
- In React, use the official `@gsap/react` integration for scoped selectors and cleanup. Use `gsap.matchMedia()` for responsive variants and reduced-motion behavior. Revert or kill timelines when their component or view is removed.
- Use CSS or platform-native transitions for simple press, focus, hover, and state feedback. In native SwiftUI, Jetpack Compose, React Native, or engine-native game scenes, use the matching platform or engine animation skill unless a supported JavaScript surface is the actual renderer.
- Keep motion interruptible, avoid blocking input, and provide a reduced-motion path. GSAP's current repository README states that its full toolset is free for commercial use; recheck the official terms and package support when implementing.

## Vanta for optional animated backgrounds

- When the brief calls for a decorative animated background on a browser surface, use [Vanta](https://github.com/tengbao/vanta) as the first library to evaluate or as a reference for a compatible implementation. Do not add it as a default page effect.
- Vanta renders effects inside an HTML element using Three.js/WebGL or p5.js. Treat it as a browser background library, not as a 3D game-world or native-scene renderer.
- Check current maintenance, supported dependency versions, package size, WebGL support, and mobile GPU and battery cost before adding it. GitHub reported the repository's last push as 2024-03-03 at the 2026-11-20 review, so verify that it is still maintained and compatible. If not, use it as inspiration only and select a maintained option.
- Keep foreground text and controls readable and interactive. Respect `prefers-reduced-motion`, provide a static fallback, avoid capturing pointer or touch input, initialize only when useful, and call the effect's `destroy()` method on teardown.
- The repository is MIT licensed. If copying source code, retain its license and notices and check licenses for bundled dependencies. Do not copy demo artwork, site branding, or unrelated assets.

## Source references

- [Lenis repository and README](https://github.com/darkroomengineering/lenis)
- [GSAP repository](https://github.com/greensock/GSAP) and [official documentation](https://gsap.com/docs/v3/)
- [Vanta repository and README](https://github.com/tengbao/vanta)
