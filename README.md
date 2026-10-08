# AI Skills Collection

A growing collection of reusable AI skills that can be used with **Claude**, **ChatGPT**, and other AI agent platforms.

These skills are designed to help users move beyond generic AI responses by creating repeatable workflows, better prompts, and specialized AI capabilities.

## What are AI Skills?

AI skills are reusable instruction sets, workflows, and frameworks that help an AI assistant perform specific tasks more consistently.

Instead of repeatedly writing the same prompts, you can create a skill once and reuse it across different AI assistants.

## Using These Skills

### Claude

1. Download or copy the skill folder.
2. Add the skill instructions to Claude Projects, Claude Skills, or your preferred Claude workflow.
3. Activate the skill when working on related tasks.

### ChatGPT / OpenAI

1. Copy the skill instructions into a Custom GPT, Project, or conversation context.
2. Provide the required files or references if the skill requires additional resources.
3. Use the skill as a reusable workflow for your tasks.

## Repository Structure

Each skill will follow a consistent structure:

```
skill-name/
├── SKILL.md        # Core instructions for the AI agent
├── examples/       # Examples and use cases
└── resources/      # Supporting materials (optional)
```

## Available Skills
Each skill is a reusable workflow: a SKILL.md with instructions an AI assistant follows, plus supporting references and scripts where needed. Copy a skill folder into a Claude Project or a ChatGPT custom GPT and use it directly.
| Skill | What it does | Platforms |
|-------|--------------|-----------|
| [ai-slop-removal](skills/ai-slop-removal/) | Detects and strips AI-generated writing patterns (generic hooks, buzzword filler, rule-of-three, symmetric “not X but Y” constructions, em dashes) while preserving meaning and tone. Ships with a mechanical detector script and a 30-pattern reference catalog. | Claude, ChatGPT |
| [product-discovery](skills/product-discovery/) | Runs a structured product discovery pass over a product description and user reviews, and produces a report covering problem statement, personas, pain points, current workarounds, unmet needs, ideas, and recommendations. | Claude, ChatGPT |

## Design Principles

These skills aim to:

- Reduce repetitive prompting
- Improve AI output quality
- Avoid generic AI-generated responses (AI slop)
- Capture expert workflows and thinking patterns
- Make AI assistants more useful for professional work

## Contributing

Have a useful workflow or AI capability to share?

Create a new skill folder, add the `SKILL.md` instructions, and update the skill catalog above.

## License

Individual skills may have their own usage instructions and licensing terms.
