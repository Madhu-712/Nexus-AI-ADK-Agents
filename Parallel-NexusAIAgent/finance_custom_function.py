
import requests
import os

def mortgageinfo(loan_amount:int,interest_rate:int,duration_years:int):
    """
    The Mortgage Calculator API provides detailed mortgage and other home financing payment information. 
    It uses the standard mortgage calculation formulas to calculate interest and monthly/annual payments.
    Args:
        loan_amount:Loan amount.
        interest_rate:Interest rate.
        duration_years:Duration in years.
    Returns:
        Returns monthly payment, annual payment, and interest rate information based 
        on the given mortgage parameters as a json response
        or None if Mortgage could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/mortgage"
    api_url = f"{base_url}?loan_amount={loan_amount}&interest_rate={interest_rate}&duration_years={duration_years}"
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


def stock_exchangeinfo(mic:str):
    """
     The Stock Exchange API provides comprehensive information about over 100 markets around the world, 
     including trading hours, location details, and number of listings.
     Args:
         mic(Market Identifier Code)
     Returns:
         The Stock Exchange information as a json response
         or None if Stock Exchange could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/stockexchange"
    api_url = f"{base_url}?mic={mic}"
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


def stockprice(ticker:str):
    """
    The Stock Price API provides access to real-time and historical stock market prices for companies in every major exchange around the world.
    Args:
        ticker:Company ticker symbol.
    Returns:
        Returns the current price information for any given ticker symbol.The Stock Price information as a json response
        or None if Stock Price could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/stockprice"
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

def mutualfundinfo(ticker:str):
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

def exchangerateinfo(pair:str):
    """
    The Exchange Rate API provides exchange rates on global currencies. 
    Choose from hundreds of different currency pairs.
    Args:currencypair
    Returns:
        Returns the Exchange Rate information for a given currency pair as a json response
        or None if Exchange Rate could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/exchangerate"
    api_url = f"{base_url}?pair={pair}"
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
















