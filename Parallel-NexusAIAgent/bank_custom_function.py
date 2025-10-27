

import requests
import os # Recommended: to securely access your API key

def get_BIN_bankinfo(bin: int):
    """
     Does the BIN Lookup to fetch bank information from Bank Identification Numbers (BIN).
     Our database contains hundreds of thousands of BINs worldwide.

     Args:
        bin: The BIN number.

     Returns:
        The Bank information as a json response
        or None if BIN could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/bin"
    api_url = f"{base_url}?bin={bin}"

    # --- IMPORTANT: How to get and use your API key ---
    # 1. Get your API key from api-ninjas.com
    # 2. Store it securely. The best practice is using environment variables.
    #    In your Cloud Shell, you can set it like this:
    #    export API_NINJAS_KEY="YOUR_ACTUAL_API_KEY_HERE"
    #
    #    Then, your Python code can access it:
    api_key = os.environ.get("API_NINJAS_KEY")

    # If you absolutely must hardcode it for a quick test (NOT recommended for production):
    # api_key = "YOUR_ACTUAL_API_KEY_HERE" # <--- Replace with your real API key!

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

# Example Usage (after setting your API_NINJAS_KEY environment variable):
# For example, if you want to look up BIN 411111
# bank_info = get_bankinfo(411111)
# if bank_info:
#     print(bank_info)
# else:
#     print("Could not retrieve bank information.")


def get_SWIFT_bankinfo(swift:str):
    """The SWIFT Code API allows you to find the SWIFT Code(s) for any bank in the world.
    Args:
        swift: The SWIFT Code.
    Returns:
        The Bank information as a json response
        or None if SWIFT Code could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/swiftcode"
    api_url = f"{base_url}?swift={swift}"
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

def get_interest_rate(rate:str):
    """The Interest Rate API provides current central bank interest rates for 22 countries.
    Args:
        rate: The interest rate.
    Returns:
        The Bank information as a json response
        or None if interest rate could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/interestrate"
    api_url = f"{base_url}?rate={rate}"
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

def get_LIBOR_rate():
    """The LIBOR API provides current and historical LIBOR (London Interbank Offered Rate) data for all tenors from 
    overnight to 12 months. LIBOR is a key benchmark interest rate at which major global banks lend to one another.
    Args:
        None
    Returns:
        The LIBOR information as a json response
        or None if LIBOR could not be fetched, or if an error occurred.
    """
    base_url = "https://api.api-ninjas.com/v1/libor"
    api_url = f"{base_url}"
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



