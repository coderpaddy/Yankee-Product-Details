# Yankee Fragrances


# Install
 ```python
 git clone https://github.com/coderpaddy/Yankee-Product-Details
 cd Yankee-Product-Details
 # You may want to create a virtual environment
 # python3 -m venv env
 pip3 install -r requirements.txt
```

# Usage
 - Use as standalone package

 ```python
 # /scrape.py

 # Enter Product Urls
 product_list = [
    "https://www.yankeecandle.com/product/honey-clementine/_/R-47064",
    # etc...
 ]

 python scrape.py
 ```
 
 - Use in own script

 ```python
 from product_get import get_product
 from requests_html import HTMLSession

 # Create session
 session = HTMLSession()
 
 # Get product
 product_data = get_product(session, url)
 # Can use same session over and over
 ```