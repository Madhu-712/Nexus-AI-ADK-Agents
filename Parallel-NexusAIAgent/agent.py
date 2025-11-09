from google.adk.tools import google_search
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent

from google.adk.tools.langchain_tool import LangchainTool
from .thirdpartytool import langchain_wikipedia_tool
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

from .custom_agents import google_search_agent

from .bank_custom_function import get_BIN_bankinfo, get_SWIFT_bankinfo, get_interest_rate,get_LIBOR_rate
from .company_custom_function import get_MarketCap,get_SECfilings,get_CompanysEarnings,get_spfindings500
from .finance_custom_function import mortgageinfo,stock_exchangeinfo,stockprice,mutualfundinfo,exchangerateinfo
from .sales_custom_function import get_commodityprice,get_VATinfo,get_SalesTAXinfo

#from google.adk.agent import AgentBuilder




load_dotenv()

# Specialist Agent 1

BankAgent=LlmAgent(
    name="BankAgent",
    model="gemini-2.5-flash",
    tools=[
         FunctionTool(get_BIN_bankinfo), 
         FunctionTool(get_SWIFT_bankinfo),
         FunctionTool(get_interest_rate),
         FunctionTool(get_LIBOR_rate),
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ],
    instruction="You are specialist Bank Agent who can give info about Bank BIN,SWIFT,interest rate,LIBOR rate",
    output_key="bank_result"
)

#Specialist Agent 2
CompanyinfoAgent=LlmAgent(
    name="CompanyinfoAgent",
    model="gemini-2.5-flash",
    tools=[
          
         FunctionTool(get_SECfilings),
         LangchainTool(langchain_wikipedia_tool),
         FunctionTool(get_CompanysEarnings),
         FunctionTool(get_MarketCap),
         FunctionTool(get_spfindings500),
         AgentTool(agent=google_search_agent),
        ],
    instruction="You are specialist Company info agent who can give general companyinfo ,Market cap, SEC filings,earnings,spfindings500",
    output_key="companyinfo_result"

)

# Specialist Agent 3

SalesAgent=LlmAgent(
    name="SalesAgent",
    model="gemini-2.5-flash",
    tools=[
         FunctionTool(get_SalesTAXinfo),
         FunctionTool(get_VATinfo),
         FunctionTool(get_commodityprice),
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ],
    instruction="You are specialist Sales agent who can give info about sales tax,VAT,Commodity price",
    output_key="sales_result"
)

# Specialist Agent 4
FinanceAgent=LlmAgent(
    name="FinanceAgent",
    model="gemini-2.5-flash",
    tools=[
         FunctionTool(mortgageinfo), 
         FunctionTool(stock_exchangeinfo),
         FunctionTool(stockprice),
         FunctionTool(mutualfundinfo),
         FunctionTool(exchangerateinfo),
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ],
    instruction="You are specialist Finance agent who can give info about mortgage,stock exchange,stock price,exchange rate and mutual fund advice  to investors",
    output_key="finance_result"
)
#Specialist Agent 5
MutualfundAgent=LlmAgent(
    name="MutualfundAgent",
    model="gemini-2.5-flash",
    tools=[
         FunctionTool( mutualfund_by_ticker),
         FunctionTool(mutualfund_by_type),
         FunctionTool(mutualfund_by_name),
         LangchainTool(langchain_wikipedia_tool),
         AgentTool(agent=google_search_agent),
        ],
    instruction="You are specialist mutualfund agent who can give info about  mutual fund advice  to investors by type, by name and by ticker",
    output_key="mutualfund_result"
)



# ✨ The ParallelAgent runs all three specialists at once ✨
parallel_research_agent=ParallelAgent(
    name="parallel_research_agent",
    sub_agents=[CompanyinfoAgent,SalesAgent,FinanceAgent,BankAgent,MutualfundAgent],

)

# Agent to synthesize the parallel results
synthesis_agent=LlmAgent(
    name="synthesis_agent", model="gemini-2.5-flash",
    input_keys=["companyinfo_result", "finance_result", "bank_result", "sales_result","mutualfund_result"],
    instruction="""You are a helpful assistant. Combine the following research results into a clear, bulleted list for the user.
    - Companyinfo: {companyinfo_result}
    - Finance: {finance_result}
    - Bank: {bank_result}
    - Sales: {sales_result}
    - Mutualfund : {mutualfund_result} """

)


# ✨ The SequentialAgent runs the parallel search, then the synthesis ✨
sequential_pipeline_agent=SequentialAgent(
    name="Parallel-NexusAIAgent",
    sub_agents=[parallel_research_agent, synthesis_agent],
    description="A workflow that finds multiple things in parallel and then summarizes the results."
)


root_agent = Agent(
   model='gemini-2.5-flash',
   name='sequential_pipeline_agent',
   description='A helpful assistant for user questions.Act as a Agent team supercharged with a ParallelAgent workflow!'
      
)

root_agent = sequential_pipeline_agent
