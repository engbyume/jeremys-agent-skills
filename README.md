# Jeremy's Agent Skills

A simple directory of skills for AI agents. Browse by purpose, then use the install command in the catalog to add a skill from its original source.

## Start here

- [Skill catalog](skills.md): descriptions, categories, source links, and install commands.
- [Sources and credits](SOURCES.md): who created the listed skills and where they come from.
- [YAML Wiki Framework guide](frameworks/yaml-wiki-framework.md): a separate reference guide, not an installable skill.

## Skills by category

### Memory and knowledge

Keep useful notes and bring them back when they matter.

- [Glean](https://github.com/robabby/claude-skills): Searches saved notes to find useful patterns and connections.
- [Graphify](https://github.com/Graphify-Labs/graphify): Turns code or notes into a navigable knowledge graph.
- [Hydrate](https://github.com/robabby/claude-skills): Loads selected project notes before work begins.
- [Pickup](https://github.com/robabby/claude-skills): Prepares a handoff for interrupted work.
- [Recall](https://github.com/robabby/claude-skills): Searches saved notes by keywords and meaning.
- [Reflect](https://github.com/robabby/claude-skills): Reviews completed work for useful lessons.
- [Remember](https://github.com/robabby/claude-skills): Saves user-approved facts and decisions for later tasks.
- [Vault Status](https://github.com/robabby/claude-skills): Checks the state of a connected Obsidian vault.

### Agent workflows

Manage context, coordination, and repeatable agent work.

- [Background Skill Fixer](https://github.com/engbyume/background-skill-fixer) (by Jeremy): Finds and repairs a skill failure after bounded retries.
- [Codex Harness Free Model Router](https://github.com/engbyume/codex-harness-free-model-router) (by Jeremy): Guides a locally configured model router for Codex.
- [Codex Recursive Self-Improvement](https://github.com/engbyume/codex-recursive-self-improvement) (by Jeremy): Uses task evidence to find an agent mistake and verify a small improvement.
- [Lean Context](https://github.com/yvgude/lean-ctx): Provides compact tools for file search, reading, shell work, and code graphs.
- [Progressive Codex Model Router](https://github.com/engbyume/progressive-codex-model-router) (by Jeremy): Routes parent and child work to a model suited to the task.
- [Session Skill Audit](https://github.com/aiwithremy/session-skill-audit): Reviews task transcripts at checkpoints and completion to find missed skill routes and root causes.
- [Sol Advisor](https://github.com/DannyMac180/sol-advisor): Routes Codex work by difficulty, tool needs, and agent role.
- [Using Superpowers](https://github.com/obra/superpowers): Offers workflows for planning, coding, debugging, and review.

### Planning and quality

Clarify the work and check the result.

- [Brainstorming](https://github.com/obra/superpowers): Clarifies goals, constraints, and options before creative or product work.
- [Coding Standards](https://github.com/robabby/claude-skills): Provides coding conventions and common patterns for web projects.
- [Evaluation Harness](https://github.com/robabby/claude-skills): Builds repeatable evaluations for model or software behavior.
- [Link Check](https://github.com/robabby/claude-skills): Finds broken or malformed wiki-links in an Obsidian vault.
- [Skill Creator](https://github.com/anthropics/skills): Guides the creation and revision of reusable agent skills.
- [TDD Workflow](https://github.com/robabby/claude-skills): Starts implementation with a failing test, then guides the code change and refactor.
- [Verification Loop](https://github.com/robabby/claude-skills): Runs available project checks before completion.
- [Web App Testing](https://github.com/anthropics/skills): Uses browser automation to exercise a local web app.

### Research and investigation

Find current information and gather evidence.

- [Agent Browser](https://github.com/vercel-labs/agent-browser): Controls a browser through a command-line tool for repeatable navigation.
- [Browser Use](https://github.com/browser-use/browser-use): Provides browser automation through the Browser Use framework.
- [User Research](https://github.com/cookiy-ai/user-research-skill): Plans interviews, surveys, and other research methods, then synthesizes findings.

### Writing and communication

Draft and improve clear writing.

- [Document Co-authoring](https://github.com/anthropics/skills): Guides a step-by-step process to plan, draft, and refine documents with a user.
- [Internal Communications](https://github.com/anthropics/skills): Helps write status reports, leadership updates, and internal messages.
- [Sepia](https://github.com/Nanako0129/sepia): Applies human-writing guidance to draft, review, rewrite, or recreate prose.

### Creative and visual work

Create and refine visual assets and interfaces.

- [Algorithmic Art](https://github.com/anthropics/skills): Creates generative artwork with p5.js and seeded randomness.
- [Brand Guidelines](https://github.com/anthropics/skills): Applies Anthropic's official colors and typography to documents or visuals.
- [Canvas Design](https://github.com/anthropics/skills): Creates standalone visual artwork for PNG and PDF deliverables.
- [Designmaxxing](https://github.com/engbyume/designmaxxing) (by Jeremy): Provides first-pass UI and UX guidance for websites, apps, games, and design systems.
- [Frontend Design](https://github.com/anthropics/skills): Builds production-ready frontend interfaces with a distinct visual direction.
- [Slack GIF Creator](https://github.com/anthropics/skills): Creates animated GIFs for Slack using timing and size constraints.
- [Theme Factory](https://github.com/anthropics/skills): Applies consistent color and type themes to generated artifacts.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): Offers design references for styles, palettes, typography, UX, and charts.

### Documents and data

Work with office files and structured data.

- [PDF](https://github.com/anthropics/skills): Reads and edits PDF files, including text extraction, OCR, merging, and splitting.
- [PowerPoint](https://github.com/anthropics/skills): Creates and edits PowerPoint slides and decks.
- [Spreadsheet Workflows](https://github.com/anthropics/skills): Creates, reads, and analyzes Excel, CSV, and other spreadsheet files.
- [Word Documents](https://github.com/anthropics/skills): Creates, edits, and reviews Word documents, including content and formatting.

### Software development

Design and build software.

- [Backend Patterns](https://github.com/robabby/claude-skills): Covers backend architecture, API design, and database choices.
- [Claude API](https://github.com/anthropics/skills): Guides integration with the Anthropic Claude API and SDKs.
- [Frontend Patterns](https://github.com/robabby/claude-skills): Covers reusable frontend architecture for React and Next.js.
- [MCP Builder](https://github.com/anthropics/skills): Guides the design and implementation of Model Context Protocol servers.
- [Open Source Inspector](https://github.com/vercel-labs/opensrc): Fetches dependency source code for local inspection.
- [Postgres Patterns](https://github.com/robabby/claude-skills): Covers PostgreSQL schema design, query tuning, and database security.
- [Web Artifacts Builder](https://github.com/anthropics/skills): Builds interactive, multi-component HTML deliverables.

### Media analysis

Review video with transcripts and frames.

- [Watch](https://github.com/bradautomates/claude-video): Reviews videos by combining transcripts, frames, and timestamps.

### Security

Review software and run authorized assessments.

- [Mantishack](https://github.com/deonmenezes/mantishack): Runs authorized security assessment workflows against scoped targets.
- [Security Review](https://github.com/robabby/claude-skills): Reviews authentication, input handling, secrets, and common application risks.
- [Securitymaxxing](https://github.com/engbyume/securitymaxxing) (by Jeremy): Provides a first-pass security baseline for software planning, implementation, review, testing, and release readiness.

## Created by Jeremy

Six catalog entries are Jeremy's original work, developed from practical workflows he has refined. Each one links to a separate public source repository in the catalog.

