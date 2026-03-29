import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 16: Memory Concepts

    Semantic, episodic, and procedural memory for AI agents.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Two Types by Scope

    Memory splits into two categories based on how far it reaches.

    | Type | Scope | What it stores | Managed by |
    |------|-------|----------------|------------|
    | **Short-term** | Single thread (one conversation) | Message history, state | Checkpointer |
    | **Long-term** | Cross-conversation | User prefs, facts, rules | Store |

    Short-term memory lives inside a thread. Long-term memory lives outside it.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Short-Term Memory

    Short-term memory tracks the current conversation. LangGraph persists it as part of the agent's state using a checkpointer, so threads can be paused and resumed.

    The challenge: long conversations overflow the context window. Three ways to handle it:

    - **Trim** old messages
    - **Summarize** the conversation so far
    - **Delete** stale or irrelevant messages

    We covered these hands-on in lesson 13.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Long-Term Memory

    Long-term memory stores information *across* conversations. It lives in a Store, scoped to custom namespaces (not thread IDs).

    Three types, borrowed from human psychology:

    | Type | What is stored | Human example | Agent example |
    |------|---------------|---------------|---------------|
    | **Semantic** | Facts | Things learned in school | Facts about a user |
    | **Episodic** | Experiences | Things I did | Past agent actions (few-shot examples) |
    | **Procedural** | Instructions | Motor skills, instincts | Agent system prompt |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Semantic Memory

    Semantic memory stores facts — things the agent knows about users, organizations, or itself. Two storage patterns exist.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Profile Pattern

    Store a single JSON document per entity. Update the whole document each time new information arrives.

    ```
    ┌──────────────────────────────────┐
    │  User Profile (JSON)             │
    │  ────────────────────────────    │
    │  name: "Alice"                   │
    │  language: "Python"              │
    │  prefers: "short responses"      │
    │  timezone: "US/Pacific"          │
    └──────────────────────────────────┘
            ↑ overwrite on each update
    ```

    **Upside:** One place to look. Easy to pass to the model.
    **Risk:** Large updates can lose information. The model must reconcile new facts with the existing profile every time.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Collection Pattern

    Store many small documents. Add new ones as facts arrive. Update or delete individual entries.

    ```
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │ Memory #1    │ │ Memory #2    │ │ Memory #3    │
    │ Likes Python │ │ US/Pacific   │ │ Short replies│
    └──────────────┘ └──────────────┘ └──────────────┘
          ↑ add/update/delete individually
    ```

    **Upside:** Higher recall. Less risk of losing info on updates.
    **Downside:** Harder to search, harder to update, and individual memories may lack context about relationships between facts.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Episodic Memory

    Episodic memory stores *experiences* — what the agent did in the past and what happened. In practice, this means few-shot examples.

    Sometimes it's easier to show than tell. The agent retrieves relevant past interactions and includes them in the prompt, so the model learns from its own history.

    ```
    New user request
         │
         ▼
    Search episodic memory for similar past tasks
         │
         ▼
    Include matching examples in prompt
         │
         ▼
    Model learns from its own past successes
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Procedural Memory

    Procedural memory stores *rules and instructions* — the agent's system prompt. Unlike semantic and episodic memory, procedural memory defines *how* the agent behaves, not *what* it knows.

    The interesting part: procedural memory can be self-updating. The agent reflects on conversations and rewrites its own instructions.

    ```
    Conversation with user
         │
         ▼
    Agent reflects on what went well / poorly
         │
         ▼
    Agent rewrites its own system prompt
         │
         ▼
    Future conversations use the updated instructions
    ```

    This is useful when the right instructions are hard to write upfront but easy to refine through feedback.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Writing Memories

    Two approaches for *when* the agent creates memories.

    | Approach | When it runs | Upside | Downside |
    |----------|-------------|--------|----------|
    | **Hot path** | During the conversation | Memories available immediately | Adds latency; agent multitasks |
    | **Background** | After the conversation ends | No latency impact | Delayed availability |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Hot Path

    The agent writes memories in real time, as part of the conversation flow. New memories are available for the very next message.

    ```
    User message → Agent reasons → Writes memory → Responds
    ```

    The cost: the agent must decide what to remember *while* also doing its main job. This adds latency and complexity (often via a dedicated `save_memory` tool).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Background

    A separate process creates memories after the conversation finishes (or on a schedule). The main agent never slows down.

    ```
    User message → Agent responds (fast)
                        │
                        └──→ Background job creates memories later
    ```

    The cost: other threads won't see the new memories until the background job runs. You need to decide *how often* to trigger it — after every conversation, on a cron schedule, or manually.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Putting It Together

    ```
    ┌─────────────────────────────────────────────────────────────┐
    │                        MEMORY                               │
    │                                                             │
    │  SHORT-TERM (thread-scoped)                                 │
    │  ┌────────────────────────────────────────────┐             │
    │  │  Message history + state                   │             │
    │  │  Managed by: Checkpointer                  │             │
    │  │  Techniques: trim, summarize, delete       │             │
    │  └────────────────────────────────────────────┘             │
    │                                                             │
    │  LONG-TERM (cross-conversation)                             │
    │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
    │  │  Semantic    │ │  Episodic    │ │  Procedural  │        │
    │  │  (facts)     │ │  (examples)  │ │  (rules)     │        │
    │  │  Profile or  │ │  Few-shot    │ │  System      │        │
    │  │  Collection  │ │  retrieval   │ │  prompt      │        │
    │  └──────────────┘ └──────────────┘ └──────────────┘        │
    │  Managed by: Store                                          │
    │  Written: hot path or background                            │
    └─────────────────────────────────────────────────────────────┘
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Memory gives agents continuity.** Short-term memory (checkpointer) tracks the current conversation. Long-term memory (store) persists across conversations in three flavors: semantic (facts), episodic (examples), and procedural (rules). Write memories on the hot path for immediacy, or in the background for speed.

    **Next:** Lesson 17 -- Retrieval
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
