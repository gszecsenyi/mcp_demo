#!/usr/bin/env python3
"""
Basic example of using the MCP demo environment.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.client.mcp_client import MCPClient
from mcp_demo.agents.calculator import CalculatorAgent
from mcp_demo.agents.weather import WeatherAgent
from mcp_demo.agents.file import FileAgent


def print_section(title):
    """Print a section header."""
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print('=' * 60)


def main():
    """Run the basic example."""
    print_section("MCP Demo - Basic Example")
    
    # Create server
    server = MCPServer()
    
    # Register agents
    print("\n1. Registering agents...")
    server.register_agent(CalculatorAgent())
    server.register_agent(WeatherAgent())
    server.register_agent(FileAgent())
    
    # Create client
    client = MCPClient(server)
    
    # Get server info
    print_section("2. Server Information")
    server_info = client.get_server_info()
    print(f"Server: {server_info['server']}")
    print(f"Version: {server_info['version']}")
    print(f"Agents: {', '.join(server_info['agents'])}")
    
    # List agents
    print_section("3. Available Agents")
    agents = client.list_agents()
    for agent in agents:
        print(f"\nAgent: {agent['name']}")
        print(f"  Description: {agent['description']}")
        print(f"  Capabilities: {', '.join(agent['capabilities'])}")
    
    # Calculator examples
    print_section("4. Calculator Agent Examples")
    
    result = client.execute_action("calculator", "add", {"a": 10, "b": 5})
    print(f"10 + 5 = {result.get('result')}")
    
    result = client.execute_action("calculator", "multiply", {"a": 7, "b": 6})
    print(f"7 × 6 = {result.get('result')}")
    
    result = client.execute_action("calculator", "divide", {"a": 20, "b": 4})
    print(f"20 ÷ 4 = {result.get('result')}")
    
    # Weather examples
    print_section("5. Weather Agent Examples")
    
    result = client.execute_action("weather", "get_weather", {"city": "New York"})
    if result.get("success"):
        print(f"\nCurrent weather in {result['city']}:")
        print(f"  Temperature: {result['temperature']}°{result['unit'][0].upper()}")
        print(f"  Condition: {result['condition']}")
        print(f"  Humidity: {result['humidity']}%")
    
    result = client.execute_action("weather", "get_forecast", {"city": "London", "days": 3})
    if result.get("success"):
        print(f"\n3-day forecast for {result['city']}:")
        for day in result['forecast']:
            print(f"  Day {day['day']}: {day['condition']}, "
                  f"High: {day['temperature_high']}°C, Low: {day['temperature_low']}°C")
    
    # File operations examples
    print_section("6. File Agent Examples")
    
    # Write a file
    result = client.execute_action("file", "write", {
        "filename": "test.txt",
        "content": "Hello from MCP demo!"
    })
    print(f"Write file: {result.get('message')}")
    
    # Read the file
    result = client.execute_action("file", "read", {"filename": "test.txt"})
    if result.get("success"):
        print(f"Read file '{result['filename']}': {result['content']}")
    
    # List files
    result = client.execute_action("file", "list", {})
    if result.get("success"):
        print(f"Files in directory: {', '.join(result['files']) if result['files'] else 'none'}")
    
    # Check if file exists
    result = client.execute_action("file", "exists", {"filename": "test.txt"})
    if result.get("success"):
        print(f"File 'test.txt' exists: {result['exists']}")
    
    print_section("Example completed!")


if __name__ == "__main__":
    main()
