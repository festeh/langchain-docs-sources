import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 5: Models

    The model is the reasoning engine. Configure it, call it three ways, and control its output.
    """)
    return


@app.cell
def _(ChatOpenAI, os):
    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model="kimi-k2.5",
    )
    return (llm,)


@app.cell
def _(mo):
    mo.md("""
    ## Parameters

    Every model accepts these standard parameters:

    | Parameter | What it does |
    |---|---|
    | `model` | Which model to use (`"glm-5"`, `"gpt-4"`, etc.) |
    | `api_key` | Authentication key |
    | `temperature` | Higher = more creative, lower = more deterministic |
    | `max_tokens` | Cap on response length |
    | `timeout` | Seconds before giving up |
    | `max_retries` | Auto-retry on network errors / rate limits (default: 6) |
    """)
    return


@app.cell
def _(ChatOpenAI, mo, os):
    # Temperature comparison
    cold = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model="glm-5",
        temperature=0.0,
    )
    hot = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model="glm-5",
        temperature=1.5,
    )

    prompt = "Name a random color."
    cold_response = cold.invoke(prompt)
    hot_response = hot.invoke(prompt)

    mo.md(f"""
    **temperature=0.0:** {cold_response.content}

    **temperature=1.5:** {hot_response.content}

    Low temperature → consistent answers. High temperature → more variety.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Invoke — Full Response

    The simplest call. Send a message (or list of messages), get back an `AIMessage`.
    """)
    return


@app.cell
def _(llm, mo):
    # Single string
    r1 = llm.invoke("What is 2 + 2?")
    mo.md(f"**String input:** {r1.content}")
    return


@app.cell
def _(llm, mo):
    # Conversation history as a list of messages
    conversation = [
        {"role": "system", "content": "You translate English to French."},
        {"role": "user", "content": "I love programming."},
        {"role": "assistant", "content": "J'adore la programmation."},
        {"role": "user", "content": "I love building agents."},
    ]
    r2 = llm.invoke(conversation)
    mo.md(f"**Conversation input:** {r2.content}")
    return


@app.cell
def _(mo):
    mo.md("""
    You can pass a plain string or a list of message dicts with `role` and `content`. The list form lets you include system prompts and conversation history.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Stream — Token by Token

    `stream()` yields chunks as the model generates them. Use this for chat UIs or any place where you want to show output progressively.
    """)
    return


@app.cell
def _(llm, mo):
    chunks = []
    for chunk in llm.stream("Write a haiku about code."):
        chunks.append(chunk.content)

    mo.md(f"**{len(chunks)} chunks streamed.** Result:\n\n{' '.join(chunks)}")
    return


@app.cell
def _(mo):
    mo.md("""
    Each chunk is an `AIMessageChunk`. You can sum them to reconstruct the full `AIMessage`:

    ```python
    full = None
    for chunk in model.stream("Hello"):
        full = chunk if full is None else full + chunk
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Batch — Parallel Calls

    `batch()` sends multiple prompts concurrently. Three prompts finish in roughly the time of one.
    """)
    return


@app.cell
def _(llm, mo):
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
    For large batches, control concurrency:

    ```python
    model.batch(prompts, config={"max_concurrency": 5})
    ```

    `batch_as_completed()` yields results as they finish (possibly out of order).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What Models Can Do

    Beyond text generation, models support:

    | Capability | What it means |
    |---|---|
    | **Tool calling** | Model decides which functions to call and with what arguments |
    | **Structured output** | Force responses into a specific schema (JSON, dataclass, Pydantic) |
    | **Multimodal** | Accept images, audio, video, files as input |
    | **Reasoning** | Multi-step thinking before answering (chain-of-thought) |

    We'll cover tools and structured output in the next lessons.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## The AIMessage Object

    Every model call returns an `AIMessage`. Here's what's inside:
    """)
    return


@app.cell
def _(llm, mo):
    msg = llm.invoke("Say hello.")
    mo.md(f"""
    | Attribute | Value |
    |---|---|
    | `content` | `{msg.content}` |
    | `response_metadata` | token usage, model name, finish reason |
    | `id` | `{msg.id}` |
    | `tool_calls` | `{msg.tool_calls}` (empty — no tools bound) |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Three ways to call a model:** `invoke()` for full responses, `stream()` for progressive output,
    > `batch()` for parallel calls. Control behavior with `temperature`, `max_tokens`, and `timeout`.
    > The same interface works standalone or inside an agent.

    **Next:** Lesson 6 — Messages
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
