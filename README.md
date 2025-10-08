# MCP Demo - Model Context Protocol Demonstration

A simple and educational implementation of a Model Context Protocol (MCP) environment with multiple intelligent agents.

## Overview

This project demonstrates a basic MCP architecture where a server manages multiple agents, each with specific capabilities. Clients can interact with these agents through the server to perform various tasks.

## Features

- **MCP Server**: Central server that manages and coordinates agents
- **Multiple Agents**:
  - **Calculator Agent**: Performs basic arithmetic operations
  - **Weather Agent**: Provides simulated weather information
  - **File Agent**: Handles basic file operations
- **MCP Client**: Simple client interface for interacting with agents
- **Extensible Architecture**: Easy to add new agents with custom capabilities

## Project Structure

```
mcp_demo/
├── mcp_demo/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py          # Base agent class
│   │   ├── calculator.py    # Calculator agent
│   │   ├── weather.py       # Weather agent
│   │   └── file.py          # File operations agent
│   ├── server/
│   │   ├── __init__.py
│   │   └── mcp_server.py    # MCP server implementation
│   └── client/
│       ├── __init__.py
│       └── mcp_client.py    # MCP client implementation
├── examples/
│   └── basic_example.py     # Example usage script
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

### Prerequisites

- Python 3.7 or higher

### Install from source

```bash
# Clone the repository
git clone https://github.com/gszecsenyi/mcp_demo.git
cd mcp_demo

# Install in development mode
pip install -e .

# Or install with dev dependencies
pip install -e ".[dev]"
```

## Quick Start

### Running the Basic Example

```bash
python examples/basic_example.py
```

This will demonstrate:
- Server initialization
- Agent registration
- Calculator operations (addition, multiplication, division)
- Weather information retrieval
- File operations (write, read, list, check existence)

### Using in Your Code

```python
from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.client.mcp_client import MCPClient
from mcp_demo.agents.calculator import CalculatorAgent
from mcp_demo.agents.weather import WeatherAgent

# Create and configure server
server = MCPServer()
server.register_agent(CalculatorAgent())
server.register_agent(WeatherAgent())

# Create client
client = MCPClient(server)

# Use calculator
result = client.execute_action("calculator", "add", {"a": 10, "b": 5})
print(f"Result: {result['result']}")  # Output: 15

# Get weather
weather = client.execute_action("weather", "get_weather", {"city": "Paris"})
print(f"Temperature: {weather['temperature']}°C")
```

## Agent Capabilities

### Calculator Agent

**Capabilities**: `add`, `subtract`, `multiply`, `divide`

```python
# Addition
client.execute_action("calculator", "add", {"a": 10, "b": 5})

# Subtraction
client.execute_action("calculator", "subtract", {"a": 10, "b": 5})

# Multiplication
client.execute_action("calculator", "multiply", {"a": 10, "b": 5})

# Division
client.execute_action("calculator", "divide", {"a": 10, "b": 5})
```

### Weather Agent

**Capabilities**: `get_weather`, `get_forecast`

```python
# Get current weather
client.execute_action("weather", "get_weather", {"city": "London"})

# Get forecast
client.execute_action("weather", "get_forecast", {"city": "London", "days": 3})
```

### File Agent

**Capabilities**: `read`, `write`, `list`, `delete`, `exists`

```python
# Write file
client.execute_action("file", "write", {
    "filename": "test.txt",
    "content": "Hello World!"
})

# Read file
client.execute_action("file", "read", {"filename": "test.txt"})

# List files
client.execute_action("file", "list", {})

# Check if file exists
client.execute_action("file", "exists", {"filename": "test.txt"})

# Delete file
client.execute_action("file", "delete", {"filename": "test.txt"})
```

## Creating Custom Agents

To create a new agent, inherit from `BaseAgent`:

```python
from mcp_demo.agents.base import BaseAgent
from typing import Any, Dict, List

class MyCustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="my_agent",
            description="My custom agent description"
        )
    
    def get_capabilities(self) -> List[str]:
        return ["action1", "action2"]
    
    def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if action == "action1":
            # Implement action1
            return {"success": True, "result": "action1 result"}
        elif action == "action2":
            # Implement action2
            return {"success": True, "result": "action2 result"}
        else:
            return {"success": False, "error": f"Unknown action: {action}"}

# Register with server
server.register_agent(MyCustomAgent())
```

## Development

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests (when available)
pytest
```

## Architecture

The MCP Demo follows a simple client-server architecture:

1. **Server Layer** (`MCPServer`): Manages agent lifecycle and routes requests
2. **Agent Layer** (`BaseAgent` and implementations): Provides specific capabilities
3. **Client Layer** (`MCPClient`): Provides interface for interacting with the server

### Communication Flow

```
Client → Server → Agent → Server → Client
```

1. Client sends request to server
2. Server validates and routes to appropriate agent
3. Agent processes request and returns result
4. Server forwards result back to client

## License

MIT License - feel free to use this project for learning and development.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Future Enhancements

- [ ] Add REST API interface
- [ ] Implement async/await support
- [ ] Add authentication and authorization
- [ ] Create web-based UI
- [ ] Add more agent types (database, API, etc.)
- [ ] Implement agent-to-agent communication
- [ ] Add logging and monitoring capabilities