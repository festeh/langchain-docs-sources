import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
        # Lesson 1: Framework Landscape

        Three open source packages, three levels of the stack. Pick the right one and you save yourself hours.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## The Stack

        ```
        ┌───────────────────────────────┐
        │  Deep Agents SDK  (harness)   │  batteries included
        ├───────────────────────────────┤
        │  LangChain        (framework) │  abstractions & integrations
        ├───────────────────────────────┤
        │  LangGraph        (runtime)   │  orchestration engine
        └───────────────────────────────┘
        ```

        Each layer builds on the one below. LangChain runs on LangGraph. Deep Agents runs on LangGraph too.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## At a Glance

        | | **Framework** | **Runtime** | **Harness** |
        |---|---|---|---|
        | Package | LangChain | LangGraph | Deep Agents SDK |
        | You get | Model abstraction, tool interface, agent loop, 100+ integrations | Durable execution, streaming, human-in-the-loop, persistence | Planning, subagents, file system, token management |
        | Use when | You want a working agent fast | You need low-level control or long-running workflows | You need autonomous agents for complex multi-step tasks |
        | Alternatives | Vercel AI SDK, CrewAI, OpenAI Agents SDK, Google ADK | Temporal, Inngest | Claude Agent SDK, Manus |
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## LangChain — the Framework

        Swap a model provider in one line. Wire up tools with a decorator. Get a working agent loop out of the box.
        """
    )
    return


@app.cell
def _(mo, os, ChatOpenAI):
    # A working agent in 5 lines
    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model="glm-5",
    )
    response = llm.invoke("What is LangChain in one sentence?")
    mo.md(f"**Model says:** {response.content}")
    return (llm,)


@app.cell
def _(mo):
    mo.md(
        """
        That's it. One class, one call. LangChain handles message formatting, retries, and provider differences.

        Use LangChain when you want to build agents fast without worrying about orchestration details.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## LangGraph — the Runtime

        LangGraph gives you the engine under the hood. You define nodes (functions) and edges (transitions) as a graph.

        - **Durable execution** — agents survive failures and resume where they stopped
        - **Streaming** — token-by-token output and event streams
        - **Human-in-the-loop** — pause, inspect, modify agent state, then continue
        - **Persistence** — save and restore conversation threads

        Use LangGraph when you need fine-grained control or your workflow mixes deterministic steps with LLM calls.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Deep Agents SDK — the Harness

        Deep Agents wraps LangGraph with opinionated defaults for complex, long-running tasks.

        - **Planning** — the agent tracks tasks with a to-do list
        - **Subagents** — delegate work, keep context clean
        - **File system** — read/write on pluggable storage
        - **Token management** — auto-summarize history, evict large results

        Use Deep Agents when your agent needs to plan, research, and produce artifacts over many steps.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Feature Comparison

        | Feature | LangChain | LangGraph | Deep Agents |
        |---|---|---|---|
        | Short-term memory | built-in | built-in | StateBackend |
        | Long-term memory | built-in | built-in | built-in |
        | Multi-agent | skills, subagents, handoffs | subgraphs | subagents, skills |
        | Human-in-the-loop | middleware | interrupts | interrupt_on param |
        | Streaming | built-in | built-in | built-in |
        """
    )
    return


@app.cell
def _(mo):
    framework = mo.ui.dropdown(
        options=["LangChain", "LangGraph", "Deep Agents SDK"],
        value="LangChain",
        label="Pick the one that fits your use case:",
    )
    framework
    return (framework,)


@app.cell
def _(framework, mo):
    guide = {
        "LangChain": (
            "**LangChain** — start here. "
            "You get a working agent in minutes, swap providers freely, and add tools with decorators. "
            "Next up: Lesson 2 (LangChain Overview)."
        ),
        "LangGraph": (
            "**LangGraph** — for when you need control. "
            "Define nodes, edges, and state explicitly. Great for production workflows. "
            "Learn LangChain first (Lessons 2-7), then jump to Phase 8."
        ),
        "Deep Agents SDK": (
            "**Deep Agents SDK** — for autonomous, long-running work. "
            "Planning, subagents, and file systems come built in. "
            "Learn LangChain first, then explore Deep Agents for advanced use cases."
        ),
    }
    mo.md(guide[framework.value])
    return


@app.cell
def _(mo):
    mo.md(
        """
        > **Start with LangChain.** Drop to LangGraph when you need low-level control.
        > Reach for Deep Agents when the task demands planning and autonomy.
        > All three come from the same team and compose together.

        **Next:** Lesson 2 — LangChain Overview
        """
    )
    return


@app.cell
def _():
    import os
    import marimo as mo
    from langchain_openai import ChatOpenAI
    return ChatOpenAI, mo, os


if __name__ == "__main__":
    app.run()
