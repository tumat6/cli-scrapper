from bs4 import BeautifulSoup

from src.modules.logger import get_logger

logger = get_logger(__name__)


def get_soup(html_content):
    logger.debug("Parsing HTML content", extra={"content_length": len(html_content)})
    return BeautifulSoup(html_content, 'html.parser')

