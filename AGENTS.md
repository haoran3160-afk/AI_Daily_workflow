# AI Daily Workflow

Read README.md and the workflow runbook before changing behavior.
Keep source collection, independent Luna review and deterministic publication.
No DeepSeek/OpenAI API/Codex CLI fallback. Do not read or commit .env, private
configuration, Obsidian notes, runtime artifacts or user history.

Use explicit staging and small commits. Test behavior and the actual reading
experience. Do not weaken assertions, review bindings or no-overwrite guarantees.
Only the current user request can authorize replacing a particular existing note.

The running private configuration project is external to this public repository.
Scheduled tasks never edit code/config and never scan unrelated Vault content.
