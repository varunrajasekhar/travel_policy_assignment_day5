"""Expose the completed Assignment 1 retrieval function over local MCP."""
from contextlib import redirect_stdout
import sys

from mcp.server import MCPServer

from rag import search_travel_knowledge as _search_travel_knowledge


mcp = MCPServer("Travel Policy MCP")


@mcp.tool()
def search_travel_knowledge(query: str, k: int = 4) -> str:
    """Retrieve company travel-policy evidence with source filenames."""
    with redirect_stdout(sys.stderr):
        return _search_travel_knowledge(query, k)


if __name__ == "__main__":
    mcp.run(transport="stdio")
