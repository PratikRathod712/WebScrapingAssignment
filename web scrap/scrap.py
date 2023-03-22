import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Create empty lists to store data
product_urls = []
product_names = []
product_prices = []
product_reviews = []
product_descriptions = []
product_asins = []
product_descriptions = []
product_manufacturers = []

# Set the number of pages to scrape
num_pages = 20
flag = 0
# Loop through each page
for page in range(1, num_pages+1):
    # Construct the URL for the page
    url = f"https://www.amazon.in/s?k=bags&page={page}&qid=1653308124&ref=sr_pg_{page}"

    # Send a GET request to the URL and get the HTML content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the products on the page
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    # Loop through each product
    for product in products:
        # Get the product URL, name, price, rating, and number of reviews
        product_url = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal'})['href']
        product_name = product.find('span', {'class': 'a-size-medium'}).text.strip()
        product_price = product.find('span', {'class': 'a-offscreen'}).text.strip()
        product_review = product.find('span', {'class': 'a-size-base'}).text.strip()

        # Add the data to the corresponding lists
        product_urls.append(product_url)
        product_names.append(product_name)
        product_prices.append(product_price)
        product_reviews.append(product_review)
        # flag +=1
        # print("Working part 1,  Iteration number: {}".format(flag) )
        
        # Wait for 1 second before making the next request to avoid overloading the server
        time.sleep(1)
    # flag+=1
    # print("Page: {}".format(flag) )
print("Ready")
dict = {'product_urls':product_urls,'product_names':product_names,'product_prices':product_prices,'product_reviews':product_reviews }
print(dict)
df = pd.DataFrame(dict)
df.to_csv("data.csv")
print("Done")