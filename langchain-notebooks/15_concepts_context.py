import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 15: Context

    Static vs dynamic, runtime vs cross-conversation.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What Is Context?

    **Context engineering** is the practice of giving your AI application the right information, in the right format, at the right time. Without it, even the best model can't do its job.

    Context has two dimensions: **mutability** (does it change?) and **lifetime** (how long does it last?).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Mutability: Static vs Dynamic

    **Static context** doesn't change during execution. Think user IDs, API keys, database connections, permissions. You set it once at the start of a run.

    **Dynamic context** evolves as the application runs. Conversation history, intermediate results, tool call outputs -- all of these grow and change mid-run.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Lifetime: Runtime vs Cross-Conversation

    **Runtime context** is scoped to a single invocation. When the run ends, it's gone.

    **Cross-conversation context** persists across multiple sessions. User preferences, long-term memory, accumulated knowledge -- these survive between runs.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Three Context Types in LangGraph

    Combine mutability and lifetime and you get three practical categories:

    | Type | Description | Mutability | Lifetime | Access |
    |------|-------------|------------|----------|--------|
    | **Static runtime** | User metadata, tools, db connections | Static | Single run | `context` arg to `invoke` |
    | **Dynamic runtime (state)** | Mutable data during a run | Dynamic | Single run | LangGraph state object |
    | **Dynamic cross-conversation (store)** | Persistent across conversations | Dynamic | Cross-conversation | LangGraph store |

    Each serves a different purpose. The rest of this lesson walks through them one by one.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Static Runtime Context

    Passed via `context=` when you call `invoke` or `stream`. Immutable -- it can't change during the run. Use it for user IDs, API keys, permissions, and database connections.

    ```python
    @dataclass
    class ContextSchema:
        user_name: str

    graph.invoke(
        {"messages": [{"role": "user", "content": "hi!"}]},
        context={"user_name": "John Smith"}
    )
    ```

    Tools and nodes can read this context but never modify it.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Where Static Context Shows Up

    Static context flows into three places:

    - **Agent prompts** -- personalize the system prompt based on the user
    - **Tool functions** -- pass db connections or user IDs without hardcoding
    - **Workflow nodes** -- access config values inside any graph node

    Think of it as dependency injection for your agent. Instead of global variables, you thread data through the `context` argument.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Dynamic Runtime Context (State)

    This is mutable data that evolves during a single run. In LangGraph, the **state object** holds it.

    The most common example: the `messages` list. Every model call appends to it. Every tool result gets added. The state grows as the agent works.

    ```python
    class CustomState(TypedDict):
        messages: list[AnyMessage]
        extra_field: int

    def node(state: CustomState):
        messages = state["messages"]
        return {"extra_field": state["extra_field"] + 1}
    ```

    State is scoped to a single run -- unless you enable memory (covered in other lessons).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Static vs Dynamic Runtime: When to Use Which

    | Question | Use static context | Use state |
    |----------|--------------------|-----------|
    | Does it change during the run? | No | Yes |
    | Is it per-user config? | Yes | No |
    | Is it conversation history? | No | Yes |
    | Do tools need to update it? | No | Yes |
    | Example | `user_id`, `api_key` | `messages`, `step_count` |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Dynamic Cross-Conversation Context (Store)

    The LangGraph **store** holds persistent, mutable data that spans multiple conversations. It survives between sessions.

    Use it for:

    - **User profiles** -- name, preferences, settings
    - **Long-term memory** -- facts learned across conversations
    - **Historical interactions** -- summaries of past sessions
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Store vs State

    State resets each run. The store persists.

    | | State | Store |
    |---|-------|-------|
    | **Lifetime** | Single run | Across conversations |
    | **Mutability** | Read/write during run | Read/write anytime |
    | **Resets** | After each invocation | Never (unless you delete) |
    | **Use for** | Messages, intermediate results | User profiles, preferences |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## How They Connect

    All three context types feed into the same agent at different levels:

    ```
    ┌─────────────────────────────────────────────────────────┐
    │                    INVOCATION                            │
    │                                                          │
    │  context={"user_id": "abc"}     Static runtime context   │
    │          │                                                │
    │          ▼                                                │
    │  ┌──────────────┐                                        │
    │  │    Agent /    │◄──── state (messages, fields)          │
    │  │    Graph      │      Dynamic runtime context           │
    │  └──────┬───────┘                                        │
    │         │                                                 │
    │         ▼                                                 │
    │  ┌──────────────┐                                        │
    │  │    Tools /    │◄──── store (profiles, memory)          │
    │  │  Middleware   │      Dynamic cross-conversation        │
    │  └──────────────┘                                        │
    └─────────────────────────────────────────────────────────┘
    ```

    Static context arrives at invocation time and stays fixed. State evolves as nodes and tools execute. The store reads and writes persistent data across the boundary of any single run.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Runtime Context Is Not LLM Context

    An important distinction: **runtime context** is data your *code* needs. It's not the same as:

    - **LLM context** -- the tokens passed in the prompt
    - **Context window** -- the maximum tokens the model can handle

    Runtime context is dependency injection. You use it to *build* the LLM context -- for example, reading a user ID from runtime context, fetching their preferences from the store, and injecting those into the prompt.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Context comes in three flavors.** Static runtime context is immutable config passed at invocation. Dynamic runtime context (state) is mutable data that evolves during a run. Dynamic cross-conversation context (store) persists across sessions. Together, they give your agent everything it needs to do its job.

    **Next:** Lesson 16
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
