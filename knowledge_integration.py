import requests
import time
import os
import logging
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO)

# Ensure the w3 directory exists
os.makedirs("w3", exist_ok=True)

def sanitize_filename(url):
    """
    Sanitizes the URL to create a safe filename.

    Args:
        url (str): The URL to sanitize.

    Returns:
        str: A sanitized filename.
    """
    return url.replace("https://", "").replace("/", "_").replace(":", "_")

def update_knowledge_base(urls):
    """
    Scrapes the specified URLs and updates the knowledge base with the latest content.

    Args:
        urls (list): List of URLs to scrape.

    Returns:
        dict: Dictionary containing the URL as the key and the scraped text as the value.
    """
    knowledge_base = {}
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure we notice bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()[:1000]  # Limit the amount of data processed
            knowledge_base[url] = text

            # Save the content to a file in the w3 folder
            file_name = os.path.join("w3", sanitize_filename(url) + ".txt")
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(text)

            logging.info(f"Updated knowledge base for {url}")
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")

    return knowledge_base

def real_time_update(interval, urls):
    """
    Continuously updates the knowledge base at the specified interval.

    Args:
        interval (int): Time interval (in seconds) for updating the knowledge base.
        urls (list): List of URLs to scrape.
    """
    while True:
        knowledge_base = update_knowledge_base(urls)
        logging.info("Knowledge base updated.")
        time.sleep(interval)

# Example usage
urls = [
    'https://github.com/mastermindml/mastermind', 
    'https://github.com/pythaiml/automindx', 
    'https://github.com/Professor-Codephreak', 
    'https://github.com/augml/lwe-plugin-shell', 
    'https://github.com/augml/nicegui'
]
interval = 3600  # Update every hour
real_time_update(interval, urls)

