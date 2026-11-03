# Saved state location

Project discovery and handoff are the only skills that persist files. Resolve one state
root before writing, and report the absolute path of every saved file.

| Package placement | State root |
| --- | --- |
| Vendored: this package folder sits inside the user's workspace, such as a cloned `agent-skills/` folder | The package folder itself: `project-contexts/` and `handoffs/` beside `skills/` |
| Installed plugin: the package root is outside the workspace, such as a Claude Code plugin cache | `${CLAUDE_PLUGIN_DATA}`, which Claude Code resolves to a per-plugin data directory kept across plugin updates |

Never write into an installed plugin root; it is replaced on every plugin update and is
shared by every project that uses the plugin. When `${CLAUDE_PLUGIN_DATA}` appears
literally instead of as an absolute path, the host did not resolve it, so treat the
installed-plugin root as unavailable.

Under the selected root, keep one PROJECT CONTEXT file per target repository in
`project-contexts/` and one folder per task in `handoffs/`. Record the target
repository's absolute path inside each file so a shared state root stays unambiguous.

If no state root can be resolved or written, return the documents in the conversation,
state that they were not saved, and name the persistence gap. Do not fall back to the
host repository, a temporary directory, or another location the user did not choose.
