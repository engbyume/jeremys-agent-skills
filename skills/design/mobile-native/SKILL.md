---
name: mobile-native
description: Make mobile websites, web apps, and PWAs feel responsive and installed. Use when building or reviewing phone-first web UI or fixing phone-only layout, touch, scroll, safe-area, keyboard, or browser-chrome behavior. Web only; not React Native.
---

# Mobile Web, Made Native

## Activation

**Activation:** Mandatory when the prompt matches.
**Trigger:** Use for phone-first websites, web apps, PWAs, or mobile-specific web interactions. It does not apply to React Native.

Use this skill with `designmaxxing` whenever a website, web app, or PWA targets phones or touch interaction. It covers the web platform layer: viewport sizing, form behavior, touch input, scrolling, safe areas, keyboard layout, browser chrome, and device verification. It does not design motion or build React Native apps.

Apply only the fixes that match the product, symptom, browser support, and accessibility needs. Preserve the project's stack and existing design system. Prefer a small CSS or metadata change when it solves the cause.

## Core rules

- Use capability queries such as `(hover: hover)`, `(pointer: fine)`, viewport units, and safe-area environment values. Do not guess input type from user-agent strings or screen width.
- Touch and mouse can exist on the same device. Support both without hiding needed controls.
- Never disable page zoom with `user-scalable=no` or `maximum-scale=1`. Fix the cause, usually small form text.
- Keep normal content selectable. Limit selection blocking and callout suppression to controls.
- Do not disable pull-to-refresh, scrolling, or browser gestures across the whole page unless the product interaction needs that behavior.
- Prefer browser-native scroll and input behavior over custom JavaScript gestures. Keep pointer and touch handlers short and passive where possible.
- A desktop device toolbar is not a phone. Use real hardware to verify touch, browser chrome, safe areas, and keyboard behavior before claiming those parts passed.
- Keep development servers on a trusted private network for phone checks. Do not create a public tunnel or deployment unless the user authorizes it. Stop temporary servers after the check.
- For computer-use inspection, follow Designmaxxing's Agent Desktop-first route. A screenshot or accessibility tree can help inspect a device, but neither proves real-device behavior by itself.

## Symptom guide

| Symptom | Likely fix |
| --- | --- |
| Hover style stays after a tap | Gate hover rules with `(hover: hover) and (pointer: fine)`; add a press state |
| Gray or blue flash appears on tap | Set `-webkit-tap-highlight-color` when the UI provides its own press feedback |
| Bottom content sits under browser chrome | Use `100dvh` for an app shell and account for the keyboard and safe areas |
| Hero shifts or is cut off while scrolling | Use `100svh` for a stable first screen |
| Focusing an input zooms the page | Keep input text at least 16px; preserve user zoom |
| Tap feels delayed | Use immediate `:active` feedback and suitable `touch-action` |
| Pull-to-refresh moves the page behind a sheet | Apply `overscroll-behavior` only to the relevant app surface |
| Header or bottom bar touches the notch | Use `viewport-fit=cover` with matching safe-area padding |
| Long press selects a button label | Disable selection on the control only |
| Carousel steals vertical scrolling | Set the correct `touch-action` or use native scroll snapping |
| Keyboard covers the focused field | Check viewport resize behavior and scroll the field into view |
| Status bar color clashes with the page | Match `theme-color` to the page surface and color scheme |
| Emulation passes but the phone fails | Verify on the target phone and browser |

## Fixes

### Hover and press feedback

Put hover styles behind both capability checks. The primary input must support hover and be precise.

```css
@media (hover: hover) and (pointer: fine) {
  .button:hover {
    background: var(--surface-hover);
  }
}
```

Give every tappable control a clear press state. Keep it brief and use the project's motion tokens.


If the browser highlight clashes with the design, remove it only after adding your own press and focus feedback.

```css
html {
  -webkit-tap-highlight-color: transparent;
}
```

```css
.button:active {
  transform: scale(0.98);
}
```


### Viewport and keyboard

Use a basic viewport declaration for web pages:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

For app shells and pinned controls, use `100dvh` when the layout should follow the visible viewport. Use `100svh` for a stable hero that must fit when browser chrome is expanded. Keep a `100vh` fallback only when the support matrix requires it. Do not use dynamic units on a long marketing page if their changes cause unwanted layout shifts.

Test the software keyboard on the actual target browser. Add an appropriate viewport keyboard-resize option only when the supported browser needs it. Scroll the focused input into view and keep bottom actions reachable.

### Inputs and one-time codes

Set inputs, textareas, and selects to at least 16px where small text causes mobile zoom. Do not hide browser zoom controls. Choose semantic input types and keyboard hints, such as `type="email"`, `inputmode="numeric"`, and `enterkeyhint="search"`.

Use the platform's one-time-code autofill hint for verification fields:

```html
<input type="text" inputmode="numeric" autocomplete="one-time-code" />
```

Keep autocomplete and capitalization settings appropriate to the field. Do not add custom keyboard or autofill behavior when native attributes work.

### Tap response and gesture ownership

Use `touch-action: manipulation` on controls when it improves tap handling without removing an expected gesture. Style `:active` for immediate feedback. Use JavaScript pointer handlers only when CSS cannot express the interaction.


```css
button,
a,
[role="button"] {
  touch-action: manipulation;
}
```

Keep this on controls, not the whole page or a surface that needs a different pan gesture.

Name which movement the browser may keep:

```css
/* Horizontal carousel: vertical page scrolling stays with the browser. */
.carousel {
  touch-action: pan-y;
}

/* Custom drag surface: reserve this only for the element that owns the drag. */
.drag-surface {
  touch-action: none;
}
```

For horizontal carousels that do not need custom physics, prefer `overflow-x: auto` with `scroll-snap-type`. Avoid non-passive `touchmove` listeners and `preventDefault()` as a general scroll fix.

### Scroll and pull-to-refresh

For an app-like full-screen surface that intentionally owns overscroll, use `overscroll-behavior` on that surface. Use `contain` on inner lists or sheets when scroll chaining should stop at their edge. Preserve normal page scrolling and pull-to-refresh on document-style websites when users expect them.


```css
.sheet-content {
  overflow-y: auto;
  overscroll-behavior: contain;
}
```

Use `overscroll-behavior: none` on a root only for an app-like surface that owns the gesture and still lets users reach all content.

### Safe areas and fixed controls

Use `viewport-fit=cover` only when the page paints edge to edge and applies padding to content that could overlap device cutouts or the home indicator.

```css
.app-header {
  padding-top: env(safe-area-inset-top, 0px);
}

.bottom-bar {
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
```

Check fixed headers, bottom tabs, dialogs, sheets, and toasts. Keep the background edge-to-edge while the interactive content stays inside the safe area.

### Text selection and callouts

Prevent long-press selection only on controls that should behave as controls. Keep paragraph text, addresses, codes, and error messages selectable.

```css
button,
[role="button"],
.tab,
.chip {
  user-select: none;
  -webkit-user-select: none;
}
```

Add `-webkit-touch-callout: none` only to a control where the callout is a real problem. Never apply these rules to `body`.

### Theme color and installed PWAs

Set `theme-color` to match the top page surface. If the page supports light and dark schemes, provide values that match each one. Keep the web manifest's theme and background colors aligned for installed PWAs. Use platform status-bar metadata only for a supported installed mode and verify it on the target device.


```html
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0a0a0a" />
```

Replace these sample colors with the actual page surface, and use separate values only if both schemes exist.

## Mobile performance and accessibility

- Prefer native scrolling and CSS behavior over a JavaScript loop that measures or moves elements during every frame.
- Reserve media space with dimensions or `aspect-ratio` to avoid layout shifts. Use responsive image sources when the project has them. Do not lazy-load the first visible, largest content by default.
- Keep touch targets large enough for the platform and user needs. Do not sacrifice visible focus, keyboard use, contrast, or reduced-motion support for a native look.
- Use measured performance tools when the user asks for a performance audit or the symptom points to a measured bottleneck. This skill does not replace a full performance review.

## Device verification

Use the actual target phone and browser for behavior that depends on touch or browser chrome. Check the URL bar expanded and collapsed, the software keyboard open, one landscape state, and installed PWA mode when the product supports it. Check both iOS Safari and Android Chrome when both are supported. Include an older target device when available.

If no phone is available, continue with code review or a simulator where useful. State which behaviors still need hardware verification. Do not report an emulation-only check as a real-device pass.

## Completion note

Keep the report short:

- Symptom and cause.
- File and change.
- What was verified in code, on a simulator, and on real hardware.
- Any phone-only behavior that still needs a device check.
