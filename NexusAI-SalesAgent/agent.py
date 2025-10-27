from google.adk.agents import Agent

from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

from .custom_agents import google_search_agent

from .sales_custom_functions import get_SalesTAXinfo,get_VATinfo,get_commodityprice

from google.adk.tools.langchain_tool import LangchainTool
from .thirdpartytool import langchain_wikipedia_tool



root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions.',
      tools=[
         FunctionTool(get_SalesTAXinfo), 
         FunctionTool(get_VATinfo),
         FunctionTool(get_commodityprice),
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ]
)