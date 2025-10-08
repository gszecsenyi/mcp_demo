"""
File operations agent - performs basic file operations.
"""
import os
from typing import Any, Dict, List
from .base import BaseAgent


class FileAgent(BaseAgent):
    """Agent that performs basic file operations."""
    
    def __init__(self, base_dir: str = "/tmp/mcp_demo"):
        super().__init__(
            name="file",
            description="Performs basic file operations (read, write, list, delete)"
        )
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)
    
    def get_capabilities(self) -> List[str]:
        """Return list of file operation capabilities."""
        return ["read", "write", "list", "delete", "exists"]
    
    def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a file operation.
        
        Args:
            action: Operation to perform
            params: Dictionary with operation parameters
            
        Returns:
            Result dictionary
        """
        try:
            if action == "read":
                return self._read_file(params.get("filename"))
            elif action == "write":
                return self._write_file(params.get("filename"), params.get("content", ""))
            elif action == "list":
                return self._list_files()
            elif action == "delete":
                return self._delete_file(params.get("filename"))
            elif action == "exists":
                return self._file_exists(params.get("filename"))
            else:
                return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _get_safe_path(self, filename: str) -> str:
        """Get safe file path within base directory."""
        # Prevent directory traversal attacks
        safe_filename = os.path.basename(filename)
        return os.path.join(self.base_dir, safe_filename)
    
    def _read_file(self, filename: str) -> Dict[str, Any]:
        """Read a file."""
        if not filename:
            return {"success": False, "error": "Filename required"}
        
        filepath = self._get_safe_path(filename)
        if not os.path.exists(filepath):
            return {"success": False, "error": f"File not found: {filename}"}
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        return {"success": True, "filename": filename, "content": content}
    
    def _write_file(self, filename: str, content: str) -> Dict[str, Any]:
        """Write to a file."""
        if not filename:
            return {"success": False, "error": "Filename required"}
        
        filepath = self._get_safe_path(filename)
        with open(filepath, 'w') as f:
            f.write(content)
        
        return {"success": True, "filename": filename, "message": "File written successfully"}
    
    def _list_files(self) -> Dict[str, Any]:
        """List all files in the base directory."""
        files = [f for f in os.listdir(self.base_dir) if os.path.isfile(os.path.join(self.base_dir, f))]
        return {"success": True, "files": files, "count": len(files)}
    
    def _delete_file(self, filename: str) -> Dict[str, Any]:
        """Delete a file."""
        if not filename:
            return {"success": False, "error": "Filename required"}
        
        filepath = self._get_safe_path(filename)
        if not os.path.exists(filepath):
            return {"success": False, "error": f"File not found: {filename}"}
        
        os.remove(filepath)
        return {"success": True, "filename": filename, "message": "File deleted successfully"}
    
    def _file_exists(self, filename: str) -> Dict[str, Any]:
        """Check if a file exists."""
        if not filename:
            return {"success": False, "error": "Filename required"}
        
        filepath = self._get_safe_path(filename)
        exists = os.path.exists(filepath)
        return {"success": True, "filename": filename, "exists": exists}
