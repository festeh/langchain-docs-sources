# Table of Contents

## LangSmith (Platform Docs)

**Path:** `docs/src/langsmith/`

- **Account & Setup** — create-account-api-key, rbac, abac, users, billing, data-storage-and-privacy
- **Tracing & Observability** — integrations, conditional-tracing, access-current-span, annotate-code, add-metadata-tags, compare-traces, configurable-logs
- **Evaluation & Testing** — code-evaluator (sdk/ui), composite-evaluators, few-shot-evaluators, annotation-queues, bind-evaluator-to-dataset
- **Prompt Engineering** — create-a-prompt, versioning, management
- **Agent Builder** — essentials, setup, tools, code, templates, triggers, webhooks, MCP servers, Slack app, pricing FAQ
- **Agent Server** — changelog, feedback, scale, distributed-tracing
- **Self-Hosting** — AWS, Azure, hybrid deploy, custom auth/docker/middleware/routes/store/models

## Open Source Frameworks

**Path:** `docs/src/oss/`

### LangChain (`oss/langchain/`)
- Overview, agents, models, tools, middleware, multi-agent, testing, errors, frontend

### LangGraph (`oss/langgraph/`)
- Overview, concepts, how-tos, tutorials, production, errors, frontend

### Deep Agents (`oss/deepagents/`)
- Overview, CLI, frontend

## Integrations

### Python (`oss/python/integrations/`) — 1,328 files
- Providers (409) · Document Loaders (199) · Tools (158) · Vector Stores (129)
- LLMs (97) · Chat Models (93) · Embeddings (88) · Retrievers (72)
- Document Transformers (21) · Graphs (16) · Callbacks (16) · Stores (9)
- Chat Loaders (7) · Middleware (4) · Splitters (3) · Adapters (2) · Others (4)

### JavaScript (`oss/javascript/integrations/`) — 323 files
- Chat models · LLMs · Embeddings · Document loaders · Vector stores
- Retrievers · Tools · Stores · Providers · Middleware · Callbacks

### Shared (`oss/shared/`) — 5 files

## Reference (`oss/reference/`)
- API reference (Agent Server API, Control Plane API)

## Contributing (`oss/contributing/`)
- OSS contribution guides

## Monorepo Source Docs

### langchain/ (29 files)
- Core, text-splitters, model-profiles, standard-tests
- Partners: anthropic, chroma, deepseek, exa, fireworks, groq, huggingface, mistralai, nomic, ollama, openai, openrouter, perplexity, qdrant, xai

### langgraph/ (15 files)
- Core, prebuilt, CLI, SDK (JS/Python)
- Checkpoints: postgres, sqlite, conformance

### deepagents/ (50 files)
- CLI, ACP, Harbor, examples (content-builder, deep-research, downloading, nvidia, ralph-mode, text-to-sql)
- Partners: daytona, modal, quickjs, runloop
