import requests
import time
import os
import logging
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)

# Ensure the w3 directory exists
os.makedirs("w3", exist_ok=True)

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def sanitize_filename(url):
    """
    Sanitizes the URL to create a safe filename.

    Args:
        url (str): The URL to sanitize.

    Returns:
        str: A sanitized filename.
    """
    return url.replace("https://", "").replace("/", "_").replace(":", "_")

def scrape_and_summarize(url):
    """
    Scrapes the specified URL, summarizes its content, and collects internal links.

    Args:
        url (str): The URL to scrape.

    Returns:
        dict: Dictionary containing the summary and internal links.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        logging.info(f"Successfully fetched content from {url}")

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        internal_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/')]

        # Log extracted text and links for debugging
        logging.info(f"Extracted text from {url}: {text[:500]}...")  # Log first 500 chars
        logging.info(f"Found {len(internal_links)} internal links on {url}")

        # Use GPT-4 to summarize the content
        response = client.chat.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Summarize the following content:\n\n{text[:5000]}"}
            ],
            max_tokens=150
        )

        # Handle the response correctly
        summary = response.choices[0].message['content']
        logging.info(f"Generated summary for {url}")

        return {
            "summary": summary,
            "internal_links": internal_links
        }
    except Exception as e:
        logging.error(f"Error processing {url}: {e}")
        return {
            "summary": "",
            "internal_links": []
        }

def update_knowledge_base(urls):
    """
    Scrapes the specified URLs, summarizes their content, and collects internal links.

    Args:
        urls (list): List of URLs to scrape.

    Returns:
        dict: Dictionary containing the URL as the key and the scraped text as the value.
    """
    knowledge_base = {}
    for url in urls:
        data = scrape_and_summarize(url)
        summary = data["summary"]
        internal_links = data["internal_links"]

        # Save the summary to a file in the w3 folder
        file_name = os.path.join("w3", sanitize_filename(url) + "_summary.txt")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(summary)

        # Save the internal links to a file in the w3 folder
        links_file_name = os.path.join("w3", sanitize_filename(url) + "_links.txt")
        with open(links_file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(internal_links))

        knowledge_base[url] = summary
        logging.info(f"Updated knowledge base for {url}")

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

