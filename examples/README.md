# External configuration

Supply a source catalog and an approved context outside Git. Their schemas and
validation live in `source_catalog.py` and `user_context_v75.py`.

Minimal conceptual context (not a production authorization file):

```json
{"projects":["Your current project"],"prior_knowledge":[],"vault_inference_allowed":false}
```

The real context adds the five interest pillars, weights and source selection
questions. This repository intentionally does not distribute anyone's profile.
The test suite builds synthetic contexts in isolated temporary directories.
