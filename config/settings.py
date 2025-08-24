#!/usr/bin/env python3
"""
Configuration settings for the Bedtime Storyteller AI Agent
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AgentConfig:
    """Configuration class for the AI agent"""
    
    def __init__(self):
        """Initialize configuration from environment variables"""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        
        # Agent settings
        self.agent_name = os.getenv("AGENT_NAME", "BedtimeStoryteller")
        self.agent_description = os.getenv(
            "AGENT_DESCRIPTION", 
            "An AI agent that creates personalized bedtime stories for children"
        )
        
        # Story settings
        self.max_story_length = int(os.getenv("MAX_STORY_LENGTH", "1000"))
        self.default_theme = os.getenv("STORY_THEME", "adventure")
        
        # OpenAI settings
        self.max_tokens = int(os.getenv("MAX_TOKENS", "300"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        
        # Validation
        self._validate_config()
    
    def _validate_config(self):
        """Validate that required configuration is present"""
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY is required in environment variables")
        
        if not self.openai_model:
            raise ValueError("OPENAI_MODEL is required in environment variables")
    
    def get_openai_config(self) -> Dict[str, Any]:
        """Get OpenAI-specific configuration"""
        return {
            "api_key": self.openai_api_key,
            "model": self.openai_model,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
    
    def get_agent_config(self) -> Dict[str, Any]:
        """Get agent-specific configuration"""
        return {
            "name": self.agent_name,
            "description": self.agent_description,
            "max_story_length": self.max_story_length,
            "default_theme": self.default_theme
        }
    
    def __str__(self) -> str:
        """String representation of configuration"""
        return f"""Agent Configuration:
  Name: {self.agent_name}
  Model: {self.openai_model}
  Max Story Length: {self.max_story_length}
  Default Theme: {self.default_theme}
  Max Tokens: {self.max_tokens}
  Temperature: {self.temperature}"""


# Global configuration instance
config = AgentConfig()
