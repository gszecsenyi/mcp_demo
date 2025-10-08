"""Tests for MCP Server."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mcp_demo.server.mcp_server import MCPServer
from mcp_demo.agents.calculator import CalculatorAgent
from mcp_demo.agents.weather import WeatherAgent


def test_server_register_agent():
    """Test registering an agent."""
    server = MCPServer()
    agent = CalculatorAgent()
    server.register_agent(agent)
    
    assert "calculator" in server.agents
    assert server.get_agent("calculator") == agent


def test_server_unregister_agent():
    """Test unregistering an agent."""
    server = MCPServer()
    agent = CalculatorAgent()
    server.register_agent(agent)
    
    result = server.unregister_agent("calculator")
    assert result is True
    assert "calculator" not in server.agents


def test_server_list_agents():
    """Test listing agents."""
    server = MCPServer()
    server.register_agent(CalculatorAgent())
    server.register_agent(WeatherAgent())
    
    agents = server.list_agents()
    assert len(agents) == 2
    assert any(a["name"] == "calculator" for a in agents)
    assert any(a["name"] == "weather" for a in agents)


def test_server_execute():
    """Test executing an action."""
    server = MCPServer()
    server.register_agent(CalculatorAgent())
    
    result = server.execute("calculator", "add", {"a": 5, "b": 3})
    assert result["success"] is True
    assert result["result"] == 8.0


def test_server_execute_unknown_agent():
    """Test executing on unknown agent."""
    server = MCPServer()
    result = server.execute("unknown", "add", {"a": 5, "b": 3})
    assert result["success"] is False
    assert "error" in result


def test_server_execute_unknown_action():
    """Test executing unknown action."""
    server = MCPServer()
    server.register_agent(CalculatorAgent())
    
    result = server.execute("calculator", "unknown_action", {})
    assert result["success"] is False
    assert "error" in result


def test_server_info():
    """Test getting server info."""
    server = MCPServer()
    server.register_agent(CalculatorAgent())
    
    info = server.get_server_info()
    assert "server" in info
    assert "version" in info
    assert info["agent_count"] == 1
    assert "calculator" in info["agents"]


if __name__ == "__main__":
    test_server_register_agent()
    test_server_unregister_agent()
    test_server_list_agents()
    test_server_execute()
    test_server_execute_unknown_agent()
    test_server_execute_unknown_action()
    test_server_info()
    print("All server tests passed!")
