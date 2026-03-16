# Deep Agents Learning Plan

A structured path to learn Deep Agents from the docs and source code in this repository.

All documentation paths are relative to `docs/src/oss/deepagents/`.

---

## Phase 1: Foundations

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 1 | Overview | `overview.mdx` | What Deep Agents is, core capabilities, when to use |
| 2 | Quickstart | `quickstart.mdx` | Build your first deep agent with planning and tools |
| 3 | Harness Capabilities | `harness.mdx` | Planning, filesystem, subagents, context management |
| 4 | Comparison | `comparison.mdx` | Deep Agents vs LangChain vs LangGraph |
| 5 | Models | `models.mdx` | Supported models and providers |

## Phase 2: Core Features

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 6 | Customization | `customization.mdx` | Custom tools, prompts, subagents |
| 7 | Backends | `backends.mdx` | Filesystem backends (in-memory, disk, store) |
| 8 | Sandboxes | `sandboxes.mdx` | Isolated code execution (Modal, Daytona, Deno) |
| 9 | Long-term Memory | `long-term-memory.mdx` | Persistent memory across conversations |
| 10 | Skills | `skills.mdx` | Reusable skill modules |
| 11 | Subagents | `subagents.mdx` | Task delegation and context isolation |
| 12 | Data Analysis | `data-analysis.mdx` | Working with data and files |

## Phase 3: Advanced Capabilities

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 13 | Streaming | `streaming.mdx` | Real-time agent output streaming |
| 14 | Human-in-the-loop | `human-in-the-loop.mdx` | Approval flows and interrupts |
| 15 | Data Locations | `data-locations.mdx` | Where agent data is stored |
| 16 | ACP | `acp.mdx` | Agent Context Protocol |

## Phase 4: CLI

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 17 | CLI Overview | `cli/overview.mdx` | Terminal coding agent |
| 18 | Configuration | `cli/configuration.mdx` | CLI config and settings |
| 19 | Providers | `cli/providers.mdx` | Model providers for CLI |
| 20 | MCP Tools | `cli/mcp-tools.mdx` | Model Context Protocol integration |

## Phase 5: Frontend Integration

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 21 | Frontend Overview | `frontend/overview.mdx` | Building UIs for deep agents |
| 22 | Todo List | `frontend/todo-list.mdx` | Displaying agent task lists |
| 23 | Subagent Streaming | `frontend/subagent-streaming.mdx` | Streaming subagent output |

## Phase 6: Examples & Real-World Patterns

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 24 | Deep Research | `examples/deep_research/` | Multi-step web research agent |
| 25 | Content Builder | `examples/content-builder-agent/` | Content writing with memory and skills |
| 26 | Text-to-SQL | `examples/text-to-sql-agent/` | Natural language SQL queries |
| 27 | Ralph Mode | `examples/ralph_mode/` | Autonomous looping pattern |
| 28 | Downloading Agents | `examples/downloading_agents/` | Agent distribution pattern |

## Phase 7: Source Code Deep Dive

| # | Topic | Source | What you'll learn |
|---|-------|--------|-------------------|
| 29 | Core Graph | `deepagents/libs/deepagents/deepagents/graph.py` | Agent implementation |
| 30 | Backends | `deepagents/libs/deepagents/deepagents/backends/` | Filesystem backends |
| 31 | Middleware | `deepagents/libs/deepagents/deepagents/middleware/` | Built-in middleware |
| 32 | CLI Implementation | `deepagents/libs/cli/deepagents_cli/` | Terminal UI with Textual |
| 33 | ACP Protocol | `deepagents/libs/acp/deepagents_acp/` | Agent Context Protocol |
| 34 | Harbor | `deepagents/libs/harbor/` | Evaluation framework |

---

## Suggested Pace

- **Week 1:** Phases 1-2 — Core concepts and basic customization
- **Week 2:** Phase 3 — Advanced features (streaming, human-in-the-loop)
- **Week 3:** Phase 4-5 — CLI and frontend integration
- **Week 4:** Phases 6-7 — Real-world examples and source code

---

## Key Concepts

### What Makes Deep Agents Different

Deep Agents is an **agent harness** — batteries-included agent with:
- **Planning** — `write_todos` for task breakdown
- **Filesystem** — `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep`
- **Shell access** — `execute` for running commands (with sandboxing)
- **Sub-agents** — `task` for delegating work with isolated context
- **Smart defaults** — Prompts that teach the model how to use tools
- **Context management** — Auto-summarization and large output handling

### Architecture

```
┌─────────────────────────────────────┐
│         Deep Agents SDK             │
│  ┌─────────┐ ┌─────────┐ ┌────────┐ │
│  │ Planning│ │Filesystem│ │Subagent│ │
│  │  Tools  │ │  Tools   │ │  Tools │ │
│  └─────────┘ └─────────┘ └────────┘ │
│  ┌─────────┐ ┌─────────┐ ┌────────┐ │
│  │  Skills │ │ Memory  │ │Context │ │
│  │         │ │         │ │  Mgmt  │ │
│  └─────────┘ └─────────┘ └────────┘ │
└─────────────────────────────────────┘
│           LangGraph Runtime           │
│    (durable execution, streaming)     │
└─────────────────────────────────────┘
│           LangChain Core              │
│    (models, tools, messages)          │
└─────────────────────────────────────┘
```

### Core Libraries

| Library | Path | Purpose |
|---------|------|---------|
| `deepagents` | `deepagents/libs/deepagents/` | Core SDK |
| `deepagents-cli` | `deepagents/libs/cli/` | Terminal UI |
| `deepagents-acp` | `deepagents/libs/acp/` | Agent Context Protocol |
| `deepagents-harbor` | `deepagents/libs/harbor/` | Evaluation framework |

---

## Integration with LangChain & LangGraph

Deep Agents builds on both:
- **LangChain** — Models, tools, messages
- **LangGraph** — Runtime for durable execution, streaming, persistence
- `create_deep_agent()` returns a compiled LangGraph graph

See `LANGCHAIN_LEARNING_PLAN.md` and `LANGGRAPH_LEARNING_PLAN.md` for prerequisites.
