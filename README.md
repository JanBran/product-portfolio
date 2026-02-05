# Simple Calendar - Product Framework

The purpose of this repository is to showcase the current options for utilizing AI tools for product management. For the demonstration of the entire product management setup, I used a light weight calendar solution.

This solution utilizes github for storage and issue tracking, VS Code for tracking and submitting changes and Claude Code extension in VS Code for the agentic work. The VS Code also has MCP server for Github actions and issues implemented.

As an elevator pitch, **Simple Calendar** is a minimal, fast calendar app for individuals who want basic scheduling without complexity. View events, add events, and stay organized.

## Product management cycle

Below are outlined major folders for providing both staff and AI agents with sufficient context and allowing for in-depth review of major sources for decision making and feature validation.

### 1. [Strategy and Vision](01-strategy-vision/)
- First product vision, strategy, personas and overall guidelines for the product are set
- This allows for both product manager, other team members and Claude Code to check and validate the product direction
- Helps keep the course of the product straight

### 2. [Market Research](02-market-research/)
- Repository of all the research
- Simple structure allows easy access for AI and can be used in further decisions and compared against the stated product goals

### 3. [Goals](03-goals-metrics/)
- Utilizing OKRs (Objectives and Key Results), the overarching goals for a specific period are set
- This then allows to break down those goals into opportunities and solutions in subsequent sections

### 4. [User research](04-user-research/)
- Contains the summaries and key findings from interviews and surveys
- Along with usage data and feedback contribute to the formation of opportunity solution trees

### 5. [Usage data](05-usage-data/)
- Shows an outline of how data ingestion set up can be put together
- Currently not a fully working solution E2E, just a representation of how to pull data from other systems

### 6. [Opportunity Solution Trees](06-opportunity-solution-trees/)
- Uses widely known framework to validate solutions within the product
- Strong focus on conducting experiments to validate hypotheses
- Aligns goals with further input from user research and usage data along with customer feedback from previous release to define what experiments should be conducted next
- Once validated, the suggested solution can be refined into full fledged product specification

### 7. [Experiments and tests](07-experiments-tests/)
- Repository of the experiments and user tests that were defined as part of Opportunity Solution Trees
- Result of the experiment directly influences the form in which the feature will be fully released

### 8. [Technical context](08-technical-context/)
- Tracks technical architecture from high point of view
- Provides brief pros and cons of the current setup
- Can be used particularly in code generation for guardrails but also to provide less technical members brief overview

### 9. [Feature specifications](09-feature-specs/)
- Features being worked on in more detail after the assumptions have been confirmed in experiments
- Generally can be used hand in hand with the issues in Github or other issue tracking tools

### 10. [Roadmap](10-roadmap/)
- Brief information on the roadmap, which I generally track elsewhere
- Explains how Claude Code is used to move features back to Github

### 11. [Decisions](11-decisions/)
- Tracking of major scope and technological decisions
- Explains why a specific solution was chosen and what alternatives were considered
- Used for historical context and to provide extra guardrails to the AI

### 12. [Customer feedback](12-customer-feedback/)
- Hub of feedback and customer interaction post release of a particular feature
- The feedback can be brought back to the start of the cycle as a basis for the next product discovery
- Keeping the most of the loop within one space allows both staff members and AI robust context

## Claude Code Integration

This repository uses [CLAUDE.md](CLAUDE.md) to instruct Claude Code on repository structure and workflows.

### Key Capabilities
- **Spec Analysis** — Validate feature specs against technical context using "provide analysis"
- **GitHub Issue Creation** — Push specs to GitHub Issues using "move to development"
- **Contextual Navigation** — Claude understands folder structure and cross-references

### How CLAUDE.md Works
The CLAUDE.md file acts as project-specific instructions for Claude Code. It defines:
- Repository structure and key files
- Trigger phrases and expected outputs
- Technical constraints Claude should enforce
- Workflows for common tasks

## Integration with Github issues
For the purposes of issue tracking, I chose the Github issues and projects. This is mainly done for simplicity's sake, but the integration can be easily done with almost any issue tracking tool that has MCP capability such as Clickup or Jira. Alternatively a simple tooling for calling 3rd party API directly would also suffice.

## Files vs. issues
- Files in the repo are mainly used for ease of access and work of the Claude Code and for version tracking
- Any actionable items that require a series of steps are done as part of issues and projects in issue tracking tool and the historical record is generally pasted into Github repo (either manually, by prompt or as part of automated workflow)

### Main workflow for manual tasks
- Market research is done via Issues as a [research task](.github/ISSUE_TEMPLATE/research-task.md) and the result is then put into the [market research](02-market-research/) folder
- Similarly user research is done via [research task](.github/ISSUE_TEMPLATE/research-task.md) except for the user interviews which have their [own template](.github/ISSUE_TEMPLATE/user-interview.md)
- Key findings from the interviews are stored in the dedicated [folder](04-user-research/interviews/), but not the full transcript itself to limit the token usage and retain only highly relevant information
- Tests and experiments are tracked utilizing the [experiment type](.github/ISSUE_TEMPLATE/experiment.md) of the issue and the results are then stored again in the relevant [folder](07-experiments-tests/)
- When all assumptions are clarified through the testing and research, the brainstorming and refinement is done using [feature spec](.github/ISSUE_TEMPLATE/feature-spec.md)
