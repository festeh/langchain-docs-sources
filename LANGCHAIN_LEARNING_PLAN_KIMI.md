# LangChain Learning Plan

A structured path to learn LangChain from the docs and source code in this repository.

All documentation paths are relative to `docs/src/oss/`.

---

## Phase 1: Foundations

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 1 | Overview | `langchain/overview.mdx` | Architecture, key benefits, ecosystem |
| 2 | Install | `langchain/install.mdx` | Installation and provider packages |
| 3 | Quickstart | `langchain/quickstart.mdx` | Build your first agent end-to-end |
| 4 | Philosophy | `langchain/philosophy.mdx` | Design principles behind the framework |
| 5 | Academy | `langchain/academy.mdx` | Learning resources and courses |
| 6 | Get Help | `langchain/get-help.mdx` | Community and support resources |

## Phase 2: Core Building Blocks

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 7 | Models | `langchain/models.mdx` | Chat model interface, provider config, model switching |
| 8 | Messages | `langchain/messages.mdx` | Message types (human, AI, system, tool) |
| 9 | Tools | `langchain/tools.mdx` | Define tools, tool calling, runtime context |
| 10 | Structured Output | `langchain/structured-output.mdx` | Response schemas, validated outputs |
| 11 | Agents Deep Dive | `langchain/agents.mdx` | Agent loop, reasoning + acting, graph internals |
| 12 | Component Architecture | `langchain/component-architecture.mdx` | How components compose together |

## Phase 3: Memory & Context

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 13 | Context Engineering | `langchain/context-engineering.mdx` | Prompt optimization, context window management |
| 14 | Short-term Memory | `langchain/short-term-memory.mdx` | Conversation history, summarization strategies |
| 15 | Long-term Memory | `langchain/long-term-memory.mdx` | Persistent memory across conversations |
| 16 | Concepts: Context | `concepts/context.mdx` | Static vs dynamic context, state vs store |
| 17 | Concepts: Memory | `concepts/memory.mdx` | Semantic, episodic, procedural memory |

## Phase 4: Retrieval & Knowledge

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 18 | Retrieval | `langchain/retrieval.mdx` | Retriever interface, document loading, splitting |
| 19 | Knowledge Base | `langchain/knowledge-base.mdx` | Build a semantic search engine |
| 20 | RAG Agent | `langchain/rag.mdx` | Full retrieval-augmented generation agent |

## Phase 5: Production Patterns

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 21 | Streaming | `langchain/streaming.mdx` | Token-by-token output, streaming events |
| 22 | Human-in-the-loop | `langchain/human-in-the-loop.mdx` | Approval flows, human oversight |
| 23 | Guardrails | `langchain/guardrails.mdx` | Input/output validation, safety |
| 24 | Middleware Overview | `langchain/middleware/overview.mdx` | Middleware concepts |
| 25 | Built-in Middleware | `langchain/middleware/built-in.mdx` | Todo lists, summarization, etc. |
| 26 | Custom Middleware | `langchain/middleware/custom.mdx` | Writing your own middleware |
| 27 | MCP | `langchain/mcp.mdx` | Model Context Protocol integration |
| 28 | Runtime | `langchain/runtime.mdx` | Execution environment details |

## Phase 6: Multi-Agent Systems

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 29 | Multi-agent Intro | `langchain/multi-agent/index.mdx` | Patterns overview |
| 30 | Handoffs | `langchain/multi-agent/handoffs.mdx` | Agent-to-agent delegation |
| 31 | Router | `langchain/multi-agent/router.mdx` | Route requests to specialized agents |
| 32 | Skills | `langchain/multi-agent/skills.mdx` | On-demand capability modules |
| 33 | Subagents | `langchain/multi-agent/subagents.mdx` | Nested agent orchestration |
| 34 | Custom Workflow | `langchain/multi-agent/custom-workflow.mdx` | Design your own patterns |

### Multi-Agent Tutorials
| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 35 | Handoffs Tutorial | `langchain/multi-agent/handoffs-customer-support.mdx` | Customer support bot |
| 36 | Router Tutorial | `langchain/multi-agent/router-knowledge-base.mdx` | Multi-source knowledge base |
| 37 | Skills Tutorial | `langchain/multi-agent/skills-sql-assistant.mdx` | SQL assistant |
| 38 | Subagents Tutorial | `langchain/multi-agent/subagents-personal-assistant.mdx` | Personal assistant |

## Phase 7: Testing & Quality

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 39 | Testing Overview | `langchain/test/index.mdx` | Testing strategies |
| 40 | Unit Testing | `langchain/test/unit-testing.mdx` | Unit test patterns |
| 41 | Integration Testing | `langchain/test/integration-testing.mdx` | Integration test patterns |
| 42 | Evals | `langchain/test/evals.mdx` | Evaluation frameworks |

## Phase 8: Frontend Integration

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 43 | Frontend Overview | `langchain/frontend/overview.mdx` | Building agent UIs |
| 44 | Generative UI | `langchain/frontend/generative-ui.mdx` | Dynamic UI generation |
| 45 | Tool Calling UI | `langchain/frontend/tool-calling.mdx` | Tool call interfaces |
| 46 | Structured Output UI | `langchain/frontend/structured-output.mdx` | Structured response UIs |
| 47 | Human-in-the-loop UI | `langchain/frontend/human-in-the-loop.mdx` | Approval interfaces |
| 48 | Branching Chat | `langchain/frontend/branching-chat.mdx` | Conversation branching |
| 49 | Time Travel | `langchain/frontend/time-travel.mdx` | State replay in UI |
| 50 | Reasoning Tokens | `langchain/frontend/reasoning-tokens.mdx` | Display reasoning |
| 51 | Join/Rejoin | `langchain/frontend/join-rejoin.mdx` | Multi-user patterns |
| 52 | Message Queues | `langchain/frontend/message-queues.mdx` | Async message handling |
| 53 | Markdown Messages | `langchain/frontend/markdown-messages.mdx` | Rich message formatting |

## Phase 9: Specialized Agents

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 54 | SQL Agent | `langchain/sql-agent.mdx` | Query databases with natural language |
| 55 | Voice Agent | `langchain/voice-agent.mdx` | Audio input/output agent |
| 56 | UI | `langchain/ui.mdx` | UI agent patterns |
| 57 | Studio | `langchain/studio.mdx` | Visual agent development |

## Phase 10: Production Deployment

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 58 | Observability | `langchain/observability.mdx` | LangSmith tracing & debugging |
| 59 | Deployment | `langchain/deploy.mdx` | Deploy to production |

## Phase 11: Concepts & Theory

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 60 | Framework Landscape | `concepts/products.mdx` | LangChain vs other frameworks |

## Phase 12: Error Reference

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 61 | Invalid Tool Results | `langchain/errors/INVALID_TOOL_RESULTS.mdx` | Tool result errors |
| 62 | Model Not Found | `langchain/errors/MODEL_NOT_FOUND.mdx` | Model configuration errors |
| 63 | Model Rate Limit | `langchain/errors/MODEL_RATE_LIMIT.mdx` | Rate limiting |
| 64 | Output Parsing Failure | `langchain/errors/OUTPUT_PARSING_FAILURE.mdx` | Parsing errors |
| 65 | Model Authentication | `langchain/errors/MODEL_AUTHENTICATION.mdx` | Auth errors |
| 66 | Message Coercion Failure | `langchain/errors/MESSAGE_COERCION_FAILURE.mdx` | Message format errors |
| 67 | Invalid Prompt Input | `langchain/errors/INVALID_PROMPT_INPUT.mdx` | Input validation errors |

## Phase 13: Version History

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 68 | Changelog (Python) | `langchain/changelog-py.mdx` | Python version history |
| 69 | Changelog (JS) | `langchain/changelog-js.mdx` | JavaScript version history |

---

## Suggested Pace

- **Week 1:** Phases 1-2 — Foundations and core building blocks
- **Week 2:** Phase 3 — Memory and context management
- **Week 3:** Phase 4 — Retrieval and knowledge systems
- **Week 4:** Phase 5 — Production patterns (streaming, guardrails, middleware)
- **Week 5:** Phase 6 — Multi-agent systems
- **Week 6:** Phase 7 — Testing and evaluation
- **Week 7:** Phase 8 — Frontend integration
- **Week 8:** Phases 9-10 — Specialized agents and deployment
- **Ongoing:** Phases 11-13 — Reference materials

---

## Integrations Reference

When you need a specific provider or tool, browse:
- **Python:** `python/integrations/` (1,328 files across 20 categories)
- **JavaScript:** `javascript/integrations/` (323 files across 16 categories)

Key categories: `chat/`, `llms/`, `embeddings/`, `vectorstores/`, `tools/`, `document_loaders/`, `retrievers/`

---

## Complete File Checklist

### Core Documentation (59 files)
- [ ] `langchain/overview.mdx`
- [ ] `langchain/install.mdx`
- [ ] `langchain/quickstart.mdx`
- [ ] `langchain/philosophy.mdx`
- [ ] `langchain/academy.mdx`
- [ ] `langchain/get-help.mdx`
- [ ] `langchain/models.mdx`
- [ ] `langchain/messages.mdx`
- [ ] `langchain/tools.mdx`
- [ ] `langchain/structured-output.mdx`
- [ ] `langchain/agents.mdx`
- [ ] `langchain/component-architecture.mdx`
- [ ] `langchain/context-engineering.mdx`
- [ ] `langchain/short-term-memory.mdx`
- [ ] `langchain/long-term-memory.mdx`
- [ ] `concepts/context.mdx`
- [ ] `concepts/memory.mdx`
- [ ] `langchain/retrieval.mdx`
- [ ] `langchain/knowledge-base.mdx`
- [ ] `langchain/rag.mdx`
- [ ] `langchain/streaming.mdx`
- [ ] `langchain/human-in-the-loop.mdx`
- [ ] `langchain/guardrails.mdx`
- [ ] `langchain/middleware/overview.mdx`
- [ ] `langchain/middleware/built-in.mdx`
- [ ] `langchain/middleware/custom.mdx`
- [ ] `langchain/mcp.mdx`
- [ ] `langchain/runtime.mdx`
- [ ] `langchain/multi-agent/index.mdx`
- [ ] `langchain/multi-agent/handoffs.mdx`
- [ ] `langchain/multi-agent/router.mdx`
- [ ] `langchain/multi-agent/skills.mdx`
- [ ] `langchain/multi-agent/subagents.mdx`
- [ ] `langchain/multi-agent/custom-workflow.mdx`
- [ ] `langchain/multi-agent/handoffs-customer-support.mdx`
- [ ] `langchain/multi-agent/router-knowledge-base.mdx`
- [ ] `langchain/multi-agent/skills-sql-assistant.mdx`
- [ ] `langchain/multi-agent/subagents-personal-assistant.mdx`
- [ ] `langchain/test/index.mdx`
- [ ] `langchain/test/unit-testing.mdx`
- [ ] `langchain/test/integration-testing.mdx`
- [ ] `langchain/test/evals.mdx`
- [ ] `langchain/frontend/overview.mdx`
- [ ] `langchain/frontend/generative-ui.mdx`
- [ ] `langchain/frontend/tool-calling.mdx`
- [ ] `langchain/frontend/structured-output.mdx`
- [ ] `langchain/frontend/human-in-the-loop.mdx`
- [ ] `langchain/frontend/branching-chat.mdx`
- [ ] `langchain/frontend/time-travel.mdx`
- [ ] `langchain/frontend/reasoning-tokens.mdx`
- [ ] `langchain/frontend/join-rejoin.mdx`
- [ ] `langchain/frontend/message-queues.mdx`
- [ ] `langchain/frontend/markdown-messages.mdx`
- [ ] `langchain/sql-agent.mdx`
- [ ] `langchain/voice-agent.mdx`
- [ ] `langchain/ui.mdx`
- [ ] `langchain/studio.mdx`
- [ ] `langchain/observability.mdx`
- [ ] `langchain/deploy.mdx`
- [ ] `concepts/products.mdx`

### Error Documentation (7 files)
- [ ] `langchain/errors/INVALID_TOOL_RESULTS.mdx`
- [ ] `langchain/errors/MODEL_NOT_FOUND.mdx`
- [ ] `langchain/errors/MODEL_RATE_LIMIT.mdx`
- [ ] `langchain/errors/OUTPUT_PARSING_FAILURE.mdx`
- [ ] `langchain/errors/MODEL_AUTHENTICATION.mdx`
- [ ] `langchain/errors/MESSAGE_COERCION_FAILURE.mdx`
- [ ] `langchain/errors/INVALID_PROMPT_INPUT.mdx`

### Changelogs (2 files)
- [ ] `langchain/changelog-py.mdx`
- [ ] `langchain/changelog-js.mdx`

---

## Integration with LangGraph & Deep Agents

LangChain is the foundation:
- **LangChain** — Core building blocks (models, tools, messages)
- **LangGraph** — Orchestration layer for complex workflows
- **Deep Agents** — Batteries-included agent harness built on both

See `LANGGRAPH_LEARNING_PLAN_KIMI.md` and `DEEPAGENTS_LEARNING_PLAN_KIMI.md` for next steps.
