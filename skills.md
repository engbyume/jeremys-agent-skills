# Skill catalog

Find a skill by the kind of work it supports. Descriptions explain its purpose and the features that help achieve it.

Run an install command from the project where you want the skill. The Creator column links to the GitHub account that owns the original source repository.

## Skills by category

### Memory and knowledge

Preserve useful context and make past information easier to find again.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Glean</td><td width="42%">Surfaces patterns and recurring ideas across saved notes, so useful knowledge is easier to spot and reuse.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill glean</code></td></tr>
    <tr><td width="14%">Graphify</td><td width="42%">Turns a codebase, documents, or an Obsidian vault into a linked, explorable knowledge graph. Its visual report and Obsidian export help people and agents see how project context connects and trace ideas to their sources.</td><td width="12%"><a href="https://github.com/Graphify-Labs">@Graphify-Labs</a></td><td width="14%"><a href="https://github.com/Graphify-Labs/graphify">graphify</a></td><td width="18%"><code>npx skills add Graphify-Labs/graphify --skill graphify</code></td></tr>
    <tr><td width="14%">Hydrate</td><td width="42%">Reopens the right project context at the start of a session by gathering current status, priorities, and decisions from Obsidian.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill hydrate</code></td></tr>
    <tr><td width="14%">Pickup</td><td width="42%">Creates a copy-ready handoff for a fresh session, preserving the goal, verified progress, decisions, blockers, and next steps.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill pickup</code></td></tr>
    <tr><td width="14%">Recall</td><td width="42%">Finds relevant stored knowledge by matching both keywords and concepts, so past decisions can inform current work.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill recall</code></td></tr>
    <tr><td width="14%">Reflect</td><td width="42%">Turns a finished session into a small, useful set of lessons and cleaned-up memory. It consolidates what matters without keeping an entire transcript.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill reflect</code></td></tr>
    <tr><td width="14%">Remember</td><td width="42%">Stores user-approved facts and decisions as Obsidian notes that can be retrieved in future work.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill remember</code></td></tr>
    <tr><td width="14%">Vault Status</td><td width="42%">Shows the connected Obsidian vault's structure, recent changes, file counts, and health, helping you decide where to look or what to maintain next.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill vault-status</code></td></tr>
  </tbody>
</table>

### Agent workflows

Help agents manage context, coordination, skill maintenance, model choices, and repeatable work.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Background Skill Fixer</td><td width="42%">Repairs a skill after its advertised capability fails bounded retries, while the parent keeps the user's task moving through an authorized fallback. It targets the cause of the failure so future work can use the skill reliably.</td><td width="12%"><a href="https://github.com/engbyume">@engbyume</a> (Jeremy)</td><td width="14%"><a href="https://github.com/engbyume/background-skill-fixer">background-skill-fixer</a></td><td width="18%"><code>npx skills add engbyume/background-skill-fixer --skill background-skill-fixer</code></td></tr>
    <tr><td width="14%">Codex Harness Free Model Router</td><td width="42%">Helps configure a local model router for Codex using your own providers, endpoints, models, and fallback rules. It keeps provider choices and credentials under your control and assumes no presets.</td><td width="12%"><a href="https://github.com/engbyume">@engbyume</a> (Jeremy)</td><td width="14%"><a href="https://github.com/engbyume/codex-harness-free-model-router">codex-harness-free-model-router</a></td><td width="18%"><code>npx skills add https://github.com/engbyume/codex-harness-free-model-router/tree/main/skill</code></td></tr>
    <tr><td width="14%">Codex Recursive Self-Improvement</td><td width="42%">Reviews task evidence for repeatable agent mistakes and turns verified causes into small, authorized improvements to prompts, skills, checks, memory, or runbooks. It improves the surrounding workflow, not model weights or hidden system messages.</td><td width="12%"><a href="https://github.com/engbyume">@engbyume</a> (Jeremy)</td><td width="14%"><a href="https://github.com/engbyume/codex-recursive-self-improvement">codex-recursive-self-improvement</a></td><td width="18%"><code>npx skills add engbyume/codex-recursive-self-improvement --skill codex-recursive-self-improvement</code></td></tr>
    <tr><td width="14%">Lean Context</td><td width="42%">Helps agents stay focused in large code tasks by retrieving relevant files and symbols, compressing command output, and showing what context was actually viewed. This cuts unnecessary reading while leaving source material intact.</td><td width="12%"><a href="https://github.com/yvgude">@yvgude</a></td><td width="14%"><a href="https://github.com/yvgude/lean-ctx">lean-ctx</a></td><td width="18%"><code>npx skills add yvgude/lean-ctx --skill lean-ctx</code></td></tr>
    <tr><td width="14%">Progressive Codex Model Router</td><td width="42%">Routes parent and child work so each task uses a suitable model and effort. It keeps shared changes, review, and final acceptance with the parent.</td><td width="12%"><a href="https://github.com/engbyume">@engbyume</a> (Jeremy)</td><td width="14%"><a href="https://github.com/engbyume/progressive-codex-model-router">progressive-codex-model-router</a></td><td width="18%"><code>npx skills add engbyume/progressive-codex-model-router --skill progressive-codex-model-router</code></td></tr>
    <tr><td width="14%">Session Skill Audit</td><td width="42%">Reviews a full session transcript, including earlier turns, to explain why a skill was missed or failed and identify the smallest evidence-backed fix. It is a diagnostic audit, not automatic permission to rewrite instructions.</td><td width="12%"><a href="https://github.com/aiwithremy">@aiwithremy</a></td><td width="14%"><a href="https://github.com/aiwithremy/session-skill-audit">session-skill-audit</a></td><td width="18%"><code>npx skills add https://github.com/aiwithremy/session-skill-audit/tree/main/session-skill-audit</code></td></tr>
    <tr><td width="14%">Sol Advisor</td><td width="42%">Helps the parent decide when to work solo, delegate a bounded task, request an audit, or run a fuller review. It keeps risk, role boundaries, and parent-owned acceptance in view.</td><td width="12%"><a href="https://github.com/DannyMac180">@DannyMac180</a></td><td width="14%"><a href="https://github.com/DannyMac180/sol-advisor">sol-advisor</a></td><td width="18%"><code>npx skills add DannyMac180/sol-advisor --skill orchestration</code></td></tr>
    <tr><td width="14%">Using Superpowers</td><td width="42%">Provides a map for discovering and applying Superpowers workflows for planning, coding, debugging, review, and delivery. It helps choose a disciplined method for the work at hand.</td><td width="12%"><a href="https://github.com/obra">@obra</a></td><td width="14%"><a href="https://github.com/obra/superpowers">superpowers</a></td><td width="18%"><code>npx skills add obra/superpowers --skill using-superpowers</code></td></tr>
  </tbody>
</table>

### Planning and quality

Clarify the goal, shape an approach, and check the result against visible criteria.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Brainstorming</td><td width="42%">Turns an early request into a shared understanding of the problem, constraints, desired outcome, and options before implementation or creative work begins.</td><td width="12%"><a href="https://github.com/obra">@obra</a></td><td width="14%"><a href="https://github.com/obra/superpowers">superpowers</a></td><td width="18%"><code>npx skills add obra/superpowers --skill brainstorming</code></td></tr>
    <tr><td width="14%">Coding Standards</td><td width="42%">Helps keep code readable and maintainable with clear naming, simple structure, and consistent conventions across projects. It provides a baseline when no framework-specific guide applies.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill coding-standards</code></td></tr>
    <tr><td width="14%">Evaluation Harness</td><td width="42%">Defines repeatable capability and regression evaluations for agent or software behavior, then uses graders and repeated runs to measure reliability. It helps compare changes against clear success criteria.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill eval-harness</code></td></tr>
    <tr><td width="14%">Link Check</td><td width="42%">Keeps an Obsidian vault navigable by finding broken wiki-links and notes with no incoming links. It also summarizes overall link health for maintenance.</td><td width="12%"><a href="https://github.com/robabby">@robabby</a></td><td width="14%"><a href="https://github.com/robabby/claude-skills">claude-skills</a></td><td width="18%"><code>npx skills add robabby/claude-skills --skill link-check</code></td></tr>
    <tr><td width="14%">Skill Creator</td><td width="42%">Helps design, revise, and evaluate agent skills so their triggers, instructions, and supporting files lead to reliable behavior. It can test performance and improve a skill's discovery description.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill skill-creator</code></td></tr>
    <tr><td width="14%">TDD Workflow</td><td width="42%">Anchors implementation in observable behavior: write a failing test, make the smallest change that passes, then refactor. This helps reduce unverified changes and catch regressions early.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill tdd-workflow</code></td></tr>
    <tr><td width="14%">Verification Loop</td><td width="42%">Provides a consistent final quality pass for code changes, checking builds, types, lint, tests, security patterns, and diffs before producing a pass or fail report.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill verification-loop</code></td></tr>
    <tr><td width="14%">Web App Testing</td><td width="42%">Exercises local web apps through Playwright to confirm pages and user flows work as expected. It can capture screenshots, inspect browser logs, and help diagnose visible behavior.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill webapp-testing</code></td></tr>
  </tbody>
</table>

### Research and investigation

Gather evidence from the web, apps, and people.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Agent Browser</td><td width="42%">Provides a command-line browser workflow for navigation, data extraction, forms, authentication, and UI testing. Accessibility snapshots and element references make repeated steps easier to inspect and verify.</td><td width="12%"><a href="https://github.com/vercel-labs">@vercel-labs</a></td><td width="14%"><a href="https://github.com/vercel-labs/agent-browser">agent-browser</a></td><td width="18%"><code>npx skills add vercel-labs/agent-browser --skill core</code></td></tr>
    <tr><td width="14%">Browser Use</td><td width="42%">Provides direct browser control through CDP or a hosted browser, so agents can research sites, inspect apps, and run browser-based tests. It supports common clients such as Playwright and Puppeteer.</td><td width="12%"><a href="https://github.com/browser-use">@browser-use</a></td><td width="14%"><a href="https://github.com/browser-use/browser-use">browser-use</a></td><td width="18%"><code>npx skills add browser-use/browser-use --skill browser-use</code></td></tr>
    <tr><td width="14%">User Research</td><td width="42%">Guides a research study from product question to evidence: plan methods, write interview or survey guides, recruit participants, run interviews or usability studies, and synthesize findings. It can also support Cookiy's AI-moderated studies.</td><td width="12%"><a href="https://github.com/cookiy-ai">@cookiy-ai</a></td><td width="14%"><a href="https://github.com/cookiy-ai/user-research-skill">user-research-skill</a></td><td width="18%"><code>npx skills add cookiy-ai/user-research-skill --skill user-research-cookiy</code></td></tr>
  </tbody>
</table>

### Writing and communication

Turn information into clear documents, internal updates, and natural prose.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Document Co-authoring</td><td width="42%">Helps people shape structured documents through an iterative process: gather context, agree on an outline, draft, revise, and check whether the result works for its readers.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill doc-coauthoring</code></td></tr>
    <tr><td width="14%">Internal Communications</td><td width="42%">Helps create organization-specific messages such as leadership updates, status reports, incident reports, FAQs, newsletters, and project updates, using the formats the organization prefers.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill internal-comms</code></td></tr>
    <tr><td width="14%">Sepia</td><td width="42%">Helps prose sound natural and suited to its audience while preserving the writer's intent. It can draft, diagnose AI-like phrasing, make targeted edits, or rewrite professional and fiction writing.</td><td width="12%"><a href="https://github.com/Nanako0129">@Nanako0129</a></td><td width="14%"><a href="https://github.com/Nanako0129/sepia">sepia</a></td><td width="18%"><code>npx skills add Nanako0129/sepia --skill sepia</code></td></tr>
  </tbody>
</table>

### Creative and visual work

Create visual concepts, interfaces, and polished assets.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Algorithmic Art</td><td width="42%">Creates original generative art with p5.js, using seeded randomness and adjustable parameters to explore visual ideas repeatably.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill algorithmic-art</code></td></tr>
    <tr><td width="14%">Brand Guidelines</td><td width="42%">Applies Anthropic's official colors and typography when an artifact needs to follow Anthropic's visual identity.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill brand-guidelines</code></td></tr>
    <tr><td width="14%">Canvas Design</td><td width="42%">Turns a visual concept into an original static composition, such as a poster or artwork, for PNG or PDF. It starts with a design philosophy and expresses it visually.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill canvas-design</code></td></tr>
    <tr><td width="14%">Designmaxxing</td><td width="42%">Helps establish a clear, user-centered visual and interaction direction for a website, app, game, or design system. It frames audience, product needs, accessibility, usability, and relevant specialist skills before design decisions spread.</td><td width="12%"><a href="https://github.com/engbyume">@engbyume</a> (Jeremy)</td><td width="14%"><a href="https://github.com/engbyume/designmaxxing">designmaxxing</a></td><td width="18%"><code>npx skills add engbyume/designmaxxing --skill designmaxxing</code></td></tr>
    <tr><td width="14%">Frontend Design</td><td width="42%">Helps make interfaces distinct and intentional through aesthetic direction, typography, hierarchy, and component styling. It aims to avoid generic template-looking results while keeping the product usable.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill frontend-design</code></td></tr>
    <tr><td width="14%">Slack GIF Creator</td><td width="42%">Creates Slack-ready animated GIFs with timing, dimensions, and file-size constraints in mind. Its guidance and validation tools help keep loops legible in emoji and message formats.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill slack-gif-creator</code></td></tr>
    <tr><td width="14%">Theme Factory</td><td width="42%">Applies a cohesive color and font theme to slides, documents, reports, or simple web artifacts. Choose from curated themes or create one to fit the project.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill theme-factory</code></td></tr>
    <tr><td width="14%">UI/UX Pro Max</td><td width="42%">Provides a searchable design reference for product interfaces across web, mobile, and desktop. It brings together styles, color palettes, typography, UX and accessibility guidance, design tokens, charts, icons, and stack-specific patterns for a consistent result.</td><td width="12%"><a href="https://github.com/nextlevelbuilder">@nextlevelbuilder</a></td><td width="14%"><a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill">ui-ux-pro-max-skill</a></td><td width="18%"><code>npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max</code></td></tr>
  </tbody>
</table>

### Documents and data

Work with common office files and structured information.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">PDF</td><td width="42%">Supports the full lifecycle of PDF work, including reading and extracting text or tables, OCR for scanned pages, form filling, editing, merging, splitting, and creating PDFs.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill pdf</code></td></tr>
    <tr><td width="14%">PowerPoint</td><td width="42%">Helps create, read, and revise PowerPoint presentations, working with templates, layouts, speaker notes, comments, and visual content.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill pptx</code></td></tr>
    <tr><td width="14%">Spreadsheet Workflows</td><td width="42%">Handles spreadsheet creation and editing, formula work, data cleanup, charts, and conversions across Excel, CSV, and TSV. It is intended for tasks where the spreadsheet itself is the main deliverable.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill xlsx</code></td></tr>
    <tr><td width="14%">Word Documents</td><td width="42%">Supports creating, reading, editing, and reorganizing Word files while preserving document structure and formatting. It also handles templates, tables, images, tracked changes, and comments.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill docx</code></td></tr>
  </tbody>
</table>

### Software development

Build APIs, interfaces, MCP servers, and other software with reusable patterns.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Backend Patterns</td><td width="42%">Guides server-side design for Node.js, Express, and Next.js APIs, including route structure, data access, and database performance. It helps keep backend behavior reliable and maintainable.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill backend-patterns</code></td></tr>
    <tr><td width="14%">Claude API</td><td width="42%">Helps build and maintain Anthropic API and SDK integrations with provider-specific guidance on model IDs, request parameters, streaming, tool use, caching, token counts, and migrations. Use it to check details before implementation when provider behavior changes.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill claude-api</code></td></tr>
    <tr><td width="14%">Frontend Patterns</td><td width="42%">Guides React and Next.js implementation across components, state, data loading, and rendering performance. It helps keep interfaces easier to build, review, and scale.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill frontend-patterns</code></td></tr>
    <tr><td width="14%">MCP Builder</td><td width="42%">Helps turn an external API or service into a high-quality MCP server with tools that map to real user tasks, plus well-designed resources and prompts. It covers secure integrations in Python or TypeScript.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill mcp-builder</code></td></tr>
    <tr><td width="14%">Open Source Inspector</td><td width="42%">Fetches dependency source at its matching version so you can inspect the implementation, not only its types or docs. Use it to answer how a library behaves internally.</td><td width="12%"><a href="https://github.com/vercel-labs">@vercel-labs</a></td><td width="14%"><a href="https://github.com/vercel-labs/opensrc">opensrc</a></td><td width="18%"><code>npx skills add vercel-labs/opensrc --skill opensrc</code></td></tr>
    <tr><td width="14%">Postgres Patterns</td><td width="42%">Guides PostgreSQL schema, query, and index choices to keep data access fast and safe. It also covers row-level security and related Supabase patterns.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill postgres-patterns</code></td></tr>
    <tr><td width="14%">Web Artifacts Builder</td><td width="42%">Helps build polished, interactive HTML experiences for Claude, especially when an artifact needs several components, state, routing, or a UI component library. It suits richer experiences than a simple single-file page.</td><td width="12%"><a href="https://github.com/anthropics">@anthropics</a></td><td width="14%"><a href="https://github.com/anthropics/skills">skills</a></td><td width="18%"><code>npx skills add anthropics/skills --skill web-artifacts-builder</code></td></tr>
  </tbody>
</table>

### Media analysis

Understand video by linking spoken content to exact moments.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Watch</td><td width="42%">Helps an agent understand a video by combining its spoken transcript with timestamped frames. It can answer questions about specific moments and supports captions, local transcription, or configured cloud analysis.</td><td width="12%"><a href="https://github.com/bradautomates">@bradautomates</a></td><td width="14%"><a href="https://github.com/bradautomates/claude-video">claude-video</a></td><td width="18%"><code>npx skills add bradautomates/claude-video --skill watch</code></td></tr>
  </tbody>
</table>

### Security

Reduce application risk and guide authorized vulnerability assessment.

<table width="100%" style="table-layout: fixed;">
  <colgroup><col width="14%" /><col width="42%" /><col width="12%" /><col width="14%" /><col width="18%" /></colgroup>
  <thead><tr><th width="14%">Skill</th><th width="42%">Description</th><th width="12%">Creator</th><th width="14%">Source repo</th><th width="18%">Install</th></tr></thead>
  <tbody>
    <tr><td width="14%">Mantis Pipeline</td><td width="42%">Orchestrates a scoped vulnerability-discovery engagement from reconnaissance through detection, reachability, validation, and reporting. It ties findings to their evidence and tools, and allows active testing only within explicit authorization.</td><td width="12%"><a href="https://github.com/deonmenezes">@deonmenezes</a></td><td width="14%"><a href="https://github.com/deonmenezes/mantishack">mantishack</a></td><td width="18%"><code>npx skills add deonmenezes/mantishack --skill mantis-pipeline</code></td></tr>
    <tr><td width="14%">Security Review</td><td width="42%">Helps spot application security issues in authentication, user input, secrets, API routes, payments, and other sensitive features. It supports safer implementation and release review.</td><td width="12%"><a href="https://github.com/affaan-m">@affaan-m</a></td><td width="14%"><a href="https://github.com/affaan-m/ECC">ECC</a></td><td width="18%"><code>npx skills add affaan-m/ECC --skill security-review</code></td></tr>
    <tr><td width="14%">Securitymaxxing</td><td width="42%">Sets an application-security baseline from planning through implementation, review, testing, and release preparation. It routes architecture-specific checks and security specialists without authorizing scans or release.</td><td width="12%"><a href="https://github.com/engbyume">@engbyume</a> (Jeremy)</td><td width="14%"><a href="https://github.com/engbyume/securitymaxxing">securitymaxxing</a></td><td width="18%"><code>npx skills add engbyume/securitymaxxing --skill securitymaxxing</code></td></tr>
  </tbody>
</table>


