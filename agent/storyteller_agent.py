#!/usr/bin/env python3
"""
Core implementation of the Bedtime Storyteller AI Agent
"""

import asyncio
import os
from typing import Optional, Dict, Any
from openai import OpenAI
from config.settings import config


class StorytellerAgent:
    """AI Agent that creates personalized bedtime stories"""
    
    def __init__(self):
        """Initialize the agent with OpenAI client and configuration"""
        self.client = OpenAI(api_key=config.openai_api_key)
        self.model = config.openai_model
        self.agent_name = config.agent_name
        self.agent_description = config.agent_description
        
        # Agent state
        self.is_running = False
        self.conversation_history = []
        
    async def start(self):
        """Start the agent and begin interaction loop"""
        self.is_running = True
        print(f"🌟 {self.agent_name} is ready!")
        print(f"📖 {self.agent_description}")
        print("\n" + "="*50)
        
        try:
            while self.is_running:
                await self.interaction_loop()
        except Exception as e:
            print(f"❌ Error in agent loop: {e}")
            self.is_running = False
    
    async def interaction_loop(self):
        """Main interaction loop for the agent"""
        try:
            # Get user input
            user_input = await self.get_user_input()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                self.is_running = False
                print("👋 Goodbye! Sweet dreams!")
                return
            
            # Process the input and generate response
            response = await self.process_input(user_input)
            
            # Display response
            print(f"\n🤖 {self.agent_name}: {response}\n")
            
            # Store in conversation history
            self.conversation_history.append({
                "user": user_input,
                "agent": response,
                "timestamp": asyncio.get_event_loop().time()
            })
            
        except KeyboardInterrupt:
            self.is_running = False
            print("\n👋 Agent stopped by user")
        except Exception as e:
            print(f"❌ Error processing input: {e}")
    
    async def get_user_input(self) -> str:
        """Get input from the user"""
        try:
            return input("👤 You: ").strip()
        except EOFError:
            return "quit"
    
    async def process_input(self, user_input: str) -> str:
        """Process user input and generate appropriate response"""
        # For now, we'll use a simple OpenAI completion
        # Later we'll integrate with the Agent SDK for more sophisticated behavior
        
        try:
            # Create a prompt for the bedtime story context
            prompt = f"""You are {self.agent_name}, {self.agent_description}.

User request: {user_input}

Please respond in a warm, engaging way that's appropriate for creating bedtime stories. 
If the user wants a story, ask for details like the child's age, interests, or preferred theme.
If they're just chatting, be friendly and encouraging.

Response:"""

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt}
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"I'm having trouble thinking right now. Could you try again? (Error: {str(e)})"
    
    def stop(self):
        """Stop the agent"""
        self.is_running = False
        print("🛑 Agent stopping...")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "name": self.agent_name,
            "is_running": self.is_running,
            "conversation_count": len(self.conversation_history),
            "model": self.model
        }
