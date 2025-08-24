#!/usr/bin/env python3
"""
Dependency installation and verification script
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"   ✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ {description} failed: {e}")
        print(f"   Error output: {e.stderr}")
        return False

def main():
    """Main installation function"""
    print("🚀 Installing Bedtime Storyteller AI Agent Dependencies")
    print("=" * 60)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: You're not in a virtual environment!")
        print("   It's recommended to create one first:")
        print("   python -m venv venv")
        print("   venv\\Scripts\\activate  # Windows")
        print("   source venv/bin/activate  # Unix/Mac")
        print()
    
    # Install dependencies
    print("📦 Installing Python dependencies...")
    
    # Upgrade pip first
    if not run_command("python -m pip install --upgrade pip", "Upgrading pip"):
        print("❌ Failed to upgrade pip. Please check your Python installation.")
        return False
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        print("❌ Failed to install requirements. Please check the error above.")
        return False
    
    # Test imports
    print("\n🧪 Testing imports...")
    
    try:
        import openai
        print("   ✅ openai package imported successfully")
    except ImportError as e:
        print(f"   ❌ openai package import failed: {e}")
        return False
    
    try:
        from openai.agents import Agent
        print("   ✅ openai.agents imported successfully")
    except ImportError as e:
        print(f"   ❌ openai.agents import failed: {e}")
        return False
    
    try:
        import dotenv
        print("   ✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"   ❌ python-dotenv import failed: {e}")
        return False
    
    print("\n🎉 All dependencies installed and verified successfully!")
    print("\nNext steps:")
    print("1. Create a .env file with your OpenAI API key")
    print("2. Run: python test_agent.py")
    print("3. Run: python main.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Installation failed. Please check the errors above.")
        sys.exit(1)
