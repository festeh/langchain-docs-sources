import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 11: Component Architecture

    Step back and see how all the pieces fit together — models, tools, agents, memory, retrieval, and more.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## The Big Picture

    LangChain organizes into five layers. Each builds on the one below it.

    ```
    ┌─────────────────────────────────────────────┐
    │              5. ORCHESTRATION                │
    │     Agents  ·  Multi-agent  ·  Middleware    │
    ├─────────────────────────────────────────────┤
    │              4. GENERATION                   │
    │     Chat models  ·  Tools  ·  Structured out │
    ├─────────────────────────────────────────────┤
    │              3. RETRIEVAL                     │
    │     Retrievers  ·  Vector stores  ·  Search  │
    ├─────────────────────────────────────────────┤
    │           2. EMBEDDING & STORAGE             │
    │     Embedding models  ·  Vector stores       │
    ├─────────────────────────────────────────────┤
    │           1. INPUT PROCESSING                │
    │     Document loaders  ·  Text splitters      │
    └─────────────────────────────────────────────┘
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Component Categories

    | Category | Purpose | What you'll use |
    |----------|---------|-----------------|
    | **Models** | Reasoning and generation | `ChatOpenAI`, embeddings |
    | **Tools** | Let models take actions | `@tool` functions, prebuilt tools |
    | **Agents** | Orchestrate model + tools in a loop | `create_agent` |
    | **Memory** | Preserve context across turns | Message history, stores |
    | **Retrievers** | Find relevant information | Vector search, web retrievers |
    | **Document processing** | Ingest raw data | Loaders, splitters, transformers |
    | **Vector stores** | Semantic search | Chroma, FAISS, Pinecone |

    You've already used the first three. Memory starts in lesson 12, retrieval in lesson 17.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## How They Connect

    Every LangChain application follows the same data flow — even when you skip layers.

    **Simplest: model only** (lessons 5-7)
    ```
    User question → Chat model → Response
    ```

    **With tools** (lessons 8-10)
    ```
    User question → Agent → Model ⇄ Tools → Response
    ```

    **With retrieval** (lessons 17-19)
    ```
    User question → Retriever → Relevant docs ─┐
                                                 ├→ Model → Response
    User question ──────────────────────────────┘
    ```

    **Full RAG agent** (lesson 19)
    ```
    User question → Agent → Retriever → docs ─┐
                                                ├→ Model ⇄ Tools → Response
                              Memory ──────────┘
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Three Common Patterns

    Most LangChain apps are one of these three. Everything else is a variation.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 1. Agent with Tools

    A model that reasons and calls tools in a loop. You built this in lesson 10.

    ```
    User request → Agent ──→ Need tool? ──yes──→ Call tool ──→ Result ──┐
                     ↑                                                   │
                     └───────────────────────────────────────────────────┘
                              ──no──→ Final answer
    ```

    **When to use:** Tasks that need real-time data, calculations, or external actions.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2. RAG (Retrieval-Augmented Generation)

    Ground the model's answers in your data. The retriever finds relevant documents, the model uses them to answer.

    ```
    User question ──→ Retriever ──→ Relevant docs ──┐
                  └──────────────────────────────────┼──→ Model ──→ Informed answer
    ```

    **When to use:** Q&A over documents, knowledge bases, any task where the model needs facts it wasn't trained on.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 3. Multi-Agent System

    Multiple specialized agents coordinated by a supervisor. Each agent handles a different domain.

    ```
    Complex task ──→ Supervisor ──→ Research agent ──→ Results ──┐
                              └──→ Analysis agent ──→ Results ──┤
                                                                 ↓
                              ←── Coordinated response ←────────┘
    ```

    **When to use:** Tasks that span multiple domains, need different expertise, or benefit from divide-and-conquer.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What Lives Where

    LangChain splits across a few packages. Here's where to find things:

    | Package | Contains | You import |
    |---------|----------|------------|
    | `langchain` | Agents, middleware, structured output | `create_agent`, `ToolStrategy` |
    | `langchain-core` | Base classes, messages, tools | `tool`, `HumanMessage`, `AIMessage` |
    | `langchain-openai` | OpenAI/compatible model classes | `ChatOpenAI`, `OpenAIEmbeddings` |
    | `langgraph` | Graph runtime, state, persistence | `StateGraph`, `ToolNode`, `Command` |
    | `langchain-community` | Integrations (vector stores, loaders) | `FAISS`, `Chroma`, loaders |

    For this tutorial series, we use `ChatOpenAI` pointed at our endpoint. The import path doesn't matter much — what matters is understanding which *component* you need.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## What You've Learned vs What's Ahead

    | Phase | Lessons | Status |
    |-------|---------|--------|
    | **Foundations** | 1-4: Landscape, overview, quickstart, philosophy | Done |
    | **Core building blocks** | 5-11: Models, messages, tools, structured output, agents, architecture | Done |
    | **Memory & context** | 12-16: Context engineering, short/long-term memory | Next |
    | **Retrieval & knowledge** | 17-19: Retrieval, knowledge base, RAG agent | Coming |
    | **Production patterns** | 20-27: Streaming, guardrails, middleware, MCP | Coming |
    | **Multi-agent systems** | 28-37: Handoffs, routers, skills, subagents | Coming |
    | **Testing & projects** | 38-45: Unit tests, evals, SQL/voice agents | Coming |
    | **LangGraph** | 53-61: Graph API, functional API, persistence | Coming |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **LangChain is a component system.** Models reason, tools act, agents orchestrate, memory persists, retrievers find. Every app combines these layers differently. Now that you know the building blocks, the rest of this series fills in the gaps — memory, retrieval, production patterns, and multi-agent systems.

    **Next:** Lesson 12 — Context Engineering
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
