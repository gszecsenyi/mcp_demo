"""
MCP Client - Interacts with the MCP server.
"""
from typing import Any, Dict, List
from ..server.mcp_server import MCPServer


class MCPClient:
    """Client for interacting with MCP Server."""
    
    def __init__(self, server: MCPServer):
        """
        Initialize the MCP client.
        
        Args:
            server: MCP Server instance
        """
        self.server = server
    
    def list_agents(self) -> List[Dict[str, Any]]:
        """
        List all available agents.
        
        Returns:
            List of agent information
        """
        return self.server.list_agents()
    
    def get_agent_info(self, agent_name: str) -> Dict[str, Any]:
        """
        Get information about a specific agent.
        
        Args:
            agent_name: Name of the agent
            
        Returns:
            Agent information or error
        """
        agent = self.server.get_agent(agent_name)
        if agent:
            return agent.get_info()
        return {"error": f"Agent not found: {agent_name}"}
    
    def execute_action(self, agent_name: str, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an action on an agent.
        
        Args:
            agent_name: Name of the agent
            action: Action to execute
            params: Parameters for the action
            
        Returns:
            Result of the action
        """
        return self.server.execute(agent_name, action, params)
    
    def get_server_info(self) -> Dict[str, Any]:
        """
        Get server information.
        
        Returns:
            Server information
        """
        return self.server.get_server_info()
