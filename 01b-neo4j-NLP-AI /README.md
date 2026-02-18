# Neo4j + AI Integration (MCP + Claude Desktop)

## Overview
This project demonstrates how to connect Neo4j AuraDB to modern AI assistants using the Model Context Protocol (MCP).

It enables natural language questions to be translated into Cypher queries and executed directly against a live graph database.


## Prerequistics 
•	Neo4j AuraDB instance
•	Claude Desktop installed
•	Python 3.10+
•	uv (https://github.com/astral-sh/uv)


## Setup
# Install uv:
    brew install uv

# Configure Claude Desktop MCP
Open Claude Desktop → Settings → Developer → Edit Config

Add the following to claude_desktop_config.json:
```
    {
    "mcpServers": {
        "neo4j": {
        "command": "uvx",
        "args": [
            "mcp-neo4j-cypher",
            "--db-url", "neo4j+s://<YOUR_AURA_ENDPOINT>",
            "--username", "neo4j",
            "--password", "<YOUR_PASSWORD>"
        ]
        }
    }
    }
```

# Start Claude Desktop 
![01-MCP](./images/neo4j_mcp.png)

# Ask questions 

![01-Schema](./images/schema.png)

![01-Query1](./images/query_1.png)

![01-Query1](./images/query_1a.png)

![01-Query2](./images/query_2.png)



