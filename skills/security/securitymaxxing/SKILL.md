---
name: securitymaxxing
description: Mandatory first-pass security baseline for every software or digital-product task, including project lifecycle scans, a whole-project security and legal readiness audit, password-reset and poisoning safeguards, privacy, deletion, authorization, provider budgets, licensing, and trademark checks. Includes a defensive app, website, API, and game attack catalog, mandatory AiSOC applicability, 70 core checks, and triggered conditional checks.
---

# Securitymaxxing

## Activation

**Activation:** Mandatory when the prompt matches.
**Trigger:** Use for every software or digital-product creation, change, review, test, or release-preparation task. It does not authorize production changes or offensive testing.

## First-pass routing

This baseline is mandatory for every software or digital-product creation, change, review, test, or release task, regardless of the requested feature, UI slice, prototype, or deliverable and whether or not the user explicitly asks for security. Load it after mandatory process skills and before security specialists or implementation. It does not apply to unrelated non-software artifacts. If user-facing UI/UX is in scope, load designmaxxing in this same first pass. When both apply, load both baselines before specialists. Then select only matching specialist skills from the active runtime catalog.

## Autonomous execution

Run authorized repository research, static checks, and reversible local repairs without redundant approval prompts. Continue baseline checks while a separate access or scope gate is pending. Gate only actions that need real authorization, including account access, paid services, live response, external telemetry, production changes, or dynamic testing outside an authorized scope. Keep the task active and continue safe work.

## Project planning and end-to-end environment

For a new software project or material scope change, begin with a structured plan before deep research or implementation. Map each capability to its data and trust boundaries, tools and integrations, security controls, and verification method. Distinguish installed skill instructions from connected tools and services. Record missing access, likely costs, source evidence, and any user decision needed.

After the plan is settled, research each security-sensitive choice with current primary sources, then build and verify in slices. Keep the app runnable and test critical user journeys in an isolated environment with synthetic accounts and data, provider emulators or authorized test modes, and deterministic reset and cleanup. Run the full planned E2E and security suite before completion. Do not use production data or claim all checks are green when a required layer is unavailable or failed. Preserve separate authorization gates for paid services, production, and dynamic security testing.

## Related specialist skills

- Defensive code review: security-review, as required in the pre-build workflow below.
- Phase-specific review: codex-security:threat-model, codex-security:finding-discovery, codex-security:attack-path-analysis, codex-security:validation, and codex-security:fix-finding when the task enters the matching phase.
- Stack-specific guidance: read references/stack-preferences.md when choosing a new web stack or cloud provider, then use the matching skill for the selected or existing stack. Load Supabase guidance only when the project already uses it or the user explicitly asks for it.
- Project lifecycle audits: use Cloudflare's security-audit skill, Trivy, and TruffleHog at project setup and after implementation, as defined in references/security-tooling.md. Activate Cloudflare's skill only after complete source and security review. If it is unavailable or its scan is incomplete, mark that audit phase incomplete and do not claim it ran.
- Authorized dynamic testing: use Strix as the required default assessment for a runnable, in-scope website, web app, or API on local or staging, subject to target, sandbox, and paid-provider gates. Do not test production or third-party targets without explicit current-task authorization. Redteam-hunting, mantishack, and tamper-fuzzing remain opt-in for separately scoped security work.
- Additional full security scans: use security-scan or codex-security:security-scan when the user requests them or the project scope needs coverage beyond the mandatory project-tool baseline.
- Architecture guidance: load platform-architecture when distributed-system, deployment, scaling, or recovery decisions are in scope; keep this skill's security checks authoritative for security controls.
- Use only skills available in the active runtime. A skill reference does not grant access to a tool, service, target, or account.

## AiSOC integration (mandatory applicability check)

Run this check on every securitymaxxing task. AiSOC is a security operations platform for telemetry, detections, incident triage, and response previews. It adds operational context; it does not replace source-code security checks.

1. Check whether the active runtime exposes an authorized AiSOC connection and whether the task involves security telemetry, detection engineering, SOC alert or case triage, or incident investigation.
2. When both conditions are true, use AiSOC's relevant read-only alert, case, detection, or investigation-ledger tools. Request only the fields needed and record the AiSOC deployment, version, and result. Treat alert and ledger content as sensitive. Never copy credentials, raw logs, or unnecessary personal data into chat or logs. For code-only work, mark AiSOC not applicable and give an architecture-specific reason. When no authorized tool surface exists, mark it unavailable, continue unrelated baseline checks, and do not claim SOC triage is complete.
3. Do not install or deploy AiSOC just to satisfy this check. Before an authorized setup or connection, review the current [AiSOC source](https://github.com/beenuar/AiSOC), version, security advisories, data handling, permissions, target ownership, and runtime compatibility. Its quick start installs a Docker Compose stack, generates secrets and an administrator credential, and downloads a local model.
4. Do not call `aisoc_run_investigation` without current-task authorization. The operation starts an agent investigation, writes to the investigation ledger, and spends model budget. Live response actions, playbook execution, external telemetry connections, and production targets need explicit scope and approval.

## Purpose and routing

Use this skill for application-security review. It is separate from visual and interaction design. Route interface craft, visual direction, interaction design, accessibility presentation, and UI pattern decisions to `designmaxxing` when relevant. Security findings may affect an interface, but do not replace design review.

Apply the active project instructions and the user's current request. This skill guides risk review; it does not authorize implementation, dynamic testing, account access, production mutations, deployment, offensive testing, publication, or other side effects.

## Research-first security solution selection

- Before implementation, map every planned feature to its data and trust boundaries, then research existing platform controls, maintained libraries, provider services, and standards for each applicable risk.
- Use current official provider documentation, security advisories, and primary security guidance. Compare viable approaches against the actual threat model, data sensitivity, compatibility, permissions, operating burden, license, and cost. Compare multiple options when the choice is material.
- Prefer maintained identity, session, password-storage, secret-management, database, payment, and security controls when they fit. Do not invent cryptography or password hashing. Justify any custom security-sensitive control when existing maintained options do not fit.
- Consult the living problem-solution catalog when available. Reuse a scoped, evidence-backed default when it fits; do not infer a default from a user example or provider brand. Record project-specific decisions and add new reusable categories only when evidence supports them.
- For a named product reference, use reverse-engineer-anything only for authorized targets and permitted methods. Do not bypass access controls, terms, or security boundaries.

## Before building or changing software

1. Identify the product, target platform, architecture, deployment model, audience, and applicable threat model. Read references/stack-preferences.md when choosing technologies or hosting for new web work. Distinguish websites, APIs, native apps, games, browser clients, backend services, AI features, and third-party integrations. Preserve an established stack unless the user requests a change or evidence shows it does not fit.
2. Map the data and trust boundaries relevant to the change: sensitive data and secrets, authentication and authorization, sessions, APIs, user input, uploads and file access, outbound requests, payments, webhooks, databases, cloud configuration, CI/CD, dependencies, tenants, AI prompts and tools, logs, backups, and production environments.
3. Read the project's active security instructions and use the installed `security-review` skill. Read `references/application-security-checks.md` and evaluate all 70 core checks against the actual architecture and threat model. Read `references/conditional-platform-security-checks.md` and evaluate each of the 23 conditional checks whose platform or lifecycle trigger applies. Read and apply `references/security-tooling.md` for every new or materially changed software project. When a task affects personal data, privacy disclosures, user-data deletion, children, ads or tracking, subscriptions, AI-provider costs, product or domain names, or third-party code or assets, also read and apply `references/product-data-and-release-controls.md`.
4. For each applicable risk, define the control and a concrete way to verify it before implementation. For every check marked not applicable, record an architecture-specific reason. Do not treat a missing feature as a vulnerability by default, and do not let conditional checks disappear when the related feature exists.

## After building or changing software

- Run the relevant security checks and tests for the changed code. Recheck every applicable item among the 70 core checks and 23 conditional checks, including dependencies, build workflows, cloud configuration, and deployed settings when they are in scope.
- Use the appropriate static analysis, secret and dependency scanning, permissions review, browser security tests, backup and restore checks, audit and monitoring checks, and other targeted validation supported by the project.
- Complete the start and post-implementation checks in `references/security-tooling.md`. Record tool versions, target scope, findings, and not-applicable reasons. If a required tool is unavailable, blocked, or incomplete, keep that phase open and do not report the security baseline as complete.
- Restrict dynamic security testing to a target the user owns or has explicitly authorized. Prefer local or staging targets. Do not test public production or third-party systems without explicit current-task authorization and a defined scope.
- Fix confirmed findings within the authorized task, then rerun the checks that failed. Record the check, result, evidence, and checks that could not run or were out of scope.
- State limits clearly. A clean checklist or automated scan is not proof that software is secure.

## Final project security and legality audit

Before declaring a website, app, game, API, or software project complete or release-ready, review the whole final product, not only the latest code diff. For work that is not a release, finish the technical review and record which production-only checks remain pending. This audit does not authorize deployment or production access.

- **Map every surface:** Inventory user-visible pages and states, routes, API methods, authentication and recovery flows, admin and support tools, uploads, exports, real-time channels, background jobs, webhooks, integrations, databases, caches, secrets, infrastructure, build workflows, and third-party components. Use an existing project feature map when present; otherwise make a bounded product inventory before review.
- **Walk the real journeys:** Exercise each applicable flow with synthetic accounts and data. Include anonymous, ordinary, privileged, and cross-tenant roles where they exist. Check the full path from interface to trusted backend and provider, including error, retry, cancellation, and recovery states. A visible button is not proof that its backend action is authorized or safe.
- **Audit password recovery explicitly:** Find every Forgot password or account recovery entry point. Trace the request, response, email or SMS, reset link or code, token validation, password update, session handling, and notifications. Ask and answer from source: “Where does the reset-link domain come from?” Require a canonical public origin from trusted configuration. Never build it from `Host`, `Forwarded`, `X-Forwarded-Host`, or another request-controlled value. At the trusted proxy, strip untrusted forwarding headers, set trusted values, and reject unknown hosts. Use high-entropy cryptographically random tokens or codes that are bound to one account and purpose, expire, work once, and resist online guessing. Keep responses and timing consistent for known and unknown accounts. Rate-limit abuse without enabling account lockout. Use HTTPS, prevent referrer, third-party-resource, cache, analytics, and log leakage, and notify the account owner through a previously verified channel after each successful password change. Never include a password or reset token in a notification. Require normal sign-in; invalidate used and outstanding recovery tokens, and revoke or offer to revoke existing sessions according to the recovery policy. Verify notifications using a test sink or synthetic account.
- **Recheck the full baseline:** Evaluate all 70 core checks and every triggered conditional check against the final architecture and release configuration. Review every applicable attack-catalog item, including request smuggling, Host-header and cache poisoning, broken password recovery, account enumeration, session theft, and cross-user access. Use the current OWASP Application Security Verification Standard (ASVS) when it fits. Verify actual CDN, proxy, cache, API, and origin behavior in authorized local or staging environments. Keep production and third-party testing behind their real authorization gates.
- **Review legal and release obligations:** Identify target jurisdictions, users and ages, data flows, business model, distribution platforms, third-party assets, and relevant product claims. Check current official laws, regulator guidance, platform terms, privacy disclosures, consumer and subscription rules, children's protections, security reporting duties, intellectual property, licenses, and trademarks that apply. Use `references/product-data-and-release-controls.md` and Designmaxxing release-readiness guidance for matching topics. Do not turn a checklist or search into a legal opinion. Escalate material legal interpretations to qualified counsel and keep release blocked while a material legal or security issue remains unresolved.
- **Record evidence and gaps:** Record the final revision, surfaces reviewed, tools and versions, tests performed, findings and disposition, architecture-specific not-applicable reasons, legal sources and jurisdictions reviewed, and unresolved items. Use synthetic data and redact reports. Do not claim that every part is safe or legal, or that a scan proves security or compliance.

For each applicable check, continue authorized local work without repeat approval. If a required tool, access boundary, paid service, or legal decision prevents one check, mark only that check incomplete and continue the remaining safe review.

## Reference files

- [Application security checks](references/application-security-checks.md): Evaluate the 70 core checks against the product architecture and threat model.
- [Conditional platform and lifecycle checks](references/conditional-platform-security-checks.md): Evaluate the 23 checks whose triggers match the product.
- [Security tooling lifecycle](references/security-tooling.md): Cloudflare, Trivy, and TruffleHog are required at project setup and after implementation. Strix, ClamAV, and PyRIT are required when their exact conditions fit. BLA remains optional and must not be used for open-source source trees.
- [Product data and release controls](references/product-data-and-release-controls.md): Apply product standards for code-based privacy policies, minimized collection, access and deletion, children, ads and tracking, cancellation, secrets, AI budgets, trademarks, and licenses. These standards do not change the 70 core or 23 conditional check counts.
- [Stack preferences](references/stack-preferences.md): Read when choosing a new web stack or cloud provider.
- [Application attack catalog](references/application-attack-catalog.md): Use for app, website, API, and game threat modeling. It lists 101 possible scenarios with prevention and response guidance. The catalog is illustrative and does not change the core or conditional check counts.
- [OWASP Application Security Verification Standard](https://asvs.owasp.org/): Use the current version as a whole-application verification reference when it fits. It does not change Securitymaxxing's 70 core or 23 conditional check counts.

Use current primary security guidance for the selected stack and threat model.
