from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from .mfcustomfunctions import mutualfund_by_ticker,mutualfund_by_type,mutualfund_by_name

from .custom_agents import google_search_agent


root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions.',
      tools=[
        FunctionTool(mutualfund_by_ticker),
        FunctionTool(mutualfund_by_type),
        FunctionTool(mutualfund_by_name),
        AgentTool(agent=google_search_agent),
    ]
)
