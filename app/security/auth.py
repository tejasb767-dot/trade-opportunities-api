from fastapi import Header, HTTPException
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This allows keeping secrets like API keys outside source code
load_dotenv()

# Read API key from environment variable
# Never hardcode secrets in production applications
API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(None)):

    # API key is expected in request header: x-api-key
    # Using header-based auth for simple API protection
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )