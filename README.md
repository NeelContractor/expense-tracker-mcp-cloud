# Expense Tracker MCP Server

A simple Expense Tracker MCP server built with FastMCP and SQLite, deployed on FastMCP Cloud.

This project demonstrates how to build, deploy, and connect an MCP server using FastMCP Cloud and Claude Desktop.

## Features

### Tools

* **add_expense** — Add a new expense.
* **list_expenses** — View expenses within a date range.
* **summarize** — Generate expense summaries by category.

### Resources

* **expense:///categories** — Returns available expense categories and subcategories.

## Tech Stack

* Python 3.14+
* FastMCP 3.4.0
* SQLite
* aiosqlite
* FastMCP Cloud

## Local Development

Run the server locally:

```bash
uv run python main.py
```

Open MCP Inspector:

```bash
uv run fastmcp dev inspector main.py
```

## Deployment

This project is deployed to FastMCP Cloud.

Remote MCP Endpoint:

```text
https://splendid-gold-dingo.fastmcp.app/mcp
```

## Claude Desktop Integration

Create a local proxy server:

```python
from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://splendid-gold-dingo.fastmcp.app/mcp",
    name="Neel Server Proxy"
)

if __name__ == "__main__":
    mcp.run()
```

Install the proxy into Claude Desktop:

```bash
uv run fastmcp install claude-desktop proxy.py
```

Restart Claude Desktop after installation.

## Example Prompts

Add an expense:

```text
Add an expense for a cab ride to Delhi last Sunday. The fare was ₹600.
```

List expenses:

```text
Show all expenses between 2026-06-01 and 2026-06-30.
```

Summarize expenses:

```text
Summarize my expenses for June 2026.
```

## Categories

The server supports categories such as:

* Food
* Transport
* Housing
* Utilities
* Health
* Education
* Entertainment
* Shopping
* Travel
* Business
* Investments
* Personal Care
* Taxes
* Miscellaneous

## Learning Goal

This project was created to learn:

* FastMCP fundamentals
* MCP tools and resources
* SQLite integration
* Async MCP tools with aiosqlite
* FastMCP Cloud deployment
* Claude Desktop integration via MCP