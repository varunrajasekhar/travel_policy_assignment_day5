# Assignment 2 - Travel Policy Sub-agents + MCP

Extend your completed Assignment 1 travel-policy assistant. This is an
intentionally incomplete starter, not a finished solution.

## Before you begin
Replace `rag.py` with your completed Assignment 1 `rag.py`. The included copy
is the original Assignment 1 scaffold, provided only for compatibility.
Do not redo its TODOs if you already completed Assignment 1. Keep the supplied
`knowledge/` files unchanged. RAG remains the evidence source; the NEW work is
sub-agent delegation and the MCP protocol boundary.

## Complete
Finish TODOs 1-9 in `mcp_server.py`, `mcp_tools.py`, and `agent.py`.
Read `Assignment2_Problem_Statement.docx` for the detailed requirements.
Do not import RAG into agent.py or mcp_tools.py. Workers retrieve through MCP.

## Local setup
Python 3.11+ and a running Ollama installation are required.

macOS/Linux:
```sh
python3 -m venv .venv
source .venv/bin/activate
```
Windows PowerShell:
```powershell
python -m venv .venv
```
Then:
```sh
python -m pip install -r requirements.txt
ollama pull qwen2.5:7b
python main.py
```
