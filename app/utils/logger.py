import logging

# Global logging configuration
# INFO level is suitable for production APIs (avoid DEBUG in prod)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Named logger for this application
# Using named logger helps when multiple modules exist
logger = logging.getLogger("trade_api")