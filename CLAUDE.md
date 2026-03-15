# CLAUDE.md — Tutorial Writing Guidelines

This repo contains marimo notebook tutorials for learning LangChain, LangGraph, and Deep Agents. Notebooks live in `langchain-notebooks/`. Source docs live in git submodules (`docs/`, `langchain/`, `langgraph/`, `deepagents/`).

## Structure

- `langchain-notebooks/` — marimo notebook tutorials (numbered `01_`, `02_`, etc.)
- `LEARNING_PLAN.md` — curriculum and reading order
- `TOC.md` — doc sources table of contents
- `docs/`, `langchain/`, `langgraph/`, `deepagents/` — submodules, do not edit

## LLM Configuration

Notebooks use an OpenAI-compatible endpoint instead of direct provider APIs. Credentials are in `.env` (encrypted with SOPS).

When writing code that calls an LLM, always use `ChatOpenAI` pointed at our endpoint:

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    base_url=os.environ["AI_ENDPOINT"] + "/v1",
    api_key=os.environ["AI_KEY"],
    model="glm-5",  # or any model available on the endpoint
)
```

Never hardcode keys. Never use provider-specific classes like `ChatAnthropic` or `ChatGoogleGenerativeAI` — route everything through `ChatOpenAI` with our endpoint.

## Writing Tutorials

### Voice and Clarity

Write like a human teaching a friend, not like a textbook.

- Use "you" and "we" — never "the user" or "one"
- State things directly — no hedging ("simply", "just", "basically", "actually")
- Short sentences. Short paragraphs. One idea per cell.
- Prefer concrete examples over abstract explanations
- If a concept needs a paragraph to explain, show code instead

**Before:** "It is important to understand that LangChain provides abstractions that facilitate the process of building agents."
**After:** "LangChain gives you building blocks for agents. Here's one in 10 lines."

### Cell Structure

Each marimo notebook follows this pattern:

1. **Title cell** — `# Lesson N: Topic` with a one-line summary
2. **Concept cells** — explain one idea each, using `mo.md()`
3. **Code cells** — runnable examples that demonstrate the concept
4. **Interactive cells** — use `mo.ui` widgets where they aid understanding
5. **Takeaway cell** — a blockquote summarizing what to remember

### What to Include

- Runnable code that works out of the box
- Tables and ASCII diagrams for comparisons and architecture
- "When to use" guidance — help the reader make decisions
- Links to source docs in the submodules when going deeper

### What to Avoid

- Walls of text — if a cell has more than 8 lines of markdown, split it
- Repeating what the source docs say verbatim — distill and reframe
- Code that requires API keys without clear setup instructions
- Passive voice — make the subject act ("LangChain provides" not "is provided by")
- Filler words: very, really, quite, rather, somewhat, essentially
- "Key features" lists — show features through examples instead
- Emojis unless the user asks for them

### Words to Cut

| Write this | Not this |
|------------|----------|
| to | in order to |
| now | at this point in time |
| if | in the event that |
| because | due to the fact that |
| use | utilize |
| start | initialize / instantiate (unless API-specific) |
| (state it) | I think / I believe / it should be noted that |

### Rewriting Checklist

Before finishing a notebook:

1. Read each cell aloud — cut what sounds awkward
2. Cut 10–20% of the prose — every draft has fat
3. Check every code cell runs
4. Verify the notebook tells a story from top to bottom
5. End with a clear next step pointing to the next lesson
