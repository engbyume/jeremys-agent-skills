# Jeremy's Agent Skills

A source-linked catalog of portable skills for AI agents. It includes upstream skills and Jeremy-authored skills with dedicated public source paths.

The `Origin` column marks Jeremy-authored entries. Full skill files remain in their linked repositories; this repository keeps the category lists, descriptions, provenance, and direct install commands together.

## Skills by category

### Memory and knowledge

Skills for preserving context, retrieving past decisions, and organizing linked notes.

- [Glean](https://github.com/robabby/claude-skills)
- [Graphify](https://github.com/Graphify-Labs/graphify)
- [Hydrate](https://github.com/robabby/claude-skills)
- [Pickup](https://github.com/robabby/claude-skills)
- [Recall](https://github.com/robabby/claude-skills)
- [Reflect](https://github.com/robabby/claude-skills)
- [Remember](https://github.com/robabby/claude-skills)
- [Vault Status](https://github.com/robabby/claude-skills)
- [YAML Wiki Framework](https://github.com/robabby/claude-skills)

### Agent efficiency

Workflows for managing context, coordination, model routing, and agent process.

- [Background Skill Fixer](https://github.com/engbyume/background-skill-fixer) **(Jeremy-authored)**
- [Codex Harness Free Model Router](https://github.com/engbyume/codex-harness-free-model-router) **(Jeremy-authored)**
- [Codex Recursive Self-Improvement](https://github.com/engbyume/codex-recursive-self-improvement) **(Jeremy-authored)**
- [Lean Context](https://github.com/yvgude/lean-ctx)
- [Programmatic Tool Calling](https://github.com/engbyume/codex-recursive-self-improvement) **(Jeremy-authored)**
- [Progressive Codex Model Router](https://github.com/engbyume/progressive-codex-model-router) **(Jeremy-authored)**
- [Session Skill Audit](https://github.com/aiwithremy/session-skill-audit)
- [Sol Advisor](https://github.com/DannyMac180/sol-advisor)
- [Using Superpowers](https://github.com/obra/superpowers)

### Planning and quality

Skills for clarifying requirements, structuring development, and verifying a result.

- [Brainstorming](https://github.com/obra/superpowers)
- [Coding Standards](https://github.com/robabby/claude-skills)
- [Evaluation Harness](https://github.com/robabby/claude-skills)
- [Link Check](https://github.com/robabby/claude-skills)
- [Skill Creator](https://github.com/anthropics/skills)
- [TDD Workflow](https://github.com/robabby/claude-skills)
- [Verification Loop](https://github.com/robabby/claude-skills)
- [Web App Testing](https://github.com/anthropics/skills)

### Research and investigation

Tools for gathering web evidence, operating browsers, and studying user needs.

- [Agent Browser](https://github.com/vercel-labs/agent-browser)
- [Browser Use](https://github.com/browser-use/browser-use)
- [User Research](https://github.com/cookiy-ai/user-research-skill)

### Writing and communication

Guidance for clear, audience-aware writing and collaborative documents.

- [Document Co-authoring](https://github.com/anthropics/skills)
- [Internal Communications](https://github.com/anthropics/skills)
- [Sepia](https://github.com/Nanako0129/sepia)

### Creative and visual work

Skills for visual design, brand systems, and creative image work.

- [Algorithmic Art](https://github.com/anthropics/skills)
- [Brand Guidelines](https://github.com/anthropics/skills)
- [Canvas Design](https://github.com/anthropics/skills)
- [Designmaxxing](https://github.com/engbyume/designmaxxing) **(Jeremy-authored)**
- [Frontend Design](https://github.com/anthropics/skills)
- [Slack GIF Creator](https://github.com/anthropics/skills)
- [Theme Factory](https://github.com/anthropics/skills)
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

### Documents and data

Workflows for reading, editing, and validating common office formats.

- [PDF](https://github.com/anthropics/skills)
- [PowerPoint](https://github.com/anthropics/skills)
- [Spreadsheet Workflows](https://github.com/anthropics/skills)
- [Word Documents](https://github.com/anthropics/skills)

### Developer workflows

Technical guidance for APIs, backends, frontends, MCP, and source inspection.

- [Backend Patterns](https://github.com/robabby/claude-skills)
- [Claude API](https://github.com/anthropics/skills)
- [Frontend Patterns](https://github.com/robabby/claude-skills)
- [MCP Builder](https://github.com/anthropics/skills)
- [Open Source Inspector](https://github.com/vercel-labs/opensrc)
- [Postgres Patterns](https://github.com/robabby/claude-skills)
- [Web Artifacts Builder](https://github.com/anthropics/skills)

### Media analysis

Tools for reviewing video, transcripts, and time-linked visual evidence.

- [Watch](https://github.com/bradautomates/claude-video)

### Security

Defensive guidance for application security and authorized assessment.

- [Mantishack](https://github.com/deonmenezes/mantishack)
- [Security Review](https://github.com/robabby/claude-skills)
- [Securitymaxxing](https://github.com/engbyume/securitymaxxing) **(Jeremy-authored)**

## Files

- [`skills.md`](skills.md): catalog of skill names, categories, descriptions, sources, and terminal commands.
- [`SOURCES.md`](SOURCES.md): source repository and provenance notes.
- [`frameworks/yaml-wiki-framework.md`](frameworks/yaml-wiki-framework.md): user and agent guide with a copyable prompt.
- [`frameworks/yaml-wiki-framework.yaml`](frameworks/yaml-wiki-framework.yaml): machine-readable framework contract.

### YAML Wiki Framework

The catalog includes a descriptive YAML Wiki Framework based on the public `robabby/claude-skills` memory system. It covers Markdown notes, YAML frontmatter, typed memory, wiki-links, hydration, recall, reflection, handoffs, and link checks. Its two research-paper references are labeled as conceptual inspirations only, not as explicit upstream citations.

## Updating the catalog

Before adding an entry, verify its source repository, skill name, category, description, and terminal command. Keep source code and full third-party skill instructions in their original repositories.

## Attribution

Each entry is marked as Jeremy-authored or upstream. Source links identify the repository that provides the skill or reference material.
