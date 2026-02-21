from src.modules.logger import get_logger

logger = get_logger(__name__)


def extract_data(soup):
    product_list = []

    # Extract all the products on the page
    products = soup.find_all('article', class_='product_pod')
    logger.debug("Extracting products", extra={"products_found": len(products)})

    for product in products:
        # Extract the product name
        name = product.h3.a['title']

        # Extract the product price
        price = product.find('p', class_='price_color').text

        # Extract the product rating
        rating = product.p['class'][1]

        # Transform the rating from words to numbers
        rating_dict = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }

        # Store the extracted data in a dictionary
        product_list.append({
            'name': name,
            'price': price,
            'rating': rating_dict[rating]
        })

    logger.debug("Extraction finished", extra={"products_extracted": len(product_list)})
    return product_list
