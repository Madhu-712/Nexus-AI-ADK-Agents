from google.adk.agents import Agent

from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

from google.adk.tools.langchain_tool import LangchainTool
from .thirdpartytool import langchain_wikipedia_tool

from .custom_agents import google_search_agent

from .bank_custom_functions import get_BIN_bankinfo, get_SWIFT_bankinfo, get_interest_rate,get_LIBOR_rate

root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions.',
      tools=[
         FunctionTool(get_BIN_bankinfo), 
         FunctionTool(get_SWIFT_bankinfo),
         FunctionTool(get_interest_rate),
         FunctionTool(get_LIBOR_rate),
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ]
)