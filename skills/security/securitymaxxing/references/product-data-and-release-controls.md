# Product data and release controls

Apply these product standards to every matching software task, including UI-only changes. They supplement the 70 core checks and 23 conditional checks. They do not change those counts. Legal duties vary by market, product, user age, data, and business model.

## Contents

- [Data map and privacy policy](#data-map-and-privacy-policy)
- [Minimize collection](#minimize-collection)
- [Authorization and deletion](#authorization-and-deletion)
- [Ads, tracking, and children](#ads-tracking-and-children)
- [Subscription cancellation](#subscription-cancellation)
- [API keys and AI budgets](#api-keys-and-ai-budgets)
- [Trademark and domain checks](#trademark-and-domain-checks)
- [Third-party license review](#third-party-license-review)
- [Release evidence](#release-evidence)

## Data map and privacy policy

- Build a field-to-destination map from the actual code and authorized configuration. Inspect forms, schemas, migrations, API requests and responses, cookies, local and server storage, logs, crash reporting, SDKs, AI prompts, uploads, webhooks, integrations, backups, and support access.
- Treat data as collected if a user enters it, it reaches the product or a vendor, or it is transiently processed, even when the product does not persist it.
- Use source, configuration, and synthetic records. Do not inspect live customer records unless the current task explicitly authorizes that access.
- Draft and update the privacy policy from this verified map. Name every third party that receives or can access personal data, not only subprocessors. For each one, state its verified purpose, data categories, role, and processing region. Include relevant hosting, identity, payment, AI, email, analytics, support, logging, storage, and backup providers.
- Do not invent a collection purpose, vendor, region, retention period, or legal basis. If a data flow or recipient is unknown, block the affected collection or release until it is verified. Recheck the policy after code, SDK, provider, or data-flow changes.

## Minimize collection

- Collect only data needed for a clear, documented product purpose. Remove fields, permissions, upload paths, SDKs, and integrations without that purpose.
- Do not collect identity-document photos, selfies, precise location, or other sensitive data by default. Add them only for a specific, authorized product requirement after privacy, security, and legal review.
- A field that is neither stored nor needed may still expose data through requests, logs, analytics, or a vendor. Remove the capture and transmission path when it has no purpose.

## Authorization and deletion

- Enforce least-privilege authorization at a trusted server or service boundary for every read, search, change, export, stream, admin action, background task, and deletion. Deny by default. Do not rely on hidden controls, client roles, or hard-to-guess IDs.
- Verify cross-user and cross-tenant denials with synthetic accounts and direct requests. Do not use real customer records for routine authorization tests.
- If a product stores personal data, provide a clear Delete my data or Delete account action in an appropriate account or settings surface. For a product without accounts, provide a clear route to delete the data tied to the user or device.
- Wire the action to a real backend workflow. Verify deletion from primary databases, object storage, replicas, caches, search and vector indexes, exports, derived records, and processors that received the data. Invalidate sessions and revoke access where needed.
- Show success only after the workflow confirms completion. For asynchronous deletion, show an accurate status. Document backup expiry and narrow legal-retention exceptions; isolate retained records and delete them when the hold ends.

## Ads, tracking, and children

- Product default: no ads and no tracking. Do not add ad placements, ad networks, Meta Pixel, Google Analytics, attribution SDKs, session replay, fingerprinting, or cross-site tracking without a new explicit product decision.
- Do not initialize an approved analytics or measurement tool before the required affirmative opt-in. Keep Accept and Reject equally prominent and easy. Never preselect consent. Make withdrawal as easy as opt-in, and load only the approved purpose after consent.
- If children under 13 can use a website or service, treat them as children under this product baseline. Check each market's current age threshold and legal trigger. Before collecting their personal data, obtain verified parental consent where required and provide the applicable parent review and deletion path. An age entry or age gate is not parental consent.
- Do not use ads or tracking for children. If age, market, or parental-consent status is unknown, block the affected data collection and tracking. Avoid collecting a birth date when a less intrusive age check is sufficient.

## Subscription cancellation

- If recurring subscriptions exist, provide one clear cancellation action from the account or the same channel used to subscribe. Do not require a call, retention conversation, repeated offers, or a cancellation maze.
- On the action, stop renewal and prevent the next charge as soon as the billing provider accepts cancellation. Show a clear confirmation and any paid-through access end date. Do not promise a refund or access cutoff that the provider has not confirmed.
- Verify cancellation and future billing state with the provider's test or sandbox flow before release. Check current laws and platform rules for each market; this product standard is not a claim about current legal requirements.

## API keys and AI budgets

- Private API keys must never enter browser code or other client-delivered configuration. Search source, build environment injection, bundles, source maps, URLs, logs, and repository history. Keep private keys in a server-side secret store. Allow only provider-designated publishable client keys with appropriate restrictions.
- If a private key was exposed to a client, revoke and rotate it. Removing the string alone does not make the old key safe.
- For every AI provider, configure a provider-side spend cap when available and an application-side hard stop for the approved budget period. Add per-user or per-project request, token, and concurrency limits where they control cost.
- Alerts do not replace a hard cap. If the provider cannot enforce a cap, the application must stop paid calls at its own limit. If neither can be verified, keep paid calls disabled.

## Trademark and domain checks

- Before purchasing a domain or launching a product, company, or feature name, search the exact name and confusingly similar marks in official registers for the target markets and related goods or services.
- Search spelling, sound, meaning, and design variants. Check the USPTO for U.S. use and registration, WIPO's Global Brand Database, and EUIPO/TMview or the relevant national IP offices for target markets. Also check state or regional registers and common-law web use where relevant.
- Record the search date, markets, goods or services, queries, and material results. Domain availability is separate from trademark clearance.
- A database search cannot guarantee legal clearance. Pause use or purchase when a material conflict or uncertainty appears and seek qualified trademark counsel. Do not claim that a search prevents a lawsuit.

## Third-party license review

- Before shipping copied or imported code, libraries, fonts, images, icons, music, video, models, or other assets, record the exact source, version, license or terms, attribution, and intended use.
- Check commercial use, modification, redistribution, notice, source-offer, patent, and copyleft obligations for the actual integration and distribution. Review direct and transitive software dependencies.
- Do not assume every copyleft license requires the entire application to become open source. Review the exact license and how the material is combined and distributed.
- If rights are unclear or a license conflicts with the product's intended commercial or closed-source use, do not ship that material until an approved alternative or qualified legal review resolves the issue.

## Release evidence

- Keep concise evidence for the source map, third-party list, consent behavior, deletion result, authorization tests, cancellation state, AI caps, name search, and license review that apply to the product.
- Treat a control as incomplete until its real behavior is verified. Keep unresolved collection, paid use, branding, and release gates closed. These checks reduce risk; they do not guarantee legal compliance or prevent every incident.

## Official source starting points

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [FTC COPPA FAQs](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)
- [FTC Negative Option Rule](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule)
- [USPTO comprehensive trademark clearance search](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks)
- [WIPO Global Brand Database](https://www.wipo.int/en/web/global-brand-database/index)
- [EUIPO trademark availability](https://www.euipo.europa.eu/en/trade-marks/before-applying/availability)
- [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)
