from src.modules.cli import parse_arguments
from src.modules.fetcher import fetch_data
from src.modules.extractor import extract_data
from src.modules.parser import get_soup

def run_pipeline(url):

    html = fetch_data(url)
    soup = get_soup(html)
    data = extract_data(soup)
    return data

if __name__ == "__main__":
    url = "https://books.toscrape.com"
    products = run_pipeline(url)

    for p in products:
        print(p)
