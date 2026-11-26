# Skill catalog

Find a skill by the kind of work it supports. Descriptions explain its purpose and the features that help achieve it.

Run an install command from the project where you want the skill. The Creator column links to the GitHub account that owns the original source repository.

## Skills by category

### Memory and knowledge

Preserve useful context and make past information easier to find again.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Glean | Surfaces patterns and recurring ideas across saved notes, so useful knowledge is easier to spot and reuse. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill glean` |
| Graphify | Turns a codebase, documents, or an Obsidian vault into a linked, explorable knowledge graph. Its visual report and Obsidian export help people and agents see how project context connects and trace ideas to their sources. | [@Graphify-Labs](https://github.com/Graphify-Labs) | [graphify](https://github.com/Graphify-Labs/graphify) | `npx skills add Graphify-Labs/graphify --skill graphify` |
| Hydrate | Reopens the right project context at the start of a session by gathering current status, priorities, and decisions from Obsidian. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill hydrate` |
| Pickup | Creates a copy-ready handoff for a fresh session, preserving the goal, verified progress, decisions, blockers, and next steps. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill pickup` |
| Recall | Finds relevant stored knowledge by matching both keywords and concepts, so past decisions can inform current work. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill recall` |
| Reflect | Turns a finished session into a small, useful set of lessons and cleaned-up memory. It consolidates what matters without keeping an entire transcript. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill reflect` |
| Remember | Stores user-approved facts and decisions as Obsidian notes that can be retrieved in future work. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill remember` |
| Vault Status | Shows the connected Obsidian vault's structure, recent changes, file counts, and health, helping you decide where to look or what to maintain next. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill vault-status` |

### Agent workflows

Help agents manage context, coordination, skill maintenance, model choices, and repeatable work.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Background Skill Fixer | Repairs a skill after its advertised capability fails bounded retries, while the parent keeps the user's task moving through an authorized fallback. It targets the cause of the failure so future work can use the skill reliably. | [@engbyume](https://github.com/engbyume) (Jeremy) | [background-skill-fixer](https://github.com/engbyume/background-skill-fixer) | `npx skills add engbyume/background-skill-fixer --skill background-skill-fixer` |
| Codex Harness Free Model Router | Helps configure a local model router for Codex using your own providers, endpoints, models, and fallback rules. It keeps provider choices and credentials under your control and assumes no presets. | [@engbyume](https://github.com/engbyume) (Jeremy) | [codex-harness-free-model-router](https://github.com/engbyume/codex-harness-free-model-router) | `npx skills add https://github.com/engbyume/codex-harness-free-model-router/tree/main/skill` |
| Codex Recursive Self-Improvement | Reviews task evidence for repeatable agent mistakes and turns verified causes into small, authorized improvements to prompts, skills, checks, memory, or runbooks. It improves the surrounding workflow, not model weights or hidden system messages. | [@engbyume](https://github.com/engbyume) (Jeremy) | [codex-recursive-self-improvement](https://github.com/engbyume/codex-recursive-self-improvement) | `npx skills add engbyume/codex-recursive-self-improvement --skill codex-recursive-self-improvement` |
| Lean Context | Helps agents stay focused in large code tasks by retrieving relevant files and symbols, compressing command output, and showing what context was actually viewed. This cuts unnecessary reading while leaving source material intact. | [@yvgude](https://github.com/yvgude) | [lean-ctx](https://github.com/yvgude/lean-ctx) | `npx skills add yvgude/lean-ctx --skill lean-ctx` |
| Codex Budget Model Router | Routes parent and child work so each task uses a suitable model and effort. It keeps shared changes, review, and final acceptance with the parent. | [@engbyume](https://github.com/engbyume) (Jeremy) | [codex-budget-model-router](https://github.com/engbyume/codex-budget-model-router) | `npx skills add engbyume/codex-budget-model-router --skill codex-budget-model-router` |
| Gemini Budget Model Router | Routes Gemini and Antigravity tasks across Hydrogen Low (easy/medium), Hydrogen Medium (routine/regular hard), and Hydrogen High (extra-hard/complex+). | [@engbyume](https://github.com/engbyume) (Jeremy) | [gemini-budget-model-router](https://github.com/engbyume/gemini-budget-model-router) | `npx skills add engbyume/gemini-budget-model-router --skill gemini-budget-model-router` |
| Session Skill Audit | Reviews a full session transcript, including earlier turns, to explain why a skill was missed or failed and identify the smallest evidence-backed fix. It is a diagnostic audit, not automatic permission to rewrite instructions. | [@aiwithremy](https://github.com/aiwithremy) | [session-skill-audit](https://github.com/aiwithremy/session-skill-audit) | `npx skills add https://github.com/aiwithremy/session-skill-audit/tree/main/session-skill-audit` |
| Sol Advisor | Helps the parent decide when to work solo, delegate a bounded task, request an audit, or run a fuller review. It keeps risk, role boundaries, and parent-owned acceptance in view. | [@DannyMac180](https://github.com/DannyMac180) | [sol-advisor](https://github.com/DannyMac180/sol-advisor) | `npx skills add DannyMac180/sol-advisor --skill orchestration` |
| Using Superpowers | Provides a map for discovering and applying Superpowers workflows for planning, coding, debugging, review, and delivery. It helps choose a disciplined method for the work at hand. | [@obra](https://github.com/obra) | [superpowers](https://github.com/obra/superpowers) | `npx skills add obra/superpowers --skill using-superpowers` |

### Planning and quality

Clarify the goal, shape an approach, and check the result against visible criteria.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Brainstorming | Turns an early request into a shared understanding of the problem, constraints, desired outcome, and options before implementation or creative work begins. | [@obra](https://github.com/obra) | [superpowers](https://github.com/obra/superpowers) | `npx skills add obra/superpowers --skill brainstorming` |
| Coding Standards | Helps keep code readable and maintainable with clear naming, simple structure, and consistent conventions across projects. It provides a baseline when no framework-specific guide applies. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill coding-standards` |
| Evaluation Harness | Defines repeatable capability and regression evaluations for agent or software behavior, then uses graders and repeated runs to measure reliability. It helps compare changes against clear success criteria. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill eval-harness` |
| Link Check | Keeps an Obsidian vault navigable by finding broken wiki-links and notes with no incoming links. It also summarizes overall link health for maintenance. | [@robabby](https://github.com/robabby) | [claude-skills](https://github.com/robabby/claude-skills) | `npx skills add robabby/claude-skills --skill link-check` |
| Skill Creator | Helps design, revise, and evaluate agent skills so their triggers, instructions, and supporting files lead to reliable behavior. It can test performance and improve a skill's discovery description. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill skill-creator` |
| TDD Workflow | Anchors implementation in observable behavior: write a failing test, make the smallest change that passes, then refactor. This helps reduce unverified changes and catch regressions early. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill tdd-workflow` |
| Verification Loop | Provides a consistent final quality pass for code changes, checking builds, types, lint, tests, security patterns, and diffs before producing a pass or fail report. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill verification-loop` |
| Web App Testing | Exercises local web apps through Playwright to confirm pages and user flows work as expected. It can capture screenshots, inspect browser logs, and help diagnose visible behavior. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill webapp-testing` |

### Research and investigation

Gather evidence from the web, apps, and people.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Agent Browser | Provides a command-line browser workflow for navigation, data extraction, forms, authentication, and UI testing. Accessibility snapshots and element references make repeated steps easier to inspect and verify. | [@vercel-labs](https://github.com/vercel-labs) | [agent-browser](https://github.com/vercel-labs/agent-browser) | `npx skills add vercel-labs/agent-browser --skill core` |
| Browser Use | Provides direct browser control through CDP or a hosted browser, so agents can research sites, inspect apps, and run browser-based tests. It supports common clients such as Playwright and Puppeteer. | [@browser-use](https://github.com/browser-use) | [browser-use](https://github.com/browser-use/browser-use) | `npx skills add browser-use/browser-use --skill browser-use` |
| User Research | Guides a research study from product question to evidence: plan methods, write interview or survey guides, recruit participants, run interviews or usability studies, and synthesize findings. It can also support Cookiy's AI-moderated studies. | [@cookiy-ai](https://github.com/cookiy-ai) | [user-research-skill](https://github.com/cookiy-ai/user-research-skill) | `npx skills add cookiy-ai/user-research-skill --skill user-research-cookiy` |

### Writing and communication

Turn information into clear documents, internal updates, and natural prose.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Document Co-authoring | Helps people shape structured documents through an iterative process: gather context, agree on an outline, draft, revise, and check whether the result works for its readers. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill doc-coauthoring` |
| Internal Communications | Helps create organization-specific messages such as leadership updates, status reports, incident reports, FAQs, newsletters, and project updates, using the formats the organization prefers. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill internal-comms` |
| Sepia | Helps prose sound natural and suited to its audience while preserving the writer's intent. It can draft, diagnose AI-like phrasing, make targeted edits, or rewrite professional and fiction writing. | [@Nanako0129](https://github.com/Nanako0129) | [sepia](https://github.com/Nanako0129/sepia) | `npx skills add Nanako0129/sepia --skill sepia` |

### Creative and visual work

Create visual concepts, interfaces, and polished assets.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Algorithmic Art | Creates original generative art with p5.js, using seeded randomness and adjustable parameters to explore visual ideas repeatably. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill algorithmic-art` |
| Brand Guidelines | Applies Anthropic's official colors and typography when an artifact needs to follow Anthropic's visual identity. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill brand-guidelines` |
| Canvas Design | Turns a visual concept into an original static composition, such as a poster or artwork, for PNG or PDF. It starts with a design philosophy and expresses it visually. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill canvas-design` |
| Designmaxxing | Helps establish a clear, user-centered visual and interaction direction for a website, app, game, or design system. It frames audience, product needs, accessibility, usability, and relevant specialist skills before design decisions spread. | [@engbyume](https://github.com/engbyume) (Jeremy) | [designmaxxing](https://github.com/engbyume/designmaxxing) | `npx skills add engbyume/designmaxxing --skill designmaxxing` |
| Frontend Design | Helps make interfaces distinct and intentional through aesthetic direction, typography, hierarchy, and component styling. It aims to avoid generic template-looking results while keeping the product usable. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill frontend-design` |
| Slack GIF Creator | Creates Slack-ready animated GIFs with timing, dimensions, and file-size constraints in mind. Its guidance and validation tools help keep loops legible in emoji and message formats. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill slack-gif-creator` |
| Theme Factory | Applies a cohesive color and font theme to slides, documents, reports, or simple web artifacts. Choose from curated themes or create one to fit the project. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill theme-factory` |
| UI/UX Pro Max | Provides a searchable design reference for product interfaces across web, mobile, and desktop. It brings together styles, color palettes, typography, UX and accessibility guidance, design tokens, charts, icons, and stack-specific patterns for a consistent result. | [@nextlevelbuilder](https://github.com/nextlevelbuilder) | [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max` |

### Documents and data

Work with common office files and structured information.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| PDF | Supports the full lifecycle of PDF work, including reading and extracting text or tables, OCR for scanned pages, form filling, editing, merging, splitting, and creating PDFs. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill pdf` |
| PowerPoint | Helps create, read, and revise PowerPoint presentations, working with templates, layouts, speaker notes, comments, and visual content. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill pptx` |
| Spreadsheet Workflows | Handles spreadsheet creation and editing, formula work, data cleanup, charts, and conversions across Excel, CSV, and TSV. It is intended for tasks where the spreadsheet itself is the main deliverable. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill xlsx` |
| Word Documents | Supports creating, reading, editing, and reorganizing Word files while preserving document structure and formatting. It also handles templates, tables, images, tracked changes, and comments. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill docx` |

### Software development

Build APIs, interfaces, MCP servers, and other software with reusable patterns.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Backend Patterns | Guides server-side design for Node.js, Express, and Next.js APIs, including route structure, data access, and database performance. It helps keep backend behavior reliable and maintainable. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill backend-patterns` |
| Claude API | Helps build and maintain Anthropic API and SDK integrations with provider-specific guidance on model IDs, request parameters, streaming, tool use, caching, token counts, and migrations. Use it to check details before implementation when provider behavior changes. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill claude-api` |
| Frontend Patterns | Guides React and Next.js implementation across components, state, data loading, and rendering performance. It helps keep interfaces easier to build, review, and scale. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill frontend-patterns` |
| MCP Builder | Helps turn an external API or service into a high-quality MCP server with tools that map to real user tasks, plus well-designed resources and prompts. It covers secure integrations in Python or TypeScript. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill mcp-builder` |
| Open Source Inspector | Fetches dependency source at its matching version so you can inspect the implementation, not only its types or docs. Use it to answer how a library behaves internally. | [@vercel-labs](https://github.com/vercel-labs) | [opensrc](https://github.com/vercel-labs/opensrc) | `npx skills add vercel-labs/opensrc --skill opensrc` |
| Postgres Patterns | Guides PostgreSQL schema, query, and index choices to keep data access fast and safe. It also covers row-level security and related Supabase patterns. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill postgres-patterns` |
| Web Artifacts Builder | Helps build polished, interactive HTML experiences for Claude, especially when an artifact needs several components, state, routing, or a UI component library. It suits richer experiences than a simple single-file page. | [@anthropics](https://github.com/anthropics) | [skills](https://github.com/anthropics/skills) | `npx skills add anthropics/skills --skill web-artifacts-builder` |

### Media analysis

Understand video by linking spoken content to exact moments.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Watch | Helps an agent understand a video by combining its spoken transcript with timestamped frames. It can answer questions about specific moments and supports captions, local transcription, or configured cloud analysis. | [@bradautomates](https://github.com/bradautomates) | [claude-video](https://github.com/bradautomates/claude-video) | `npx skills add bradautomates/claude-video --skill watch` |

### Security

Reduce application risk and guide authorized vulnerability assessment.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Mantis Pipeline | Orchestrates a scoped vulnerability-discovery engagement from reconnaissance through detection, reachability, validation, and reporting. It ties findings to their evidence and tools, and allows active testing only within explicit authorization. | [@deonmenezes](https://github.com/deonmenezes) | [mantishack](https://github.com/deonmenezes/mantishack) | `npx skills add deonmenezes/mantishack --skill mantis-pipeline` |
| Security Review | Helps spot application security issues in authentication, user input, secrets, API routes, payments, and other sensitive features. It supports safer implementation and release review. | [@affaan-m](https://github.com/affaan-m) | [ECC](https://github.com/affaan-m/ECC) | `npx skills add affaan-m/ECC --skill security-review` |
| Securitymaxxing | Sets an application-security baseline from planning through implementation, review, testing, and release preparation. It routes architecture-specific checks and security specialists without authorizing scans or release. | [@engbyume](https://github.com/engbyume) (Jeremy) | [securitymaxxing](https://github.com/engbyume/securitymaxxing) | `npx skills add engbyume/securitymaxxing --skill securitymaxxing` |

### Trust Pyramid & Engineering Rigor (pstack)

Enforce deterministic checks, runtime verification, and minimal slop-free changes across agent workflows.

| Skill | Description | Creator | Source repo | Install |
| --- | --- | --- | --- | --- |
| Poteto Mode | Default playbook router for rigorous engineering work across 23 playbooks, enforcing minimal changes and evidence-backed completion. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill poteto-mode` |
| Correct | Mines history for recurring agent mistakes and encodes each fix at the highest Trust Pyramid layer (architecture, types, lint, CI, tests, docs last). | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill correct` |
| Interrogate | Runs multi-lens adversarial diff reviews so different models and quality lenses try to break a change before shipping. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill interrogate` |
| Blast Radius | Evaluates what a small change could break and proves safety by running code rather than asserting it. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill blast-radius` |
| Architect | Settles caller usage, types, and module shape before writing code across function or module boundaries. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill architect` |
| Create Verification Skill | Generates a project-local verification skill with a feature map for any language or platform when no scripted proof exists. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill create-verification-skill` |
| Maintain Verification Skill | Keeps a project-local verification skill's feature map aligned with the live app via source and runtime checks. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill maintain-verification-skill` |
| No Comments | Strips redundant inline comments before review, flags claimed constraints, and encodes real invariants into structure. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill no-comments` |
| Unslop | Removes AI writing tells, filler phrases, and em-dash patterns from prose and documentation. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill unslop` |
| TypeScript Best Practices | Grounds type-system discipline in concrete TypeScript syntax when reading or editing TypeScript codebases. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill typescript-best-practices` |
| Benchmark Checklist | Vets performance measurements (limiters, tuning, errors, repeat runs, end-to-end relevance) before reporting or acting on them. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill benchmark-checklist` |
| How | Produces a concise walkthrough of how a subsystem works from verified source files. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill how` |
| Why | Investigates why a system was built a given way across source control, issues, docs, and logs. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill why` |
| TDD (pstack) | Enforces writing a failing test first on a cheap local test path, then implementing the minimal fix. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill tdd` |
| Show Me Your Work | Logs engineering decisions to a reviewable TSV trail that can be committed alongside changes. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill show-me-your-work` |
| Figure It Out | Designs a rigorous, auditable playbook when no bundled playbook fits the task. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill figure-it-out` |
| Arena | Runs N parallel attempts at the same problem and synthesizes the strongest parts of each. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill arena` |
| Swarm (pstack) | Coordinates N parallel workers across independent slices or races and returns one aggregated report. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill swarm` |
| Teach | Combines how and why investigations into a plain-language, diagram-driven explanation of a change or subsystem. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill teach` |
| Technical Writing | Applies a layered documentation standard (Diataxis, Google developer style, STE, Global English) to docs, RFCs, and PRs. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill technical-writing` |
| Bro | Restates the previous technical message in plain human language without jargon. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill bro` |
| Automate Me | Drafts a custom `-mode` skill based on observed workflow patterns. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill automate-me` |
| Poteto Help | Guides selection of the right pstack skill, playbook, or engineering principle for a task. | [@poteto](https://github.com/poteto) | [pstack](https://github.com/PickleBoxer/pstack) | `npx skills add PickleBoxer/pstack --skill poteto-help` |

