from slowapi import Limiter
from slowapi.util import get_remote_address

# Global rate limiter instance
# Uses client IP address as key to limit requests per user
# Helps prevent API abuse and protects AI / external API usage
limiter = Limiter(key_func=get_remote_address)