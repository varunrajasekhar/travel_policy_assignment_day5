"""LangChain tool wrapper for the local MCP server; no direct RAG import."""
import anyio
import os
import sys
from pathlib import Path
from langchain_core.tools import tool
from mcp import Client, StdioServerParameters

PROJECT_DIR = Path(__file__).resolve().parent

def _server_parameters() -> StdioServerParameters:
    # TODO 3: use sys.executable, mcp_server.py's absolute path,
    # cwd=str(PROJECT_DIR), and env=dict(os.environ).
    raise NotImplementedError("TODO 3: configure the MCP subprocess")

async def _call_mcp_tool(name: str, arguments: dict) -> str:
    # TODO 4: open Client(_server_parameters()) with async with.
    # Await client.call_tool(name, arguments). Check result.is_error;
    # raise RuntimeError with the returned text if the tool failed.
    # Join text content blocks using newlines; reject an empty text result.
    raise NotImplementedError("TODO 4: call MCP and read its text result")

def _call(name: str, arguments: dict) -> str:
    return anyio.run(_call_mcp_tool, name, arguments)

@tool
def mcp_search_travel_knowledge(query: str, k: int = 4) -> str:
    """Search company travel-policy evidence through the local MCP server."""
    # TODO 5: return _call("search_travel_knowledge", {"query": query, "k": k}).
    raise NotImplementedError("TODO 5: connect the LangChain tool to MCP")
