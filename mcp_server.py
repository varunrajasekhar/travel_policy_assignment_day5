"""Expose the completed Assignment 1 retrieval function over local MCP."""
from contextlib import redirect_stdout
import sys
from mcp.server import MCPServer
from rag import search_travel_knowledge as _search_travel_knowledge

mcp = MCPServer("Travel Policy MCP")

@mcp.tool()
def search_travel_knowledge(query: str, k: int = 4) -> str:
    """Retrieve company travel-policy evidence with source filenames."""
    # TODO 1: call _search_travel_knowledge(query, k) and return its JSON text.
    # Redirect stdout to sys.stderr while retrieval runs. MCP owns stdout.
    raise NotImplementedError("TODO 1: expose retrieval through MCP")

if __name__ == "__main__":
    # TODO 2: start the MCP server using the stdio transport.
    raise NotImplementedError("TODO 2: run the MCP server")
