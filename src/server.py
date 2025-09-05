import sqlite3
from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("sqlite-demo")

# Khởi tạo bảng player nếu chưa có
def init_db():
    conn = sqlite3.connect("demo.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        sport TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@mcp.tool()
def add_data(query: str) -> bool:
    """Execute an INSERT query to add a record into player table."""
    conn = sqlite3.connect("demo.db")
    conn.execute(query)
    conn.commit()
    conn.close()
    return True 

@mcp.tool()
def read_data(query: str = "SELECT * FROM player") -> list:
    """Execute a SELECT query and return all records from player table."""
    conn = sqlite3.connect("demo.db")
    results = conn.execute(query).fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Starting server...")
    mcp.run(transport="sse")
