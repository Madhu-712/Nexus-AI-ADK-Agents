import os
import requests
import json
import logging 


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)
from google.adk.tools import google_search

def mutualfund_by_ticker(ticker:str):
    """
    The Mutual Fund API provides detailed information about Mutual Funds including their holdings, expense ratios, assets under management, and other key metrics.
    Args:
        ticker:Company ticker symbol.
    Returns:
        Returns the Mutual Fund information for a given ticker symbol as a json response
        or None if Mutual Fund could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/mutualfund"
    api_url = f"{base_url}?ticker={ticker}"
    api_key = os.environ.get("API_NINJAS_KEY")
    if not api_key:
       print("Error: API_NINJAS_KEY environment variable not set or API key is missing.")
       return None
        # Construct the headers with your API key
    headers = {
        "X-Api-Key": api_key
    }
    try:
        
        response = requests.get(api_url, headers=headers)

        # Check for a successful HTTP status code (200 OK)
        if response.status_code == 200:
            return response.json()
        else:
            # Print error details for debugging
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return None # Return None on non-200 status codes
    except requests.exceptions.RequestException as e:
        # Catch any request-related exceptions (e.g., network issues, timeouts)
        print(f"An error occurred during the API request: {e}")
        return None 


def mutualfund_by_type(fund_type: str) -> dict: # 'tools' parameter is no longer needed
    """
    Retrieves general information about mutual funds of a specific type
    (e.g., Equity, Debt, Hybrid, Index, Money Market Funds)
    by using the built-in 'google_search' tool from google.adk.tools.

    Args:
        fund_type: The type of mutual fund to search for (e.g., "Equity", "Debt").

    Returns:
        A dictionary containing the search results summary and list latest Top 10 performing funds in that category, or an error message if the search fails.
    """
    if not fund_type:
        logger.error("Mutual fund type cannot be empty.")
        return {"error": "fund_type parameter is required."}

    # The google_search tool is directly imported and available
    search_tool_executor = google_search

    standardized_type = fund_type.strip().lower()

    # Optimized search queries for common fund types
    search_query_phrases = {
        "equity": "overview of equity mutual funds explained",
        "debt": "characteristics of debt mutual funds explained",
        "hybrid": "what are hybrid mutual funds explained",
        "index": "understanding index mutual funds explained",
        "moneymarketfunds": "explanation of money market funds",
        "money market": "explanation of money market funds"
    }

    # Construct the search query
    search_query = search_query_phrases.get(standardized_type, f"mutual fund type: {fund_type} explained")

    logger.info(f"Using google_search tool to find info for type: '{fund_type}' with query: '{search_query}'")

    try:
        # Execute the Google Search tool.
        # The ADK's google_search is expected to return a JSON string.
        search_results_str = search_tool_executor(query=search_query)

        # Parse the JSON string from the tool's output
        search_data = json.loads(search_results_str)

        # Construct a concise and helpful response
        return {
            "fund_type_query": fund_type,
            "search_query_used": search_query,
            "summary_from_search": search_data.get("summary", "No summary available from search results."),
            "top_links": [link.get("url") for link in search_data.get("links", [])[:3]], # Get top 3 links
            "full_search_response_summary": search_data # Include full response for debugging/details if needed
        }

    except json.JSONDecodeError as e:
        logger.error(f"Could not decode JSON from google_search tool response: {e}")
        # Log a snippet of the raw response for debugging
        logger.error(f"Raw response snippet: {search_results_str[:500]}...")
        return {"error": f"Invalid JSON response from google_search tool: {e}. Check ADK tool's output format."}
    except Exception as e:
        logger.exception(f"An unexpected error occurred while using the ADK's google_search tool: {e}")
        return {"error": f"An unexpected error occurred during search: {e}"}




def mutualfund_by_name(fund_name: str) -> dict:
    """
    Retrieves general information about a mutual fund by its name
    using the built-in 'google_search' tool from google.adk.tools.

    Args:
        fund_name: The full or partial name of the mutual fund
                   (e.g., "Vanguard 500 Index Fund Admiral Shares").

    Returns:
        A dictionary containing the search results summary for the fund which includes NAV,fund performance,Trailing returns,AUM,exit load,expense ratio,holdings,lock-in period,expense ratio and important considerations and tips while investing.
        or an error message if the search fails.
    """
    if not fund_name:
        logger.error("Mutual fund name cannot be empty.")
        return {"error": "fund_name parameter is required."}

    # The google_search tool is directly imported and available
    search_tool_executor = google_search

    # Construct the search query
    # We want general information, so a direct query is appropriate.
    search_query = f"mutual fund information {fund_name}"

    logger.info(f"Using google_search tool to find info for fund name: '{fund_name}' with query: '{search_query}'")

    try:
        # Execute the Google Search tool.
        # The ADK's google_search is expected to return a JSON string.
        search_results_str = search_tool_executor(query=search_query)

        # Parse the JSON string from the tool's output
        search_data = json.loads(search_results_str)

        # Construct a concise and helpful response, similar to mutualfund_by_type
        return {
            "fund_name_query": fund_name,
            "search_query_used": search_query,
            "summary_from_search": search_data.get("summary", "No summary available from search results."),
            "top_links": [link.get("url") for link in search_data.get("links", [])[:3]], # Get top 3 links
            "full_search_response_summary": search_data # Include full response for debugging/details if needed
        }

    except json.JSONDecodeError as e:
        logger.error(f"Could not decode JSON from google_search tool response: {e}")
        # Log a snippet of the raw response for debugging
        logger.error(f"Raw response snippet: {search_results_str[:500]}...")
        return {"error": f"Invalid JSON response from google_search tool: {e}. Check ADK tool's output format."}
    except Exception as e:
        logger.exception(f"An unexpected error occurred while using the ADK's google_search tool: {e}")
        return {"error": f"An unexpected error occurred during search: {e}"}



