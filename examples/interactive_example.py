#!/usr/bin/env python3
"""
Interactive example of the MCP demo environment.
Allows users to interact with agents through a simple CLI.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.client.mcp_client import MCPClient
from mcp_demo.agents.calculator import CalculatorAgent
from mcp_demo.agents.weather import WeatherAgent
from mcp_demo.agents.file import FileAgent


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 60)
    print("MCP Demo - Interactive Mode")
    print("=" * 60)
    print("1. List all agents")
    print("2. Use Calculator")
    print("3. Get Weather")
    print("4. File Operations")
    print("5. Server Info")
    print("0. Exit")
    print("=" * 60)


def calculator_menu(client):
    """Calculator submenu."""
    print("\nCalculator Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("\nSelect operation (1-4): ").strip()
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        actions = {"1": "add", "2": "subtract", "3": "multiply", "4": "divide"}
        action = actions.get(choice)
        
        if action:
            result = client.execute_action("calculator", action, {"a": a, "b": b})
            if result.get("success"):
                print(f"\nResult: {result['result']}")
            else:
                print(f"\nError: {result.get('error')}")
        else:
            print("\nInvalid choice!")
    except ValueError:
        print("\nInvalid input! Please enter numbers.")


def weather_menu(client):
    """Weather submenu."""
    print("\nWeather Operations:")
    print("1. Current Weather")
    print("2. Forecast")
    
    choice = input("\nSelect operation (1-2): ").strip()
    city = input("Enter city name: ").strip()
    
    if choice == "1":
        result = client.execute_action("weather", "get_weather", {"city": city})
        if result.get("success"):
            print(f"\nWeather in {result['city']}:")
            print(f"  Temperature: {result['temperature']}°C")
            print(f"  Condition: {result['condition']}")
            print(f"  Humidity: {result['humidity']}%")
    elif choice == "2":
        try:
            days = int(input("Number of days (1-7): "))
            result = client.execute_action("weather", "get_forecast", {"city": city, "days": days})
            if result.get("success"):
                print(f"\nForecast for {result['city']}:")
                for day in result['forecast']:
                    print(f"  Day {day['day']}: {day['condition']}, "
                          f"High: {day['temperature_high']}°C, Low: {day['temperature_low']}°C")
        except ValueError:
            print("\nInvalid number of days!")


def file_menu(client):
    """File operations submenu."""
    print("\nFile Operations:")
    print("1. Write File")
    print("2. Read File")
    print("3. List Files")
    print("4. Check File Exists")
    print("5. Delete File")
    
    choice = input("\nSelect operation (1-5): ").strip()
    
    if choice == "1":
        filename = input("Enter filename: ").strip()
        content = input("Enter content: ").strip()
        result = client.execute_action("file", "write", {"filename": filename, "content": content})
        if result.get("success"):
            print(f"\n{result['message']}")
        else:
            print(f"\nError: {result.get('error')}")
    
    elif choice == "2":
        filename = input("Enter filename: ").strip()
        result = client.execute_action("file", "read", {"filename": filename})
        if result.get("success"):
            print(f"\nContent: {result['content']}")
        else:
            print(f"\nError: {result.get('error')}")
    
    elif choice == "3":
        result = client.execute_action("file", "list", {})
        if result.get("success"):
            print(f"\nFiles ({result['count']}): {', '.join(result['files']) if result['files'] else 'none'}")
    
    elif choice == "4":
        filename = input("Enter filename: ").strip()
        result = client.execute_action("file", "exists", {"filename": filename})
        if result.get("success"):
            print(f"\nFile exists: {result['exists']}")
    
    elif choice == "5":
        filename = input("Enter filename: ").strip()
        result = client.execute_action("file", "delete", {"filename": filename})
        if result.get("success"):
            print(f"\n{result['message']}")
        else:
            print(f"\nError: {result.get('error')}")


def main():
    """Run the interactive demo."""
    # Create and configure server
    server = MCPServer()
    server.register_agent(CalculatorAgent())
    server.register_agent(WeatherAgent())
    server.register_agent(FileAgent())
    
    # Create client
    client = MCPClient(server)
    
    print("\nWelcome to MCP Demo!")
    print("Server initialized with 3 agents: calculator, weather, file")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "0":
            print("\nGoodbye!")
            break
        elif choice == "1":
            agents = client.list_agents()
            print("\nAvailable Agents:")
            for agent in agents:
                print(f"\n  {agent['name']}: {agent['description']}")
                print(f"  Capabilities: {', '.join(agent['capabilities'])}")
        elif choice == "2":
            calculator_menu(client)
        elif choice == "3":
            weather_menu(client)
        elif choice == "4":
            file_menu(client)
        elif choice == "5":
            info = client.get_server_info()
            print(f"\nServer: {info['server']}")
            print(f"Version: {info['version']}")
            print(f"Agents: {', '.join(info['agents'])}")
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
