# LangChain Learning Plan

All paths relative to `docs/src/oss/`.

---

## Phase 1: Foundations

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 1 | ~~Framework landscape~~ | `concepts/products.mdx` | ~~LangChain vs other frameworks — when to use what~~ |
| 2 | ~~LangChain overview~~ | `langchain/overview.mdx` | ~~Architecture, key benefits, 10-line agent~~ |
| 3 | ~~Install~~ | `langchain/install.mdx` | ~~`pip install langchain` + provider packages~~ |
| 4 | ~~Quickstart~~ | `langchain/quickstart.mdx` | ~~Build your first agent end-to-end~~ |
| 5 | Philosophy | `langchain/philosophy.mdx` | Design principles behind the framework |

## Phase 2: Core Building Blocks

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 6 | Models | `langchain/models.mdx` | Chat model interface, provider config, model switching |
| 7 | Messages | `langchain/messages.mdx` | Message types (human, AI, system, tool) |
| 8 | Tools | `langchain/tools.mdx` | Define tools, tool calling, runtime context |
| 9 | Structured output | `langchain/structured-output.mdx` | Response schemas, validated outputs |
| 10 | Agents (deep dive) | `langchain/agents.mdx` | Agent loop, reasoning + acting, graph internals |

## Phase 3: Memory & Context

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 11 | Context engineering | `langchain/context-engineering.mdx` | Prompt optimization, context window management |
| 12 | Short-term memory | `langchain/short-term-memory.mdx` | Conversation history, summarization strategies |
| 13 | Long-term memory | `langchain/long-term-memory.mdx` | Persistent memory across conversations |
| 14 | Concepts: context | `concepts/context.mdx` | Static vs dynamic context, state vs store |
| 15 | Concepts: memory | `concepts/memory.mdx` | Semantic, episodic, procedural memory |

## Phase 4: Retrieval & Knowledge

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 16 | Retrieval | `langchain/retrieval.mdx` | Retriever interface, document loading, splitting |
| 17 | Knowledge base | `langchain/knowledge-base.mdx` | Build a semantic search engine |
| 18 | RAG agent | `langchain/rag.mdx` | Full retrieval-augmented generation agent |
| 19 | Component architecture | `langchain/component-architecture.mdx` | How components compose together |

## Phase 5: Production Patterns

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 20 | Streaming | `langchain/streaming.mdx` | Token-by-token output, streaming events |
| 21 | Human-in-the-loop | `langchain/human-in-the-loop.mdx` | Approval flows, human oversight |
| 22 | Guardrails | `langchain/guardrails.mdx` | Input/output validation, safety |
| 23 | Middleware | `langchain/middleware/overview.mdx` | Built-in + custom middleware |
| 24 | MCP | `langchain/mcp.mdx` | Model Context Protocol integration |
| 25 | Runtime | `langchain/runtime.mdx` | Execution environment details |

## Phase 6: Multi-Agent Systems

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 26 | Multi-agent intro | `langchain/multi-agent/index.mdx` | Patterns overview |
| 27 | Handoffs | `langchain/multi-agent/handoffs.mdx` | Agent-to-agent delegation |
| 28 | Router | `langchain/multi-agent/router.mdx` | Route requests to specialized agents |
| 29 | Skills | `langchain/multi-agent/skills.mdx` | On-demand capability modules |
| 30 | Subagents | `langchain/multi-agent/subagents.mdx` | Nested agent orchestration |
| 31 | Custom workflow | `langchain/multi-agent/custom-workflow.mdx` | Design your own patterns |

### Tutorials (build along)
- `langchain/multi-agent/handoffs-customer-support.mdx` — customer support bot
- `langchain/multi-agent/router-knowledge-base.mdx` — multi-source knowledge base
- `langchain/multi-agent/skills-sql-assistant.mdx` — SQL assistant
- `langchain/multi-agent/subagents-personal-assistant.mdx` — personal assistant

## Phase 7: Practical Projects

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 32 | SQL agent | `langchain/sql-agent.mdx` | Query databases with natural language |
| 33 | Voice agent | `langchain/voice-agent.mdx` | Audio input/output agent |
| 34 | Observability | `langchain/observability.mdx` | LangSmith tracing & debugging |
| 35 | Deployment | `langchain/deploy.mdx` | Deploy to production |

## Integrations Reference

When you need a specific provider or tool, browse:
- **Python:** `python/integrations/` (1,328 files across 20 categories)
- **JavaScript:** `javascript/integrations/` (323 files across 16 categories)

Key categories: `chat/`, `llms/`, `embeddings/`, `vectorstores/`, `tools/`, `document_loaders/`, `retrievers/`

---

## Suggested Pace

- **Week 1:** Phases 1-2 (foundations + building blocks) — get a working agent
- **Week 2:** Phase 3 (memory & context) — make agents remember
- **Week 3:** Phases 4-5 (retrieval + production) — build RAG, add guardrails
- **Week 4:** Phase 6 (multi-agent) — orchestrate multiple agents
- **Ongoing:** Phase 7 (projects) — build real applications
