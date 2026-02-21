import argparse

from src.modules.logger import get_logger

logger = get_logger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(description='A simple CLI tool to fetch data from a URL.')
    parser.add_argument('url', type=str, help='The URL to fetch data from')
    args = parser.parse_args()
    logger.debug("Parsed CLI arguments", extra={"url": args.url})
    return args.url

