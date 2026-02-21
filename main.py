from src.modules.cli import parse_arguments
from src.modules.crawler import crawl_all
from src.modules.logger import get_logger, setup_logging

logger = get_logger(__name__)


def run_pipeline(url):
    logger.info("Starting pipeline", extra={"url": url})
    pipeline = crawl_all(url)
    logger.info("Pipeline completed", extra={"items_count": len(pipeline)})
    return pipeline

if __name__ == "__main__":
    setup_logging()
    url = parse_arguments()
    run_pipeline(url)
    
