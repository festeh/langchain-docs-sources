import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 8: Tools

    Give your model hands — let it fetch data, run calculations, and take actions beyond generating text.
    """)
    return


@app.cell
def _(ChatOpenAI, os):
    MODEL = "glm-5"

    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model=MODEL,
    )
    return (llm,)


@app.cell
def _(mo):
    mo.md("""
    ## What Are Tools?

    Tools are functions the model can call. You define the function — the model decides when to use it and what arguments to pass.

    The model sees a tool's name, description, and input schema. It never runs the function itself — it asks *you* to run it and pass the result back.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Create a Tool

    The `@tool` decorator turns a function into a tool. Type hints define the input schema. The docstring becomes the description the model reads.
    """)
    return


@app.cell
def _(mo, tool):
    @tool
    def search_database(query: str, limit: int = 10) -> str:
        """Search the customer database for records matching the query.

        Args:
            query: Search terms to look for
            limit: Maximum number of results to return
        """
        return f"Found {limit} results for '{query}'"

    mo.md(f"""
    | Property | Value |
    |----------|-------|
    | **Name** | `{search_database.name}` |
    | **Description** | {search_database.description} |
    | **Args** | `{search_database.args}` |

    Type hints are required — they tell the model what to pass in.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Customize Name and Description

    Override defaults when you need a clearer tool name or a more specific description for the model.
    """)
    return


@app.cell
def _(mo, tool):
    @tool("web_search", description="Search the web for current information. Use for questions about recent events.")
    def search(query: str) -> str:
        """Search the web."""
        return f"Results for: {query}"

    mo.md(f"""
    | Property | Value |
    |----------|-------|
    | **Name** | `{search.name}` (overrides function name `search`) |
    | **Description** | {search.description} |

    Prefer `snake_case` for tool names — some providers reject spaces or special characters.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Complex Inputs with Pydantic

    For tools with many parameters or constraints, define the schema as a Pydantic model. Each field gets its own description the model can read.
    """)
    return


@app.cell
def _(BaseModel, Field, Literal, mo, tool):
    class WeatherInput(BaseModel):
        """Input for weather queries."""
        location: str = Field(description="City name or coordinates")
        units: Literal["celsius", "fahrenheit"] = Field(
            default="celsius",
            description="Temperature unit preference"
        )

    @tool(args_schema=WeatherInput)
    def get_weather(location: str, units: str = "celsius") -> str:
        """Get current weather for a location."""
        temp = 22 if units == "celsius" else 72
        return f"{location}: {temp} {'C' if units == 'celsius' else 'F'}, sunny"

    mo.md(f"""
    **Tool:** `{get_weather.name}` — {get_weather.description}

    **Schema:** `{get_weather.args}`

    Each field's `description` helps the model understand what to pass.
    """)
    return (get_weather,)


@app.cell
def _(mo):
    mo.md("""
    ## The Tool Call Cycle

    This is the core loop every tool-using agent runs:

    ```
    You ask a question
      → Model picks a tool and fills in arguments
      → You execute the tool
      → You pass the result back as a ToolMessage
      → Model writes a final response
    ```

    Use `.bind_tools()` to tell the model which tools are available.
    """)
    return


@app.cell
def _(HumanMessage, ToolMessage, get_weather, llm, mo):
    # Step 1: Bind tools and ask a question
    llm_with_tools = llm.bind_tools([get_weather])
    question = "What's the weather in Paris?"
    ai_msg = llm_with_tools.invoke(question)
    tool_call = ai_msg.tool_calls[0]

    # Step 2: Execute the tool with the model's chosen arguments
    tool_result = get_weather.invoke(tool_call["args"])

    # Step 3: Pass everything back for the final response
    final = llm_with_tools.invoke([
        HumanMessage(question),
        ai_msg,
        ToolMessage(content=tool_result, tool_call_id=tool_call["id"]),
    ])

    mo.md(f"""
    ```
    You:    "{question}"
    Model:  calls {tool_call["name"]}({tool_call["args"]})
    Tool:   "{tool_result}"
    Model:  "{final.content}"
    ```

    The model never ran `get_weather` — it told us to, we did, and we passed the result back.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Multiple Tools

    Bind several tools — the model picks the right one based on the question. If none fit, it responds with plain text.
    """)
    return


@app.cell
def _(llm, mo, tool):
    @tool
    def calculate(expression: str) -> str:
        """Evaluate a math expression. Use for arithmetic questions."""
        return str(eval(expression))

    @tool
    def lookup_capital(country: str) -> str:
        """Look up the capital city of a country."""
        capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
        return capitals.get(country, f"Unknown capital for {country}")

    multi_llm = llm.bind_tools([calculate, lookup_capital])

    questions = [
        ("Math", "What is 15 * 7 + 3?"),
        ("Geography", "What's the capital of Japan?"),
        ("Chat", "Hello, how are you?"),
    ]

    rows = []
    for label, q in questions:
        r = multi_llm.invoke(q)
        if r.tool_calls:
            tc = r.tool_calls[0]
            picked = f"`{tc['name']}({tc['args']})`"
        else:
            picked = "No tool — plain text response"
        rows.append(f"| {label} | {q} | {picked} |")

    mo.md(f"""
    | Type | Question | Model's choice |
    |------|----------|---------------|
    {chr(10).join(rows)}

    The model reads each tool's description and picks the best match.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Return Values

    Tools can return different types. The model reads the result either way.
    """)
    return


@app.cell
def _(mo, tool):
    @tool
    def get_price_text(ticker: str) -> str:
        """Get stock price as text."""
        return f"{ticker}: $142.50, up 2.3%"

    @tool
    def get_price_data(ticker: str) -> dict:
        """Get stock price as structured data."""
        return {"ticker": ticker, "price": 142.50, "change_pct": 2.3}

    text_result = get_price_text.invoke({"ticker": "ACME"})
    dict_result = get_price_data.invoke({"ticker": "ACME"})

    mo.md(f"""
    | Return type | Result | When to use |
    |-------------|--------|-------------|
    | **String** | `{text_result}` | Simple, human-readable output |
    | **Dict** | `{dict_result}` | Structured data the model should parse |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Tools can also return a `Command` to update agent state — setting user preferences, language, or custom fields. This requires an agent execution context (lesson 10).

    ```python
    from langgraph.types import Command
    from langchain.tools import tool, ToolRuntime

    @tool
    def set_language(language: str, runtime: ToolRuntime) -> Command:
        \"\"\"Set the preferred response language.\"\"\"
        return Command(update={"preferred_language": language})
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## ToolRuntime

    Tools get more powerful when they access conversation state, user identity, or persistent memory. Add `runtime: ToolRuntime` to your signature — it's injected automatically and hidden from the model's schema.

    | Component | What it holds | Example |
    |-----------|--------------|---------|
    | `runtime.state` | Messages and custom fields for this conversation | Read message history |
    | `runtime.context` | Immutable config passed at invocation (user ID, session) | Personalize responses |
    | `runtime.store` | Persistent storage across conversations | Save user preferences |
    | `runtime.stream_writer` | Emit real-time progress updates | Show "searching..." status |
    | `runtime.tool_call_id` | Unique ID for this invocation | Correlate logs, build ToolMessages |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ```python
    from langchain.tools import tool, ToolRuntime

    @tool
    def smart_search(query: str, runtime: ToolRuntime) -> str:
        \"\"\"Search with conversation context.\"\"\"
        msg_count = len(runtime.state["messages"])
        user_id = runtime.context.user_id
        return f"User {user_id}: found results for '{query}' ({msg_count} messages)"
    ```

    `ToolRuntime` requires an agent execution context — we'll use it hands-on in lesson 10.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Reserved Argument Names

    Two parameter names are reserved — using them as tool arguments causes a runtime error:

    | Name | Reserved for |
    |------|-------------|
    | `config` | Internal `RunnableConfig` |
    | `runtime` | `ToolRuntime` injection |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Prebuilt Tools

    LangChain ships ready-made tools for web search, code execution, database access, and more. Some model providers also offer **server-side tools** (like built-in web search) that run on the provider's infrastructure — no tool definition needed.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Tools let models act, not just talk.** Define them with `@tool`, bind them with `.bind_tools()`, and run the cycle: model requests, you execute, you pass back. Use Pydantic for complex inputs. Use `ToolRuntime` for state-aware tools.

    **Next:** Lesson 9 — Structured Output
    """)
    return


@app.cell
def _():
    import os
    from typing import Literal

    import marimo as mo
    from langchain_core.tools import tool
    from langchain_core.messages import HumanMessage, ToolMessage
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel, Field

    return (
        BaseModel,
        ChatOpenAI,
        Field,
        HumanMessage,
        Literal,
        ToolMessage,
        mo,
        os,
        tool,
    )


if __name__ == "__main__":
    app.run()
