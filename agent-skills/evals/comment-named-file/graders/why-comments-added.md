---
type: regex
pattern: '#[^\n]*(lockstep|synchron|rate.?limit|jitter)[\s\S]*#[^\n]*(mobile|legacy|older)'
flags: i
target: { source: file, path: sync_client.py }
---
