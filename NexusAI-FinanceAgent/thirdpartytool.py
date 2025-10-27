
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Configure the Wikipedia LangChain tool to act as our cultural guide
langchain_wikipedia_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=3000)
)

# Give the tool a more specific description for our agent
langchain_wikipedia_tool.description = (
    "Provides answer to user queries related to Company finance,stocks,mutualfund,mortgage and latest NAV ,historical trends,Mutualfund suggestions ,risk management/tolerance,exit loads,AUM,expense ratio")


