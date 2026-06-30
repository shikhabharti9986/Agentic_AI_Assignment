# Design Decisions

## 1. Goal

Build an agent that answers online store customer questions by deciding which tools to use, chaining them when necessary, and returning grounded, customer-friendly responses.

## 2. Architecture

The solution uses a simple three-stage pipeline:

```text
Customer Question
      |
      v
   Planner  -> intent + initial tool calls
      |
      v
  Executor  -> run tools + dynamic chaining
      |
      v
  Responder -> friendly final answer
```

This separation keeps responsibilities clear:

- **Planner** decides what to do.
- **Executor** performs actions and handles follow-up logic.
- **Responder** formats the answer for the customer.

## 3. Tool Design

Three tools wrap mock store data:

| Tool | Purpose | Failure Mode |
|------|---------|--------------|
| `get_order(order_id)` | Fetch order status and items | Raises error for unknown order IDs |
| `get_product(product_id)` | Fetch one product | Raises error for unknown product IDs |
| `search_products(query)` | Keyword search over catalog | Returns empty list when nothing matches |

Tools return structured data or explicit errors. They do not generate natural language responses. This keeps the agent honest: all customer-facing wording is created only after tool execution.

## 4. Intent Detection

The planner supports two modes:

### Rule-based planner (default)

Uses regular expressions and keyword heuristics to detect:

- order tracking
- product details
- product search
- cheaper alternatives

This mode requires no API key, is deterministic, and is easy to test.

### Optional LLM planner

If `OPENAI_API_KEY` is configured, the agent can ask an LLM to produce a JSON plan with intent and tool calls. This improves flexibility for varied phrasing while still grounding final answers in tool outputs.

If the LLM is unavailable, the rule-based planner is used automatically.

## 5. Tool Chaining

Some questions need more than one tool call.

Example:

> Is there a cheaper alternative to the shoes I ordered in ORD-1002?

Execution flow:

1. `get_order("ORD-1002")` to find ordered items
2. `get_product("P-101")` to learn category and price
3. `search_products("shoes")` to find same-category options
4. Compare prices and recommend a cheaper in-stock product

The executor handles this follow-up chaining after the initial plan, so the planner stays simple.

## 6. Error Handling Strategy

The agent handles failures explicitly:

- **Invalid order/product ID** – return a polite message asking the customer to verify the ID
- **Empty search results** – say no products matched; do not guess
- **Missing order ID in question** – ask for the order ID format
- **Unsupported question** – explain what the agent can help with

No fallback data is invented when tools fail.

## 7. Response Generation

Responses are generated in two layers:

1. **Template-based responses** – deterministic and always available
2. **Optional LLM polishing** – rewrites the answer in natural language using only tool results

Even with LLM polishing, the responder instructs the model not to invent orders, prices, stock status, or delivery dates.

## 8. Logging

Every question, selected intent, tool call, and tool result is logged through Python's `logging` module to:

- console
- `agent.log`

This helps during evaluation and debugging.

## 9. Testing Strategy

Unit tests cover:

- individual tool behavior
- planner intent detection
- end-to-end `run_agent` responses
- invalid order handling
- empty search handling
- cheaper alternative chaining

Tests run without an API key to keep CI/local execution simple.

## 10. Trade-offs

| Decision | Why |
|----------|-----|
| Mock in-memory data | Keeps the assignment self-contained and easy to run |
| Rule-based default | Works offline and is predictable for evaluation |
| Optional LLM layer | Adds flexibility without making the project API-dependent |
| Template responses | Guarantees grounded output even without an LLM |
| Streamlit UI | Simple way to demo the agent interactively |

## 11. Possible Improvements

- Persistent database instead of mock dictionaries
- Semantic product search instead of keyword matching
- Conversation memory for follow-up questions
- Authentication for customer-specific order lookup
- Structured JSON responses for frontend integration

## 12. Key Takeaway

The agent is designed to **plan**, **act**, and **explain** using real tool outputs. That makes it reliable for customer support scenarios where guessing is unacceptable.
