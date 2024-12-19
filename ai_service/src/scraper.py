import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

BACKEND_URL = "http://localhost:3000" #backend url

def get_scraping_url():
    """Ambil URL target dari backend."""
    try:
        response = requests.get(f"{BACKEND_URL}/get-url")
        if response.status_code == 200:
            return response.json().get("url", "")
        else:
            return None
    except Exception as e:
        print(f"Error fetching scraping URL: {e}")
        return None
def scrape_reviews(num_pages=5):
    """Scrape ulasan dari URL target."""
    url = get_scraping_url()
    if not url:
        print("URL scraping belum diatur dari backend.")
        return[]
        
    reviews = []
    for page in rang(1, num_pages + 1):
        response = requests.get(f"{url}?page={page}")
        if response.status_code != 200:
            printe(f"failed to retrieve page {page}")
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        for review in soup.find_all("div", class_="review"):
            text = review.find("p", class_="content").text.strip()
            rating = int(review.find("span", class_="rating").text.strip())
            reviews.append({
                "text": text,
                "rating": rating
            })
        return reviews

if __name__ == "__main__":
    data = scrapte_reviews()
    if data:
        df = pd.DataFrame(data)
        df.to_csv("data/scraped_data.csv", index=False)
        print("Data berhasil disimpan ke 'data/scraped_data.csv'.")
    else:
        print("Tidak ada data untuk disimpan.")