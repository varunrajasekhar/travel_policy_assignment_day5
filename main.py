"""Provided local runner. Finish the TODOs before running the assistant."""
import os
from langchain_ollama import ChatOllama
from agent import build_agent

def main():
    print("Travel Policy Assistant - Sub-agents + MCP")
    model = ChatOllama(model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"), temperature=0)
    try:
        agent = build_agent(model)
    except NotImplementedError as exc:
        print(f"Assignment is not complete yet: {exc}")
        return
    conversation = []
    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        pending = conversation + [{"role": "user", "content": question}]
        try:
            result = agent.invoke({"messages": pending})
            answer = result["messages"][-1].content
            print(f"Assistant: {answer}\n")
            conversation = pending + [{"role": "assistant", "content": answer}]
        except Exception as exc:
            print(f"Assistant error: {exc}")

if __name__ == "__main__":
    main()
