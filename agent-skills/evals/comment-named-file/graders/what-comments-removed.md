---
type: regex
pattern: '# (loop over attempts|send the request|create the body dict)'
match: not_contains
target: { source: file, path: sync_client.py }
---
