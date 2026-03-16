import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 4: Philosophy

    Why LangChain exists, what problems it solves, and how it got here.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Two Core Goals

    LangChain focuses on two things:

    1. **Use any model, no lock-in.** Providers have different APIs, message formats, and parameters. LangChain standardizes them so you can swap models in one line.

    2. **Models should do more than generate text.** They should orchestrate — call tools, query databases, process documents. LangChain makes that wiring easy.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## The Hard Problem

    Building an LLM prototype is easy. Making it reliable enough for production is hard.

    That gap — prototype to production — is what LangChain, LangGraph, and LangSmith exist to close:

    | Layer | What it solves |
    |---|---|
    | **LangChain** | Standard interface, tools, agent loop |
    | **LangGraph** | Durable execution, streaming, state management |
    | **LangSmith** | Observability, tracing, evaluation |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## How We Got Here

    LangChain has evolved alongside the LLM ecosystem. Here's the timeline:

    ```
    2022-10  LangChain v0.0.1 — LLM abstractions + "chains" (predefined steps)
         12  First agents added (ReAct: reasoning + acting)

    2023-01  OpenAI releases Chat Completions API (strings → messages)
         01  LangChain JS launched
         02  LangChain Inc. formed — goal: "make intelligent agents ubiquitous"
         03  OpenAI adds function calling → LangChain adopts it for tool use
         06  LangSmith released — observability and evals

    2024-01  LangChain v0.1.0 — focus shifts to stability
         02  LangGraph released — low-level orchestration layer
         06  700+ integrations, split into standalone packages
         10  LangGraph becomes the preferred runtime for anything beyond a single LLM call

    2025-04  Multimodal APIs — images, files, video in standard message format
         10  LangChain v1.0 — one agent abstraction (built on LangGraph),
             standard message content format across providers
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Key Shifts

    Three big changes shaped LangChain's design:
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 1. Chains → Agents

    Early LangChain was about **chains**: fixed sequences of steps (retrieve, then generate). Now it's about **agents**: the model decides what to do next. Chains are deterministic. Agents are dynamic.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2. JSON Parsing → Native Tool Calling

    First-gen agents parsed raw JSON from model output to figure out which tool to call. Now models have built-in tool calling APIs — they return structured tool calls directly. More reliable, less parsing.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 3. High-Level Only → Layered Stack

    LangChain v0.x tried to be everything. v1.0 split into layers:
    - **LangChain** — high-level agent abstraction
    - **LangGraph** — low-level control when you need it
    - **LangSmith** — see what your agent is doing

    You pick the level of control you need.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What This Means for You

    - Start with `create_agent` — it covers most use cases
    - Drop to LangGraph when you need custom orchestration
    - Use LangSmith when debugging agent behavior
    - Don't worry about provider lock-in — the standard interface lets you switch anytime
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **LangChain exists to close the gap between LLM prototype and production.**
    > It standardizes model interfaces, provides an agent loop, and layers control
    > so you use only as much complexity as you need.

    **Next:** Lesson 5 — Models
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
