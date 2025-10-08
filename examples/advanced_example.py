#!/usr/bin/env python3
"""
Advanced example demonstrating error handling and edge cases.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.client.mcp_client import MCPClient
from mcp_demo.agents.calculator import CalculatorAgent
from mcp_demo.agents.weather import WeatherAgent
from mcp_demo.agents.file import FileAgent


def print_result(description, result):
    """Print a formatted result."""
    print(f"\n{description}")
    if result.get("success"):
        print(f"  ✓ Success: {result}")
    else:
        print(f"  ✗ Error: {result.get('error', 'Unknown error')}")


def main():
    """Run advanced examples."""
    print("=" * 60)
    print("MCP Demo - Advanced Examples")
    print("=" * 60)
    
    # Setup
    server = MCPServer()
    server.register_agent(CalculatorAgent())
    server.register_agent(WeatherAgent())
    server.register_agent(FileAgent())
    client = MCPClient(server)
    
    # Error Handling Examples
    print("\n--- Error Handling Examples ---")
    
    # 1. Division by zero
    result = client.execute_action("calculator", "divide", {"a": 10, "b": 0})
    print_result("Division by zero", result)
    
    # 2. Unknown agent
    result = client.execute_action("unknown_agent", "action", {})
    print_result("Unknown agent", result)
    
    # 3. Unknown action
    result = client.execute_action("calculator", "unknown_action", {"a": 1})
    print_result("Unknown action", result)
    
    # 4. Invalid parameters
    result = client.execute_action("calculator", "add", {"x": 1, "y": 2})
    print_result("Invalid parameters (defaults to 0)", result)
    
    # 5. Non-existent file
    result = client.execute_action("file", "read", {"filename": "nonexistent.txt"})
    print_result("Reading non-existent file", result)
    
    # Advanced Use Cases
    print("\n--- Advanced Use Cases ---")
    
    # 1. Chained operations
    print("\nChained calculator operations:")
    result1 = client.execute_action("calculator", "add", {"a": 10, "b": 5})
    if result1.get("success"):
        result2 = client.execute_action("calculator", "multiply", {"a": result1["result"], "b": 2})
        if result2.get("success"):
            result3 = client.execute_action("calculator", "subtract", {"a": result2["result"], "b": 10})
            print(f"  (10 + 5) * 2 - 10 = {result3.get('result')}")
    
    # 2. Multiple weather forecasts
    print("\nMultiple city weather:")
    cities = ["Paris", "Tokyo", "New York", "London"]
    for city in cities:
        result = client.execute_action("weather", "get_weather", {"city": city})
        if result.get("success"):
            print(f"  {city}: {result['temperature']}°C, {result['condition']}")
    
    # 3. File batch operations
    print("\nBatch file operations:")
    files = [
        {"name": "file1.txt", "content": "Content 1"},
        {"name": "file2.txt", "content": "Content 2"},
        {"name": "file3.txt", "content": "Content 3"}
    ]
    
    # Write multiple files
    for file_info in files:
        result = client.execute_action("file", "write", {
            "filename": file_info["name"],
            "content": file_info["content"]
        })
        if result.get("success"):
            print(f"  ✓ Written: {file_info['name']}")
    
    # List all files
    result = client.execute_action("file", "list", {})
    if result.get("success"):
        print(f"  Total files: {result['count']}")
    
    # Read and verify
    for file_info in files:
        result = client.execute_action("file", "read", {"filename": file_info["name"]})
        if result.get("success") and result["content"] == file_info["content"]:
            print(f"  ✓ Verified: {file_info['name']}")
    
    # Clean up
    for file_info in files:
        client.execute_action("file", "delete", {"filename": file_info["name"]})
    
    # 4. Agent introspection
    print("\n--- Agent Introspection ---")
    agents = client.list_agents()
    for agent in agents:
        print(f"\nAgent: {agent['name']}")
        print(f"  Description: {agent['description']}")
        print(f"  Capabilities ({len(agent['capabilities'])}): {', '.join(agent['capabilities'])}")
    
    print("\n" + "=" * 60)
    print("Advanced examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
