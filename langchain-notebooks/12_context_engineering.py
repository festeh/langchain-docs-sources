import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 12: Context Engineering

    Provide the right information so models make the right decisions.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Why Agents Fail

    When an agent takes the wrong action, there are two possible causes:

    1. **The model is not capable enough** — it can't reason through the task
    2. **The wrong context was passed** — it didn't have the information it needed

    Most failures come from reason 2. The model could have solved it — you gave it the wrong inputs.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What Is Context Engineering?

    Context engineering is providing the right information and tools, in the right format, so the model can accomplish a task. This is the core job of anyone building with LLMs.

    It goes beyond prompt engineering. You're not just writing a system prompt — you're controlling what data, tools, and instructions reach the model at each step of the agent loop.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Three Context Types

    Everything you control falls into one of three categories:

    | Context Type | What You Control | Persistence |
    |--------------|------------------|-------------|
    | **Model context** | Instructions, messages, tools, response format | Transient — per model call |
    | **Tool context** | What tools can read and write (state, store, config) | Persistent — survives across calls |
    | **Life-cycle context** | What happens between steps (summarization, guardrails, logging) | Persistent — modifies state |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **Transient** context is what the model sees for a single call. You can reshape messages or swap tools without changing what's saved.

    **Persistent** context is what gets saved across turns. Tool writes and life-cycle hooks modify state permanently.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Three Data Sources

    Your agent reads from and writes to three places:

    | Data Source | Also Known As | Scope | Examples |
    |-------------|---------------|-------|----------|
    | **Runtime Context** | Static config | Conversation-scoped | User ID, API keys, permissions |
    | **State** | Short-term memory | Conversation-scoped | Messages, tool results, uploaded files |
    | **Store** | Long-term memory | Cross-conversation | User preferences, historical data |

    Runtime context is set once at invocation and never changes. State evolves within a conversation. Store persists across conversations.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## How It Works: Middleware

    LangChain middleware is the mechanism that makes context engineering practical. Middleware lets you hook into any step of the agent loop and:

    - Update the context (add instructions, filter tools, inject data)
    - Jump to a different step (skip tool calls, redirect flow)

    ```
    User message
      → [middleware: adjust prompt] → Model call
      → [middleware: filter tools] → Tool execution
      → [middleware: summarize]    → Next model call
      → ...
      → Final answer
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Dynamic System Prompt from State

    A static system prompt treats every turn the same. A dynamic prompt adapts based on the conversation so far.

    Here's a middleware that adjusts the prompt when a conversation gets long:

    ```python
    from langchain.agents import create_agent
    from langchain.agents.middleware import dynamic_prompt, ModelRequest

    @dynamic_prompt
    def state_aware_prompt(request: ModelRequest) -> str:
        message_count = len(request.messages)

        base = "You are a helpful assistant."

        if message_count > 10:
            base += "\\nThis is a long conversation - be extra concise."

        return base

    agent = create_agent(
        model=llm,
        tools=[...],
        middleware=[state_aware_prompt],
    )
    ```

    `request.messages` gives you the current conversation history from state. You read it, decide what the model needs, and return the right prompt.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Dynamic System Prompt from Runtime Context

    Runtime context carries static configuration — user identity, permissions, environment. It's set once when you invoke the agent and stays constant.

    ```python
    from dataclasses import dataclass
    from langchain.agents import create_agent
    from langchain.agents.middleware import dynamic_prompt, ModelRequest

    @dataclass
    class Context:
        user_role: str
        deployment_env: str

    @dynamic_prompt
    def context_aware_prompt(request: ModelRequest) -> str:
        user_role = request.runtime.context.user_role
        env = request.runtime.context.deployment_env

        base = "You are a helpful assistant."

        if user_role == "admin":
            base += "\\nYou have admin access. You can perform all operations."
        elif user_role == "viewer":
            base += "\\nYou have read-only access. Guide users to read operations only."

        if env == "production":
            base += "\\nBe extra careful with any data modifications."

        return base

    agent = create_agent(
        model=llm,
        tools=[...],
        middleware=[context_aware_prompt],
        context_schema=Context,
    )
    ```

    The `context_schema` dataclass defines what runtime context the agent expects. When you invoke the agent, you pass these values in.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Dynamic Tool Selection

    Too many tools overwhelm the model and increase errors. Too few limit what it can do. Dynamic tool selection adapts the available toolset based on state.

    ```python
    from langchain.agents import create_agent
    from langchain.agents.middleware import select_tools, ModelRequest
    from langchain_core.tools import BaseTool

    @select_tools
    def filter_tools_by_auth(
        request: ModelRequest,
        tools: list[BaseTool],
    ) -> list[BaseTool]:
        # Check if user has authenticated in this conversation
        is_authenticated = request.state.get("is_authenticated", False)

        if is_authenticated:
            return tools  # All tools available
        else:
            # Only allow public tools before authentication
            return [t for t in tools if t.name in ("search", "help")]

    agent = create_agent(
        model=llm,
        tools=[search, help, delete_account, transfer_funds],
        middleware=[filter_tools_by_auth],
    )
    ```

    The model only sees tools that match the current state. This reduces errors and enforces security without extra prompt instructions.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Putting It Together

    Here's how the three context types, three data sources, and middleware connect:

    ```
    ┌─────────────────────────────────────────────────────────────┐
    │                     AGENT LOOP                              │
    │                                                             │
    │  ┌──────────────────────────┐                               │
    │  │      Model Context       │  ← dynamic_prompt (state)     │
    │  │  prompt, messages, tools │  ← select_tools (permissions) │
    │  │  response format, model  │  ← wrap_model_call (store)    │
    │  └──────────┬───────────────┘                               │
    │             │                                                │
    │             ▼                                                │
    │  ┌──────────────────────────┐                               │
    │  │      Tool Context        │  ← tools read/write state     │
    │  │  state, store, config    │  ← tools access runtime ctx   │
    │  └──────────┬───────────────┘                               │
    │             │                                                │
    │             ▼                                                │
    │  ┌──────────────────────────┐                               │
    │  │   Life-cycle Context     │  ← summarize long histories   │
    │  │  between-step hooks      │  ← run guardrails             │
    │  └──────────────────────────┘  ← log and audit              │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## A Simple Demo: Context Shapes Output

    You don't need middleware to see context engineering at work. Even changing the system prompt on a plain model call changes behavior. Here's a quick example.
    """)
    return


@app.cell
def _(ChatOpenAI, os):
    MODEL = "kimi-k2.5"

    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model=MODEL,
    )
    return (llm,)


@app.cell
def _(llm, mo):
    question = "What should I eat for dinner?"

    # Same question, two different contexts
    casual_response = llm.invoke([
        {"role": "system", "content": "You are a friendly neighbor. Keep it short."},
        {"role": "user", "content": question},
    ])

    chef_response = llm.invoke([
        {"role": "system", "content": "You are a Michelin-star chef. Keep it short."},
        {"role": "user", "content": question},
    ])

    mo.md(f"""
    **Same question:** "{question}"

    **Casual context** (friendly neighbor):
    > {casual_response.content}

    **Expert context** (Michelin-star chef):
    > {chef_response.content}

    Different context, different output. Context engineering applies this idea at every layer of an agent.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## When to Use Each Data Source

    | Situation | Data Source | Why |
    |-----------|------------|-----|
    | User permissions differ per session | **Runtime Context** | Set once, read everywhere, never changes |
    | Conversation grows too long | **State** | Read message count, summarize or trim |
    | User prefers terse responses | **Store** | Persists across conversations |
    | Tool needs an API key | **Runtime Context** | Static config, not conversation data |
    | Agent should remember past interactions | **Store** | Cross-conversation memory |
    | Agent tracks files uploaded this session | **State** | Conversation-scoped, changes with each upload |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Context engineering = the right info, the right format, the right time.** Three context types (model, tool, life-cycle) draw from three data sources (runtime context, state, store). Middleware is the mechanism that wires them together. Most agent failures aren't model failures — they're context failures. Fix the context, fix the agent.

    **Next:** Lesson 13 — Memory
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
