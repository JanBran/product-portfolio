## Roadmap and backlog management
- For the demonstration purposes, this repository uses GitHub Issues for task tracking, keeping documentation and version control in one place. This means most product management use cases can be handled within your code repository using GitHub Projects and Issues.
    - See the roadmap project here.
- I would generally recommend something more pronounced if you need really in-depth data analysis, such as JetBrains' DataSpell could be interesting fit or having matrixes similar to what Product Board offers could be a good fit
- For opportunity solution trees, Obsidian, Miro or other solutions could be useful, though I would still recommend having some sort of written counterpart, be it mermaid code or something similar to that (although you can get those data from 3rd party tools by other means)

## Flow from Github to other solutions
- Once the feature spec is finalized, you can prompt Claude to push it to Github as an issue using Github MCP by using the phrase "move to development"
- For details please check adjusted [CLAUDE.md](CLAUDE.md) in the root

---

## Related Folders

- [Feature Specs](../09-feature-specs/) — Detailed specifications pushed to development
- [Spec Templates](.github\ISSUE_TEMPLATE\feature-spec.md) — Templates for creating new specs
- [Opportunity Solution Trees](../06-opportunity-solution-trees/) — Where feature ideas originate
- [Technical Context](../08-technical-context/) — Architecture and technical decisions
- [Decision Log](../11-decisions/) — Record of key decisions made
