import requests

from src.modules.logger import get_logger

logger = get_logger(__name__)


def fetch_data(url):
    logger.debug("Fetching URL", extra={"url": url})
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        logger.debug(
            "Fetched URL successfully",
            extra={"url": url, "status_code": response.status_code},
        )
        return response.text
    except requests.RequestException:
        logger.exception("Failed to fetch URL", extra={"url": url})
        raise

