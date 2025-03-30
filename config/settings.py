import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if running locally)
load_dotenv()

SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")

IDMC_AUTH_URL = os.getenv("IDMC_AUTH_URL")
IDMC_CLIENT_ID = os.getenv("IDMC_CLIENT_ID")
IDMC_CLIENT_SECRET = os.getenv("IDMC_CLIENT_SECRET")
IDMC_USERNAME = os.getenv("IDMC_USERNAME")
IDMC_PASSWORD = os.getenv("IDMC_PASSWORD")
IDMC_BASE_URL = os.getenv("IDMC_BASE_URL")