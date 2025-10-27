






from .custom_agents import google_search_agent
from .company_custom_function import get_MarketCap,get_SECfilings,get_CompanysEarnings,get_spfindings500



from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.langchain_tool import LangchainTool
from .thirdpartytool import langchain_wikipedia_tool







root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions related to finance and general company information.',
       tools=[
         FunctionTool(get_MarketCap), 
         FunctionTool(get_SECfilings),
         LangchainTool(langchain_wikipedia_tool),
         FunctionTool(get_CompanysEarnings),
         FunctionTool(get_spfindings500),
         AgentTool(agent=google_search_agent),
        ]
)