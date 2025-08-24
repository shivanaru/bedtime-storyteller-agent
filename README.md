# Bedtime Storyteller AI Agent

An AI agent built using OpenAI's API that creates personalized bedtime stories in multiple styles.

## Setup

1. **Create and activate a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies:**
```bash
# Option 1: Automatic installation (recommended)
python install_deps.py

# Option 2: Manual installation
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp env.example .env
# Edit .env with your OpenAI API key
```

4. **Test the setup (optional but recommended):**
```bash
python test_agent.py
```

5. **Run the agent:**
```bash
python main.py
```

## Project Structure

- `main.py` - Main entry point for the agent
- `agent/` - Core agent implementation
- `tools/` - Custom tools for the agent
- `config/` - Configuration and settings
- `.env` - Environment variables (API keys, etc.)
- `venv/` - Virtual environment (created during setup)

## Deactivating the Virtual Environment

When you're done working on the project:
```bash
deactivate
```
