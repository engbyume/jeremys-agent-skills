# Jeremy's Agent Skills

A human-readable index of agent skills, grouped by the problem they help solve. Browse the categories, then use the catalog to check each source and install command.

## Start here

- [Skill catalog](skills.md): purpose-first descriptions, creator profiles, source repositories, and direct install commands.
- [Sources and credits](SOURCES.md): original authorship and source information.
- [YAML Wiki Framework guide](frameworks/yaml-wiki-framework.md): a separate reference guide, not an installable skill.

## 1. General all-agent skills

### Memory and knowledge

Preserve useful context and make past information easier to find again.

- [Glean](https://github.com/robabby/claude-skills): Surfaces patterns and recurring ideas across saved notes, so useful knowledge is easier to spot and reuse.
- [Graphify](https://github.com/Graphify-Labs/graphify): Turns a codebase, documents, or an Obsidian vault into a linked, explorable knowledge graph. Its visual report and Obsidian export help people and agents see how project context connects and trace ideas to their sources.
- [Hydrate](https://github.com/robabby/claude-skills): Reopens the right project context at the start of a session by gathering current status, priorities, and decisions from Obsidian.
- [Pickup](https://github.com/robabby/claude-skills): Creates a copy-ready handoff for a fresh session, preserving the goal, verified progress, decisions, blockers, and next steps.
- [Recall](https://github.com/robabby/claude-skills): Finds relevant stored knowledge by matching both keywords and concepts, so past decisions can inform current work.
- [Reflect](https://github.com/robabby/claude-skills): Turns a finished session into a small, useful set of lessons and cleaned-up memory. It consolidates what matters without keeping an entire transcript.
- [Remember](https://github.com/robabby/claude-skills): Stores user-approved facts and decisions as Obsidian notes that can be retrieved in future work.
- [Vault Status](https://github.com/robabby/claude-skills): Shows the connected Obsidian vault's structure, recent changes, file counts, and health, helping you decide where to look or what to maintain next.

### Agent workflows

Help agents manage context, coordination, skill maintenance, model choices, and repeatable work.

- [Background Skill Fixer](https://github.com/engbyume/background-skill-fixer) (by Jeremy): Repairs a skill after its advertised capability fails bounded retries, while the parent keeps the user's task moving through an authorized fallback. It targets the cause of the failure so future work can use the skill reliably.
- [Lean Context](https://github.com/yvgude/lean-ctx): Helps agents stay focused in large code tasks by retrieving relevant files and symbols, compressing command output, and showing what context was actually viewed. This cuts unnecessary reading while leaving source material intact.
- [Session Skill Audit](https://github.com/aiwithremy/session-skill-audit): Reviews a full session transcript, including earlier turns, to explain why a skill was missed or failed and identify the smallest evidence-backed fix. It is a diagnostic audit, not automatic permission to rewrite instructions.
- [Sol Advisor](https://github.com/DannyMac180/sol-advisor): Helps the parent decide when to work solo, delegate a bounded task, request an audit, or run a fuller review. It keeps risk, role boundaries, and parent-owned acceptance in view.
- [Using Superpowers](https://github.com/obra/superpowers): Provides a map for discovering and applying Superpowers workflows for planning, coding, debugging, review, and delivery. It helps choose a disciplined method for the work at hand.

### Planning and quality

Clarify the goal, shape an approach, and check the result against visible criteria.

- [Brainstorming](https://github.com/obra/superpowers): Turns an early request into a shared understanding of the problem, constraints, desired outcome, and options before implementation or creative work begins.
- [Coding Standards](https://github.com/affaan-m/ECC): Helps keep code readable and maintainable with clear naming, simple structure, and consistent conventions across projects. It provides a baseline when no framework-specific guide applies.
- [Evaluation Harness](https://github.com/affaan-m/ECC): Defines repeatable capability and regression evaluations for agent or software behavior, then uses graders and repeated runs to measure reliability. It helps compare changes against clear success criteria.
- [Link Check](https://github.com/robabby/claude-skills): Keeps an Obsidian vault navigable by finding broken wiki-links and notes with no incoming links. It also summarizes overall link health for maintenance.
- [Skill Creator](https://github.com/anthropics/skills): Helps design, revise, and evaluate agent skills so their triggers, instructions, and supporting files lead to reliable behavior. It can test performance and improve a skill's discovery description.
- [TDD Workflow](https://github.com/affaan-m/ECC): Anchors implementation in observable behavior: write a failing test, make the smallest change that passes, then refactor. This helps reduce unverified changes and catch regressions early.
- [Verification Loop](https://github.com/affaan-m/ECC): Provides a consistent final quality pass for code changes, checking builds, types, lint, tests, security patterns, and diffs before producing a pass or fail report.
- [Web App Testing](https://github.com/anthropics/skills): Exercises local web apps through Playwright to confirm pages and user flows work as expected. It can capture screenshots, inspect browser logs, and help diagnose visible behavior.

### Research and investigation

Gather evidence from the web, apps, and people.

- [Agent Browser](https://github.com/vercel-labs/agent-browser): Provides a command-line browser workflow for navigation, data extraction, forms, authentication, and UI testing. Accessibility snapshots and element references make repeated steps easier to inspect and verify.
- [Browser Use](https://github.com/browser-use/browser-use): Provides direct browser control through CDP or a hosted browser, so agents can research sites, inspect apps, and run browser-based tests. It supports common clients such as Playwright and Puppeteer.
- [User Research](https://github.com/cookiy-ai/user-research-skill): Guides a research study from product question to evidence: plan methods, write interview or survey guides, recruit participants, run interviews or usability studies, and synthesize findings. It can also support Cookiy's AI-moderated studies.

### Writing and communication

Turn information into clear documents, internal updates, and natural prose.

- [Document Co-authoring](https://github.com/anthropics/skills): Helps people shape structured documents through an iterative process: gather context, agree on an outline, draft, revise, and check whether the result works for its readers.
- [Internal Communications](https://github.com/anthropics/skills): Helps create organization-specific messages such as leadership updates, status reports, incident reports, FAQs, newsletters, and project updates, using the formats the organization prefers.
- [Sepia](https://github.com/Nanako0129/sepia): Helps prose sound natural and suited to its audience while preserving the writer's intent. It can draft, diagnose AI-like phrasing, make targeted edits, or rewrite professional and fiction writing.

### Creative and visual work

Create visual concepts, interfaces, and polished assets.

- [Algorithmic Art](https://github.com/anthropics/skills): Creates original generative art with p5.js, using seeded randomness and adjustable parameters to explore visual ideas repeatably.
- [Brand Guidelines](https://github.com/anthropics/skills): Applies Anthropic's official colors and typography when an artifact needs to follow Anthropic's visual identity.
- [Canvas Design](https://github.com/anthropics/skills): Turns a visual concept into an original static composition, such as a poster or artwork, for PNG or PDF. It starts with a design philosophy and expresses it visually.
- [Designmaxxing](https://github.com/engbyume/designmaxxing) (by Jeremy): Helps establish a clear, user-centered visual and interaction direction for a website, app, game, or design system. It frames audience, product needs, accessibility, usability, and relevant specialist skills before design decisions spread.
- [Frontend Design](https://github.com/anthropics/skills): Helps make interfaces distinct and intentional through aesthetic direction, typography, hierarchy, and component styling. It aims to avoid generic template-looking results while keeping the product usable.
- [Slack GIF Creator](https://github.com/anthropics/skills): Creates Slack-ready animated GIFs with timing, dimensions, and file-size constraints in mind. Its guidance and validation tools help keep loops legible in emoji and message formats.
- [Theme Factory](https://github.com/anthropics/skills): Applies a cohesive color and font theme to slides, documents, reports, or simple web artifacts. Choose from curated themes or create one to fit the project.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): Provides a searchable design reference for product interfaces across web, mobile, and desktop. It brings together styles, color palettes, typography, UX and accessibility guidance, design tokens, charts, icons, and stack-specific patterns for a consistent result.

### Documents and data

Work with common office files and structured information.

- [PDF](https://github.com/anthropics/skills): Supports the full lifecycle of PDF work, including reading and extracting text or tables, OCR for scanned pages, form filling, editing, merging, splitting, and creating PDFs.
- [PowerPoint](https://github.com/anthropics/skills): Helps create, read, and revise PowerPoint presentations, working with templates, layouts, speaker notes, comments, and visual content.
- [Spreadsheet Workflows](https://github.com/anthropics/skills): Handles spreadsheet creation and editing, formula work, data cleanup, charts, and conversions across Excel, CSV, and TSV. It is intended for tasks where the spreadsheet itself is the main deliverable.
- [Word Documents](https://github.com/anthropics/skills): Supports creating, reading, editing, and reorganizing Word files while preserving document structure and formatting. It also handles templates, tables, images, tracked changes, and comments.

### Software development

Build APIs, interfaces, MCP servers, and other software with reusable patterns.

- [Backend Patterns](https://github.com/affaan-m/ECC): Guides server-side design for Node.js, Express, and Next.js APIs, including route structure, data access, and database performance. It helps keep backend behavior reliable and maintainable.
- [Claude API](https://github.com/anthropics/skills): Helps build and maintain Anthropic API and SDK integrations with provider-specific guidance on model IDs, request parameters, streaming, tool use, caching, token counts, and migrations. Use it to check details before implementation when provider behavior changes.
- [Frontend Patterns](https://github.com/affaan-m/ECC): Guides React and Next.js implementation across components, state, data loading, and rendering performance. It helps keep interfaces easier to build, review, and scale.
- [MCP Builder](https://github.com/anthropics/skills): Helps turn an external API or service into a high-quality MCP server with tools that map to real user tasks, plus well-designed resources and prompts. It covers secure integrations in Python or TypeScript.
- [Open Source Inspector](https://github.com/vercel-labs/opensrc): Fetches dependency source at its matching version so you can inspect the implementation, not only its types or docs. Use it to answer how a library behaves internally.
- [Postgres Patterns](https://github.com/affaan-m/ECC): Guides PostgreSQL schema, query, and index choices to keep data access fast and safe. It also covers row-level security and related Supabase patterns.
- [Web Artifacts Builder](https://github.com/anthropics/skills): Helps build polished, interactive HTML experiences for Claude, especially when an artifact needs several components, state, routing, or a UI component library. It suits richer experiences than a simple single-file page.

### Media analysis

Understand video by linking spoken content to exact moments.

- [Watch](https://github.com/bradautomates/claude-video): Helps an agent understand a video by combining its spoken transcript with timestamped frames. It can answer questions about specific moments and supports captions, local transcription, or configured cloud analysis.

### Security

Reduce application risk and guide authorized vulnerability assessment.

- [Mantis Pipeline](https://github.com/deonmenezes/mantishack): Orchestrates a scoped vulnerability-discovery engagement from reconnaissance through detection, reachability, validation, and reporting. It ties findings to their evidence and tools, and allows active testing only within explicit authorization.
- [Security Review](https://github.com/affaan-m/ECC): Helps spot application security issues in authentication, user input, secrets, API routes, payments, and other sensitive features. It supports safer implementation and release review.
- [Securitymaxxing](https://github.com/engbyume/securitymaxxing) (by Jeremy): Sets an application-security baseline from planning through implementation, review, testing, and release preparation. It routes architecture-specific checks and security specialists without authorizing scans or release.

## 2. Codex-adapted skills

Skills tailored specifically for OpenAI Codex workflows, model routing, and self-improvement.

- [Codex Harness Free Model Router](https://github.com/engbyume/codex-harness-free-model-router) (by Jeremy): Helps configure a local model router for Codex using your own providers, endpoints, models, and fallback rules. It keeps provider choices and credentials under your control and assumes no presets.
- [Codex Recursive Self-Improvement](https://github.com/engbyume/codex-recursive-self-improvement) (by Jeremy): Reviews task evidence for repeatable agent mistakes and turns verified causes into small, authorized improvements to prompts, skills, checks, memory, or runbooks. It improves the surrounding workflow, not model weights or hidden system messages.
- [Codex Budget Model Router](https://github.com/engbyume/codex-budget-model-router) (by Jeremy): Routes Codex parent and subagent work across GPT-6 Luna / max (easy/medium), GPT-6.1 Terra / low (routine hard), and GPT-6.2 Sol / medium (complex/high-risk).

## 3. Gemini-adapted skills

Skills tailored specifically for Gemini / Antigravity workflows and model routing.

- [Gemini Free Trial Model Router](https://github.com/engbyume/gemini-free-trial-model-router) (by Jeremy): Model router for users on the free trial of the $20 Gemini plan without access to higher-tier paid models, routing across Hydrogen Low (easy/medium), Hydrogen Medium (routine/regular hard), and Hydrogen High (extra-hard/complex+).

## Created by Jeremy

Six skills in this catalog are original work by Jeremy, shaped by workflows he developed and refined. Each has its own public source repository and is marked beside its name above.
