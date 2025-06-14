import requests
from bs4 import BeautifulSoup

def scrape_website(domain):
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text(separator=" ", strip=True)
        else:
            return f"Failed to fetch website: {response.status_code}"
    except Exception as e:
        return f"Error occurred: {str(e)}"
