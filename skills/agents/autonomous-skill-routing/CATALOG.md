# Autonomous Skill Routing

**Category:** [Agents](../README.md)

Uses a machine-readable routing policy to select the smallest matching skill set and a generated source index to check current availability. Separates routing from authorization, preserves real action gates, and keeps the same goal active through safe retries and fallbacks.

**Activation:** Always mandatory
**When:** Use on every prompt. If a required connection or tool is unavailable, follow the fallback in the skill.

**Source:** Owner-approved redacted catalog entry; no upstream repository is claimed.

**Availability:** Catalog entry only. Use the source link to inspect or install the original skill.
