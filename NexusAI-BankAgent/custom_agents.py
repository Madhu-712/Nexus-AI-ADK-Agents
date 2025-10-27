from google.adk.agents.llm_agent import Agent




from google.adk.agents import Agent
from google.adk.tools import google_search


# Create an agent with google search tool as a search specialist
google_search_agent = Agent(
    model='gemini-2.5-flash',
    name='google_search_agent',
    instruction='Use google search to answer user questions about real-time, logistical information related to banking and finance.',
    tools=[google_search],
)

