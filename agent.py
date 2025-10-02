from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv
import openai
import os

load_dotenv()

web_search_agent = Agent(
    name = "web search agent",
    role= "search the web page for information",
    model = Groq(id="qwen/qwen3-32b"),
    tools = [DuckDuckGo()],
    instructions = ['Always give references'],
    show_tools_calls = True,
    markdown = True
)

Wikipedia_agent = Agent(
    name = "Finance agent",
    role= "Give information related to given topic",
    model = Groq(id="qwen/qwen3-32b"),
    tools = [WikipediaTools()],
    instructions = ['Give answer in buttet points and give references'],
    show_tools_calls = True,
    markdown = True
)

multi_agent = Agent(
    team = [web_search_agent,Wikipedia_agent],
    instruction=['Always give references','Give answer in buttet points and give references'],
    model = Groq(id="qwen/qwen3-32b"),
    show_tools_calls = True,
    markdown = True
)

multi_agent.print_response("tell me about world war 2.")