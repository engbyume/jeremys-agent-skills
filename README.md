# Universal Agent Skills

Portable, public-safe skill packages for agents that design, build, secure, and maintain software.

**11 installable packages** · **78 catalog records** · **10 categories**

[Browse the packages](#first-party-packages) · [Full catalog](skills.json) · [Sources and provenance](SOURCES.md)

## Install

Install selected packages with the [Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md):

```sh
npx skills@latest add engbyume/universal-agent-skills
```

The CLI prompts you to choose packages and target agents. Use `--list` to preview available packages, repeat `--skill <name>` to select a specific set, and add `-g` for user-level installation.

The CLI documents anonymous usage telemetry, including repository and skill identifiers, plus the `DISABLE_TELEMETRY=1` and `DO_NOT_TRACK=1` opt-outs. See its [telemetry notes](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

## Why this library exists

Good agent work depends on small, repeatable decisions: which guidance applies, what evidence to collect, and where to stop for permission. These packages make those decisions easier to reuse across projects and agent runtimes.

The repository keeps installable first-party skills separate from the wider source catalog. Upstream skills remain linked to their authors. Their instructions are not copied here.

## Common starting points

| Example request | Start here |
| --- | --- |
| “The mobile bottom bar covers the home indicator.” | [Mobile Native](skills/mobile-native/SKILL.md) |
| “Help shape a distinctive product UI and its data-collection flow.” | [Designmaxxing](skills/designmaxxing/SKILL.md) |
| “Review this software change against the security baseline.” | [Securitymaxxing](skills/securitymaxxing/SKILL.md) |
| “Check a skill source and scan it before activation.” | [Universal Skill Audit](skills/universal-skill-audit/SKILL.md) |
| “Prepare a release candidate with health checks and rollback planning.” | [Agent-Managed CI/CD](skills/agent-managed-cicd/SKILL.md)

## First-party packages

Ordered by common project workflow.

### Product and engineering

- [Designmaxxing](skills/designmaxxing/SKILL.md): product-specific UI, accessibility, design research, and a mandatory personal-data baseline.
- [Mobile Native](skills/mobile-native/SKILL.md): phone-specific behavior for websites, web apps, and PWAs, with real-device checks.
- [Platform Architecture](skills/platform-architecture/SKILL.md): backend, data consistency, realtime, delivery, observability, and recovery choices.
- [Securitymaxxing](skills/securitymaxxing/SKILL.md): the first-pass application-security baseline for software changes, with a researched attack catalog for apps, websites, APIs, and games.

### Skill trust and recovery

- [Universal Skill Audit](skills/universal-skill-audit/SKILL.md): source provenance, complete security scans, and source-level review before skill activation.
- [Skill Inspector](skills/skill-inspector/SKILL.md): focused static scanning and evidence-based review of skill packages.
- [Background Skill Fixer](skills/background-skill-fixer/SKILL.md): bounded root-cause repair when a skill fails and an authorized fallback begins.

### Workflow and continuity

- [Agent-Managed CI/CD](skills/agent-managed-cicd/SKILL.md): release candidates, health checks, rollback planning, and explicit release gates.
- [Codex Email Approval Gateway](skills/codex-email-approval-gateway/SKILL.md): task-scoped approval relays and threshold alerts without a scheduled poller.
- [Task Observer](skills/task-observer/SKILL.md): prompt-start, mid-task, and end checks for task scope, evidence, and skill autonomy.
- [GBrain Memory](skills/gbrain-memory/SKILL.md): bounded local-first recall with automatic capture and provider calls off.

## Full catalog and provenance

The [78-entry catalog](skills.json) records short descriptions, categories, and source metadata. [SOURCES.md](SOURCES.md) explains which upstream repositories are included and why. Only the packages under [`skills/`](skills/) are installable from this repository. Other entries point to upstream projects or contain an approved redacted summary.

## Public-safety rules

- Upstream skill instructions stay in their original repositories.
- First-party packages require explicit owner approval and a public-safety review.
- Do not add private prompts, personal data, credentials, environment files, or machine-specific paths.
- Static scans and source review reduce risk. They do not guarantee security or legal compliance.

## Frameworks

- [YAML Wiki Framework](frameworks/yaml-wiki-framework.md): a descriptive guide to structured Markdown memory.
- [Machine-readable YAML Wiki contract](frameworks/yaml-wiki-framework.yaml).
- [Skill autonomy compatibility](frameworks/skill-autonomy-compatibility.md): routine authorized work and genuine action boundaries.

## Attribution

Skill names, descriptions, and upstream links belong to their respective authors. This catalog is an organizational index and is not affiliated with upstream projects.
