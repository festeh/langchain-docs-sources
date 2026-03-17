import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 6: Models — Multimodal & Advanced

    Reasoning tokens, prompt caching, token tracking, rate limiting, and runtime configuration.
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
    return MODEL, llm


@app.cell
def _(mo):
    mo.md("""
    ## Multimodal Inputs

    Models that support it can accept images, audio, and files as content blocks alongside text. You pass them as a list of content items in the message:

    ```python
    response = llm.invoke([
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "https://example.com/cat.jpg"}},
            ],
        }
    ])
    ```

    Models can also *return* multimodal content. The response's `content_blocks` will include items like `{"type": "image", "base64": "...", "mime_type": "image/jpeg"}`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Reasoning Tokens

    Some models expose their chain-of-thought as reasoning blocks. You can extract them from `content_blocks`:
    """)
    return


@app.cell
def _(ChatOpenAI, mo, os):
    # Use a reasoning model if available
    try:
        reasoning_llm = ChatOpenAI(
            base_url=os.environ["AI_ENDPOINT"] + "/v1",
            api_key=os.environ["AI_KEY"],
            model="claude-opus-4-6-thinking",
        )

        response = reasoning_llm.invoke("What is 17 * 23? Show your thinking.")
        reasoning = [b for b in response.content_blocks if b["type"] == "reasoning"]
        text = [b for b in response.content_blocks if b["type"] == "text"]

        mo.md(f"""
        **Reasoning blocks:** {len(reasoning)}

        **Reasoning:** {reasoning[0]["reasoning"][:300] if reasoning else "N/A"}...

        **Answer:** {text[0]["text"] if text else response.content}
        """)
    except Exception as e:
        mo.md(f"""
        **Reasoning model unavailable:** `{type(e).__name__}`

        Reasoning tokens work the same way — `content_blocks` includes items with `type: "reasoning"`.
        Try with a model that supports it (e.g. `claude-opus-4-6-thinking`, `o1`).
        """)
    return


@app.cell
def _(mo):
    mo.md("""
    Not all models support reasoning tokens. When they do, reasoning blocks appear in `content_blocks` with `type: "reasoning"`. You can stream them too:

    ```python
    for chunk in model.stream("Solve this step by step..."):
        for block in chunk.content_blocks:
            if block["type"] == "reasoning":
                print(block["reasoning"], end="")
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Prompt Caching

    Many providers cache repeated prompt prefixes to reduce latency and cost:

    | Type | How it works | Providers |
    |---|---|---|
    | **Implicit** | Automatic — provider caches behind the scenes | OpenAI, Gemini |
    | **Explicit** | You mark cache points in the prompt | Anthropic, AWS Bedrock |

    Cache hits show up in `response.response_metadata` under usage details (e.g. `cache_read` tokens).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Token Usage Tracking

    Every `AIMessage` includes token counts in `response_metadata`. To track usage across multiple calls, use a callback:
    """)
    return


@app.cell
def _(llm, mo):
    from langchain_core.callbacks import UsageMetadataCallbackHandler

    callback = UsageMetadataCallbackHandler()
    llm.invoke("Hello", config={"callbacks": [callback]})
    llm.invoke("How are you?", config={"callbacks": [callback]})

    mo.md(f"**Aggregate usage across 2 calls:**\n\n```\n{callback.usage_metadata}\n```")
    return


@app.cell
def _(mo):
    mo.md("""
    ## Rate Limiting

    Control how fast you hit a provider's API:

    ```python
    from langchain_core.rate_limiters import InMemoryRateLimiter

    rate_limiter = InMemoryRateLimiter(
        requests_per_second=0.1,  # 1 request every 10s
        check_every_n_seconds=0.1,
        max_bucket_size=10,
    )

    model = ChatOpenAI(..., rate_limiter=rate_limiter)
    ```

    The rate limiter is thread-safe and can be shared across multiple model instances.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Invocation Config

    Pass runtime metadata to any model call via `config`. This is useful for tracing and debugging with LangSmith:
    """)
    return


@app.cell
def _(llm, mo):
    response = llm.invoke(
        "Tell me a joke",
        config={
            "run_name": "joke_generation",
            "tags": ["humor", "demo"],
            "metadata": {"user_id": "42"},
        },
    )
    mo.md(f"**Response:** {response.content}\n\n`run_name`, `tags`, and `metadata` are now visible in LangSmith traces.")
    return


@app.cell
def _(mo):
    mo.md("""
    ## Server-Side Tool Use

    Some providers (OpenAI, Google) can run tools server-side — web search, code interpreters — in a single turn. You bind them the same way, but the model executes them internally:

    ```python
    tool = {"type": "web_search"}
    model_with_tools = llm.bind_tools([tool])

    response = model_with_tools.invoke("Latest news about LangChain?")
    # response.content_blocks includes:
    # - server_tool_call (the search request)
    # - server_tool_result (the search result)
    # - text (the final answer with citations)
    ```

    No `ToolMessage` round-trip needed — it all happens in one call.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Log Probabilities

    Some models can return per-token log probabilities — useful for confidence scoring:

    ```python
    model = llm.bind(logprobs=True)
    response = model.invoke("Why is the sky blue?")
    response.response_metadata["logprobs"]
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Local Models

    Run models on your own hardware with Ollama:

    ```bash
    pip install langchain-ollama
    ```

    ```python
    from langchain_ollama import ChatOllama

    local_llm = ChatOllama(model="llama3")
    local_llm.invoke("Hello from my laptop")
    ```

    Same interface as cloud models — swap in and out freely.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Models go beyond text:** multimodal inputs, reasoning tokens, server-side tools,
    > and log probabilities. Control costs with prompt caching, rate limiting, and token tracking.
    > Same `invoke`/`stream`/`batch` interface for everything — cloud or local.

    **Next:** Lesson 7 — Messages
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
