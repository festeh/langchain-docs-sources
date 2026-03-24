import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Lesson 9: Structured Output

    Stop parsing free text — make the model return validated data structures you can use directly.
    """)
    return


@app.cell
def _(ChatOpenAI, os):
    MODEL = "glm-5"

    llm = ChatOpenAI(
        base_url=os.environ["AI_ENDPOINT"] + "/v1",
        api_key=os.environ["AI_KEY"],
        model=MODEL,
    )
    return (llm,)


@app.cell
def _(mo):
    mo.md("""
    ## The Problem with Free Text

    Ask a model to extract data and you get prose. Ask it to return JSON and you get *almost* JSON. Structured output solves this — the model returns a validated object that matches your schema.

    ```
    Without:  "The sentiment is positive and the rating is 4 out of 5."
    With:     ProductReview(sentiment="positive", rating=4)
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## with_structured_output

    Call `.with_structured_output(Schema)` on any chat model. It returns a new model that produces schema instances instead of `AIMessage` objects.
    """)
    return


@app.cell
def _(BaseModel, Field, Literal, llm, mo):
    class ReviewAnalysis(BaseModel):
        """Analysis of a product review."""
        sentiment: Literal["positive", "negative", "mixed"] = Field(
            description="Overall sentiment of the review"
        )
        rating: int = Field(description="Rating from 1-5", ge=1, le=5)
        key_points: list[str] = Field(
            description="Main points made in the review, 1-3 words each"
        )

    structured_llm = llm.with_structured_output(ReviewAnalysis)

    review = structured_llm.invoke(
        "Amazing laptop! Fast processor, great screen. "
        "Battery could be better though. 4 out of 5."
    )

    mo.md(f"""
    **Type:** `{type(review).__name__}`

    | Field | Value |
    |-------|-------|
    | `sentiment` | `{review.sentiment}` |
    | `rating` | `{review.rating}` |
    | `key_points` | `{review.key_points}` |

    No parsing. No regex. A validated Pydantic instance you can use directly.
    """)
    return (ReviewAnalysis,)


@app.cell
def _(mo):
    mo.md("""
    ## Schema Types

    `with_structured_output` accepts three schema types. Each returns data differently.
    """)
    return


@app.cell
def _(Annotated, BaseModel, Field, Literal, TypedDict, llm, mo):
    # 1. Pydantic model — returns a validated instance
    class ContactPydantic(BaseModel):
        """Contact information."""
        name: str = Field(description="Full name")
        email: str = Field(description="Email address")

    # 2. TypedDict — returns a plain dict
    class ContactTypedDict(TypedDict):
        """Contact information."""
        name: Annotated[str, "Full name"]
        email: Annotated[str, "Email address"]

    # 3. JSON Schema — returns a plain dict
    contact_json_schema = {
        "title": "Contact",
        "description": "Contact information.",
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Full name"},
            "email": {"type": "string", "description": "Email address"},
        },
        "required": ["name", "email"],
    }

    prompt = "Extract: Jane Smith, jane@example.com"

    r_pydantic = llm.with_structured_output(ContactPydantic).invoke(prompt)
    r_typed = llm.with_structured_output(ContactTypedDict).invoke(prompt)
    r_json = llm.with_structured_output(contact_json_schema).invoke(prompt)

    mo.md(f"""
    | Schema type | Returns | Result |
    |-------------|---------|--------|
    | **Pydantic** | Validated instance | `{r_pydantic}` |
    | **TypedDict** | Plain dict | `{r_typed}` |
    | **JSON Schema** | Plain dict | `{r_json}` |

    Pydantic gives you validation. TypedDict and JSON Schema give you flexibility.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Pydantic Validation

    Pydantic schemas enforce constraints. If the model returns `rating: 10` but your schema says `le=5`, validation catches it. Combined with LangChain's retry logic, the model gets a second chance to fix its output.
    """)
    return


@app.cell
def _(BaseModel, Field, llm, mo):
    class StrictRating(BaseModel):
        """A product rating."""
        score: int = Field(description="Score from 1 to 5", ge=1, le=5)
        summary: str = Field(description="One-sentence summary")

    strict_llm = llm.with_structured_output(StrictRating)

    # Even an ambiguous prompt should produce a valid 1-5 score
    result = strict_llm.invoke(
        "This product is incredible, 11 out of 10! Best purchase ever."
    )

    valid = 1 <= result.score <= 5

    mo.md(f"""
    **Input:** "This product is incredible, 11 out of 10!"

    | Field | Value | Valid? |
    |-------|-------|--------|
    | `score` | `{result.score}` | `{valid}` (constrained to 1-5) |
    | `summary` | "{result.summary}" | |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## include_raw

    Set `include_raw=True` to get both the raw `AIMessage` and the parsed output. Useful for debugging or when you need token counts alongside structured data.
    """)
    return


@app.cell
def _(ReviewAnalysis, llm, mo):
    raw_llm = llm.with_structured_output(ReviewAnalysis, include_raw=True)

    raw_result = raw_llm.invoke("Decent phone. Camera is good, price is fair. 3/5.")

    ai_msg = raw_result["raw"]
    parsed = raw_result["parsed"]
    error = raw_result["parsing_error"]

    mo.md(f"""
    The result is a dict with three keys:

    | Key | Value |
    |-----|-------|
    | `raw` | `{type(ai_msg).__name__}` — the original model response |
    | `parsed` | `{parsed}` |
    | `parsing_error` | `{error}` |

    Token usage from raw: `{ai_msg.usage_metadata}`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Methods

    Three methods control *how* the model produces structured output:

    | Method | How it works | Reliability |
    |--------|-------------|-------------|
    | `"json_schema"` | Provider enforces schema server-side | Highest — guaranteed match |
    | `"function_calling"` | Uses tool calling under the hood | High — works with most models |
    | `"json_mode"` | Model returns JSON, you describe schema in prompt | Lower — no schema enforcement |

    ```python
    # Specify a method explicitly
    llm.with_structured_output(Schema, method="function_calling")
    ```

    Default depends on the provider. For OpenAI-compatible models, `"function_calling"` is the safest default.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Multiple Output Types with Union

    When the model might return different structures, use `Union` types. The model picks the best match based on context.
    """)
    return


@app.cell
def _(BaseModel, Field, Literal, Union, llm, mo):
    class PersonInfo(BaseModel):
        """Information about a person."""
        name: str = Field(description="Person's full name")
        role: str = Field(description="Person's role or title")

    class EventInfo(BaseModel):
        """Information about an event."""
        event_name: str = Field(description="Name of the event")
        date: str = Field(description="Event date")
        location: str = Field(description="Event location")

    union_llm = llm.with_structured_output(Union[PersonInfo, EventInfo])

    r_person = union_llm.invoke("Tell me about Marie Curie, the physicist.")
    r_event = union_llm.invoke("PyCon 2025 is in Pittsburgh on May 14-22.")

    mo.md(f"""
    | Input | Type returned | Result |
    |-------|-------------|--------|
    | Person query | `{type(r_person).__name__}` | `{r_person}` |
    | Event query | `{type(r_event).__name__}` | `{r_event}` |

    The model reads the schema descriptions and picks the right one.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## With Agents

    When using `create_agent`, pass your schema as `response_format`. The agent handles the full cycle — tool calls, retries, validation — and returns the structured result in `result["structured_response"]`.

    ```python
    from langchain.agents import create_agent

    agent = create_agent(
        model=llm,
        tools=[search_tool],
        response_format=ReviewAnalysis,  # schema goes here
    )

    result = agent.invoke({
        "messages": [{"role": "user", "content": "Review this product..."}]
    })
    result["structured_response"]
    # ReviewAnalysis(sentiment="positive", rating=4, ...)
    ```

    Two strategies control how the agent generates structured output:

    | Strategy | When to use |
    |----------|-------------|
    | `ProviderStrategy(Schema)` | Provider supports native structured output (OpenAI, Anthropic) |
    | `ToolStrategy(Schema)` | All other models — uses tool calling under the hood |

    Pass a bare schema and LangChain picks the best strategy for your model. We'll use this hands-on in lesson 10.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    > **Structured output turns prose into data.** Use `with_structured_output(Schema)` on any model for direct extraction. Use Pydantic for validation, TypedDict or JSON Schema for flexibility. In agents, pass `response_format` and let LangChain handle the rest.

    **Next:** Lesson 10 — Agents (Deep Dive)
    """)
    return


@app.cell
def _():
    import os
    from typing import Annotated, Literal, Union

    import marimo as mo
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel, Field
    from typing_extensions import TypedDict

    return (
        Annotated,
        BaseModel,
        ChatOpenAI,
        Field,
        Literal,
        TypedDict,
        Union,
        mo,
        os,
    )


if __name__ == "__main__":
    app.run()
