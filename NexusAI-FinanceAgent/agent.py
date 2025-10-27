


from google.adk.agents import Agent

from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

from .custom_agents import google_search_agent

from .finance_custom_function import mortgageinfo,stock_exchangeinfo,stockprice,mutualfundinfo,exchangerateinfo




from google.adk.tools.langchain_tool import LangchainTool
from .thirdpartytool import langchain_wikipedia_tool



root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions.',
      tools=[
         FunctionTool(mortgageinfo), 
         FunctionTool(stock_exchangeinfo),
         FunctionTool(stockprice),
         FunctionTool(mutualfundinfo),
         FunctionTool(exchangerateinfo),

         
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ]
)
