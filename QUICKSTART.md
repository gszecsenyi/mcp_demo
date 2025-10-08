# Quick Start Guide

Get started with MCP Demo in 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/gszecsenyi/mcp_demo.git
cd mcp_demo

# Install (optional, for development)
pip install -e .
```

## Run Your First Example

```bash
python examples/basic_example.py
```

You should see output showing:
- ✅ Server initialization
- ✅ Agent registration
- ✅ Calculator operations
- ✅ Weather queries
- ✅ File operations

## Try the Interactive Mode

```bash
python examples/interactive_example.py
```

Follow the menu to:
1. List available agents
2. Perform calculations
3. Get weather information
4. Manage files

## Write Your First Code

Create a file `my_first_mcp.py`:

```python
from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.client.mcp_client import MCPClient
from mcp_demo.agents.calculator import CalculatorAgent

# Setup
server = MCPServer()
server.register_agent(CalculatorAgent())
client = MCPClient(server)

# Use it
result = client.execute_action("calculator", "add", {"a": 10, "b": 5})
print(f"10 + 5 = {result['result']}")
```

Run it:
```bash
python my_first_mcp.py
```

## Next Steps

1. **Explore Examples**: Check out `examples/advanced_example.py` for error handling
2. **Read Documentation**: See `README.md` for complete API reference
3. **Create Your Agent**: Follow the custom agent guide in `README.md`
4. **Run Tests**: Execute `python tests/test_calculator.py`

## Need Help?

- Check the main `README.md` for detailed documentation
- Look at example scripts in the `examples/` directory
- Review the implementation in `mcp_demo/` directory

Happy coding! 🚀
