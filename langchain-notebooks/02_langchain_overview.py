import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 2: LangChain Overview

    Build a working agent in under 10 lines. Swap models, add tools, and let the agent loop do the rest.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What LangChain Gives You

    - **Standard model interface** — one API for OpenAI, Anthropic, Google, and dozens more
    - **Tool calling** — give your agent functions, it decides when to call them
    - **Agent loop** — the model reasons, acts, observes, and repeats until done
    - **Built on LangGraph** — durable execution, streaming, and persistence under the hood
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## The Agent Loop

    Every LangChain agent follows this cycle:

    ```
    input ──▶ [ model ] ──action──▶ [ tool ] ──observation──▶ [ model ] ──finish──▶ output
                  ▲                                               │
                  └───────────────────────────────────────────────┘
    ```

    The model picks a tool, reads the result, and decides: call another tool or return a final answer.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Your First Model Call

    Before building an agent, let's call a model directly. This is the simplest thing you can do with LangChain.
    """)
    return


@app.cell
def _(ChatOpenAI, mo, os):
    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model="glm-5",
    )
    response = llm.invoke("What can LangChain do? Answer in one sentence.")
    mo.md(f"**Model says:** {response.content}")
    return (llm,)


@app.cell
def _(mo):
    mo.md("""
    One class, one call. `ChatOpenAI` works with any OpenAI-compatible endpoint.
    LangChain handles message formatting and provider differences for you.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Adding Tools

    Tools are plain Python functions with a docstring. The model reads the docstring to decide when to call each tool.
    """)
    return


@app.cell
def _(llm, mo):
    from langchain_core.tools import tool

    @tool
    def get_weather(city: str) -> str:
        """Get the current weather for a city."""
        return f"It's sunny and 22C in {city}."

    # Bind the tool to the model
    llm_with_tools = llm.bind_tools([get_weather])
    result = llm_with_tools.invoke("What's the weather in Tokyo?")

    # The model returns a tool call, not a text response
    mo.md(f"""
    **Tool calls:** `{result.tool_calls}`

    The model chose to call `get_weather` with `city="Tokyo"` instead of guessing.
    """)
    return (get_weather,)


@app.cell
def _(mo):
    mo.md("""
    ## Building an Agent

    An agent combines a model + tools + a loop. You give it a goal, and it figures out the steps.
    """)
    return


@app.cell
def _(agent_response):
    agent_response
    return


@app.cell
def _(get_weather, llm, mo):
    from langchain.agents import create_agent

    agent = create_agent(llm, tools=[get_weather])

    agent_response = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in Paris and London?"}]}
    )

    # Show the final message
    final = agent_response["messages"][-1]
    mo.md(f"**Agent says:** {final.content}")
    return (agent_response,)


@app.cell
def _(mo):
    mo.md("""
    The agent called `get_weather` twice (once for Paris, once for London), read both results, and composed a final answer. You wrote zero orchestration code.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Three Ways to Call a Model

    | Method | What it does | When to use |
    |---|---|---|
    | `invoke()` | Returns the full response | Most cases |
    | `stream()` | Yields tokens as they arrive | Chat UIs, real-time output |
    | `batch()` | Sends multiple prompts at once | Bulk processing |
    """)
    return


@app.cell
def _(llm, mo):
    # Streaming example
    chunks = []
    for chunk in llm.stream("Count from 1 to 5."):
        chunks.append(chunk.content)

    mo.md(f"**Streamed {len(chunks)} chunks.** Full response: {''.join(chunks)}")
    return (chunks,)


@app.cell
def _(chunks):
    chunks
    return


@app.cell
def _(llm, mo):
    # Batch example — send multiple prompts at once
    responses = llm.batch([
        "Capital of France?",
        "Capital of Japan?",
        "Capital of Brazil?",
    ])
    answers = [r.content for r in responses]
    mo.md(f"**Batch results:** {answers}")
    return


@app.cell
def _(mo):
    mo.md("""
    > **LangChain = model interface + tools + agent loop.**
    > Call models with `invoke`/`stream`/`batch`. Add tools as decorated functions.
    > The agent loop handles reasoning and tool orchestration for you.

    **Next:** Lesson 3 — Installation and Setup
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
