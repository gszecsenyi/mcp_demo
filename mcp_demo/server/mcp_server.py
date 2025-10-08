"""
MCP Server - Manages agents and handles requests.
"""
from typing import Any, Dict, List, Optional
from ..agents.base import BaseAgent


class MCPServer:
    """Model Context Protocol Server that manages multiple agents."""
    
    def __init__(self):
        """Initialize the MCP server."""
        self.agents: Dict[str, BaseAgent] = {}
    
    def register_agent(self, agent: BaseAgent) -> None:
        """
        Register an agent with the server.
        
        Args:
            agent: Agent instance to register
        """
        self.agents[agent.name] = agent
        print(f"Registered agent: {agent.name}")
    
    def unregister_agent(self, agent_name: str) -> bool:
        """
        Unregister an agent from the server.
        
        Args:
            agent_name: Name of the agent to unregister
            
        Returns:
            True if successful, False otherwise
        """
        if agent_name in self.agents:
            del self.agents[agent_name]
            print(f"Unregistered agent: {agent_name}")
            return True
        return False
    
    def list_agents(self) -> List[Dict[str, Any]]:
        """
        List all registered agents.
        
        Returns:
            List of agent information dictionaries
        """
        return [agent.get_info() for agent in self.agents.values()]
    
    def get_agent(self, agent_name: str) -> Optional[BaseAgent]:
        """
        Get an agent by name.
        
        Args:
            agent_name: Name of the agent
            
        Returns:
            Agent instance or None if not found
        """
        return self.agents.get(agent_name)
    
    def execute(self, agent_name: str, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an action on a specific agent.
        
        Args:
            agent_name: Name of the agent
            action: Action to execute
            params: Parameters for the action
            
        Returns:
            Result dictionary
        """
        agent = self.get_agent(agent_name)
        if not agent:
            return {"success": False, "error": f"Agent not found: {agent_name}"}
        
        if action not in agent.get_capabilities():
            return {
                "success": False,
                "error": f"Agent '{agent_name}' does not support action '{action}'"
            }
        
        return agent.execute(action, params)
    
    def get_server_info(self) -> Dict[str, Any]:
        """
        Get server information.
        
        Returns:
            Dictionary with server info
        """
        return {
            "server": "MCP Demo Server",
            "version": "0.1.0",
            "agent_count": len(self.agents),
            "agents": [agent.name for agent in self.agents.values()]
        }
