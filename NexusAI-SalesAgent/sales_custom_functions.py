

import requests
import os # Recommended: to securely access your API key


def get_commodityprice(commodity:str):
    """
    The Commodity Price API provides access to real-time commodity prices for dozens of 
    commonly-traded commodities in major exchanges (CME, NYMEX, etc.).
    Args:
            commodity:Commodity name.
    Returns:
            The Commodity information as a json response
                or None if Commodity could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/commodityprice"
    api_url = f"{base_url}?commodity={commodity}"
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






def get_VATinfo(country:str,amount:int):
    """
    The VAT API provides current and historical Value Added Tax (VAT) rates for all countries in the European Union.
    Args:
         Country:Two-letter country code (ISO 3166-1 alpha-2).
         amount:Purchase amount.
    Returns:
        The VAT information as a json response
        or None if VAT could not be fetched, or if an error occurred
    """
    base_url = "https://api.api-ninjas.com/v1/vat"
    api_url = f"{base_url}?country={country}&amount={amount}"
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


def get_SalesTAXinfo(zip_code:int,amount:int):
    """ 
     The Sales Tax Calculator API provides accurate and detailed sales tax calculations for any purchase amount in the United States,
     including tax breakdowns and total amounts.
    Args:
       zip_code:Valid US ZIP code.
       amount:Purchase amount.
        
    Returns:
       Calculates sales tax for a given amount and location. 
       Returns a detailed breakdown including state, county, city, and special district taxes, along with the calculated tax amount and total amount after tax.
       or None if sales tax could not be fetched, or if an error occurred.

        
    """
    base_url = "https://api.api-ninjas.com/v1/salestaxcalculator"
    api_url = f"{base_url}?zip_code={zip_code}&amount={amount}"
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




