"""
Weather agent - provides simulated weather information.
"""
import random
from typing import Any, Dict, List
from .base import BaseAgent


class WeatherAgent(BaseAgent):
    """Agent that provides simulated weather information."""
    
    def __init__(self):
        super().__init__(
            name="weather",
            description="Provides simulated weather information for cities"
        )
        self.weather_conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Foggy"]
    
    def get_capabilities(self) -> List[str]:
        """Return list of weather capabilities."""
        return ["get_weather", "get_forecast"]
    
    def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a weather operation.
        
        Args:
            action: Operation to perform (get_weather, get_forecast)
            params: Dictionary with 'city' parameter
            
        Returns:
            Result dictionary with weather information
        """
        city = params.get("city", "Unknown")
        
        if action == "get_weather":
            return self._get_current_weather(city)
        elif action == "get_forecast":
            days = params.get("days", 3)
            return self._get_forecast(city, days)
        else:
            return {"success": False, "error": f"Unknown action: {action}"}
    
    def _get_current_weather(self, city: str) -> Dict[str, Any]:
        """Get simulated current weather."""
        temperature = random.randint(-10, 35)
        condition = random.choice(self.weather_conditions)
        humidity = random.randint(30, 90)
        
        return {
            "success": True,
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "humidity": humidity,
            "unit": "celsius"
        }
    
    def _get_forecast(self, city: str, days: int) -> Dict[str, Any]:
        """Get simulated weather forecast."""
        forecast = []
        for i in range(min(days, 7)):  # Max 7 days
            day_forecast = {
                "day": i + 1,
                "temperature_high": random.randint(15, 35),
                "temperature_low": random.randint(-5, 15),
                "condition": random.choice(self.weather_conditions)
            }
            forecast.append(day_forecast)
        
        return {
            "success": True,
            "city": city,
            "forecast": forecast,
            "unit": "celsius"
        }
