# Codex Budget Model Router

**Category:** [Agents](../README.md)

Routes parent and subagent work by task difficulty: routine Easy and Medium tasks use GPT-6 Luna / max, routine Hard tasks use GPT-6.1 Terra / low, and complex or high-risk implementation uses GPT-6.2 Sol / medium. Select the parent route before task startup. All other models outside these routes require an explicit current-task user request and are never selected automatically. The README explains the observed performance-versus-usage rationale, compares Artificial Analysis benchmark scores and Index task time, and distinguishes OpenAI Standard API rates from ChatGPT and Codex plan usage.

**Activation:** Before parent or subagent model-route selection
**When:** Use for parent startup routing or subagent model selection. Skip when no model route needs to be chosen.

**Source:** [Upstream repository](https://github.com/engbyume/codex-budget-model-router).

**Availability:** Catalog entry only. Use the source link to inspect or install the original skill.
