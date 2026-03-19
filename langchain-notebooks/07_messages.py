import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 7: Messages

    The units of conversation — how LangChain represents what you say, what the model says back, and everything in between.
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
    return MODEL, llm


@app.cell
def _(mo):
    mo.md("""
    ## What's in a Message?

    Every message has three parts:

    | Part | What it carries |
    |------|----------------|
    | **Role** | Who sent it — `system`, `user` (human), `assistant` (AI), or `tool` |
    | **Content** | The payload — text, images, audio, tool calls |
    | **Metadata** | Token counts, response info, message IDs |

    LangChain wraps all of this into four message classes: `SystemMessage`, `HumanMessage`, `AIMessage`, and `ToolMessage`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Three Ways to Pass Messages

    You can give a model its input as a plain string, as message objects, or as dictionaries. All three produce the same result.
    """)
    return


@app.cell
def _(HumanMessage, SystemMessage, llm, mo):
    # 1. Plain string — shortcut for a single HumanMessage
    r1 = llm.invoke("What is 2 + 2?")

    # 2. Message objects — full control over roles
    r2 = llm.invoke([
        SystemMessage("Answer in one word."),
        HumanMessage("What is 2 + 2?"),
    ])

    # 3. Dictionary format — OpenAI-compatible
    r3 = llm.invoke([
        {"role": "system", "content": "Answer in one word."},
        {"role": "user", "content": "What is 2 + 2?"},
    ])

    mo.md(f"""
    | Format | Response |
    |--------|----------|
    | String | {r1.content} |
    | Message objects | {r2.content} |
    | Dictionaries | {r3.content} |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **When to use each:**

    - **String** — one-off questions, no conversation history needed
    - **Message objects** — multi-turn conversations, full type safety
    - **Dictionaries** — when you already have OpenAI-format data (e.g. from a database)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Message Types

    ### SystemMessage

    Sets the model's behavior. Goes first in the message list.
    """)
    return


@app.cell
def _(HumanMessage, SystemMessage, llm, mo):
    pirate = llm.invoke([
        SystemMessage("You are a pirate. Answer in one sentence, in character."),
        HumanMessage("What's the weather like?"),
    ])
    mo.md(f"**Pirate response:** {pirate.content}")
    return


@app.cell
def _(mo):
    mo.md("""
    ### HumanMessage

    Represents what the user says. Supports text, and optionally `name` and `id` metadata:

    ```python
    human_msg = HumanMessage(
        content="Hello!",
        name="alice",    # identify different users
        id="msg_123",    # unique ID for tracing
    )
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### AIMessage

    What the model returns. This is where all the interesting metadata lives.
    """)
    return


@app.cell
def _(llm, mo):
    response = llm.invoke("Tell me a one-sentence fun fact.")

    mo.md(f"""
    **Content:** {response.content}

    **Type:** `{type(response).__name__}`

    **Key attributes:**

    | Attribute | Value |
    |-----------|-------|
    | `.content` | The raw response (string or list of blocks) |
    | `.text` | Text-only content |
    | `.usage_metadata` | `{response.usage_metadata}` |
    | `.response_metadata` | `{dict(list(response.response_metadata.items())[:3])}...` |
    | `.id` | `{response.id}` |
    """)
    return (response,)


@app.cell
def _(mo):
    mo.md("""
    ### AIMessage in Conversation History

    You can create `AIMessage` objects manually to seed a conversation with fake history. The model treats them as if it said those things:
    """)
    return


@app.cell
def _(AIMessage, HumanMessage, SystemMessage, llm, mo):
    conversation = [
        SystemMessage("You are a math tutor."),
        HumanMessage("What is 10 * 5?"),
        AIMessage("10 * 5 = 50"),  # fake prior response
        HumanMessage("Now divide that by 2"),
    ]
    follow_up = llm.invoke(conversation)
    mo.md(f"**Follow-up:** {follow_up.content}")
    return


@app.cell
def _(mo):
    mo.md("""
    ### ToolMessage

    Passes tool execution results back to the model. Every `ToolMessage` must reference the `tool_call_id` from the `AIMessage` that triggered it.
    """)
    return


@app.cell
def _(AIMessage, HumanMessage, ToolMessage, llm, mo):
    # Simulate the full tool-call cycle:
    # 1. Model requests a tool call (we construct this manually)
    ai_with_tool_call = AIMessage(
        content="",
        tool_calls=[{
            "name": "get_weather",
            "args": {"location": "Paris"},
            "id": "call_abc123",
        }],
    )

    # 2. We "execute" the tool and send the result back
    tool_result = ToolMessage(
        content="Sunny, 22C",
        tool_call_id="call_abc123",
    )

    # 3. Model gets the full history and produces a final answer
    messages = [
        HumanMessage("What's the weather in Paris?"),
        ai_with_tool_call,
        tool_result,
    ]
    final = llm.invoke(messages)

    mo.md(f"""
    **Tool call flow:**

    ```
    Human: "What's the weather in Paris?"
        -> AI requests tool: get_weather(location="Paris")
        -> Tool returns: "Sunny, 22C"
        -> AI final answer: "{final.content}"
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    The `artifact` field on `ToolMessage` stores extra data (document IDs, metadata) that your app can use but that won't be sent to the model:

    ```python
    tool_msg = ToolMessage(
        content="It was the best of times...",
        tool_call_id="call_123",
        name="search_books",
        artifact={"document_id": "doc_456", "page": 0},
    )
    # tool_msg.artifact -> {"document_id": "doc_456", "page": 0}
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Content Blocks

    Message `.content` can be a string or a list of typed blocks. The `.content_blocks` property gives you a standardized view that works the same across providers.
    """)
    return


@app.cell
def _(llm, mo):
    ai_response = llm.invoke("What is Python?")

    mo.md(f"""
    **`.content` (raw):**
    ```
    {repr(ai_response.content)[:200]}
    ```

    **`.content_blocks` (standardized):**
    ```
    {ai_response.content_blocks}
    ```

    Each block has a `type` field. The most common is `"text"`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Content Block Reference

    | Category | Block type | `type` value | Purpose |
    |----------|-----------|-------------|---------|
    | **Core** | TextContentBlock | `"text"` | Standard text output |
    | | ReasoningContentBlock | `"reasoning"` | Model chain-of-thought |
    | **Multimodal** | ImageContentBlock | `"image"` | Image data (URL, base64, or file ID) |
    | | AudioContentBlock | `"audio"` | Audio data |
    | | VideoContentBlock | `"video"` | Video data |
    | | FileContentBlock | `"file"` | Generic files (PDF, etc.) |
    | | PlainTextContentBlock | `"text-plain"` | Document text (.txt, .md) |
    | **Tool calling** | ToolCall | `"tool_call"` | Function call request |
    | | ToolCallChunk | `"tool_call_chunk"` | Streaming tool call fragment |
    | | InvalidToolCall | `"invalid_tool_call"` | Malformed call (JSON parse error) |
    | **Server-side** | ServerToolCall | `"server_tool_call"` | Provider-executed tool |
    | | ServerToolResult | `"server_tool_result"` | Provider-executed tool result |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Multimodal Content

    Pass images, audio, video, or files as content blocks in a `HumanMessage`. Three ways to reference media:

    ```python
    # From URL
    {"type": "image", "url": "https://example.com/cat.jpg"}

    # From base64
    {"type": "image", "base64": "...", "mime_type": "image/jpeg"}

    # From provider file ID
    {"type": "image", "file_id": "file-abc123"}
    ```

    Works the same for `"audio"`, `"video"`, and `"file"` blocks — swap the type and mime_type.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Streaming with AIMessageChunk

    When you stream, each piece arrives as an `AIMessageChunk`. You can combine them with `+` to build the full message:
    """)
    return


@app.cell
def _(llm, mo):
    chunks = []
    full = None
    for chunk in llm.stream("Name three colors."):
        chunks.append(chunk)
        full = chunk if full is None else full + chunk

    mo.md(f"""
    **Chunks received:** {len(chunks)}

    **First chunk type:** `{type(chunks[0]).__name__}`

    **Combined result:** {full.content}

    **Usage (from combined):** `{full.usage_metadata}`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Messages are the language models speak.** Four types — System, Human, AI, Tool — cover every part of a conversation.
    > Use `.content_blocks` for a provider-independent view. Use `.usage_metadata` for token tracking.
    > The tool-call cycle (AIMessage with tool_calls -> ToolMessage with result) is the foundation for agents.

    **Next:** Lesson 8 — Tools
    """)
    return


@app.cell
def _():
    import os
    import marimo as mo
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import (
        AIMessage,
        HumanMessage,
        SystemMessage,
        ToolMessage,
    )
    return AIMessage, ChatOpenAI, HumanMessage, SystemMessage, ToolMessage, mo, os


if __name__ == "__main__":
    app.run()
