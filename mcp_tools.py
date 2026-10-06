"""LangChain tool wrapper for the local MCP server; no direct RAG import."""
import os
import sys
from pathlib import Path

import anyio
from langchain_core.tools import tool
from mcp import Client, StdioServerParameters
from mcp.types import TextContent


PROJECT_DIR = Path(__file__).resolve().parent


def _server_parameters() -> StdioServerParameters:
    return StdioServerParameters(
        command=sys.executable,
        args=[str(PROJECT_DIR / "mcp_server.py")],
        cwd=str(PROJECT_DIR),
        env=dict(os.environ),
    )


async def _call_mcp_tool(name: str, arguments: dict) -> str:
    async with Client(_server_parameters()) as client:
        result = await client.call_tool(name, arguments)

    text_blocks = [
        block.text for block in result.content if isinstance(block, TextContent)
    ]
    text = "\n".join(text_blocks)

    if result.is_error:
        detail = text.strip() or "MCP tool returned an unspecified error."
        raise RuntimeError(f"MCP tool '{name}' failed: {detail}")

    if not text.strip():
        raise RuntimeError(f"MCP tool '{name}' returned no text content.")

    return text


def _call(name: str, arguments: dict) -> str:
    return anyio.run(_call_mcp_tool, name, arguments)


@tool
def mcp_search_travel_knowledge(query: str, k: int = 4) -> str:
    """Search company travel-policy evidence through the local MCP server."""
    return _call("search_travel_knowledge", {"query": query, "k": k})
