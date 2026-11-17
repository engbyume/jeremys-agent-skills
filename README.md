# Universal Agent Skills

Portable, public-safe skill packages for agents that design, build, secure, and maintain software.

**11 installable packages** · **200 catalog records** · **10 categories**

[Browse by category](#browse-by-category) · [Installable packages](#first-party-packages) · [Full catalog](skills.json) · [Sources and provenance](SOURCES.md)

## Install

Install selected packages with the [Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md):

```sh
npx skills@latest add engbyume/universal-agent-skills
```

The CLI prompts you to choose packages and target agents. Use `--list` to preview available packages, repeat `--skill <name>` to select a specific set, and add `-g` for user-level installation.

The CLI documents anonymous usage telemetry, including repository and skill identifiers, plus the `DISABLE_TELEMETRY=1` and `DO_NOT_TRACK=1` opt-outs. See its [telemetry notes](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

## Why this library exists

Good agent work depends on small, repeatable decisions: which guidance applies, what evidence to collect, and where to stop for permission. These packages make those decisions easier to reuse across projects and agent runtimes.

Every record sits under `skills/<category>/<skill>/`. The 11 installable packages have a `SKILL.md`; catalog-only entries have a `CATALOG.md` card. This release contains 200 selected entries from 535 active skill names in the local inventory. The other 189 entries are catalog-only. They link to pinned upstream sources or describe explicitly approved local skills. Upstream instructions are not copied.

## Common starting points

| Example request | Start here |
| --- | --- |
| “The mobile bottom bar covers the home indicator.” | [Mobile Native](skills/design/mobile-native/SKILL.md) |
| “Help shape a distinctive product UI and its data-collection flow.” | [Designmaxxing](skills/design/designmaxxing/SKILL.md) |
| “Review this software change against the security baseline.” | [Securitymaxxing](skills/security/securitymaxxing/SKILL.md) |
| “Check a skill source and scan it before activation.” | [Universal Skill Audit](skills/security/universal-skill-audit/SKILL.md) |
| “Prepare a release candidate with health checks and rollback planning.” | [Agent-Managed CI/CD](skills/development/agent-managed-cicd/SKILL.md)

## Browse by category

The category folders use short names:

- [Agents](skills/agents/README.md)
- [Design](skills/design/README.md)
- [Development](skills/development/README.md)
- [Documents](skills/documents/README.md)
- [Media](skills/media/README.md)
- [Memory](skills/memory/README.md)
- [Planning](skills/planning/README.md)
- [Research](skills/research/README.md)
- [Security](skills/security/README.md)
- [Writing](skills/writing/README.md)

## Activation defaults

Each record has an `activation` label in `skills.json` and its `CATALOG.md` card.

| Label | Meaning | Current entries |
| --- | --- | ---: |
| **Always mandatory** | Load on every prompt under this library's current defaults. | 6 |
| **Mandatory when the prompt matches** | Load when the task trigger in the skill description matches. | 152 |
| **Optional when the prompt matches** | Use when requested or when agent judgment says it materially helps. | 42 |

<details><summary>Always mandatory (6)</summary>

`autonomous-skill-routing`, `codex-recursive-self-improvement`, `gbrain-memory`, `i-have-adhd`
`programmatic-tool-calling`, `task-observer`

</details>

<details><summary>Mandatory when the prompt matches (152)</summary>

`agent-desktop`, `agent-desktop-macos`, `agent-managed-cicd`, `background-skill-fixer`, `brainstorming`
`build-ios-apps-ios-app-intents`, `build-ios-apps-ios-debugger-agent`
`build-ios-apps-ios-ettrace-performance`, `build-ios-apps-ios-memgraph-leaks`
`build-ios-apps-swiftui-liquid-glass`, `build-ios-apps-swiftui-performance-audit`
`build-ios-apps-swiftui-ui-patterns`, `build-ios-apps-swiftui-view-refactor`
`build-macos-apps-appkit-interop`, `build-macos-apps-build-run-debug`, `build-macos-apps-liquid-glass`
`build-macos-apps-packaging-notarization`, `build-macos-apps-signing-entitlements`
`build-macos-apps-swiftpm-macos`, `build-macos-apps-swiftui-patterns`, `build-macos-apps-telemetry`
`build-macos-apps-test-triage`, `build-macos-apps-view-refactor`, `build-macos-apps-window-management`
`build-web-apps-frontend-app-builder`, `build-web-apps-react-best-practices`
`build-web-apps-shadcn-best-practices`, `build-web-apps-stripe-best-practices`
`build-web-apps-supabase-best-practices`, `canva-canva-branded-presentation`
`canva-canva-resize-for-all-social-media`, `canva-canva-translate-design`, `cloudflare-agents-sdk`
`cloudflare-building-ai-agent-on-cloudflare`, `cloudflare-building-mcp-server-on-cloudflare`
`cloudflare-cloudflare`, `cloudflare-durable-objects`, `cloudflare-sandbox-sdk`, `cloudflare-web-perf`
`cloudflare-workers-best-practices`, `cloudflare-wrangler`, `codex-email-approval-gateway`
`codex-usage-fallback-router`, `composio-cli`, `designmaxxing`, `docx`, `expo-building-native-ui`
`expo-codex-expo-run-actions`, `expo-expo-api-routes`, `expo-expo-cicd-workflows`, `expo-expo-deployment`
`expo-expo-dev-client`, `expo-expo-module`, `expo-expo-tailwind-setup`, `expo-expo-ui-jetpack-compose`
`expo-expo-ui-swift-ui`, `expo-native-data-fetching`, `expo-upgrading-expo`, `expo-use-dom`
`jeremy-agent-mentor`, `jeremy-batch`, `jeremy-eval-loop`, `lean-ctx`, `life-science-research-alphafold-skill`
`life-science-research-bgee-skill`, `life-science-research-bindingdb-skill`
`life-science-research-biobankjapan-phewas-skill`, `life-science-research-biorxiv-skill`
`life-science-research-biostudies-arrayexpress-skill`, `life-science-research-cbioportal-skill`
`life-science-research-cellxgene-skill`, `life-science-research-chebi-skill`
`life-science-research-chembl-skill`, `life-science-research-civic-skill`
`life-science-research-clinicaltrials-skill`, `life-science-research-clinvar-variation-skill`
`life-science-research-efo-ontology-skill`, `life-science-research-encode-skill`
`life-science-research-ensembl-skill`, `life-science-research-epigraphdb-skill`
`life-science-research-eqtl-catalogue-skill`, `life-science-research-eva-skill`
`life-science-research-finngen-phewas-skill`, `life-science-research-genebass-gene-burden-skill`
`life-science-research-gnomad-graphql-skill`, `life-science-research-gtex-eqtl-skill`
`life-science-research-gwas-catalog-skill`, `life-science-research-hmdb-skill`
`life-science-research-human-protein-atlas-skill`, `life-science-research-ipd-skill`
`life-science-research-locus-to-gene-mapper-skill`, `life-science-research-metabolights-skill`
`life-science-research-mgnify-skill`, `life-science-research-ncbi-blast-skill`
`life-science-research-ncbi-clinicaltables-skill`, `life-science-research-ncbi-datasets-skill`
`life-science-research-ncbi-entrez-skill`, `life-science-research-ncbi-pmc-skill`
`life-science-research-opentargets-skill`, `life-science-research-pharmgkb-skill`
`life-science-research-pride-skill`, `life-science-research-proteomexchange-skill`
`life-science-research-pubchem-pug-skill`, `life-science-research-quickgo-skill`
`life-science-research-rcsb-pdb-skill`, `life-science-research-reactome-skill`
`life-science-research-research-router-skill`, `life-science-research-rhea-skill`
`life-science-research-rnacentral-skill`, `life-science-research-string-skill`
`life-science-research-tpmi-phewas-skill`, `life-science-research-ukb-topmed-phewas-skill`
`life-science-research-uniprot-skill`, `mcp-builder`, `mobile-native`, `pdf`, `platform-architecture`
`ponytail`, `pptx`, `security-review`, `securitymaxxing`, `sepia`, `skill-creator`, `skill-inspector`
`sol-advisor`, `universal-skill-audit`, `usage-limit-resume`, `vercel-ai-gateway`, `vercel-ai-sdk`
`vercel-auth`, `vercel-cron-jobs`, `vercel-deployments-cicd`, `vercel-email`, `vercel-env-vars`
`vercel-nextjs`, `vercel-observability`, `vercel-payments`, `vercel-react-best-practices`
`vercel-routing-middleware`, `vercel-runtime-cache`, `vercel-swr`, `vercel-turbopack`, `vercel-turborepo`
`vercel-vercel-api`, `vercel-vercel-cli`, `vercel-vercel-firewall`, `vercel-vercel-functions`
`vercel-vercel-storage`, `vercel-verification`, `vercel-workflow`, `watch`, `xlsx`

</details>

<details><summary>Optional when the prompt matches (42)</summary>

`agent-browser`, `algorithmic-art`, `apify-ultimate-scraper`, `backend-patterns`, `brand-guidelines`
`browser-use`, `canvas-design`, `claude-api`, `codex-harness-free-model-router`, `coding-standards`
`doc-coauthoring`, `eval-harness`, `frontend-design`, `frontend-patterns`, `glean`, `graphify`, `headroom`
`hydrate`, `internal-comms`, `link-check`, `mantishack`, `opensrc`, `pickup`, `postgres-patterns`
`progressive-codex-model-router`, `recall`, `reflect`, `remember`, `rtk`, `shadcn-ui-design-system`
`slack-gif-creator`, `tdd-workflow`, `theme-factory`, `ui-ux-pro-max`, `user-research`, `using-superpowers`
`vault-status`, `verification-loop`, `verify-fitlab`, `web-artifacts-builder`, `webapp-testing`
`yaml-wiki-framework`

</details>

**Current selection default:** Agents use best judgment to select matching skills. These labels do not grant permission or remove access, consent, paid-use, production, security, or destructive-action gates.

### Set your preferences

Which skill IDs should be always mandatory, mandatory when the prompt matches, or optional when the prompt matches? Would you like agents to use best judgment to select matches, or ask you each time? Reply with lists of IDs or edit the `activation` field in `skills.json`.

## First-party packages

Ordered by common project workflow.

### Product and engineering

- [Designmaxxing](skills/design/designmaxxing/SKILL.md): product-specific UI, accessibility, research, contextual motion guidance, and a mandatory personal-data baseline.
- [Mobile Native](skills/design/mobile-native/SKILL.md): phone-specific behavior for websites, web apps, and PWAs, with real-device checks.
- [Platform Architecture](skills/development/platform-architecture/SKILL.md): backend, data consistency, realtime, delivery, observability, and recovery choices.
- [Securitymaxxing](skills/security/securitymaxxing/SKILL.md): the first-pass application-security baseline for software changes, with a researched attack catalog for apps, websites, APIs, and games.

### Skill trust and recovery

- [Universal Skill Audit](skills/security/universal-skill-audit/SKILL.md): source provenance, complete security scans, and source-level review before skill activation.
- [Skill Inspector](skills/security/skill-inspector/SKILL.md): focused static scanning and evidence-based review of skill packages.
- [Background Skill Fixer](skills/agents/background-skill-fixer/SKILL.md): bounded root-cause repair when a skill fails and an authorized fallback begins.

### Workflow and continuity

- [Agent-Managed CI/CD](skills/development/agent-managed-cicd/SKILL.md): release candidates, health checks, rollback planning, and explicit release gates.
- [Codex Email Approval Gateway](skills/agents/codex-email-approval-gateway/SKILL.md): task-scoped approval relays and threshold alerts without a scheduled poller.
- [Task Observer](skills/agents/task-observer/SKILL.md): prompt-start, mid-task, and end checks for task scope, evidence, and skill autonomy.
- [GBrain Memory](skills/memory/gbrain-memory/SKILL.md): bounded local-first recall with automatic capture and provider calls off.

## Full catalog and provenance

The [200-entry catalog](skills.json) records short descriptions, simplified categories, activation labels, and source metadata. Each record has a category folder and `CATALOG.md` card; the 11 installable packages also include `SKILL.md`. Upstream skill bodies stay with their authors. See [SOURCES.md](SOURCES.md) for provenance.

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
