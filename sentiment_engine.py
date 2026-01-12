from models.sentiment_model import SentimentModel
from sources.news import fetch_crypto_news

SYMBOLS = ["BTC", "ETH", "SOL", "USDT", "BNB"]

def classify_signal(score: float) -> str:
    if score > 0.6: return "STRONG BUY"
    if score > 0.2: return "BUY"
    if score >= -0.2: return "NEUTRAL"
    if score >= -0.6: return "SELL"
    return "STRONG SELL"

class SentimentEngine:
    def __init__(self):
        self.model = SentimentModel()

    def map_symbol(self, text: str):
        text = text.upper()
        for sym in SYMBOLS:
            if sym in text:
                return sym
        return "GENERAL"

    def analyze(self):
        raw = fetch_crypto_news()
        data = []

        for item in raw:
            title = item["title"]
            url = item["url"]
            score = self.model.score(title)
            symbol = self.map_symbol(title)
            signal = classify_signal(score)

            data.append({
                "symbol": symbol,
                "title": title,
                "url": url,
                "score": round(score, 3),
                "signal": signal,
            })

        return data
