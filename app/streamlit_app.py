from __future__ import annotations

import os
import sys

# Add project root to Python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import streamlit as st
from dotenv import load_dotenv

from src.agent.run_agent import run_agent

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Store AI Agent",
    page_icon="🛍️",
    layout="wide",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    .stChatMessage {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
    }

    .user-msg {
        background-color: #1E293B;
        padding: 12px;
        border-radius: 10px;
    }

    .bot-msg {
        background-color: #111827;
        padding: 12px;
        border-radius: 10px;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown(
    "<div class='title'>🛍️ Store AI Agent</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Ask about orders, products, recommendations, and deals.</div>",
    unsafe_allow_html=True,
)

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Example Questions")

    examples = [
        "Where is order ORD-1002?",
        "Tell me about product P-201",
        "Do you have running shoes?",
        "Best products in market",
        "Cheaper alternatives for headphones",
    ]

    for ex in examples:
        if st.button(ex):
            st.session_state.messages.append(
                {"role": "user", "content": ex}
            )

            answer = run_agent(ex)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

# Display chat messages
for message in st.session_state.messages:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])

    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Chat input
prompt = st.chat_input(
    "Ask about products, orders, or recommendations..."
)

if prompt:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = run_agent(prompt)

            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
