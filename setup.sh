#!/bin/bash

echo "Setting up Bedtime Storyteller AI Agent..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment"
    exit 1
fi

echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo
echo "Setup complete!"
echo
echo "To activate the virtual environment in the future, run:"
echo "  source venv/bin/activate"
echo
echo "To run the agent:"
echo "  python main.py"
echo
echo "To deactivate the virtual environment:"
echo "  deactivate"
echo
