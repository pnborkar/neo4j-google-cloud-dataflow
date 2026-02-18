import os
from neo4j import GraphDatabase
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

# =========================
# Environment Variables
# =========================
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

if not all([NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD]):
    raise ValueError("Missing Neo4j environment variables.")

# =========================
# Neo4j Driver Setup
# =========================
driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)

# =========================
# Tool Functions
# =========================

def get_schema():
    """Returns Neo4j database schema."""
    try:
        with driver.session() as session:
            result = session.run("CALL db.schema.visualization()")
            return str(result.data())
    except Exception as e:
        return f"Error fetching schema: {str(e)}"


def run_cypher(query: str):
    """Executes a Cypher query and returns results."""
    try:
        with driver.session() as session:
            result = session.run(query)
            return str(result.data())
    except Exception as e:
        return f"Error executing query: {str(e)}"


# =========================
# Register Tools
# =========================

schema_tool = FunctionTool(get_schema)
cypher_tool = FunctionTool(run_cypher)

# =========================
# Root Agent
# =========================

root_agent = LlmAgent(
    name="london_transport_assistant",
    model="gemini-2.0-flash",   # ✅ fixed model
    tools=[schema_tool, cypher_tool],  # ✅ tools attached
    instruction="""
You are a Neo4j graph assistant.
You help users understand schema, write Cypher queries,
and explain graph modeling concepts clearly.
"""
)