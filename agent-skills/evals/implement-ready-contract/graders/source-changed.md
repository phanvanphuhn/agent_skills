---
type: regex
pattern: 'def total\(amount\):[\s\S]*(1\.2|0\.2|\* *6 */ *5|120)'
target: { source: file, path: pricing.py }
---
