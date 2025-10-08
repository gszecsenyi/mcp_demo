"""
Base agent class for MCP demo.
All agents inherit from this base class.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseAgent(ABC):
    """Base class for all MCP agents."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize the base agent.
        
        Args:
            name: Name of the agent
            description: Description of what the agent does
        """
        self.name = name
        self.description = description
    
    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Return list of capabilities this agent provides.
        
        Returns:
            List of capability names
        """
        pass
    
    @abstractmethod
    def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an action with given parameters.
        
        Args:
            action: Action to execute
            params: Parameters for the action
            
        Returns:
            Result of the action
        """
        pass
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get agent information.
        
        Returns:
            Dictionary with agent info
        """
        return {
            "name": self.name,
            "description": self.description,
            "capabilities": self.get_capabilities()
        }
