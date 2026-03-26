import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 10: Agents

    Put models, tools, and structured output together — build a system that reasons, acts, and loops until it solves your problem.
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
    ## What Is an Agent?

    An agent is a model that runs tools in a loop. It follows the **ReAct** pattern: reason about what to do, act by calling a tool, observe the result, repeat until done.

    ```
    Input
      → Model reasons, picks a tool
      → Tool runs, returns result
      → Model reasons again (loop)
      → Model produces final answer
    Output
    ```

    `create_agent` builds this loop for you as a LangGraph graph.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Your First Agent

    Define some tools, pass them to `create_agent` with a model, and invoke.
    """)
    return


@app.cell
def _(create_agent, llm, mo, tool):
    @tool
    def get_weather(location: str) -> str:
        """Get current weather for a location."""
        weather_data = {
            "San Francisco": "Foggy, 15C",
            "Tokyo": "Sunny, 28C",
            "London": "Rainy, 12C",
        }
        return weather_data.get(location, f"No data for {location}")

    @tool
    def get_population(city: str) -> str:
        """Get the population of a city."""
        populations = {
            "San Francisco": "870,000",
            "Tokyo": "14,000,000",
            "London": "9,000,000",
        }
        return populations.get(city, f"Unknown population for {city}")

    agent = create_agent(llm, tools=[get_weather, get_population])

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather and population of Tokyo?"}]}
    )

    lines = []
    for msg in result["messages"]:
        role = type(msg).__name__
        if msg.content:
            lines.append(f"**{role}:** {msg.content}")
        elif hasattr(msg, "tool_calls") and msg.tool_calls:
            names = [tc["name"] for tc in msg.tool_calls]
            lines.append(f"**{role}:** calls `{', '.join(names)}`")

    mo.md("\n\n".join(lines))
    return (agent, get_population, get_weather)


@app.cell
def _(mo):
    mo.md("""
    The agent decided which tools to call, called them (possibly in parallel), read the results, and composed a final answer. You wrote zero loop logic.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## System Prompt

    Shape how your agent behaves with `system_prompt`. It's prepended to every model call.
    """)
    return


@app.cell
def _(create_agent, get_weather, llm, mo):
    pirate_agent = create_agent(
        llm,
        tools=[get_weather],
        system_prompt="You are a pirate. Answer in character, but still use tools when needed.",
    )

    pirate_result = pirate_agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in London?"}]}
    )

    final_msg = pirate_result["messages"][-1].content
    mo.md(f"**Agent response:** {final_msg}")
    return


@app.cell
def _(mo):
    mo.md("""
    ## Streaming

    `invoke` waits for the full result. `stream` shows each step as it happens — model reasoning, tool calls, and the final answer.
    """)
    return


@app.cell
def _(agent, mo):
    steps = []
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "What's the population of San Francisco?"}]},
        stream_mode="values",
    ):
        msg = chunk["messages"][-1]
        role = type(msg).__name__
        if msg.content:
            steps.append(f"**{role}:** {msg.content}")
        elif hasattr(msg, "tool_calls") and msg.tool_calls:
            names = [tc["name"] for tc in msg.tool_calls]
            steps.append(f"**{role}:** calls `{', '.join(names)}`")

    mo.md("**Stream steps:**\n\n" + "\n\n".join(steps))
    return


@app.cell
def _(mo):
    mo.md("""
    Each chunk is the full state at that point. You can display tool calls as they happen, show progress, or render partial results.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Structured Output with Agents

    Pass `response_format` to get validated data back instead of free text. The agent handles tool calls first, then returns structured output in `result["structured_response"]`.
    """)
    return


@app.cell
def _(BaseModel, Field, Literal, create_agent, get_weather, llm, mo):
    class WeatherReport(BaseModel):
        """Structured weather report."""
        city: str = Field(description="City name")
        conditions: str = Field(description="Weather conditions")
        temperature_c: int = Field(description="Temperature in Celsius")
        recommendation: str = Field(description="What to wear or bring")
        mood: Literal["great", "okay", "rough"] = Field(
            description="How pleasant the weather is"
        )

    structured_agent = create_agent(
        llm,
        tools=[get_weather],
        response_format=WeatherReport,
    )

    structured_result = structured_agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
    )

    report = structured_result["structured_response"]

    mo.md(f"""
    **Type:** `{type(report).__name__}`

    | Field | Value |
    |-------|-------|
    | `city` | {report.city} |
    | `conditions` | {report.conditions} |
    | `temperature_c` | {report.temperature_c} |
    | `recommendation` | {report.recommendation} |
    | `mood` | {report.mood} |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    The agent called `get_weather` to get real data, then structured its response into a validated `WeatherReport`. The model did the work — you got clean data.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Agent Name

    Give your agent a name with `name`. This becomes the node identifier in multi-agent systems (lesson 28+).

    ```python
    agent = create_agent(
        llm,
        tools=[search, get_weather],
        name="research_assistant",
    )
    ```

    Prefer `snake_case` — some providers reject spaces in names.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## create_agent Reference

    | Parameter | Purpose | Covered in |
    |-----------|---------|------------|
    | `model` | The LLM that reasons and decides | This lesson |
    | `tools` | Functions the agent can call | Lesson 8, this lesson |
    | `system_prompt` | Shapes agent behavior | This lesson |
    | `response_format` | Return structured data | Lesson 9, this lesson |
    | `name` | Agent identifier for multi-agent | This lesson |
    | `middleware` | Intercept model/tool calls | Lesson 23-25 |
    | `state_schema` | Custom state beyond messages | Lesson 13-14 |
    | `context_schema` | Immutable runtime config | Lesson 12 |
    | `store` | Long-term memory | Lesson 14 |

    Under the hood, `create_agent` builds a LangGraph `StateGraph` with a model node, a tool node, and edges that loop between them until the model stops calling tools.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## The ReAct Loop Internalized

    Here's what `create_agent` builds:

    ```
    START → [model] → has tool calls? → yes → [tools] → [model] → ...
                                       → no  → END
    ```

    The model node calls the LLM with bound tools. If the response has `tool_calls`, the tools node executes them and loops back. If not, the agent returns the final message.

    You don't need to build this graph yourself — but knowing the structure helps when you debug agents or add middleware.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Agents = model + tools + loop.** `create_agent` gives you a production-ready ReAct agent. Add `system_prompt` for personality, `response_format` for structured output, and `stream` for visibility. The model decides what to do — you define what it can do.

    **Next:** Lesson 11 — Component Architecture
    """)
    return


@app.cell
def _():
    import os
    from typing import Literal

    import marimo as mo
    from langchain.agents import create_agent
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel, Field

    return (
        BaseModel,
        ChatOpenAI,
        Field,
        Literal,
        create_agent,
        mo,
        os,
        tool,
    )


if __name__ == "__main__":
    app.run()
