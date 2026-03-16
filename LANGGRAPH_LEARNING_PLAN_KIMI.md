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
| 12 | Add Memory | `add-memory.mdx` | Adding memory to agents |
| 13 | Interrupts | `interrupts.mdx` | Human-in-the-loop patterns |

## Phase 3: Advanced Capabilities

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 14 | Streaming | `streaming.mdx` | Token streaming, event streaming |
| 15 | Durable Execution | `durable-execution.mdx` | Fault tolerance, resumption |
| 16 | Time Travel | `use-time-travel.mdx` | Replay and debug execution |
| 17 | Subgraphs | `use-subgraphs.mdx` | Nested graph composition |
| 18 | Agentic RAG | `agentic-rag.mdx` | RAG with agent orchestration |
| 19 | SQL Agent | `sql-agent.mdx` | Database querying agents |
| 20 | Workflows vs Agents | `workflows-agents.mdx` | When to use which pattern |

## Phase 4: Production

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 21 | Application Structure | `application-structure.mdx` | Project organization |
| 22 | Testing | `test.mdx` | Unit and integration testing |
| 23 | Observability | `observability.mdx` | Tracing and debugging |
| 24 | Studio | `studio.mdx` | Visual debugging and prototyping |
| 25 | Local Server | `local-server.mdx` | Local development server |
| 26 | Deploy | `deploy.mdx` | Production deployment |
| 27 | UI | `ui.mdx` | Building agent UIs |
| 28 | Frontend Integration | `frontend/graph-execution.mdx` | Frontend graph execution |

## Phase 5: Implementation Details

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 29 | Pregel | `pregel.mdx` | Execution engine internals |
| 30 | Case Studies | `case-studies.mdx` | Real-world examples |
| 31 | Changelog (Python) | `changelog-py.mdx` | Python version history |
| 32 | Changelog (JS) | `changelog-js.mdx` | JavaScript version history |

## Phase 6: Example Patterns

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 33 | Chatbots | `langgraph/examples/chatbots/` | Conversational agents |
| 34 | Code Assistant | `langgraph/examples/code_assistant/` | Code generation agents |
| 35 | Customer Support | `langgraph/examples/customer-support/` | Support automation |
| 36 | Extraction | `langgraph/examples/extraction/` | Information extraction |
| 37 | Human-in-the-Loop | `langgraph/examples/human_in_the_loop/` | Human oversight patterns |
| 38 | LATS | `langgraph/examples/lats/` | Language Agent Tree Search |
| 39 | LLM Compiler | `langgraph/examples/llm-compiler/` | LLM compiler pattern |
| 40 | Multi-Agent | `langgraph/examples/multi_agent/` | Multi-agent systems |
| 41 | Plan-and-Execute | `langgraph/examples/plan-and-execute/` | Planning agents |
| 42 | RAG | `langgraph/examples/rag/` | RAG implementations |
| 43 | Reflection | `langgraph/examples/reflection/` | Self-improving agents |
| 44 | Reflexion | `langgraph/examples/reflexion/` | Reflexion pattern |
| 45 | ReWOO | `langgraph/examples/rewoo/` | ReWOO pattern |
| 46 | Self-Discover | `langgraph/examples/self-discover/` | Self-discovering agents |
| 47 | USACO | `langgraph/examples/usaco/` | Competitive programming |
| 48 | Web Navigation | `langgraph/examples/web-navigation/` | Browser automation |
| 49 | Chatbot Simulation | `langgraph/examples/chatbot-simulation-evaluation/` | Evaluation patterns |
| 50 | Tutorials | `langgraph/examples/tutorials/` | Additional tutorials |
| 51 | Notebook: ReAct Agent | `langgraph/examples/react-agent-from-scratch.ipynb` | Build ReAct from scratch |
| 52 | Notebook: Structured Output | `langgraph/examples/react-agent-structured-output.ipynb` | Structured agent outputs |
| 53 | Notebook: Subgraphs | `langgraph/examples/subgraph.ipynb` | Subgraph composition |
| 54 | Notebook: Tool Calling | `langgraph/examples/tool-calling.ipynb` | Tool calling patterns |
| 55 | Notebook: LangSmith Run ID | `langgraph/examples/run-id-langsmith.ipynb` | LangSmith integration |

## Phase 7: Source Code Deep Dive

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 56 | Core Graph | `langgraph/libs/langgraph/langgraph/graph/` | StateGraph implementation |
| 57 | Types | `langgraph/libs/langgraph/langgraph/types.py` | Type definitions |
| 58 | Channels | `langgraph/libs/langgraph/langgraph/channels/` | State management |
| 59 | Pregel Engine | `langgraph/libs/langgraph/langgraph/pregel/` | Execution engine |
| 60 | Prebuilt Agents | `langgraph/libs/prebuilt/` | `create_react_agent`, ToolNode |
| 61 | Checkpointing | `langgraph/libs/checkpoint/` | Persistence layer |
| 62 | Checkpoint SQLite | `langgraph/libs/checkpoint-sqlite/` | SQLite implementation |
| 63 | Checkpoint Postgres | `langgraph/libs/checkpoint-postgres/` | Postgres implementation |
| 64 | CLI | `langgraph/libs/cli/` | Command-line interface |
| 65 | Python SDK | `langgraph/libs/sdk-py/` | Python SDK for API |
| 66 | JS SDK | `langgraph/libs/sdk-js/` | JavaScript SDK for API |

---

## Suggested Pace

- **Week 1:** Phases 1-2 — Core concepts and basic agents
- **Week 2:** Phase 3 — Advanced capabilities (streaming, subgraphs, RAG)
- **Week 3:** Phase 4 — Production (testing, observability, deployment)
- **Week 4:** Phase 5 — Implementation details and changelogs
- **Week 5:** Phase 6 — Example patterns (pick 5-10 most relevant)
- **Week 6:** Phase 7 — Source code deep dive

---

## Key Documentation Sections

| Section | Path | Contents |
|---------|------|----------|
| Get started | `overview.mdx`, `install.mdx`, `quickstart.mdx` | Installation and first steps |
| Capabilities | `persistence.mdx`, `memory.mdx`, `add-memory.mdx`, `interrupts.mdx`, `streaming.mdx`, `durable-execution.mdx` | Core features |
| Production | `test.mdx`, `observability.mdx`, `deploy.mdx`, `studio.mdx`, `ui.mdx`, `frontend/graph-execution.mdx` | Production patterns |
| Graph API | `graph-api.mdx`, `use-graph-api.mdx` | Graph-based development |
| Functional API | `functional-api.mdx`, `use-functional-api.mdx` | Function-based development |
| Tutorials | `sql-agent.mdx`, `agentic-rag.mdx` | Step-by-step guides |
| Internals | `pregel.mdx`, `workflows-agents.mdx` | Implementation details |

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

---

## Complete File Checklist

### Documentation (32 files)
- [ ] `overview.mdx`
- [ ] `install.mdx`
- [ ] `quickstart.mdx`
- [ ] `thinking-in-langgraph.mdx`
- [ ] `choosing-apis.mdx`
- [ ] `graph-api.mdx`
- [ ] `functional-api.mdx`
- [ ] `use-graph-api.mdx`
- [ ] `use-functional-api.mdx`
- [ ] `persistence.mdx`
- [ ] `memory.mdx`
- [ ] `add-memory.mdx`
- [ ] `interrupts.mdx`
- [ ] `streaming.mdx`
- [ ] `durable-execution.mdx`
- [ ] `use-time-travel.mdx`
- [ ] `use-subgraphs.mdx`
- [ ] `agentic-rag.mdx`
- [ ] `sql-agent.mdx`
- [ ] `workflows-agents.mdx`
- [ ] `application-structure.mdx`
- [ ] `test.mdx`
- [ ] `observability.mdx`
- [ ] `studio.mdx`
- [ ] `local-server.mdx`
- [ ] `deploy.mdx`
- [ ] `ui.mdx`
- [ ] `frontend/graph-execution.mdx`
- [ ] `pregel.mdx`
- [ ] `case-studies.mdx`
- [ ] `changelog-py.mdx`
- [ ] `changelog-js.mdx`

### Error Docs (6 files)
- [ ] `errors/INVALID_CONCURRENT_GRAPH_UPDATE.mdx`
- [ ] `errors/GRAPH_RECURSION_LIMIT.mdx`
- [ ] `errors/INVALID_GRAPH_NODE_RETURN_VALUE.mdx`
- [ ] `errors/MISSING_CHECKPOINTER.mdx`
- [ ] `errors/MULTIPLE_SUBGRAPHS.mdx`
- [ ] `errors/INVALID_CHAT_HISTORY.mdx`

### Examples (23 items)
- [ ] `chatbots/`
- [ ] `code_assistant/`
- [ ] `customer-support/`
- [ ] `extraction/`
- [ ] `human_in_the_loop/`
- [ ] `lats/`
- [ ] `llm-compiler/`
- [ ] `multi_agent/`
- [ ] `plan-and-execute/`
- [ ] `rag/`
- [ ] `reflection/`
- [ ] `reflexion/`
- [ ] `rewoo/`
- [ ] `self-discover/`
- [ ] `usaco/`
- [ ] `web-navigation/`
- [ ] `chatbot-simulation-evaluation/`
- [ ] `tutorials/`
- [ ] `react-agent-from-scratch.ipynb`
- [ ] `react-agent-structured-output.ipynb`
- [ ] `subgraph.ipynb`
- [ ] `tool-calling.ipynb`
- [ ] `run-id-langsmith.ipynb`
