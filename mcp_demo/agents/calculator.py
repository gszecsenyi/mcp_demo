"""
Calculator agent - performs basic arithmetic operations.
"""
from typing import Any, Dict, List
from .base import BaseAgent


class CalculatorAgent(BaseAgent):
    """Agent that performs basic calculator operations."""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs basic arithmetic operations (add, subtract, multiply, divide)"
        )
    
    def get_capabilities(self) -> List[str]:
        """Return list of calculator capabilities."""
        return ["add", "subtract", "multiply", "divide"]
    
    def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a calculator operation.
        
        Args:
            action: Operation to perform (add, subtract, multiply, divide)
            params: Dictionary with 'a' and 'b' values
            
        Returns:
            Result dictionary with 'result' key
        """
        try:
            a = float(params.get("a", 0))
            b = float(params.get("b", 0))
            
            if action == "add":
                result = a + b
            elif action == "subtract":
                result = a - b
            elif action == "multiply":
                result = a * b
            elif action == "divide":
                if b == 0:
                    return {"success": False, "error": "Division by zero"}
                result = a / b
            else:
                return {"success": False, "error": f"Unknown action: {action}"}
            
            return {"success": True, "result": result}
        except (ValueError, KeyError) as e:
            return {"success": False, "error": str(e)}
