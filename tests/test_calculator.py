"""Tests for Calculator Agent."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mcp_demo.agents.calculator import CalculatorAgent


def test_calculator_add():
    """Test calculator addition."""
    agent = CalculatorAgent()
    result = agent.execute("add", {"a": 10, "b": 5})
    assert result["success"] is True
    assert result["result"] == 15.0


def test_calculator_subtract():
    """Test calculator subtraction."""
    agent = CalculatorAgent()
    result = agent.execute("subtract", {"a": 10, "b": 5})
    assert result["success"] is True
    assert result["result"] == 5.0


def test_calculator_multiply():
    """Test calculator multiplication."""
    agent = CalculatorAgent()
    result = agent.execute("multiply", {"a": 10, "b": 5})
    assert result["success"] is True
    assert result["result"] == 50.0


def test_calculator_divide():
    """Test calculator division."""
    agent = CalculatorAgent()
    result = agent.execute("divide", {"a": 10, "b": 5})
    assert result["success"] is True
    assert result["result"] == 2.0


def test_calculator_divide_by_zero():
    """Test calculator division by zero."""
    agent = CalculatorAgent()
    result = agent.execute("divide", {"a": 10, "b": 0})
    assert result["success"] is False
    assert "error" in result


def test_calculator_capabilities():
    """Test calculator capabilities."""
    agent = CalculatorAgent()
    capabilities = agent.get_capabilities()
    assert "add" in capabilities
    assert "subtract" in capabilities
    assert "multiply" in capabilities
    assert "divide" in capabilities


def test_calculator_info():
    """Test calculator info."""
    agent = CalculatorAgent()
    info = agent.get_info()
    assert info["name"] == "calculator"
    assert "description" in info
    assert "capabilities" in info


if __name__ == "__main__":
    test_calculator_add()
    test_calculator_subtract()
    test_calculator_multiply()
    test_calculator_divide()
    test_calculator_divide_by_zero()
    test_calculator_capabilities()
    test_calculator_info()
    print("All calculator tests passed!")
