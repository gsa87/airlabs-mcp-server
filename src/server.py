#!/usr/bin/env python3
import os
from fastmcp import FastMCP
from tools import register_airlabs

# Initialize the server with a descriptive name for the public repo
mcp = FastMCP("airlabs-mcp-server")

# Register only the AirLabs tools
register_airlabs(mcp)

@mcp.tool(description="Get information about the AirLabs MCP server")
def get_server_info() -> dict:
    """
    Returns metadata about the running AirLabs MCP server.
    """
    return {
        "server_name": "AirLabs Flight Data Server",
        "version": "1.0.0",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "python_version": os.sys.version.split()[0]
    }

if __name__ == "__main__":
    # Default to port 8000 if not specified
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"Starting AirLabs MCP server on {host}:{port}")
    
    # Run the server using HTTP transport (compatible with Poke/Claude)
    mcp.run(
        transport="http",
        host=host,
        port=port,
        stateless_http=True
    )