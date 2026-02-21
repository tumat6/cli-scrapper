from src.modules.fetcher import fetch_data
from src.modules.parser import get_soup
from src.modules.extractor import extract_data
from src.modules.logger import get_logger
from urllib.parse import urljoin

logger = get_logger(__name__)


def navigation(soup):
    navigator = soup.find('li', class_='next')

    if navigator is not None:
        next_link = navigator.a['href']
        return next_link
    else:
        return None
    
def resolve_url(base_url, relative_link):
    new_link = urljoin(base_url, relative_link)
    if new_link == base_url:
        return None
    return new_link

def crawl_all(start_url):
    current_url = start_url
    all_products = []
    page_counter = 1

    logger.info("Crawler started", extra={"start_url": start_url})

    while page_counter < 50:
        logger.info("Crawling page", extra={"page": page_counter, "url": current_url})
        html = fetch_data(current_url)
        soup = get_soup(html)

        products = extract_data(soup)
        ref_next_page = navigation(soup)
        next_page = resolve_url(current_url, ref_next_page)

        for p in products:
            all_products.append(p)

        logger.debug(
            "Page crawled",
            extra={"page": page_counter, "products_on_page": len(products)},
        )

        if next_page is None:
            logger.info(
                "No next page found, crawler finished",
                extra={"last_page": page_counter, "total_products": len(all_products)},
            )
            break

        current_url = next_page
        page_counter += 1

    if page_counter >= 50:
        logger.warning("Crawler hit max page limit", extra={"max_pages": 50})

    logger.info("Crawler completed", extra={"total_products": len(all_products)})
    return all_products

