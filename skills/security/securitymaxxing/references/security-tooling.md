# Project Security Tooling

Apply this reference to every new or materially changed software project. The tools are mandatory at the checkpoints below when their applicability conditions match. They supplement, and do not change, the 70 core and 23 conditional Securitymaxxing checks.

## Contents

- [Project checkpoints](#project-checkpoints)
- [Cloudflare security-audit skill](#cloudflare-security-audit-skill)
- [Repository scanning with Trivy and TruffleHog](#repository-scanning-with-trivy-and-trufflehog)
- [Dynamic web testing with Strix](#dynamic-web-testing-with-strix)
- [File scanning with ClamAV](#file-scanning-with-clamav)
- [AI testing with PyRIT](#ai-testing-with-pyrit)
- [Reverse-engineering protection with BLA](#reverse-engineering-protection-with-bla)
- [Results and limits](#results-and-limits)
- [Official sources](#official-sources)

## Mandatory use and exceptions

- Run the Cloudflare audit workflow, Trivy, and TruffleHog at project setup and after implementation for every software project with source or configuration. Run them again after relevant dependency, build, authentication, API, or security-sensitive changes.
- Use Strix as the required default dynamic assessment for a runnable, in-scope website, web app, or API on local or staging. Run it after the first stable build, after fixes, and before release.
- Use ClamAV when the product accepts untrusted files. Use PyRIT when it includes generative-AI features.
- Mark a tool not applicable only when the product architecture has no matching target. A missing tool, incomplete scan, failed run, unavailable sandbox, or unmet authorization or paid-use gate means the phase is incomplete, not not-applicable. Continue other safe checks.
- Do not add these scanners to the shipped application or deploy the audit skill as a production service. Run them as development and release controls.

## Project checkpoints

- At project setup, once the repository contains source or configuration, record its revision, deployment shape, applicable tools, tool availability, scope, and any authorization or cost gates. Run the initial applicable scans before implementation proceeds far.
- After implementation and before release, rerun the required scans. Rerun the relevant scanner after dependency, build, authentication, API, file-ingestion, or AI-system changes.
- For an empty scaffold or a project with no supported scan target, record the exact reason and rerun when source or artifacts exist.
- Keep scan outputs in restricted project or CI storage. Redact secrets and personal data before sharing reports. Never claim a tool ran when it did not.
- If a required baseline tool is unavailable, its scan fails, or an authorization or budget gate remains, mark that phase incomplete. Continue other safe checks and do not claim the project security baseline is complete.

## Cloudflare security-audit skill

- Use Cloudflare's multi-phase security-audit skill at project setup for reconnaissance and a coverage plan, then after implementation for the full audit and verified report before release. Jeremy's standing instruction makes these project audits mandatory.
- Read the source from [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill). Use it only when its exact package is active in this runtime and has passed the complete required source and Skillspector review. A catalog link is not an active skill.
- Keep the audit within a project the user owns or is authorized to review. Follow the skill's source-first boundary and OS-enforced sandbox rules. Use synthetic records, no external network for target-controlled code, and no production identity or data.
- If the skill is not installed, its scan is incomplete, or the runtime cannot enforce its required sandbox, leave it inactive and mark the Cloudflare audit phase incomplete. Continue the other checks. Do not copy its instructions into the project or claim that its audit ran.

## Repository scanning with Trivy and TruffleHog

Run both tools on every software repository at setup and before release. Their scopes differ; neither replaces source review.

- **Trivy:** Scan the local filesystem for vulnerabilities, misconfiguration, secrets, and licenses. Enable all relevant scanners explicitly because filesystem misconfiguration and license checks are not enabled by default. At project setup, run `trivy fs --scanners vuln,misconfig,secret,license .`. Before release, run `trivy fs --scanners vuln,misconfig,secret,license --license-full .` to check loose source, font, media, and license files; this pass can take longer. Also scan IaC with `trivy config` and each built container image when those artifacts exist. Use a current database and record its freshness. Keep repository content local; update the scanner database only through an approved source.
- **TruffleHog:** Scan the current filesystem and local Git history at setup and before release. From the repository root, run `trufflehog filesystem . --no-verification --json` and `trufflehog git file://. --no-verification --json`. No-verification is the default so a match does not trigger credential checks against external services. Extend scans to organization repositories, cloud stores, chats, wikis, or other sources only when the current task authorizes that exact account and scope.
- Treat scanner output as sensitive. Do not print raw secret values in chat, logs, pull requests, or artifacts. Report the detector, source path, and line or commit with values redacted. Rotate confirmed exposed credentials through the separately authorized owner process; a scan does not itself revoke them.

## Dynamic web testing with Strix

- For a runnable, user-owned website, web app, or API, use Strix as the required default dynamic assessment after a first stable local or staging build and again before release. Recheck after fixing confirmed findings.
- Confirm the exact target and test scope. Prefer local or staging. Never test a public production or third-party target without explicit current-task authorization.
- Strix requires a running Docker environment and an LLM provider. Do not install software, create accounts, enter credentials, or spend paid model quota until the applicable gate is satisfied. Keep keys out of source, shell history, and scan artifacts.
- If the target, sandbox, Docker runtime, provider authorization, or budget is unavailable, mark the dynamic assessment incomplete and continue static review. A clean scan does not prove the product is secure.

## File scanning with ClamAV

- Require malware scanning when the product receives email attachments, user uploads, or other untrusted files before it parses, serves, or forwards those files.
- Use a current signature database, size and time limits, and an isolated quarantine path. Treat encrypted, oversized, or unscannable files as unverified. Quarantine for review instead of deleting automatically; ClamAV documents false positives and warns against automatic removal.
- Keep clamd on a local or private socket. Do not expose its unauthenticated TCP socket to the Internet. Do not submit user files to ClamAV's sample-review forms unless the user explicitly approves that external disclosure.
- If the product has no file or attachment intake, mark ClamAV not applicable with that architecture-specific reason.

## AI testing with PyRIT

- For products that include generative-AI features, use PyRIT for a structured security and safety evaluation during development and after material changes to models, prompts, tools, data retrieval, or permissions. Run a final relevant assessment before release.
- Use an owned local or staging target and synthetic test data. Keep model, provider, and test scope explicit. Do not send real user data or incur paid provider usage without authorization.
- If there is no generative-AI feature, record PyRIT as not applicable. Automated attack results need source review and human evaluation; do not treat a passing run as a security guarantee.

## Reverse-engineering protection with BLA

- BLA is not a mandatory security tool and is not required for open-source projects. Public source remains available for review, so obfuscating release artifacts cannot hide that source or prevent reverse engineering.
- Consider BLA only for a proprietary, compiled or packaged release artifact when the owner explicitly wants added resistance to AI reverse-engineering tools. Treat its decoys and resource-exhaustion mechanisms as defense in depth, not as confidentiality or a security boundary. Its benchmark claims apply to the listed test targets; an analyzer may raise some resource limits.
- Never apply it to an open-source source tree, audit copy, or artifact that must remain easy to inspect. Its benchmark does not establish protection from human analysts or every reverse-engineering tool. Preserve the original build, review each transformation, run the project's own functional and security tests on the hardened output, and keep a tested restore path. Do not ship if outputs differ or if the protection harms reliability, accessibility, maintenance, or compatibility.

## Results and limits

- Record tool name and version, target, scope, command or profile, database freshness where relevant, findings, dispositions, and explicit not-applicable reasons.
- Use the existing project result format. Do not make a new report directory solely for this tool reference unless the project workflow needs it.
- Scanner findings require source-level validation. Resolve false positives without suppressing unrelated findings. A missing tool, incomplete scan, unknown target, or unresolved high-risk result remains visible as incomplete.
- TruffleHog is AGPL-3.0 and ClamAV is GPL-2.0. Keep them as separate scanning tools unless the exact license and distribution model have been reviewed before bundling or linking them into a product. A license label is not a legal conclusion about the whole application.

## Official sources

- [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill)
- [Trivy filesystem scanning](https://trivy.dev/docs/latest/target/filesystem/) and [license scanning](https://trivy.dev/docs/latest/guide/scanner/license/)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [Strix](https://github.com/usestrix/strix)
- [ClamAV scanning guide](https://docs.clamav.net/manual/Usage/Scanning.html)
- [Microsoft PyRIT](https://github.com/microsoft/PyRIT)
- [BLA](https://github.com/qybaihe/bla)
