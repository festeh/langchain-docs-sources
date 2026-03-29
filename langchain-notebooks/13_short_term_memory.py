import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 13: Short-Term Memory

    Let your agent remember the conversation.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What Is Short-Term Memory?

    Short-term memory is thread-scoped persistence. The agent remembers what happened *in this conversation* and forgets everything when the thread ends.

    Think of it like a phone call — you remember what was said during the call, but not after you hang up.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Why It Matters

    Without memory, every `invoke` call starts fresh. The agent has no idea what you said two messages ago.

    | Turn | You say | Agent without memory | Agent with memory |
    |------|---------|---------------------|-------------------|
    | 1 | "I'm Bob" | "Hi Bob!" | "Hi Bob!" |
    | 2 | "What's my name?" | "I don't know" | "Your name is Bob" |

    Memory also introduces a tradeoff: messages grow, context windows are finite, and costs increase with every token.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Adding Memory with a Checkpointer

    Pass `checkpointer=InMemorySaver()` when creating an agent. Then include a `thread_id` in every call to group messages into a conversation.

    ```python
    from langchain.agents import create_agent
    from langgraph.checkpoint.memory import InMemorySaver

    agent = create_agent(
        llm,
        tools=[get_user_info],
        checkpointer=InMemorySaver(),
    )

    # First turn — agent learns your name
    agent.invoke(
        {"messages": [{"role": "user", "content": "Hi! My name is Bob."}]},
        {"configurable": {"thread_id": "1"}},
    )

    # Second turn — same thread_id, agent remembers
    agent.invoke(
        {"messages": [{"role": "user", "content": "What's my name?"}]},
        {"configurable": {"thread_id": "1"}},
    )
    # -> "Your name is Bob!"
    ```

    `InMemorySaver` stores state in a Python dict. It works for development but loses everything when the process stops.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## How It Works Under the Hood

    ```
    invoke(thread_id="1")
      -> Load state for thread "1" (or create empty state)
      -> Append new messages
      -> Run the agent (model + tools loop)
      -> Save updated state back to checkpointer
    ```

    State is read at the start of each step and saved after each step completes. Tool calls, model responses — everything gets persisted.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Custom State

    The default `AgentState` only tracks `messages`. Extend it to store anything thread-scoped — user IDs, preferences, intermediate results.

    ```python
    from langchain.agents import create_agent, AgentState
    from langgraph.checkpoint.memory import InMemorySaver

    class CustomAgentState(AgentState):
        user_id: str
        preferences: dict

    agent = create_agent(
        llm,
        tools=[get_user_info],
        state_schema=CustomAgentState,
        checkpointer=InMemorySaver(),
    )

    result = agent.invoke(
        {
            "messages": [{"role": "user", "content": "Hello"}],
            "user_id": "user_123",
            "preferences": {"theme": "dark"},
        },
        {"configurable": {"thread_id": "1"}},
    )
    ```

    Custom fields persist across turns, just like messages.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Managing Long Conversations

    Messages pile up. A 50-turn conversation might have 100+ messages. Three problems:

    1. **Context overflow** — the model hits its token limit and fails
    2. **Lost focus** — models get distracted by stale messages
    3. **Rising costs** — you pay per token, every turn

    Three solutions: trim, summarize, or delete.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Solution 1: Trim Messages

    Use `@before_model` middleware to cut old messages before each model call. The checkpointer keeps the full history — trimming only affects what the model *sees*.

    ```python
    from langchain.messages import RemoveMessage
    from langgraph.graph.message import REMOVE_ALL_MESSAGES
    from langchain.agents import create_agent, AgentState
    from langchain.agents.middleware import before_model
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.runtime import Runtime
    from typing import Any

    @before_model
    def trim_messages(
        state: AgentState, runtime: Runtime
    ) -> dict[str, Any] | None:
        \"\"\"Keep only the last few messages.\"\"\"
        messages = state["messages"]
        if len(messages) <= 3:
            return None  # Nothing to trim

        first_msg = messages[0]
        recent = messages[-3:]
        return {
            "messages": [
                RemoveMessage(id=REMOVE_ALL_MESSAGES),
                first_msg,
                *recent,
            ]
        }

    agent = create_agent(
        llm,
        tools=[],
        middleware=[trim_messages],
        checkpointer=InMemorySaver(),
    )
    ```

    This keeps the first message (often a system message or initial context) plus the three most recent messages.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Solution 2: Summarize Messages

    Trimming drops information. Summarization compresses it instead. The built-in `SummarizationMiddleware` replaces older messages with a summary.

    ```python
    from langchain.agents import create_agent
    from langchain.agents.middleware import SummarizationMiddleware
    from langgraph.checkpoint.memory import InMemorySaver

    agent = create_agent(
        llm,
        tools=[],
        middleware=[
            SummarizationMiddleware(
                model="kimi-k2.5",
                trigger=("tokens", 4000),
                keep=("messages", 20),
            )
        ],
        checkpointer=InMemorySaver(),
    )
    ```

    | Parameter | What it controls |
    |-----------|-----------------|
    | `model` | Which model writes the summary |
    | `trigger` | When to summarize (token count threshold) |
    | `keep` | How many recent messages to preserve as-is |

    The agent still remembers the gist of early conversation, but the token count stays bounded.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Solution 3: Delete Messages

    `RemoveMessage` removes specific messages from state permanently. Unlike trimming (which only affects model input), deletion modifies the stored history.

    ```python
    from langchain.messages import RemoveMessage
    from langchain.agents import AgentState
    from langchain.agents.middleware import after_model
    from langgraph.runtime import Runtime

    @after_model
    def delete_old_messages(
        state: AgentState, runtime: Runtime
    ) -> dict | None:
        \"\"\"Remove the earliest two messages after each model call.\"\"\"
        messages = state["messages"]
        if len(messages) > 2:
            return {
                "messages": [
                    RemoveMessage(id=m.id) for m in messages[:2]
                ]
            }
        return None
    ```

    Be careful: some providers expect message history to start with a `user` message, and `assistant` messages with tool calls must be followed by matching `tool` messages. Deleting the wrong messages breaks the conversation.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Comparing Strategies

    | Strategy | Preserves info? | Token cost | Complexity |
    |----------|----------------|------------|------------|
    | **Trim** | No — drops old messages | Low | Low |
    | **Summarize** | Partially — keeps a summary | Medium (extra LLM call) | Medium |
    | **Delete** | No — permanent removal | Low | Low |

    Start with trimming. Move to summarization if the agent needs to recall earlier context. Use deletion for cleanup tasks (e.g., removing sensitive data after processing).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Accessing State from Tools

    Tools can read and write agent state through the `runtime` parameter.

    **Reading state:**

    ```python
    from langchain.tools import tool, ToolRuntime
    from langchain.agents import AgentState

    class CustomState(AgentState):
        user_id: str

    @tool
    def get_user_info(runtime: ToolRuntime) -> str:
        \"\"\"Look up user info.\"\"\"
        user_id = runtime.state["user_id"]
        return "John Smith" if user_id == "user_123" else "Unknown"
    ```

    The `runtime` parameter is hidden from the model — it won't appear in the tool's schema.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **Writing state from tools:**

    Return a `Command` to update state fields. This persists data for subsequent turns and tool calls.

    ```python
    from langchain.tools import tool, ToolRuntime
    from langchain.messages import ToolMessage
    from langgraph.types import Command

    @tool
    def update_user_info(runtime: ToolRuntime) -> Command:
        \"\"\"Look up and update user info.\"\"\"
        user_id = runtime.context.user_id
        name = "John Smith" if user_id == "user_123" else "Unknown"
        return Command(update={
            "user_name": name,
            "messages": [
                ToolMessage(
                    "Updated user info",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
        })
    ```

    The updated `user_name` is now available to other tools and middleware for the rest of the thread.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Production Checkpointers

    `InMemorySaver` is for development. For production, use a database-backed checkpointer so state survives restarts.

    ```python
    from langgraph.checkpoint.postgres import PostgresSaver

    DB_URI = "postgresql://user:pass@localhost:5432/mydb"
    with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
        checkpointer.setup()  # creates tables if needed
        agent = create_agent(
            llm,
            tools=[get_user_info],
            checkpointer=checkpointer,
        )
    ```

    | Checkpointer | Use case |
    |-------------|----------|
    | `InMemorySaver` | Development, testing |
    | `PostgresSaver` | Production (durable, scalable) |
    | `SqliteSaver` | Single-machine production |

    Install with `pip install langgraph-checkpoint-postgres` or `langgraph-checkpoint-sqlite`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Quick Reference

    ```
    Short-term memory flow:

    invoke(thread_id="1")
      -> Checkpointer loads state
      -> @before_model middleware (trim/summarize)
      -> Model call
      -> @after_model middleware (delete/validate)
      -> Tools run (can read/write state)
      -> Checkpointer saves state
    ```

    | Concept | API |
    |---------|-----|
    | Enable memory | `checkpointer=InMemorySaver()` |
    | Group messages | `{"configurable": {"thread_id": "..."}}` |
    | Custom state | `state_schema=CustomAgentState` |
    | Trim before model | `@before_model` middleware |
    | Summarize history | `SummarizationMiddleware(...)` |
    | Delete messages | `RemoveMessage(id=msg.id)` |
    | Read state in tools | `runtime.state["key"]` |
    | Write state from tools | `Command(update={...})` |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Short-term memory = checkpointer + thread_id.** Add `InMemorySaver` to remember conversations. Extend `AgentState` for custom fields. Manage growing history with trim, summarize, or delete strategies. Tools can read and write state through `runtime`. Use `PostgresSaver` in production.

    **Next:** Lesson 14 — Long-Term Memory
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
