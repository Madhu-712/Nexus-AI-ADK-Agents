
import os
import requests




def get_MarketCap(ticker:str):   
    """
    The Market Cap API provides access to real-time market cap data for companies in all major exchanges.
    Args:
        Ticker:Company ticker symbol.
    Returns:
        The Market Cap information as a json response
        or None if Market Cap could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/marketcap"
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

def get_SECfilings(ticker:str,filing:str):
    """
    The SEC API allows you to search millions of SEC filings from thousands of public companies.
    Args:
        Ticker:Company ticker symbol.
        Filing:Filing type.
    Returns:
        The SEC filings information as a json response
        or None if SEC filings could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/secfilings"
    api_url = f"{base_url}?ticker={ticker}&filing={filing}"
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

def get_CompanysEarnings(ticker:str,year:int,quarter:int):
    """
    The Earnings API provides comprehensive earnings report data for any public company listed in the United States, 
    including financial statements, balance sheets, cash flow statements, and key financial metrics. 
    All data is sourced from official SEC filings (10-Q, 10-K).
    Args:
        Ticker:Company ticker symbol.
        Year:Year.
        Quarter:Quarter.
    Returns:
        The Company Earnings information as a json response
        or None if Company Earnings could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/earnings"
    api_url = f"{base_url}?ticker={ticker}&year={year}&quarter={quarter}"
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

def get_spfindings500(ticker:str):
    """
    The S&P 500 API provides information about companies in the S&P 500 index,
    including ticker, name, sector, and the date the company was added to the index.
    Args:
        Ticker:Company ticker symbol.
    Returns:
        The S&P 500 information as a json response
        or None if S&P 500 could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/s&pfindings500"
    api_url = f"{base_url}?ticker={ticker}"
    api_key = os.environ.get("API_NINJAS_KEY")
    
    if not api_key:
        # Handle the case where the API key is missing

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




    


        





        







