import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
        # Lesson 1: Framework Landscape

        **LangChain vs LangGraph vs Deep Agents — when to use what**

        LangChain maintains three open source packages for building agents.
        Each sits at a different level of the stack:

        | | Framework | Runtime | Harness |
        |---|---|---|---|
        | **Package** | LangChain | LangGraph | Deep Agents SDK |
        | **Value** | Abstractions, Integrations | Durable execution, Streaming, HITL, Persistence | Predefined tools, Prompts, Subagents |
        | **When to use** | Getting started quickly, Standardizing team builds | Low-level control, Long-running stateful workflows | Autonomous agents, Complex non-deterministic tasks |
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## The Three Layers

        Think of them as a stack — each layer builds on the one below:

        ```
        ┌─────────────────────────────────┐
        │   Deep Agents SDK  (harness)    │  ← batteries included
        ├─────────────────────────────────┤
        │   LangChain        (framework)  │  ← abstractions & integrations
        ├─────────────────────────────────┤
        │   LangGraph        (runtime)    │  ← orchestration engine
        └─────────────────────────────────┘
        ```

        LangChain 1.0 is built **on top of** LangGraph. You don't need to know LangGraph to use LangChain.
        Deep Agents SDK builds on top of LangGraph and adds planning, file systems, and subagent spawning.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 1. Agent Frameworks (LangChain)

        Agent frameworks provide **abstractions** that make it easier to get started building with LLMs.

        LangChain gives you:
        - Standard model interface (swap providers with one line)
        - Structured content blocks & agent loop
        - Middleware system
        - 100+ integrations out of the box

        **Use LangChain when:**
        - You want to quickly build agents and autonomous applications
        - You need standard abstractions for models, tools, and agent loops
        - You want easy-to-use but still flexible
        - Building straightforward agent apps without complex orchestration

        **Alternatives:** Vercel AI SDK, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 2. Agent Runtimes (LangGraph)

        Agent runtimes provide the tooling for **running agents in production**.

        LangGraph gives you:
        - **Durable execution** — agents persist through failures, resume where they left off
        - **Streaming** — streaming workflows and responses
        - **Human-in-the-loop** — inspect and modify agent state
        - **Persistence** — thread-level and cross-thread state management
        - **Low-level control** — direct control over orchestration

        **Use LangGraph when:**
        - You need fine-grained control over agent orchestration
        - You need durable execution for long-running stateful agents
        - Building complex workflows mixing deterministic + agentic steps
        - You need production-ready infrastructure

        **Alternatives:** Temporal, Inngest
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 3. Agent Harnesses (Deep Agents SDK)

        Agent harnesses are **opinionated, batteries-included** frameworks with built-in tools.

        Deep Agents SDK gives you:
        - **Planning** — track multiple tasks with a to-do list
        - **Task delegation** — spawn subagents, keep context clean
        - **File system** — read/write on pluggable storage backends
        - **Token management** — conversation summarization, large result eviction

        **Use Deep Agents SDK when:**
        - Building agents that run over long time periods
        - Handling complex, multi-step tasks requiring planning
        - You want predefined tools (filesystem, bash, context engineering)
        - You want predefined prompts and subagents

        **Alternatives:** Claude Agent SDK, Manus
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Feature Comparison

        | Feature | LangChain | LangGraph | Deep Agents |
        |---------|-----------|-----------|-------------|
        | Short-term memory | built-in | built-in | StateBackend |
        | Long-term memory | built-in | built-in | built-in |
        | Skills / plugins | multi-agent skills | — | skills |
        | Subagents | multi-agent subagents | subgraphs | subagents |
        | Human-in-the-loop | middleware | interrupts | interrupt_on param |
        | Streaming | agent streaming | built-in | built-in |
        """
    )
    return


@app.cell
def _(mo):
    framework = mo.ui.dropdown(
        options=["LangChain", "LangGraph", "Deep Agents SDK"],
        value="LangChain",
        label="Which framework fits your use case?",
    )
    framework
    return (framework,)


@app.cell
def _(framework, mo):
    descriptions = {
        "LangChain": mo.md(
            """
            ### You picked: LangChain (Framework)

            **Best for:** Getting started fast, standard agent patterns, team standardization.

            **Next step:** Go to Lesson 2 (LangChain Overview) to learn the architecture and build your first agent in ~10 lines of code.

            ```
            pip install langchain langchain-openai
            ```
            """
        ),
        "LangGraph": mo.md(
            """
            ### You picked: LangGraph (Runtime)

            **Best for:** Production workflows, durable execution, complex state machines.

            **Next step:** Start with LangChain first (Lessons 2-7), then dive into LangGraph in Phase 8 of the learning plan.

            ```
            pip install langgraph
            ```
            """
        ),
        "Deep Agents SDK": mo.md(
            """
            ### You picked: Deep Agents SDK (Harness)

            **Best for:** Autonomous long-running agents, complex multi-step tasks with planning.

            **Next step:** Learn LangChain basics first (it's the foundation), then explore Deep Agents for advanced autonomous use cases.

            ```
            pip install deepagents
            ```
            """
        ),
    }
    descriptions[framework.value]
    return (descriptions,)


@app.cell
def _(mo):
    mo.md(
        """
        ## Key Takeaway

        > **Start with LangChain** for most use cases. Drop down to **LangGraph** when you need
        > low-level control or durable execution. Use **Deep Agents SDK** when you need
        > batteries-included autonomous agents for complex tasks.

        All three are maintained by the same team and designed to work together.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
