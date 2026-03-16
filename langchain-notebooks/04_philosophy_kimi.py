import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 4: Philosophy

    Why LangChain exists and what it believes about building with LLMs.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Core Beliefs

    LangChain is built on a few simple ideas:

    1. **LLMs are powerful** — but they become even more useful when combined with external data
    2. **Future applications will be agentic** — apps that reason, act, and iterate
    3. **Prototypes are easy, production is hard** — reliability is the main challenge

    These beliefs shape everything in the framework.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Two Core Goals

    LangChain focuses on two things:

    | Goal | What it means |
    |------|---------------|
    | **Standardize model access** | Same interface for OpenAI, Anthropic, Google, local models — swap providers without rewriting code |
    | **Enable complex orchestration** | Tools, memory, retrieval — let models interact with data and systems beyond text generation |

    The first goal saves you from vendor lock-in. The second lets you build agents that actually do things.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## A Brief History

    Understanding where LangChain came from helps you use it better today.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2022: The Beginning

    LangChain launched a month before ChatGPT. The original idea was simple:

    - Abstract different LLM providers behind a common interface
    - Chain together steps (retrieval → generation) for common tasks

    The name comes from "Language" + "Chains".
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2023: Agents and Tool Calling

    - **January**: Chat models arrived (messages in, messages out)
    - **March**: OpenAI added function calling — models could generate structured tool calls
    - **June**: LangSmith released for observability and evaluation

    Agents evolved from parsing JSON to native tool calling. Reliability became the focus.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2024: Production and LangGraph

    - **February**: LangGraph released for low-level orchestration
    - **October**: LangGraph became the recommended way to build complex applications

    The lesson: high-level abstractions get you started, but production requires control.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2025: LangChain 1.0

    Two major changes:

    1. **One agent abstraction** — built on LangGraph, replacing all old chains and agents
    2. **Standard message format** — handles reasoning blocks, citations, multimodal content

    The framework is now simpler and more powerful.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What This Means for You

    - Start with high-level abstractions (`create_agent`) to get something working fast
    - Drop down to LangGraph when you need control over execution flow
    - Use LangSmith from day one — observability is essential for reliable agents

    > **Remember**: LangChain's job is to make the easy things easy and the hard things possible. Start simple, add complexity only when you need it.
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
