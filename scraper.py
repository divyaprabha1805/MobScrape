from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse, urlunparse, parse_qs

# URL for searching "mobile phones" on Amazon
URL = "https://www.amazon.in/s?k=mobile+phones&ref=nb_sb_noss_2"

# Setting up Selenium WebDriver options to run in headless mode (no UI)
options = Options()
options.add_argument("--headless")

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the first page
driver.get(URL)

# Set to store already seen product URLs (to avoid duplicates)
seen_urls = set()

# Product count
product_count = 0

# Function to clean URLs by removing query parameters
def clean_url(url):
    parsed_url = urlparse(url)
    cleaned_url = urlunparse(parsed_url._replace(query=''))  # Remove the query parameters
    return cleaned_url

# Loop through multiple pages
while True:
    # Find all the product links on the current page
    links = driver.find_elements(By.CLASS_NAME, "a-link-normal")
    
    # Loop through all the links found on the page
    for i, link in enumerate(links):
        product_url = link.get_attribute("href")
        
        if product_url and "dp/" in product_url:  # Filter valid product links
            # Clean the URL to remove query parameters
            cleaned_url = clean_url(product_url)

            # Avoid processing the same URL multiple times
            if cleaned_url in seen_urls:
                continue
            seen_urls.add(cleaned_url)

            product_count += 1
            print(f"Product {product_count} Link:", product_url)

            # Now, we will request the product page and parse it using BeautifulSoup
            product_page = requests.get(product_url)
            product_soup = BeautifulSoup(product_page.content, "html.parser")

            # Get the product title
            title = product_soup.find("span", attrs={"id": 'productTitle'})
            if title:
                print("Product Title:", title.text.strip())

            # Get the product price
            price = product_soup.find("span", attrs={"class": "a-price-whole"})
            if price:
                print("Product Price:", price.text.strip())

            # Get the product rating
            rating = product_soup.find("span", attrs={"class": "a-icon-alt"})
            if rating:
                print("Product Rating:", rating.text.strip())

            print("-" * 40)  # Separator for better readability

    # Find and click the "Next" button to go to the next page
    try:
        next_button = driver.find_element(By.XPATH, "//a[@class='s-pagination-next']")
        if next_button:
            next_button.click()
            time.sleep(3)  # Wait for the next page to load
        else:
            break  # No more pages, exit the loop
    except Exception as e:
        print("No more pages or error:", e)
        break  # No more pages or error occurred, exit the loop

# Close the Selenium WebDriver
driver.quit()
