from fastmcp import FastMCP

# Create a proxy to your remote FastMCP Cloud server
# FastMCP Cloud uses Streamable HTTP (default), so just use the /mcp URL
mcp = FastMCP.as_proxy(
    "<YOUR_FASTMCP_CLOUD_URL>/mcp",  # Standard FastMCP Cloud URL, exmaple "https://splendid-gold-dingo.fastmcp.app/mcp"
    name="Neel Server Proxy"
)

if __name__ == "__main__":
    # This runs via STDIO, which Claude Desktop can connect to
    mcp.run()