<<<<<<< HEAD
# Online Store Support Agent

A simple AI agent that answers customer questions for an online store by selecting the right tools, chaining them when needed, and returning clear customer-friendly responses.

## Features

- `run_agent(question: str) -> str` as the main assignment entry point
- Tool selection for:
  - `get_order(order_id)`
  - `search_products(query)`
  - `get_product(product_id)`
- Multi-step chaining for questions like cheaper alternatives
- Graceful handling of invalid orders/products and empty search results
- Rule-based planner with optional OpenAI enhancement
- Tool call logging to console and `agent.log`
- Streamlit web UI
- Unit tests with `pytest`

## Project Structure

```text
store-ai-agent/
├── src/
│   ├── agent/
│   │   ├── planner.py      # Intent detection and tool planning
│   │   ├── executor.py     # Tool execution and chaining
│   │   ├── responder.py    # Customer-friendly responses
│   │   └── run_agent.py    # Main run_agent function
│   ├── tools/
│   │   ├── data.py         # Mock store catalog and orders
│   │   └── store_tools.py  # Tool implementations
│   └── logging_config.py
├── app/
│   └── streamlit_app.py
├── tests/
│   └── test_agent.py
├── docs/
│   └── DESIGN.md
├── samples/
│   └── SAMPLE_IO.md
├── main.py
└── requirements.txt
```

## Setup

```bash
cd store-ai-agent
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Optional LLM support:

```bash
copy .env.example .env
# Add your OPENAI_API_KEY
```

The agent works without an API key using the built-in rule-based planner and response templates.

## Usage

### Python

```python
from src.agent.run_agent import run_agent

print(run_agent("Where is order ORD-1002?"))
```

### CLI demo

```bash
python main.py "Where is order ORD-1002?"
python main.py
```

### Streamlit UI

```bash
streamlit run app/streamlit_app.py
```

### Tests

```bash
pytest
```

## Approach

1. **Plan** – Detect intent from the question and choose initial tool calls.
2. **Execute** – Call tools in order and chain follow-up calls when needed.
3. **Respond** – Convert grounded tool outputs into a friendly answer without inventing data.

Example chaining for cheaper alternatives:

```text
Question -> get_order(ORD-1002)
         -> get_product(P-101)
         -> search_products("shoes")
         -> compare prices and respond
```

## Sample Data

Orders:

- `ORD-1001`, `ORD-1002`, `ORD-1003`

Products:

- Shoes: `P-101`, `P-102`, `P-103`
- Electronics: `P-201`, `P-202`
- Apparel: `P-301`

See `samples/SAMPLE_IO.md` for more example inputs and outputs.

## Design Notes

See `docs/DESIGN.md` for architecture and design decisions.

## Evaluation Checklist

- Correct tool selection
- Tool chaining for multi-step questions
- Error handling for invalid IDs and empty searches
- No fabricated data in responses
- Logging, tests, and optional web UI included
=======
# Agentic_AI_Assignment
>>>>>>> 5c6b71551b33b3c8173697412347d4f994f16ea6
