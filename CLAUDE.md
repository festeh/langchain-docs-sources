# CLAUDE.md — Tutorial Writing Guidelines

This repo contains marimo notebook tutorials for learning LangChain, LangGraph, and Deep Agents. Notebooks live in `langchain-notebooks/`. Source docs live in git submodules (`docs/`, `langchain/`, `langgraph/`, `deepagents/`).

## Structure

- `langchain-notebooks/` — marimo notebook tutorials (numbered `01_`, `02_`, etc.)
- `LEARNING_PLAN.md` — curriculum and reading order
- `TOC.md` — doc sources table of contents
- `docs/`, `langchain/`, `langgraph/`, `deepagents/` — submodules, do not edit

## LLM Configuration

Notebooks use an OpenAI-compatible endpoint instead of direct provider APIs. Credentials are in `.env` (encrypted with SOPS).

When writing code that calls an LLM, always use `ChatOpenAI` pointed at our endpoint. Define `MODEL` once and reuse it — never duplicate model names across cells:

```python
import os
from langchain_openai import ChatOpenAI

MODEL = "glm-5"  # single source of truth for model name

llm = ChatOpenAI(
    base_url=os.environ["AI_ENDPOINT"] + "/v1",
    api_key=os.environ["AI_KEY"],
    model=MODEL,
)
```

When using `create_agent`, pass the `ChatOpenAI` instance directly — not a string identifier:

```python
from langchain.agents import create_agent

agent = create_agent(llm, tools=[...])
```

Never hardcode keys. Never use provider-specific classes like `ChatAnthropic` or `ChatGoogleGenerativeAI` — route everything through `ChatOpenAI` with our endpoint.

## Running Code

All code that needs env vars must go through the justfile, which handles SOPS decryption:

```bash
just py script.py          # run a script
just py -c "print('hi')"   # run inline python
just edit notebook.py       # marimo edit mode (no token required)
```

Never call `sops exec-env` directly — use `just py` instead.

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

### Code Cell Output

Every code cell must end with a single `mo.md(...)` call — no branching. Collect results into a variable, then display it:

```python
# Good — gather state, display at the end
results = []
for doc in docs:
    results.append(f"- **{doc.metadata['source']}**: {doc.page_content[:80]}")

mo.md("\n".join(results))
```

```python
# Bad — conditional md calls
if response:
    mo.md(f"Got: {response}")
else:
    mo.md("No response")
```

```python
# Bad — md inside try/except
try:
    result = chain.invoke(query)
    mo.md(f"Result: {result}")
except Exception as e:
    mo.md(f"Error: {e}")
```

Build the string first, then call `mo.md()` once at the bottom.

### Coverage Rule

Every topic in the source docs must be covered somewhere in the notebooks. If a source file (e.g. `models.mdx`) contains more content than fits in one notebook, split it across multiple lessons or defer specific subtopics to later lessons — but update `LANGCHAIN_LEARNING_PLAN.md` so nothing falls through the cracks. The plan is the source of truth for what gets covered and where.

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
