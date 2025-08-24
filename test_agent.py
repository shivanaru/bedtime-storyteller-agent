#!/usr/bin/env python3
"""
Simple test script to verify the agent setup
"""

import asyncio
import os
from dotenv import load_dotenv

async def test_setup():
    """Test the basic setup without running the full agent"""
    print("🧪 Testing Bedtime Storyteller AI Agent Setup...")
    print("=" * 50)
    
    # Test 1: Environment loading
    print("1. Testing environment loading...")
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("   ✅ OPENAI_API_KEY found")
    else:
        print("   ❌ OPENAI_API_KEY not found")
        print("   Please create a .env file with your OpenAI API key")
        return False
    
    # Test 2: Configuration loading
    print("2. Testing configuration loading...")
    try:
        from config.settings import config
        print(f"   ✅ Configuration loaded successfully")
        print(f"   Agent: {config.agent_name}")
        print(f"   Model: {config.openai_model}")
    except Exception as e:
        print(f"   ❌ Configuration error: {e}")
        return False
    
    # Test 3: OpenAI Agent SDK import
    print("3. Testing OpenAI Agent SDK import...")
    try:
        from openai.agents import Agent
        print("   ✅ OpenAI Agent SDK imported successfully")
    except Exception as e:
        print(f"   ❌ OpenAI Agent SDK import error: {e}")
        return False
    
    # Test 4: Agent creation
    print("4. Testing agent creation...")
    try:
        test_agent = Agent(
            name="Test Agent",
            instructions="You are a test agent",
            model=config.openai_model,
            tools=[]
        )
        print(f"   ✅ Test agent created successfully: {test_agent.name}")
    except Exception as e:
        print(f"   ❌ Agent creation error: {e}")
        return False
    
    print("\n🎉 All tests passed! The OpenAI Agent SDK is ready to use.")
    print("\nTo test the agents, run: python main.py")
    return True

if __name__ == "__main__":
    success = asyncio.run(test_setup())
    if not success:
        print("\n❌ Setup test failed. Please check the errors above.")
        exit(1)
