# AI Daily Workflow

A small personal Obsidian brief: source collection → GPT-5.6 Luna generation →
independent Luna review → deterministic Markdown → create-new publication.

## Clean baseline

This repository starts from a curated snapshot of the working six-module engine
at upstream commit `2ac477a`. Runtime implementation and selected portable behavior
tests are preserved, not rewritten. The original checkout and history remain intact.

Included: the active Python engine, its RSS fetcher/import dependencies, portable
tests and MIT license. Excluded: private source/context files, credentials, notes,
model outputs, runtime receipts, development transcripts, legacy UI/activation
infrastructure and unrelated Git history. No secrets are needed for offline tests.

The baseline still reads deployment configuration from the existing external local
paths. It is a working snapshot for this deployment, not a zero-configuration hosted
service. Never commit those private files. See `examples/README.md` for the boundary.

## Development (Windows, Python 3.12)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest tests
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\python.exe -m mypy src/pkm_workflow
```

Only Codex performs the model roles. Python never invokes DeepSeek, an OpenAI API,
or Codex CLI. An existing daily note is never silently overwritten. Local scheduled
operation requires the host and app to be available; no cloud availability promise.

## Current cadence

Mon/Thu: research + AI practice. Tue/Fri: builders + venture/industry.
Wed/Sat: cognition + GitHub. Sunday: one six-module weekly synthesis instead of a
daily. Daily evidence is capped at 12,000 characters; weekly at 24,000.

See [the operating contract](docs/ai-daily-luna.md). Weekly uses verified daily
history, with source dates and original links; it never fetches another news dump.
The immutable `baseline-six-modules` tag retains the pre-change six-item version.

Development lives in this repository. The existing local engine deployment remains
in its original MVP checkout; only reviewed runtime changes are synchronized there.
Neither private configuration nor the user's Vault is migrated into this repository.
