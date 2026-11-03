# agent_skills

The usable package is the single Claude Code plugin folder [`agent-skills/`](agent-skills/).
Do not copy anything from this repository root into another project.

Load it for a session, or install it once from its local marketplace:

```bash
git clone <this-repo-url> /path/to/agent_skills
claude --plugin-dir /path/to/agent_skills/agent-skills
# or
claude plugin marketplace add /path/to/agent_skills/agent-skills
claude plugin install agent-skills@agent-skills-local
```

Its eval suite runs from inside the folder with `claude plugin eval .`; see
[`agent-skills/evals/README.md`](agent-skills/evals/README.md).
