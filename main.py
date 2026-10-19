import urllib.request
import re

# The URL of the page to scrape
# This example targets a Wikipedia page on web scraping, fitting the article's topic.
URL = "https://en.wikipedia.org/wiki/Web_scraping"

def scrape_and_parse_wikipedia_page(url):
    """
    Fetches a Wikipedia page and extracts its title and the first paragraph
    using only Python's standard library (urllib.request and re).
    """
    try:
        # Step 1: Document Scraping - Fetch the HTML content from the URL
        # urllib.request is used to open and read URLs, acting as the 'scraper'.
        print(f"Attempting to scrape: {url}")
        with urllib.request.urlopen(url) as response:
            # Read the content and decode it to a UTF-8 string
            html_content = response.read().decode('utf-8')
        print("Successfully scraped HTML content.\n")

        # Step 2: Parsing - Extract the page title using regular expressions
        # Regular expressions (re) are used here for basic parsing of the HTML string.
        # This regex looks for content within <title>...</title> tags.
        title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE | re.DOTALL)
        page_title = title_match.group(1).strip() if title_match else "Title not found"
        print(f"Extracted Page Title: {page_title}\n")

        # Step 3: Parsing - Extract the text of the first main paragraph
        # This regex attempts to find the content of the first <p> tag.
        # Note: Regex is generally not robust for complex HTML parsing due to nested tags.
        paragraph_match = re.search(r"<p>(.*?)</p>", html_content, re.IGNORECASE | re.DOTALL)
        if paragraph_match:
            first_paragraph_raw = paragraph_match.group(1)
            # Remove any remaining HTML tags within the paragraph content
            first_paragraph_text = re.sub(r"<[^>]*>", "", first_paragraph_raw).strip()
            print(f"Extracted First Paragraph:\n{first_paragraph_text}\n")
        else:
            print("First paragraph not found.\n")

    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scrape_and_parse_wikipedia_page(URL)
