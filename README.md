---
title: Bedtime Storyteller AI Agent
emoji: 🌙
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: main.py
pinned: false
---

# Bedtime Storyteller AI Agent

An AI agent built using OpenAI's Agent SDK that creates personalized bedtime stories with a beautiful Gradio web interface.

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

## How It Works

The system uses a multi-agent architecture:

1. **Story Generators**: Three specialized agents create different types of bedtime stories:
   - **Funny Agent**: Creates humorous, engaging stories
   - **Wise Agent**: Generates moral stories from Buddhist/Jataka philosophy
   - **Historical Agent**: Tells child-friendly historical tales

2. **Story Picker**: A master agent that:
   - Uses all three storytellers as tools
   - Generates three different stories
   - Evaluates and selects the single best story
   - Returns only the final selected story

3. **Web Interface**: Gradio provides a simple button-click interface to generate stories

5. **Run the web interface:**
```bash
python main.py
```
This will launch a Gradio web interface in your browser.

## Project Structure

- `main.py` - Main entry point with Gradio web interface
- `agent/` - Core agent implementation
- `tools/` - Custom tools for the agent
- `config/` - Configuration and settings
- `.env` - Environment variables (API keys, etc.)
- `venv/` - Virtual environment (created during setup)

## Features

- **Three AI Agents**: Funny, Wise, and Historical storytellers
- **Smart Story Selection**: AI-powered story picker that evaluates and selects the best story
- **Web Interface**: Beautiful Gradio UI for easy interaction
- **Multi-style Stories**: Different storytelling approaches for variety
- **Agent Tools**: Each storyteller is available as a tool for the story picker

## Dependencies

- **openai**: OpenAI API client for AI interactions
- **openai-agents**: OpenAI Agent SDK for multi-agent orchestration
- **gradio**: Web interface framework for easy interaction
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation and settings management

## Troubleshooting

### Common Issues

1. **Import Error: No module named 'agents'**
   - Make sure you've installed all dependencies: `pip install -r requirements.txt`
   - Verify you're in the correct virtual environment

2. **OpenAI API Key Error**
   - Check that your `.env` file contains a valid `OPENAI_API_KEY`
   - Ensure the API key has sufficient credits

3. **Gradio Launch Issues**
   - Make sure port 7860 is available (default Gradio port)
   - Check firewall settings if running on a remote server

### Getting Help

If you encounter issues:
1. Run `python test_agent.py` to verify your setup
2. Check that all dependencies are installed correctly
3. Verify your OpenAI API key is valid and has credits

## Deactivating the Virtual Environment

When you're done working on the project:
```bash
deactivate
```
