# MCP Demo Examples

This directory contains various examples demonstrating the MCP Demo functionality.

## Available Examples

### 1. Basic Example (`basic_example.py`)

A comprehensive walkthrough of all the basic features:
- Server initialization and agent registration
- Using the Calculator agent (add, multiply, divide)
- Getting weather information (current weather and forecasts)
- File operations (write, read, list, check existence)

**Run it:**
```bash
python examples/basic_example.py
```

### 2. Advanced Example (`advanced_example.py`)

Demonstrates error handling and advanced use cases:
- Error handling (division by zero, unknown agents, invalid parameters)
- Chained calculator operations
- Batch operations with multiple cities
- Batch file operations
- Agent introspection

**Run it:**
```bash
python examples/advanced_example.py
```

### 3. Interactive Example (`interactive_example.py`)

An interactive CLI that allows you to:
- Browse available agents
- Execute calculator operations interactively
- Query weather information
- Perform file operations
- View server information

**Run it:**
```bash
python examples/interactive_example.py
```

Then follow the on-screen menu to interact with the agents.

## Creating Your Own Examples

Here's a minimal example to get started:

```python
from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.client.mcp_client import MCPClient
from mcp_demo.agents.calculator import CalculatorAgent

# Create server and register agents
server = MCPServer()
server.register_agent(CalculatorAgent())

# Create client
client = MCPClient(server)

# Use the calculator
result = client.execute_action("calculator", "add", {"a": 10, "b": 5})
print(f"Result: {result['result']}")  # Output: 15.0
```

## Tips

- All examples can be run from the repository root
- Examples automatically add the parent directory to the Python path
- Check the main README.md for detailed API documentation
- Use the interactive example to explore agent capabilities
