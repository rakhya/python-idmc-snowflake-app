import requests
import time
from config.settings import (
    IDMC_AUTH_URL, IDMC_CLIENT_ID, IDMC_CLIENT_SECRET,
    IDMC_USERNAME, IDMC_PASSWORD, IDMC_BASE_URL
)

# Global variables for caching the token
_cached_token = None
_token_expiry = 0  # Epoch timestamp for expiration


def get_idmc_token():
    """
    Fetch IDMC API access token using client credentials if expired or not set.
    """
    global _cached_token, _token_expiry

    # Check if token is still valid
    if _cached_token and time.time() < _token_expiry:
        return _cached_token  # Return cached token if not expired

    try:
        payload = {
            "grant_type": "password",
            "client_id": IDMC_CLIENT_ID,
            "client_secret": IDMC_CLIENT_SECRET,
            "username": IDMC_USERNAME,
            "password": IDMC_PASSWORD
        }

        response = requests.post(IDMC_AUTH_URL, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response.raise_for_status()  # Raise an error for HTTP errors

        token_data = response.json()
        _cached_token = token_data.get("access_token")
        expires_in = token_data.get("expires_in", 3600)  # Default to 1 hour if not provided

        # Set expiry time (current time + expires_in seconds)
        _token_expiry = time.time() + expires_in - 60  # Refresh 1 min before actual expiry

        return _cached_token
    except requests.RequestException as e:
        print(f"Error fetching IDMC token: {e}")
        return None


def fetch_idmc_data():
    """
    Fetch data from IDMC API using a cached access token.
    """
    token = get_idmc_token()
    if not token:
        return None

    try:
        url = f"{IDMC_BASE_URL}/api/v2/data"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from IDMC: {e}")
        return None
