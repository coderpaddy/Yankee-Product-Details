from requests_html import HTMLSession
from product_get import get_product

session = HTMLSession()

product_list = [
    "https://www.yankeecandle.com/product/honey-clementine/_/R-47064",
    "https://www.yankeecandle.com/product/lemon-lavender/_/R-47069"
]
product_dict = {}

for product in product_list:
    product_data = get_product(session, product)
    key = list(product_data.keys())[0]
    product_dict[key] = product_data[key]

print(product_dict)
