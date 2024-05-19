import requests
import time
from bs4 import BeautifulSoup4

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
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        knowledge_base[url] = soup.get_text()
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
        print("Knowledge base updated.")
        time.sleep(interval)

# Example usage
urls = ['https://example.com/programming', 'https://example.com/frameworks']
interval = 3600  # Update every hour
real_time_update(interval, urls)
