# LangChain Learning Plan

All paths relative to `docs/src/oss/`.

---

## Phase 1: Foundations

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 1 | ~~Framework landscape~~ | `concepts/products.mdx` | ~~LangChain vs other frameworks — when to use what~~ |
| 2 | ~~LangChain overview~~ | `langchain/overview.mdx` | ~~Architecture, key benefits, 10-line agent~~ |
| 3 | ~~Install + Quickstart~~ | `langchain/install.mdx`, `langchain/quickstart.mdx` | ~~Setup and first agent end-to-end~~ |
| 4 | ~~Philosophy~~ | `langchain/philosophy.mdx` | ~~Design principles and history~~ |

## Phase 2: Core Building Blocks

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 5 | ~~Models~~ | `langchain/models.mdx` | ~~Chat model interface, parameters, invoke/stream/batch~~ |
| 6 | ~~Models: multimodal & advanced~~ | `langchain/models.mdx` | ~~Multimodal inputs, reasoning tokens, caching, custom models~~ |
| 7 | ~~Messages~~ | `langchain/messages.mdx` | ~~Message types (human, AI, system, tool), content blocks~~ |
| 8 | ~~Tools~~ | `langchain/tools.mdx` | ~~Define tools, tool calling, ToolRuntime, injection~~ |
| 9 | ~~Structured output~~ | `langchain/structured-output.mdx` | ~~Response schemas, ToolStrategy, validated outputs~~ |
| 10 | Agents (deep dive) | `langchain/agents.mdx` | Agent loop, create_agent options, graph internals |
| 11 | Component architecture | `langchain/component-architecture.mdx` | How components compose together |

## Phase 3: Memory & Context

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 12 | Context engineering | `langchain/context-engineering.mdx` | Prompt optimization, context window management |
| 13 | Short-term memory | `langchain/short-term-memory.mdx` | Conversation history, trimming, summarization |
| 14 | Long-term memory | `langchain/long-term-memory.mdx` | Persistent memory across conversations |
| 15 | Concepts: context | `concepts/context.mdx` | Static vs dynamic context, state vs store |
| 16 | Concepts: memory | `concepts/memory.mdx` | Semantic, episodic, procedural memory |

## Phase 4: Retrieval & Knowledge

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 17 | Retrieval | `langchain/retrieval.mdx` | Retriever interface, document loading, splitting |
| 18 | Knowledge base | `langchain/knowledge-base.mdx` | Build a semantic search engine |
| 19 | RAG agent | `langchain/rag.mdx` | Full retrieval-augmented generation agent |

## Phase 5: Production Patterns

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 20 | Streaming | `langchain/streaming.mdx` | Token-by-token output, streaming events |
| 21 | Human-in-the-loop | `langchain/human-in-the-loop.mdx` | Approval flows, human oversight |
| 22 | Guardrails | `langchain/guardrails.mdx` | Input/output validation, safety |
| 23 | Middleware overview | `langchain/middleware/overview.mdx` | Middleware concepts and pipeline |
| 24 | Built-in middleware | `langchain/middleware/built-in.mdx` | Summarization, message trimming |
| 25 | Custom middleware | `langchain/middleware/custom.mdx` | Write your own middleware |
| 26 | MCP | `langchain/mcp.mdx` | Model Context Protocol integration |
| 27 | Runtime | `langchain/runtime.mdx` | Execution environment, Runtime object |

## Phase 6: Multi-Agent Systems

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 28 | Multi-agent intro | `langchain/multi-agent/index.mdx` | Patterns overview |
| 29 | Handoffs | `langchain/multi-agent/handoffs.mdx` | Agent-to-agent delegation |
| 30 | Router | `langchain/multi-agent/router.mdx` | Route requests to specialized agents |
| 31 | Skills | `langchain/multi-agent/skills.mdx` | On-demand capability modules |
| 32 | Subagents | `langchain/multi-agent/subagents.mdx` | Nested agent orchestration |
| 33 | Custom workflow | `langchain/multi-agent/custom-workflow.mdx` | Design your own patterns |

### Multi-Agent Tutorials (build along)

| # | Topic | File | What you'll build |
|---|-------|------|-------------------|
| 34 | Handoffs tutorial | `langchain/multi-agent/handoffs-customer-support.mdx` | Customer support bot |
| 35 | Router tutorial | `langchain/multi-agent/router-knowledge-base.mdx` | Multi-source knowledge base |
| 36 | Skills tutorial | `langchain/multi-agent/skills-sql-assistant.mdx` | SQL assistant |
| 37 | Subagents tutorial | `langchain/multi-agent/subagents-personal-assistant.mdx` | Personal assistant |

## Phase 7: Testing & Evaluation

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 38 | Testing overview | `langchain/test/index.mdx` | Testing strategies for agents |
| 39 | Unit testing | `langchain/test/unit-testing.mdx` | Mock models and tools, test in isolation |
| 40 | Integration testing | `langchain/test/integration-testing.mdx` | End-to-end agent tests |
| 41 | Evals | `langchain/test/evals.mdx` | LLM-as-judge, evaluation frameworks |

## Phase 8: Practical Projects

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 42 | SQL agent | `langchain/sql-agent.mdx` | Query databases with natural language |
| 43 | Voice agent | `langchain/voice-agent.mdx` | Audio input/output agent |
| 44 | Observability | `langchain/observability.mdx` | LangSmith tracing & debugging |
| 45 | Deployment | `langchain/deploy.mdx` | Deploy to production |

## Phase 9: Frontend Integration

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 46 | Frontend overview | `langchain/frontend/overview.mdx` | Building agent UIs |
| 47 | Generative UI | `langchain/frontend/generative-ui.mdx` | Dynamic UI generation from agent output |
| 48 | Tool calling UI | `langchain/frontend/tool-calling.mdx` | Display tool calls in the interface |
| 49 | Structured output UI | `langchain/frontend/structured-output.mdx` | Render structured responses |
| 50 | Human-in-the-loop UI | `langchain/frontend/human-in-the-loop.mdx` | Approval interfaces |
| 51 | Branching chat | `langchain/frontend/branching-chat.mdx` | Conversation branching and forking |
| 52 | Time travel | `langchain/frontend/time-travel.mdx` | Replay and rewind state in UI |

## Phase 10: LangGraph (Advanced)

For when you need lower-level control over agent orchestration:

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 53 | LangGraph overview | `langgraph/overview.mdx` | Architecture, when to use LangGraph |
| 54 | Quickstart | `langgraph/quickstart.mdx` | First LangGraph agent |
| 55 | Choosing APIs | `langgraph/choosing-apis.mdx` | Graph API vs Functional API |
| 56 | Graph API | `langgraph/graph-api.mdx` | StateGraph, nodes, edges |
| 57 | Functional API | `langgraph/functional-api.mdx` | @entrypoint, @task, control flow |
| 58 | Persistence | `langgraph/persistence.mdx` | Checkpointing and state snapshots |
| 59 | Durable execution | `langgraph/durable-execution.mdx` | Fault tolerance and resumption |
| 60 | Custom RAG agent | `langgraph/agentic-rag.mdx` | RAG with full graph control |
| 61 | Custom SQL agent | `langgraph/sql-agent.mdx` | SQL with full graph control |

## Integrations Reference

When you need a specific provider or tool, browse:
- **Python:** `python/integrations/` (1,328 files across 20 categories)
- **JavaScript:** `javascript/integrations/` (323 files across 16 categories)

Key categories: `chat/`, `llms/`, `embeddings/`, `vectorstores/`, `tools/`, `document_loaders/`, `retrievers/`

## Error Reference

Consult when you hit a specific error:
- `langchain/errors/INVALID_TOOL_RESULTS.mdx` — tool result format issues
- `langchain/errors/MODEL_NOT_FOUND.mdx` — model configuration errors
- `langchain/errors/MODEL_RATE_LIMIT.mdx` — rate limiting
- `langchain/errors/OUTPUT_PARSING_FAILURE.mdx` — parsing errors
- `langchain/errors/MODEL_AUTHENTICATION.mdx` — auth errors
- `langchain/errors/MESSAGE_COERCION_FAILURE.mdx` — message format errors
- `langchain/errors/INVALID_PROMPT_INPUT.mdx` — input validation errors

---

## Suggested Pace

- **Week 1:** Phases 1-2 (foundations + building blocks) — get a working agent
- **Week 2:** Phase 3 (memory & context) — make agents remember
- **Week 3:** Phases 4-5 (retrieval + production) — build RAG, add guardrails
- **Week 4:** Phase 6 (multi-agent) — orchestrate multiple agents
- **Week 5:** Phases 7-8 (testing + projects) — test and deploy
- **Week 6:** Phase 9 (frontend) — build agent UIs
- **Ongoing:** Phase 10 (LangGraph) — drop to low-level when needed
