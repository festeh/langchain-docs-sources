import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 3: Install and Quickstart

    Set up LangChain, then build a real agent with tools, memory, and structured output.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Installation

    ```bash
    uv add langchain langchain-openai
    ```

    That's two packages: `langchain` (the framework) and `langchain-openai` (the provider integration). We route all calls through an OpenAI-compatible endpoint, so `langchain-openai` is all you need.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Minimal Agent

    The smallest useful agent: a model + one tool + `create_agent`.
    """)
    return


@app.cell
def _(ChatOpenAI, os):
    from langchain_core.tools import tool

    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model="glm-5",
    )

    @tool
    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    return get_weather, llm, tool


@app.cell
def _(get_weather, llm, mo):
    from langchain.agents import create_agent

    agent = create_agent(
        llm,
        tools=[get_weather],
        system_prompt="You are a helpful assistant.",
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in SF?"}]}
    )
    mo.md(f"**Agent:** {result['messages'][-1].content}")
    return create_agent, result


@app.cell
def _(result):
    result
    return


@app.cell
def _(mo):
    mo.md("""
    Five lines to create the agent, one to run it. The model saw `get_weather`, called it, read the result, and wrote a response.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## System Prompts

    A system prompt shapes how the agent behaves. Be specific — tell it what tools it has and when to use them.
    """)
    return


@app.cell
def _():
    SYSTEM_PROMPT = """You are an expert weather forecaster who speaks in puns.

    You have two tools:
    - get_weather: get the weather for a specific city
    - get_user_city: get the user's current city

    If the user asks about "the weather" without naming a city, call get_user_city first."""
    return (SYSTEM_PROMPT,)


@app.cell
def _(mo):
    mo.md("""
    ## Tools with Runtime Context

    Tools can access runtime context — data that changes per request, like the current user's ID.
    """)
    return


@app.cell
def _(tool):
    from dataclasses import dataclass
    from langchain.tools import ToolRuntime

    @dataclass
    class Context:
        user_id: str

    @tool
    def get_user_city(runtime: ToolRuntime[Context]) -> str:
        """Get the current user's city based on their profile."""
        cities = {"1": "Paris", "2": "Tokyo", "3": "New York"}
        return cities.get(runtime.context.user_id, "Unknown")

    return Context, dataclass, get_user_city


@app.cell
def _(mo):
    mo.md("""
    `ToolRuntime` injects the context you pass at `invoke()` time. The model never sees raw user IDs — it calls the tool and gets back a city name.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Structured Output

    Force the agent to return data in a specific shape. Define a dataclass (or Pydantic model) and wrap it in `ToolStrategy`.

    `ToolStrategy` works by creating a hidden tool from your schema. When the agent is ready to respond, it "calls" this tool — which forces the output to match your dataclass fields exactly. The result lands in `response['structured_response']`.
    """)
    return


@app.cell
def _(dataclass):
    @dataclass
    class WeatherReport:
        """Structured weather report."""
        summary: str
        conditions: str | None = None

    return (WeatherReport,)


@app.cell
def _(mo):
    mo.md("""
    ## Memory

    Add a checkpointer so the agent remembers previous messages in the same thread.
    """)
    return


@app.cell
def _():
    from langgraph.checkpoint.memory import InMemorySaver

    checkpointer = InMemorySaver()
    return (checkpointer,)


@app.cell
def _(mo):
    mo.md("""
    `InMemorySaver` keeps state in RAM — fine for experiments. In production, swap it for a database-backed checkpointer (Postgres, SQLite).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### How thread memory works

    Memory is keyed by `thread_id` — a string you pass in the config. Think of it like a chat session ID.

    - **Same `thread_id`** = same conversation. Each `invoke()` appends your new message and the agent's response to the existing thread. The agent sees the full history.
    - **Different `thread_id`** = fresh start, no shared history.

    ```python
    config = {"configurable": {"thread_id": "user-42-chat-1"}}
    agent.invoke({"messages": [...]}, config=config)  # first exchange
    agent.invoke({"messages": [...]}, config=config)  # appended to same thread
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Inspecting memory

    Since LangChain agents are LangGraph graphs, you can call `get_state()` to see the full conversation state at any point:

    ```python
    state = agent.get_state(config)
    state.values["messages"]  # all messages in this thread
    ```

    You can also walk through the history with `get_state_history()`:

    ```python
    for snapshot in agent.get_state_history(config):
        print(len(snapshot.values["messages"]), "messages")
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Putting It All Together

    Combine system prompt + tools + structured output + memory into one agent.
    """)
    return


@app.cell
def _(
    Context,
    SYSTEM_PROMPT,
    WeatherReport,
    checkpointer,
    create_agent,
    get_user_city,
    get_weather,
    llm,
    mo,
):
    from langchain.agents.structured_output import ToolStrategy

    full_agent = create_agent(
        llm,
        system_prompt=SYSTEM_PROMPT,
        tools=[get_weather, get_user_city],
        context_schema=Context,
        response_format=ToolStrategy(WeatherReport),
        checkpointer=checkpointer,
    )

    # thread_id groups messages into a conversation
    config = {"configurable": {"thread_id": "demo-1"}}

    response = full_agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather where I am?"}]},
        config=config,
        context=Context(user_id="1"),
    )

    mo.md(f"""
    **Structured response:**
    - `summary`: {response['structured_response'].summary}
    - `conditions`: {response['structured_response'].conditions}
    """)
    return config, full_agent


@app.cell
def _(mo):
    mo.md("""
    The agent called `get_user_city` (got "Paris"), then `get_weather` (got the forecast), then packed everything into a `WeatherReport`.
    """)
    return


@app.cell
def _(Context, config, full_agent, mo):
    # Continue the same conversation — the agent remembers the first exchange
    response2 = full_agent.invoke(
        {"messages": [{"role": "user", "content": "What about Tokyo?"}]},
        config=config,
        context=Context(user_id="1"),
    )

    mo.md(f"""
    **Follow-up (same thread):**
    - `summary`: {response2['structured_response'].summary}
    - `conditions`: {response2['structured_response'].conditions}

    The agent remembered we were talking about weather and went straight to `get_weather("Tokyo")`.
    """)
    return


@app.cell
def _(config, full_agent, mo):
    # Inspect the full conversation state
    state = full_agent.get_state(config)
    msgs = state.values["messages"]

    summary = "\n".join(
        f"- **{m.type}**: {m.content[:120]}{'...' if len(m.content) > 120 else ''}"
        for m in msgs
        if m.content
    )
    mo.md(f"""
    ### Memory Inspection

    `get_state(config)` returns all {len(msgs)} messages in this thread:

    {summary}
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Install:** `uv add langchain langchain-openai`. That's it.
    > **Build agents with:** `create_agent(model, tools=[], system_prompt="...")`.
    > **Add structure** with `response_format`, **add memory** with a checkpointer,
    > and **pass per-request data** through `context`.

    **Next:** Lesson 4 — Philosophy
    """)
    return


@app.cell
def _():
    import os
    import marimo as mo
    from langchain_openai import ChatOpenAI

    return ChatOpenAI, mo, os


if __name__ == "__main__":
    app.run()
