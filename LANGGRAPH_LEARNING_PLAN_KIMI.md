# LangGraph Learning Plan

A structured path to learn LangGraph from the docs and source code in this repository.

All documentation paths are relative to `docs/src/oss/langgraph/`.

---

## Phase 1: Foundations

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 1 | Overview | `overview.mdx` | What LangGraph is, core benefits, ecosystem |
| 2 | Install | `install.mdx` | Installation for Python and JS |
| 3 | Quickstart | `quickstart.mdx` | Build your first agent (Graph API + Functional API) |
| 4 | Thinking in LangGraph | `thinking-in-langgraph.mdx` | Mental models and design principles |
| 5 | Choosing APIs | `choosing-apis.mdx` | When to use Graph API vs Functional API |

## Phase 2: Core Concepts

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 6 | Graph API | `graph-api.mdx` | StateGraph, nodes, edges, compilation |
| 7 | Functional API | `functional-api.mdx` | `@entrypoint`, `@task`, control flow |
| 8 | Using Graph API | `use-graph-api.mdx` | Practical Graph API patterns |
| 9 | Using Functional API | `use-functional-api.mdx` | Practical Functional API patterns |
| 10 | Persistence | `persistence.mdx` | Checkpointing, threads, state snapshots |
| 11 | Memory | `memory.mdx` | Short-term and long-term memory |
| 12 | Interrupts | `interrupts.mdx` | Human-in-the-loop patterns |

## Phase 3: Advanced Capabilities

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 13 | Streaming | `streaming.mdx` | Token streaming, event streaming |
| 14 | Durable Execution | `durable-execution.mdx` | Fault tolerance, resumption |
| 15 | Time Travel | `use-time-travel.mdx` | Replay and debug execution |
| 16 | Subgraphs | `use-subgraphs.mdx` | Nested graph composition |
| 17 | Agentic RAG | `agentic-rag.mdx` | RAG with agent orchestration |
| 18 | SQL Agent | `sql-agent.mdx` | Database querying agents |

## Phase 4: Production

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 19 | Application Structure | `application-structure.mdx` | Project organization |
| 20 | Testing | `test.mdx` | Unit and integration testing |
| 21 | Observability | `observability.mdx` | Tracing and debugging |
| 22 | Studio | `studio.mdx` | Visual debugging and prototyping |
| 23 | Local Server | `local-server.mdx` | Local development server |
| 24 | Deploy | `deploy.mdx` | Production deployment |
| 25 | UI | `ui.mdx` | Building agent UIs |

## Phase 5: Implementation Details

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 26 | Pregel | `pregel.mdx` | Execution engine internals |
| 27 | Workflows vs Agents | `workflows-agents.mdx` | When to use which pattern |
| 28 | Case Studies | `case-studies.mdx` | Real-world examples |
| 29 | Changelog | `changelog-py.mdx` | Version history |

## Phase 6: Source Code Deep Dive

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 30 | Core Graph | `langgraph/libs/langgraph/langgraph/graph/` | StateGraph implementation |
| 31 | Types | `langgraph/libs/langgraph/langgraph/types.py` | Type definitions |
| 32 | Channels | `langgraph/libs/langgraph/langgraph/channels/` | State management |
| 33 | Pregel Engine | `langgraph/libs/langgraph/langgraph/pregel/` | Execution engine |
| 34 | Prebuilt Agents | `langgraph/libs/prebuilt/` | `create_react_agent`, ToolNode |
| 35 | Checkpointing | `langgraph/libs/checkpoint/` | Persistence layer |
| 36 | Examples | `langgraph/examples/` | Reference implementations |

---

## Suggested Pace

- **Week 1:** Phases 1-2 — Core concepts and basic agents
- **Week 2:** Phase 3 — Advanced capabilities (streaming, subgraphs, RAG)
- **Week 3:** Phase 4 — Production (testing, observability, deployment)
- **Week 4:** Phases 5-6 — Deep dive into internals and examples

---

## Key Documentation Sections

| Section | Path | Contents |
|---------|------|----------|
| Get started | `overview.mdx`, `install.mdx`, `quickstart.mdx` | Installation and first steps |
| Capabilities | `persistence.mdx`, `memory.mdx`, `interrupts.mdx`, `streaming.mdx`, `durable-execution.mdx` | Core features |
| Production | `test.mdx`, `observability.mdx`, `deploy.mdx`, `studio.mdx` | Production patterns |
| Graph API | `graph-api.mdx`, `use-graph-api.mdx` | Graph-based development |
| Functional API | `functional-api.mdx`, `use-functional-api.mdx` | Function-based development |
| Tutorials | `sql-agent.mdx`, `agentic-rag.mdx` | Step-by-step guides |

---

## Error Reference

Common errors and solutions:
- `INVALID_CONCURRENT_GRAPH_UPDATE.mdx`
- `GRAPH_RECURSION_LIMIT.mdx`
- `INVALID_GRAPH_NODE_RETURN_VALUE.mdx`
- `MISSING_CHECKPOINTER.mdx`
- `MULTIPLE_SUBGRAPHS.mdx`
- `INVALID_CHAT_HISTORY.mdx`

---

## Integration with LangChain

LangGraph builds on LangChain:
- Use LangChain models, messages, and tools
- LangGraph provides the orchestration layer
- Both Graph API and Functional API work with LangChain components

See `LANGCHAIN_LEARNING_PLAN.md` for prerequisites.
