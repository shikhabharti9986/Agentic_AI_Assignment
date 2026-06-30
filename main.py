"""CLI demo for the store support agent."""

from __future__ import annotations

import argparse

from dotenv import load_dotenv

from src.agent.run_agent import run_agent


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Online store support agent")
    parser.add_argument("question", nargs="?", help="Customer question to answer")
    args = parser.parse_args()

    if args.question:
        print(run_agent(args.question))
        return

    examples = [
        "Where is order ORD-1002?",
        "Is there a cheaper alternative to the shoes I ordered in ORD-1002?",
        "Tell me about product P-201",
        "Do you have wireless earbuds?",
        "Where is order ORD-9999?",
    ]
    for question in examples:
        print(f"\nQ: {question}\nA: {run_agent(question)}\n{'-' * 60}")


if __name__ == "__main__":
    main()
