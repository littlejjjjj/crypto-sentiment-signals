import requests
from bs4 import BeautifulSoup

CRYPTO_NEWS_RSS = [
    "https://cointelegraph.com/rss",
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
]

def fetch_crypto_news(limit=20):
    articles = []

    for feed in CRYPTO_NEWS_RSS:
        try:
            r = requests.get(feed, timeout=5)
            soup = BeautifulSoup(r.text, "xml")
            items = soup.find_all("item")

            for item in items[:limit]:
                articles.append({
                    "title": item.title.text,
                    "url": item.link.text,
                })
        except Exception:
            continue

    return articles
