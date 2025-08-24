#!/usr/bin/env python3
"""
Main entry point for the Bedtime Storyteller AI Agent
"""

import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool
from config.settings import config
import gradio as gr


"""Main function to run the AI agent"""
# Load environment variables
load_dotenv(override=True)

instructions_funny = "You are a bedtime story teller for kids powered by AI. \
    You tell funny bedtime stories to kids."

instructions_wise = "You are a bedtime story teller for kids powered by AI. \
    You tell wise bedtime stories to kids more from Buddhist philosophy or Jataka tales. \
    You do not include any violence, explicit, scary stories."

instructions_history = "You are a bedtime story teller for kids powered by AI. \
    You act like a history teacher and tell stories from history."

# Create agents with proper OpenAI Agent SDK syntax
agent_funny = Agent(
    name="Funny Bedtime Storyteller",
    instructions=instructions_funny,
    model=config.openai_model,
    tools=[]  # We'll add tools later
)

agent_wise = Agent(
    name="Wise Bedtime Storyteller", 
    instructions=instructions_wise,
    model=config.openai_model,
    tools=[]
)

agent_historian = Agent(
    name="Historical Bedtime Storyteller",
    instructions=instructions_history,
    model=config.openai_model,
    tools=[]
)    

story_picker = Agent(
    name="Best bedtime story picker",
    instructions="You are the best judge to pick a bedtime story using all agent tools. \
        Follow these steps carefully: \
        1. Generate stories: Use all three agent_ tools to generate three different bedtime stories. Do not proceed until \
                all three drafts are ready. \
        2. Evaluate and select: Review the three stories and choose the single best bedtime story using your judgment. \
        3. Output: Finally output the best story you picked. DO NOT show all three stories or explanation for your selection. \
        Crucial Rules: \
            - You must use the tools to generate the stories. Do not generate them yourself. \
            - You must pick ONE complete story from the tools - never more than one. \
            - You must OUTPUT the final selection story. Not the explanations for picking or summary of three stories. ",
    model=config.openai_model,
    tools=[]
)

message = "Tell a bedtime story"

tool_wise = agent_wise.as_tool(tool_name="agent_wise", tool_description = message)
tool_funny = agent_funny.as_tool(tool_name="agent_funny", tool_description = message)
tool_historian = agent_historian.as_tool(tool_name="agent_historian", tool_description = message)

tools = [tool_wise, tool_funny, tool_historian]

story_picker.tools = tools 

async def run_story():
    with trace("Story picker"):
        result = await Runner.run(story_picker, "The best bedtime story")
        print("Best pick:\n")
        return result.final_output
        
def get_story():
    return asyncio.run(run_story())

with gr.Blocks() as demo:
    gr.Markdown("# Kid's Bedtime Story Teller")
    btn = gr.Button("Generate Story")
    out = gr.Textbox(label="Your Story", lines=50)

    btn.click(fn=get_story, inputs=None, outputs=out)

if __name__ == "__main__":
    demo.launch()