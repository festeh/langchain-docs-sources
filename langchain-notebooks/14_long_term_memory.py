import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 14: Long-Term Memory

    Store data that survives across conversations.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Short-Term vs Long-Term Memory

    Short-term memory lives inside a single conversation thread. It's the list of messages the model sees during one exchange. When the thread ends, the memory is gone.

    Long-term memory persists across conversations. User preferences, facts, history — anything you want to remember between sessions.

    ```
    Short-term (thread-scoped)          Long-term (cross-conversation)
    ┌─────────────────────┐             ┌─────────────────────┐
    │ Message 1           │             │ user_123:            │
    │ Message 2           │             │   name: Alice        │
    │ Message 3           │             │   lang: Python       │
    │ (gone when done)    │             │   tone: casual       │
    └─────────────────────┘             │ (survives forever)   │
                                        └─────────────────────┘
    ```

    LangGraph stores long-term memories as JSON documents in a **store**.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## InMemoryStore Basics

    `InMemoryStore` is a dictionary-backed store for development. You can use it without an agent — it's a standalone data structure.

    Two concepts to know:

    | Concept | Analogy | Example |
    |---------|---------|---------|
    | **Namespace** | Folder path | `("users",)` or `("users", "prefs")` |
    | **Key** | Filename | `"user_123"` |
    """)
    return


@app.cell
def _(InMemoryStore, mo):
    # Create a store
    store = InMemoryStore()

    # Write data — namespace is a tuple, key is a string
    store.put(
        ("users",),       # namespace (like a folder)
        "user_123",       # key (like a filename)
        {
            "name": "Alice",
            "language": "Python",
            "tone": "casual",
        },
    )

    # Read it back
    item = store.get(("users",), "user_123")

    mo.md(f"""
    **Stored and retrieved:**

    - Namespace: `("users",)`
    - Key: `"user_123"`
    - Value: `{item.value}`
    """)
    return (store,)


@app.cell
def _(mo, store):
    # Store a second user
    store.put(
        ("users",),
        "user_456",
        {
            "name": "Bob",
            "language": "JavaScript",
            "tone": "formal",
        },
    )

    # Retrieve both
    alice = store.get(("users",), "user_123")
    bob = store.get(("users",), "user_456")

    mo.md(f"""
    **Multiple items in the same namespace:**

    | Key | Name | Language |
    |-----|------|----------|
    | `user_123` | {alice.value["name"]} | {alice.value["language"]} |
    | `user_456` | {bob.value["name"]} | {bob.value["language"]} |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Namespace Organization

    Namespaces are tuples that work like folder paths. Use user IDs, org IDs, or application contexts to scope your data.

    ```
    ("users",)                          # all users
    ("users", "prefs")                  # user preferences
    ("org_42", "users")                 # users within an org
    ("user_123", "chitchat")            # one user's chat history
    ```

    Each namespace + key combination is unique. Calling `put` with the same namespace and key overwrites the previous value.
    """)
    return


@app.cell
def _(mo, store):
    # Nested namespaces
    store.put(("user_123", "prefs"), "display", {"theme": "dark", "font_size": 14})
    store.put(("user_123", "prefs"), "notifications", {"email": True, "sms": False})

    display = store.get(("user_123", "prefs"), "display")
    notifs = store.get(("user_123", "prefs"), "notifications")

    mo.md(f"""
    **Nested namespace `("user_123", "prefs")`:**

    - `display`: `{display.value}`
    - `notifications`: `{notifs.value}`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Reading Memory in Tools

    When you connect a store to an agent, tools can read from it through `ToolRuntime`. The runtime gives tools access to the store and a context object (like the current user ID).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ```python
    from dataclasses import dataclass
    from langchain.tools import tool, ToolRuntime

    @dataclass
    class Context:
        user_id: str

    @tool
    def get_user_info(runtime: ToolRuntime[Context]) -> str:
        \"\"\"Look up user info.\"\"\"
        store = runtime.store
        user_id = runtime.context.user_id
        user_info = store.get(("users",), user_id)
        return str(user_info.value) if user_info else "Unknown user"
    ```

    The tool reads from the same store you passed to `create_agent`. No global variables needed — the runtime wires it together.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Writing Memory from Tools

    Tools can also write to the store. This lets agents learn and remember things during conversations.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ```python
    from typing_extensions import TypedDict

    class UserInfo(TypedDict):
        name: str

    @tool
    def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
        \"\"\"Save user info.\"\"\"
        store = runtime.store
        user_id = runtime.context.user_id
        store.put(("users",), user_id, user_info)
        return "Saved."
    ```

    When the user says "My name is Alice," the agent calls `save_user_info` and the data persists for future conversations.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Connecting a Store to an Agent

    Pass `store` and `context_schema` to `create_agent`. The store becomes available to all tools through their `ToolRuntime`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ```python
    from langchain.agents import create_agent
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore()

    agent = create_agent(
        llm,
        tools=[get_user_info, save_user_info],
        store=store,
        context_schema=Context,
    )

    # Run with a user context
    agent.invoke(
        {"messages": [{"role": "user", "content": "Look up my info"}]},
        context=Context(user_id="user_123"),
    )
    ```

    The `context_schema` defines what runtime context your tools expect. Here, every tool gets `user_id` through `runtime.context.user_id`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Searching the Store

    Beyond `get` by exact key, you can search across a namespace with filters and semantic queries.

    ```python
    # Exact filter match
    results = store.search(("users",), filter={"language": "Python"})

    # Semantic search (requires an embedding function in store config)
    results = store.search(("users",), query="prefers short responses")
    ```

    For semantic search, pass an embedding function when creating the store:

    ```python
    store = InMemoryStore(index={"embed": my_embed_fn, "dims": 1536})
    ```

    Filters match on exact field values. Queries rank results by vector similarity.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Production Stores

    `InMemoryStore` is for development — data disappears when the process ends.

    For production, use a database-backed store:

    ```python
    from langgraph.store.postgres import PostgresStore

    store = PostgresStore(connection_string="postgresql://...")
    ```

    The API is identical. Swap `InMemoryStore` for `PostgresStore` and your code works the same way with durable storage.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Long-term memory = store + namespaces + keys.** Use `InMemoryStore` for development, `PostgresStore` for production. Tools read and write through `ToolRuntime`. Scope data with namespaces — user IDs, org IDs, or application contexts. The store persists across conversations so your agent remembers.

    **Next:** Lesson 15
    """)
    return


@app.cell
def _():
    import marimo as mo
    from langgraph.store.memory import InMemoryStore

    return InMemoryStore, mo


if __name__ == "__main__":
    app.run()
