from bs4 import BeautifulSoup

def get_soup(html_content):
    return BeautifulSoup(html_content, 'html.parser')

