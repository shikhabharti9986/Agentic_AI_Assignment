# Online Store Support Agent

An AI-powered customer support agent for an online store that can answer questions about orders, products, recommendations, and cheaper alternatives.

The project uses Gemini API, Streamlit, and a modular agent architecture.

---

# Features

* AI-powered customer support agent
* Gemini LLM integration
* Modern Streamlit chat interface
* Product search support
* Order tracking support
* Product recommendations
* Cheaper alternative suggestions
* Error handling for invalid queries
* Logging support using `agent.log`
* Modular project structure

---

# Project Structure

```text
store-ai-agent/
│
├── app/
│   └── streamlit_app.py
│
├── docs/
│
├── src/
│   ├── agent/
│   │   └── run_agent.py
│   │
│   ├── tools/
│   │   ├── orders.py
│   │   ├── products.py
│   │   └── search.py
│   │
│   └── data/
│       ├── orders.json
│       └── products.json
│
├── venv/
├── .env
├── .env.example
├── .gitignore
├── agent.log
├── main.py
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/shikhabharti9986/Agentic_AI_Assignment.git
```

Move into project folder:

```bash
cd Agentic_AI_Assignment
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Run the Application

Start Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

---

# Example Questions

* Where is order ORD-1002?
* Tell me about product P-201
* Do you have running shoes?
* Is there a cheaper alternative?
* Best products in market

---

# Technologies Used

* Python
* Streamlit
* Gemini API
* google-genai
* python-dotenv
* Git & GitHub

---

# Agent Workflow

1. User asks a question
2. Agent detects intent
3. Appropriate tools are selected
4. Tool outputs are processed
5. Customer-friendly response is generated

---

# Bonus Features

* Gemini AI integration
* Streamlit chat UI
* Logging support
* Modular architecture
* GitHub repository

---

# Author

Shikha Bharti
