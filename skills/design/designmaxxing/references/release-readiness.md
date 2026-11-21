# Release readiness: accessibility, trust, and legal surfaces

Use this reference when a website, app, game, or other interface is planned for public release and includes relevant claims, data, forms, purchases, tracking, third-party services, or user content. It is a design risk checklist, not legal advice. It cannot guarantee compliance or prevent a lawsuit. Requirements depend on the product, audience, business model, distribution platform, and each target market. Do not claim that a UI is legally compliant from a design review alone.

Before making a legal or compliance claim, identify the target jurisdictions and audiences. Check current official laws, regulators, accessibility standards, and platform rules. Use qualified counsel for material legal questions. Keep user-facing policies accurate and consistent with actual product behavior. Do not invent business details, policies, consents, reviews, or claims.

## User-supplied checks

Apply each check only when it fits the product and its release context. Some items are legally required only in particular places or business models. A policy page does not correct a misleading flow or unlawful data practice.

| # | Check | Design and review action |
|---|---|---|
| 1 | Check color contrast | Measure text, controls, icons, focus indicators, and important states against their actual backgrounds. Use a current accessibility standard and the conformance target that applies. Do not rely on color alone. |
| 2 | Add text alternatives to images | Give informative images meaningful alternatives. Use an empty alternative for decorative images. Describe the purpose of functional images and provide equivalent information for charts or diagrams. |
| 3 | Refund and cancellation | If the product sells goods, digital content, subscriptions, or services, verify applicable refund, cancellation, and withdrawal rules. For subscriptions, make cancellation one clear action, no harder than signup, and stop renewal before the next charge. Show the confirmed status and paid-through date. Do not suggest a policy can waive statutory rights. |
| 4 | Privacy policy page | Where required or expected by the platform, explain actual collection, purposes, sharing, retention, deletion, choices, and contact route. Derive the policy from inspected code and configuration. Name every third party that receives or can access personal data, not only subprocessors. |
| 5 | Fix accessibility | Review the full experience with keyboard, screen reader, zoom or text resizing, contrast, focus, labels, error recovery, motion settings, and relevant assistive technology. Combine automated checks with manual testing by people using the interface. Do not claim accessibility from a scanner result alone. |
| 6 | Remove fake reviews | Never create, buy, or present fabricated reviews or testimonials as real. Keep real customer feedback tied to real experience. Check disclosure and moderation rules for incentives, employee relationships, endorsements, and review excerpts in each target market. |
| 7 | Terms and conditions | If terms apply, use accurate, readable terms that match the product, account, payment, subscription, user content, and support flows. Confirm required disclosures and enforceability for the target markets. Do not copy a generic template as a substitute for review. |
| 8 | Check third-party embeds | Inventory embedded players, maps, fonts, analytics, ad tags, SDKs, and other external services. Check what data they receive, when they load, their license and terms, and whether a notice, consent, or alternative is required. Do not load tracking before affirmative opt-in. Provide a useful fallback where possible. |
| 9 | Check image and media rights | Confirm ownership or a license for the actual use, audience, platforms, territories, and commercial purpose. Check attribution, derivative-use limits, model or property releases, trademarks, and music or voice rights when relevant. Keep a source record. |
| 10 | Cookies policy | If cookies or similar storage are used, document the actual categories, providers, purposes, and retention. Distinguish essential operation from analytics and advertising. Keep the policy current when vendors or behavior change. |
| 11 | Check tracking | Default to no ads and no tracking. Map analytics, advertising pixels, attribution links, SDKs, and identifiers. If a specific analytics purpose is explicitly approved, keep it disabled until affirmative opt-in and make Reject as easy as Accept. Check current market and platform rules. |
| 12 | Form consent | Explain why each sensitive or optional field is requested. Separate optional marketing consent from necessary processing. Do not preselect optional consent or bundle unrelated purposes. Record and honor choices where required. |
| 13 | Check local laws | Check the actual countries or states served, age groups, product category, monetization, data types, and platform. Verify current requirements using official sources. Escalate legal interpretation to qualified counsel. |
| 14 | Use clear button labels | Name the actual action and its consequence, especially for purchases, subscriptions, deletion, sharing, consent, and irreversible changes. Avoid vague labels such as "Continue" when the user needs to know what happens next. |
| 15 | Check cookie consent | Consent is not the same as a cookie banner or policy page. Determine whether consent is required for each cookie or tracker in each market. When consent is required, make choices clear, accessible, and easy to change. Do not load consent-gated tracking before the required choice. |
| 16 | Add real business details | Use the correct operator, seller, or publisher identity and contact route. Add legal address, registration, tax, or support details when required. Verify each detail against the real business record. Never invent a business identity. |
| 17 | Connect only necessary data | Apply data minimization and least privilege. Remove unused permissions, SDKs, fields, uploads, and integrations. Do not request identity photos, selfies, or precise location by default. Map data from collection to storage, sharing, retention, and deletion. Document why each connection is needed. |
| 18 | Make forms keyboard friendly | Use programmatic labels, logical tab order, visible focus, accessible groups, and clear instructions. Associate errors with fields, summarize errors when needed, announce status changes, and preserve entered data after recoverable errors. |
| 19 | Remove unsupported claims | Check product, performance, safety, health, price, privacy, security, environmental, and testimonial claims. Keep evidence for objective claims before publication. Remove, qualify, or correct claims that the available evidence does not support. Disclaimers do not repair a false main claim. |
| 20 | Trademark and domain clearance | Before buying a domain or launching a name, search official trademark registers in target markets for exact and confusingly similar marks used with related goods or services. Search common-law use where relevant. Domain availability is separate from trademark clearance; pause on material conflicts and seek qualified counsel. |
| 21 | Dynamic application security assessment | For a runnable website, web app, or API, use Strix as the required default on a local or staging target after the first stable build, after fixes, and before release when the target is owned or explicitly authorized, the scope is defined, and the model budget is approved. If a gate blocks it, record the assessment as incomplete. Do not test public production or third-party targets without current explicit authorization. A clean scan is not proof that the product is secure. |

## Product-specific checks

- **Websites:** check checkout disclosures, cookie and tracking behavior, contact details, forms, third-party embeds, and the mobile and keyboard paths.
- **Apps:** check store privacy disclosures, permission prompts, billing, subscriptions, refunds, account deletion, data collection, and all external SDKs against current platform rules.
- **Games:** check age ratings and child-directed features, chat and user-generated content, reporting and blocking, moderation, save data, purchases and subscriptions, virtual currency, random paid rewards, parental controls, and input accessibility when those features exist.
- **Dashboards and internal tools:** check data access, role visibility, export and deletion controls, audit traces, and accessibility for dense tables and charts.
- **Embedded widgets:** check the host theme, keyboard and screen-reader operation, restricted viewport, third-party requests, and which party owns the user data and support path.

## Official source starting points

These sources are examples, not a complete legal analysis. Check their current versions and the rules for every target market and platform.

- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [US FTC guidance on consumer reviews and testimonials](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)
- [US FTC advertising and marketing guidance](https://www.ftc.gov/business-guidance/advertising-marketing/advertising-marketing-basics)
- [EU General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) and [ePrivacy Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058)
- [EU Consumer Rights Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011L0083)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [Google Play Developer Program policies](https://support.google.com/googleplay/android-developer/answer/18258653)
