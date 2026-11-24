# Sources and provenance

This source ledger records the provenance decisions for the public catalog. One-word category folders and activation labels were added on 2026-11-17; upstream skill instructions remain with their authors.

## Included repositories

| Repository | Why it is included |
| --- | --- |
| [openai/plugins](https://github.com/openai/plugins) | Public source pinned to `82fd64bce3869f0d4c0bb2bf0e36a6e262ca5ad8`; 122 active skills are catalog-only links. GitHub reports no repository license metadata, so no upstream instructions are copied. |
| [engbyume/progressive-codex-model-router](https://github.com/engbyume/progressive-codex-model-router) | Owner-published standalone public-safe Codex skill for cost-aware subagent routing, with the parent on GPT-6 Luna / max. |
| [engbyume/background-skill-fixer](https://github.com/engbyume/background-skill-fixer) | Owner-published standalone public-safe skill for isolated root-cause repair of failed skills while the parent continues its authorized task. |
| [obra/superpowers](https://github.com/obra/superpowers) | Present in the skills lockfile. |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Present in the skills lockfile and used as a general browser automation capability. |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | User-requested cross-platform desktop automation skill, reviewed at the Apache-2.0 v1.2.0 release commit `2b0a7334fc111730454b726e6800aa41cdafc093`; the third-party skill body is not copied into this catalog. |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Present in the skills lockfile and used for browser automation workflows. |
| [anthropics/skills](https://github.com/anthropics/skills) | Installed Git repository containing general-purpose document, design, planning, and developer skills. |
| [robabby/claude-skills](https://github.com/robabby/claude-skills) | Installed Git repository containing memory, workflow, coding, testing, and quality skills, including the YAML-frontmatter memory architecture documented in this catalog. |
| [deonmenezes/mantishack](https://github.com/deonmenezes/mantishack) | Installed Git repository containing an authorized security workflow. |
| [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc) | Installed Git repository containing a general source-inspection skill. |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Installed Git repository containing general UI/UX design intelligence. |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | User-requested shadcn skill pinned to commit `d2fba50ee5b9113008b5bb908563527b7efd2f27`; local adapted copy passed complete static review and is not mirrored here. |
| [cookiy-ai/user-research-skill](https://github.com/cookiy-ai/user-research-skill) | Installed Git repository containing a general user-research workflow. |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | Installed Git repository containing a general video analysis workflow. |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Installed context tools with bounded raw-CLI and retry-safe modes plus a writable native fallback for MCP failures (2026-09-29). |
| [DannyMac180/sol-advisor](https://github.com/DannyMac180/sol-advisor) | Installed Codex plugin with public repository metadata; cataloged for risk-gated role routing, cost-aware selection, and parent-owned verification. The local routing overlay uses Luna / Max by default, Sol / High for hard work, and Astra / High for very complex short work; it does not change upstream. |
| [olsenbrands/sol-foreman](https://github.com/olsenbrands/sol-foreman) | Upstream source for the former local Sol Foreman workflow; its license is retained. The owner-published Progressive Codex Model Router adaptation lives in its own public repository, which this catalog links to. Upstream remains unchanged. |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | GitHub source verified from the installed skill documentation. |
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | Scoped `skills/sepia` package installed after static audit; repository-level CI workflow quarantined. A local writing adapter combines structure-aware narrative and professional-prose routes with conditional surface-style and formatting checks plus evidence-gated model guidance; upstream unchanged. |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | `skills/i-have-adhd` installed after universal static audit; active copy is mandatory for agent responses. |
| [engbyume/codex-harness-free-model-router](https://github.com/engbyume/codex-harness-free-model-router) | Public standalone package for a provider-neutral, user-configured Codex model router, local daemon, fallback panel, real availability tracking, and optional provider client-header support; snapshot updated at commit `b591882` (2026-09-08). |
| [engbyume/codex-recursive-self-improvement](https://github.com/engbyume/codex-recursive-self-improvement) | Public standalone package for mandatory post-action learning and programmatic tool calling audits for ChatGPT and the Codex harness; snapshot at commit `fc52786` (2026-09-12). |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Existing local skill passed static audit and is mandatory for simplicity and YAGNI decisions. |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Official Headroom source installed as a local compression tool; use it as a mutually exclusive alternative to Lean CTX and RTK. |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Official Rust Token Killer source built and installed as a command-output optimizer; bundled agent skills were not installed. |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | User-requested MIT coding-agent audit skill pinned to c1c8a8c1471069fb0e188eeaff69b8e8db6564a8. Skillspector 2.13.4 left four validator files partially inspected, so this is catalog-only and inactive until complete source coverage is restored. No upstream instructions are copied. |

| [apify/agent-skills](https://github.com/apify/agent-skills) | Official Apify-maintained scraper skill installed from skills/apify-ultimate-scraper at audited commit d522584df6d01746d76b0c674f375cc7d48a838f; local safeguards cover login, tokens, target authorization, and billable runs. |
| [rebelytics/one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) | Audited at commit `56e890712273ce231b478adc56ee2eb81101c3d6`; its Task Observer workflow informed a Codex-native, hook-free package for prompt-start, material-change, and end audits. The adaptation now checks goal continuity through retries and fallback. Added 2026-10-14 after public-safety review. |
| [NVIDIA/skillspector](https://github.com/NVIDIA/skillspector) | Apache-2.0 scanner source updated to verified main commit `3fb77b4cc9a97724481a6745157efcbfb20e2f32`; focused parser and reference-resolution regression tests passed. The cataloged skill-inspector adaptation remains sourced from commit `4c52fbb83bbca0dd13f2685453c9b661d8c95bf8`. |
| [garrytan/gbrain](https://github.com/garrytan/gbrain) | Owner-requested, redacted local-first memory adapter based on upstream commit 44eb0493ff2776f04d6616b1a526657702f7544a; it does not enable automatic capture, provider calls, or machine-specific configuration. |

## Referenced tools

| Repository | Use in this catalog |
| --- | --- |
| [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | Referenced by Securitymaxxing for a mandatory applicability check on operational SOC telemetry and incident work. Current main was reviewed at `010a3981bfc791266d62aaa31531f05798531efd`; no product code, telemetry, credentials, or deployment configuration is copied here. |
| [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) | User-requested MIT implementation source for intentional smooth scrolling on browser DOM surfaces. It wraps native scrolling and its current README keeps reduced-motion behavior enabled by default. Use only when smooth scrolling fits the product and verify anchors and nested scroll. |
| [greensock/GSAP](https://github.com/greensock/GSAP) | User-requested source for complex JavaScript animation and ScrollTrigger on compatible surfaces. Its current README says commercial use is free; verify current terms, framework support, and cleanup guidance when implementing. |
| [tengbao/vanta](https://github.com/tengbao/vanta) | User-requested optional source for animated browser backgrounds using Three.js/WebGL or p5. MIT licensed. GitHub reported its last push as 2024-03-03 at the 2026-11-20 review, so verify maintenance, dependencies, and performance before using it in production. |
| [usestrix/strix](https://github.com/usestrix/strix) | Required default dynamic assessment for runnable, owned or explicitly authorized web apps on local or staging when scope, sandbox, Docker, and paid LLM gates are satisfied. Apache-2.0. |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Required project-start and pre-release scans for repositories, IaC, and built images. Explicitly enable misconfiguration and license scanners; full license scanning is for release review. Apache-2.0. |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | Required project-start and pre-release local filesystem and Git-history secret scans. Verification stays off by default; external account and cloud scans need explicit scope. AGPL-3.0. |
| [Cisco-Talos/clamav](https://github.com/Cisco-Talos/clamav) | Required malware scanning when products process untrusted file uploads or email attachments. Quarantine detections, keep signatures fresh, avoid automatic deletion, and keep unauthenticated TCP sockets private. GPL-2.0. |
| [microsoft/PyRIT](https://github.com/microsoft/PyRIT) | Required security and safety evaluation for products with generative-AI features. Use synthetic inputs and authorized local or staging targets. MIT. |
| [qybaihe/bla](https://github.com/qybaihe/bla) | Reviewed as an optional defense-in-depth candidate for proprietary release artifacts only. It does not hide public open-source code or guarantee resistance to human or other tool analysis; never make it a universal requirement. MIT. |

## Explicitly approved local entries

These entries have no claimed upstream repository. The descriptions are public-safe, and approved first-party packages are under `skills/<category>/<skill>/`.

| Skill | Why it is included |
| --- | --- |
| Codex Usage Fallback Router | Explicitly approved local skill for quota checks, a 10%-remaining weekly global stop, and a permitted five-hour fallback at the 5% threshold. |
| Eval Loop | Explicitly approved local skill for bounded verification. A retry limit ends the current approach, not the goal; replan and keep safe work moving. |
| Autonomous Skill Routing | Explicitly approved local skill for compact skill discovery, safe defaults, and keeping the same goal active through failures and fallbacks. |
| Agent Mentor | Explicitly approved local skill for authority, scope, and runtime evidence checks. |
| Jeremy Batch | Explicitly approved local skill for batching independent operations. |
| Composio CLI | Explicitly approved local skill for mandatory Composio discovery and schema guidance; tool calls remain task-scoped. |
| Usage Limit Resume | Explicitly approved local skill for passive reset checkpoints. It pauses all goals at 10% weekly remaining, keeps quota reads in the active task, preserves reserve and final-review safeguards, and creates no task-specific automation. |
| Codex Email Approval Gateway | Public-safe first-party skill for once-per-reset 5% quota alerts observed inside an active task and verified same-thread approval replies relayed to the matching Codex task. It uses no scheduled poller and preserves native permission gates. |
| Designmaxxing | First-party visual-design guidance for websites, apps, game UI, widgets, and other visual products. It adapts principles to platform, routes 3D scenes to engine-specific skills, and includes Agent Desktop, Awwwards MCP, accessibility, privacy safeguards, contextual carousel, modal, autofill, stepper, and choice guidance, plus conditional Lenis, GSAP, and Vanta tooling. Product-specific policies use scope-matched [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) templates. Updated 2026-11-23. |
| Mobile Native | Explicitly approved first-party, portable, web-only guidance for mobile websites, web apps, and PWAs. Covers viewport, inputs, touch, scrolling, safe areas, keyboard behavior, mobile performance, and real-device verification. Does not apply to React Native. |
| Securitymaxxing | First-party application-security skill with 70 core and 23 conditional checks, mandatory project lifecycle scans, a whole-project security and legal readiness audit, password-reset and poisoning safeguards, and a 101-scenario defensive threat catalog. Controls remain architecture-dependent. Updated 2026-11-21. |
| Platform Architecture | First-party conditional guidance for backend, distributed systems, push-based realtime updates, data consistency, delivery, observability, recovery, and public-product service selection; routes detailed work to existing specialists. Added 2026-10-17. |
| Agent-Managed CI/CD | Public-safe first-party release workflow with deployment patterns, health checks, rollback, and explicit release gates. Added 2026-10-17. |
| Skill Inspector | Public-safe Apache-2.0 adaptation for mandatory Skillspector intake scanning, coverage review, source triage, and source-confirmed malware removal. |
| Universal Skill Audit | Public-safe first-party guidance for skill-source provenance, mandatory Skillspector scans, complete coverage, and evidence-based install decisions. |
| FitLab Verification | Explicitly approved project-local verification catalog entry. The catalog stores only a redacted summary; the detailed feature map stays with the application. Updated 2026-10-19. |

## Methodology

1. Enumerate installed skill directories and resolve their Git repositories.
2. Check the local skills lockfile for GitHub sources that are not represented by a local repository.
3. Keep public GitHub origins that could be verified, plus explicitly approved local skills with redacted entries.
4. Categorize each skill by its primary job and write a short description from its installed metadata.
5. Scan the final catalog for credentials, private prompts, machine paths, and unapproved platform or service entries.
6. Keep usage-saving process skills mandatory, route connector and specialized skills by task or condition, select one canonical source for duplicate manifests, and use a compact routing index instead of scanning every skill body.

General agent capabilities such as browser automation, context compression, graph-based knowledge organization, and source inspection are retained because they are reusable agent workflows. Platform-specific and tool-specific skills are included only when they add useful coverage within the selected 201-record catalog and have a verified public source. The selected OpenAI plugin entries link to pinned upstream files and do not copy their instructions.

## Provenance notes

- 2026-11-09: Aligned Usage Limit Resume final-review guidance with the parent-Luna, child-only Codex routing rule; preserved its serialized review action for compatibility.
- 2026-11-09: Published Progressive Codex Model Router as a standalone public repository. This catalog links to the root-level skill instead of bundling a second copy.
- 2026-11-14: Published Background Skill Fixer as a standalone public repository and added the full reviewed package to `skills/agents/background-skill-fixer`.
- 2026-11-14: Strengthened Designmaxxing, Securitymaxxing, and Platform Architecture with research-first capability planning, evidence-based reuse, current source checks, and justified custom implementation.
- 2026-11-16: Reconciled quota and email approval guidance to active-task-only checks. Preserve the weekly 10%-remaining global stop, send 5%-remaining alerts only when an active task observes the threshold, process replies only in the matching active task, and do not use scheduled pollers.
- 2026-11-16: Expanded Designmaxxing from the General-Legal policy-template route to a mandatory user-data baseline for products that collect personal data, with tracker consent, data rights, retention, subprocessors, transfer safeguards, security, and breach response.
- 2026-11-20: Added platform-aware visual scope and conditional Lenis, GSAP, and Vanta guidance to Designmaxxing. Lenis and Vanta are MIT licensed; the current GSAP README says commercial use is free. Vanta was last pushed in 2024, so the skill requires a current maintenance, compatibility, and performance check before use.
- 2026-11-20: Reinforced Securitymaxxing and aligned Designmaxxing with code-derived privacy policies, complete third-party disclosure, data minimization and deletion, server-side authorization, child safeguards, no ads or tracking by default, simple subscription cancellation, AI spend caps, trademark clearance, and license compatibility review.
- 2026-11-23: Added contextual Designmaxxing guidance for a 32% next-card preview in swipeable card sets, modal dimming, context-consistent important content, accessible address autofill with manual entry, connected step indicators, and progressive choice presentation. These are applied only when the matching interaction fits the product and platform.
- 2026-11-20: Added mandatory project-start and post-implementation checks with Trivy, TruffleHog, and Cloudflare's security-audit workflow. Strix is the required default for eligible runnable web targets; ClamAV applies to untrusted file intake and PyRIT to generative-AI features. BLA remains optional because it cannot hide public source and can impair review. The Cloudflare skill stays catalog-only because its pinned source scan is incomplete.
- 2026-11-21: Added an end-of-project Securitymaxxing audit of the whole product and applicable legal obligations. Strengthened reset-link origin, Host/forwarded-header, token, leakage, session, account-owner notification, and cache-poisoning controls. The 70 core and 23 conditional check counts remain unchanged.
- 2026-11-17: Expanded the catalog to 200 records using 122 active, source-pinned OpenAI plugin entries across life-science research, Vercel, Cloudflare, Expo, Apple development, web development, and Canva. These entries link to upstream SKILL.md files without copying their instructions.
- 2026-10-17: Added the pinned shadcn/ui source link. Its audited local adaptation is installed in Codex-compatible runtimes; third-party instructions are not copied into this library.

- 2026-10-15: Added the Apache-2.0 NVIDIA Skillspector source and two public-safe intake skills. The local intake route now requires no-LLM scans and source review for every skill change.
- 2026-10-12: Added a portable autonomy and hook-free fallback check for active skills, including routine authorized work, genuine action boundaries, and complete inventory audits.

- Repository links identify source repositories. This catalog links to those sources and does not imply that it created a copy or fork. The current catalog has 201 records after the owner-requested Cloudflare security-audit entry was added.
- On September 28, 2026, redacted local agent instructions were clarified to separate
  user authorization from goal-state evidence, avoid repeated continuation prompts,
  checkpoint at first-compaction thresholds, and avoid guessing active model identity.
  No upstream repository was changed by that local work.
- The YAML Wiki Framework guide is a descriptive synthesis for agents and users. It does not copy the upstream repository's private/local configuration or reproduce research-paper text.
- Paper links are public reference links: [Generative Agents](https://arxiv.org/abs/2304.03442) and [Mem0](https://arxiv.org/abs/2504.19413). They are labeled as conceptual inspiration only.
- `source_snapshot` values in `skills.json` are local commit identifiers where the source repository was available locally. They are provenance markers, not claims that the catalog vendors a particular version.
- Monorepo entries include their subpath so a reader can find the original skill in the upstream repository.
- The public catalog intentionally avoids local filesystem paths, secrets, credentials, environment files, raw prompts, and bundled third-party code.

## Exclusions

The following are not cataloged:

- **Aside skills:** bundled Aside resources and `aside-*` skills, per request.
- **Unapproved local or private operating skills:** personal mentor, workspace, memory, and machine-operation instructions where no public GitHub origin was verified and no explicit redacted-entry approval exists.
- **Tool or service-specific skills outside the selected catalog:** Anytype, Firecrawl, Higgsfield, Composio, Google Stitch, Unusual Whales, OfficeCLI, Scrapling, and other unselected hosted-service wrappers. The selected OpenAI plugin entries are source-only links.
- **Open Pencil:** excluded because it is a skill tightly coupled to the OpenPencil editor, despite having a public repository.
- **Unverified local skills:** skills with no GitHub remote, lockfile entry, or explicit upstream repository metadata.

Future entries need a verified public source and exact skill path. Record whether each entry links upstream or includes an approved package. Keep unselected inventory entries outside the current 201-record catalog unless Jeremy changes the scope.
